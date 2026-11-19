# Direct Drive Tech DIABLO

> Self-balancing two-wheel-legged open development platform with six direct-drive joints; 4 kg payload standing, 80 kg in crouched mode, near-silent operation.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=direct-drive-tech-diablo
- Category: Wheel-legged
- Locomotion: Wheel-legged
- Manufacturer: Direct Drive Tech (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 540 mm |
| Width | 371 mm |
| Height | 491 mm |
| Weight | 22.9 kg |
| Payload | 4 kg |
| Max speed | 2 m/s (7.2 km/h) |
| Wheels | 2 |
| Degrees of freedom | 6 |
| Runtime | 1.5 h |
| Battery | 178 Wh |
| Status | Commercial |
| SDK | yes |
| On-board compute | yes |
| Compute | Raspberry Pi 4 Model B (Ubuntu 20.04) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

53 values from 5 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Configurations | Diablo (Standard); Diablo + Navigation Tower; Diablo + Quad Wheel-Legs |  | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 540 mm | standing and crouched | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |
| Width | 371 mm |  | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |
| Height (standing) | 491 mm |  | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |
| Height (crouched/creeping) | 270 mm |  | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |
| Material | Aluminium alloy + high-strength engineering plastic |  | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |
| Weight | 22.9 kg | incl. docking mechanism | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |
| Head height adjustment | 20 cm | up to about 20 cm (published paper) | [shop.directdrive.com](https://shop.directdrive.com/blogs/robotics-blog/inside-diablo-direct-drive-self-balancing-wheeled-leg-robot-platform) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Degrees of freedom | 6 |  | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |
| Payload (crouched/creeping mode) | 80 kg |  | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |
| Payload (standing mode) | 4 kg |  | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |
| Max continuous speed | 2 m/s |  | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |
| Jump height | 80 mm | no load | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |
| Controllable tilt angle | 37 ° | self-balance | [en.directdrive.com](https://en.directdrive.com/product_diablo) |
| Impact absorption | 60 % | leg impedance control absorbs 60% impact force | [en.directdrive.com](https://en.directdrive.com/product_diablo) |
| Balance control | LQR on inverted-pendulum model; stable within ~30° of equilibrium; jump and fall recovery | https://shop.directdrive.com/blogs/robotics-blog/inside-diablo-direct-drive-self-balancing-wheeled-leg-robot-platform | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Obstacle crossing | 8 cm | about, on flat ground | [shop.directdrive.com](https://shop.directdrive.com/blogs/robotics-blog/inside-diablo-direct-drive-self-balancing-wheeled-leg-robot-platform) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery capacity | 0.178 kWh | stated '0.178 kWh, 220V, 235.2W' | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |
| Runtime | 1.5 h | ≈1.5 h (product page) | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |
| Runtime (creeping, high speed) | 3 h | ≈3 h at 34 °C ambient (shop/blog; Weston guide says ≈4 h) | [shop.directdrive.com](https://shop.directdrive.com/products/diablo-world-s-first-direct-drive-self-balancing-wheeled-leg-robot) |
| Runtime (standing, low speed) | 3 h | ≈3 h at 34 °C ambient | [westonrobot.github.io](https://westonrobot.github.io/docs-legacy/robot_user_guide/directdrive/diablo.html) |
| Standing time upright | 3 h | ≈3 h at 25 °C | [shop.directdrive.com](https://shop.directdrive.com/products/diablo-world-s-first-direct-drive-self-balancing-wheeled-leg-robot) |
| Standing time half-squat | 15 min | ≈15 min at 25 °C | [shop.directdrive.com](https://shop.directdrive.com/products/diablo-world-s-first-direct-drive-self-balancing-wheeled-leg-robot) |
| Battery type | Li-ion |  | [westonrobot.github.io](https://westonrobot.github.io/docs-legacy/robot_user_guide/directdrive/diablo.html) |
| Battery capacity | 6 Ah |  | [westonrobot.github.io](https://westonrobot.github.io/docs-legacy/robot_user_guide/directdrive/diablo.html) |
| Cycle life | 1,000 cycles | >80% capacity retained after 1000 cycles | [westonrobot.github.io](https://westonrobot.github.io/docs-legacy/robot_user_guide/directdrive/diablo.html) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Standard charging time | 1 h | ≈1 h | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |
| Power adapter output | 32.9 V / 3 A | model XVE126-3290300; input 110 V AC | [westonrobot.github.io](https://westonrobot.github.io/docs-legacy/robot_user_guide/directdrive/diablo.html) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| IMU | BMI088 (SPI) | https://shop.directdrive.com/blogs/robotics-blog/inside-diablo-direct-drive-self-balancing-wheeled-leg-robot-platform | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Processor | Raspberry Pi 4 Model B | application control panel | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |
| Operating system | Ubuntu 20.04 | Weston guide: Ubuntu Mate | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |
| OTA updates | Supported |  | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |
| Low-level controller | Microcontroller on ChibiOS/RT; CAN bus to motor drivers | https://shop.directdrive.com/blogs/robotics-blog/inside-diablo-direct-drive-self-balancing-wheeled-leg-robot-platform | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |
| Mini PC edge inference | 5 TOPS | quad-core ARM A53 mini PC; H.264/H.265 video; UART link | [shop.directdrive.com](https://shop.directdrive.com/blogs/robotics-blog/inside-diablo-direct-drive-self-balancing-wheeled-leg-robot-platform) |
| ROS | Open-source ROS framework (ROS 2 package diablo_ros2) | https://shop.directdrive.com/blogs/robotics-blog/inside-diablo-direct-drive-self-balancing-wheeled-leg-robot-platform | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Max safe remote control distance | 150 m |  | [westonrobot.github.io](https://westonrobot.github.io/docs-legacy/robot_user_guide/directdrive/diablo.html) |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Payload space | Top cargo space and front sensor space (LiDAR, GPS, anti-collision modules) | https://shop.directdrive.com/products/diablo-world-s-first-direct-drive-self-balancing-wheeled-leg-robot | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |

### Actuation & Joints

| Spec | Value | Note | Source |
|---|---|---|---|
| Joints | 6 × M1502D direct-drive joint modules (no gearbox), built-in driver and angle sensor | https://shop.directdrive.com/blogs/robotics-blog/inside-diablo-direct-drive-self-balancing-wheeled-leg-robot-platform | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |
| Joint rated torque | 9.6 N·m | M1502D | [shop.directdrive.com](https://shop.directdrive.com/blogs/robotics-blog/inside-diablo-direct-drive-self-balancing-wheeled-leg-robot-platform) |
| Joint stall/peak torque | 17 N·m | M1502D (Weston guide lists 20 N·m stall) | [shop.directdrive.com](https://shop.directdrive.com/blogs/robotics-blog/inside-diablo-direct-drive-self-balancing-wheeled-leg-robot-platform) |
| Joint rated speed | 115 rpm | no-load 220 rpm | [shop.directdrive.com](https://shop.directdrive.com/blogs/robotics-blog/inside-diablo-direct-drive-self-balancing-wheeled-leg-robot-platform) |
| Joint rated voltage | 24 V | M1502D (Weston guide: 32 V rated, 28–32 V operating) | [shop.directdrive.com](https://shop.directdrive.com/blogs/robotics-blog/inside-diablo-direct-drive-self-balancing-wheeled-leg-robot-platform) |
| Joint max efficiency | ≥76 % |  | [shop.directdrive.com](https://shop.directdrive.com/blogs/robotics-blog/inside-diablo-direct-drive-self-balancing-wheeled-leg-robot-platform) |
| Joint motor mass | 2.6 ± 0.1 kg | Weston guide: 2.3 kg | [shop.directdrive.com](https://shop.directdrive.com/blogs/robotics-blog/inside-diablo-direct-drive-self-balancing-wheeled-leg-robot-platform) |
| Joint encoder resolution | 16,384 counts | 16-bit; accuracy within 0.01° (older product page) | [shop.directdrive.com](https://shop.directdrive.com/blogs/robotics-blog/inside-diablo-direct-drive-self-balancing-wheeled-leg-robot-platform) |
| Joint ambient temperature | −15 to 45 °C |  | [shop.directdrive.com](https://shop.directdrive.com/blogs/robotics-blog/inside-diablo-direct-drive-self-balancing-wheeled-leg-robot-platform) |
| Joint motor dimensions | Φ144 × 41.8 mm |  | [westonrobot.github.io](https://westonrobot.github.io/docs-legacy/robot_user_guide/directdrive/diablo.html) |
| Joint stall current | 28 A | rated 12 A (non-continuous) | [westonrobot.github.io](https://westonrobot.github.io/docs-legacy/robot_user_guide/directdrive/diablo.html) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Power-failure protection | Supported |  | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |
| Operating noise | <49 dB |  | [shop.directdrive.com](https://shop.directdrive.com/products/diablo-world-s-first-direct-drive-self-balancing-wheeled-leg-robot) |
| Emergency stop | Handle-mounted emergency stop; BMS; watchdog | https://shop.directdrive.com/blogs/robotics-blog/inside-diablo-direct-drive-self-balancing-wheeled-leg-robot-platform | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Remote control | RadioLink T8S, 2.4 GHz, −104 dBm sensitivity | https://westonrobot.github.io/docs-legacy/robot_user_guide/directdrive/diablo.html | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Optional accessories | Navigation tower; food-delivery module |  | [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306) |

## Documents

- [Direct Drive Tech DIABLO product page (spec table)](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306)
- [Direct Drive Tech shop – DIABLO product page](https://shop.directdrive.com/products/diablo-world-s-first-direct-drive-self-balancing-wheeled-leg-robot)
- [Direct Drive Tech blog – Inside Diablo (Aug 2026)](https://shop.directdrive.com/blogs/robotics-blog/inside-diablo-direct-drive-self-balancing-wheeled-leg-robot-platform)
- [Weston Robot (distributor) DIABLO user guide specs](https://westonrobot.github.io/docs-legacy/robot_user_guide/directdrive/diablo.html)
- [Direct Drive Tech DIABLO product page (older EN site)](https://en.directdrive.com/product_diablo)

## Notes

Direct Drive Technology Diablo product page (checked 2026-11-17): standing 540 x 371 x 491 mm (crouched 540 x 371 x 270 mm), 22.9 kg incl. docking mechanism, 6 DoF, battery 0.178 kWh (178 Wh), runtime about 1.5 h, charge about 1 h, payload 4 kg standing / 80 kg crouched, 2 m/s, 80 mm jump, Raspberry Pi 4 Model B, Ubuntu 20.04.

## Sources

- Official page: [robotics.directdrive.com](https://robotics.directdrive.com/en/products/xingtian-robot/1653337674873306)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-19). Source repository: https://github.com/htcrefactor/robot-catalog*
