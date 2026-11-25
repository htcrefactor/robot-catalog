# BXI Robotics Elf 3

> BXI Robotics' 1.45 m research humanoid with 31 DoF, a ROS2 SDK and MuJoCo simulation, built around the company's own hollow-shaft joint motors.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=bxi-robotics-elf-3
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: BXI Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 280 mm |
| Width | 450 mm |
| Height | 1,450 mm |
| Weight | 38 kg |
| Payload | 5 kg |
| Max speed | 5 m/s (18.0 km/h) |
| Degrees of freedom | 31 |
| Runtime | 1 h |
| Battery | 518 Wh |
| Status | Commercial |
| API | yes |
| SDK | yes |
| SDK name | BXI ROS2 hardware-control SDK + MuJoCo simulation (Ubuntu 22.04) |
| ROS | yes |
| On-board compute | yes |
| Compute | Intel Core i7-1370P, 16 GB RAM, 512 GB storage |
| Sensors | RealSense D435i depth camera, IMU, 8-microphone array |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Maker product page and its own spec article: 31 DoF excluding hands (6 per leg, 7 per arm, 3 waist, 2 head), height 1450 mm, width x depth 450 x 280 mm (recorded as width 450, length 280), ~38 kg, max speed 5 m/s, single-arm payload 5 kg horizontal continuous / 10 kg elbow-supported (payload_kg = 5), 518 Wh battery with ~1 h walking runtime, 31 in-house hollow-shaft planetary joint motors (5014/5018/7010/8515) at 25-150 N.m peak torque with dual absolute encoders, >1000 Hz control over PCIE-CANFD, Intel i7-1370P / 16 GB / 512 GB onboard, RealSense D435i + IMU + 8-mic array, Ubuntu 22.04 with a ROS2 SDK and MuJoCo sim, teleoperation and autonomous modes. Maker quotes price per configuration and publishes no list price, so price stays empty.

## Sources

- Official page: [bxirobotics.com](https://www.bxirobotics.com/robots/humanoid-robot)
- [bxirobotics.com](https://www.bxirobotics.com/blog/elf3-humanoid-robot-specifications)
- [wiki.bxirobotics.com](https://wiki.bxirobotics.com/)

Listed by these directories (discovery only, never used as a spec source):

- [embodied.guide](https://embodied.guide/robots/bxi-robotics-elf-3/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-25). Source repository: https://github.com/htcrefactor/robot-catalog*
