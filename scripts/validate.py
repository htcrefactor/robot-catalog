"""Validate catalog data. Fails on bad JSON, duplicate ids, missing required fields, unknown categories, a stale robots.json, or an unexplained drop in robot count."""
import json, glob, os, sys
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
base = os.environ.get("BASE_COUNT")
if base and len(ids) < int(base) and os.environ.get("ALLOW_DROP") != "1":
    err.append(f"robot count dropped from {base} to {len(ids)}: explain in the PR and add the label count-drop-ok")
print(f"{len(ids)} robots checked, {len(err)} problems")
for e in err[:300]: print("ERROR:", e)
sys.exit(1 if err else 0)
