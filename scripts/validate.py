"""Validate catalog data. Fails on bad JSON, duplicate ids, missing required fields, unknown categories, a stale robots.json, or an unexplained drop in robot count. Also checks the shape of the developer-readiness fields (sdk, ros2_support/ros2_url, sim_models, open_source_repos) added for issue #29."""
import json, glob, os, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATS = {"AMR","AGV","Humanoid","Quadruped","Wheel-legged","Indoor delivery","Outdoor delivery","Mobile platform","Misc"}
SDK_KEYS = {"languages", "open_source", "license", "url"}
SIM_KEYS = {"urdf", "mjcf", "usd", "isaac", "mujoco", "gazebo"}
err, ids = [], {}
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
        check_dev(r, i)
built = json.load(open(os.path.join(root, "data/robots.json"), encoding="utf-8"))["robots"]
if len(built) != len(ids): err.append(f"data/robots.json has {len(built)} robots but parts have {len(ids)}: run scripts/merge.py")
base = os.environ.get("BASE_COUNT")
if base and len(ids) < int(base) and os.environ.get("ALLOW_DROP") != "1":
    err.append(f"robot count dropped from {base} to {len(ids)}: explain in the PR and add the label count-drop-ok")
print(f"{len(ids)} robots checked, {len(err)} problems")
for e in err[:300]: print("ERROR:", e)
sys.exit(1 if err else 0)
