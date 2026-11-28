# Unitree Robotics H1

> Unitree's first full-size humanoid, the H1, able to walk and run at up to 3.3 m/s on a 360-degree LiDAR and depth-camera perception stack.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=unitree-h1
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: Unitree Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 220 mm |
| Width | 570 mm |
| Height | 1,800 mm |
| Weight | 47 kg |
| Payload | 7 kg |
| Max speed | 3.3 m/s (11.9 km/h) |
| Degrees of freedom | 19 |
| Battery | 864 Wh |
| Released | 2023 |
| Status | Commercial |
| API | yes |
| SDK | yes |
| SDK name | unitree_sdk2 |
| ROS | yes |
| On-board compute | yes |
| Compute | Intel Core i5 (platform) + Intel Core i7 (user development); optional Orin NX |
| Sensors | 3D LiDAR, Depth camera |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

68 values from 3 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Variants | H1; H1-2 | H1-2 figures in this file are labelled; H1-2: ~178 cm, ~70 kg, 27 DoF | [unitree.com](https://www.unitree.com/h1) |
| Form factor | full-size | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Height | 1,805 mm | key dimensions (1520+285) mm x 570 mm x 220 mm; about 180 cm | [unitree.com](https://www.unitree.com/h1) |
| Width | 570 mm |  | [unitree.com](https://www.unitree.com/h1) |
| Thickness | 220 mm |  | [unitree.com](https://www.unitree.com/h1) |
| Total weight | 47 kg | about 47 kg | [unitree.com](https://www.unitree.com/h1) |
| Thigh and calf length | 400 x 2 mm |  | [unitree.com](https://www.unitree.com/h1) |
| Total arm length | 338 x 2 mm |  | [unitree.com](https://www.unitree.com/h1) |
| Height (H1-2) | 1,788 mm | (1503+285) mm x 510 mm x 287 mm; about 178 cm | [unitree.com](https://www.unitree.com/h1) |
| Total weight (H1-2) | 70 kg | about 70 kg | [unitree.com](https://www.unitree.com/h1) |
| Total arm length (H1-2) | 685 mm |  | [unitree.com](https://www.unitree.com/h1) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total degrees of freedom | 19 | 19 joint motors (H1) | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |
| Total degrees of freedom (H1-2) | 27 |  | [unitree.com](https://www.unitree.com/h1) |
| Moving speed | 3.3 m/s | claimed world record; potential mobility > 5 m/s; H1-2 < 2 m/s | [unitree.com](https://www.unitree.com/h1) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery capacity | 864 Wh | 15 Ah (0.864 kWh); quickly replaceable | [unitree.com](https://www.unitree.com/h1) |
| Battery max voltage | 67.2 V |  | [unitree.com](https://www.unitree.com/h1) |
| Quickly replaceable battery | yes |  | [unitree.com](https://www.unitree.com/h1) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| 3D LiDAR | Livox MID-360 | head; IP 192.168.123.120 | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |
| Depth camera | Intel RealSense D435 | head | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |
| Depth sensing coverage | 360° depth perception (3D LiDAR + depth camera) |  | [unitree.com](https://www.unitree.com/h1) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Motion control computer (PC1) | Intel Core i5-1235U, 10 cores / 12 threads, 4.40 GHz turbo | platform functions; not user-accessible | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |
| Development computer (PC2/PC3) | Intel Core i7-1255U / i7-1265U, 10 cores / 12 threads, 4.70 / 4.80 GHz | PC3 optional | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |
| Development computer memory | 16 / 32 GB | LPDDR5 5200 MT/s dual-channel | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |
| Computer storage | 500 GB or more | PC1 and PC2/PC3 | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |
| Integrated GPU | Intel Iris Xe Graphics, max 1.20 GHz |  | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |
| Cache | 12 MB Intel Smart Cache |  | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |
| Optional compute | Intel Core i7 or NVIDIA Jetson Orin NX | H1-2: up to 3 devices | [unitree.com](https://www.unitree.com/h1) |
| OTA software upgrade | yes | continuous OTA | [unitree.com](https://www.unitree.com/h1) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Development computer IP | 192.168.123.162 / .163 | PC2 / optional PC3 | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |
| Electrical interfaces | Aviation-plug interfaces on right side (joint motors, peripherals, Ethernet) | hot-swapping prohibited | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Arm load (H1-2) | 7 kg | rated about 7 kg; peak about 21 kg | [unitree.com](https://www.unitree.com/h1) |
| Dexterous hand | Optional | H1-2: optional Dex5-1 or other hands | [unitree.com](https://www.unitree.com/h1) |
| Hands | optional | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1) |

### Actuation & Joints

| Spec | Value | Note | Source |
|---|---|---|---|
| DoF per leg | 5 | hip x3 + knee x1 + ankle x1; H1-2: 6 (ankle x2) | [unitree.com](https://www.unitree.com/h1) |
| DoF per arm | 4 | expandable; H1-2: 7 (shoulder 3 + elbow 1 + wrist 3) | [unitree.com](https://www.unitree.com/h1) |
| Waist DoF | 1 |  | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |
| Peak torque density | 189 N·m/kg |  | [unitree.com](https://www.unitree.com/h1) |
| Knee torque | 360 N·m | about | [unitree.com](https://www.unitree.com/h1) |
| Hip joint torque | 220 N·m | about | [unitree.com](https://www.unitree.com/h1) |
| Ankle torque | 59 N·m | about; H1-2 ankle about 75 x2 N·m | [unitree.com](https://www.unitree.com/h1) |
| Arm joint torque | 75 N·m | about; H1-2 shoulder/elbow ~120 N·m, wrist ~30 N·m | [unitree.com](https://www.unitree.com/h1) |
| Waist joint torque (H1-2) | 220 N·m | about | [unitree.com](https://www.unitree.com/h1) |
| Joint motor | Unitree M107 | hollow axle, dual encoders | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |
| M107 motor max torque | 360 N·m |  | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |
| M107 max tension | 10,000 N | equivalent at 3.5 cm force arm | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |
| Joint output bearing | Industrial-grade crossed roller bearings |  | [unitree.com](https://www.unitree.com/h1) |
| Core joint motor | Low-inertia high-speed internal-rotor PMSM |  | [unitree.com](https://www.unitree.com/h1) |
| Joint encoder | Dual encoder | M107 | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |
| Joint limit – Hip yaw | -0.43 to +0.43 rad | SDK joint limit table; right side mirrored for roll/yaw | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |
| Joint limit – Hip roll | -0.43 to +0.43 rad | SDK joint limit table; right side mirrored for roll/yaw | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |
| Joint limit – Hip pitch | -3.14 to +2.53 rad | SDK joint limit table; right side mirrored for roll/yaw | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |
| Joint limit – Knee | -0.26 to +2.05 rad | SDK joint limit table; right side mirrored for roll/yaw | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |
| Joint limit – Ankle | -0.87 to +0.52 rad | SDK joint limit table; right side mirrored for roll/yaw | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |
| Joint limit – Torso | -2.35 to +2.35 rad | SDK joint limit table; right side mirrored for roll/yaw | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |
| Joint limit – Shoulder pitch | -2.87 to +2.87 rad | SDK joint limit table; right side mirrored for roll/yaw | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |
| Joint limit – L shoulder roll | -0.34 to +3.11 rad | SDK joint limit table; right side mirrored for roll/yaw | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |
| Joint limit – L shoulder yaw | -1.3 to +4.45 rad | SDK joint limit table; right side mirrored for roll/yaw | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |
| Joint limit – Elbow | -1.25 to +2.61 rad | SDK joint limit table; right side mirrored for roll/yaw | [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Intended use / caution | Civilian robot; keep safe distance; no dangerous modifications |  | [unitree.com](https://www.unitree.com/h1) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Sales status | shipping-now | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1) |
| Who can buy | research | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1) |
| Price | 90,000 USD | list price (maker price); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1) |
| Delivered price to US | 99,900 USD | before sales tax; route: seller: RoboStore; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1) |
| Delivered price to Germany | 97,942 EUR | incl. 19% VAT; route: estimate: import; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1) |
| Route to US | reseller | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1) |
| Route to EU | reseller | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1) |
| Sellers listed | 18 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1) |
| Documented uses | Robotics R&D; Manipulation research | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1) |

## Documents

- [Unitree H1 / H1-2 product page – parameter table](https://www.unitree.com/h1)
- [Unitree H1 SDK Development Guide – About H1 (updated 2026-03-12)](https://support.unitree.com/home/en/H1_developer/About_H1)
- [HumanoidStore datasheet – Unitree Robotics H1 (CC BY 4.0)](https://humanoidstore.co/robots/unitree-h1)

## Notes

Maker figures: about 180 cm, about 47 kg, (1520+285) x 570 x 220 mm, 5 DoF per leg and 4 per arm (18 total, summed from the maker's per-limb counts; arms are expandable), 3.3 m/s walking with potential above 5 m/s, 864 Wh (15 Ah, 67.2 V) swappable battery, knee 360 Nm, hip 220 Nm, ankle 59 Nm, arm 75 Nm, 3D LiDAR plus depth camera, i5 for platform functions and i7 for user development. Unitree's H1 page does not publish a price; the USD 90,000 figure in catalogues is not a maker price.

## Sources

- Official page: [unitree.com](https://www.unitree.com/h1/)
- [unitree.com](https://www.unitree.com/h1)
- [support.unitree.com](https://support.unitree.com/home/en/H1_developer/About_H1)
- [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1)
- [github.com](https://github.com/unitreerobotics/unitree_sdk2)
- [github.com](https://github.com/unitreerobotics/unitree_ros2)
- [github.com](https://github.com/unitreerobotics/unitree_ros/blob/master/robots/h1_description/urdf/h1.urdf)
- [github.com](https://github.com/unitreerobotics/unitree_ros/blob/master/robots/h1_description/mjcf/h1.xml)
- [github.com](https://github.com/unitreerobotics/unitree_sdk2_python)
- [github.com](https://github.com/unitreerobotics/unitree_ros)
- [github.com](https://github.com/unitreerobotics/unitree_mujoco)
- [shop.unitree.com](https://shop.unitree.com/products/unitree-h1)
- [younginmobility.com](https://www.younginmobility.com/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-28). Source repository: https://github.com/htcrefactor/robot-catalog*
