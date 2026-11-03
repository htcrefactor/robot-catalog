"""Merge data/parts/*.json into data/robots.json (what the site reads)."""
import json, glob, datetime, os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
robots = {}
for f in sorted(glob.glob(os.path.join(root, "data/parts/*.json"))):
    for r in json.load(open(f, encoding="utf-8")):
        robots[r["id"]] = r
out = {"meta": {"updated": datetime.date.today().isoformat(), "count": len(robots)},
       "robots": sorted(robots.values(), key=lambda r: (r["category"], r["manufacturer"], r["name"]))}
json.dump(out, open(os.path.join(root, "data/robots.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(robots), "robots")
