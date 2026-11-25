## Scope

Verify 12 records that still carry `verification: null`, against each maker's own site, datasheet, manual or press release. Records already handled by open PR #76 (the last 9 of issue #1) or #78 are excluded; issue #1's remaining scope is closed by #76.

Batch (2026-11-25):

| # | id | Category | Maker |
|---|---|---|---|
| 1 | `irobot-create-3` | Mobile platform | iRobot |
| 2 | `petoi-quaddle` | Quadruped | Petoi |
| 3 | `yahboom-dogzilla-s2` | Quadruped | Yahboom |
| 4 | `ogadjet-xgo-rider2` | Wheel-legged | Ogadjet (XGO) |
| 5 | `robotnik-rb-watcher` | AMR | Robotnik |
| 6 | `pal-stockbot` | AMR | PAL Robotics |
| 7 | `bear-robotics-servi` | Indoor delivery | Bear Robotics |
| 8 | `pudu-bellabot-pro` | Indoor delivery | Pudu Robotics |
| 9 | `temi-v3` | Indoor delivery | temi |
| 10 | `keenon-t5` | Indoor delivery | KEENON Robotics |
| 11 | `simbe-tally-4` | AMR | Simbe Robotics |
| 12 | `isento-pib-pro` | Humanoid | isento |

## Rules

- Specs from maker sources only (`AGENTS.md` §3); unknown stays `null`.
- `verification: official` when a maker document states the values, `unconfirmed` when no maker source exists for the record.
- Every changed record lists the URLs actually opened in `sources`.
- Generated files rebuilt with `merge.py`, `build_sitemap.py`, `build_llms.py`, `validate.py`; robot count before/after in the PR.
