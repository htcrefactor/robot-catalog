# ROBOTIS AI Worker

> ROBOTIS' semi-humanoid industrial platform: a swerve-drive mobile base with dual 7-DOF DYNAMIXEL arms, a lift column and a leader-follower teleoperation rig for imitation learning.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=robotis-ai-worker
- Category: Humanoid
- Locomotion: Wheeled
- Manufacturer: ROBOTIS (South Korea)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 602 mm |
| Width | 604 mm |
| Height | 1,623 mm |
| Weight | 90 kg |
| Payload | 3 kg |
| Max speed | 1.5 m/s (5.4 km/h) |
| Degrees of freedom | 25 |
| Runtime | 6 h |
| Battery | 2,040 Wh |
| Status | Commercial |
| SDK | yes |
| SDK name | ROS 2, Python, C++, Web UI |
| ROS | yes |
| On-board compute | NVIDIA Jetson AGX Orin 32GB |
| Sensors | Stereolabs ZED Mini RGBD head camera, 2x Intel RealSense D405 hand cameras, 2x LakiBeam 1 2D LiDAR, IMU |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

16 values from 1 document, checked against maker sources on 2026-11-13.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Form factor | wheeled (bimanual torso on a wheeled base) | configuration: FFW-SG2; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-ai-worker) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Height (standing) | 162.3 cm | configuration: FFW-SG2; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-ai-worker) |
| Weight | 90 kg | configuration: FFW-SG2; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-ai-worker) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total degrees of freedom | 25 | configuration: FFW-SG2; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-ai-worker) |
| Top speed | 1.5 m/s | configuration: FFW-SG2; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-ai-worker) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Runtime per charge | 360 min | configuration: FFW-SG2; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-ai-worker) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Hands | fixed-grippers | configuration: FFW-SG2; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-ai-worker) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Sales status | shipping-now | configuration: FFW-SG2; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-ai-worker) |
| Who can buy | anyone | configuration: FFW-SG2; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-ai-worker) |
| Price | 69,000 USD | configuration: FFW-SG2; list price (reseller price); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-ai-worker) |
| Delivered price to US | 69,000 USD | configuration: FFW-SG2; before sales tax; route: seller: ROBOTIS America (direct); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-ai-worker) |
| Route to US | direct | configuration: FFW-SG2; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-ai-worker) |
| Route to EU | reseller | configuration: FFW-SG2; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-ai-worker) |
| Sellers listed | 2 | configuration: FFW-SG2; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-ai-worker) |
| Documented uses | Robotics R&D; Manipulation research | configuration: FFW-SG2; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-ai-worker) |

### Payload

| Spec | Value | Note | Source |
|---|---|---|---|
| Rated payload | 3 kg | configuration: FFW-SG2; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-ai-worker) |

## Documents

- [HumanoidStore datasheet – ROBOTIS AI Worker (CC BY 4.0)](https://humanoidstore.co/robots/robotis-ai-worker)

## Notes

Maker spec table for the follower FFW-SG2: 604 x 602 x 1,623 mm, 90 kg, 25 total DOF (arm 7 x 2, gripper 1 x 2, head 2, lift 1, mobile 6), 641 mm arm reach to the wrist, 3.0 kg nominal payload per arm (6.0 kg dual; 5.0 kg / 10.0 kg peak), 1.5 m/s swerve drive, 25 V 80 Ah battery (2,040 Wh), RGBD x 3 + LiDAR x 2 + IMU, NVIDIA Jetson AGX Orin 32GB, ROS 2 / Python / C++ / Web UI, 0-40 C operation, aluminium and plastic exterior. Payload entered as the nominal single-arm figure. Maker store states up to 6 hours of continuous operation on the built-in battery. FFW-BG2 is a Korea-only 19-DOF version without the mobile base; FFW-SH3P is in preparation. The 69,000 USD in this record was a reseller figure (the maker sells by quote) and was removed.

## Sources

- Official page: [ai.robotis.com](https://ai.robotis.com/ai_worker/hardware_ai_worker.html)
- [ai.robotis.com](https://ai.robotis.com/ai_worker/hardware_ai_worker)
- [robotis.us](https://robotis.us/ai-worker-ffw-sg2-us/)
- [humanoidstore.co](https://humanoidstore.co/robots/robotis-ai-worker)
- [robotis.com](https://www.robotis.com/ko/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-24). Source repository: https://github.com/htcrefactor/robot-catalog*
