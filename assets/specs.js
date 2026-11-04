// All-specs explorer: filter robots, then compare any field (or a family of related fields)
// as a ranked chart, a distribution, a scatter against another field, or a table.
(async()=>{
const $=id=>document.getElementById(id);
const d=await loadData();$("foot").innerHTML=footer(d.meta);
const K=await (await fetch("data/spec_keys.json",{cache:"no-cache"})).json();
const M=await (await fetch("data/spec_matrix.json",{cache:"no-cache"})).json();
const R=Object.fromEntries(d.robots.map(r=>[r.id,r]));
const KEY=Object.fromEntries(K.keys.map(k=>[k.key,k]));
const FAM=Object.fromEntries((K.families||[]).map(f=>[f.id,f]));
const LOCOS=[...new Set(d.robots.map(r=>r.locomotion).filter(Boolean))].sort();
$("sub").textContent=t("specs_sub",{k:K.keys.length,r:K.robots_with_specs});
// ---------- state (kept in the URL hash so a comparison can be shared) ----------
const S={k:"",fam:"",vs:"",loco:new Set(),cat:new Set(),q:"",view:"chart",proxy:false,sort:"asc"};
const readHash=()=>{const h=new URLSearchParams(location.hash.slice(1));
 if(h.has("k")||h.has("fam")){S.k=h.get("k")||"";S.fam=h.get("fam")||"";S.vs=h.get("vs")||"";S.view=h.get("view")||"chart";S.proxy=h.get("proxy")==="1";S.sort=h.get("sort")||"asc";
  S.loco=new Set((h.get("loco")||"").split(",").filter(Boolean));S.cat=new Set((h.get("cat")||"").split(",").filter(Boolean));}
 else if(location.hash.length>1&&KEY[decodeURIComponent(location.hash.slice(1))])S.k=decodeURIComponent(location.hash.slice(1));};
const writeHash=()=>{const h=new URLSearchParams();if(S.fam)h.set("fam",S.fam);else if(S.k)h.set("k",S.k);
 if(S.vs)h.set("vs",S.vs);if(S.view!=="chart")h.set("view",S.view);if(S.proxy)h.set("proxy","1");if(S.sort!=="asc")h.set("sort",S.sort);
 if(S.loco.size)h.set("loco",[...S.loco].join(","));if(S.cat.size)h.set("cat",[...S.cat].join(","));history.replaceState(null,"","#"+h.toString());};
readHash();
const inFilter=r=>r&&(!S.loco.size||S.loco.has(r.locomotion))&&(!S.cat.size||S.cat.has(r.category))&&(!S.q||(r.name+" "+r.manufacturer).toLowerCase().includes(S.q));
const pool=()=>d.robots.filter(inFilter);
const rname=id=>{const r=R[id];return r?`${r.manufacturer} ${r.name}`:id};
const sname=id=>{const r=R[id];return r?r.name:id}; // short label for charts; full name in tooltip
const color=id=>CAT_COLORS[(R[id]||{}).category]||"#8a94a6";
const nf=x=>x==null?"—":(+(+x).toPrecision(4)).toLocaleString();
// per-robot numeric summary for a key: {id,lo,hi,vals[],rows[]}
const perRobot=(key,ids)=>{const out={};(M[key]||[]).forEach(x=>{if(!ids.has(x.id))return;const o=out[x.id]??={id:x.id,vals:[],rows:[]};o.rows.push(x);
 if(x.n!=null)o.vals.push(x.n);else if(x.lo!=null){o.vals.push(x.lo,x.hi);}});
 return Object.values(out).map(o=>({...o,lo:o.vals.length?Math.min(...o.vals):null,hi:o.vals.length?Math.max(...o.vals):null}));};
const median=a=>{const s=[...a].sort((x,y)=>x-y),m=s.length>>1;return s.length?(s.length%2?s[m]:(s[m-1]+s[m])/2):null};
// ---------- filters ----------
const chips=(id,vals,set,lab)=>{$(id).innerHTML=`<span class="small muted">${lab}</span>`+vals.map(v=>`<button class="chip ${set.has(v)?"on":""}" data-v="${esc(v)}">${esc(tv(v))}</button>`).join("");
 $(id).querySelectorAll("button").forEach(b=>b.onclick=()=>{set.has(b.dataset.v)?set.delete(b.dataset.v):set.add(b.dataset.v);b.classList.toggle("on");render();});};
chips("fLoco",LOCOS,S.loco,t("locomotion"));chips("fCat",CATS.filter(c=>d.robots.some(r=>r.category===c)),S.cat,t("category"));
$("fq").oninput=e=>{S.q=e.target.value.toLowerCase();render();};
// ---------- field list ----------
const kl=$("kl"),q=$("q");
const drawList=()=>{const s=q.value.toLowerCase();let h="";
 const fams=(K.families||[]).filter(f=>!s||f.label.toLowerCase().includes(s)||(f.label_ko||"").includes(s));
 if(fams.length)h+=`<div class="small muted grouphd">${t("families")}</div>`+fams.map(f=>`<a data-f="${f.id}" class="${S.fam===f.id?"on":""}"><span>▦ ${esc(LANG==="ko"&&f.label_ko?f.label_ko:f.label)}</span><span class="muted small">${f.keys.length}</span></a>`).join("");
 const order=[...GROUPS,...new Set(K.keys.map(k=>k.group).filter(g=>!GROUPS.includes(g)))];
 order.forEach(g=>{const ks=K.keys.filter(k=>k.group===g&&(!s||k.label.toLowerCase().includes(s)||k.key.includes(s)));if(!ks.length)return;
  h+=`<div class="small muted grouphd">${esc(tg(g))}</div>`+ks.map(k=>`<a data-k="${esc(k.key)}" class="${!S.fam&&S.k===k.key?"on":""}"><span>${esc(k.label)}${k.numeric>=3?' <span class="numtag">#</span>':""}</span><span class="muted small">${k.robots}</span></a>`).join("");});
 kl.innerHTML=h;
 kl.querySelectorAll("a[data-k]").forEach(a=>a.onclick=()=>{S.k=a.dataset.k;S.fam="";S.vs="";render();drawList();$("vals").scrollIntoView({behavior:"smooth",block:"start"});});
 kl.querySelectorAll("a[data-f]").forEach(a=>a.onclick=()=>{S.fam=a.dataset.f;S.k="";S.vs="";render();drawList();$("vals").scrollIntoView({behavior:"smooth",block:"start"});});};
q.oninput=drawList;
// ---------- SVG charts ----------
const W=760;
function rankChart(items,unit,proxyItems){ // items: [{id,lo,hi,vals,label?}] sorted
 const all=[...items,...(proxyItems||[])];if(!all.length)return"";
 const max=Math.max(...all.map(o=>o.hi)),min=Math.min(0,...all.map(o=>o.lo));const L=230,P=60,rh=20;
 const x=v=>L+(v-min)/(max-min||1)*(W-L-P);const H=all.length*rh+28;
 let g="";all.forEach((o,i)=>{const y=i*rh+6,px=o.proxy;
  g+=`<g class="row"><title>${esc(rname(o.id))}: ${o.vals.map(nf).join(", ")} ${esc(unit)}${px?" ("+t("proxy_short")+")":""}</title>
  <a href="robot.html?id=${encodeURIComponent(o.id)}"><text x="${L-8}" y="${y+13}" text-anchor="end" class="lbl">${esc(sname(o.id).slice(0,32))}</text></a>
  <rect x="${x(min)}" y="${y+3}" width="${Math.max(1,x(o.lo)-x(min))}" height="${rh-8}" rx="3" fill="${color(o.id)}" opacity="${px?.25:.85}" ${px?'stroke="'+color(o.id)+'" stroke-dasharray="3 2"':""}/>
  ${o.hi>o.lo?`<line x1="${x(o.lo)}" x2="${x(o.hi)}" y1="${y+rh/2}" y2="${y+rh/2}" stroke="${color(o.id)}" stroke-width="2"/>`+o.vals.map(v=>`<circle cx="${x(v)}" cy="${y+rh/2}" r="3.5" fill="${color(o.id)}"/>`).join(""):""}
  <text x="${x(o.hi)+6}" y="${y+13}" class="val">${o.hi>o.lo?nf(o.lo)+"–"+nf(o.hi):nf(o.lo)}${px?" *":""}</text></g>`;});
 const ticks=niceTicks(min,max,5).map(v=>`<line x1="${x(v)}" x2="${x(v)}" y1="0" y2="${H-22}" class="grid"/><text x="${x(v)}" y="${H-6}" text-anchor="middle" class="tick">${nf(v)}</text>`).join("");
 return `<svg viewBox="0 0 ${W} ${H}" class="chart" role="img">${ticks}${g}<text x="${W-4}" y="${H-6}" text-anchor="end" class="tick">${esc(unit)}</text></svg>`;}
function niceTicks(a,b,n){const span=b-a||1,step=Math.pow(10,Math.floor(Math.log10(span/n)));const m=[1,2,5,10].find(m=>span/(m*step)<=n)||10;const s=m*step,out=[];for(let v=Math.ceil(a/s)*s;v<=b+1e-9;v+=s)out.push(+v.toFixed(10));return out;}
function histogram(items,unit){const v=items.map(o=>o.lo);if(v.length<3)return"";
 const mn=Math.min(...v),mx=Math.max(...v);const nb=Math.min(12,Math.max(4,Math.ceil(Math.sqrt(v.length))+1));const ticks=niceTicks(mn,mx,nb);
 const step=ticks.length>1?ticks[1]-ticks[0]:1;const lo0=Math.floor(mn/step)*step;const bins=[];for(let b=lo0;b<=mx+1e-9;b+=step)bins.push({a:b,b:b+step,ids:[]});
 items.forEach(o=>{const i=Math.min(bins.length-1,Math.floor((o.lo-lo0)/step+1e-9));bins[i].ids.push(o.id);});
 const H=170,B=30,top=Math.max(...bins.map(b=>b.ids.length));const bw=(W-60)/bins.length;
 const bars=bins.map((b,i)=>{let y=H-B;return b.ids.map(id=>{const h=(H-B-24)/top;y-=h;return `<rect x="${40+i*bw+2}" y="${y}" width="${bw-4}" height="${h-1}" fill="${color(id)}"><title>${esc(rname(id))}</title></rect>`}).join("")+
  `<text x="${40+i*bw+bw/2}" y="${H-B+14}" text-anchor="middle" class="tick">${nf(b.a)}–${nf(b.b)}</text>`+(b.ids.length?`<text x="${40+i*bw+bw/2}" y="${H-B-(H-B-24)/top*b.ids.length-4}" text-anchor="middle" class="tick">${b.ids.length}</text>`:"");}).join("");
 return `<h3>${t("distribution")}</h3><svg viewBox="0 0 ${W} ${H}" class="chart">${bars}<text x="${W-4}" y="${H-4}" text-anchor="end" class="tick">${esc(unit)} · ${t("robots_per_bin")}</text></svg>`;}
function scatter(a,b,ka,kb){const B=Object.fromEntries(b.map(o=>[o.id,o]));const pts=a.filter(o=>B[o.id]).map(o=>({id:o.id,x:o.lo,y:B[o.id].lo}));
 if(pts.length<2)return `<p class="muted">${t("scatter_few",{n:pts.length})}</p>`;
 const H=380,L=60,P=20;const xs=pts.map(p=>p.x),ys=pts.map(p=>p.y);const x0=Math.min(...xs),x1=Math.max(...xs),y0=Math.min(...ys),y1=Math.max(...ys);
 const X=v=>L+(v-x0)/(x1-x0||1)*(W-L-P),Y=v=>H-40-(v-y0)/(y1-y0||1)*(H-60);
 const tx=niceTicks(x0,x1,6).map(v=>`<line x1="${X(v)}" x2="${X(v)}" y1="10" y2="${H-40}" class="grid"/><text x="${X(v)}" y="${H-24}" text-anchor="middle" class="tick">${nf(v)}</text>`).join("");
 const ty=niceTicks(y0,y1,6).map(v=>`<line x1="${L}" x2="${W-P}" y1="${Y(v)}" y2="${Y(v)}" class="grid"/><text x="${L-6}" y="${Y(v)+4}" text-anchor="end" class="tick">${nf(v)}</text>`).join("");
 const dots=pts.map(p=>`<a href="robot.html?id=${encodeURIComponent(p.id)}"><circle cx="${X(p.x)}" cy="${Y(p.y)}" r="5" fill="${color(p.id)}" opacity=".85"><title>${esc(rname(p.id))}: ${nf(p.x)} ${esc(ka.unit)}, ${nf(p.y)} ${esc(kb.unit)}</title></circle></a>`).join("");
 return `<svg viewBox="0 0 ${W} ${H}" class="chart">${tx}${ty}${dots}<text x="${W-P}" y="${H-6}" text-anchor="end" class="tick">${esc(ka.label)} (${esc(ka.unit)})</text><text x="${L}" y="12" class="tick">${esc(kb.label)} (${esc(kb.unit)})</text></svg>`;}
const legend=ids=>{const cs=[...new Set(ids.map(id=>(R[id]||{}).category))].filter(Boolean);return `<div class="legend">${cs.map(c=>`<span><i style="background:${CAT_COLORS[c]}"></i>${esc(tv(c))}</span>`).join("")}</div>`};
const csv=(rows,name)=>{const s=rows.map(r=>r.map(c=>`"${String(c??"").replace(/"/g,'""')}"`).join(",")).join("\n");const a=document.createElement("a");a.href=URL.createObjectURL(new Blob(["\ufeff"+s],{type:"text/csv"}));a.download=name+".csv";a.click();};
// ---------- views ----------
function viewKey(){const k=KEY[S.k];const P=pool(),ids=new Set(P.map(r=>r.id));const rows=(M[k.key]||[]).filter(x=>ids.has(x.id));
 const have=new Set(rows.map(x=>x.id));const items=perRobot(k.key,ids).filter(o=>o.lo!=null);items.sort((a,b)=>S.sort==="asc"?a.lo-b.lo:b.hi-a.hi);
 const numeric=k.numeric>=3&&items.length>0;const lows=items.map(o=>o.lo);
 let h=`<h2>${esc(k.label)} <span class="muted small">${esc(tg(k.group))}</span></h2>
 <p class="small">${t("coverage_line",{a:have.size,b:P.length})}${numeric&&items.length<have.size?" · "+t("text_only",{n:have.size-items.length}):""}</p>`;
 if(numeric){h+=`<div class="stats"><div><b>${nf(Math.min(...lows))}</b><span>${t("min")}</span></div><div><b>${nf(median(lows))}</b><span>${t("median")}</span></div><div><b>${nf(Math.max(...items.map(o=>o.hi)))}</b><span>${t("max")}</span></div><div><b>${esc(k.unit)}</b><span>${t("unit")}</span></div></div>
  <div class="toolbar"><div class="seg2">${["chart","dist","scatter","table"].map(v=>`<button class="${S.view===v?"on":""}" data-view="${v}">${t("view_"+v)}</button>`).join("")}</div>
  ${S.view==="chart"?`<button class="chip" id="sortBtn">${S.sort==="asc"?t("sort_asc"):t("sort_desc")}</button>`:""}
  <button class="chip" id="csvBtn">CSV ↓</button></div>`;
  if(S.view==="chart")h+=legend(items.map(o=>o.id))+rankChart(items,k.unit);
  if(S.view==="dist")h+=legend(items.map(o=>o.id))+histogram(items,k.unit);
  if(S.view==="scatter"){const opts=K.keys.filter(x=>x.numeric>=3&&x.key!==k.key).sort((a,b)=>b.numeric-a.numeric);
   h+=`<p><label>${t("plot_against")} <select id="vsSel"><option value="">—</option>${opts.map(x=>`<option value="${esc(x.key)}" ${S.vs===x.key?"selected":""}>${esc(x.label)} (${x.numeric})</option>`).join("")}</select></label></p>`;
   if(S.vs&&KEY[S.vs])h+=legend(items.map(o=>o.id))+scatter(items,perRobot(S.vs,ids).filter(o=>o.lo!=null),k,KEY[S.vs]);}
 }
 if(!numeric||S.view==="table")h+=table(rows,numeric);
 const miss=P.filter(r=>!have.has(r.id));
 if(miss.length)h+=`<details class="miss"><summary>${t("not_published_by",{n:miss.length})}</summary><p class="small">${miss.map(r=>`<a href="robot.html?id=${encodeURIComponent(r.id)}">${esc(r.manufacturer)} ${esc(r.name)}</a>`).join(" · ")}</p></details>`;
 $("vals").innerHTML=h;wire(k,rows);}
function table(rows,numeric){const rs=[...rows];if(numeric)rs.sort((a,b)=>(a.n??a.lo??Infinity)-(b.n??b.lo??Infinity));
 return `<div class="tablewrap"><table class="mega"><thead><tr><th>${t("robot")}</th><th>${t("category")}</th><th>${t("value")}</th><th>${t("note")}</th><th>${t("source")}</th></tr></thead><tbody>
 ${rs.map(x=>{const r=R[x.id]||{name:x.id,manufacturer:"",category:""};return `<tr><td><a href="robot.html?id=${encodeURIComponent(x.id)}">${esc(r.manufacturer)} ${esc(r.name)}</a></td><td>${esc(tv(r.category))}</td><td>${sv(x.value,x.unit)}</td><td class="small">${esc(x.note||"")}</td><td class="small">${x.source?`<a href="${esc(x.source)}" target="_blank" rel="noopener">${esc(host(x.source))}</a>`:""}</td></tr>`}).join("")}</tbody></table></div>`;}
function viewFam(){const f=FAM[S.fam];const P=pool(),ids=new Set(P.map(r=>r.id));const fl=LANG==="ko"&&f.label_ko?f.label_ko:f.label;
 const toB=(k,o)=>{const m=KEY[k].f2b||1;return {...o,lo:o.lo*m,hi:o.hi*m,vals:o.vals.map(v=>v*m)}};
 const per=f.keys.map(k=>({k,items:perRobot(k,ids).filter(o=>o.lo!=null).map(o=>toB(k,o))}));
 const dims=new Set(per.filter(p=>p.items.length).map(p=>KEY[p.k].dim));const unit=(per.find(p=>p.items.length&&KEY[p.k].base)||{k:f.keys[0]});const U0=KEY[unit.k].base||KEY[unit.k].unit||"";const have=new Set(per.flatMap(p=>p.items.map(o=>o.id)));
 const proxyK=f.proxy&&KEY[f.proxy];const proxy=proxyK?perRobot(f.proxy,ids).filter(o=>o.lo!=null).map(o=>toB(f.proxy,o)):[];
 const pal=["#2f5bea","#e04f16","#16b364","#7a5af8","#eaaa08","#ee46bc","#0ba5ec","#8a94a6","#b54708"];
 let robots=[...have];if(S.proxy&&proxyK)robots=[...new Set([...robots,...proxy.map(o=>o.id)])];
 const first=id=>{for(const p of per){const o=p.items.find(o=>o.id===id);if(o)return o.lo}const o=proxy.find(o=>o.id===id);return o?o.lo:Infinity};
 robots.sort((a,b)=>first(a)-first(b));
 let h=`<h2>${esc(fl)} <span class="muted small">${t("family")}</span></h2><p class="small">${t("fam_cov",{a:have.size,b:P.length})}</p>`;
 if(proxyK)h+=`<label class="small"><input type="checkbox" id="pxBox" ${S.proxy?"checked":""}> ${t("proxy_toggle",{f:esc(proxyK.label)})}</label><p class="small muted">${esc(f.proxy_note||"")}</p>`;
 if(dims.size===1&&robots.length){const unit=U0;{const all=[...per.flatMap(p=>p.items.flatMap(o=>o.vals)),...(S.proxy?proxy.flatMap(o=>o.vals):[])];const mx=Math.max(...all),L=230,P2=50,rh=20,H=robots.length*rh+28;const x=v=>L+v/(mx||1)*(W-L-P2);
  let g="";robots.forEach((id,i)=>{const y=i*rh+6;g+=`<a href="robot.html?id=${encodeURIComponent(id)}"><text x="${L-8}" y="${y+13}" text-anchor="end" class="lbl">${esc(sname(id).slice(0,32))}</text></a><line x1="${L}" x2="${W-P2}" y1="${y+rh/2}" y2="${y+rh/2}" class="grid"/>`;
   if(S.proxy){const o=proxy.find(o=>o.id===id);if(o)g+=`<rect x="${L}" y="${y+5}" width="${x(o.lo)-L}" height="${rh-10}" fill="var(--muted)" opacity=".25"><title>${esc(proxyK.label)}: ${nf(o.lo)} ${esc(unit)}</title></rect>`;}
   per.forEach((p,j)=>{const o=p.items.find(o=>o.id===id);if(o)o.vals.forEach(v=>g+=`<circle cx="${x(v)}" cy="${y+rh/2}" r="5" fill="${pal[j%pal.length]}"><title>${esc(rname(id))} · ${esc(KEY[p.k].label)}: ${nf(v)} ${esc(unit)}</title></circle>`);});});
  const ticks=niceTicks(0,mx,6).map(v=>`<line x1="${x(v)}" x2="${x(v)}" y1="0" y2="${H-22}" class="grid"/><text x="${x(v)}" y="${H-6}" text-anchor="middle" class="tick">${nf(v)}</text>`).join("");
  h+=`<div class="legend">${per.map((p,j)=>p.items.length?`<span><i style="background:${pal[j%pal.length]};border-radius:50%"></i>${esc(KEY[p.k].label)} (${p.items.length})</span>`:"").join("")}${S.proxy&&proxyK?`<span><i style="background:var(--muted);opacity:.4"></i>${esc(proxyK.label)}</span>`:""}</div>
  <svg viewBox="0 0 ${W} ${H}" class="chart">${ticks}${g}<text x="${W-4}" y="${H-6}" text-anchor="end" class="tick">${esc(unit)}</text></svg>`;}}
 // matrix table: robot × field (only fields someone in the filter publishes)
 const cols=f.keys.filter(k=>(M[k]||[]).some(x=>robots.includes(x.id)));
 h+=`<div class="tablewrap"><table class="mega"><thead><tr><th>${t("robot")}</th><th>${t("category")}</th>${cols.map(k=>`<th><a href="#k=${k}" data-jump="${k}">${esc(KEY[k].label)}</a>${KEY[k].unit?` <span class="muted small">${esc(KEY[k].unit)}</span>`:""}</th>`).join("")}${proxyK?`<th class="muted">${esc(proxyK.label)} <span class="small">${esc(proxyK.unit)}</span></th>`:""}</tr></thead><tbody>
 ${robots.map(id=>`<tr><td><a href="robot.html?id=${encodeURIComponent(id)}">${esc(rname(id))}</a></td><td>${esc(tv((R[id]||{}).category))}</td>${per.filter(p=>cols.includes(p.k)).map(p=>{const o=p.items.find(o=>o.id===id);const raw=(M[p.k]||[]).filter(x=>x.id===id);const m=KEY[p.k].f2b||1;return `<td>${o?o.vals.map(v=>nf(v/m)).join(" / "):raw.length?`<span class="small">${raw.map(x=>sv(x.value,x.unit)).join("; ")}</span>`:'<span class="muted">—</span>'}</td>`}).join("")}${proxyK?`<td class="muted">${(o=>o?nf(o.lo/(proxyK.f2b||1)):"—")(proxy.find(o=>o.id===id))}</td>`:""}</tr>`).join("")}</tbody></table></div>`;
 $("vals").innerHTML=h;
 const px=$("pxBox");if(px)px.onchange=()=>{S.proxy=px.checked;render();};
 $("vals").querySelectorAll("[data-jump]").forEach(a=>a.onclick=e=>{e.preventDefault();S.k=a.dataset.jump;S.fam="";render();drawList();});writeHash();}
function wire(k,rows){$("vals").querySelectorAll("[data-view]").forEach(b=>b.onclick=()=>{S.view=b.dataset.view;render();});
 const sb=$("sortBtn");if(sb)sb.onclick=()=>{S.sort=S.sort==="asc"?"desc":"asc";render();};
 const vs=$("vsSel");if(vs)vs.onchange=()=>{S.vs=vs.value;render();};
 const cb=$("csvBtn");if(cb)cb.onclick=()=>csv([["robot","manufacturer","category","locomotion","value","unit","value_in_"+k.unit,"note","source"],...rows.map(x=>{const r=R[x.id]||{};return [r.name,r.manufacturer,r.category,r.locomotion,x.value,x.unit,x.n??(x.lo!=null?x.lo+"-"+x.hi:""),x.note,x.source]})],k.key);writeHash();}
function render(){$("fcount").textContent=t("filter_count",{n:pool().length,t:d.robots.length});
 if(S.fam&&FAM[S.fam])viewFam();else if(S.k&&KEY[S.k])viewKey();else{$("vals").innerHTML=`<p class="muted">${t("pick_field")}</p>`;writeHash();}}
drawList();render();
})();
