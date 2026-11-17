"""Validate catalog data. Fails on bad JSON, duplicate ids, missing required fields, unknown categories, a stale robots.json or robots.csv, or an unexplained drop in robot count."""
import csv, json, glob, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catalog_data import CSV_COLUMNS, csv_row  # noqa: E402

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATS = {"AMR","AGV","Humanoid","Quadruped","Wheel-legged","Indoor delivery","Outdoor delivery","Mobile platform","Misc"}
err, ids, records = [], {}, {}
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
base = os.environ.get("BASE_COUNT")
if base and len(ids) < int(base) and os.environ.get("ALLOW_DROP") != "1":
    err.append(f"robot count dropped from {base} to {len(ids)}: explain in the PR and add the label count-drop-ok")
print(f"{len(ids)} robots checked, {len(err)} problems")
for e in err[:300]: print("ERROR:", e)
sys.exit(1 if err else 0)
