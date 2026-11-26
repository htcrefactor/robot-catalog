# Unitree Robotics G1

> Unitree's small full-body humanoid for research and development, with 23 joints on the base model, expandable to 43 on the EDU version with dexterous hands.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=unitree-g1
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: Unitree Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 200 mm |
| Width | 450 mm |
| Height | 1,320 mm |
| Weight | 35 kg |
| Payload | 2 kg |
| Max speed | 2 m/s (7.2 km/h) |
| Degrees of freedom | 23 |
| Runtime | 2 h |
| Released | 2024 |
| Status | Commercial |
| API | yes |
| SDK | yes |
| SDK name | unitree_sdk2 |
| ROS | yes |
| On-board compute | yes |
| Compute | 8-core high-performance CPU standard; EDU adds optional high-compute module (e.g. NVIDIA Orin) |
| Sensors | Depth camera, 3D LiDAR, 4-microphone array |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

130 values from 5 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Variants | G1; G1 EDU | EDU adds optional DoF, dexterous hands, compute module and secondary development | [unitree.com](https://www.unitree.com/g1) |
| Form factor | mid-size | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Height (standing) | 1,320 mm | H x W x T standing 1320 x 450 x 200 mm (G1 and G1 EDU) | [unitree.com](https://www.unitree.com/g1) |
| Width (standing) | 450 mm |  | [unitree.com](https://www.unitree.com/g1) |
| Thickness (standing) | 200 mm | front-to-back thickness | [unitree.com](https://www.unitree.com/g1) |
| Folded dimensions (H x W x T) | 690 x 450 x 300 mm |  | [unitree.com](https://www.unitree.com/g1) |
| Weight (with battery) | 35 kg | about 35 kg; G1 EDU about 35 kg+ | [unitree.com](https://www.unitree.com/g1) |
| Calf + thigh length | 0.6 m |  | [unitree.com](https://www.unitree.com/g1) |
| Arm span | 0.45 m | about 0.45 m | [unitree.com](https://www.unitree.com/g1) |
| Weight | 35 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1) |
| Height (standing) | 132 cm | G1 EDU; configuration: G1 EDU U1; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1-edu) |
| Height (standing) | 134 cm | G1+; configuration: G1+; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1-plus) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total degrees of freedom | 23 | G1 base | [unitree.com](https://www.unitree.com/g1) |
| Total degrees of freedom | 23 to 43 | G1 EDU, depending on options | [unitree.com](https://www.unitree.com/g1) |
| Top speed | 2 m/s | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1) |
| Total degrees of freedom | 23 | G1 EDU; configuration: G1 EDU U1; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1-edu) |
| Total degrees of freedom | 25 | G1+; configuration: G1+; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1-plus) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Power supply | 13-string lithium battery |  | [unitree.com](https://www.unitree.com/g1) |
| Smart battery capacity | 9,000 mAh | quick-release smart battery | [unitree.com](https://www.unitree.com/g1) |
| Quick-release battery | yes |  | [unitree.com](https://www.unitree.com/g1) |
| Battery life | 2 h | about 2 h | [unitree.com](https://www.unitree.com/g1) |
| Runtime per charge | 120 min | G1 EDU; configuration: G1 EDU U1; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1-edu) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charger | 54 V 5 A |  | [unitree.com](https://www.unitree.com/g1) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Dex3-1 tactile array sensors | 9 | number of array sensors; tactile arrays optional | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) |
| 3D LiDAR | Livox MID-360 | head-mounted | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) |
| LiDAR FOV | 360 horizontal; up to 59 vertical ° |  | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) |
| Depth camera | Intel RealSense D435i | head-mounted | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) |
| Microphone array | 4-microphone array |  | [unitree.com](https://www.unitree.com/g1) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Basic computing | 8-core high-performance CPU |  | [unitree.com](https://www.unitree.com/g1) |
| Development computer (PC2) CPU | Arm Cortex-A78AE, 8 cores / 8 threads, 2 GHz | G1 EDU development computing unit, NVIDIA Jetson Orin NX | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) |
| Development computer (PC2) module | NVIDIA Jetson Orin NX | G1 EDU; motion-control unit (PC1) is closed to users | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) |
| Development computer memory | 16 GB | PC2 | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) |
| Development computer storage | 2 TB | PC2 | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) |
| Development computer GPU | 1024-core NVIDIA Ampere GPU with 32 Tensor Cores, max 918 MHz | PC2 | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) |
| Development computer cache | 2 MB L2 + 4 MB L3 | PC2 | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) |
| High computing power module | Optional (e.g. NVIDIA Jetson Orin); multiple brands/models | G1 EDU accessory | [unitree.com](https://www.unitree.com/g1) |
| Thor backpack module | NVIDIA Jetson T5000 | optional Thor backpack accessory | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) · Thor Backpack Specifications |
| Thor backpack AI performance | 2,070 TFLOPS (FP4) | optional Thor backpack | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) |
| Thor backpack GPU | 2560-core NVIDIA Blackwell GPU, 96 fifth-gen Tensor Cores | optional Thor backpack | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) |
| Thor backpack CPU | 14-core Arm Neoverse-V3AE 64-bit | optional Thor backpack | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) |
| Thor backpack unified memory | 128 GB | 256-bit LPDDR5X; optional Thor backpack | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) |
| Thor backpack storage | 1 TB | optional Thor backpack | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) |
| Thor backpack peak power | 130 W | optional Thor backpack | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) |
| Thor backpack OS | Jetson Linux 38.2.1 (Ubuntu-based), JetPack 7 | optional Thor backpack | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) |
| Upgraded intelligent OTA | yes |  | [unitree.com](https://www.unitree.com/g1) |
| Secondary development | G1 EDU only | unitree_sdk2 / DDS (ROS 2 compatible) | [unitree.com](https://www.unitree.com/g1) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Development computer IP | 192.168.123.164 | PC2 | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) |
| Thor backpack USB | Type-A 3.2 x2; Type-C 3.1 x2 | optional Thor backpack | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) |
| Wi-Fi | Wi-Fi 6 |  | [unitree.com](https://www.unitree.com/g1) |
| Bluetooth | 5.2 |  | [unitree.com](https://www.unitree.com/g1) |
| Top interface – VBAT (XT30UPB-F) | 58 V / 5 A battery power output (direct battery) | electrical interface on top of robot | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) · Electrical Interface |
| Top interface – 24V (XT30UPB-F) | 24 V / 5 A power output | electrical interface on top of robot | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) · Electrical Interface |
| Top interface – 12V (XT30UPB-F) | 12 V / 5 A power output | electrical interface on top of robot | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) · Electrical Interface |
| Top interface – RJ45 x2 | 1000BASE-T Gigabit Ethernet | electrical interface on top of robot | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) · Electrical Interface |
| Top interface – Type-C x3 | USB 3.0 host, 5 V / 1.5 A power output | electrical interface on top of robot | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) · Electrical Interface |
| Top interface – Alt Mode Type-C | USB 3.2 host and DisplayPort 1.4 | electrical interface on top of robot | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) · Electrical Interface |
| Top interface – I/O OUT (5577) | 12 V / 3 A power output + GPIO (UART, I2C, GPIO) | electrical interface on top of robot | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) · Electrical Interface |
| FCC ID | 2A5PE-YUSHU008 | granted 2025-03-03; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Hand DoF | 7 | G1 EDU only: optional force-controlled three-fingered hand Dex3-1 (+2 optional wrist DoF); base G1 has no hand | [unitree.com](https://www.unitree.com/g1) |
| Dexterous hand | Dex3-1 three-fingered dexterous hand (optional) | thumb 3 active DoF, index 2, middle 2; optional tactile sensor arrays | [unitree.com](https://www.unitree.com/g1) |
| Dex3-1 hand operating voltage | 12-58 V |  | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) |
| Dex3-1 hand perception range | 10-2500 g |  | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) |
| Dex3-1 thumb joint ranges | 0 to +100; -35 to +60; -60 to +60 ° | thumb joints | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) |
| Dex3-1 index/middle finger joint ranges | 0 to +90; 0 to +100 ° | index and middle fingers | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) |
| Arm maximum load | 2 kg | about 2 kg (G1); varies greatly with arm extension posture | [unitree.com](https://www.unitree.com/g1) |
| Arm maximum load | 3 kg | about 3 kg (G1 EDU) | [unitree.com](https://www.unitree.com/g1) |
| Hands | fixed-grippers | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1) |
| Hands | optional | G1 EDU; configuration: G1 EDU U1; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1-edu) |
| Hands | none | G1+; configuration: G1+; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1-plus) |

### Actuation & Joints

| Spec | Value | Note | Source |
|---|---|---|---|
| DoF per leg | 6 |  | [unitree.com](https://www.unitree.com/g1) |
| Waist DoF | 1 | G1; EDU 1 + optional 2 additional waist DoF | [unitree.com](https://www.unitree.com/g1) |
| DoF per arm | 5 |  | [unitree.com](https://www.unitree.com/g1) |
| Joint output bearing | Industrial-grade crossed roller bearings |  | [unitree.com](https://www.unitree.com/g1) |
| Joint motor | Low-inertia high-speed internal-rotor PMSM | permanent magnet synchronous motor | [unitree.com](https://www.unitree.com/g1) |
| Max knee joint torque | 90 N·m | G1; largest joint motor | [unitree.com](https://www.unitree.com/g1) |
| Max knee joint torque | 120 N·m | G1 EDU; largest joint motor | [unitree.com](https://www.unitree.com/g1) |
| Waist joint range | Z ±155 ° | G1; EDU adds X ±30°, Y ±30° | [unitree.com](https://www.unitree.com/g1) |
| Knee joint range | 0 to 165 ° |  | [unitree.com](https://www.unitree.com/g1) |
| Hip joint range | P ±154; R -30 to +170; Y ±158 ° |  | [unitree.com](https://www.unitree.com/g1) |
| Wrist joint range | P ±92.5; Y ±92.5 ° | G1 EDU with optional wrist DoF | [unitree.com](https://www.unitree.com/g1) |
| Joint limit – L hip pitch | -2.5307 to 2.8798 rad | SDK joint limit table (29-joint config); right side mirrored | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) · Joint serial number and joint limit |
| Joint limit – L hip roll | -0.5236 to 2.9671 rad | SDK joint limit table (29-joint config); right side mirrored | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) · Joint serial number and joint limit |
| Joint limit – L hip yaw | -2.7576 to 2.7576 rad | SDK joint limit table (29-joint config); right side mirrored | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) · Joint serial number and joint limit |
| Joint limit – L knee | -0.087267 to 2.8798 rad | SDK joint limit table (29-joint config); right side mirrored | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) · Joint serial number and joint limit |
| Joint limit – L ankle pitch | -0.87267 to 0.5236 rad | SDK joint limit table (29-joint config); right side mirrored | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) · Joint serial number and joint limit |
| Joint limit – L ankle roll | -0.2618 to 0.2618 rad | SDK joint limit table (29-joint config); right side mirrored | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) · Joint serial number and joint limit |
| Joint limit – Waist yaw | -2.618 to 2.618 rad | SDK joint limit table (29-joint config); right side mirrored | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) · Joint serial number and joint limit |
| Joint limit – Waist roll | -0.52 to 0.52 rad | SDK joint limit table (29-joint config); right side mirrored | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) · Joint serial number and joint limit |
| Joint limit – Waist pitch | -0.52 to 0.52 rad | SDK joint limit table (29-joint config); right side mirrored | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) · Joint serial number and joint limit |
| Joint limit – L shoulder pitch | -3.0892 to 2.6704 rad | SDK joint limit table (29-joint config); right side mirrored | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) · Joint serial number and joint limit |
| Joint limit – L shoulder roll | -1.5882 to 2.2515 rad | SDK joint limit table (29-joint config); right side mirrored | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) · Joint serial number and joint limit |
| Joint limit – L shoulder yaw | -2.618 to 2.618 rad | SDK joint limit table (29-joint config); right side mirrored | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) · Joint serial number and joint limit |
| Joint limit – L elbow | -1.0472 to 2.0944 rad | SDK joint limit table (29-joint config); right side mirrored | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) · Joint serial number and joint limit |
| Joint limit – L wrist roll | -1.972222054 to 1.972222054 rad | SDK joint limit table (29-joint config); right side mirrored | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) · Joint serial number and joint limit |
| Joint limit – L wrist pitch | -1.614429558 to 1.614429558 rad | SDK joint limit table (29-joint config); right side mirrored | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) · Joint serial number and joint limit |
| Joint limit – L wrist yaw | -1.614429558 to 1.614429558 rad | SDK joint limit table (29-joint config); right side mirrored | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) · Joint serial number and joint limit |
| Joint indices in SDK | 29 | joint index 0-28 in SDK table (full EDU configuration) | [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1) |
| Full-joint hollow electrical routing | yes |  | [unitree.com](https://www.unitree.com/g1) |
| Joint encoder | Dual encoder |  | [unitree.com](https://www.unitree.com/g1) |
| Cooling system | Local air cooling |  | [unitree.com](https://www.unitree.com/g1) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Intended use / caution | Civilian robot; keep sufficient safe distance; no dangerous modifications |  | [unitree.com](https://www.unitree.com/g1) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Manual controller | Included |  | [unitree.com](https://www.unitree.com/g1) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Speaker | 5 W |  | [unitree.com](https://www.unitree.com/g1) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Warranty | 8 months | G1 | [unitree.com](https://www.unitree.com/g1) |
| Warranty | 18 months | G1 EDU | [unitree.com](https://www.unitree.com/g1) |
| Price | 13,500 USD | G1, tax and shipping excluded; G1 EDU contact sales | [unitree.com](https://www.unitree.com/g1) |
| Sales status | shipping-now | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1) |
| Who can buy | anyone | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1) |
| Price | 13,500 USD | list price (maker price); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1) |
| Delivered price to US | 17,990 USD | before sales tax; route: seller: RoboStore; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1) |
| Delivered price to Germany | 15,462 EUR | incl. 19% VAT; route: estimate: import; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1) |
| Route to US | direct | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1) |
| Route to EU | reseller | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1) |
| Sellers listed | 53 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1) |
| Documented uses | Demo / showpiece | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1) |
| Price | 39,000 EUR | G1 EDU; configuration: G1 EDU U1; list price (reseller price); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1-edu) |
| Price (USD equivalent) | 43,778 USD | G1 EDU; configuration: G1 EDU U1; EUR list price at ECB reference rate; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1-edu) |
| Delivered price to US | 41,705 USD | G1 EDU; configuration: G1 EDU U1; before sales tax; route: seller: Toborlife (official Unitree US partner); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1-edu) |
| Delivered price to Germany | 38,675 EUR | G1 EDU; configuration: G1 EDU U1; incl. 19% VAT; route: seller: Generation Robots; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1-edu) |
| Route to US | reseller | G1 EDU; configuration: G1 EDU U1; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1-edu) |
| Sellers listed | 25 | G1 EDU; configuration: G1 EDU U1; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1-edu) |
| Documented uses | Robotics R&D | G1 EDU; configuration: G1 EDU U1; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1-edu) |
| Sales status | announced | G1+; configuration: G1+; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1-plus) |
| Who can buy | restricted | G1+; configuration: G1+; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1-plus) |
| Route to US | unclear | G1+; configuration: G1+; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1-plus) |
| Route to EU | unclear | G1+; configuration: G1+; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1-plus) |
| Sellers listed | 5 | G1+; configuration: G1+; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1-plus) |
| Public tender price per unit | 52,567 EUR | CNRS (LORIA laboratory, Nancy) (FR), awarded 2026-07-22: 3 x Unitree G1 EDU (identical to the lab's EDU-U4); 4 bid(s); before VAT; winner Génération Robots; via HumanoidStore tender record (CC BY 4.0) | [ted.europa.eu](https://ted.europa.eu/en/notice/-/detail/510222-2026) |

### Payload

| Spec | Value | Note | Source |
|---|---|---|---|
| Rated payload | 2 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1) |
| Rated payload | 3 kg | G1 EDU; configuration: G1 EDU U1; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1-edu) |

## Documents

- [Unitree G1 product page – G1 Parameter table](https://www.unitree.com/g1)
- [Unitree G1 SDK Development Guide – About G1 (updated 2026-09-17)](https://support.unitree.com/home/en/G1_developer/about_G1)
- [HumanoidStore datasheet – Unitree Robotics G1 (CC BY 4.0)](https://humanoidstore.co/robots/unitree-g1)
- [HumanoidStore datasheet – Unitree Robotics G1 EDU (CC BY 4.0)](https://humanoidstore.co/robots/unitree-g1-edu)
- [HumanoidStore datasheet – Unitree Robotics G1+ (CC BY 4.0)](https://humanoidstore.co/robots/unitree-g1-plus)

## Notes

Maker page unitree.com/g1 re-checked 2026-11-17: standing 1,320 x 450 x 200 mm (H x W x T), folded 690 x 450 x 300 mm, 35 kg with battery, 23 DoF base (23-43 EDU), arm load about 2 kg (3 kg EDU), about 2 h, US$13.5K base (tax and shipping excluded). The stored height is the maker's standing figure; an earlier G1 manual and the May-2024 launch coverage give 1,270 mm (127 cm), which the current maker page does not state. | Maker figures: 1320 x 450 x 200 mm standing (690 x 450 x 300 folded), ~35 kg, 23 DoF (G1) or 23-43 (G1 EDU), 6 per leg, 1 waist (+2 optional), 5 per arm, optional 7-DoF three-finger hand, 90 Nm knee (120 Nm on EDU), about 2 kg arm load (3 kg on EDU), 9000 mAh quick-release pack, about 2 h, depth camera plus 3D LiDAR, 4-microphone array, 5 W speaker, Wi-Fi 6 and Bluetooth 5.2, 8-core CPU; trotting speed above 2 m/s. Price US$13,500 for G1.

## Sources

- Official page: [unitree.com](https://www.unitree.com/g1/)
- [unitree.com](https://www.unitree.com/g1)
- [support.unitree.com](https://support.unitree.com/home/en/G1_developer/about_G1)
- [unitree.com](https://www.unitree.com/operate/g1/)
- [github.com](https://github.com/unitreerobotics/unitree_sdk2)
- [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1)
- [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1-edu)
- [humanoidstore.co](https://humanoidstore.co/robots/unitree-g1-plus)
- [github.com](https://github.com/unitreerobotics/unitree_ros/blob/master/robots/g1_description/g1_29dof.urdf)
- [github.com](https://github.com/unitreerobotics/unitree_sdk2_python)
- [github.com](https://github.com/unitreerobotics/unitree_ros)
- [github.com](https://github.com/unitreerobotics/unitree_ros2)
- [github.com](https://github.com/unitreerobotics/unitree_mujoco)
- [shop.unitree.com](https://shop.unitree.com/products/unitree-g1)
- [younginmobility.com](https://www.younginmobility.com/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-26). Source repository: https://github.com/htcrefactor/robot-catalog*
