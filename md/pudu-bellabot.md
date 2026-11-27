# Pudu Robotics BellaBot

> Cat-faced restaurant and retail tray-delivery robot with four trays (10 kg each), dual LiDAR/visual SLAM and swappable battery.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=pudu-bellabot
- Category: Indoor delivery
- Locomotion: Wheeled
- Manufacturer: Pudu Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 565 mm |
| Width | 537 mm |
| Height | 1,290 mm |
| Weight | 55 kg |
| Payload | 40 kg |
| Max speed | 1.2 m/s (4.3 km/h) |
| Min speed | 0.5 m/s |
| Runtime | 13 h |
| Status | Commercial |
| Sensors | LiDAR, 3x RGBD camera, Visual SLAM camera, Infrared tray sensors |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

51 values from 2 documents, checked against maker sources on 2026-11-04.

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 565 mm |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Width | 537 mm |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Height | 1,290 mm |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Robot weight | 55 kg |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Machine material | ABS / aviation-grade aluminum alloy |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Max load capacity | 40 kg | 10 kg per tray | [pudurobotics.com](https://www.pudurobotics.com/en/products/bellabot) |
| Number of trays | 4 |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Load per tray | 10 kg |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Max cruise speed | 1.2 m/s | adjustable | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Min cruise speed | 0.5 m/s | adjustable | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Suspension | Automotive-grade adaptive variable independent suspension |  | [pudurobotics.com](https://www.pudurobotics.com/en/products/bellabot) |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Min. travel width | 700 mm |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Min. turning width | 650 mm | latest APK version required | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Max. surmountable height | 10 mm |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Max. climbing angle | 5 ° |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Navigation | Laser and visual integrated SLAM positioning |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Positioning method (marker) | Marker positioning, max ceiling height 8 m | optional high-level code | [pudurobotics.com](https://www.pudurobotics.com/en/products/bellabot) |
| Positioning method (laser) | Laser positioning, code-free, no height restriction |  | [pudurobotics.com](https://www.pudurobotics.com/en/products/bellabot) |
| Surface requirement | Indoor environment, flat and smooth ground |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Operating voltage | 23–29.4 V DC |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Battery capacity | 25.6 Ah |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Battery life | 12–24 h | academy spec table | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Battery life | 13 h | no load (product page) | [pudurobotics.com](https://www.pudurobotics.com/en/products/bellabot) |
| Swappable battery | yes | quick battery swap | [pudurobotics.com](https://www.pudurobotics.com/en/products/bellabot) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charger power input | AC 100–240 V, 50/60 Hz |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Charger power output | 29.4 V, 8 A |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Charging time | 4.5 h |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| Working temperature | 0 to 40 °C |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Working humidity | ≤ 85 % RH |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Storage temperature | −40 to 65 °C | RH ≤ 85% | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Working altitude | < 2000 m |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| IP rating | IP20 |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| LiDAR | LiDAR (laser SLAM) |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| RGBD cameras | 3 | 3D omnidirectional obstacle avoidance | [pudurobotics.com](https://www.pudurobotics.com/en/products/bellabot) |
| Vision sensor | Visual SLAM vision sensor |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Tray sensors | Infrared tray sensors |  | [pudurobotics.com](https://www.pudurobotics.com/en/products/bellabot) |
| Touch sensor | Touch sensor on head (haptic feedback) |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Microphone | 6-mic circular array kit |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Operating system | Android |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Management app | PUDU Link app (call, monitor, configure, view operational data) |  | [pudurobotics.com](https://www.pudurobotics.com/en/products/bellabot) |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Tray dimensions | 410 × 510 mm | Product page states 41.00 × 50.01 cm | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Height between trays | 230 / 200 / 200 / 180 mm | top to bottom | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Obstacle avoidance | 3D omnidirectional; stops for obstacles at any angle, low-lying and overhanging |  | [pudurobotics.com](https://www.pudurobotics.com/en/products/bellabot) |
| Obstacle stop response time | 0.5 s | as short as | [pudurobotics.com](https://www.pudurobotics.com/en/products/bellabot) |
| Emergency stop | Emergency switch |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Operating modes | Delivery; Cruise; Direct; Birthday; Escorting |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Calling methods | PUDU Link app; push-button caller; 4G watch |  | [pudurobotics.com](https://www.pudurobotics.com/en/products/bellabot) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Screen | 10.1-inch LCD | animated cat-face expressions | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Speakers | 2 × 10 W stereo |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |
| Light interaction | Light strip; status-dependent light effects |  | [pudurobotics.com](https://www.pudurobotics.com/en/products/bellabot) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Service life | 5 years |  | [academy.pudutech.com](https://academy.pudutech.com/en/docs/chan-pin-jie-shao) |

## Documents

- [BellaBot product page (Pudu Robotics)](https://www.pudurobotics.com/en/products/bellabot)
- [BellaBot Product Introduction (PUDU Academy)](https://academy.pudutech.com/en/docs/chan-pin-jie-shao)

## Sources

- Official page: [pudurobotics.com](https://www.pudurobotics.com/en/products/bellabot)
- [pudurobotics.com](https://www.pudurobotics.com/products/bellabot)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-27). Source repository: https://github.com/htcrefactor/robot-catalog*
