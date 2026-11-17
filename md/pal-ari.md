# PAL Robotics ARI

> ROS-based wheeled social humanoid with touchscreen, expressive LCD eyes and arms for human-robot interaction research and front-desk service.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=pal-ari
- Category: Humanoid
- Locomotion: Wheeled
- Manufacturer: PAL Robotics (Spain)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 750 mm |
| Width | 530 mm |
| Height | 1,650 mm |
| Payload | 0.5 kg |
| Max speed | 1.5 m/s (5.4 km/h) |
| Degrees of freedom | 14 |
| Runtime | 12 h |
| Battery | 960 Wh |
| Status | Commercial |
| API | yes |
| SDK | yes |
| SDK name | PAL OS / PAL SDK (ROS 2) |
| ROS | yes |
| On-board compute | yes |
| Compute | Intel i5/i7/i9, up to 32 GB RAM; optional NVIDIA Xavier NX or Orin |
| Sensors | 8MP RGB head camera (opt. RGB-D), RealSense D435i torso RGB-D, RealSense T265 back stereo-fisheye, YDLIDAR TG15 (optional), 4-mic array |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Wheeled social humanoid (2-DoF differential base). dims: depth 75 cm per datasheet (73 cm on web page); runtime 8–12 h (max used); dof 14 = 2 head + 2 base + 5×2 arms per datasheet (docs list 4-DoF arms + optional hand); battery_wh computed from 24V×40Ah (60Ah optional)

## Sources

- Official page: [pal-robotics.com](https://pal-robotics.com/robot/ari/)
- [pal-robotics.com](https://pal-robotics.com/wp-content/uploads/2025/02/ARI-Datasheet.pdf)
- [docs.pal-robotics.com](https://docs.pal-robotics.com/25.01/hardware/ari/hardware-overview.html)
- [pal-robotics.com](https://pal-robotics.com/wp-content/uploads/2024/05/Brochure-ARI.pdf)

Listed by these directories (discovery only, never used as a spec source):

- [humanoid.guide](https://humanoid.guide/product/ari/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-16). Source repository: https://github.com/htcrefactor/robot-catalog*
