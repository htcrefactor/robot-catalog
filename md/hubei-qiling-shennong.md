# Hubei Qiling Robotics Shennong

> Hubei Qiling's Shennong industrial biped (1.75 m, 43 DoF) built on an RL+MPC whole-body controller for logistics, inspection and education.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=hubei-qiling-shennong
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: Hubei Qiling Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Height | 1,750 mm |
| Weight | 55 kg |
| Max speed | 2 m/s (7.2 km/h) |
| Degrees of freedom | 43 |
| Runtime | 2 h |
| SDK | yes |
| SDK name | Shennong SDK (ROS / Python / C++) |
| ROS | ROS |
| On-board compute | NVIDIA AGX Orin or Orin NX |
| Compute | module-level, TOPS not stated |
| Sensors | LiDAR, RGB-D camera |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Maker's own exhibit entry and product brochure (WRC 2026): 175 cm, 55 kg, up to 43 whole-body DoF (7 per arm = 3 shoulder + 1 elbow + 3 wrist, 6 per leg), self-developed high torque-density motors (200 N.m/kg peak), 2.0 m/s navigation and 6 km continuous running, about 2 h endurance, LiDAR + RGB-D perception, AGX Orin / Orin NX compute, open SDK supporting ROS/Python/C++, RL+MPC fused controller, voice interaction. Company founded 2025 with Huazhong University of Science and Technology ties. No price published.

## Sources

- Official page: [wrc.cie.org.cn](https://wrc.cie.org.cn/expo/product/1392.html)
- [wrc.cie.org.cn](https://wrc.cie.org.cn/profile/robot/download/2026/07/30/20260730123237000308_20260730123237A012.pdf)

Listed by these directories (discovery only, never used as a spec source):

- [embodied.guide](https://embodied.guide/robots/hubei-qiling-shennong/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-20). Source repository: https://github.com/htcrefactor/robot-catalog*
