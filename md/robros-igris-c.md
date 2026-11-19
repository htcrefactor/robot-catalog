# Robros IGRIS-C

> ROBROS' 154 cm bipedal indoor humanoid for research, pilot deployment and education, with 11-DOF hands, whole-body force limiting and a master-arm teleoperation kit.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=robros-igris-c
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: Robros (South Korea)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 300 mm |
| Width | 440 mm |
| Height | 1,540 mm |
| Weight | 56 kg |
| Payload | 6 kg |
| Max speed | 1 m/s (3.6 km/h) |
| Degrees of freedom | 43 |
| Runtime | 2 h |
| Battery | 816 Wh |
| Status | Commercial |
| SDK | yes |
| SDK name | C++ and Python APIs over Cyclone DDS on Linux; master arm + control app + data platform |
| On-board compute | Intel Core i7 + NVIDIA Jetson Orin Nano (v1.0.5 docs) / Intel Core i7 (v2.1.1 docs) |
| Sensors | GXIVISION LSM22100 stereo eye camera, Intel RealSense D435i RGBD head camera, RGB end-effector cameras (one per hand), MicroStrain 3DM-CV7-AR IMU |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

15 values from 1 document, checked against maker sources on 2026-11-13.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Form factor | mid-size | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robros-igris-c) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Height (standing) | 154 cm | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robros-igris-c) |
| Weight | 56 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robros-igris-c) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total degrees of freedom | 53 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robros-igris-c) |
| Top speed | 1 m/s | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robros-igris-c) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Runtime per charge | 120 min | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robros-igris-c) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Hands | included | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robros-igris-c) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Sales status | b2b-only | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robros-igris-c) |
| Who can buy | research | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robros-igris-c) |
| Price | 100,000 USD | list price (maker price); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robros-igris-c) |
| Route to US | unclear | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robros-igris-c) |
| Route to EU | unclear | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robros-igris-c) |
| Sellers listed | 0 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robros-igris-c) |
| Documented uses | Robotics R&D; Manipulation research; Teaching / education | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robros-igris-c) |

### Payload

| Spec | Value | Note | Source |
|---|---|---|---|
| Rated payload | 6 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robros-igris-c) |

## Documents

- [HumanoidStore datasheet – Robros IGRIS-C (CC BY 4.0)](https://humanoidstore.co/robots/robros-igris-c)

## Notes

Maker product page: 154 cm, 56 kg, 17,000 mAh 48 V battery (=816 Wh, derived), 2.5 h charge, 53 DOF per the maker docs (legs 6 x 2, arms 7 x 2, waist 3, neck 2, hands 11 x 2 where each hand has 6 active + 5 passive DoF); the marketing page's DOF list omits the hand joints and adds up to 43. CONFLICT: the developer docs (v1.0.5 and v2.1.1, updated 2026-06-24) give 60 kg and 1540 x 440 x 300 mm while the product page gives 56 kg; the product page figure is used here and the docs figure is recorded. Max joint torque 150 Nm, 6 kg payload with both arms, Linux/Cyclone DDS with C++ and Python APIs, RGB stereo + RealSense D435i depth head cameras and per-hand RGB cameras, 6-axis IMU, Wi-Fi AP and BLE, force limiting and collision detection, emergency stop, industrial Class A, sold in Korea with global inquiries. Max speed and runtime are not published. ROBROS reported building 36 units and selling 18 by end-August 2026.

## Sources

- Official page: [robros.co.kr](https://www.robros.co.kr/en/igrisc)
- [robros.co.kr](https://www.robros.co.kr/ko/developers/v2.1.1/c304d82d-d289-40e1-a6dd-036e028279de/Overview)
- [humanoidstore.co](https://humanoidstore.co/robots/robros-igris-c)
- [robros.co.kr](https://www.robros.co.kr/ko)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-19). Source repository: https://github.com/htcrefactor/robot-catalog*
