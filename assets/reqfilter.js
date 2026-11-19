// Requirement minimums (issue #72): payload, runtime, top speed and IP rating, shared by
// index.html and table.html so both pages narrow and share a view the same way.
// A minimum is a floor on a value the maker publishes. It is never a score or a ranking, it
// never fills in a missing value, and the sort stays the user's own choice. A robot whose value
// is not stated is left out only while a minimum is set; the "unknown" toggle brings it back.
const REQ_FIELDS=[["payload","payload_kg","payload","kg"],["runtime","runtime_h","runtime","h"],["speed","max_speed_mps","max_speed","m/s"],["ip","ip_rating","ip",""]];
// "IP67" -> {s:6,w:7}; "IPX4" -> {s:null,w:4} (solid protection not stated); anything else -> null.
function ipParts(v){const m=/^ip\s*([0-9x])\s*([0-9x])$/i.exec(String(v==null?"":v).trim());if(!m)return null;
 const d=c=>c.toLowerCase()==="x"?null:+c;const s=d(m[1]),w=d(m[2]);return s===null&&w===null?null:{s,w};}
// true / false, or null when a digit the minimum asks for is not stated (so it cannot be confirmed).
function ipAtLeast(v,min){const a=ipParts(v),b=ipParts(min);if(!a||!b)return null;
 if((b.s!==null&&a.s===null)||(b.w!==null&&a.w===null))return null;
 return (b.s===null||a.s>=b.s)&&(b.w===null||a.w>=b.w);}
function makeReqFilters({el,robots,onChange}){
 const P=new URLSearchParams(location.search);
 const num=k=>{const v=P.get(k+"_min");return v===null||v.trim()===""||isNaN(+v)?"":+v;};
 const ip=P.get("ip_min")||"";
 const S={payload:num("payload"),runtime:num("runtime"),speed:num("speed"),ip:ipParts(ip)?ip:"",unknown:P.get("unknown")==="1"};
 const active=()=>REQ_FIELDS.some(([k])=>S[k]!=="");
 const ipVals=[...new Set(robots.map(r=>r.ip_rating).filter(v=>ipParts(v)))].sort((x,y)=>{const a=ipParts(x),b=ipParts(y);return (a.s===null?-1:a.s)-(b.s===null?-1:b.s)||(a.w===null?-1:a.w)-(b.w===null?-1:b.w);});
 if(S.ip&&!ipVals.includes(S.ip))ipVals.push(S.ip);
 const field=([k,,l,u])=>k==="ip"
  ?`<label class="small">${t("ip")} ≥ <select data-rk="ip" title="${esc(t("req_ip_t"))}" aria-label="${esc(t("ip"))} ≥">${["",...ipVals].map(v=>`<option value="${esc(v)}"${v===S.ip?" selected":""}>${v?esc(v):esc(t("ip_any"))}</option>`).join("")}</select></label>`
  :`<label class="small">${t(l)} ≥ <input type="number" min="0" step="any" inputmode="decimal" data-rk="${k}" value="${S[k]}" placeholder="${esc(t("req_min"))}" aria-label="${esc(t(l))} ≥ (${esc(u)})"> ${esc(u)}</label>`;
 el.innerHTML=`<span class="small muted" title="${esc(t("req_title_t"))}">${t("req_title")}</span>${REQ_FIELDS.map(field).join("")}`+
  `<label class="small chk" data-unk><input type="checkbox" data-rk="unknown"${S.unknown?" checked":""}> <span>${esc(t("req_unknown"))}</span></label>`+
  `<button class="btn" data-clear>${t("req_clear")}</button><span class="small muted" data-n></span>`;
 const $=q=>el.querySelector(q);
 function writeURL(){const p=new URLSearchParams(location.search);
  REQ_FIELDS.forEach(([k])=>p.delete(k+"_min"));p.delete("unknown");
  REQ_FIELDS.forEach(([k])=>{if(S[k]!=="")p.set(k+"_min",S[k]);});
  if(S.unknown&&active())p.set("unknown","1");
  const qs=p.toString();history.replaceState(null,"",location.pathname+(qs?"?"+qs:"")+location.hash);}
 // the toggle is only meaningful while a minimum is set: otherwise nothing is excluded
 const sync=()=>{const u=$("[data-unk]");if(u)u.hidden=!active();};
 const fire=()=>{sync();writeURL();onChange();};
 el.querySelectorAll("[data-rk]").forEach(i=>{const k=i.dataset.rk;
  const h=()=>{const v=i.value;
   if(k==="unknown"){S.unknown=i.checked;}
   else if(k==="ip"){S.ip=v;}
   else{S[k]=v.trim()===""||isNaN(+v)?"":+v;}
   fire();};
  if(i.tagName==="SELECT"||i.type==="checkbox")i.onchange=h;else i.oninput=h;});
 $("[data-clear]").onclick=()=>{REQ_FIELDS.forEach(([k])=>S[k]="");S.unknown=false;
  el.querySelectorAll("[data-rk]").forEach(i=>{if(i.dataset.rk==="unknown")i.checked=false;else i.value="";});
  fire();};
 function match(r){if(!active())return true; // no minimum set: every robot stays in the list
  for(const [k,f] of REQ_FIELDS){if(S[k]==="")continue;
   const v=r[f];
   if(k==="ip"){const ok=ipAtLeast(v,S.ip);if(ok===true)continue;if(ok===null&&S.unknown)continue;return false;}
   if(v===null||v===undefined||v===""){if(S.unknown)continue;return false;}
   if(!(+v>=+S[k]))return false;}
  return true;}
 function note(n,m){const e=$("[data-n]");if(e)e.textContent=active()?t("req_n",{n,m}):"";}
 sync();
 return {state:S,match,active,note};
}
