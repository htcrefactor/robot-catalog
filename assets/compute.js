// Chip families for the structured compute fields (Issue #28).
// compute_soc keeps the maker's own wording (e.g. "NVIDIA Jetson AGX Orin 32GB", "AGX Orin"), and
// this table groups those wordings into chips for the filter and chips.html.
// The grouping lives here, not in the data; nothing in it scores or ranks robots.
const CHIP_FAMILIES=[
 {id:"jetson-thor",label:"NVIDIA Jetson Thor",re:/jetson\s*thor|thor\s*t\d{3,4}|nvidia\s+thor|jetson\s+t\d{3,4}/i},
 {id:"jetson-orin-nx",label:"NVIDIA Jetson Orin NX",re:/orin\s*nx/i,parent:"jetson-orin"},
 {id:"jetson-orin-nano",label:"NVIDIA Jetson Orin Nano",re:/orin\s*nano/i,parent:"jetson-orin"},
 {id:"jetson-agx-orin",label:"NVIDIA Jetson AGX Orin",re:/agx\s*orin|orin\s*agx/i,parent:"jetson-orin"},
 {id:"jetson-orin",label:"NVIDIA Jetson Orin",re:/jetson\s*orin|\borin\b/i},
 {id:"jetson-xavier-nx",label:"NVIDIA Jetson Xavier NX",re:/xavier\s*nx/i,parent:"jetson-xavier"},
 {id:"jetson-agx-xavier",label:"NVIDIA Jetson AGX Xavier",re:/agx\s*xavier/i,parent:"jetson-xavier"},
 {id:"jetson-xavier",label:"NVIDIA Jetson Xavier",re:/\bxavier\b/i},
 {id:"jetson-nano",label:"NVIDIA Jetson Nano",re:/jetson\s*nano/i},
 {id:"nvidia-rtx",label:"NVIDIA RTX GPU",re:/rtx\s*\d{3,4}/i},
 {id:"rockchip-rk3588",label:"Rockchip RK3588",re:/rk\s*-?\s*3588/i},
 {id:"raspberry-pi",label:"Raspberry Pi",re:/raspberry\s*pi|\bcm4\b/i},
 {id:"esp32",label:"Espressif ESP32",re:/esp32/i},
 {id:"intel-core-ultra",label:"Intel Core Ultra",re:/core\s*ultra/i,parent:"intel-x86"},
 {id:"intel-x86",label:"Intel x86 CPU",re:/\bintel\b|\bnuc\b|core\s*i[3579]\b/i},
 {id:"amd-x86",label:"AMD x86 CPU",re:/ryzen|\bamd\b|\be-450\b/i}
];
const CHIP_BY_ID=Object.fromEntries(CHIP_FAMILIES.map(f=>[f.id,f]));
function chipIds(r){
 const s=(r&&r.compute_soc)||"";if(!s)return [];
 const hit=CHIP_FAMILIES.filter(f=>f.re.test(s));
 // a named variant wins over its family ("Orin NX" over "Jetson Orin"), so a chip filter is precise
 const parents=new Set(hit.map(f=>f.parent).filter(Boolean));
 return hit.filter(f=>!parents.has(f.id)).map(f=>f.id);
}
function chipLabel(id){return CHIP_BY_ID[id]?CHIP_BY_ID[id].label:id;}
const hasCompute=r=>!!(r&&(r.compute_soc||r.compute_tops!=null||r.compute_memory_gb!=null));
const topsText=(r,unit="TOPS")=>r&&r.compute_tops!=null?`${fmt(r.compute_tops)}${r.compute_tops_precision?` ${esc(r.compute_tops_precision)}`:""} ${unit}`:"";
