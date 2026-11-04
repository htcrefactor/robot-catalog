#!/usr/bin/env python3
"""Build the spec superset from data/specs/*.json. Run from anywhere.
Writes:
  data/spec_keys.json   every key ever used: group, label, display unit, dimension, robot count, numeric count
  data/spec_matrix.json key -> rows {id,value,unit,note,source,n|lo,hi} where n / lo,hi are the value
                        converted to the key's display unit (so every robot is comparable and sortable).
Aliases (data/spec_key_aliases.json) fold duplicate keys; data/spec_key_meta.json holds curated labels and families."""
import json,glob,os,re,collections,datetime
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ids={r["id"] for f in glob.glob(f"{root}/data/parts/*.json") for r in json.load(open(f))}
A=json.load(open(f"{root}/data/spec_key_aliases.json")) if os.path.exists(f"{root}/data/spec_key_aliases.json") else {}
META=json.load(open(f"{root}/data/spec_key_meta.json")) if os.path.exists(f"{root}/data/spec_key_meta.json") else {"labels":{},"families":[]}

# unit -> (dimension, factor to that dimension's base unit). Temperature °F handled specially.
U={"mm":("length",1),"cm":("length",10),"m":("length",1000),"km":("length",1e6),"in":("length",25.4),"ft":("length",304.8),"mi":("length",1609344),
   "g":("mass",.001),"kg":("mass",1),"t":("mass",1000),"lb":("mass",.45359237),"lbs":("mass",.45359237),
   "m/s":("speed",1),"km/h":("speed",1/3.6),"mph":("speed",.44704),"mm/s":("speed",.001),
   "ms":("time",1/3.6e6),"s":("time",1/3600),"min":("time",1/60),"h":("time",1),"days":("time",24),
   "Wh":("energy",1),"kWh":("energy",1000),"Ah":("charge",1),"mAh":("charge",.001),
   "°C":("temp",1),"°F":("temp",None),"°":("angle",1),"deg":("angle",1),"rad":("angle",57.29577951),
   "°/s":("angvel",1),"deg/s":("angvel",1),"rad/s":("angvel",57.29577951),
   "V":("volt",1),"V DC":("volt",1),"VDC":("volt",1),"W":("power",1),"kW":("power",1000),
   "dBA":("dba",1),"dB(A)":("dba",1),"% RH":("rh",1),"%RH":("rh",1),"GB":("bytes",1),"TB":("bytes",1000),
   "months":("months",1),"year":("months",12),"years":("months",12)}
BASE={"length":"mm","mass":"kg","speed":"m/s","time":"h","energy":"Wh","charge":"Ah","temp":"°C","angle":"°","angvel":"°/s","volt":"V","power":"W","dba":"dB(A)","rh":"% RH","bytes":"GB","months":"months"}
NUM=r"[-+]?\d+(?:[.,]\d+)?"
def tonum(s): return float(s.replace(",","")) if s.count(",")==1 and len(s.split(",")[1])==3 else float(s.replace(",","."))
def parse(v,unit):
    """Return (dimension_unit, lo, hi) in the row's own unit, or None if not a clean number/range."""
    if isinstance(v,bool) or v is None: return None
    if isinstance(v,(int,float)): return (unit,float(v),float(v))
    s=str(v).strip()
    m=re.fullmatch(r"(\d+)\s*'\s*(\d+(?:\.\d+)?)\s*\"?",s)            # 5'6"
    if m: return ("in",int(m[1])*12+float(m[2]),int(m[1])*12+float(m[2]))
    m=re.fullmatch(rf"(?:≤|<=|up to|max\.?|~|≈|about)?\s*({NUM})\s*(?:(?:–|-|to|~)\s*({NUM}))?\s*([^\d\s][^()]*)?",s,re.I)
    if not m: return None
    u=(m[3] or unit or "").strip()
    if u and u not in U and u!=unit: return None
    lo=tonum(m[1]);hi=tonum(m[2]) if m[2] else lo
    return (u,min(lo,hi),max(lo,hi))
def conv(x,u,target):
    d,f=U[u];dt,ft=U[target]
    if d=="temp":
        c=(x-32)*5/9 if u=="°F" else x
        return c if target=="°C" else c*9/5+32
    return x*f/ft

keys={};labels=collections.defaultdict(collections.Counter);cnt=collections.defaultdict(set);matrix=collections.defaultdict(list);n=0
for f in sorted(glob.glob(f"{root}/data/specs/*.json")):
    d=json.load(open(f));rid=d["id"]
    if rid not in ids: print("WARN unknown id",rid);continue
    n+=1
    for s in d.get("specs",[]):
        k=A.get(s["key"],s["key"])
        if k not in keys: keys[k]={"key":k,"group":s.get("group","")}
        labels[k][s.get("label",k)]+=1
        cnt[k].add(rid)
        matrix[k].append({"id":rid,"value":s.get("value"),"unit":s.get("unit",""),"note":s.get("note",""),"source":s.get("source","")})

out=[]
for k,rows in matrix.items():
    parsed=[(r,parse(r["value"],r["unit"])) for r in rows]
    dims=collections.Counter(U[p[0]][0] for r,p in parsed if p and p[0] in U)
    disp="";dim=""
    if dims:
        dim=dims.most_common(1)[0][0]
        units=collections.Counter(p[0] for r,p in parsed if p and p[0] in U and U[p[0]][0]==dim)
        disp=units.most_common(1)[0][0]
        # Prefer the metric/base unit when it is tied or the key mixes imperial units in
        if disp in ("in","ft","mi","lb","lbs","mph","°F") and BASE[dim] in units: disp=BASE[dim]
    else:
        units=collections.Counter(p[0] for r,p in parsed if p)
        if units: disp=units.most_common(1)[0][0]
    num=0
    for r,p in parsed:
        if not p: continue
        u,lo,hi=p
        if dim and u in U and U[u][0]==dim: lo,hi=conv(lo,u,disp),conv(hi,u,disp)
        elif u!=disp: continue
        lo,hi=round(lo,4),round(hi,4)
        if lo==hi: r["n"]=lo
        else: r["lo"],r["hi"]=lo,hi
        num+=1
    lab=META["labels"].get(k) or labels[k].most_common(1)[0][0]
    f2b=round(U[disp][1],10) if dim and dim!="temp" and disp in U else 1  # display unit -> dimension base unit (BASE[dim])
    out.append(dict(keys[k],label=lab,unit=disp,dim=dim,base=BASE.get(dim,disp),f2b=f2b,robots=len(cnt[k]),numeric=num))
out.sort(key=lambda x:(x["group"],-x["robots"],x["label"].lower()))
fam=[dict(f,keys=[k for k in f["keys"] if k in matrix]) for f in META.get("families",[])]
json.dump({"updated":datetime.date.today().isoformat(),"robots_with_specs":n,"keys":out,"families":fam},open(f"{root}/data/spec_keys.json","w"),ensure_ascii=False,indent=1)
json.dump(matrix,open(f"{root}/data/spec_matrix.json","w"),ensure_ascii=False)
print(f"{n} robots, {len(out)} keys, {sum(len(v) for v in matrix.values())} values, {sum(o['numeric'] for o in out)} comparable numbers")
