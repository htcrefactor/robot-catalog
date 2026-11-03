#!/usr/bin/env python3
"""Build the spec superset from data/specs/*.json.
Writes data/spec_keys.json (every key ever used: group, label, unit, robot count)
and data/spec_matrix.json (key -> rows of {id,value,unit,note,source}). Run from repo root."""
import json,glob,os,collections,datetime
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ids={r["id"] for f in glob.glob(f"{root}/data/parts/*.json") for r in json.load(open(f))}
keys={};cnt=collections.defaultdict(set);matrix=collections.defaultdict(list);n=0
for f in sorted(glob.glob(f"{root}/data/specs/*.json")):
    d=json.load(open(f));rid=d["id"]
    if rid not in ids: print("WARN unknown id",rid);continue
    n+=1
    for s in d.get("specs",[]):
        k=s["key"]
        if k not in keys: keys[k]={"key":k,"group":s.get("group",""),"label":s.get("label",k),"unit":s.get("unit","")}
        cnt[k].add(rid)
        matrix[k].append({"id":rid,"value":s.get("value"),"unit":s.get("unit",""),"note":s.get("note",""),"source":s.get("source","")})
out=[dict(v,robots=len(cnt[k])) for k,v in keys.items()]
out.sort(key=lambda x:(x["group"],-x["robots"],x["label"].lower()))
json.dump({"updated":datetime.date.today().isoformat(),"robots_with_specs":n,"keys":out},open(f"{root}/data/spec_keys.json","w"),ensure_ascii=False,indent=1)
json.dump(matrix,open(f"{root}/data/spec_matrix.json","w"),ensure_ascii=False)
print(f"{n} robots, {len(out)} keys, {sum(len(v) for v in matrix.values())} values")
