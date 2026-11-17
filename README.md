# Robot Catalog

Product specs for mobile robots of all kinds — AMRs, AGVs, humanoids, quadrupeds, wheel-legged robots, indoor and outdoor delivery robots, and development platforms — with a page per robot, a dashboard and a mega table.

**Live site:** https://htcrefactor.github.io/robot-catalog/

## Layout
- `data/parts/*.json` — source of truth, one file per category, one record per robot (see `data/SCHEMA.md`)
- `data/robots.json` — merged file the site reads (`python scripts/merge.py`)
- `index.html` (all robots) · `robot.html?id=…` (one robot) · `dashboard.html` (charts) · `table.html` (mega table)

## Data rules
Every number comes from a manufacturer page, datasheet or manual listed in that record's `sources`, except where noted below. Unknown values are `null` and show as "—" or "N/S" (not stated). Nothing is guessed.

Humanoid prices, delivered prices to the US and Germany, sales status, FCC IDs and public tender prices come from HumanoidStore's open data (https://humanoidstore.co/data, dataset dated 2026-11-04, CC BY 4.0, credit "HumanoidStore (humanoidstore.co)"). 107 humanoids whose only source so far is that dataset carry `"data_source": "HumanoidStore open data (CC BY 4.0)"`; their specs are as HumanoidStore states them, not yet checked against the makers' own pages.

## Safety & certifications
AMR, AGV, delivery and mobile-platform records carry the safety profile their maker states: `safety_standards` (e.g. ISO 3691-4, EN ISO 13849-1), `certifications` (CE, UL 3100, FCC, KC, KIRIA …), `safety_pl` (PL d, SIL 2), a `safety_note` for exclusions or an explicit absence of certification, and the maker URL that states them in `safety_source` (see `data/SCHEMA.md`). The robot list and mega table filter on them and the robot page shows them next to the IP rating. The payload class (≤50 / 50–200 / 200–500 / 500–1500 / >1500 kg) is a display band derived from `payload_kg`, not a stored field.

## Theme and languages
- Light/dark toggle (🌙/☀️) in the header; follows the system setting until changed, then remembered.
- UI in English and Korean (EN/KR switch). Strings live in `assets/i18n.js`: add a language by adding a block with the same keys and listing it in `LANGS`. Category/status/country values are translated via `VALUE_KO`. Robot summaries stay in English unless a record has `summary_ko`.
