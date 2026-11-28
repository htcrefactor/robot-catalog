# DEEP Robotics Lite3 (Basic)

> Compact quadruped for robotics education, reinforcement-learning research and entertainment.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=deep-robotics-lite3
- Category: Quadruped
- Locomotion: Legged
- Manufacturer: DEEP Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 610 mm |
| Width | 370 mm |
| Height | 406 mm |
| Weight | 12 kg |
| Payload | 5 kg |
| Runtime | 1.5 h |
| Status | Commercial |
| API | yes |
| SDK | yes |
| SDK name | Lite3 Motion SDK |
| ROS | yes |
| On-board compute | yes |
| Compute | RK3588 motion host; NVIDIA Jetson Xavier NX perception host on Pro/LiDAR versions |
| Sensors | Wide-angle camera, Depth camera (Intel RealSense D435i, Pro/LiDAR), LiDAR (LiDAR version) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

89 values from 8 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Manufacturer | DEEP Robotics (Hangzhou Yunshenchu Technology Co., Ltd.) |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) |
| Variants | Basic; Venture; Pro; LiDAR |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |
| Manual version | Jueying Lite3-AI User Manual V1.0.3-0 |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length (standing) | 610 mm | all variants | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |
| Width (standing) | 370 mm | all variants | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |
| Height (standing) | 406 mm | Basic | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |
| Height (standing) | 445 mm | Venture | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |
| Height (standing) | 450 mm | Pro | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |
| Height (standing) | 496 mm | LiDAR | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |
| Length (sitting) | 680 mm | sitting size 680 × 370 × 115 mm (Lite3-AI) | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §1.4 |
| Height (sitting) | 115 mm | Lite3-AI | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §1.4 |
| Weight (incl. battery) | 12 kg | Basic | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |
| Weight (incl. battery) | 12.2 kg | Venture | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |
| Weight (incl. battery) | 12.9 kg | Pro | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |
| Weight (incl. battery) | 13.5 kg | LiDAR | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |
| Body weight | 11 kg | body incl. battery and hip abduction joints | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/lite3/guide/hardware/mechanics/) |
| Thigh length | 200 mm | hip-pitch to knee centre | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/lite3/guide/hardware/mechanics/) |
| Shank length | 210 mm | knee centre to foot centre | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/lite3/guide/hardware/mechanics/) |
| Hip spacing | 124 (left–right); 349 (front–rear) mm |  | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/lite3/guide/hardware/mechanics/) |
| Foot radius | 20 mm |  | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/lite3/guide/hardware/mechanics/) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Walking load | 5 kg | Basic | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |
| Walking load | 4.5 kg | Venture | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |
| Walking load | 4 kg | Pro | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |
| Walking load | 2.5 kg | LiDAR | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |
| Maximum walking load | 7.5 kg | "increased by 40 %, reaching 7.5 kg" | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |
| Max speed (fast gait) | 2.5 m/s |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §1.4 |
| Max speed (medium gait) | 1.3 m/s |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §1.4 |
| Max speed (slow gait) | 0.5 m/s |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §1.4 |
| Jumping height | 30 cm |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §1.4 |
| Degrees of freedom | 12 | 3 joints per leg (HipX, HipY, Knee) | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/lite3/guide/hardware/joint/) |
| Gaits | Flat (NRM/Crawl height); RUG: General, Grip, H-Step |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §2.3 |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Slope | 40 ° | RUG Grip gait | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §1.4 |
| Steps height | 15 cm | manual; brochure states 18 cm stair-climbing height | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §1.4 |
| Stair-climbing height (brochure) | 18 cm |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |
| Gap width | 50 cm |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §1.4 |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| No-load duration | 1.5–2 h | rapid interchange of batteries | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §1.4 |
| Range | 5 km | Basic | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |
| Range | 4 km | Venture | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |
| Range | 3.4 km | Pro | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |
| Range | 2.7 km | LiDAR | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |
| Battery capacity | 4.4 Ah |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §1.4 |
| Nominal battery voltage | 28.8 V |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §1.4 |
| Replaceable battery | yes | charged in separate charging base | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §3.2 |
| Low battery | Warning below 35 %; low-power protection below 20 % |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §3.11.4 |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charger input | 100–240 V |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §1.4 |
| Charger output | 33.6 V / 5 A |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §1.4 |
| Charging time | 40 min–1 h |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §1.4 |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| Operating temperature | 0 to 40 °C |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §1.4 |
| Storage temperature | 0 to 40 °C | clean and dry | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §6.2 |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Wide-angle camera | 1 |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §1.4 |
| Ultrasonic radar | 2 | front and rear | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §1.4 |
| Depth camera | Intel RealSense D435i | Pro / LiDAR versions | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/lite3/guide/hardware/camera/) |
| LiDAR | Optional Livox or Leishen LiDAR module | LiDAR version | [deeprobotics.us](https://www.deeprobotics.us/products/lite-3/) |
| Perception functions | Basic/Venture: front/rear obstacle stop, visual following; Pro: + forward obstacle avoidance; LiDAR: + autonomous navigation |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Motion host | RK3588 ARM-architecture processor |  | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/lite3/guide/software/compute/) |
| Perception host | NVIDIA Jetson Xavier NX | Pro / LiDAR versions | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/lite3/guide/software/compute/) |
| Operating system | Ubuntu 20.04 |  | [deeprobotics.us](https://www.deeprobotics.us/products/lite-3/) |
| ROS versions | ROS1 Noetic; ROS2 Foxy | switchable via built-in scripts | [deeprobotics.us](https://www.deeprobotics.us/products/lite-3/) |
| SDKs | Motion SDK; RL SDK (Lite3_rl_deploy); Gamepad SDK; perception development interfaces |  | [deeprobotics.us](https://www.deeprobotics.us/products/lite-3/) |
| Control frequency | 1 kHz | up to 1 kHz communication | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |
| OTA upgrades | yes |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Wi-Fi frequency band | 5150–5250 MHz; 5725–5850 MHz | 5150–5250 MHz indoor use only | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §1.4, §4.3 |
| Wi-Fi transmitter power | 5150–5250 MHz: 14.87 dBm; 5725–5850 MHz: 13.89 dBm |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §1.4 |
| Hardware interfaces | Basic: none; Venture: Ethernet ×2, external power input (24V/12V/5V); Pro/LiDAR: USB 3.0, HDMI, Ethernet, external power input (24V/12V/5V), power connector |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |
| Default IPs | Perception host 192.168.1.103; motion host 192.168.1.120; LiDAR 192.168.1.201 |  | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/lite3/guide/software/network/) |

### Actuation & Joints

| Spec | Value | Note | Source |
|---|---|---|---|
| Joints | 12 |  | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/lite3/guide/hardware/joint/) |
| HipX range | −24 to 24 ° |  | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/lite3/guide/hardware/joint/) |
| HipY range | −200 to 20 ° |  | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/lite3/guide/hardware/joint/) |
| Knee range | 34.5 to 156 ° |  | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/lite3/guide/hardware/joint/) |
| Rated torque (HipX / HipY) | 6.48 N·m |  | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/lite3/guide/hardware/joint/) |
| Rated torque (Knee) | 9.72 N·m |  | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/lite3/guide/hardware/joint/) |
| Max torque (HipX / HipY) | 24 N·m |  | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/lite3/guide/hardware/joint/) |
| Max torque (Knee) | 36 N·m |  | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/lite3/guide/hardware/joint/) |
| Max speed (HipX) | 26.16 rad/s |  | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/lite3/guide/hardware/joint/) |
| Max speed (HipY) | 26.1 rad/s |  | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/lite3/guide/hardware/joint/) |
| Max speed (Knee) | 17.1 rad/s |  | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/lite3/guide/hardware/joint/) |
| Joint masses | HipX 0.435 kg; HipY 0.501 kg; Knee + thigh 0.96 kg; shank 0.16 kg |  | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/lite3/guide/hardware/joint/) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Protection | Overtemperature protection (stops and lies down); fall-down protection (increased joint damping); motion logs |  | [deeprobotics.us](https://www.deeprobotics.us/products/lite-3/) |
| Safety distance | 1 m | keep at least 1 m from people | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §4.1 |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Actions | Backflip, Carpet Backflip, Hello, Twist, Moonwalk, Long Jump, Twist Jump, Turn Over |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §2.3.5 |
| Controller | Android app; dedicated controller (not with Basic without-controller option) |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §1.2 |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Speaker | Built-in Hi-Fi speaker |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |
| LED eyes / light communication | Intelligent light communication system; LED eye status lights |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |
| Voice control | yes | voice-controlled movement and interactive performances | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |

### Transport & Storage

| Spec | Value | Note | Source |
|---|---|---|---|
| Transport case | 633 × 462 × 329 mm |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §6.1 |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Product list | Robot (battery not included), transport case, sole kit, replaceable battery, charger, controller, charging base, certificate, warranty card, fold-out guide |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §1.2 |
| Warranty (joint module) | 3 months | from date of receipt | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §7.1 |
| Warranty (replaceable battery) | 6 months |  | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf) · §7.1 |
| Retail price | From 2,890 USD | Basic; other versions contact sales | [deeprobotics.us](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf) |

## Documents

- [Jueying Lite3-AI User Manual V1.0.3-0](https://www.deeprobotics.us/wp-content/uploads/2025/08/Jueying-Lite3-AI-User-Manual-V1.0.3-0.pdf)
- [DEEP Robotics Lite3 brochure (EN, 2025)](https://www.deeprobotics.us/wp-content/uploads/2025/08/DEEPRobotics-Lite3-Quadruped-Robot-ENV-7.2.2025.pdf)
- [DEEP Robotics Lite 3 page incl. FAQ (deeprobotics.us, official partner)](https://www.deeprobotics.us/products/lite-3/)
- [DEEP Robotics developer center – Lite3 joints](https://developer.deeprobotics.cn/docs/lite3/guide/hardware/joint/)
- [DEEP Robotics developer center – Lite3 mechanics](https://developer.deeprobotics.cn/docs/lite3/guide/hardware/mechanics/)
- [DEEP Robotics developer center – Lite3 compute](https://developer.deeprobotics.cn/docs/lite3/guide/software/compute/)
- [DEEP Robotics developer center – Lite3 camera](https://developer.deeprobotics.cn/docs/lite3/guide/hardware/camera/)
- [DEEP Robotics developer center – Lite3 network](https://developer.deeprobotics.cn/docs/lite3/guide/software/network/)

## Notes

Maker page: Basic 610 x 370 x 406 mm, 12 kg, 5 kg payload, 1.5-2 h operation (1.5 recorded), 40 deg slope, RK3588 motion host plus Jetson Xavier NX perception host on Pro/LiDAR versions, Ubuntu 20.04, ROS 1 Noetic / ROS 2 Foxy and a Motion SDK. Other editions: Venture 445 mm/12.2 kg/4.5 kg, Pro 450 mm/12.9 kg/4 kg, LiDAR 496 mm/13.5 kg/2.5 kg.

## Sources

- Official page: [deeprobotics.us](https://www.deeprobotics.us/products/lite-3/)
- [github.com](https://github.com/DeepRoboticsLab/Lite3_MotionSDK)
- [github.com](https://github.com/DeepRoboticsLab/deep_robotics_model/blob/main/Lite3/urdf/Lite3.urdf)
- [github.com](https://github.com/DeepRoboticsLab/deep_robotics_model/blob/main/Lite3/mjcf/Lite3.xml)
- [github.com](https://github.com/DeepRoboticsLab/deep_robotics_model/blob/main/Lite3/usd/Lite3.usd)
- [github.com](https://github.com/DeepRoboticsLab/rl_training)
- [github.com](https://github.com/DeepRoboticsLab/deep_robotics_model)
- [github.com](https://github.com/DeepRoboticsLab/Lite3_ROS)
- [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/lite3/guide/software/compute/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-28). Source repository: https://github.com/htcrefactor/robot-catalog*
