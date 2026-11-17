// Cross-catalogue review view — reads research/disagreements.json (built by scripts/build_disagreements.py).
// A maintainer aid: it shows what a competitor catalogue publishes next to our value, plus the conflicts
// our own records already note and the records still unconfirmed. Nothing here writes data.
const RFIELDS = ["height_mm", "width_mm", "length_mm", "weight_kg", "payload_kg", "max_speed_mps",
                 "dof", "runtime_h", "battery_wh", "price_usd", "ip_rating"];
const RUNIT = {height_mm: "mm", width_mm: "mm", length_mm: "mm", weight_kg: "kg", payload_kg: "kg",
               max_speed_mps: "m/s", runtime_h: "h", battery_wh: "Wh", price_usd: "USD"};

function fieldLabel(f) {
  const k = {height_mm: "review_f_height", width_mm: "review_f_width", length_mm: "review_f_length",
             weight_kg: "weight", payload_kg: "payload", max_speed_mps: "max_speed", dof: "dof",
             runtime_h: "runtime", battery_wh: "battery", price_usd: "price", ip_rating: "ip"}[f];
  return k ? t(k) : f;
}

function ourValue(field, v) {
  if (v === null || v === undefined || v === "") return "—";
  if (field === "ip_rating" || field === "dof") return esc(v);
  if (field === "price_usd") return "$" + fmt(Number(v));
  return fmt(Number(v)) + (RUNIT[field] ? " " + RUNIT[field] : "");
}

// The catalogue's own wording first; when it printed another unit, the figure we compared with comes after it.
function theirValue(d) {
  const raw = d.their_text ? esc(d.their_text) : (d.theirs === null || d.theirs === undefined ? "—" : esc(d.theirs));
  if (typeof d.theirs !== "number" || !RUNIT[d.field]) return raw;
  const norm = d.field === "price_usd" ? "$" + fmt(d.theirs) : fmt(d.theirs) + " " + RUNIT[d.field];
  const asTyped = String(d.their_text || "").replace(/[^0-9.]/g, "");
  if (asTyped && Math.abs(parseFloat(asTyped) - d.theirs) < 0.5) return raw;
  return `${raw} <span class="muted small">→ ${norm}</span>`;
}

function matches(rb, f) {
  return !f.q || (rb.manufacturer + " " + rb.name + " " + rb.id).toLowerCase().indexOf(f.q) >= 0;
}

function diffRows(rb, f) {
  const rows = rb.diffs.filter(d => (!f.cat || d.catalog === f.cat) && (!f.field || d.field === f.field) &&
    (f.kind === "all" || d.kind === f.kind));
  rows.sort((a, b) => RFIELDS.indexOf(a.field) - RFIELDS.indexOf(b.field) || a.catalog.localeCompare(b.catalog));
  return rows;
}

function robotHead(rb, extra) {
  return `<summary><a href="robot.html?id=${encodeURIComponent(rb.id)}">${esc(rb.manufacturer)} ${esc(rb.name)}</a>
 <span class="muted small">${extra}</span>${rb.verification === "unconfirmed" ? ` <span class="badge unk">${t("ns")}</span>` : ""}</summary>`;
}

function diffBlock(rb, rows, open) {
  const n1 = rows.filter(d => d.kind === "differs").length, n2 = rows.length - n1;
  const counts = [n1 ? `<span class="badge no" title="${t("review_kind_differs")}">≠ ${n1}</span>` : "",
                  n2 ? `<span class="badge unk" title="${t("review_kind_missing")}">— ${n2}</span>` : ""].filter(Boolean).join(" ");
  return `<details class="panel rv"${open ? " open" : ""}>${robotHead(rb, counts)}
 <table class="fs">${rows.map(d => `<tr>
  <td>${esc(fieldLabel(d.field))}</td>
  <td class="num">${ourValue(d.field, d.ours)}</td>
  <td>${d.kind === "differs" ? '<span class="badge no">≠</span> ' : ""}${theirValue(d)}
   <div class="small"><a href="${esc(d.url)}" target="_blank" rel="noopener">${esc(d.catalog)} ${t("review_page_link")}</a>
   ${d.source ? ` · <a href="${esc(d.source)}" target="_blank" rel="noopener">${t("review_source")}</a>` : ""}</div></td>
  </tr>`).join("")}</table></details>`;
}

function conflictBlock(rb, open) {
  const dupes = rb.spec_dupes || [];
  const head = `${dupes.length ? `<span class="badge no">${dupes.length} ${t("review_spec_dupes")}</span>` : ""}`;
  return `<details class="panel rv"${open ? " open" : ""}>${robotHead(rb, head)}
 ${rb.note ? `<p class="small"><b>${t("review_note")}</b> ${esc(rb.note)}</p>` : ""}
 ${dupes.length ? `<table class="fs">${dupes.map(dp => `<tr>
   <td>${esc(dp.label)}</td>
   <td>${dp.values.map(v => `${esc(v.value)}${v.unit ? " " + esc(v.unit) : ""}${v.note ? ` <span class="muted small">(${esc(v.note)})</span>` : ""}${v.source ? ` <a class="small" href="${esc(v.source)}" target="_blank" rel="noopener">↗</a>` : ""}`).join("<br>")}</td>
  </tr>`).join("")}</table>` : ""}</details>`;
}

function unconfirmedBlock(rb, open) {
  return `<details class="panel rv"${open ? " open" : ""}>${robotHead(rb, `${rb.sources_n || 0} ${t("review_sources_n")}`)}
 <p class="small muted">${t("review_unconfirmed_why")}</p></details>`;
}

function renderReview(data, f) {
  const robots = (data.robots || data).filter(rb => matches(rb, f));
  const out = {differs: [], conflicts: [], unconfirmed: []};
  const withDiffs = robots.filter(rb => diffRows(rb, f).length).map(rb => ({rb, rows: diffRows(rb, f)}));
  out.differs = withDiffs.length
    ? withDiffs.map(x => diffBlock(x.rb, x.rows, withDiffs.length <= 3)).join("")
    : `<p class="muted">${t("review_none")}</p>`;
  const conflicts = robots.filter(rb => rb.note || (rb.spec_dupes || []).length);
  out.conflicts = conflicts.length
    ? conflicts.map(rb => conflictBlock(rb, conflicts.length <= 3)).join("")
    : `<p class="muted">${t("review_none")}</p>`;
  const unconf = robots.filter(rb => rb.unconfirmed);
  out.unconfirmed = unconf.length
    ? unconf.map(rb => unconfirmedBlock(rb, unconf.length <= 3)).join("")
    : `<p class="muted">${t("review_none")}</p>`;
  return out;
}

function coverageBlock(data) {
  return `<table class="fs"><tr><th>${t("review_catalog_col")}</th><th>${t("review_listed")}</th><th>${t("review_read")}</th>
  <th>${t("review_no_values")}</th><th>${t("review_divergences")}</th></tr>
  ${data.catalogs.map(c => `<tr><td><a href="${esc(c.url)}" target="_blank" rel="noopener">${esc(c.id)}</a></td>
   <td class="num">${c.listed}</td><td class="num">${c.read}</td><td class="num">${c.unread}</td><td class="num">${c.divergences}</td></tr>`).join("")}</table>`;
}

function startReview() {
  const state = {q: "", cat: "", field: "", kind: "differs"};
  let DATA = null;
  const el = id => document.getElementById(id);
  fetch("research/disagreements.json", {cache: "no-cache"}).then(r => r.json()).then(data => {
    DATA = data;
    el("stats").innerHTML =
      `<div class="stat"><b>${data.scope.robots_with_disagreement}</b>${t("review_robots_with")}</div>` +
      `<div class="stat"><b>${data.summary.differs}</b>${t("review_differs_n")}</div>` +
      `<div class="stat"><b>${data.scope.robots_note_conflict + data.scope.robots_spec_dupes}</b>${t("review_conflicts_n")}</div>` +
      `<div class="stat"><b>${data.scope.robots_unconfirmed}</b>${t("review_unconfirmed_n")}</div>`;
    const cats = data.catalogs.map(c => c.id);
    el("fCat").innerHTML = [""].concat(cats).map(c =>
      `<button class="chip${c === state.cat ? " on" : ""}" data-c="${esc(c)}">${c ? esc(c) : t("all")}</button>`).join(" ");
    el("field").innerHTML = [""].concat(RFIELDS).map(f =>
      `<option value="${f}">${f ? esc(fieldLabel(f)) : t("review_field_col")}</option>`).join("");
    el("fCat").onclick = e => { const b = e.target.closest("button[data-c]"); if (!b) return; state.cat = b.dataset.c; el("fCat").querySelectorAll(".chip").forEach(x => x.classList.toggle("on", x.dataset.c === state.cat)); draw(); };
    el("q").oninput = e => { state.q = e.target.value.toLowerCase(); draw(); };
    el("field").onchange = e => { state.field = e.target.value; draw(); };
    el("kind").onclick = e => { const b = e.target.closest("button[data-k]"); if (!b) return; state.kind = b.dataset.k; el("kind").querySelectorAll("button").forEach(x => x.classList.toggle("on", x.dataset.k === state.kind)); draw(); };
    el("coverage").innerHTML = coverageBlock(data) + `<p class="small muted">${t("review_tolerance")}</p>`;
    draw();
  });
  function draw() {
    const out = renderReview(DATA, state);
    el("diffs").innerHTML = out.differs;
    el("conflicts").innerHTML = out.conflicts;
    el("unconfirmed").innerHTML = out.unconfirmed;
  }
}
if (typeof document !== "undefined" && document.getElementById) document.addEventListener("DOMContentLoaded", startReview);
