// Shared filter + sort for index.html and table.html. State lives in the URL query string
// (history.replaceState), so any filtered/sorted view can be shared by copying the address.
// No scoring and no comparison: filters only narrow the list, sorts only order it.
const RF_NUM=[["weight","weight_kg","weight","kg"],["payload","payload_kg","payload","kg"],["speed","max_speed_mps","max_speed","m/s"],["runtime","runtime_h","runtime","h"]];
const RF_SORTS=[["name","robot"],["manufacturer","col_maker"],["release_year","col_year"],["price_usd","price"],["weight_kg","weight"],["payload_kg","payload"],["max_speed_mps","max_speed"],["runtime_h","runtime"],["completeness","completeness"]];
const RF_DESC=new Set(["release_year","payload_kg","max_speed_mps","runtime_h","completeness","battery_wh","dof"]);// these default to high→low
const RF_FEAT=[["sdk","sdk_available","has_sdk"],["ros","ros_support","has_ros"],["onb","onboard_compute","has_onboard"],["photo","image_url","has_photo"]];
const RF_SELECTS=[["status","status","all_status"],["country","country","all_countries"],["loco","locomotion","all_locos"]];

function makeFilters({el,robots,onChange,defaultSort="manufacturer",sortKeys=[]}){
 const validSort=new Set([...RF_SORTS.map(s=>s[0]),...sortKeys.map(s=>s[0])]);const sLabel=k=>{const a=sortKeys.find(s=>s[0]===k);return a?a[1]:k;};// sortKeys: [[field,label]] extra sorts (table columns)
 // precompute search text once (fast with hundreds of robots)
 robots.forEach(r=>{if(r._hay==null)r._hay=[r.name,r.manufacturer,r.id,r.category,tv(r.category),r.country,tv(r.country),r.locomotion,r.status,r.sdk_name,r.compute_detail,(r.sensors||[]).join(" "),r.summary,r.summary_ko].filter(Boolean).join(" ").toLowerCase();});
 const P=new URLSearchParams(location.search);
 const num=k=>{const v=P.get(k);return v===null||v===""||isNaN(+v)?"":+v;};
 const S={q:P.get("q")||"",cat:P.get("cat")||"",status:P.get("status")||"",country:P.get("country")||"",loco:P.get("loco")||"",
  price:P.get("price")==="has"?"has":"",pmax:num("pmax"),feat:new Set(RF_FEAT.map(f=>f[0]).filter(k=>P.get(k)==="1")),rng:{},
  sort:validSort.has(P.get("sort"))?P.get("sort"):defaultSort,dir:null};
 RF_NUM.forEach(([k])=>S.rng[k]=[num(k+"_min"),num(k+"_max")]);
 S.dir=P.get("dir")==="desc"||P.get("dir")==="asc"?P.get("dir"):(RF_DESC.has(S.sort)?"desc":"asc");
 const defDir=k=>RF_DESC.has(k)?"desc":"asc";
 const opts=(f,allKey,cur)=>{const vals=[...new Set(robots.map(r=>r[f]).filter(Boolean))].sort((a,b)=>tv(a).localeCompare(tv(b)));
  return `<option value="">${esc(t(allKey))}</option>`+vals.map(v=>`<option value="${esc(v)}"${v===cur?" selected":""}>${esc(tv(v))}</option>`).join("");};
 const cats=CATS.filter(c=>robots.some(r=>r.category===c)).concat([...new Set(robots.map(r=>r.category).filter(c=>c&&!CATS.includes(c)))]);
 const moreOn=()=>S.price||S.pmax!==""||S.feat.size||Object.values(S.rng).some(([a,b])=>a!==""||b!=="");
 el.innerHTML=`<div class="fbar">
 <div class="chiprow" id="rfCat">${["",...cats].map(c=>`<button class="chip ${c===S.cat?"on":""}" data-c="${esc(c)}">${c?esc(tv(c)):t("all")}</button>`).join("")}</div>
 <div class="controls">
  <input type="search" id="rfQ" data-i18n-ph="search" placeholder="${esc(t("search"))}" value="${esc(S.q)}">
  ${RF_SELECTS.map(([k,f,a])=>`<select id="rf_${k}" aria-label="${esc(t(a))}">${opts(f,a,S[k])}</select>`).join("")}
  <label class="small muted" for="rfSort">${t("sort_by")}</label>
  <select id="rfSort">${RF_SORTS.map(([k,l])=>`<option value="${k}"${k===S.sort?" selected":""}>${esc(t(l))}</option>`).join("")}${validSort.has(S.sort)&&!RF_SORTS.some(s=>s[0]===S.sort)?`<option value="${esc(S.sort)}" selected>${esc(sLabel(S.sort))}</option>`:""}</select>
  <button class="btn" id="rfDir"></button>
  <button class="btn" id="rfReset">${t("reset")}</button>
  <button class="btn" id="rfCopy">${t("copy_link")}</button>
  <span class="small muted" id="rfN"></span>
 </div>
 <details class="more" id="rfMore"${moreOn()?" open":""}><summary>${t("flt_more")}</summary>
  <div class="morebody">
   <div class="fgrp"><div class="small muted">${t("flt_price")}</div>
    <select id="rfPrice"><option value="">${t("price_any")}</option><option value="has"${S.price==="has"?" selected":""}>${t("price_has")}</option></select>
    <label class="small">${t("price_under")} <input type="number" min="0" step="any" id="rfPmax" class="num" value="${S.pmax}"></label></div>
   <div class="fgrp"><div class="small muted">${t("flt_features")}</div>
    ${RF_FEAT.map(([k,,l])=>`<label class="small chk"><input type="checkbox" data-f="${k}"${S.feat.has(k)?" checked":""}> ${t(l)}</label>`).join("")}</div>
   <div class="fgrp wide"><div class="small muted">${t("flt_ranges")}</div><div class="ranges">
    ${RF_NUM.map(([k,,l,u])=>`<div class="rng"><span class="small">${t(l)} <span class="muted">(${u})</span></span><input type="number" step="any" class="num" data-r="${k}" data-i="0" placeholder="${t("rf_min")}" value="${S.rng[k][0]}"><span class="muted">–</span><input type="number" step="any" class="num" data-r="${k}" data-i="1" placeholder="${t("rf_max")}" value="${S.rng[k][1]}"></div>`).join("")}
   </div></div>
  </div></details></div>`;
 const $=id=>el.querySelector("#"+id);
 const dirBtn=()=>{$("rfDir").textContent=S.dir==="asc"?t("rf_sort_asc"):t("rf_sort_desc");};dirBtn();
 function writeURL(){const p=new URLSearchParams(location.search);
  ["q","cat","status","country","loco","price","pmax","sort","dir",...RF_FEAT.map(f=>f[0]),...RF_NUM.flatMap(([k])=>[k+"_min",k+"_max"])].forEach(k=>p.delete(k));
  const set=(k,v)=>{if(v!==""&&v!=null)p.set(k,v)};
  set("q",S.q.trim());set("cat",S.cat);set("status",S.status);set("country",S.country);set("loco",S.loco);set("price",S.price);set("pmax",S.pmax);
  S.feat.forEach(k=>p.set(k,"1"));RF_NUM.forEach(([k])=>{set(k+"_min",S.rng[k][0]);set(k+"_max",S.rng[k][1]);});
  if(S.sort!==defaultSort||S.dir!==defDir(defaultSort)){p.set("sort",S.sort);if(S.dir!==defDir(S.sort))p.set("dir",S.dir);}
  const qs=p.toString();history.replaceState(null,"",location.pathname+(qs?"?"+qs:"")+location.hash);}
 let tm=0;const fire=(now)=>{clearTimeout(tm);const go=()=>{writeURL();onChange();};if(now)go();else tm=setTimeout(go,150);};
 $("rfCat").onclick=e=>{const b=e.target.closest("[data-c]");if(!b)return;S.cat=b.dataset.c;$("rfCat").querySelectorAll(".chip").forEach(x=>x.classList.toggle("on",x.dataset.c===S.cat));fire(1);};
 $("rfQ").oninput=e=>{S.q=e.target.value;fire();};
 RF_SELECTS.forEach(([k])=>$("rf_"+k).onchange=e=>{S[k]=e.target.value;fire(1);});
 $("rfSort").onchange=e=>{S.sort=e.target.value;S.dir=defDir(S.sort);dirBtn();fire(1);};
 $("rfDir").onclick=()=>{S.dir=S.dir==="asc"?"desc":"asc";dirBtn();fire(1);};
 $("rfPrice").onchange=e=>{S.price=e.target.value;fire(1);};
 $("rfPmax").oninput=e=>{S.pmax=e.target.value===""||isNaN(+e.target.value)?"":+e.target.value;fire();};
 el.querySelectorAll("[data-f]").forEach(c=>c.onchange=()=>{c.checked?S.feat.add(c.dataset.f):S.feat.delete(c.dataset.f);fire(1);});
 el.querySelectorAll("[data-r]").forEach(i=>i.oninput=()=>{S.rng[i.dataset.r][+i.dataset.i]=i.value===""||isNaN(+i.value)?"":+i.value;fire();});
 $("rfReset").onclick=()=>{history.replaceState(null,"",location.pathname+location.hash);location.reload();};
 $("rfCopy").onclick=async()=>{try{await navigator.clipboard.writeText(location.href);$("rfCopy").textContent=t("link_copied");setTimeout(()=>$("rfCopy").textContent=t("copy_link"),1500);}catch(e){prompt(t("copy_link"),location.href);}};
 function apply(){const q=S.q.trim().toLowerCase().split(/\s+/).filter(Boolean);
  const feat=RF_FEAT.filter(f=>S.feat.has(f[0]));const rng=RF_NUM.filter(([k])=>S.rng[k][0]!==""||S.rng[k][1]!=="");
  const out=robots.filter(r=>{
   if(S.cat&&r.category!==S.cat)return false;if(S.status&&r.status!==S.status)return false;if(S.country&&r.country!==S.country)return false;if(S.loco&&r.locomotion!==S.loco)return false;
   // "has price" means any published price signal: a USD figure, a stated price note or a dated
   // observation (a migrated record carries price_usd: null). The max-price box compares USD only.
   if(S.price==="has"&&!(r.price_usd!=null||hasVal(r.price_note)||hasVal(r.price_observations)))return false;
   if(S.pmax!==""&&!(r.price_usd<S.pmax))return false;
   for(const [,f] of feat){if(f==="image_url"?!r.image_url:r[f]!==true)return false;}
   for(const [k,f] of rng){const v=r[f],[lo,hi]=S.rng[k];if(v==null)return false;if(lo!==""&&v<lo)return false;if(hi!==""&&v>hi)return false;}
   for(const w of q)if(!r._hay.includes(w))return false;return true;});
  const k=S.sort,m=S.dir==="asc"?1:-1,str=v=>Array.isArray(v)?v.join(", "):v;
  const tie=(a,b)=>(a.manufacturer||"").localeCompare(b.manufacturer||"")||(a.name||"").localeCompare(b.name||"");
  // 'completeness' is computed, not a record key: sort on the percentage completeness() returns.
  const sv=r=>k==="completeness"?completeness(r).pct:str(r[k]);
  out.sort((a,b)=>{let x=sv(a),y=sv(b);const nx=x==null||x==="",ny=y==null||y==="";
   if(nx&&ny)return tie(a,b);if(nx)return 1;if(ny)return -1;// unknown values always last
   const c=typeof x==="string"||typeof y==="string"?String(x).localeCompare(String(y)):typeof x==="boolean"?(x===y?0:x?1:-1):x-y;return c*m||tie(a,b);});
  const n=$("rfN");if(n)n.textContent=t("n_of",{n:out.length,m:robots.length});return out;}
 function setSort(k){if(!validSort.has(k))return;if(k===S.sort)S.dir=S.dir==="asc"?"desc":"asc";else{S.sort=k;S.dir=defDir(k);}
  const sel=$("rfSort");if(![...sel.options].some(o=>o.value===k))sel.add(new Option(sLabel(k),k));sel.value=k;dirBtn();fire(1);}
 return {state:S,apply,setSort};
}
