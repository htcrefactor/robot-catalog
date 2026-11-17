"""Merge data/parts/*.json into data/robots.json (what the site reads) and
data/robots.csv (the open-data download: the same records, one row per robot).

Run after editing data/parts/*.json:

    python3 scripts/merge.py
"""
import csv, datetime, glob, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catalog_data import CSV_COLUMNS, csv_row  # noqa: E402

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

robots = {}
for f in sorted(glob.glob(os.path.join(root, "data/parts/*.json"))):
    for r in json.load(open(f, encoding="utf-8")):
        robots[r["id"]] = r

today = datetime.date.today().isoformat()
out = {
    "meta": {
        "version": today.replace("-", "."),
        "updated": today,
        "count": len(robots),
        "license": "CC BY 4.0",
        "license_url": "https://creativecommons.org/licenses/by/4.0/",
        "homepage": "https://htcrefactor.github.io/robot-catalog/data.html",
    },
    "robots": sorted(robots.values(), key=lambda r: (r["category"], r["manufacturer"], r["name"])),
}
json.dump(out, open(os.path.join(root, "data/robots.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

# CSV: UTF-8, comma separated, header row, one row per robot, sorted by id so a
# rebuild shows only the records that actually changed.
with open(os.path.join(root, "data/robots.csv"), "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, lineterminator="\n")
    w.writerow(CSV_COLUMNS)
    for r in sorted(robots.values(), key=lambda r: r["id"]):
        w.writerow(csv_row(r))

print(f"{len(robots)} robots -> data/robots.json, data/robots.csv ({len(CSV_COLUMNS)} columns)")
