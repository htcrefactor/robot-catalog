"""Build feed.xml (Atom 1.0): new robots and field-level spec changes.

Two sources, newest first:
  data/history/<id>.json  events scripts/merge.py recorded for one robot (added / updated /
                          removed, with old -> new values and the record's source URL)
  data/CHANGELOG.json     catalog-level imports; a robot listed under "added" gets an "added"
                          entry on that entry's date (those robots predate the history files)

merge.py runs this at the end of every merge, so the feed stays in step with data/robots.json.
Output is deterministic (no build timestamp, stable order), which scripts/validate.py checks.
Usage: python3 scripts/build_feed.py [--limit N]
"""
import datetime, glob, json, os, sys
from urllib.parse import quote
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://htcrefactor.github.io/robot-catalog/"
FEED_URL = SITE + "feed.xml"
LIMIT = 100

UNITS = {"length_mm": "mm", "width_mm": "mm", "height_mm": "mm", "wheel_diameter_mm": "mm",
         "weight_kg": "kg", "payload_kg": "kg", "max_speed_mps": "m/s", "min_speed_mps": "m/s",
         "runtime_h": "h", "battery_wh": "Wh", "price_usd": "USD"}
MAX_CHANGES_PER_ENTRY = 12


def _load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def robots_index():
    """id -> 'Maker Name', from the generated catalog."""
    try:
        data = _load(os.path.join(ROOT, "data", "robots.json"))
    except (FileNotFoundError, ValueError):
        return {}
    out = {}
    for r in data.get("robots", []):
        out[r["id"]] = " ".join(x for x in (r.get("manufacturer"), r.get("name")) if x) or r["id"]
    return out


def history_events(index):
    events = []
    for path in sorted(glob.glob(os.path.join(ROOT, "data", "history", "*.json"))):
        try:
            h = _load(path)
        except ValueError:
            continue
        rid = h.get("id") or os.path.basename(path)[:-5]
        title = index.get(rid) or " ".join(x for x in (h.get("manufacturer"), h.get("name")) if x) or rid
        for e in h.get("events") or []:
            events.append({"id": rid, "title": title, "date": str(e.get("date") or ""),
                           "type": e.get("type") or "", "source": e.get("source"),
                           "changes": e.get("changes") or []})
    return events


def changelog_events(index):
    """Robots first imported before per-robot history existed (data/CHANGELOG.json)."""
    path = os.path.join(ROOT, "data", "CHANGELOG.json")
    if not os.path.exists(path):
        return []
    try:
        log = _load(path)
    except ValueError:
        return []
    out = []
    for entry in log:
        date = str(entry.get("date") or "")
        for rid in entry.get("added") or []:
            if rid in index:
                out.append({"id": rid, "title": index[rid], "date": date, "type": "added",
                            "source": None, "changes": []})
    return out


def collect(limit=LIMIT):
    index = robots_index()
    events = history_events(index)
    seen = {(e["id"], e["type"], e["date"]) for e in events}
    for e in changelog_events(index):
        if (e["id"], e["type"], e["date"]) not in seen:
            events.append(e)
            seen.add((e["id"], e["type"], e["date"]))
    # newest first, then a stable alphabetical order inside one day
    events.sort(key=lambda e: (e["date"], e["title"].lower(), e["type"], e["id"]), reverse=True)
    return events[:limit]


def _val(v, field):
    if v is None or v == "":
        return "<em>—</em>"
    if isinstance(v, bool):
        return "YES" if v else "NO"
    if isinstance(v, (list, dict)):
        text = "; ".join(str(x) for x in v) if isinstance(v, list) else json.dumps(v, ensure_ascii=False)
        if len(text) > 120:
            text = text[:117] + "…"
        return escape(text)
    s = escape(str(v))
    unit = UNITS.get(field)
    return f"{s} {unit}" if unit else s


def _entry(ev):
    rid, date = ev["id"], ev["date"]
    stamp = f"{date}T00:00:00Z"
    url = f"{SITE}robot.html?id={quote(rid)}"
    if ev["type"] == "added":
        title = f"New robot: {ev['title']}"
    elif ev["type"] == "removed":
        title = f"Removed from the catalog: {ev['title']}"
    else:
        n = len(ev["changes"])
        title = f"{ev['title']}: {n} field{'s' if n != 1 else ''} changed"
    body = []
    changes = ev["changes"][:MAX_CHANGES_PER_ENTRY]
    if changes:
        body.append("<ul>" + "".join(
            f"<li>{escape(str(c.get('field')))}: {_val(c.get('from'), c.get('field'))} → "
            f"{_val(c.get('to'), c.get('field'))}</li>" for c in changes) + "</ul>")
        if len(ev["changes"]) > len(changes):
            body.append(f"<p>{len(ev['changes']) - len(changes)} more field(s) changed.</p>")
    body.append(f'<p><a href="{escape(url)}">{escape(ev["title"])} — robot page</a></p>')
    if ev.get("source"):
        body.append(f'<p>Source: <a href="{escape(ev["source"])}">{escape(ev["source"])}</a></p>')
    return (
        "  <entry>\n"
        f"    <id>tag:htcrefactor.github.io,{escape(date[:4])}:robot-catalog/{escape(rid)}/{escape(ev['type'])}/{escape(date)}</id>\n"
        f"    <title>{escape(title)}</title>\n"
        f"    <updated>{stamp}</updated>\n"
        f'    <link rel="alternate" type="text/html" href="{escape(url)}"/>\n'
        f'    <category term="{escape(ev["type"])}"/>\n'
        f'    <summary type="html">{escape("".join(body))}</summary>\n'
        "  </entry>\n"
    )


def build(limit=LIMIT):
    events = collect(limit)
    dates = [e["date"] for e in events if e["date"]]
    if dates:
        updated = max(dates) + "T00:00:00Z"
    else:
        try:
            updated = str(_load(os.path.join(ROOT, "data", "robots.json"))["meta"]["updated"]) + "T00:00:00Z"
        except (FileNotFoundError, ValueError, KeyError):
            updated = "1970-01-01T00:00:00Z"
    head = (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<feed xmlns="http://www.w3.org/2005/Atom">\n'
        "  <title>Robot Catalog — new robots and spec changes</title>\n"
        "  <subtitle>Field-level changes to mobile robot records: every old value, new value and source.</subtitle>\n"
        f'  <link rel="self" type="application/atom+xml" href="{FEED_URL}"/>\n'
        f'  <link rel="alternate" type="text/html" href="{SITE}"/>\n'
        f"  <id>tag:htcrefactor.github.io,2026:robot-catalog/feed</id>\n"
        f"  <updated>{updated}</updated>\n"
        "  <author><name>Robot Catalog</name><uri>https://github.com/htcrefactor/robot-catalog</uri></author>\n"
    )
    return head + "".join(_entry(e) for e in events) + "</feed>\n"


def write(limit=LIMIT):
    xml = build(limit)
    with open(os.path.join(ROOT, "feed.xml"), "w", encoding="utf-8", newline="\n") as f:
        f.write(xml)
    return xml


if __name__ == "__main__":
    args = sys.argv[1:]
    limit = int(args[args.index("--limit") + 1]) if "--limit" in args else LIMIT
    write(limit)
    print(f"feed.xml: {len(collect(limit))} entries")
