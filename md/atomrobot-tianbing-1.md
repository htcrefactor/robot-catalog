# ATOMROBOT Tianbing-1

> Wheeled industrial humanoid with a Stewart parallel waist (200 kg waist load) and 7-axis force-controlled arms for heavy handling and precision assembly.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=atomrobot-tianbing-1
- Category: Humanoid
- Locomotion: Wheeled
- Manufacturer: ATOMROBOT (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Height | 1,750 mm |
| Weight | 200 kg |
| Payload | 12.5 kg |
| Max speed | 1.25 m/s (4.5 km/h) |
| Degrees of freedom | 26 |
| Runtime | 4 h |
| Released | 2025 |
| Status | Commercial |
| API | yes |
| On-board compute | yes |
| Compute | 170 TOPS module: 12-core Arm Cortex-A78AE + 2048-core NVIDIA CUDA GPU |
| Sensors | Depth camera, Multi-line LiDAR, IMU |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Variants

- **SkyBot AR-H1** — English product name of the same robot as Tianbing-1 (天兵一号, model code AR-H1). Folded into this record on 2026-11-24; not a separate model. ([maker page](https://www.atomrobot.ai/products/embodied-intelligent-robots/skybot-ar-h1/))

## Notes

Model code AR-H1 / ATOM01 ('天兵一号'). Wheeled omnidirectional base with Stewart parallel waist. First 2025 version was 140 cm/70 kg/37 DoF; Dec 2025 update 27 DoF; current product page 26 DoF — values below from current page. Maker: Tianjin Atom Robotics (ATOMROBOT). spec: height 165–175 cm (max used); payload 12.5 kg per arm; api_support from 'open full secondary-development interface'; status Commercial per official 'external sales' statement (May 2026) | Issue #1 (2026-11-24): ATOMBOT's English AR-H1 page (same robot, 'SkyBot AR-H1') gives 26 DoF (dual 7-DoF arms, 2-DoF neck, 6-DoF Stewart waist, 4-DoF chassis), 12.5 kg per arm, 686 mm reach, 170 TOPS and 4 h runtime (runtime added here). It also states a 180 kg body weight while the Chinese product list gives 200 kg for the same model; the 200 kg value is kept and the conflict recorded. The duplicate record atomrobot-skybot-ar-h1 was folded into this record's variants (count -1).

## Sources

- Official page: [atomrobot.ai](https://www.atomrobot.ai/products/embodied-intelligent-robots/skybot-ar-h1/)
- [atomrobot.com](https://www.atomrobot.com/product/163)
- [atomrobot.com](https://www.atomrobot.com/detail/16/1900)
- [atomrobot.com](https://www.atomrobot.com/detail/16/1771)
- [atomrobot.com](https://www.atomrobot.com/detail/16/1430)
- [atomrobot.ai](https://www.atomrobot.ai/products/embodied-intelligent-robots)

Listed by these directories (discovery only, never used as a spec source):

- [humanoidversus.com](https://humanoidversus.com/robots/atomrobot-tianbing-1)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-24). Source repository: https://github.com/htcrefactor/robot-catalog*
