"""Validate catalog data. Fails on bad JSON, duplicate ids, missing required fields, unknown categories, malformed Korean-market fields, a stale robots.json, or an unexplained drop in robot count."""
import json, glob, os, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATS = {"AMR","AGV","Humanoid","Quadruped","Wheel-legged","Indoor delivery","Outdoor delivery","Mobile platform","Misc"}
KR_KINDS = {"direct", "distributor", "reseller"}
err, ids, warn = [], {}, []
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
built = json.load(open(os.path.join(root, "data/robots.json"), encoding="utf-8"))["robots"]
if len(built) != len(ids): err.append(f"data/robots.json has {len(built)} robots but parts have {len(ids)}: run scripts/merge.py")
base = os.environ.get("BASE_COUNT")
if base and len(ids) < int(base) and os.environ.get("ALLOW_DROP") != "1":
    err.append(f"robot count dropped from {base} to {len(ids)}: explain in the PR and add the label count-drop-ok")
print(f"{len(ids)} robots checked, {len(err)} problems")
for e in err[:300]: print("ERROR:", e)
for w in warn[:50]: print("WARN:", w)
sys.exit(1 if err else 0)
