"""Validate catalog data. Fails on bad JSON, duplicate ids, missing required fields, unknown categories, bad structured compute fields, a stale robots.json, or an unexplained drop in robot count."""
import json, glob, os, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATS = {"AMR","AGV","Humanoid","Quadruped","Wheel-legged","Indoor delivery","Outdoor delivery","Mobile platform","Misc"}
PRECISIONS = {"INT8","INT4","FP8","FP4","FP16","BF16","FP32"}
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
built = json.load(open(os.path.join(root, "data/robots.json"), encoding="utf-8"))["robots"]
if len(built) != len(ids): err.append(f"data/robots.json has {len(built)} robots but parts have {len(ids)}: run scripts/merge.py")
base = os.environ.get("BASE_COUNT")
if base and len(ids) < int(base) and os.environ.get("ALLOW_DROP") != "1":
    err.append(f"robot count dropped from {base} to {len(ids)}: explain in the PR and add the label count-drop-ok")
print(f"{len(ids)} robots checked, {len(err)} problems")
for e in err[:300]: print("ERROR:", e)
sys.exit(1 if err else 0)
