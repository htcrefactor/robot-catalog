#!/usr/bin/env python3
"""Build research/disagreements.json — the cross-catalog disagreement view (issue #33).

For every record that carries `seen_on` (the competitor catalogs we know list it), open the
page we recorded, read the values that catalog publishes for that model, and compare them
with the values stored in data/parts/*.json.

This is a review aid for maintainers. A competitor value is evidence that a field deserves a
second look at the maker's own document; it is NEVER a value for data/parts or data/specs.
Nothing under data/ is written by this script.

Usage
  python3 scripts/build_disagreements.py                  # fetch what is missing, rebuild the JSON
  python3 scripts/build_disagreements.py --offline        # rebuild from the cache only
  python3 scripts/build_disagreements.py --catalog droid.monster
  python3 scripts/build_disagreements.py --fetch-only

Pages and API payloads are cached under .cache/disagreements/ (git-ignored), one file per URL,
so a rerun only fetches what is missing.
"""
import argparse, concurrent.futures, datetime, glob, hashlib, html as htmlmod, json, os, re, time
import urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, ".cache", "disagreements")
OUT = os.path.join(ROOT, "research", "disagreements.json")
UA = "robot-catalog-review/1.0 (maintainer review aid; +https://github.com/htcrefactor/robot-catalog)"

# ---------------------------------------------------------------- units
# unit -> (dimension, factor to the dimension's base unit)
U = {"mm": ("length", 1), "cm": ("length", 10), "m": ("length", 1000), "in": ("length", 25.4), "ft": ("length", 304.8),
     "g": ("mass", .001), "kg": ("mass", 1), "lb": ("mass", .45359237),
     "m/s": ("speed", 1), "km/h": ("speed", 1 / 3.6), "mph": ("speed", .44704),
     "s": ("time", 1 / 3600), "min": ("time", 1 / 60), "h": ("time", 1),
     "Wh": ("energy", 1), "kWh": ("energy", 1000)}
BASE = {"length": "mm", "mass": "kg", "speed": "m/s", "time": "h", "energy": "Wh"}
UNIT_ALIAS = {"lbs": "lb", "pound": "lb", "pounds": "lb", "kmh": "km/h", "kph": "km/h", "m/sec": "m/s",
              "hr": "h", "hrs": "h", "hour": "h", "hours": "h", "sec": "s", "secs": "s", "second": "s",
              "seconds": "s", "mins": "min", "minute": "min", "minutes": "min", "inch": "in", "inches": "in",
              "wh": "Wh", "kwh": "kWh", "mile/h": "mph"}
NUM = r"\d+(?:[.,]\d+)?"


def tonum(s):
    s = s.strip()
    return float(s.replace(",", "")) if re.fullmatch(r"\d{1,3}(?:,\d{3})+", s) else float(s.replace(",", "."))


def parse_num_unit(text, dim=None):
    """First figure in `text` with a unit, converted to the base unit of its dimension.
    A range ("160-180 cm", "55 to 75 kg") keeps lo and hi instead of a single value.
    Returns {"value", "lo", "hi", "unit", "dim"} or None. `dim` restricts to one dimension."""
    if text is None:
        return None
    s = htmlmod.unescape(str(text)).replace("\u00a0", " ").replace("~", " ").replace("≈", " ")
    rng = re.search(rf"(\d[\d.,]*)\s*(?:[-–—]|to)\s*(\d[\d.,]*)\s*([A-Za-z/]+)\.?", s)
    single = re.search(rf"(\d[\d.,]*)\s*([A-Za-z/]+)\.?", s)
    m = rng or single
    if not m:
        return None
    unit = m.group(3) if rng else m.group(2)
    key = UNIT_ALIAS.get(unit.lower(), unit if unit in U else None)
    if key is None:
        lk = unit.lower()
        key = next((k for k in U if k.lower() == lk), None)
    if key is None:
        return None
    d = U[key][0]
    if dim and d != dim:
        return None
    f = U[key][1] / U[BASE[d]][1]
    if rng:
        lo, hi = sorted((tonum(rng.group(1)), tonum(rng.group(2))))
        return {"value": None, "lo": lo * f, "hi": hi * f, "unit": unit, "dim": d}
    return {"value": tonum(m.group(1)) * f, "lo": None, "hi": None, "unit": unit, "dim": d}


# ---------------------------------------------------------------- our data
CORE = [("height_mm", "Height", "length"), ("width_mm", "Width", "length"), ("length_mm", "Length", "length"),
        ("weight_kg", "Weight", "mass"), ("payload_kg", "Payload", "mass"),
        ("max_speed_mps", "Max speed", "speed"), ("dof", "DoF", "count"), ("runtime_h", "Runtime", "time"),
        ("battery_wh", "Battery", "energy"), ("price_usd", "Price", "money"),
        ("ip_rating", "IP rating", "ip")]
LABEL = {f: lab for f, lab, _ in CORE}
DIM = {f: d for f, _, d in CORE}
TOL = {"length": 0.02, "mass": 0.03, "speed": 0.05, "time": 0.10, "energy": 0.05, "count": 0.0, "money": 0.15,
       "ip": 0.0, "year": 0.0}
FLOOR = {"length": 5, "mass": 0.5, "speed": 0.06, "time": 0.15, "energy": 20, "count": 0, "money": 50}


def load_ours():
    ours = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "data/parts/*.json"))):
        for r in json.load(open(f, encoding="utf-8")):
            ours[r["id"]] = r
    return ours


# ---------------------------------------------------------------- review signals from our own records
CONFLICT_WORDS = re.compile(r"conflict|disagree|differ|inconsisten|varies|varie[sd]|two values|"
                            r"mislabe|incorrect|wrong|typo|not maker-stated|aggregator", re.I)


def spec_dupes():
    """Keys stated more than once in data/specs/<id>.json with different values: the maker
    documents themselves disagree (or state two conditions). Not a competitor value."""
    A = {}
    ap = os.path.join(ROOT, "data/spec_key_aliases.json")
    if os.path.exists(ap):
        A = json.load(open(ap, encoding="utf-8"))
    out = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "data/specs/*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        groups = {}
        for row in d.get("specs") or []:
            k = A.get(row.get("key"), row.get("key"))
            groups.setdefault((k, row.get("label") or k), []).append(row)
        dups = []
        for (k, _label), rows in groups.items():
            seen = {(str(r.get("value")).strip(), str(r.get("unit") or "").strip()) for r in rows}
            if len(rows) > 1 and len(seen) > 1:
                dups.append({"key": k, "label": rows[0].get("label") or k,
                             "values": [{"value": r.get("value"), "unit": r.get("unit", ""),
                                         "note": r.get("note", ""), "source": r.get("source", "")} for r in rows]})
        if dups:
            out[d["id"]] = sorted(dups, key=lambda x: (x["key"], x["label"]))
    return out


# ---------------------------------------------------------------- fetch + cache
def cache_path(url):
    parts = urllib.parse.urlsplit(url)
    host = re.sub(r"[^a-z0-9.-]", "_", parts.netloc)
    name = re.sub(r"[^A-Za-z0-9._-]", "-", parts.path.strip("/"))[-80:] or "index"
    return os.path.join(CACHE, host, f"{name}-{hashlib.sha1(url.encode()).hexdigest()[:10]}.txt")


def fetch(url, offline=False, retries=3):
    p = cache_path(url)
    if os.path.exists(p) and os.path.getsize(p) > 0:
        return open(p, encoding="utf-8", errors="replace").read()
    if offline:
        return None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en"})
            with urllib.request.urlopen(req, timeout=30) as r:
                body = r.read().decode("utf-8", "replace")
            os.makedirs(os.path.dirname(p), exist_ok=True)
            open(p, "w", encoding="utf-8").write(body)
            return body
        except Exception:
            time.sleep(1 + attempt)
    return None


def fetch_many(urls, offline=False, workers=8, label=""):
    todo = [u for u in urls if not (os.path.exists(cache_path(u)) and os.path.getsize(cache_path(u)) > 0)]
    if offline or not todo:
        return
    print(f"  {label}: fetching {len(todo)} of {len(urls)} pages…", flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
        list(ex.map(lambda u: fetch(u), todo))


# ---------------------------------------------------------------- html helpers
def strip_tags(s):
    s = re.sub(r"<br\s*/?>", " ", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", htmlmod.unescape(s)).strip()


def tables(html):
    """[[cell text, …], …] for every table row on the page (script/style removed)."""
    html = re.sub(r"<(script|style).*?</\1>", " ", html, flags=re.S | re.I)
    out = []
    for t in re.findall(r"<table.*?</table>", html, re.S | re.I):
        for tr in re.findall(r"<tr.*?</tr>", t, re.S | re.I):
            cells = [strip_tags(c) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, re.S | re.I)]
            cells = [c for c in cells if c]
            if cells:
                out.append(cells)
    return out


# ---------------------------------------------------------------- adapters
# Each adapter returns {"url": page, "values": {our_field: {"value"|"text", "unit", "text", "source"}}}
# "value" is numeric in our field's unit; "text" is what the catalog printed.

def a_droid(url, ctx):
    """droid.monster publishes one JSON per model: /robots/<maker>/<model> -> api/v1/models/<maker>/<model>.json"""
    p = urllib.parse.urlsplit(url).path.strip("/").split("/")
    if len(p) < 3:
        return None
    body = fetch("https://api.droid.monster/v1/models/%s/%s.json" % (p[1], p[2]))
    if not body:
        return None
    d = json.loads(body)
    vals = {}
    for s in d.get("specs") or []:
        k, v, unit = s.get("key"), s.get("value"), s.get("unit")
        src = (s.get("source") or {}).get("url")
        pub = s.get("as_published") or {}
        text = f"{pub.get('value')} {pub.get('unit') or ''}".strip() if pub else (f"{v} {unit or ''}".strip())
        fld = {"mass_kg": "weight_kg", "payload_kg": "payload_kg", "height_mm": "height_mm",
               "width_mm": "width_mm", "length_mm": "length_mm", "max_speed_ms": "max_speed_mps",
               "dof": "dof", "runtime_s": "runtime_h", "battery_capacity_wh": "battery_wh"}.get(k)
        if fld and isinstance(v, (int, float)) and not isinstance(v, bool):
            val = v
            if k == "runtime_s":
                val = v / 3600.0
            vals.setdefault(fld, {"value": val, "unit": unit or "", "text": text, "source": src})
        if k == "ip_rating" and isinstance(v, str) and v.strip():
            vals.setdefault("ip_rating", {"text": v, "value": v, "unit": "", "source": src})
    for k, v in (d.get("commercial") or {}).items():
        if "price" in k and isinstance(v, (int, float)):
            vals.setdefault("price_usd", {"value": v, "unit": "USD", "text": str(v), "source": None})
    return {"url": url, "values": vals}


def a_buyl(url, ctx):
    """botupyourlife.com: /en/robots/<id>/ and the whole set at api/robots.json."""
    rid = urllib.parse.urlsplit(url).path.strip("/").split("/")[-1]
    rows = ctx["buyl"]
    r = rows.get(rid)
    if not r:
        return None
    vals = {}

    def add(fld, v, text, unit=""):
        if isinstance(v, (int, float)) and v:
            vals.setdefault(fld, {"value": v, "unit": unit, "text": text, "source": r.get("official_url")})

    add("height_mm", r.get("height_cm") and r["height_cm"] * 10, f"{r.get('height_cm')} cm", "cm")
    add("weight_kg", r.get("weight_kg"), f"{r.get('weight_kg')} kg", "kg")
    add("payload_kg", r.get("payload_kg"), f"{r.get('payload_kg')} kg", "kg")
    add("dof", r.get("dof_total"), f"{r.get('dof_total')} DoF")
    if r.get("max_speed_kmh"):
        add("max_speed_mps", r["max_speed_kmh"] / 3.6, f"{r['max_speed_kmh']} km/h", "km/h")
    add("runtime_h", r.get("runtime_h"), f"{r.get('runtime_h')} h", "h")
    if r.get("battery_kwh"):
        add("battery_wh", r["battery_kwh"] * 1000, f"{r['battery_kwh']} kWh", "kWh")
    if r.get("ip_rating"):
        vals.setdefault("ip_rating", {"value": r["ip_rating"], "text": r["ip_rating"], "unit": "", "source": r.get("official_url")})
    add("price_usd", r.get("price_usd_min"), f"${r.get('price_usd_min')}", "USD")
    return {"url": url, "values": vals}


def a_r2u(url, ctx):
    """data.robo2u.com: /robots/<slug> and the whole set at api/robots."""
    slug = urllib.parse.urlsplit(url).path.strip("/").split("/")[-1]
    r = ctx["r2u"].get(slug)
    if not r:
        return None
    vals = {}

    def add(fld, v, text, unit=""):
        if isinstance(v, (int, float)) and v:
            vals.setdefault(fld, {"value": v, "unit": unit, "text": text, "source": None})

    add("height_mm", r.get("height_cm") and r["height_cm"] * 10, f"{r.get('height_cm')} cm", "cm")
    add("weight_kg", r.get("weight_kg"), f"{r.get('weight_kg')} kg", "kg")
    add("payload_kg", r.get("payload_kg"), f"{r.get('payload_kg')} kg", "kg")
    add("dof", r.get("dof"), f"{r.get('dof')} DoF")
    add("max_speed_mps", r.get("max_speed_ms"), f"{r.get('max_speed_ms')} m/s", "m/s")
    if r.get("battery_min"):
        add("runtime_h", r["battery_min"] / 60.0, f"{r['battery_min']} min", "min")
    add("price_usd", r.get("price_usd"), f"${r.get('price_usd')}", "USD")
    return {"url": url, "values": vals}


# label -> our field, per catalog. Keys are lower-cased labels with markup and units removed.
HG_LABELS = {
    "height": "height_mm", "weight": "weight_kg", "payload": "payload_kg", "max payload": "payload_kg",
    "max speed": "max_speed_mps", "top speed": "max_speed_mps", "speed": "max_speed_mps",
    "runtime pr charge": "runtime_h", "runtime": "runtime_h", "battery capacity": "battery_wh",
    "price": "price_usd", "dof": "dof", "degrees of freedom": "dof",
}


def label_key(s):
    s = re.sub(r"\[[^\]]*\]|\([^)]*\)", " ", s)              # drop the unit in brackets
    s = re.sub(r"[^A-Za-z ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def val_from_parse(p, text, source=None, unit=None):
    return {"value": p.get("value"), "lo": p.get("lo"), "hi": p.get("hi"), "unit": unit or p.get("unit", ""),
            "text": text, "source": source}


def label_unit(label):
    m = re.search(r"\[([^\]]+)\]|\(([^)]+)\)", label)
    return (m.group(1) or m.group(2)).strip() if m else ""


def a_humanoid_guide(url, ctx):
    """humanoid.guide: one spec table per product page; the unit sits in the label, e.g. 'Height [cm]'."""
    body = fetch(url)
    if not body:
        return None
    vals = {}
    for row in tables(body):
        if len(row) < 2:
            continue
        fld = HG_LABELS.get(label_key(row[0]))
        if not fld:
            continue
        cell, unit = row[1], label_unit(row[0])
        if fld == "price_usd":
            m = re.search(rf"{NUM}", cell.replace(",", ""))
            if m:
                vals.setdefault(fld, {"value": tonum(m.group(0)), "unit": unit or "USD", "text": cell, "source": None})
            continue
        if fld == "dof":
            m = re.search(r"\d+", cell)
            if m:
                vals.setdefault(fld, {"value": float(m.group(0)), "unit": "", "text": cell, "source": None})
            continue
        p = parse_num_unit(f"{cell} {unit}", DIM[fld])
        if p:
            shown = cell if (not unit or re.search(r"[A-Za-z]", cell)) else f"{cell} {unit}"
            vals.setdefault(fld, val_from_parse(p, shown, None, unit or p["unit"]))
    return {"url": url, "values": vals}


HV_LABELS = {
    "height": "height_mm", "height standing": "height_mm", "weight": "weight_kg", "mass": "weight_kg",
    "payload": "payload_kg", "maximum speed": "max_speed_mps", "max speed": "max_speed_mps",
    "total dof": "dof", "dof": "dof", "battery": "battery_wh", "runtime": "runtime_h", "price": "price_usd",
}


def a_humanoidversus(url, ctx):
    """humanoidversus.com: /robots/<slug>, a 'Specifications' table whose value cell appends notes."""
    body = fetch(url)
    if not body:
        return None
    vals = {}
    for row in tables(body):
        if len(row) < 2:
            continue
        fld = HV_LABELS.get(label_key(row[0]))
        if not fld:
            continue
        cell = re.split(r"Notes?\s*&\s*sources", row[1])[0]
        cell = cell.split("·")[0].strip()
        if fld == "dof":
            m = re.search(r"\d+", cell)
            if m:
                vals.setdefault(fld, {"value": float(m.group(0)), "unit": "", "text": cell, "source": None})
            continue
        if fld == "price_usd":
            m = re.search(rf"{NUM}", cell.replace(",", ""))
            if m:
                vals.setdefault(fld, {"value": tonum(m.group(0)), "unit": "USD", "text": row[1], "source": None})
            continue
        p = parse_num_unit(cell, DIM[fld])
        if p:
            vals.setdefault(fld, val_from_parse(p, cell))
    return {"url": url, "values": vals}


RR_LABELS = {
    "mass": "weight_kg", "weight": "weight_kg", "payload": "payload_kg", "top speed": "max_speed_mps",
    "maximum speed": "max_speed_mps", "runtime per charge": "runtime_h", "runtime": "runtime_h",
    "battery energy": "battery_wh", "price": "price_usd", "dimensions": "dims",
}


def a_roboticsrankings(url, ctx):
    """roboticsrankings.com: a Product JSON-LD block carries the specs as additionalProperty."""
    body = fetch(url)
    if not body:
        return None
    vals = {}
    for bl in re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', body, re.S):
        if "additionalProperty" not in bl:
            continue
        try:
            d = json.loads(bl)
        except ValueError:
            continue
        for item in (d if isinstance(d, list) else [d]):
            for prop in item.get("additionalProperty") or []:
                name, val, unit = prop.get("name", ""), prop.get("value"), prop.get("unitText") or ""
                key = label_key(name)
                if key.startswith("dimensions"):
                    nums = [tonum(x) for x in re.findall(NUM, str(val))]
                    du = (unit or re.search(r"[a-z]+\s*$", str(val)).group(0).strip() if re.search(r"[a-z]+\s*$", str(val)) else "mm")
                    du = {"mm": 1, "cm": 10, "m": 1000, "in": 25.4, "inch": 25.4}.get(du.lower(), 1)
                    for fld, n in zip(("length_mm", "width_mm", "height_mm"), nums):
                        vals.setdefault(fld, {"value": n * du, "unit": unit or "mm", "text": str(val), "source": None})
                    continue
                fld = RR_LABELS.get(key)
                if not fld:
                    continue
                if fld == "price_usd" and isinstance(val, (int, float)):
                    vals.setdefault(fld, {"value": float(val), "unit": unit or "USD", "text": f"{val} {unit}".strip(), "source": None})
                    continue
                p = parse_num_unit(f"{val} {unit}", DIM[fld])
                if p:
                    vals.setdefault(fld, val_from_parse(p, f"{val} {unit}".strip(), None, unit or p["unit"]))
    return {"url": url, "values": vals}


EG_FELT = {"egenvaegt": "weight_kg", "hoejde": "height_mm", "bredde": "width_mm", "laengde": "length_mm",
           "nyttelast": "payload_kg", "hastighed": "max_speed_mps", "frihedsgrader": "dof",
           "driftstid": "runtime_h", "pris": "price_usd"}


def eg_source(block):
    m = re.search(r'nt--src.*?href="([^"]+)"', block, re.S)
    return m.group(1) if m else None


def a_embodied(url, ctx):
    """embodied.guide: one div per field (id="felt-…"); the metric figure is the first b.num + span.enhed."""
    body = fetch(url)
    if not body:
        return None
    vals = {}
    for m in re.finditer(r'id="felt-([a-z0-9-]+)"(.{0,6000}?)(?=<div class="r r--|</section>)', body, re.S):
        fld = EG_FELT.get(m.group(1))
        if not fld:
            continue
        block = m.group(2)
        vm = re.search(r'<b class="num">([\d.,]+)</b>\s*<span class="enhed">([^<]+)</span>', block)
        if not vm:
            continue
        num, unit = tonum(vm.group(1)), vm.group(2).strip()
        text = f"{vm.group(1)} {unit}".strip()
        if fld == "price_usd":
            vals.setdefault(fld, {"value": num, "unit": unit, "text": text, "source": eg_source(block)})
            continue
        if fld == "dof":
            vals.setdefault(fld, {"value": num, "unit": "", "text": text, "source": eg_source(block)})
            continue
        p = parse_num_unit(text, DIM[fld])
        if p:
            vals.setdefault(fld, val_from_parse(p, text, eg_source(block), unit))
    return {"url": url, "values": vals}


ADAPTERS = {"droid.monster": a_droid, "botupyourlife.com": a_buyl, "data.robo2u.com": a_r2u,
            "humanoid.guide": a_humanoid_guide, "humanoidversus.com": a_humanoidversus,
            "roboticsrankings.com": a_roboticsrankings, "embodied.guide": a_embodied}
CATALOG_URL = {"droid.monster": "https://droid.monster", "botupyourlife.com": "https://botupyourlife.com",
               "data.robo2u.com": "https://data.robo2u.com", "humanoid.guide": "https://humanoid.guide",
               "humanoidversus.com": "https://humanoidversus.com", "roboticsrankings.com": "https://roboticsrankings.com",
               "embodied.guide": "https://embodied.guide"}


# ---------------------------------------------------------------- compare
def same_ip(a, b):
    n = lambda s: re.sub(r"[^A-Za-z0-9]", "", str(s)).lower()
    return n(a) == n(b)


def compare_field(field, mine, theirs):
    """Return a disagreement dict, or None when the two agree (or cannot be compared)."""
    if mine is None or mine == "":
        tv = theirs.get("value")
        if isinstance(tv, (int, float)):
            tv = round(tv, 3)
        return {"kind": "ours_missing", "theirs": tv, "their_text": theirs.get("text")}
    dim = DIM[field]
    if dim in ("ip", "text"):
        if same_ip(mine, theirs.get("value")):
            return None
        return {"kind": "differs", "ours": mine, "theirs": theirs.get("value")}
    try:
        o = float(mine)
    except (TypeError, ValueError):
        return None
    tol, floor = TOL.get(dim, (0.02, 0)), FLOOR.get(dim, 0)
    lo, hi, t = theirs.get("lo"), theirs.get("hi"), theirs.get("value")
    if hi is not None:                       # the catalog states a range
        if lo - max(abs(lo) * tol, floor) <= o <= hi + max(abs(hi) * tol, floor):
            return None
        return {"kind": "differs", "ours": mine, "theirs": theirs.get("text")}
    if t is None:
        return None
    t = float(t)
    slack = max(abs(o) * tol, floor)
    if abs(t - o) <= slack:
        return None
    return {"kind": "differs", "ours": mine, "theirs": round(t, 4)}


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true", help="use the cache only, never touch the network")
    ap.add_argument("--fetch-only", action="store_true", help="download the pages and stop")
    ap.add_argument("--catalog", action="append", help="limit to one catalog id (repeatable)")
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()

    ours = load_ours()
    have_seen = {rid: r for rid, r in ours.items() if r.get("seen_on")}
    pages = [(rid, u) for rid, r in have_seen.items() for u in r["seen_on"]]
    hosts = sorted({urllib.parse.urlsplit(u).netloc for _, u in pages})
    unknown = [h for h in hosts if h not in ADAPTERS]
    if unknown:
        print("WARN no adapter for:", ", ".join(unknown))

    ctx = {}
    # bulk endpoints, fetched once
    if any(h in ADAPTERS for h in hosts):
        b = fetch("https://botupyourlife.com/api/robots.json")
        ctx["buyl"] = {r["id"]: r for r in json.loads(b)} if b else {}
        b = fetch("https://data.robo2u.com/api/robots")
        ctx["r2u"] = {r["slug"]: r for r in (json.loads(b).get("robots") if b else [])}
        b = fetch("https://api.droid.monster/v1/models.json")
        ctx["droid"] = json.loads(b) if b else {"models": []}

    # page fetches for the HTML catalogs
    html_urls = [u for _, u in pages if urllib.parse.urlsplit(u).netloc in ADAPTERS
                 and urllib.parse.urlsplit(u).netloc not in ("droid.monster", "botupyourlife.com", "data.robo2u.com")]
    fetch_many(html_urls, offline=args.offline, workers=args.workers, label="pages")
    if args.fetch_only:
        return

    # read each recorded page
    per_robot = {}
    stats = {h: {"listed": 0, "read": 0, "unread": 0, "entries": 0} for h in hosts if h in ADAPTERS}
    unread = []
    for rid, url in pages:
        host = urllib.parse.urlsplit(url).netloc
        fn = ADAPTERS.get(host)
        if not fn or (args.catalog and host not in args.catalog):
            continue
        stats[host]["listed"] += 1
        got = None
        try:
            got = fn(url, ctx)
        except Exception as e:
            got = None
        if not got:
            stats[host]["unread"] += 1
            unread.append({"robot": rid, "catalog": host, "url": url, "why": "page not readable"})
            continue
        if not got["values"]:
            stats[host]["unread"] += 1
            unread.append({"robot": rid, "catalog": host, "url": url, "why": "no comparable field on the page"})
            continue
        stats[host]["read"] += 1
        rec = per_robot.setdefault(rid, {})
        rec[host] = got

    # review signals from our own records
    dupes = spec_dupes()
    unconfirmed = sorted(rid for rid, r in ours.items() if r.get("verification") == "unconfirmed")
    noted = sorted(rid for rid, r in ours.items() if r.get("note") and CONFLICT_WORDS.search(r["note"]))

    # compare
    robots = []
    by_field = {}
    by_catalog = {}
    n_diff = n_missing = 0
    for rid in sorted(per_robot, key=lambda i: (ours[i]["manufacturer"].lower(), ours[i]["name"].lower())):
        r = ours[rid]
        diffs = []
        for host, got in per_robot[rid].items():
            for field, theirs in got["values"].items():
                res = compare_field(field, r.get(field), theirs)
                if not res:
                    continue
                d = {"catalog": host, "field": field, "kind": res["kind"],
                     "ours": res.get("ours"), "theirs": res.get("theirs"),
                     "their_text": theirs.get("text"), "unit": theirs.get("unit", ""),
                     "source": theirs.get("source"), "url": got["url"]}
                if d["theirs"] is None and res["kind"] == "ours_missing":
                    d["theirs"] = theirs.get("text")
                diffs.append(d)
                by_field[field] = by_field.get(field, 0) + 1
                by_catalog[host] = by_catalog.get(host, 0) + 1
                if res["kind"] == "differs":
                    n_diff += 1
                else:
                    n_missing += 1
        if diffs:
            diffs.sort(key=lambda d: ([f for f, _, _ in CORE].index(d["field"]), d["catalog"]))
            robots.append({"id": rid, "name": r["name"], "manufacturer": r["manufacturer"],
                           "category": r["category"], "verification": r.get("verification"),
                           "catalogs": sorted(per_robot[rid]), "diffs": diffs})
    seen_ids = {rb["id"] for rb in robots}
    for rid in sorted(set(noted) | set(dupes) | set(unconfirmed), key=lambda i: (ours[i]["manufacturer"].lower(), ours[i]["name"].lower())):
        if rid in seen_ids:
            continue
        r = ours[rid]
        robots.append({"id": rid, "name": r["name"], "manufacturer": r["manufacturer"],
                       "category": r["category"], "verification": r.get("verification"),
                       "catalogs": sorted(per_robot.get(rid, {})), "diffs": []})
    robots.sort(key=lambda rb: (rb["manufacturer"].lower(), rb["name"].lower()))
    for rb in robots:
        rid = rb["id"]
        r = ours[rid]
        if r.get("note") and CONFLICT_WORDS.search(r["note"]):
            rb["note"] = r["note"]
        if rid in dupes:
            rb["spec_dupes"] = dupes[rid]
        if r.get("verification") == "unconfirmed":
            rb["unconfirmed"] = True
            rb["sources_n"] = len(r.get("sources") or [])

    catalogs = []
    for h in sorted(stats, key=lambda h: -stats[h]["listed"]):
        s = stats[h]
        fields = sorted({d["field"] for rb in robots for d in rb["diffs"] if d["catalog"] == h},
                        key=lambda f: [x for x, _, _ in CORE].index(f))
        catalogs.append({"id": h, "url": CATALOG_URL.get(h, "https://" + h), "listed": s["listed"],
                         "read": s["read"], "unread": s["unread"], "divergences": by_catalog.get(h, 0),
                         "fields": fields})
    out = {
        "doc": "Cross-catalog disagreement view (issue #33). Review aid for maintainers: it shows what a competitor "
               "catalog publishes for a robot whose record carries that catalog in seen_on, next to the value in "
               "data/parts/*.json. A competitor value never goes into data/ — only a maker source can change a spec.",
        "generated": datetime.date.today().isoformat(),
        "tolerance": {k: v for k, v in TOL.items()},
        "scope": {"robots": len(ours), "with_seen_on": len(have_seen), "recorded_pages": len(pages),
                  "pages_read": sum(s["read"] for s in stats.values()),
                  "robots_compared": len(per_robot),
                  "robots_with_disagreement": sum(1 for rb in robots if rb["diffs"]),
                  "robots_unconfirmed": len(unconfirmed), "robots_note_conflict": len(noted),
                  "robots_spec_dupes": len(dupes), "robots_listed": len(robots)},
        "summary": {"differs": n_diff, "ours_missing": n_missing, "entries": n_diff + n_missing,
                    "by_field": {f: by_field[f] for f in sorted(by_field, key=lambda f: -by_field[f])},
                    "by_catalog": {h: by_catalog[h] for h in sorted(by_catalog, key=lambda h: -by_catalog[h])}},
        "catalogs": catalogs,
        "unread": unread,
        "robots": robots,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    print(f"{len(robots)} robots with a disagreement, {n_diff} differing values, {n_missing} fields we leave empty")
    print(f"catalogs: " + ", ".join(f"{c['id']} {c['read']}/{c['listed']}" for c in catalogs))
    print(f"wrote research/disagreements.json ({os.path.getsize(OUT)/1024:.0f} KB)")


if __name__ == "__main__":
    main()
