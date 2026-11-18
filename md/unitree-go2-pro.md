# Unitree Robotics Go2 Pro

> Consumer quadruped with 4G, voice and side-follow features for enthusiasts.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=unitree-go2-pro
- Category: Quadruped
- Locomotion: Legged
- Manufacturer: Unitree Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 700 mm |
| Width | 310 mm |
| Height | 400 mm |
| Weight | 15 kg |
| Payload | 8 kg |
| Max speed | 3.5 m/s (12.6 km/h) |
| Degrees of freedom | 12 |
| Runtime | 1 h |
| Status | Commercial |
| SDK | no |
| Compute | 8-core high-performance CPU |
| Sensors | 4D LiDAR L2, HD wide-angle camera, Wireless vector positioning module |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

63 values from 2 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Manufacturer | Unitree Robotics (Hangzhou Yushu Technology Co., Ltd.) |  | [unitree.com](https://www.unitree.com/go2) |
| Variants | Go2 AIR; Go2 PRO; Go2 X; Go2 EDU | "Available in diverse configurations" | [unitree.com](https://www.unitree.com/go2) |
| Model | Go2 PRO |  | [unitree.com](https://www.unitree.com/go2) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length (standing) | 70 cm | dimension of standing 70 × 31 × 40 cm | [unitree.com](https://www.unitree.com/go2) |
| Width (standing) | 31 cm |  | [unitree.com](https://www.unitree.com/go2) |
| Height (standing) | 40 cm |  | [unitree.com](https://www.unitree.com/go2) |
| Length (crouching) | 76 cm | dimension of crouching 76 × 31 × 20 cm | [unitree.com](https://www.unitree.com/go2) |
| Height (crouching) | 20 cm |  | [unitree.com](https://www.unitree.com/go2) |
| Weight (with battery) | 15 kg | about | [unitree.com](https://www.unitree.com/go2) |
| Material | Aluminium alloy + high strength engineering plastic |  | [unitree.com](https://www.unitree.com/go2) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Degrees of freedom | 12 | 12 joint motors | [unitree.com](https://www.unitree.com/go2) |
| Advanced AI gaits | Upside-down walking, adaptive roll-over, climbing over obstacles (AI mode) | learned via large-scale AI simulation training | [unitree.com](https://www.unitree.com/go2) |
| Payload | 8 kg | ≈8 kg | [unitree.com](https://www.unitree.com/go2) |
| Maximum payload | 10 kg | MAX ~10 kg | [unitree.com](https://www.unitree.com/go2) |
| Speed | 0–3.5 m/s |  | [unitree.com](https://www.unitree.com/go2) |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| 3D LiDAR mapping | Point-cloud map construction with L2 LiDAR and app; specify a path for autonomous movement |  | [unitree.com](https://www.unitree.com/go2) |
| Recommended max stair height | 16 cm | not recommended to walk stairs higher than 16 cm | [static1.squarespace.com](https://static1.squarespace.com/static/5e76e0c52a318c0c1a850442/t/6670b6185e6f531946071db4/1718662712134/GO2+Edu+User+Manual.pdf) · Cautions p.20 |
| Max climb/drop height | 16 cm | about | [unitree.com](https://www.unitree.com/go2) |
| Max climb angle | 40 ° |  | [unitree.com](https://www.unitree.com/go2) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Voltage | 28–33.6 V |  | [unitree.com](https://www.unitree.com/go2) |
| Working maximum power | 3,000 W | about | [unitree.com](https://www.unitree.com/go2) |
| Smart battery | 8,000 mAh | standard | [unitree.com](https://www.unitree.com/go2) |
| Battery life | 1–2 h | about | [unitree.com](https://www.unitree.com/go2) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charging pile compatibility | no |  | [unitree.com](https://www.unitree.com/go2) |
| Charger | Standard 33.6 V 3.5 A |  | [unitree.com](https://www.unitree.com/go2) |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| Operating temperature | 5 to 35 °C | run in good weather; do not run in fog, snow, rain, thunder, sandstorm etc. | [static1.squarespace.com](https://static1.squarespace.com/static/5e76e0c52a318c0c1a850442/t/6670b6185e6f531946071db4/1718662712134/GO2+Edu+User+Manual.pdf) · Safety Instructions p.2 |
| Water resistance | Not waterproof | do not run with water on the ground, in rain, snow or wet conditions; not dustproof or waterproof for storage | [static1.squarespace.com](https://static1.squarespace.com/static/5e76e0c52a318c0c1a850442/t/6670b6185e6f531946071db4/1718662712134/GO2+Edu+User+Manual.pdf) · p.2, p.21 |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| LiDAR | Unitree 4D LiDAR L2 (super-wide-angle) | standard on all versions; the 2023 EDU manual describes the earlier L1 (360° × 90°) | [unitree.com](https://www.unitree.com/go2) |
| LiDAR field of view | 360 × 96 ° | hemispherical ultra-wide recognition | [unitree.com](https://www.unitree.com/go2) |
| LiDAR minimum detection distance | 0.05 m | minimum detection distance as low as 0.05 m | [unitree.com](https://www.unitree.com/go2) |
| Camera | HD wide-angle camera |  | [unitree.com](https://www.unitree.com/go2) |
| Foot-end force sensor | no |  | [unitree.com](https://www.unitree.com/go2) |
| GPS | yes | part of 4G module | [unitree.com](https://www.unitree.com/go2) |
| Depth camera | 0 | not available | [unitree.com](https://www.unitree.com/go2) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| OTA updates | Upgraded intelligent OTA (cloud-based, with user authorisation) |  | [unitree.com](https://www.unitree.com/go2) |
| Graphical programming | yes |  | [unitree.com](https://www.unitree.com/go2) |
| Secondary development | no |  | [unitree.com](https://www.unitree.com/go2) |
| Basic computing power | 8-core high-performance CPU | supports advanced mode, AI mode, 3D LiDAR mapping, etc. | [unitree.com](https://www.unitree.com/go2) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Image transmission | RTT 2.0 HD real-time image transmission | quality varies with network environment | [unitree.com](https://www.unitree.com/go2) |
| Wi-Fi | Wi-Fi 6, dual-band |  | [unitree.com](https://www.unitree.com/go2) |
| Bluetooth | 5.2 / 4.2 / 2.1 |  | [unitree.com](https://www.unitree.com/go2) |
| 4G module (with GPS) | yes | built-in 4G and eSIM | [unitree.com](https://www.unitree.com/go2) |

### Actuation & Joints

| Spec | Value | Note | Source |
|---|---|---|---|
| Joint motors | 12 | aluminum knee joint motor, 12 sets | [unitree.com](https://www.unitree.com/go2) |
| Range of motion (body) | −48 to 48 ° |  | [unitree.com](https://www.unitree.com/go2) |
| Range of motion (thigh) | −200 to 90 ° |  | [unitree.com](https://www.unitree.com/go2) |
| Range of motion (shank) | −156 to −48 ° |  | [unitree.com](https://www.unitree.com/go2) |
| Intra-joint circuit (knee) | yes |  | [unitree.com](https://www.unitree.com/go2) |
| Joint heat pipe cooler | yes |  | [unitree.com](https://www.unitree.com/go2) |
| Max joint torque | 45 N·m | about; maximum torque of the largest joint motor; varies across the 12 joint motors | [unitree.com](https://www.unitree.com/go2) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Intelligent detection and avoidance | yes |  | [unitree.com](https://www.unitree.com/go2) |
| Intended use | Civilian robot; not a toy; not for persons under 14; dangerous modifications or hazardous use prohibited |  | [unitree.com](https://www.unitree.com/go2) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Basic actions | yes |  | [unitree.com](https://www.unitree.com/go2) |
| Wireless vector positioning tracking module | yes |  | [unitree.com](https://www.unitree.com/go2) |
| ISS 2.0 intelligent side-follow system | yes | positioning accuracy upgraded 50 %; remote control distance over 30 m in open environment without interference | [unitree.com](https://www.unitree.com/go2) |
| Manual controller | Optional |  | [unitree.com](https://www.unitree.com/go2) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Front lamp | yes |  | [unitree.com](https://www.unitree.com/go2) |
| Head indicator light | Status indication by head light colour (e.g. slow yellow flash = low battery, auto crouch within 10 min) |  | [static1.squarespace.com](https://static1.squarespace.com/static/5e76e0c52a318c0c1a850442/t/6670b6185e6f531946071db4/1718662712134/GO2+Edu+User+Manual.pdf) · p.6 |
| Voice function | yes | offline voice interaction, commands, intercom and music play | [unitree.com](https://www.unitree.com/go2) |
| Front searchlight power | 3 W | head front light, constant white | [static1.squarespace.com](https://static1.squarespace.com/static/5e76e0c52a318c0c1a850442/t/6670b6185e6f531946071db4/1718662712134/GO2+Edu+User+Manual.pdf) · Chinese section p.6 |

### Transport & Storage

| Spec | Value | Note | Source |
|---|---|---|---|
| Auto-scaling strap | yes |  | [unitree.com](https://www.unitree.com/go2) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Regional note | 4G function of non-Chinese-mainland version supports only 43 European countries (except Ukraine) and some Asian regions | footnote [10] | [unitree.com](https://www.unitree.com/go2) |
| Warranty period | 12 months | see product warranty brochure | [unitree.com](https://www.unitree.com/go2) |
| Price | 2,800 USD | tax and freight excluded | [unitree.com](https://www.unitree.com/go2) |

## Documents

- [Unitree Go2 product page (parameter table AIR / PRO / X / EDU)](https://www.unitree.com/go2)
- [Unitree Go2 EDU User Manual (© 2023 Unitree Robotics; hosted by reseller)](https://static1.squarespace.com/static/5e76e0c52a318c0c1a850442/t/6670b6185e6f531946071db4/1718662712134/GO2+Edu+User+Manual.pdf)

## Notes

Unitree Go2 page comparison table (PRO column, checked 2026-11-17): 70 x 31 x 40 cm, about 15 kg, payload about 8 kg (max ~10 kg), 0-3.5 m/s, 12 joint motors, 8000 mAh battery, 1-2 h, 4D LiDAR L2 + HD wide-angle camera + wireless vector positioning module, 8-core CPU, $2,800. IP rating and battery Wh are not published.

## Sources

- Official page: [unitree.com](https://www.unitree.com/go2)
- [github.com](https://github.com/unitreerobotics/unitree_ros/blob/master/robots/go2_description/urdf/go2_description.urdf)
- [github.com](https://github.com/unitreerobotics/unitree_mujoco)
- [github.com](https://github.com/unitreerobotics/unitree_ros)
- [shop.unitree.com](https://shop.unitree.com/products/unitree-go2)
- [younginmobility.com](https://www.younginmobility.com/)

Listed by these directories (discovery only, never used as a spec source):

- [robocensus.com](https://robocensus.com/robots/unitree-go2/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-18). Source repository: https://github.com/htcrefactor/robot-catalog*
