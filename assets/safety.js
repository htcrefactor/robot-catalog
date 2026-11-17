// Safety & certification helpers (issue #30).
// Everything here is UI-side only: the payload bands and the filter groups are derived from
// `payload_kg` and from the maker-stated `safety_standards` / `certifications` / `safety_pl`
// strings on each record. Nothing in this file is written back into data/parts/*.json.
const PAYLOAD_CLASSES = [
  { id: "p50", max: 50 },
  { id: "p200", max: 200 },
  { id: "p500", max: 500 },
  { id: "p1500", max: 1500 },
  { id: "pinf", max: Infinity },
];
function payloadClassOf(kg) {
  if (kg == null || isNaN(kg)) return "";
  for (const c of PAYLOAD_CLASSES) if (kg <= c.max) return c.id;
  return "pinf";
}
function payloadClassLabel(kg) {
  const id = payloadClassOf(kg);
  if (!id) return "";
  const i = PAYLOAD_CLASSES.findIndex((c) => c.id === id);
  if (i === 0) return `≤ ${PAYLOAD_CLASSES[0].max} kg`;
  const lo = PAYLOAD_CLASSES[i - 1].max;
  return i === PAYLOAD_CLASSES.length - 1 ? `> ${lo} kg` : `${lo}–${PAYLOAD_CLASSES[i].max} kg`;
}

const SAFETY_FILTERS = [
  { id: "iso3691", re: /3691/i },
  { id: "iso13482", re: /13482/i },
  { id: "iso13849", re: /13849/i },
  { id: "pl", test: (r) => !!r.safety_pl },
  { id: "ul3100", re: /UL\s*3100/i },
  { id: "ce", test: (r) => (r.certifications || []).some((c) => /^CE\b/i.test(c)) },
  { id: "fcc", re: /FCC/i },
  { id: "none", test: (r) => !hasSafety(r) },
];

function hasSafety(r) {
  return !!((r.safety_standards || []).length || (r.certifications || []).length || r.safety_pl || r.safety_note);
}
function safetyMatch(r, id) {
  if (!id) return true;
  const f = SAFETY_FILTERS.find((x) => x.id === id);
  if (!f) return true;
  if (f.test) return f.test(r);
  return f.re.test([...(r.safety_standards || []), ...(r.certifications || [])].join(" "));
}
// One short line for a card: certifications first, then performance level, then a standard.
function safetyLine(r) {
  const certs = (r.certifications || []).slice(0, 2);
  const pl = r.safety_pl ? [r.safety_pl] : [];
  const out = [...certs, ...pl];
  if (out.length) return out.join(" · ");
  return (r.safety_standards || []).slice(0, 2).join(" · ");
}
function safetyOptions(sel, withAll) {
  sel.innerHTML =
    `<option value="">${t(withAll)}</option>` +
    SAFETY_FILTERS.map((f) => `<option value="${f.id}">${esc(t("sf_" + f.id))}</option>`).join("");
}
function payloadOptions(sel) {
  sel.innerHTML =
    `<option value="">${t("pc_any")}</option>` +
    PAYLOAD_CLASSES.map((c, i) => {
      const lo = i === 0 ? 0 : PAYLOAD_CLASSES[i - 1].max;
      const label = i === 0 ? `≤ ${c.max} kg` : c.max === Infinity ? `> ${lo} kg` : `${lo}–${c.max} kg`;
      return `<option value="${c.id}">${esc(label)}</option>`;
    }).join("");
}
