const CATS=["AMR","AGV","Humanoid","Quadruped","Wheel-legged","Indoor delivery","Outdoor delivery","Mobile platform","Misc"];
const CAT_COLORS={"AMR":"#2f5bea","AGV":"#7a5af8","Humanoid":"#e04f16","Quadruped":"#16b364","Wheel-legged":"#0ba5ec","Indoor delivery":"#ee46bc","Outdoor delivery":"#eaaa08","Mobile platform":"#8a94a6","Misc":"#667085"};
// ---- theme (set before paint) ----
const THEME=localStorage.getItem("theme")||(matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light");
document.documentElement.dataset.theme=THEME;
function toggleTheme(){const t=document.documentElement.dataset.theme==="dark"?"light":"dark";document.documentElement.dataset.theme=t;localStorage.setItem("theme",t);
 const b=document.getElementById("themeBtn");if(b)b.textContent=t==="dark"?"☀️":"🌙";document.dispatchEvent(new Event("themechange"));}
// ---- language ----
let LANG=localStorage.getItem("lang")||((navigator.language||"").toLowerCase().startsWith("ko")?"ko":"en");if(!I18N[LANG])LANG="en";
document.documentElement.lang=LANG;
function t(k,v){let s=(I18N[LANG]&&I18N[LANG][k])??I18N.en[k]??k;if(v)for(const x in v)s=s.replace("{"+x+"}",v[x]);return s;}
function tv(s){return LANG==="ko"&&VALUE_KO[s]?VALUE_KO[s]:s;} // translate a data value (category, status…)
function setLang(l){localStorage.setItem("lang",l);location.reload();}
function applyI18n(){document.querySelectorAll("[data-i18n]").forEach(e=>e.textContent=t(e.dataset.i18n));document.querySelectorAll("[data-i18n-ph]").forEach(e=>e.placeholder=t(e.dataset.i18nPh));}
document.addEventListener("DOMContentLoaded",applyI18n);
// ---- helpers ----
const FEATURES=[["api_support","api"],["sdk_available","sdk"],["onboard_compute","onboard"],["ros_support","ros"]];
const esc=s=>String(s??"").replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const fmt=(v,u="")=>v===null||v===undefined||v===""?"—":(typeof v==="number"?(+v.toFixed(2)).toLocaleString():esc(v))+(u?` ${u}`:"");
const yn=v=>v===true?`<span class="badge yes">${t("yes")}</span>`:v===false?`<span class="badge no">${t("no")}</span>`:`<span class="badge unk">${t("ns")}</span>`;
const kmh=mps=>mps==null?null:mps*3.6;
const css=n=>getComputedStyle(document.documentElement).getPropertyValue(n).trim();
function nav(on){const links=[["index.html","nav_robots"],["dashboard.html","nav_dash"],["table.html","nav_table"],["specs.html","nav_specs"]];
document.write(`<header class="top"><a class="brand" href="index.html">🤖 ${t("brand")}</a><nav>${links.map(([h,k])=>`<a href="${h}" class="${on===h?"on":""}">${t(k)}</a>`).join("")}</nav>
<div class="tools"><div class="seg">${Object.entries(LANGS).map(([k,l])=>`<button class="${k===LANG?"on":""}" onclick="setLang('${k}')">${l}</button>`).join("")}</div>
<button class="iconbtn" id="themeBtn" title="${t("theme_dark")} / ${t("theme_light")}" onclick="toggleTheme()">${THEME==="dark"?"☀️":"🌙"}</button></div></header>`);}
function footer(meta){return `<footer>${t("footer")} ${meta&&meta.updated?t("updated",{d:esc(meta.updated)}):""}</footer>`}
async function loadData(){return (await fetch("data/robots.json",{cache:"no-cache"})).json();}
// ---- data completeness and per-value provenance (issue #26) ----
// Core fields: the values this catalog keeps for every robot. A core field is a group of record
// keys that count as one: 'dims' needs all three of L/W/H, 'price' is a USD figure or a stated
// price note. Fields that cannot apply to a robot are left out of that robot's denominator, so a
// legged robot is not marked down for having no wheel size: wheel diameter and wheel count apply
// to Wheeled / Tracked / Wheel-legged robots, DoF to Legged / Wheel-legged robots.
const CORE_BASE=[["dims",["length_mm","width_mm","height_mm"]],["weight_kg"],["payload_kg"],["max_speed_mps"],["runtime_h"],["battery_wh"],["ip_rating"],["release_year"],["price",["price_usd","price_note"]],["api_support"],["sdk_available"],["ros_support"],["onboard_compute"],["sensors"]];
const CORE_WHEEL=[["wheel_diameter_mm"],["wheel_count"]];
const CORE_LEG=[["dof"]];
const hasVal=v=>v!==null&&v!==undefined&&!(Array.isArray(v)&&!v.length)&&!(typeof v==="string"&&!v.trim());
function coreFields(r){const f=CORE_BASE.slice(),l=r.locomotion||"";
 if(l==="Wheeled"||l==="Tracked"||l==="Wheel-legged")f.push(...CORE_WHEEL);
 if(l==="Legged"||l==="Wheel-legged")f.push(...CORE_LEG);return f;}
function completeness(r){const f=coreFields(r);let n=0;
 f.forEach(g=>{const keys=g[1]||[g[0]];if(keys.every(k=>hasVal(r[k])))n++;});
 return {n:n,d:f.length,pct:f.length?Math.round(100*n/f.length):0};}
// A value is 'derived' when the record's own note says it was computed rather than stated by the
// maker (e.g. "battery_wh computed from 48V×30Ah"). Only explicit wording counts, so a note that
// merely maps or bounds a value ("runtime_h = lower bound") stays out.
const DERIVED_WORD="(?:computed|derived|calculated)";
function derivedNote(r,key){const n=r.note||"";if(!n||!hasVal(r[key]))return null;
 const a=new RegExp("\\b"+key+"\\b[^.;]{0,24}"+DERIVED_WORD,"i"),b=new RegExp(DERIVED_WORD+"[^.;]{0,24}\\b"+key+"\\b","i");
 const sents=n.split(/[.;]\s+/);
 for(let i=0;i<sents.length;i++)if(a.test(sents[i])||b.test(sents[i]))return sents[i].trim();
 if(key==="battery_wh"){const m=n.match(new RegExp("[^.;]{0,60}[\\d.,]+\\s*Wh\\s*"+DERIVED_WORD,"i"));if(m)return m[0].trim().replace(/^[,;]\s*/,"");}
 return null;}
// Provenance of one value, from what the data records: a derivation note in the record wins, then
// the record's `verification` (official = checked against a maker source). No per-value provenance
// field exists in the data yet, so the record-level check is the basis -- and an unchecked record
// (verification null) is shown as unconfirmed rather than silently promoted.
function provenance(r,fields){const fs=Array.isArray(fields)?fields:[fields];
 for(let i=0;i<fs.length;i++){const s=derivedNote(r,fs[i]);if(s)return {l:"derived",why:t("pv_derived_t",{n:s})};}
 if(r.verification==="official")return {l:"official",why:t("pv_official_t")};
 return {l:"unconfirmed",why:r.verification==="unconfirmed"?t("pv_unconfirmed_t"):t("pv_unchecked_t")};}
function pvBadge(r,fields){const fs=Array.isArray(fields)?fields:[fields];
 if(!fs.some(k=>hasVal(r[k])))return "";
 const p=provenance(r,fs);
 return ` <span class="pv ${p.l}" title="${esc(p.why)}">${t("pv_"+p.l)}</span>`;}
function pvLegend(){return `<div class="pvlegend">${[["official","pv_official_s"],["derived","pv_derived_s"],["unconfirmed","pv_unconfirmed_s"]].map(([l,k])=>`<span><span class="pv ${l}">${t("pv_"+l)}</span> ${t(k)}</span>`).join("")}</div>`;}
const makerVerified=r=>r.verification==="official";
