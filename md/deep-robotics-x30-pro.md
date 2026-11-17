# DEEP Robotics X30 Pro

> Flagship IP67 industrial quadruped for inspection, security and emergency response in extreme weather.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=deep-robotics-x30-pro
- Category: Quadruped
- Locomotion: Legged
- Manufacturer: DEEP Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 1,000 mm |
| Width | 470 mm |
| Height | 715 mm |
| Weight | 59 kg |
| Payload | 20 kg |
| Max speed | 2.5 m/s (9.0 km/h) |
| Degrees of freedom | 12 |
| Runtime | 2.5 h |
| Battery | 1612.8 Wh |
| IP rating | IP67 |
| Status | Commercial |
| API | yes |
| On-board compute | yes |
| Compute | Separate motion-control and perception hosts plus an Intelligent Controller host for navigation (SSH access) |
| Sensors | LiDAR ×4, Wide-angle camera, Bi-spectrum PTZ camera (optional) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

66 values from 6 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Manufacturer | DEEP Robotics (Hangzhou Yunshenchu Technology Co., Ltd.) |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) |
| Manufacturer address | Building 3, Zijin Dream Plaza, No.36 Xinran Street, Sandun Town, Xihu District, Hangzhou, Zhejiang, China |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · back cover |
| Model | Jueying X30 Pro |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) |
| Manual version | V2.0.5-0 (2025.11.29) |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length (standing) | 1,000 mm | standing size 1000 × 470 × 715 mm | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |
| Width | 470 mm |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |
| Height (standing) | 715 mm |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |
| Length (sitting) | 1,130 mm | sitting size 1130 × 470 × 285 mm | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |
| Height (sitting) | 285 mm |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |
| Weight | 59 kg | approx.; two people recommended to carry | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3, §5.3 |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Degrees of freedom | 12 |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.1 |
| Maximum speed | 4.95 m/s | data from extreme test | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |
| Maximum walking speed | 1.2 m/s | Walk gait | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |
| Maximum running speed | 2.5 m/s | Run gait | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |
| Maximum load | 85 kg | data from extreme test | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |
| Payload | 20 kg | Intelligent Controller weight included | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |
| Gaits | Walk; Run; Slope; Off-Road; Stair; 45° Stairs; L-Walk; Mountain; Silent |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.6 |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Maximum slope | ±30 ° |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |
| Maximum step height | 20 cm |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |
| Maximum slope of staircase | ±45 ° | 45° Stairs gait only in multi-frame mode | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3, §1.6 |
| Mountain gait stair step | 25 cm | Mountain gait: single steps of 25 cm, slopes of 30°; L-Walk: 15 cm steps, 18° slopes | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.6 |
| Terrain | Concrete, stairs, slopes, stone piles and ruins (Off-Road); muddy/flooded surfaces (L-Walk); rubble (Mountain); avoid ice, sharp/undulating terrain, high edges |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.6, FAQ Q4 |
| Elevation map modes | Solid ground; grid ground; stair without risers; multi-frame |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.6 |
| Control modes | Manual mode; Assist mode (obstacle avoidance: decelerate/detour); Nav mode |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §2.4.1 |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery capacity | 22.4 Ah | ideal data at 25 °C | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |
| Nominal battery voltage | 72 V |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |
| Battery type | Ternary lithium battery, replaceable |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §2.2.1 |
| Battery replaceable | yes | two hand-screws and cover plate | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §2.2.2 |
| No-load runtime | 4 h |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |
| Payload runtime | 2.5 h |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |
| Patrol range | ≥ 10 km |  | [deeprobotics.us](https://www.deeprobotics.us/products/x30/) |
| Low battery behaviour | Warning below 10 %; below 3 % low-battery protection: robot lies down automatically |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §2.5.5 |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charger input voltage | 200–240 V |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |
| Charger output | 84 V / 8 A |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |
| Charging time | 2.5–3 h |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |
| Recommended charging temperature | 0 to 45 °C |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §2.2.2 |
| Autonomous charging | Supported |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| Ingress protection | IP67 | Intelligent Controller keeps IP67 only when USB 3.0 dust/water cap is in place | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3, §1.5 |
| Operating temperature | −20 to 55 °C |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |
| Storage temperature | −20 to 55 °C | clean and dry place; charge every three months | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §5.2 |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Laser radar | 4 | front up/down and rear up/down | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |
| LiDAR positions (body frame) | Front-up (443.67, 0, 54.15) mm; front-down (432.97, 0, −55.19) mm; rear-up (−465.76, 0, 34.84) mm; rear-down (−410.74, 0, −56.01) mm |  | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/x30/guide/hardware/lidar/) |
| Wide-angle camera | 1 |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |
| Optional module | Bi-spectrum PTZ camera | other optional modules | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Onboard hosts | Motion host + perception host inside body; navigation host inside Intelligent Controller |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.1 |
| Protocols | TCP monitoring protocol (navigation host 192.168.1.106:30000, XML ASDU); UDP motion control protocol (motion host 192.168.1.103:43893, binary) |  | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/x30/guide/communication/architecture/) |
| ROS topic interface | yes | ROS topic interface listed in developer docs | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/x30/guide/communication/architecture/) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Communication interfaces | Ethernet; Wi-Fi; USB 2.0; USB 3.0 |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |
| Intelligent Controller interfaces | LAN1+12V; LAN2; 24V; USB3.0 ×2; USB2.0 ×2; LAN3+12V; LAN4+12V; LAN5+24V; LAN6+24V |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.5 p.6 |
| Body external network ports | Port 1 (192.168.1.*), Port 2 (192.168.2.*); plus debugging Ethernet port |  | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/x30/guide/hardware/interfaces/) |
| Wi-Fi | Robot Wi-Fi access point (X30*****) |  | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/x30/guide/software/network/) |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Power supply to payloads | 12V; 24V; 5V (USB) |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |
| Maximum power to payload | 600 W | total; LAN(12V) ports max 36 W each, LAN(24V) ports max 72 W each, single 24V port max 480 W | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/x30/guide/hardware/interfaces/) |
| Body external power port | 72 V, 600 W | body external power supply port; should not exceed 600 W | [developer.deeprobotics.cn](https://developer.deeprobotics.cn/docs/x30/guide/hardware/interfaces/) |
| Mounting rails | yes | on back | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.2 |
| Payload | 20 kg | Intelligent Controller weight included | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.3 p.3 |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Silent gait noise | ≤ 50 dB standing still; ≤ 60 dB walking | Silent gait; no stairs or slopes | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.6 |
| Emergency stops | Soft emergency stop (button on robot and controller SW1+SW4); hard emergency stop button at tail (hardware power cut) |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §2.5 |
| Overtemperature protection | yes | motor/driver over-temperature protection; wait 10 min | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §2.5.3 |
| Safety distance | 2 m | keep people/objects > 2 m away | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §2.1.1 |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Controller | Handheld controller with Jueying Lab app |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §2.4 |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Indicators | 4-segment power/battery LED; Intelligent Controller indicator (green/yellow/red) |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.4–1.5 |

### Transport & Storage

| Spec | Value | Note | Source |
|---|---|---|---|
| Transport case | 1.09 × 0.55 × 0.57 m | with brake wheels | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §5.1 |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Product list | Robot (without battery), Intelligent Controller, controller, charger, replaceable battery, 8 aviation plugs, antistatic cloth, certificate, warranty card, user manual |  | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §1.2 |
| Warranty (joint module, upper/lower legs) | 6 months | from acceptance date | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §6.2 |
| Warranty (battery, laser radar, wide-angle cameras, hosts) | 12 months | shell, feet, wear parts, transport case not covered | [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf) · §6.2 |

## Documents

- [Jueying X30 Pro User Manual V2.0.5-0 (2025-11-29)](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf)
- [DEEP Robotics developer center – X30 hardware/electrical interfaces](https://developer.deeprobotics.cn/docs/x30/guide/hardware/interfaces/)
- [DEEP Robotics developer center – X30 network configuration](https://developer.deeprobotics.cn/docs/x30/guide/software/network/)
- [DEEP Robotics developer center – X30 LiDAR](https://developer.deeprobotics.cn/docs/x30/guide/hardware/lidar/)
- [DEEP Robotics developer center – X30 communication architecture](https://developer.deeprobotics.cn/docs/x30/guide/communication/architecture/)
- [DEEP Robotics X30 page (deeprobotics.us, official partner)](https://www.deeprobotics.us/products/x30/)

## Notes

Maker X30 page: X30 Pro is ~1000 x 470 x 715 mm and ~59 kg (X30: 695 mm, ~56 kg), 20 kg payload, 2.5 m/s working speed with a 4.5 m/s extreme, 30 cm stairs, IP67, -20 to 55 C, output power 5/12/24 V. Runtime 2.5 h and the 1,612.8 Wh pack come from the X30 user manual, which is hosted outside the maker's domain.

## Sources

- Official page: [deeprobotics.cn](https://www.deeprobotics.cn/en/index/product3.html)
- [cdn.robotshop.com](https://cdn.robotshop.com/media/D/DER/RB-Der-02/pdf/deep-robotics-x30-user-manual.pdf)
- [github.com](https://github.com/DeepRoboticsLab/deep_robotics_model/blob/main/X30/urdf/X30.urdf)
- [github.com](https://github.com/DeepRoboticsLab/deep_robotics_model/blob/main/X30/mjcf/X30.xml)
- [github.com](https://github.com/DeepRoboticsLab/deep_robotics_model/blob/main/X30/usd/X30.usd)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-17). Source repository: https://github.com/htcrefactor/robot-catalog*
