# Unitree Robotics B2-W

> Industrial wheel-legged quadruped (B2 with wheeled feet) for long-range inspection and patrol; >40 kg walking load (120 kg standing), 15 km/h max in special configuration, ~25 km range with 40 kg.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=unitree-b2-w
- Category: Wheel-legged
- Locomotion: Wheel-legged
- Manufacturer: Unitree Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 1,098 mm |
| Width | 550 mm |
| Height | 758 mm |
| Weight | 85 kg |
| Payload | 40 kg |
| Max speed | 4.17 m/s (15.0 km/h) |
| Wheel diameter | 225 mm |
| Wheels | 4 |
| IP rating | IP67 |
| Status | Commercial |
| On-board compute | yes |
| Compute | Intel Core i5 (platform) + Intel Core i7 (user development); optional Intel Core i7 or Orin NX, up to 3 devices |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

28 values from 1 document, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Robot type | Industrial wheel-legged quadruped (B2 with wheeled feet) |  | [unitree.com](https://www.unitree.com/b2-w) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 1,098 mm | standing, approx. | [unitree.com](https://www.unitree.com/b2-w) |
| Width | 550 mm | standing, approx. | [unitree.com](https://www.unitree.com/b2-w) |
| Height (standing) | 758 mm | approx. | [unitree.com](https://www.unitree.com/b2-w) |
| Length | 950 mm | lying prone, approx. | [unitree.com](https://www.unitree.com/b2-w) |
| Width | 550 mm | lying prone, approx. | [unitree.com](https://www.unitree.com/b2-w) |
| Height (lying prone) | 450 mm | approx. | [unitree.com](https://www.unitree.com/b2-w) |
| Weight (with battery) | 85 kg | approx., total weight | [unitree.com](https://www.unitree.com/b2-w) |
| Wheel diameter | 225 mm |  | [unitree.com](https://www.unitree.com/b2-w) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Maximum speed | 15 km/h | realized in special configurations; in practice there is a speed limit for security purposes (footnote [1]) | [unitree.com](https://www.unitree.com/b2-w) |
| Maximum load (standing) | 120 kg | static standing load | [unitree.com](https://www.unitree.com/b2-w) |
| Load (walking) | >40 kg | continuous walking load | [unitree.com](https://www.unitree.com/b2-w) |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Continuous stair climbing | 20–25 cm | stairs of 20–25 cm | [unitree.com](https://www.unitree.com/b2-w) |
| Max single step (forward) | 40 cm | climb up and down stairs of 40 cm in forward direction | [unitree.com](https://www.unitree.com/b2-w) |
| Climbing angle | >45 ° |  | [unitree.com](https://www.unitree.com/b2-w) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery capacity | >2 kWh |  | [unitree.com](https://www.unitree.com/b2-w) |
| Battery voltage | 58 V |  | [unitree.com](https://www.unitree.com/b2-w) |
| Range per charge | 25 km | maximum endurance with 40 kg load; special configuration (footnote [2]) | [unitree.com](https://www.unitree.com/b2-w) |
| Range per charge | 30 km | without load, approx. | [unitree.com](https://www.unitree.com/b2-w) |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| Operating temperature | −20 to 55 °C |  | [unitree.com](https://www.unitree.com/b2-w) |
| Ingress protection | IP67 |  | [unitree.com](https://www.unitree.com/b2-w) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Computer (platform functions) | Intel Core i5 | standard configuration | [unitree.com](https://www.unitree.com/b2-w) |
| Computer (user development) | Intel Core i7 | standard configuration | [unitree.com](https://www.unitree.com/b2-w) |
| Optional compute | Intel Core i7 or NVIDIA Orin NX (multiple brands/models), up to 3 devices | optional configuration | [unitree.com](https://www.unitree.com/b2-w) |
| OTA updates | Continuous OTA software upgrade and update |  | [unitree.com](https://www.unitree.com/b2-w) |

### Actuation & Joints

| Spec | Value | Note | Source |
|---|---|---|---|
| Maximum wheel speed | 50 rad/s |  | [unitree.com](https://www.unitree.com/b2-w) |
| Maximum wheel torque | 40 N·m |  | [unitree.com](https://www.unitree.com/b2-w) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Intended use | Civilian robot; dangerous modifications or hazardous use prohibited |  | [unitree.com](https://www.unitree.com/b2-w) |

## Documents

- [Unitree B2-W product page (spec table)](https://www.unitree.com/b2-w)

## Notes

Unitree B2-W page (checked 2026-11-17): standing about 1098 x 550 x 758 mm, about 85 kg with battery, wheel diameter 225 mm, battery >2 kWh at 58 V (no Wh figure), max speed 15 km/h (4.17 m/s, special configurations), 25 km with 40 kg / about 30 km unloaded, walking load >40 kg and standing load 120 kg, IP67, -20 to 55 C. No runtime in hours and no DoF are published; battery_wh and runtime_h stay empty.

## Sources

- Official page: [unitree.com](https://www.unitree.com/b2-w)
- [github.com](https://github.com/unitreerobotics/unitree_sdk2)
- [github.com](https://github.com/unitreerobotics/unitree_ros/blob/master/robots/b2w_description/urdf/b2w_description.urdf)
- [github.com](https://github.com/unitreerobotics/unitree_sdk2_python)
- [github.com](https://github.com/unitreerobotics/unitree_ros)
- [github.com](https://github.com/unitreerobotics/unitree_ros2)
- [github.com](https://github.com/unitreerobotics/unitree_mujoco)
- [younginmobility.com](https://www.younginmobility.com/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-18). Source repository: https://github.com/htcrefactor/robot-catalog*
