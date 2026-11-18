# Pollen Robotics Reachy 2

> Pollen's open-source bimanual humanoid for embodied AI: 7-DoF arms and a 3-DoF neck on an omnidirectional base, 3 kg per arm, ROS 2 and a Python SDK, height adjustable 136-166 cm.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=pollen-reachy-2
- Category: Humanoid
- Locomotion: Wheeled
- Manufacturer: Pollen Robotics (France)
- Verification: official — checked against a maker source
- Data source: Maker sources (verified 2026-11-17)

## Core specs

| Field | Value |
|---|---|
| Height | 1,660 mm |
| Weight | 50 kg |
| Payload | 3 kg |
| Battery | 840 Wh |
| Status | Commercial |
| Price | Pollen sells through sales quotes and publishes no price; about 70,000 USD was reported at the 2025 Hugging Face acquisition |
| Compute | Onboard CPU running the Reachy stack; EtherCAT low-level loop at 500 Hz; ROS 2 Humble with a Python SDK |
| Sensors | 2x IMX296 global-shutter RGB cameras, Luxonis OAK-FFC ToF depth sensor, Orbbec Gemini 336 RGB-D torso camera, RPLIDAR S2, Hall sensors and IMU on each wheel |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

18 values from 1 document, checked against maker sources on 2026-11-13.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Form factor | wheeled (bimanual torso on a wheeled base) | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pollen-reachy-2) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Height (standing) | 166 cm | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pollen-reachy-2) |
| Weight | 50 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pollen-reachy-2) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total degrees of freedom | 17 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pollen-reachy-2) |
| Top speed | 1.86 m/s | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pollen-reachy-2) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Runtime per charge | 480 min | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pollen-reachy-2) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Hands | optional | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pollen-reachy-2) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Sales status | shipping-now | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pollen-reachy-2) |
| Who can buy | anyone | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pollen-reachy-2) |
| Price | 70,000 EUR | list price (maker price); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pollen-reachy-2) |
| Price (USD equivalent) | 70,000 USD | EUR list price at ECB reference rate; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pollen-reachy-2) |
| Delivered price to US | 87,353 USD | before sales tax; route: estimate: import; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pollen-reachy-2) |
| Delivered price to Germany | 83,407 EUR | incl. 19% VAT; route: estimate: domestic delivery; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pollen-reachy-2) |
| Route to US | direct | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pollen-reachy-2) |
| Route to EU | direct | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pollen-reachy-2) |
| Sellers listed | 2 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pollen-reachy-2) |
| Documented uses | Robotics R&D; Manipulation research | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pollen-reachy-2) |

### Payload

| Spec | Value | Note | Source |
|---|---|---|---|
| Rated payload | 3 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pollen-reachy-2) |

## Documents

- [HumanoidStore datasheet – Pollen Robotics Reachy 2 (CC BY 4.0)](https://humanoidstore.co/robots/pollen-reachy-2)

## Notes

Pollen's datasheet and docs (checked 2026-11-17): height adjustable 136-166 cm (recorded at the top), about 50 kg, 7-DoF arms with about 3 kg payload per arm, 3-DoF neck, so 17 DoF for arms plus neck, three omniwheels with LiDAR, LiFePO4 pack at 24 V 35 Ah (840 Wh computed as V x Ah), ROS 2 Humble and a Python SDK. Top speed and runtime per charge are not published.

## Sources

- Official page: [pollen-robotics.com](https://www.pollen-robotics.com/reachy/)
- [pollen-robotics.com](https://pollen-robotics.com/reachy-2/)
- [pollen-robotics.com](https://pollen-robotics.com/assets/reachy2/datasheets/reachy2-dual-arm-mobile-base.pdf)
- [docs.pollen-robotics.com](https://docs.pollen-robotics.com/hardware-guide/specifications/general/)

Listed by these directories (discovery only, never used as a spec source):

- [robopear.com](https://robopear.com/robots/pollen-reachy-2)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-18). Source repository: https://github.com/htcrefactor/robot-catalog*
