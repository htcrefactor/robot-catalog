# Robot Catalog

Product specs for mobile robots of all kinds — AMRs, AGVs, humanoids, quadrupeds, wheel-legged robots, indoor and outdoor delivery robots, and development platforms — with a page per robot, a dashboard and a mega table.

**Live site:** https://htcrefactor.github.io/robot-catalog/

## Layout
- `data/parts/*.json` — source of truth, one file per category, one record per robot (see `data/SCHEMA.md`)
- `data/robots.json` — merged file the site reads (`python scripts/merge.py`)
- `index.html` (all robots) · `robot.html?id=…` (one robot) · `dashboard.html` (charts) · `table.html` (mega table)

## Data rules
Every number comes from a manufacturer page, datasheet or manual listed in that record's `sources`. Unknown values are `null` and show as "—" or "N/S" (not stated). Nothing is guessed.

## Theme and languages
- Light/dark toggle (🌙/☀️) in the header; follows the system setting until changed, then remembered.
- UI in English and Korean (EN/KR switch). Strings live in `assets/i18n.js`: add a language by adding a block with the same keys and listing it in `LANGS`. Category/status/country values are translated via `VALUE_KO`. Robot summaries stay in English unless a record has `summary_ko`.
