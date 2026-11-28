# Gento Robotics (Tianji) Gento Luna

> Gento Robotics' wheeled folding humanoid: a 26-DoF force-controlled body on an omnidirectional four-wheel chassis that folds from 1720 mm to 790 mm for transport.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=gento-robotics-gento-luna
- Category: Humanoid
- Locomotion: Wheeled
- Manufacturer: Gento Robotics (Tianji) (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Height | 1,720 mm |
| Payload | 5 kg |
| Degrees of freedom | 26 |
| Runtime | 4 h |
| Battery | 1,651 Wh |
| SDK | yes |
| SDK name | Gento SDK |
| ROS | ROS 2 |
| On-board compute | NVIDIA Jetson Orin AGX 64GB |
| Compute | up to 275 TOPS |
| Sensors | 3D LiDAR, Ultrasonic radar, Cameras |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Maker page: 26 DoF excluding dexterous hands plus an omnidirectional chassis (in-place rotation, any-direction translation); 1720 mm fully extended, folding to 790 mm; 7-DoF force-controlled arms in three reach options (615/680/750 mm) rated 5/4/3 kg per arm (payload field = 5 kg, the 615 mm option); 48 V 34.4 Ah LiFePO4 pack (=1651 Wh derived); 4-6 h continuous operation (runtime field = lower bound); three charging modes (manual/auto/quick-swap); Jetson Orin AGX 64GB up to 275 TOPS; ROS 2, SDK and secondary-development APIs; active anti-tipping. No price published.

## Sources

- Official page: [gentorobotics.ai](https://gentorobotics.ai/products/gento-luna/)

Listed by these directories (discovery only, never used as a spec source):

- [humanoidversus.com](https://humanoidversus.com/robots/tianji-gento-luna)
- [embodied.guide](https://embodied.guide/robots/gento-robotics-gento-luna/)
- [humanoid.guide](https://humanoid.guide/product/gento-luna/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-28). Source repository: https://github.com/htcrefactor/robot-catalog*
