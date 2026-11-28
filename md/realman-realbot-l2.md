# RealMan Robotics RealBot-L2

> RealMan's full-size wheeled dual-arm lift humanoid: 17 active DOF, a 300 mm lift that reaches 0-2.1 m, 5 kg per arm and about 6 h of running time for home service, retail and data collection.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=realman-realbot-l2
- Category: Humanoid
- Locomotion: Wheeled
- Manufacturer: RealMan Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 650 mm |
| Width | 512 mm |
| Height | 1,700 mm |
| Weight | 120 kg |
| Payload | 5 kg |
| Max speed | 1 m/s (3.6 km/h) |
| Degrees of freedom | 17 |
| Runtime | 6 h |
| Battery | 960 Wh |
| Status | Commercial |
| SDK | yes |
| SDK name | Teaching pendant, local and remote teleoperation |
| On-board compute | NVIDIA Jetson AGX Orin 64G (D-Robotics S100 optional) |
| Sensors | Stereo RGB head camera (depth optional), RGBD hand cameras (mono RGB optional) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Maker product page (opened 2026-11-17): full-size wheeled dual-arm lift humanoid, 17 active DoF, 0-2.1 m vertical working range, 300 mm lift travel, 5 kg payload per arm, two-wheel differential chassis, 48 V 20 Ah / ~6 h, 650x512x1700 mm, ~120 kg, Jetson AGX Orin 64G (D-Robotics S100 option). Locomotion confirmed WHEELED (two-wheel differential chassis). Numeric spec fields left for the thin-record batch (issue #15). | Maker product page and developer docs: 650 x 512 x 1,700 mm, about 120 kg, 17 active DOF, 5 kg per arm, vertical working range 0-2.1 m, 300 mm lift stroke, lift capacity >=60 kg including arms and payload, 0.1-1.0 m/s, Jetson AGX Orin 64G (or D-Robotics S100), stereo RGB head camera with optional depth, RGBD hand cameras, 2-finger gripper or 5-finger hand quick-swap, two-wheel differential chassis, 48 V 20 Ah battery (=960 Wh, derived from V x Ah; the maker states only 48 V 20 Ah), about 6 h typical runtime with about 1 h full charge, wired and Wi-Fi (5G optional on S2). Per-arm 7 DOF.

## Sources

- Official page: [realman-robotics.com](https://www.realman-robotics.com/en/products/realbot-l2.html)
- [develop.realman-robotics.com](https://develop.realman-robotics.com/en/wheelRobot/RealBotL2/)

Listed by these directories (discovery only, never used as a spec source):

- [humanoidversus.com](https://humanoidversus.com/robots/realman-realbot-l2)
- [embodied.guide](https://embodied.guide/robots/realman-realbot-l2/)
- [humanoid.guide](https://humanoid.guide/product/realbot-l2/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-28). Source repository: https://github.com/htcrefactor/robot-catalog*
