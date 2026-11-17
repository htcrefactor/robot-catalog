"""Validate catalog data. Fails on bad JSON, duplicate ids, missing required fields, unknown categories, a stale robots.json, an unexplained drop in robot count, a bad data/history file or a stale feed.xml."""
import json, glob, os, re, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATS = {"AMR","AGV","Humanoid","Quadruped","Wheel-legged","Indoor delivery","Outdoor delivery","Mobile platform","Misc"}
err, ids = [], {}
for f in sorted(glob.glob(os.path.join(root, "data/parts/*.json"))):
    try: recs = json.load(open(f, encoding="utf-8"))
    except Exception as e: err.append(f"{f}: invalid JSON ({e})"); continue
    for r in recs:
        i = r.get("id")
        if not i: err.append(f"{os.path.basename(f)}: record without id"); continue
        if i in ids: err.append(f"duplicate id {i} in {os.path.basename(f)} and {ids[i]}")
        ids[i] = os.path.basename(f)
        for k in ("name", "manufacturer", "category"):
            if not r.get(k): err.append(f"{i}: missing {k}")
        if r.get("category") and r["category"] not in CATS: err.append(f"{i}: unknown category {r['category']}")
        if r.get("verification") not in (None, "official", "unconfirmed"): err.append(f"{i}: bad verification {r.get('verification')}")
built = json.load(open(os.path.join(root, "data/robots.json"), encoding="utf-8"))["robots"]
if len(built) != len(ids): err.append(f"data/robots.json has {len(built)} robots but parts have {len(ids)}: run scripts/merge.py")
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
sys.exit(1 if err else 0)
