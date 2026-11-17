// Dated price observations, KRW conversion and the price-history chart (Issue #31).
// A record's `price_observations` is the only price the site converts: the amount in the currency
// the maker states, the date it was checked, and the maker / official-store URL behind it. No KRW
// figure is ever stored in the data — the page converts at run time with data/fx.json (ECB daily
// reference rates) so the rate and its date stay visible next to the number. Records that still
// carry the older price_usd / price_note fields are shown as "recorded price (undated)".
var PRICE_KINDS = ["list", "from", "rental", "edu"];
var CUR_SIGN = {USD: "$", KRW: "₩", EUR: "€", CNY: "CN¥", JPY: "¥", GBP: "£", CHF: "CHF ", TWD: "NT$", HKD: "HK$", SGD: "S$", AUD: "A$", CAD: "C$", SEK: "SEK ", NOK: "NOK ", DKK: "DKK ", PLN: "PLN ", INR: "₹", BRL: "R$", ILS: "₪"};

var obsList = r => ((r && r.price_observations) || []).slice().sort((a, b) => (a.date < b.date ? -1 : a.date > b.date ? 1 : 0));
var kindText = k => t("kind_" + k);
// grouping done here rather than through toLocaleString, so the same figure reads the same in every browser
var numText = a => { const n = Math.round((+a) * 100) / 100; const s = String(n).split("."); return s[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",") + (s[1] ? "." + s[1] : ""); };
var money = (a, c) => { const s = CUR_SIGN[c] || ""; const n = numText(a); return s ? s + n : n + " " + (c || ""); };
var krwText = v => v == null ? "—" : "₩" + numText(Math.round(v));
var fxRate = (cur, fx) => cur === "KRW" ? 1 : (fx && fx.rates && fx.rates[cur] != null ? fx.rates[cur] : null);
var obsKrw = (o, fx) => { const rt = fxRate(o.currency, fx); return rt == null ? null : o.amount * rt; };

// the headline price: the latest date, and on that date the "from" price first, then a list price, then a rental, then an education price
var markOrder = k => { const i = ["from", "list", "rental", "edu"].indexOf(k); return i < 0 ? 9 : i; };
function obsSameDate(r) {
  const O = obsList(r); if (!O.length) return [];
  const d = O[O.length - 1].date;
  return O.filter(o => o.date === d);
}
function latestObs(r) {
  const same = obsSameDate(r).slice().sort((a, b) => markOrder(a.kind) - markOrder(b.kind) || a.amount - b.amount);
  return same[0] || null;
}

async function loadFx() {
  try { const res = await fetch("data/fx.json", {cache: "no-cache"}); if (!res.ok) return null; const j = await res.json(); return j && j.rates ? j : null; }
  catch (e) { return null; }
}

// "US$1 = ₩1,334.87 · ECB reference rate 2026-11-16"
function fxNote(fx) {
  if (!fx) return t("price_fx_missing");
  const usd = fx.rates.USD;
  return t("price_fx", {d: fx.date, r: usd == null ? "—" : numText(usd)});
}

// A price in the three shapes the site needs: the native amount, the KRW figure and (when the
// native amount is not in USD) the USD figure.
function priceText(o, fx) {
  if (!o) return "—";
  const krw = obsKrw(o, fx);
  const usd = fxRate("USD", fx);
  const usdAmt = o.currency === "USD" ? o.amount : (krw != null && usd != null ? krw / usd : null);
  return `${krwText(krw)} <span class="muted small">(${money(o.amount, o.currency)}${usdAmt != null && o.currency !== "USD" ? " · " + money(usdAmt, "USD") : ""} · ${esc(kindText(o.kind))} · ${esc(o.date)})</span>`;
}

// Price-history chart: one point per observation, y in KRW, x by date (dates are the categories so
// a single date still reads). A rental point is drawn hollow because it is a rate, not a sale price.
function priceChart(r, fx) {
  const seq = obsList(r).map(o => ({o, krw: obsKrw(o, fx)})).filter(p => p.krw != null);
  if (seq.length < 2) return "";
  const W = 720, H = 210, L = 78, R = 18, T = 18, B = 34;
  const dates = [...new Set(seq.map(p => p.o.date))].sort();
  const x = d => dates.length === 1 ? (L + (W - L - R) / 2) : L + dates.indexOf(d) * (W - L - R) / (dates.length - 1);
  const vs = seq.map(p => p.krw), lo = Math.min(...vs), hi = Math.max(...vs);
  const pad = (hi - lo) * 0.15 || Math.abs(hi) * 0.1 || 1, y0 = lo - pad, y1 = hi + pad;
  const y = v => T + (H - T - B) - (v - y0) / (y1 - y0) * (H - T - B);
  const grid = [0, 0.5, 1].map(f => { const v = y0 + (y1 - y0) * f; return `<line class="grid" x1="${L}" x2="${W - R}" y1="${y(v).toFixed(1)}" y2="${y(v).toFixed(1)}"/><text class="tick" x="${L - 6}" y="${(y(v) + 3).toFixed(1)}" text-anchor="end">${krwText(v)}</text>`; }).join("");
  const single = dates.every(d => seq.filter(p => p.o.date === d).length === 1);
  const line = single && seq.length > 1 ? `<polyline fill="none" stroke="var(--accent)" stroke-width="2" points="${seq.map(p => `${x(p.o.date).toFixed(1)},${y(p.krw).toFixed(1)}`).join(" ")}"/>` : "";
  const dots = seq.map(p => `<circle cx="${x(p.o.date).toFixed(1)}" cy="${y(p.krw).toFixed(1)}" r="4.5" fill="${p.o.kind === "rental" ? "none" : "var(--accent)"}" stroke="var(--accent)" stroke-width="2"><title>${esc(p.o.date)} · ${esc(kindText(p.o.kind))} · ${esc(money(p.o.amount, p.o.currency))} = ${krwText(p.krw)}</title></circle>`).join("");
  const xl = dates.map(d => `<text class="tick" x="${x(d).toFixed(1)}" y="${H - 10}" text-anchor="middle">${esc(d)}</text>`).join("");
  return `<svg viewBox="0 0 ${W} ${H}" class="chart" role="img" aria-label="${esc(t("price_history"))}">${grid}${line}${dots}${xl}<text class="tick" x="${L - 6}" y="${T - 6}" text-anchor="end">${t("price_krw")}</text></svg>`;
}

// The whole price panel for one robot page.
function pricePanel(r, fx) {
  const O = obsList(r);
  const head = O.length
    ? `<h2>${t("price_history")} <span class="muted small">${O.length === 1 ? t("price_obs_1") : t("price_obs_n", {n: O.length})}</span></h2>`
    : `<h2>${t("price")}</h2>`;
  if (!O.length) {
    const legacy = r.price_usd != null
      ? `<p>${money(r.price_usd, "USD")} <span class="muted small">${t("price_legacy")}</span></p>`
      : (r.price_note ? `<p class="small">${esc(r.price_note)} <span class="muted small">${t("price_legacy")}</span></p>` : `<p class="muted">${t("price_no_obs")}</p>`);
    return `<div class="panel">${head}${legacy}${r.price_usd != null || r.price_note ? `<p class="small muted">${t("price_legacy_why")}</p>` : ""}</div>`;
  }
  const last = latestObs(r), same = obsSameDate(r);
  const others = same.filter(o => o !== last);
  const rows = O.slice().reverse().map(o => {
    const k = obsKrw(o, fx);
    return `<tr><td>${esc(o.date)}</td><td>${esc(kindText(o.kind))}</td><td class="num">${money(o.amount, o.currency)}${o.note ? `<div class="small muted">${esc(o.note)}</div>` : ""}</td><td class="num">${k == null ? "—" : krwText(k)}</td><td class="small"><a href="${esc(o.source)}" target="_blank" rel="noopener">${esc(host(o.source))}</a></td></tr>`;
  }).join("");
  const otherLine = others.length
    ? `<p class="small">${t("price_same_date", {d: last.date})} ` + others.map(o => `${money(o.amount, o.currency)} <span class="muted">(${esc(kindText(o.kind))})</span>`).join(" · ") + `</p>` : "";
  const missing = O.filter(o => obsKrw(o, fx) == null).map(o => esc(o.currency));
  const headline = obsKrw(last, fx) == null ? money(last.amount, last.currency) : krwText(obsKrw(last, fx));
  return `<div class="panel">${head}
<p style="font-size:24px;font-weight:650;margin:2px 0 4px">${headline}</p>
<p class="small">${money(last.amount, last.currency)} <span class="muted">${esc(kindText(last.kind))} · ${esc(last.date)}</span> · <a href="${esc(last.source)}" target="_blank" rel="noopener" class="small">${esc(host(last.source))} ↗</a></p>
${last.note ? `<p class="small muted">${esc(last.note)}</p>` : ""}
${otherLine}
${priceChart(r, fx)}
<table class="fs"><tbody>${rows}</tbody></table>
<p class="small muted">${fxNote(fx)}${missing.length ? ` ${t("price_no_rate", {c: [...new Set(missing)].join(", ")})}` : ""}</p>
<p class="small muted">${t("price_rules")}</p></div>`;
}
