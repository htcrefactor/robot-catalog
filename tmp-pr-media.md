## What this does

The 2026-11-20 ~ 11-25 media window produced no robot that is both missing from the catalog and documented by its maker. The one genuinely new launch — NOETIX **Boomy** — is the international edition of a robot already carried as `noetix-bumi`, so it is folded in as a `variants` entry and the record is updated from Noetix's own launch material. **Robot count: 1,004 → 1,004** (no record added, removed or moved).

## Candidates checked

| Candidate | Report | Result |
|---|---|---|
| NOETIX **Boomy** | 2026-11-24 Noetix press release (Newswire), Kickstarter launch | Same machine as `noetix-bumi` (Bumi is the China name, Boomy the international/Kickstarter edition — confirmed by the maker's own product pages and by two independent humanoid trackers). Folded into `variants`, record updated |
| Topstar **Star** | TOPS DAY 2026, 2026-11-07/08 (reported 11-20~11-21 in Chinese and English media) | Already `topstar-star`, `verification: official`, specs from the same event; nothing new to add |
| Topstar **Xiaotuo** | Same event | Already `topstar-xiao-tuo`, `verification: official`; nothing new to add |
| T-Robotics **TR-WORKS** | 2026-11-25 Asia Economy / SK Securities note | Already `t-robotics-tr-works`; the broker note gives different figures → recorded in `note`, fields unchanged |

## `noetix-bumi` — what changed

Official sources opened: Noetix's Boomy product page, the 2026-11-24 Noetix release on Newswire, the maker-run Kickstarter campaign page (read directly), and the maker's existing Bumi page.

- `variants` — new entry `noetix-boomy`, "Boomy (international edition)", with the note that it is the same 21-DoF body and that the Boomy pages say 97 cm / 1 m/s / 2-3 h while the China Bumi page says 98 cm / 0.5 m/s / up to 3 h.
- **Fields kept, not overwritten:** `height_mm` 980 and `max_speed_mps` 0.5 stay as the maker's China Bumi page states them; the Boomy launch figures are in `note` (`AGENTS.md` §3 — keep the maker value, record the other in notes).
- Filled from the Boomy pages: `api_support` true, `sdk_available` true, `sdk_name` "Noetix Boomy open SDK", `sdk` {Python, C++, url = Boomy page; licence/open-source not stated → null}, `ros_support` true (ROS 2 stated; no package URL published, so `ros2_*` stays null), `onboard_compute` true, `compute_detail`/`compute_soc` "NVIDIA Jetson Orin NX (Boomy EDU)", `compute_tops` 117, `compute_source` = the maker release; `sensors` = RGB camera, RealSense D435i (EDU), microphone array, speaker.
- **Prices (dated observations, 2026-11-24):** Boomy Standard MSRP **US$5,899** and EDU MSRP **US$9,999**, source = the maker-run Kickstarter campaign (which states both MSRPs); each observation's note records the super early bird pledge (US$3,599 / US$5,999) and that delivery is estimated from Jan 2027. The legacy `price_note` was cleared as `validate.py` requires once observations exist; the Chinese price (CNY 9,998, JD Noetix flagship store) is stated in `note` and deliberately not turned into an observation, because no page was opened that states it on the date.
- `summary`, `official_url` (now the Bumi page) and `sources` updated.

## `t-robotics-tr-works` — what changed

`note` and `sources` only. A 2026-11-25 SK Securities note (Asia Economy) reports 140 cm, 131 kg, 30 kg payload and 8 h of work on the AMR battery, plus a CES 2027 North American debut and supply from 2027. These are broker figures, not maker statements, so the fields keep the company's own Automation World 2026 values (180 cm, 180 kg, 3 kg, 20 DoF) and the difference is written into `note`; the 30 kg matches the company's stated plan to raise payload to 20-30 kg.

## Checks

- `python3 scripts/build_fx.py` → ECB 2026-11-24, US$1 = KRW 1,344.5134 (`data/fx.json` committed)
- `python3 scripts/merge.py --notes "Media sweep 2026-11-25: …"` → 1,004 robots, 2 changed, history + feed updated
- `python3 scripts/build_sitemap.py` → 1,010 URLs; `python3 scripts/build_llms.py` → md/ for 1,004 robots
- `python3 scripts/validate.py` → **1,004 robots checked, 0 problems** (only the pre-existing `manufacturer_ko` warnings)

Closes #82
