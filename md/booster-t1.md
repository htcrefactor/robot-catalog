# Booster Robotics T1

> Booster Robotics' 1.18 m developer humanoid that won the RoboCup AdultSize 2025 title and is now superseded by T2 and K1.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=booster-t1
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: Booster Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Height | 1,180 mm |
| Weight | 30 kg |
| Max speed | 1 m/s (3.6 km/h) |
| Degrees of freedom | 23 |
| Runtime | 2 h |
| Status | Discontinued |
| SDK | yes |
| On-board compute | yes |
| Compute | NVIDIA Jetson AGX Orin (200 TOPS) in Basic; Standard and Customized add an Intel i7 board |
| Sensors | Depth camera, Microphone array, Speaker |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

66 values from 5 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Versions | Basic; Standard | differ in computing platform | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |
| Form factor | mid-size | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t1) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Height (standing upright) | 1.18 m |  | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |
| Weight | 30 kg | about | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total DoF | 23 |  | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |
| Walking speed | 1 m/s |  | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |
| Turning speed | 1.5 rad/s |  | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |
| Motion capabilities | Omnidirectional walking; disturbance resistance; self-rising |  | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/overview/) |
| Top speed | 0.97 m/s | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t1) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery life | 2 h |  | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |
| Cycle life | ≥500 cycles |  | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |
| Slide-in battery pack | yes | installed in torso socket | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/quick-start/) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charging time | ≤2 h |  | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| Environmental adaptability | -10 to 45 °C |  | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |
| Operating humidity | 5 to 90 % | non-condensing | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Depth camera | 1 | in head | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |
| Microphone array | yes | in head | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Computing platform (Basic) | 1x NVIDIA Jetson AGX Orin 32GB | motion control + perception on one board | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |
| Computing platform (Standard) | Intel i7 (Express-i7) motion board + Jetson AGX Orin 32GB perception board |  | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |
| Orin CPU | 8-core Cortex-A78AE @ 2 GHz |  | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |
| Orin GPU | Tensor Core GPU @ 930 MHz |  | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |
| AI performance | 200 TOPS | per Jetson AGX Orin board | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |
| Motion control board CPU (Standard) | Intel i7, 6P + 8E cores, P 4.80 GHz / E 3.90 GHz |  | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |
| Memory | 32 GB | Orin boards; i7 motion board 8 GB | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |
| Storage | 512 GB | each board | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Wired network | 2x 1000M | each board | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |
| Wi-Fi | Wi-Fi 6 |  | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |
| Bluetooth | 5.2 |  | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Hands | optional | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t1) |

### Actuation & Joints

| Spec | Value | Note | Source |
|---|---|---|---|
| DoF per leg | 6 | hip pitch/roll/yaw, knee, ankle up/down | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/overview/) |
| DoF per arm | 4 | expandable; shoulder pitch/roll/yaw + elbow | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |
| Waist DoF | 1 | yaw | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |
| Head DoF | 2 | yaw + pitch | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |
| Joint limit – Head yaw | -58 to 58 ° | right side mirrored | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) · Joint ID and limits |
| Joint limit – Head pitch | -18 to 47 ° | right side mirrored | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) · Joint ID and limits |
| Joint limit – L shoulder pitch | -188 to 68 ° | right side mirrored | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) · Joint ID and limits |
| Joint limit – L shoulder roll | -94 to 88 ° | right side mirrored | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) · Joint ID and limits |
| Joint limit – Shoulder yaw | -128 to 128 ° | right side mirrored | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) · Joint ID and limits |
| Joint limit – L elbow | -120 to 2 ° | right side mirrored | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) · Joint ID and limits |
| Joint limit – Waist yaw | -58 to 58 ° | right side mirrored | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) · Joint ID and limits |
| Joint limit – Hip pitch | -118 to 118 ° | right side mirrored | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) · Joint ID and limits |
| Joint limit – L hip roll | -21 to 88 ° | right side mirrored | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) · Joint ID and limits |
| Joint limit – Hip yaw | -58 to 58 ° | right side mirrored | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) · Joint ID and limits |
| Joint limit – Knee | 0 to 123 ° | right side mirrored | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) · Joint ID and limits |
| Joint limit – Ankle up | -23 to 49 ° | right side mirrored | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) · Joint ID and limits |
| Joint limit – Ankle down | -24 to 45 ° | right side mirrored | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) · Joint ID and limits |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Emergency stop | 1 | hard E-stop; press to activate, press again to release; restart required | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |
| Certification standards | CE / FCC |  | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |
| Walking noise | ≤70 dB |  | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |
| Safety protection | Automatic damping mode in uncontrolled states |  | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/overview/) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Controller | Joystick (PREP / WALK / DAMP modes) |  | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/quick-start/) |
| Modes | PREP; WALK; DAMP |  | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/quick-start/) |
| Boot time | 1 min | about one minute after power-on | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/quick-start/) |
| Built-in agents | Booster (motions); Soccer; Hi Chat (voice); Teach; Dance | 7-DoF version lacks soccer/teach/dance agents | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/overview/) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Speaker | 1 |  | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |
| Auditory alerts | Low battery alert; joint overheat alert |  | [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Sales status | shipping-now | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t1) |
| Who can buy | anyone | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t1) |
| Price | 39,795 EUR | list price (reseller price); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t1) |
| Price (USD equivalent) | 44,670 USD | EUR list price at ECB reference rate; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t1) |
| Delivered price to Germany | 39,795 EUR | incl. 19% VAT; route: seller: OpenELAB; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t1) |
| Route to US | unclear | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t1) |
| Route to EU | reseller | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t1) |
| Sellers listed | 4 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t1) |
| Documented uses | Robotics R&D | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t1) |

### Payload

| Spec | Value | Note | Source |
|---|---|---|---|
| Rated payload | 5 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t1) |

## Documents

- [Booster T1 Product Manual – Specifications](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/)
- [Booster T1 Product Manual – Overview](https://docs.booster.tech/docs/product-manual/t1/getting-started/overview/)
- [Booster T1 Product Manual – Quick Start](https://docs.booster.tech/docs/product-manual/t1/getting-started/quick-start/)
- [Booster T1 Product Manual – Safety and Warnings](https://docs.booster.tech/docs/product-manual/t1/getting-started/safety-warnings/)
- [HumanoidStore datasheet – Booster Robotics T1 (CC BY 4.0)](https://humanoidstore.co/robots/booster-t1)

## Notes

Maker T1 manual (docs.booster.tech > T1 > Specifications): height 1.18 m, ~30 kg, 23 DoF (6 per leg, 4 per arm expandable, 1 waist, 2 head), walking speed 1 m/s, turning 1.5 rad/s, battery life 2 h with <=2 h charge, -10 to 45 C, 5-90% humidity, depth camera + mic array + speaker, Wi-Fi 6 / BT 5.2, CE/FCC, emergency stop; Basic ships the Jetson AGX Orin (200 TOPS), Standard and Customized add an Intel i7 board. The printed spec sheet on the maker's old product page adds 10.5 Ah battery, 130 N.m peak torque and 6-mic array; pack voltage is not published so battery_wh stays empty. The product page booster.tech/booster-t1 now redirects to the T2/K1 lineup, so status recorded as Discontinued. Price is the HumanoidStore figure, not a maker price.

## Sources

- Official page: [docs.booster.tech](https://docs.booster.tech/docs/product-manual/t1/getting-started/specifications/)
- [booster.tech](https://www.booster.tech/booster-t1/)
- [humanoidstore.co](https://humanoidstore.co/robots/booster-t1)
- [github.com](https://github.com/BoosterRobotics/booster_robotics_sdk)
- [github.com](https://github.com/BoosterRobotics/booster_assets/blob/main/robots/T1/T1_23dof.urdf)
- [github.com](https://github.com/BoosterRobotics/booster_assets/blob/main/robots/T1/T1_23dof.xml)
- [github.com](https://github.com/BoosterRobotics/booster_assets)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-19). Source repository: https://github.com/htcrefactor/robot-catalog*
