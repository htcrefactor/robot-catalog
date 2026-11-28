# Galbot G1

> Galbot's wheeled bimanual humanoid on a four-wheel omnidirectional base with a lifting torso, used in unmanned retail stores and warehouses across China.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=galbot-g1
- Category: Humanoid
- Locomotion: Wheeled
- Manufacturer: Galbot (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Height | 1,730 mm |
| Weight | 92.5 kg |
| Payload | 5 kg |
| Max speed | 1.5 m/s (5.4 km/h) |
| Degrees of freedom | 21 |
| Runtime | 8 h |
| Battery | 1,440 Wh |
| IP rating | IP54 |
| Status | Commercial |
| On-board compute | NVIDIA Jetson AGX Orin 64GB |
| Compute | 275 TOPS |
| Sensors | Stereo camera (head), RGB cameras x4 (torso), Depth cameras x2 (wrists), 6-axis force/torque sensors x2 (wrists), 3D LiDAR x1 (base), Ultrasonic sensors x8 (base), IMU x2, Linear 4-microphone array x2 |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

15 values from 1 document, checked against maker sources on 2026-11-13.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Form factor | wheeled (bimanual torso on a wheeled base) | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galbot-g1) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Height (standing) | 173 cm | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galbot-g1) |
| Weight | 92.5 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galbot-g1) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total degrees of freedom | 21 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galbot-g1) |
| Top speed | 1.5 m/s | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galbot-g1) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Runtime per charge | 480 min | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galbot-g1) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Hands | optional | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galbot-g1) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Sales status | b2b-only | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galbot-g1) |
| Who can buy | business | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galbot-g1) |
| Price | 87,000 USD | list price (maker price); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galbot-g1) |
| Route to US | reseller | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galbot-g1) |
| Route to EU | reseller | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galbot-g1) |
| Sellers listed | 3 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galbot-g1) |
| Documented uses | Robotics R&D; Manipulation research; Teaching / education; Demo / showpiece; Real work / logistics | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galbot-g1) |

### Payload

| Spec | Value | Note | Source |
|---|---|---|---|
| Rated payload | 10 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galbot-g1) |

## Documents

- [HumanoidStore datasheet – Galbot G1 (CC BY 4.0)](https://humanoidstore.co/robots/galbot-g1)

## Notes

Maker spec panel (galbot.com/g1): max height 1730 mm (leg lift 650 mm), 92.5 kg, payload 5 kg per arm / 10 kg total at the wrist, 21 DoF (neck 2 + arms 7x2 + waist 3 + legs 2, excluding chassis and end effectors), 8 h working time with 3.5 h adapter charging, 48 V 30 Ah battery (=1440 Wh, derived from V x Ah), IP54, 4-wheel omnidirectional chassis 600/600/625 mm, 1.5 m/s, NVIDIA AGX Orin 64GB / 275 TOPS, 0-40 C. No price on the maker site; HumanoidStore's 87,000 USD list price was removed (aggregator).

## Sources

- Official page: [galbot.com](https://www.galbot.com/g1/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-28). Source repository: https://github.com/htcrefactor/robot-catalog*
