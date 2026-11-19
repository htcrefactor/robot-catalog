# Unitree Robotics H1-2

> The H1-2 update of Unitree's full-size humanoid: 27 DoF, 7-DoF arms and a 21 kg peak arm payload, for heavier manipulation than the H1.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=unitree-h1-2
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: Unitree Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 287 mm |
| Width | 510 mm |
| Height | 1,788 mm |
| Weight | 70 kg |
| Payload | 21 kg |
| Max speed | 2 m/s (7.2 km/h) |
| Degrees of freedom | 27 |
| Battery | 864 Wh |
| Released | 2024 |
| Status | Commercial |
| API | yes |
| SDK | yes |
| SDK name | unitree_sdk2 |
| ROS | yes |
| On-board compute | yes |
| Compute | Intel Core i5 (platform) + Intel Core i7 (user development); up to 3 optional Orin NX modules |
| Sensors | 3D LiDAR, Depth camera |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

14 values from 1 document, checked against maker sources on 2026-11-13.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Form factor | full-size | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1-2) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Height (standing) | 178 cm | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1-2) |
| Weight | 70 kg | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1-2) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total degrees of freedom | 27 | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1-2) |
| Top speed | 2 m/s | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1-2) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Runtime per charge | 120 min | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1-2) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Hands | optional | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1-2) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Sales status | discontinued | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1-2) |
| Who can buy | research | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1-2) |
| Price | 128,900 USD | list price (maker price); HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1-2) |
| Route to US | unclear | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1-2) |
| Route to EU | unclear | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1-2) |
| Sellers listed | 4 | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1-2) |

### Payload

| Spec | Value | Note | Source |
|---|---|---|---|
| Rated payload | 7 kg | HumanoidStore open data (CC BY 4.0), checked 2026-09 | [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1-2) |

## Documents

- [HumanoidStore datasheet – Unitree Robotics H1-2 (CC BY 4.0)](https://humanoidstore.co/robots/unitree-h1-2)

## Notes

Maker figures: about 178 cm, about 70 kg, (1503+285) x 510 x 287 mm, 27 DoF total (6 per leg, 7 per arm), 2 m/s, 21 kg peak and 7 kg rated arm load, 120 Nm shoulder and elbow, 30 Nm wrist, 360 Nm knee and 220 Nm hip and waist, 864 Wh (15 Ah, 67.2 V) battery, optional Dex5-1 hands, 3D LiDAR plus depth camera. The 21 kg figure is the maker's peak value. Unitree does not publish a price or runtime for the H1-2; catalogue values are not maker figures.

## Sources

- Official page: [unitree.com](https://www.unitree.com/h1/)
- [unitree.com](https://www.unitree.com/h1)
- [humanoidstore.co](https://humanoidstore.co/robots/unitree-h1-2)
- [github.com](https://github.com/unitreerobotics/unitree_ros/blob/master/robots/h1_2_description/h1_2.urdf)
- [younginmobility.com](https://www.younginmobility.com/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-19). Source repository: https://github.com/htcrefactor/robot-catalog*
