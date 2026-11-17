# Robot Catalog

Product specs for mobile robots of all kinds — AMRs, AGVs, humanoids, quadrupeds, wheel-legged robots, indoor and outdoor delivery robots, and development platforms — with a page per robot, a dashboard and a mega table.

**Live site:** https://htcrefactor.github.io/robot-catalog/

## Layout
- `data/parts/*.json` — source of truth, one file per category, one record per robot (see `data/SCHEMA.md`)
- `data/robots.json` — merged file the site reads (`python scripts/merge.py`)
- `data/fx.json` — KRW cross rates and their ECB reference date, for the KRW figures (`python scripts/build_fx.py`)
- `index.html` (all robots) · `robot.html?id=…` (one robot) · `dashboard.html` (charts) · `table.html` (mega table)

## Data rules
Every number comes from a manufacturer page, datasheet or manual listed in that record's `sources`, except where noted below. Unknown values are `null` and show as "—" or "N/S" (not stated). Nothing is guessed.

Humanoid prices, delivered prices to the US and Germany, sales status, FCC IDs and public tender prices come from HumanoidStore's open data (https://humanoidstore.co/data, dataset dated 2026-11-04, CC BY 4.0, credit "HumanoidStore (humanoidstore.co)"). 107 humanoids whose only source so far is that dataset carry `"data_source": "HumanoidStore open data (CC BY 4.0)"`; their specs are as HumanoidStore states them, not yet checked against the makers' own pages.

## Prices
A price is stored as a dated observation (`price_observations`): the amount in the currency the maker states, the date it was checked, the kind of price, and the maker or official-store URL — never a competitor, reseller or aggregator. A record can carry several, one per date or variant, and the robot page draws them as a price history.

KRW is not stored anywhere. `data/fx.json` holds KRW per 1 unit for 30 currencies crossed from the European Central Bank's daily reference rates, with the ECB's reference date, and the pages convert at display time so the rate and its date stay next to the figure (`python3 scripts/build_fx.py` refreshes it). A price recorded before dated observations were introduced has no date, so it is shown as stated and **not** converted; those are the only records that still use `price_usd` / `price_note`.

## Theme and languages
- Light/dark toggle (🌙/☀️) in the header; follows the system setting until changed, then remembered.
- UI in English and Korean (EN/KR switch). Strings live in `assets/i18n.js`: add a language by adding a block with the same keys and listing it in `LANGS`. Category/status/country values are translated via `VALUE_KO`. Robot summaries stay in English unless a record has `summary_ko`.
