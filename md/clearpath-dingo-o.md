# Clearpath Robotics (Rockwell Automation) Dingo-O

> Lightweight, low-profile indoor omnidirectional (mecanum) base for robotics research and education; a differential Dingo-D variant also exists.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=clearpath-dingo-o
- Category: Mobile platform
- Locomotion: Wheeled
- Manufacturer: Clearpath Robotics (Rockwell Automation) (Canada)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 686 mm |
| Width | 517 mm |
| Height | 114 mm |
| Weight | 13 kg |
| Payload | 20 kg |
| Max speed | 1.3 m/s (4.7 km/h) |
| Wheel diameter | 101.6 mm |
| Wheels | 4 |
| Status | Commercial |
| API | yes |
| SDK | yes |
| SDK name | ROS 2 Jazzy (Clearpath packages) |
| ROS | yes |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

52 values from 3 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Manufacturer address | Clearpath Robotics Inc., 1425 Strasburg Road, Unit 2A, Kitchener, Ontario N2R 1H2, Canada |  | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) |
| Variants | Dingo-D (differential, 2 module bays); Dingo-O (omnidirectional, 4 module bays); hardware revisions Dingo 1.0 and 1.5 |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/dingo/user_manual_dingo) · Introduction |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 686 mm |  | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) |
| Width | 517 mm |  | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) |
| Height | 114 mm |  | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) |
| Weight | 17.5 kg | datasheet and user manual (Dingo-O) | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) |
| Weight | 13 kg | product page tech specs | [clearpathrobotics.com](https://clearpathrobotics.com/dingo-indoor-mobile-robot/) · Tech Specs |
| Obstacle / ground clearance | 16 mm |  | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) |
| Wheel diameter | 101.6 mm | mecanum wheels | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/dingo/user_manual_dingo) · Exterior Features |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Max speed | 1.3 m/s |  | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) |
| Minimum controllable speed | 0.1 m/s |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/dingo/user_manual_dingo) · General Warnings |
| Max payload | 25 kg | datasheet and user manual (Dingo-O) | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) |
| Max payload | 20 kg | product page tech specs | [clearpathrobotics.com](https://clearpathrobotics.com/dingo-indoor-mobile-robot/) · Tech Specs |
| Drive configuration | Omnidirectional (mecanum wheels) |  | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) |
| Power | 170 W | typical use | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Operating environment | Indoor |  | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery chemistry | Sealed lead acid or LiFePO4 (Dingo 1.5); SLA or 14.4 V lithium (Dingo 1.0) |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/dingo/user_manual_dingo) · System Specifications |
| Battery module capacity | 12 V 20 Ah | per lead-acid or LiFePO4 module | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) · Expansion Modules |
| Battery voltage | 12 V SLA; 12.8 V LiFePO4; 14.4 V lithium (1.0) |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/dingo/user_manual_dingo) · Shipment Contents |
| Operating time (SLA) | 2 - 6 h | 1x - 3x SLA modules | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) |
| Operating time (LiFePO4) | 3.5 - 11 h | 1x - 3x LiFePO4 modules | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) |
| Operating time (Dingo 1.0) | 2 h (2x SLA); 4 h (2x lithium) |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/dingo/user_manual_dingo) · System Specifications |
| Battery hot-swap | yes | Dingo 1.0: hot-swap one at a time while at least one battery present | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/dingo/user_manual_dingo) · Battery Charging |
| Battery peak power | over 2000 W | short durations | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/dingo/user_manual_dingo) · Electrical System |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charge time (SLA) | 3.3 - 10 h | 1x - 3x | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) |
| Charge time (LiFePO4) | 3 - 9 h | 1x - 3x | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) |
| Charge current | 6 A (SLA); 7 A (LiFePO4) | Dingo 1.5 manual charger | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/dingo/user_manual_dingo) · Battery Charging |
| Charging | Front charge port (Dingo 1.5); external charging (1.0); optional WiBotic wireless charging; DC shore power |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/dingo/user_manual_dingo) |
| Wireless charging power | 150 W | Wireless Charging Kit: WiBotic OC-150 onboard charger + receiver coil | [clearpathrobotics.com](https://clearpathrobotics.com/dingo-indoor-mobile-robot/) · Packages |
| Shore power supply | Mean Well GST280A15-C6P | motors disabled on shore power | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/dingo/user_manual_dingo) · DC Shore Power |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| Charging temperature | 0 to 45 °C (SLA, LiFePO4); 0 to 50 °C (lithium) |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/dingo/user_manual_dingo) · Battery Charging |
| Discharge temperature | -30 to 60 °C (SLA); -20 to 60 °C (lithium, LiFePO4) |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/dingo/user_manual_dingo) · Battery Charging |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| IMU | Onboard IMU |  | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) |
| Internal sensing | Battery status, wheel odometry, motor currents, onboard IMU |  | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Computing module | Mini-ITX computer or NVIDIA Jetson developer kit |  | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) · Expansion Modules |
| Microcontroller | 32-bit MCU, 100 Mbps Ethernet to computer |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/dingo/user_manual_dingo) · System Architecture |
| Operating system | Ubuntu |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/dingo/user_manual_dingo) |
| ROS version | ROS 2 Jazzy |  | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) |
| Simulation / tools | RViz, Gazebo, MoveIt! |  | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Communication | Ethernet, USB 3.0 |  | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Maximum modules | 4 | battery, computing or empty modules | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) · Expansion Modules |
| User power (Dingo 1.5) | 20 A @ VBAT (11-15 V); 10 A @ 12 V; 5 A @ 5 V |  | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) |
| User power (Dingo 1.0) | 20 A @ VBAT (11-16.8 V); 7 A @ 12 V; 5 A @ 5 V |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/dingo/user_manual_dingo) |
| Top cover screws | M5 flathead (trough cover) |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/dingo/user_manual_dingo) · Payload Details |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Stop | Motion Stop button on HMI; external motion-stop breakout on MCU |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/dingo/user_manual_dingo) |
| Max manual push speed | 0.5 m/s |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/dingo/user_manual_dingo) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Control modes | Kinematic control |  | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) |
| Controller | Sony PS4 Bluetooth wireless controller |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/dingo/user_manual_dingo) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Lights / HMI | 4 corner LEDs (ROS /mcu/lights override); HMI panel with motion stop, comms, Wi-Fi, battery, power indicators |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/dingo/user_manual_dingo) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Included | Wireless controller, batteries, universal charger, quick start guide, USB cable, Molex connectors, spare fuses (5/10/20 A) |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/dingo/user_manual_dingo) · Shipment Contents |
| Packages / upgrades | Vision (NVIDIA AGX Orin, ZED 2i, 3D lidar); Manipulation (Kinova Gen3 lite up to 0.5 kg, Intel D435); IndoorNav (2x 2D lidar, IMU); Wireless Charging Kit; Shore Power |  | [clearpathrobotics.com](https://clearpathrobotics.com/dingo-indoor-mobile-robot/) · Packages |
| Price | Contact sales |  | [storage.pardot.com](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf) |

## Documents

- [Dingo-O Data Sheet (Jul 2026)](https://storage.pardot.com/92812/1784208851BERynha7/DINGO_Datasheet_07162026.pdf)
- [Dingo User Manual (Clearpath docs)](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/dingo/user_manual_dingo)
- [Dingo product page](https://clearpathrobotics.com/dingo-indoor-mobile-robot/)

## Sources

- Official page: [clearpathrobotics.com](https://clearpathrobotics.com/dingo-indoor-mobile-robot/)
- [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/dingo/user_manual_dingo)
- [github.com](https://github.com/clearpathrobotics/clearpath_robot)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-22). Source repository: https://github.com/htcrefactor/robot-catalog*
