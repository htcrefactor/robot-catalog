# Unitree Robotics As2-W

> Compact wheel-legged quadruped with 7-inch wheels, side-follow mode and SDK/APIs for security, inspection and outdoor carrying; 0–3.7 m/s normal, ~6 m/s max.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=unitree-as2-w
- Category: Wheel-legged
- Locomotion: Wheel-legged
- Manufacturer: Unitree Robotics (China)
- Verification: not recorded

## Core specs

| Field | Value |
|---|---|
| Length | 721 mm |
| Width | 493 mm |
| Height | 521 mm |
| Weight | 25 kg |
| Payload | 16 kg |
| Max speed | 6 m/s (21.6 km/h) |
| Wheel diameter | 178 mm |
| Wheels | 4 |
| Degrees of freedom | 16 |
| Runtime | 3 h |
| Battery | 648 Wh |
| IP rating | IP54 |
| Status | Commercial |
| Price | Contact sales |
| API | yes |
| SDK | yes |
| Compute | 8-core high-performance CPU; optional high-compute expansion dock (e.g. Orin NX, 150 TOPS module) |
| Sensors | 64–128-line LiDAR, HD camera, GPS, Microphone |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

58 values from 1 document, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Variants | As2-W X; As2-W EDU (custom industry solutions) |  | [unitree.com](https://www.unitree.com/As2-W) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 721 mm | standing | [unitree.com](https://www.unitree.com/As2-W) |
| Width | 493 mm | standing | [unitree.com](https://www.unitree.com/As2-W) |
| Height (standing) | 521 mm |  | [unitree.com](https://www.unitree.com/As2-W) |
| Length | 768 mm | lying prone | [unitree.com](https://www.unitree.com/As2-W) |
| Width | 602 mm | lying prone | [unitree.com](https://www.unitree.com/As2-W) |
| Height (lying prone) | 211 mm |  | [unitree.com](https://www.unitree.com/As2-W) |
| Tyre size | 178 mm | 7 inch; radius 50 mm as stated | [unitree.com](https://www.unitree.com/As2-W) |
| Material | Aluminium alloy + high-strength engineering plastic |  | [unitree.com](https://www.unitree.com/As2-W) |
| Weight (with battery) | 25 kg | approx. | [unitree.com](https://www.unitree.com/As2-W) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Degrees of freedom (joint motors) | 16 |  | [unitree.com](https://www.unitree.com/As2-W) |
| Max standing load | 150 kg | approx., static | [unitree.com](https://www.unitree.com/As2-W) |
| Continuous walking load | 16 kg | approx. | [unitree.com](https://www.unitree.com/As2-W) |
| Speed (normal) | 0–3.7 m/s |  | [unitree.com](https://www.unitree.com/As2-W) |
| Max speed | 6 m/s | approx.; 'over 6 m/s' in headline | [unitree.com](https://www.unitree.com/As2-W) |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Slope walking capability | 45 ° | approx. | [unitree.com](https://www.unitree.com/As2-W) |
| Stair climbing | 30 cm |  | [unitree.com](https://www.unitree.com/As2-W) |
| Max climb height | 0.4–0.8 m | approx.; 80 cm steps | [unitree.com](https://www.unitree.com/As2-W) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Supply voltage | 36–50.4 V |  | [unitree.com](https://www.unitree.com/As2-W) |
| Power supply | Lithium battery |  | [unitree.com](https://www.unitree.com/As2-W) |
| Battery capacity | 648 Wh | 15,000 mAh | [unitree.com](https://www.unitree.com/As2-W) |
| Battery life (unloaded) | 3 h | ~3 h continuous walking, approx. 30 km (headline: 3 h+, >33 km) | [unitree.com](https://www.unitree.com/As2-W) |
| Range (unloaded) | 30 km | approx. | [unitree.com](https://www.unitree.com/As2-W) |
| Battery life (16 kg load) | >2 h | approx. 25 km (headline: >16 km) | [unitree.com](https://www.unitree.com/As2-W) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charger | 50.4 V 7.4 A fast charging |  | [unitree.com](https://www.unitree.com/As2-W) |
| Charging dock | EDU only |  | [unitree.com](https://www.unitree.com/As2-W) |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| Operating temperature | −20 to 55 °C |  | [unitree.com](https://www.unitree.com/As2-W) |
| Protection rating | IP54 |  | [unitree.com](https://www.unitree.com/As2-W) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Microphone | Yes |  | [unitree.com](https://www.unitree.com/As2-W) |
| GPS | Yes | disabled by default; enabled with user authorization; mainland China version only (footnote [4]) | [unitree.com](https://www.unitree.com/As2-W) |
| Camera | HD camera |  | [unitree.com](https://www.unitree.com/As2-W) |
| LiDAR | Industrial-grade 64–128-line ultra-wide-angle LiDAR |  | [unitree.com](https://www.unitree.com/As2-W) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Computing power | 8-core high-performance CPU |  | [unitree.com](https://www.unitree.com/As2-W) |
| Expansion module compute | 150 TOPS | optional high-performance expansion module | [unitree.com](https://www.unitree.com/As2-W) |
| High computing power expansion dock | Multiple brands/models, e.g. NVIDIA Orin NX | EDU only | [unitree.com](https://www.unitree.com/As2-W) |
| Secondary development | Supported; SDK and APIs support large AI models |  | [unitree.com](https://www.unitree.com/As2-W) |
| UniStore platform | Supported |  | [unitree.com](https://www.unitree.com/As2-W) |
| Smart OTA upgrade | Continuous upgrades |  | [unitree.com](https://www.unitree.com/As2-W) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Wi-Fi | Wi-Fi 6 |  | [unitree.com](https://www.unitree.com/As2-W) |
| Bluetooth | 5.2 |  | [unitree.com](https://www.unitree.com/As2-W) |
| 4G | Yes | disabled by default; enabled with user authorization | [unitree.com](https://www.unitree.com/As2-W) |
| Gigabit Ethernet | 1 port |  | [unitree.com](https://www.unitree.com/As2-W) |
| SBUS | 1 port |  | [unitree.com](https://www.unitree.com/As2-W) |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Power output | BAT |  | [unitree.com](https://www.unitree.com/As2-W) |

### Actuation & Joints

| Spec | Value | Note | Source |
|---|---|---|---|
| Joint bearings | Industrial-grade crossed roller bearings |  | [unitree.com](https://www.unitree.com/As2-W) |
| Joint motors | Low-inertia, high-speed inner-rotor PMSM |  | [unitree.com](https://www.unitree.com/As2-W) |
| Max joint torque | 95 N·m | approx.; industrial-grade joint modules | [unitree.com](https://www.unitree.com/As2-W) |
| Range of motion (body) | −45 to 45 ° |  | [unitree.com](https://www.unitree.com/As2-W) |
| Range of motion (thigh) | −115 to 200 ° |  | [unitree.com](https://www.unitree.com/As2-W) |
| Range of motion (shank) | −159 to −47 ° |  | [unitree.com](https://www.unitree.com/As2-W) |
| Joint encoder | Dual encoders |  | [unitree.com](https://www.unitree.com/As2-W) |
| Cooling system | Local air cooling |  | [unitree.com](https://www.unitree.com/As2-W) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Side-follow system | ISS 3.0 Intelligent Side-follow System (centimetre-level positioning) |  | [unitree.com](https://www.unitree.com/As2-W) |
| Remote controller | Included |  | [unitree.com](https://www.unitree.com/As2-W) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Speaker | Yes |  | [unitree.com](https://www.unitree.com/As2-W) |
| Front light | Yes |  | [unitree.com](https://www.unitree.com/As2-W) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Warranty | 12 months |  | [unitree.com](https://www.unitree.com/As2-W) |
| Price | Contact sales | tax and freight excluded | [unitree.com](https://www.unitree.com/As2-W) |

## Documents

- [Unitree As2-W product page (As2-W X / EDU parameter table)](https://www.unitree.com/As2-W)

## Sources

- Official page: [unitree.com](https://www.unitree.com/As2-W)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-16). Source repository: https://github.com/htcrefactor/robot-catalog*
