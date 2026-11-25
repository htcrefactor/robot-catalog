# Corenetic Monte01

> Corenetic's wheeled two-arm humanoid on a two-wheel differential base, aimed at laboratory automation, logistics and caregiving work.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=corenetic-monte01
- Category: Humanoid
- Locomotion: Wheeled
- Manufacturer: Corenetic (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 600 mm |
| Width | 650 mm |
| Height | 1,530 mm |
| Weight | 120 kg |
| Payload | 3.5 kg |
| Max speed | 1 m/s (3.6 km/h) |
| Degrees of freedom | 25 |
| Runtime | 8 h |
| Battery | 1,536 Wh |
| Status | Commercial |
| On-board compute | yes |
| Compute | Embedded AI processor 200+ TOPS plus an x86 industrial real-time control board |
| Sensors | 1 RGBD camera (head), 2 RGBD cameras (arm ends) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Maker spec slide linked from corenetic.ai/en/product (cdn.yuanluo.cloud/.../monte_01_params.webp, read 2026-11-17): dimensions 600 x 650 x 1530 mm, 120 kg, 25 DoF with the two-finger grippers (base 2 + waist 3 + head 2 + arms 7x2 + grippers 2x2; with two 9-DoF dexterous hands it is 39), 700 mm arm length, 3.5 kg max per arm at the end flange (payload_kg = per-arm figure), two-wheel differential drive at 1.0 m/s max on indoor floors with slope <=10 deg, 51.2 V / 30 Ah battery (battery_wh = 51.2x30 = 1536 Wh, computed), 8 h typical runtime and 4 h charge, 200+ TOPS embedded AI processor plus x86 industrial real-time control board, 1 head RGBD camera and 2x1 RGBD cameras at the arm ends, Wi-Fi 6 / gigabit Ethernet / full Type-C. Maker's slide carries a disclaimer that the figures are lab measurements for reference only.

## Sources

- Official page: [corenetic.ai](https://www.corenetic.ai/en/product)
- [cdn.yuanluo.cloud](https://cdn.yuanluo.cloud/corenetic_original/assets/webp/monte_01_params.webp)

Listed by these directories (discovery only, never used as a spec source):

- [embodied.guide](https://embodied.guide/robots/corenetic-monte01/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-24). Source repository: https://github.com/htcrefactor/robot-catalog*
