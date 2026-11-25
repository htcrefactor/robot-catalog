# Stanford University ToddlerBot

> ToddlerBot is Stanford's open-source, 3D-printed 56 cm humanoid for loco-manipulation research, with 30 active DOF, a Jetson Orin NX and a build cost under USD 6,000.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=stanford-robotis-toddlerbot
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: Stanford University (United States)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Height | 600 mm |
| Weight | 2.7 kg |
| Payload | 1.5 kg |
| Degrees of freedom | 30 |
| Released | 2025 |
| Status | Research |
| Price | bill of materials under USD 6,000 for the open-source build (maker paper), not a sale price |
| SDK | yes |
| SDK name | Open-source: Python library (pip installable), RL/DP training, teleoperation interface; design files under CC BY-NC-SA |
| On-board compute | NVIDIA Jetson Orin NX 16GB |
| Sensors | 2x fisheye cameras, IMU (chest), Speaker, 2x microphones |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

17 values from 1 document, checked against maker sources on 2026-11-13.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Form factor | compact | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/stanford-robotis-toddlerbot) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Height (standing) | 56 cm | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/stanford-robotis-toddlerbot) |
| Weight | 3.4 kg | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/stanford-robotis-toddlerbot) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total degrees of freedom | 30 | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/stanford-robotis-toddlerbot) |
| Top speed | 0.25 m/s | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/stanford-robotis-toddlerbot) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Runtime per charge | 19 min | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/stanford-robotis-toddlerbot) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Hands | fixed-grippers | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/stanford-robotis-toddlerbot) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Sales status | shipping-now | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/stanford-robotis-toddlerbot) |
| Who can buy | anyone | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/stanford-robotis-toddlerbot) |
| Price | 6,000 USD | list price (maker price); HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/stanford-robotis-toddlerbot) |
| Delivered price to US | 6,011 USD | before sales tax; route: estimate: domestic delivery; HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/stanford-robotis-toddlerbot) |
| Delivered price to Germany | 6,483 EUR | incl. 19% VAT; route: estimate: import; HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/stanford-robotis-toddlerbot) |
| Route to US | direct | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/stanford-robotis-toddlerbot) |
| Route to EU | direct | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/stanford-robotis-toddlerbot) |
| Sellers listed | 2 | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/stanford-robotis-toddlerbot) |
| Documented uses | Robotics R&D; Manipulation research | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/stanford-robotis-toddlerbot) |

### Payload

| Spec | Value | Note | Source |
|---|---|---|---|
| Rated payload | 1.484 kg | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/stanford-robotis-toddlerbot) |

## Documents

- [HumanoidStore datasheet – Stanford University ToddlerBot (CC BY 4.0)](https://humanoidstore.co/robots/stanford-robotis-toddlerbot)

## Notes

Maker paper (CoRL 2025) and project site: 0.56 m tall, 3.4 kg, 30 active DOF excluding end effectors (7 per arm, 6 per leg, 2 neck, 2 waist), 2 fisheye cameras, IMU in the chest, speaker, 2 microphones, Jetson Orin NX 16GB, entirely 3D-printed with off-the-shelf Dynamixel motors, total BOM cost under USD 6,000, design under CC BY-NC-SA and code under MIT, with zero-shot sim-to-real transfer and a teleoperation interface; two end-effector designs (parallel jaw gripper and compliant palm) swap in two minutes. The catalog's earlier payload (1.484 kg), max speed (0.25 m/s) and runtime (0.32 h) were HumanoidStore figures that the maker paper does not state in those terms, so they were removed rather than kept on an aggregator's authority.

## Sources

- Official page: [toddlerbot.github.io](https://toddlerbot.github.io/)
- [arxiv.org](https://arxiv.org/abs/2502.00893)
- [github.com](https://github.com/hshi74/toddlerbot)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-25). Source repository: https://github.com/htcrefactor/robot-catalog*
