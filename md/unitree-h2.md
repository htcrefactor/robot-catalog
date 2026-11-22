# Unitree Robotics H2

> Unitree's 1.82 m humanoid with a bionic head and 31 DoF, built for heavier industrial and research work with 360 Nm leg joints.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=unitree-h2
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: Unitree Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 218 mm |
| Width | 456 mm |
| Height | 1,820 mm |
| Weight | 70 kg |
| Payload | 15 kg |
| Degrees of freedom | 31 |
| Released | 2025 |
| Status | Commercial |
| API | yes |
| SDK | yes |
| SDK name | unitree_sdk2 |
| ROS | yes |
| On-board compute | yes |
| Compute | PC1 Intel Core i5 (platform); EDU adds PC2 Intel Core i7 for custom development; optional module e.g. NVIDIA Thor |
| Sensors | Bionic head with facial features |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

111 values from 5 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Variants | H2; H2 EDU; H2plus (camera table) |  | [unitree.com](https://www.unitree.com/H2) |
| Form factor | full-size | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Height (standing) | 1,820 mm | H x W x T 1820 x 456 x 218 mm | [unitree.com](https://www.unitree.com/H2) |
| Width | 456 mm |  | [unitree.com](https://www.unitree.com/H2) |
| Thickness | 218 mm |  | [unitree.com](https://www.unitree.com/H2) |
| Weight (with battery) | 70 kg | about 70 kg | [unitree.com](https://www.unitree.com/H2) |
| Calf + thigh length | 1,045 mm |  | [unitree.com](https://www.unitree.com/H2) |
| Forearm + upper arm length | 690 mm |  | [unitree.com](https://www.unitree.com/H2) |
| Construction materials | Aircraft-grade aluminium + titanium alloy + high-strength engineering plastics |  | [unitree.com](https://www.unitree.com/H2) |
| Weight | 70 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2) |
| Height (standing) | 182 cm | H2 EDU; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2-edu) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total degrees of freedom | 31 | 31 joint motors | [unitree.com](https://www.unitree.com/H2) |
| Total degrees of freedom | 31 | H2 EDU; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2-edu) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Power supply | Lithium battery with low internal resistance |  | [unitree.com](https://www.unitree.com/H2) |
| Battery capacity | 972 Wh | 15 Ah (0.972 kWh) | [unitree.com](https://www.unitree.com/H2) |
| Battery max voltage | 75.6 V |  | [unitree.com](https://www.unitree.com/H2) |
| Smart battery (quick release) | yes |  | [unitree.com](https://www.unitree.com/H2) |
| Battery life | 3 h | about 3 h | [unitree.com](https://www.unitree.com/H2) |
| Runtime per charge | 180 min | H2 EDU; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2-edu) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charger | Included |  | [unitree.com](https://www.unitree.com/H2) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Head camera | Humanoid binocular camera with wide field of view |  | [unitree.com](https://www.unitree.com/H2) |
| Binocular camera sensors | 2 | 2 RGB sensors | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| Binocular camera resolution | 2064 x 1552 px | H2 / H2 EDU; H2plus 2560 x 1984 | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| Binocular camera frame rate | 30 fps |  | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| Camera shutter | Global shutter |  | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| Camera output data | 12-bit RAW | H2plus 10-bit RAW | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| Stereo baseline | 60 mm |  | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| Camera horizontal FOV | 156 ° | H2 / H2 EDU; H2plus 140° ±3° | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| Camera vertical FOV | 116 ° | H2 / H2 EDU; H2plus 102° ±3° | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| Camera F-number | F2.0 |  | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| Camera focal length | 1.53 mm | H2plus 2.67 mm | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| Camera depth of field | 0.15 m to infinity (focus 0.4 m) | H2plus 0.4 m to infinity | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| Camera operating temperature | -20 to +60 °C | H2plus -30 to +70 °C | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| Camera interface | PC1 / MIPI 4-lane | H2plus: PC3 / GMSL2 | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| Microphone | Array microphone |  | [unitree.com](https://www.unitree.com/H2) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Motion control unit (PC1) | Intel Core i5, 10 cores / 12 threads, 4.40 GHz, 8 GB LPDDR5 | platform capabilities; not externally accessible | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| Development unit (PC2) | Intel Core i7, 10 cores / 12 threads, 4.70 / 4.80 GHz | H2 EDU custom development | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| PC2 memory | 16 / 32 GB | LPDDR5 5200 MT/s dual-channel | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| PC1/PC2 storage | 500 GB or above |  | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| PC1/PC2 GPU | Intel Iris Xe Graphics, max 1.20 GHz |  | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| Optional development unit PC3 | NVIDIA Jetson Thor (T5000) | optional | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| PC3 AI performance | 2,070 TFLOPS (FP4 sparse) | optional Jetson Thor | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| PC3 GPU | 2560-core NVIDIA Blackwell, 5th-gen Tensor Cores, 1.57 GHz | optional | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| PC3 CPU | 14-core Arm Neoverse-V3AE, 2.6 GHz | optional | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| PC3 memory | 128 GB | 256-bit LPDDR5X, 273 GB/s | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| PC3 power | 40-130 W |  | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| Optional development unit PC4 | NVIDIA Jetson Orin NX 16GB | optional | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| PC4 AI performance | 100 TOPS | optional Jetson Orin NX | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| PC4 GPU | 1024-core NVIDIA Ampere, 32 Tensor Cores, 918 MHz |  | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| PC4 CPU | 8-core Arm Cortex-A78AE v8.2, 2 GHz |  | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| PC4 memory | 16 GB | 128-bit LPDDR5, 102.4 GB/s | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| PC3/PC4 storage | 2 TB | NVMe | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| PC4 power | 10-25 W |  | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| PC3/PC4 video encode | 1x 4K60, 3x 4K30, 6x 1080p60, 12x 1080p30 (H.265) |  | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| PC3/PC4 video decode | 1x 8K30, 2x 4K60, 4x 4K30, 9x 1080p60, 18x 1080p30 (H.265) |  | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| Headline compute | 2,070 TOPS | product page: 'powered by a 2070 TOPS chip' (optional Thor module) | [unitree.com](https://www.unitree.com/H2) |
| Upgraded intelligent OTA | yes |  | [unitree.com](https://www.unitree.com/H2) |
| Secondary development | H2 EDU only |  | [unitree.com](https://www.unitree.com/H2) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Development computer IPs | PC2 192.168.123.162 / 192.168.124.162; PC3 .163; PC4 .164 |  | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| Wi-Fi | Wi-Fi 6 |  | [unitree.com](https://www.unitree.com/H2) |
| Bluetooth | 5.2 |  | [unitree.com](https://www.unitree.com/H2) |
| Top interface – VBAT+485 (GXT30(2)-M) | 54-75.6 V / 10 A battery output + RS-485 (to PC2) |  | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) · Electrical Interfaces |
| Top interface – 24V+CAN (GXT30(2)-M) x2 | 24 V / 10 A output + CAN (to PC2) |  | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) · Electrical Interfaces |
| Top interface – 12V+485 (GXT30(2)-M) | 12 V / 10 A output + RS-485 (to PC2) |  | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) · Electrical Interfaces |
| Top interface – Type-C (PC2) | USB 3.0 host, DP 1.4, PD 3.0 |  | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) · Electrical Interfaces |
| Top interface – Type-C x5 | USB 3.0 host, 5 V / 2 A output (some route to optional PC3/PC4 with DP 1.4 + PD 3.0) |  | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) · Electrical Interfaces |
| Top interface – GMSL | Video input (with optional PC3) |  | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) · Electrical Interfaces |
| Top interface – RJ45 x2 | Gigabit Ethernet (192.168.123.x and 192.168.124.x segments) |  | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) · Electrical Interfaces |
| Top interface – Dexterous hand connector x2 | 24 V / 10 A + RS-485 + USB 2.0 (optional 100 Mbps Ethernet) |  | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) · Electrical Interfaces |
| FCC ID | 2A5PE-YUSHU012 | granted 2026-06-30; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2) |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Total external power output | 500 W | max, excluding direct battery output | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| Installation holes | Rear mounting hole pattern (see 3D model) |  | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Dexterous hand | Multiple model options (H2 EDU) | H2 base: none | [unitree.com](https://www.unitree.com/H2) |
| Arm payload (rated) | 7 kg | ~7 kg rated; peak ~15 kg | [unitree.com](https://www.unitree.com/H2) |
| Arm payload (peak) | 15 kg | ~15 kg | [unitree.com](https://www.unitree.com/H2) |
| Hands | none | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2) |
| Hands | optional | H2 EDU; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2-edu) |

### Actuation & Joints

| Spec | Value | Note | Source |
|---|---|---|---|
| DoF per leg | 6 | hip 3, knee 1, ankle 2 | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| DoF per arm | 7 | shoulder 3, elbow 2, wrist 2 | [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2) |
| Waist DoF | 3 |  | [unitree.com](https://www.unitree.com/H2) |
| Head DoF | 2 |  | [unitree.com](https://www.unitree.com/H2) |
| Joint output bearing | Industrial-grade crossed roller bearings |  | [unitree.com](https://www.unitree.com/H2) |
| Joint motor | Low-inertia high-speed internal-rotor PMSM |  | [unitree.com](https://www.unitree.com/H2) |
| Max arm joint torque | 120 N·m |  | [unitree.com](https://www.unitree.com/H2) |
| Max leg joint torque | 360 N·m |  | [unitree.com](https://www.unitree.com/H2) |
| Cooling system | Local air cooling |  | [unitree.com](https://www.unitree.com/H2) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Intended use / caution | Civilian robot; keep safe distance; no dangerous modifications |  | [unitree.com](https://www.unitree.com/H2) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Manual controller | Included |  | [unitree.com](https://www.unitree.com/H2) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Bionic head with facial features | yes |  | [unitree.com](https://www.unitree.com/H2) |
| Speaker | High-power speaker | voice interaction | [unitree.com](https://www.unitree.com/H2) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Price | 29,900 USD | H2, tax and shipping excluded; H2 EDU contact sales | [unitree.com](https://www.unitree.com/H2) |
| Warranty | 8 months | H2 | [unitree.com](https://www.unitree.com/H2) |
| Warranty | 12 months | H2 EDU | [unitree.com](https://www.unitree.com/H2) |
| Sales status | shipping-now | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2) |
| Who can buy | anyone | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2) |
| Price | 29,900 USD | list price (maker price); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2) |
| Delivered price to US | 39,900 USD | before sales tax; route: seller: Toborlife (official Unitree US partner); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2) |
| Delivered price to Germany | 33,501 EUR | incl. 19% VAT; route: estimate: import; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2) |
| Route to US | reseller | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2) |
| Route to EU | reseller | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2) |
| Sellers listed | 27 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2) |
| Documented uses | Demo / showpiece | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2) |
| Price | 50,000 EUR | H2 EDU; list price (reseller price); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2-edu) |
| Price (USD equivalent) | 66,800 USD | H2 EDU; EUR list price at ECB reference rate; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2-edu) |
| Delivered price to US | 66,800 USD | H2 EDU; before sales tax; route: seller: Toborlife (official Unitree US partner); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2-edu) |
| Delivered price to Germany | 59,202 EUR | H2 EDU; incl. 19% VAT; route: seller: reichelt elektronik; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2-edu) |
| Sellers listed | 15 | H2 EDU; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2-edu) |
| Documented uses | Robotics R&D; Manipulation research | H2 EDU; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2-edu) |
| Sellers listed | 10 | H2 Plus; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2-plus) |
| Public tender price per unit | 1,030,502 SEK | University of Borås (SE), awarded 2026-08-14: 1 x Unitree H2; 1 bid(s); before VAT; winner Robolution AB; via HumanoidStore tender record (CC BY 4.0) | [ted.europa.eu](https://ted.europa.eu/en/notice/-/detail/567197-2026) |

### Payload

| Spec | Value | Note | Source |
|---|---|---|---|
| Rated payload | 7 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2) |

## Documents

- [Unitree H2 product page – H2 Parameter table](https://www.unitree.com/H2)
- [Unitree H2 SDK Development Guide – About H2 (updated 2026-09-03)](https://support.unitree.com/home/en/H2_developer/About_H2)
- [HumanoidStore datasheet – Unitree Robotics H2 (CC BY 4.0)](https://humanoidstore.co/robots/unitree-h2)
- [HumanoidStore datasheet – Unitree Robotics H2 EDU (CC BY 4.0)](https://humanoidstore.co/robots/unitree-h2-edu)
- [HumanoidStore datasheet – Unitree Robotics H2 Plus (CC BY 4.0)](https://humanoidstore.co/robots/unitree-h2-plus)

## Notes

Maker figures: 1820 x 456 x 218 mm, about 70 kg, 31 DoF (6 per leg, 7 per arm, 3 waist, 2 head), 360 Nm peak leg joint, 120 Nm arm joint, about 15 kg peak and 7 kg rated arm payload, bionic head with facial features, optional dexterous hands, 1045 mm calf plus thigh and 690 mm forearm plus upper arm. Price US$29,900 for H2; the 15 kg figure is the maker's peak value. Unitree does not publish runtime or battery capacity for the H2.

## Sources

- Official page: [unitree.com](https://www.unitree.com/H2/)
- [unitree.com](https://www.unitree.com/H2)
- [support.unitree.com](https://support.unitree.com/home/en/H2_developer/About_H2)
- [unitree.com](https://www.unitree.com/cn/H2/)
- [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2)
- [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2-edu)
- [humanoidstore.co](https://humanoidstore.co/robots/unitree-h2-plus)
- [github.com](https://github.com/unitreerobotics/unitree_sdk2)
- [github.com](https://github.com/unitreerobotics/unitree_ros/blob/master/robots/h2_description/H2.urdf)
- [github.com](https://github.com/unitreerobotics/unitree_sdk2_python)
- [github.com](https://github.com/unitreerobotics/unitree_ros)
- [github.com](https://github.com/unitreerobotics/unitree_ros2)
- [github.com](https://github.com/unitreerobotics/unitree_mujoco)
- [shop.unitree.com](https://shop.unitree.com/products/unitree-h2)
- [younginmobility.com](https://www.younginmobility.com/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-22). Source repository: https://github.com/htcrefactor/robot-catalog*
