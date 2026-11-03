const CATS=["AMR","AGV","Humanoid","Quadruped","Wheel-legged","Indoor delivery","Outdoor delivery","Mobile platform"];
const CAT_COLORS={"AMR":"#2f5bea","AGV":"#7a5af8","Humanoid":"#e04f16","Quadruped":"#16b364","Wheel-legged":"#0ba5ec","Indoor delivery":"#ee46bc","Outdoor delivery":"#eaaa08","Mobile platform":"#8a94a6"};
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
