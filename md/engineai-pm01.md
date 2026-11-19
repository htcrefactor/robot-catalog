# EngineAI PM01

> Lightweight, open-source research/education humanoid (2026 Education Edition specs); speed listed as >2 m/s hardware-supported; 320° waist rotation.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=engineai-pm01
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: EngineAI (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 295 mm |
| Width | 540 mm |
| Height | 1,400 mm |
| Weight | 44.5 kg |
| Max speed | 2 m/s (7.2 km/h) |
| Degrees of freedom | 24 |
| Runtime | 2 h |
| Status | Commercial |
| API | yes |
| SDK | yes |
| SDK name | EngineAI ROS 2 deployment framework (open source) |
| ROS | yes |
| On-board compute | yes |
| Compute | NVIDIA Jetson Orin NX 16GB |
| Sensors | Wide-FOV binocular camera (head), Wide-FOV binocular camera (waist), 3D LiDAR (Navigation Edition) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

51 values from 2 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Editions | 2026 Education Edition; 2026 Navigation Edition |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| Form factor | mid-size | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-pm01) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Height | 1,400 mm | 1400 (H) x 540 (W) x 253 (D) mm, Education Edition | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| Width | 540 mm |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| Depth | 253 mm | Education; Navigation Edition 295 mm | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| Weight (with battery) | 44 kg | approx.; Navigation Edition approx. 44.5 kg | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| Leg length (thigh + lower leg) | 686.5 mm |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| Arm span (fully extended) | 1,440 mm |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| Single-arm length | 470 mm | upper arm + forearm | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| Structural material | Aviation aluminium |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| Height (standing) | 140 cm | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-pm01) |
| Weight | 44 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-pm01) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total DoF | 24 | number of joint motors | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| Moving speed | >2 m/s | hardware supported | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Smart battery quick disassembly | yes |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| Battery life | 2 h |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charging power | 54.6 V / 4.5 A |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| Charging duration | 2 h | full charge | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Cameras | Ultra-wide FOV binocular camera x2 (head & waist) |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| Binocular cameras | 2 |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| 3D LiDAR | Navigation Edition only |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| Voice interaction | yes |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Base computing | 8-core high-performance CPU |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| High computing module | NVIDIA Jetson Orin NX (16G) |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| Secondary development | Open-source training and ROS deployment code repositories; low-level hardware interfaces |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| ROS deployment framework | yes | EngineAI ROS deployment framework, dual-mode | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Hands | optional | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-pm01) |

### Actuation & Joints

| Spec | Value | Note | Source |
|---|---|---|---|
| Neck DoF | 1 |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| DoF per leg | 6 |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| Waist DoF | 1 |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| DoF per arm | 5 |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| Waist rotation | >300 ° | highlights also quote 320° | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| Hip joint range | R -29 to +134; P -180 to +140; Y -90 to +230 ° |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| Knee joint range | -30 to +137 ° |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| Joint output bearing | Industrial-grade high-precision crossed roller bearing |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| Joint motor | Ultra-high-speed internal-rotor PMSM |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| Max torque | 164 N·m | detailed specs; highlights quote 130 N·m integrated joint module | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| Peak torque density | 145 N·m/kg |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| Cooling | Super air-cooled heat dissipation |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Controller | Handheld touchscreen remote controller |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Chest touch screen | Education Edition only | interactive core display | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |
| Lighting | Signature Star Halo ring light |  | [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Sales status | shipping-now | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-pm01) |
| Who can buy | anyone | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-pm01) |
| Price | 26,000 USD | list price (maker price); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-pm01) |
| Delivered price to US | 37,276 USD | before sales tax; route: estimate: import; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-pm01) |
| Delivered price to Germany | 28,939 EUR | incl. 19% VAT; route: estimate: import; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-pm01) |
| Route to US | reseller | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-pm01) |
| Route to EU | reseller | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-pm01) |
| Sellers listed | 4 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-pm01) |
| Documented uses | Robotics R&D; Teaching / education; Learn and tinker | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-pm01) |

## Documents

- [EngineAI PM01 product page – detailed specifications (2026 Education / Navigation Editions)](https://en.engineai.com.cn/product-pm01.html)
- [HumanoidStore datasheet – EngineAI PM01 (CC BY 4.0)](https://humanoidstore.co/robots/engineai-pm01)

## Notes

Maker product page (engineai.com.cn/product-pm01.html, Chinese page carries the numeric table): 1400 (H) x 540 (W) x 295 (D) mm, about 44.5 kg, 24 total DoF with a waist that rotates 320 degrees, walking speed over 2 m/s with hardware support, 10,000 mAh battery for about 2 h and about 2 h to full charge, NVIDIA Jetson Orin NX (16G) onboard, head and waist wide-angle binocular cameras, 3D LiDAR on the navigation edition, open SDK/ROS 2 development framework. Earlier record had depth 253 mm and 44 kg; the maker page values are recorded. Maker publishes no list price, so the HumanoidStore figure stands with its own label.

## Sources

- Official page: [engineai.com.cn](https://www.engineai.com.cn/product-pm01.html)
- [en.engineai.com.cn](https://en.engineai.com.cn/product-pm01.html)
- [humanoidstore.co](https://humanoidstore.co/robots/engineai-pm01)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-19). Source repository: https://github.com/htcrefactor/robot-catalog*
