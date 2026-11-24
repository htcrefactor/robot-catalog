# ATOMROBOT SkyRise AR-H2

> Wheeled lifting dual-arm humanoid with an 800 mm lift mast that covers low-table assembly to high-rack handling in manufacturing, logistics and service work.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=atomrobot-skyrise-ar-h2
- Category: Humanoid
- Locomotion: Wheeled
- Manufacturer: ATOMROBOT (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 735 mm |
| Width | 644 mm |
| Height | 1,851 mm |
| Weight | 220 kg |
| Payload | 12 kg |
| Max speed | 1.5 m/s (5.4 km/h) |
| Degrees of freedom | 25 |
| Runtime | 4 h |
| API | yes |
| On-board compute | yes |
| Compute | 12-core Arm Cortex-A78AE CPU + 2048-core NVIDIA CUDA GPU |
| Sensors | Depth camera, Multi-line LiDAR, Single-line LiDAR, Ultrasonic radar |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Issue #1 (2026-11-24): 25 DoF (dual 7-DoF force-controlled arms, lifting torso, 4-DoF omnidirectional chassis), 800 mm lift stroke, 686 mm arm reach, 12 kg rated per arm, 1.5 m/s, 220 kg, 735 x 644 x 1,851 mm (zh product list gives height 185.1 cm), 48 V battery with 4-6 h runtime (4 h recorded), 12-core Arm Cortex-A78AE + 2,048-core NVIDIA CUDA GPU, 2 depth cameras + 2 multi-line + 2 single-line LiDAR + 8 ultrasonic radars, 485/24 V end-effector interface. Battery Ah and AI TOPS are not stated, so battery_wh and compute_tops stay empty; the maker does not state availability, so status stays empty.

## Sources

- Official page: [atomrobot.ai](https://www.atomrobot.ai/products/embodied-intelligent-robots/skyrise-ar-h2/)
- [atomrobot.com](https://www.atomrobot.com/robot/163/1881)
- [atomrobot.com](https://www.atomrobot.com/robot/163)

Listed by these directories (discovery only, never used as a spec source):

- [embodied.guide](https://embodied.guide/robots/atomrobot-skyrise-ar-h2/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-24). Source repository: https://github.com/htcrefactor/robot-catalog*
