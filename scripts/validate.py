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
built = json.load(open(os.path.join(root, "data/robots.json"), encoding="utf-8"))["robots"]
if len(built) != len(ids): err.append(f"data/robots.json has {len(built)} robots but parts have {len(ids)}: run scripts/merge.py")
base = os.environ.get("BASE_COUNT")
if base and len(ids) < int(base) and os.environ.get("ALLOW_DROP") != "1":
    err.append(f"robot count dropped from {base} to {len(ids)}: explain in the PR and add the label count-drop-ok")
print(f"{len(ids)} robots checked, {len(err)} problems")
for e in err[:300]: print("ERROR:", e)
sys.exit(1 if err else 0)
