"""Validate catalog data. Fails on bad JSON, duplicate ids, missing required fields, unknown categories, a stale robots.json or robots.csv, bad dated price observations, a missing FX table, or an unexplained drop in robot count."""
import csv, json, glob, os, re, sys, datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catalog_data import CSV_COLUMNS, csv_row  # noqa: E402

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATS = {"AMR","AGV","Humanoid","Quadruped","Wheel-legged","Indoor delivery","Outdoor delivery","Mobile platform","Misc"}
KINDS = {"list","from","rental","edu"}
PRECISIONS = {"INT8","INT4","FP8","FP4","FP16","BF16","FP32"}
err, ids, records, warn = [], {}, {}, []
KR_KINDS = {"direct", "distributor", "reseller"}
SDK_KEYS = {"languages", "open_source", "license", "url"}
SIM_KEYS = {"urdf", "mjcf", "usd", "isaac", "mujoco", "gazebo"}
def is_url(v): return isinstance(v, str) and v.startswith(("http://", "https://"))
def check_dev(r, rid):
    s = r.get("sdk")
    if s is not None:
        if not isinstance(s, dict): err.append(f"{rid}: sdk must be an object or null")
        else:
            for k in s:
                if k not in SDK_KEYS: err.append(f"{rid}: unknown sdk key {k}")
            l = s.get("languages")
            if l is not None and (not isinstance(l, list) or not all(isinstance(x, str) and x for x in l)):
                err.append(f"{rid}: sdk.languages must be a list of strings")
            if s.get("open_source") not in (None, True, False): err.append(f"{rid}: sdk.open_source must be true/false/null")
            if s.get("license") is not None and not isinstance(s["license"], str): err.append(f"{rid}: sdk.license must be a string or null")
            if not is_url(s.get("url")): err.append(f"{rid}: sdk.url must be an http(s) URL")
            if r.get("sdk_available") is False: err.append(f"{rid}: sdk is filled but sdk_available is false")
    if r.get("ros2_support") not in (None, True, False): err.append(f"{rid}: ros2_support must be true/false/null")
    if r.get("ros2_url") is not None and not is_url(r["ros2_url"]): err.append(f"{rid}: ros2_url must be an http(s) URL")
    if r.get("ros2_support") is True and not r.get("ros2_url"): err.append(f"{rid}: ros2_support is true but ros2_url is empty")
    sm = r.get("sim_models")
    if sm is not None:
        if not isinstance(sm, dict): err.append(f"{rid}: sim_models must be an object or null")
        else:
            for k, v in sm.items():
                if k not in SIM_KEYS: err.append(f"{rid}: unknown sim_models key {k}")
                elif not isinstance(v, dict) or not is_url(v.get("url")):
                    err.append(f"{rid}: sim_models.{k} needs an http(s) url")
                elif v.get("license") is not None and not isinstance(v["license"], str):
                    err.append(f"{rid}: sim_models.{k}.license must be a string or null")
                elif set(v) - {"url", "license"}: err.append(f"{rid}: sim_models.{k} has unknown keys {sorted(set(v) - {'url', 'license'})}")
    oss = r.get("open_source_repos")
    if oss is not None:
        if not isinstance(oss, list): err.append(f"{rid}: open_source_repos must be a list")
        else:
            for o in oss:
                if not isinstance(o, dict) or not o.get("name") or not is_url(o.get("url")):
                    err.append(f"{rid}: every open_source_repos entry needs a name and an http(s) url")
                elif set(o) - {"name", "url", "license"}: err.append(f"{rid}: open_source_repos entry has unknown keys {sorted(set(o) - {'name', 'url', 'license'})}")


def load_fx():
    p = os.path.join(root, "data/fx.json")
    try:
        fx = json.load(open(p, encoding="utf-8"))
    except Exception as e:
        err.append(f"data/fx.json: missing or invalid ({e}) — run scripts/build_fx.py")
        return {}
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(fx.get("date", ""))):
        err.append("data/fx.json: no reference date")
    rates = fx.get("rates") or {}
    if not rates:
        err.append("data/fx.json: no rates")
    if rates.get("KRW") != 1:
        err.append("data/fx.json: KRW must be the base (rate 1)")
    if rates.get("USD") in (None, 0):
        err.append("data/fx.json: no USD rate, so observations cannot be shown in KRW and USD")
    if not fx.get("source_url"):
        err.append("data/fx.json: no source_url")
    return rates


RATES = load_fx()
today = datetime.date.today()
for f in sorted(glob.glob(os.path.join(root, "data/parts/*.json"))):
    try: recs = json.load(open(f, encoding="utf-8"))
    except Exception as e: err.append(f"{f}: invalid JSON ({e})"); continue
    for r in recs:
        i = r.get("id")
        if not i: err.append(f"{os.path.basename(f)}: record without id"); continue
        if i in ids: err.append(f"duplicate id {i} in {os.path.basename(f)} and {ids[i]}")
        ids[i] = os.path.basename(f)
        records[i] = r
        for k in ("name", "manufacturer", "category"):
            if not r.get(k): err.append(f"{i}: missing {k}")
        if r.get("category") and r["category"] not in CATS: err.append(f"{i}: unknown category {r['category']}")
        if r.get("verification") not in (None, "official", "unconfirmed"): err.append(f"{i}: bad verification {r.get('verification')}")
        check_dev(r, i)
        # safety & certification fields (issue #30)
        for k in ("safety_standards", "certifications"):
            v = r.get(k)
            if v is None:
                continue
            if not isinstance(v, list) or any(not isinstance(x, str) or not x.strip() for x in v):
                err.append(f"{i}: {k} must be a list of non-empty strings")
        for k in ("safety_pl", "safety_note"):
            v = r.get(k)
            if v is not None and (not isinstance(v, str) or not v.strip()):
                err.append(f"{i}: {k} must be a non-empty string or null")
        ssrc = r.get("safety_source")
        has_safety = any(r.get(k) for k in ("safety_standards", "certifications", "safety_pl", "safety_note"))
        if ssrc is not None:
            if not isinstance(ssrc, str) or not ssrc.startswith(("http://", "https://")):
                err.append(f"{i}: safety_source must be an http(s) URL")
            elif ssrc not in (r.get("sources") or []):
                err.append(f"{i}: safety_source {ssrc} is not listed in sources")
        elif has_safety:
            err.append(f"{i}: safety fields set but safety_source is null")
        for k in ("name_ko", "manufacturer_ko"):
            if r.get(k) is not None and not (isinstance(r[k], str) and r[k].strip()): err.append(f"{i}: {k} must be a non-empty string")
        if r.get("kr_note") is not None and not (isinstance(r["kr_note"], str) and r["kr_note"].strip()): err.append(f"{i}: kr_note must be a non-empty string")
        dists = r.get("kr_distributors")
        if dists is not None:
            if not isinstance(dists, list): err.append(f"{i}: kr_distributors must be a list")
            else:
                if len(dists) > 6: err.append(f"{i}: kr_distributors has more than 6 entries")
                seen = set()
                for d in dists:
                    if not isinstance(d, dict): err.append(f"{i}: kr_distributors entry must be an object"); continue
                    name = d.get("name")
                    if not (isinstance(name, str) and name.strip()): err.append(f"{i}: kr_distributors entry without name")
                    elif name in seen: err.append(f"{i}: duplicate kr_distributors name {name}")
                    else: seen.add(name)
                    if not (isinstance(d.get("url"), str) and d["url"].startswith("http")): err.append(f"{i}: kr_distributors entry needs an http(s) url ({name})")
                    if d.get("kind") not in KR_KINDS: err.append(f"{i}: kr_distributors kind must be one of {sorted(KR_KINDS)} ({name})")
        if r.get("country") == "South Korea" and not r.get("manufacturer_ko"): warn.append(f"{i}: South Korean record without manufacturer_ko")
        # structured compute (Issue #28): types, precision vocabulary, source must be in sources
        cs = r.get("compute_soc")
        if cs is not None and (not isinstance(cs, str) or not cs.strip()): err.append(f"{i}: compute_soc must be a non-empty string or null")
        ct = r.get("compute_tops")
        if ct is not None and (isinstance(ct, bool) or not isinstance(ct, (int, float)) or ct <= 0): err.append(f"{i}: compute_tops must be a positive number or null")
        cp = r.get("compute_tops_precision")
        if cp is not None and cp not in PRECISIONS: err.append(f"{i}: unknown compute_tops_precision {cp}")
        cm = r.get("compute_memory_gb")
        if cm is not None and (isinstance(cm, bool) or not isinstance(cm, int) or cm <= 0): err.append(f"{i}: compute_memory_gb must be a positive integer or null")
        csrc = r.get("compute_source")
        if csrc is not None and (not isinstance(csrc, str) or not csrc.startswith("http")): err.append(f"{i}: compute_source must be a URL or null")
        if csrc and csrc not in (r.get("sources") or []): err.append(f"{i}: compute_source {csrc} is not listed in sources")
        if (cs or ct or cm) and r.get("onboard_compute") is False: err.append(f"{i}: compute values but onboard_compute is false")
        obs = r.get("price_observations")
        if obs is None: continue
        if not isinstance(obs, list): err.append(f"{i}: price_observations must be a list"); continue
        if r.get("price_usd") is not None or r.get("price_note") is not None:
            err.append(f"{i}: has price_observations and also the legacy price_usd/price_note — keep one")
        if not obs: err.append(f"{i}: price_observations is empty — omit the field instead")
        seen = set()
        for n, o in enumerate(obs):
            at = f"{i}: price_observations[{n}]"
            if not isinstance(o, dict): err.append(f"{at} is not an object"); continue
            d = str(o.get("date", ""))
            if not re.match(r"^\d{4}-\d{2}-\d{2}$", d):
                err.append(f"{at}: date must be YYYY-MM-DD, got {o.get('date')!r}")
            else:
                try:
                    dd = datetime.date.fromisoformat(d)
                    if dd > today: err.append(f"{at}: date {d} is in the future")
                except ValueError:
                    err.append(f"{at}: date {d} is not a real date")
            a = o.get("amount")
            if not isinstance(a, (int, float)) or isinstance(a, bool) or a <= 0:
                err.append(f"{at}: amount must be a positive number, got {a!r}")
            c = o.get("currency")
            if not (isinstance(c, str) and re.match(r"^[A-Z]{3}$", c)):
                err.append(f"{at}: currency must be an ISO 4217 code, got {c!r}")
            elif c not in RATES:
                err.append(f"{at}: no FX rate for {c} in data/fx.json — run scripts/build_fx.py")
            k = o.get("kind")
            if k not in KINDS:
                err.append(f"{at}: kind must be one of {sorted(KINDS)}, got {k!r}")
            s = o.get("source")
            if not (isinstance(s, str) and s.startswith("http")):
                err.append(f"{at}: source must be an http(s) URL")
            elif s not in (r.get("sources") or []):
                err.append(f"{at}: source {s} is not listed in the record's sources")
            if o.get("note") is not None and not isinstance(o.get("note"), str):
                err.append(f"{at}: note must be a string")
            key = (d, a, c, k, s)
            if key in seen: err.append(f"{at}: duplicate observation {key}")
            seen.add(key)
built = json.load(open(os.path.join(root, "data/robots.json"), encoding="utf-8"))["robots"]
if len(built) != len(ids): err.append(f"data/robots.json has {len(built)} robots but parts have {len(ids)}: run scripts/merge.py")
# data/robots.csv is generated from the same parts: it must be present and match them cell for cell.
csv_path = os.path.join(root, "data/robots.csv")
if not os.path.exists(csv_path):
    err.append("data/robots.csv is missing: run scripts/merge.py")
else:
    with open(csv_path, encoding="utf-8", newline="") as fh:
        rows = list(csv.reader(fh))
    expected = [[i] + csv_row(records[i])[1:] for i in sorted(records)]
    if not rows:
        err.append("data/robots.csv is empty: run scripts/merge.py")
    elif rows[0] != CSV_COLUMNS:
        err.append("data/robots.csv header is out of date: run scripts/merge.py")
    elif rows[1:] != expected:
        bad = next((n for n, (a, b) in enumerate(zip(rows[1:], expected)) if a != b), min(len(rows), len(expected)) - 1)
        err.append(f"data/robots.csv is out of date at row {bad + 2} (id {rows[bad + 1][0] if bad + 1 < len(rows) else '?'}, "
                   f"{len(rows) - 1} rows vs {len(expected)} expected): run scripts/merge.py")
for path in sorted(glob.glob(os.path.join(root, "data/history/*.json"))):
    name = os.path.basename(path)
    try: hist = json.load(open(path, encoding="utf-8"))
    except Exception as e: err.append(f"data/history/{name}: invalid JSON ({e})"); continue
    rid = hist.get("id") or name[:-5]
    if name != f"{rid}.json": err.append(f"data/history/{name}: file name must match its id ({rid}.json)")
    events = hist.get("events")
    if not isinstance(events, list) or not events: err.append(f"data/history/{name}: needs a non-empty events list"); continue
    # a robot dropped from the catalog keeps its history file, ending in a "removed" event
    if rid not in ids and events[-1].get("type") != "removed":
        err.append(f"data/history/{name}: unknown robot id {rid}")
    for e in events:
        if not isinstance(e, dict): err.append(f"data/history/{name}: event is not an object"); continue
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(e.get("date") or "")): err.append(f"data/history/{name}: bad date {e.get('date')!r}")
        if e.get("type") not in ("added", "updated", "removed"): err.append(f"data/history/{name}: bad type {e.get('type')!r}")
        if e.get("type") == "updated" and not e.get("changes"): err.append(f"data/history/{name}: updated event without changes")
        for c in e.get("changes") or []:
            if not isinstance(c, dict) or not c.get("field") or "from" not in c or "to" not in c:
                err.append(f"data/history/{name}: change needs field, from and to ({c!r})")
sys.path.insert(0, os.path.join(root, "scripts"))
import build_feed
from xml.etree import ElementTree
feed_path = os.path.join(root, "feed.xml")
if not os.path.exists(feed_path):
    err.append("feed.xml is missing: run scripts/merge.py (or scripts/build_feed.py)")
else:
    try: ElementTree.parse(feed_path)
    except Exception as e: err.append(f"feed.xml is not valid XML ({e})")
    if open(feed_path, encoding="utf-8").read() != build_feed.build():
        err.append("feed.xml is out of date: run scripts/merge.py (or scripts/build_feed.py)")
base = os.environ.get("BASE_COUNT")
if base and len(ids) < int(base) and os.environ.get("ALLOW_DROP") != "1":
    err.append(f"robot count dropped from {base} to {len(ids)}: explain in the PR and add the label count-drop-ok")
print(f"{len(ids)} robots checked, {len(err)} problems")
for e in err[:300]: print("ERROR:", e)
for w in warn[:50]: print("WARN:", w)
sys.exit(1 if err else 0)
