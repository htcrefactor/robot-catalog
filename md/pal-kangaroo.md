# PAL Robotics Kangaroo

> PAL's configurable biped for locomotion research: 1.6 m, 50-65 kg, 14-40 DoF depending on arm and leg configuration, with a 976 Wh pack and ROS 2 tooling.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=pal-kangaroo
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: PAL Robotics (Spain)
- Verification: official — checked against a maker source
- Data source: Maker sources (verified 2026-11-17)

## Core specs

| Field | Value |
|---|---|
| Height | 1,600 mm |
| Weight | 50 kg |
| Payload | 3 kg |
| Degrees of freedom | 14 |
| Battery | 976 Wh |
| Status | Commercial |
| On-board compute | 2x Intel i7 (control PC and multimedia PC) |
| Compute | 32 GB RAM and 1 TB SSD each; optional NVIDIA Jetson GPU; 2x WiFi 6 |
| Sensors | 4x RGB-D cameras, IMU and AHRS at 1 kHz, 6-axis F/T sensor on wrists and feet (add-ons), Integrated force sensors in leg actuators |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

13 values from 1 document, checked against maker sources on 2026-11-13.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Form factor | mid-size | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-kangaroo) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Height (standing) | 160 cm | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-kangaroo) |
| Weight | 55 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-kangaroo) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total degrees of freedom | 28 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-kangaroo) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Runtime per charge | 180 min | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-kangaroo) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Hands | optional | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-kangaroo) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Sales status | shipping-now | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-kangaroo) |
| Who can buy | research | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-kangaroo) |
| Route to US | direct | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-kangaroo) |
| Route to EU | direct | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-kangaroo) |
| Sellers listed | 1 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-kangaroo) |
| Documented uses | Robotics R&D; Manipulation research | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-kangaroo) |

### Payload

| Spec | Value | Note | Source |
|---|---|---|---|
| Rated payload | 5 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-kangaroo) |

## Documents

- [HumanoidStore datasheet – PAL Robotics Kangaroo (CC BY 4.0)](https://humanoidstore.co/robots/pal-kangaroo)

## Notes

PAL's Kangaroo page (checked 2026-11-17): 1.60 m, 50-65 kg (recorded at 50 kg), total DoF 14-40 depending on platform configuration with 6 DoF per leg, 2 torso DoF and 4, 5 or 7 DoF arms; 3 kg payload with 7-DoF arms fully extended and 25 kg bimanual; 15 Ah 63 V battery (976 Wh), EtherCAT loop at 2 kHz, Ubuntu LTS with ROS 2. Speed and runtime are not published.

## Sources

- Official page: [pal-robotics.com](https://pal-robotics.com/robot/kangaroo/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-19). Source repository: https://github.com/htcrefactor/robot-catalog*
