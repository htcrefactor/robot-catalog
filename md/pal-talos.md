# PAL Robotics TALOS

> PAL's torque-controlled industrial research humanoid: 1.75 m, 95 kg, 32 DoF, 6 kg per arm and 1.5 h of walking, with EtherCAT control at 2 kHz.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=pal-talos
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: PAL Robotics (Spain)
- Verification: official — checked against a maker source
- Data source: Maker sources (verified 2026-11-17)

## Core specs

| Field | Value |
|---|---|
| Height | 1,750 mm |
| Weight | 95 kg |
| Payload | 6 kg |
| Max speed | 0.83 m/s (3.0 km/h) |
| Degrees of freedom | 32 |
| Runtime | 1.5 h |
| Battery | 1,080 Wh |
| Status | Commercial |
| Price | PAL publishes no price; the earlier 1,000,000 EUR figure came from a reseller listing |
| Sensors | Full torque-sensor feedback in all joints (except head, wrists and grippers), 4x 6-axis F/T sensors at wrists and ankles, AHRS/IMU at 1 kHz |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

18 values from 1 document, checked against maker sources on 2026-11-13.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Form factor | full-size | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-talos) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Height (standing) | 175 cm | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-talos) |
| Weight | 95 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-talos) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total degrees of freedom | 32 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-talos) |
| Top speed | 0.83 m/s | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-talos) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Runtime per charge | 90 min | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-talos) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Hands | fixed-grippers | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-talos) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Sales status | shipping-now | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-talos) |
| Who can buy | research | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-talos) |
| Price | 1,000,000 EUR | list price (maker price); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-talos) |
| Price (USD equivalent) | 1,122,500 USD | EUR list price at ECB reference rate; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-talos) |
| Delivered price to US | 1,236,317 USD | before sales tax; route: estimate: import; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-talos) |
| Delivered price to Germany | 1,190,107 EUR | incl. 19% VAT; route: estimate: domestic delivery; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-talos) |
| Route to US | direct | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-talos) |
| Route to EU | direct | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-talos) |
| Sellers listed | 1 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-talos) |
| Documented uses | Robotics R&D; Manipulation research | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-talos) |

### Payload

| Spec | Value | Note | Source |
|---|---|---|---|
| Rated payload | 6 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/pal-talos) |

## Documents

- [HumanoidStore datasheet – PAL Robotics TALOS (CC BY 4.0)](https://humanoidstore.co/robots/pal-talos)

## Notes

PAL's TALOS page and datasheet (checked 2026-11-17): 175 cm, 95 kg, 32 DoF (6 per leg, 7 per arm, 1 per gripper, 2 waist, 2 neck), 6 kg arm payload fully extended, 1.5 h walking or 3 h standby on a 1,080 Wh lithium-ion pack, Ubuntu LTS, ROS and ros_control. The 3 km/h walking speed recorded here comes from PAL's 2016 launch post; the product page itself lists no speed.

## Sources

- Official page: [pal-robotics.com](https://pal-robotics.com/robot/talos/)
- [pal-robotics.com](https://pal-robotics.com/wp-content/uploads/2025/09/TALOS-DataSheet-1.pdf)
- [pal-robotics.com](https://pal-robotics.com/wp-content/uploads/2024/05/Datasheet-TALOS.pdf)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-17). Source repository: https://github.com/htcrefactor/robot-catalog*
