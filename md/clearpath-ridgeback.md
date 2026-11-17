# Clearpath Robotics (Rockwell Automation) Ridgeback

> Indoor omnidirectional mecanum-wheel base for carrying manipulators and heavy payloads in mobile-manipulation research.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=clearpath-ridgeback
- Category: Mobile platform
- Locomotion: Wheeled
- Manufacturer: Clearpath Robotics (Rockwell Automation) (Canada)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 960 mm |
| Width | 793 mm |
| Height | 311 mm |
| Weight | 135 kg |
| Payload | 100 kg |
| Max speed | 1.1 m/s (4.0 km/h) |
| Wheels | 4 |
| Runtime | 15 h |
| Battery | 2,400 Wh |
| Status | Commercial |
| API | yes |
| SDK | yes |
| SDK name | ROS 2 Jazzy; MoveIt / MoveIt Pro |
| ROS | yes |
| On-board compute | yes |
| Sensors | 2D LiDAR (front, optional rear), IMU, Wheel encoders |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

51 values from 3 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Manufacturer address | Clearpath Robotics, by Rockwell Automation, 1425 Strasburg Rd. Suite 2A, Kitchener, ON N2R 1H2, Canada |  | [clearpathrobotics.com](https://clearpathrobotics.com/ridgeback-indoor-robot-platform/) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 960 mm |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526548LF9RMqfY/RIDGEBACK_DATA_SHEET_May2025.pdf) |
| Width | 793 mm |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526548LF9RMqfY/RIDGEBACK_DATA_SHEET_May2025.pdf) |
| Height | 311 mm | from serial R100-0111; older units 296 mm | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback) · System Specifications |
| Weight | 135 kg |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526548LF9RMqfY/RIDGEBACK_DATA_SHEET_May2025.pdf) |
| Ground / obstacle clearance | 18 mm |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526548LF9RMqfY/RIDGEBACK_DATA_SHEET_May2025.pdf) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Max speed | 1.1 m/s |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526548LF9RMqfY/RIDGEBACK_DATA_SHEET_May2025.pdf) |
| Minimum controllable speed | 0.1 m/s | control loops accurately maintain velocities as low as 0.1 m/s | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback) · General Warnings |
| Max payload | 100 kg |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526548LF9RMqfY/RIDGEBACK_DATA_SHEET_May2025.pdf) |
| Drive configuration | 4 independently driven omnidirectional (mecanum) wheels |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526548LF9RMqfY/RIDGEBACK_DATA_SHEET_May2025.pdf) |
| Encoder resolution | 35,840 pulses/rev | high resolution encoders | [clearpathrobotics.com](https://clearpathrobotics.com/ridgeback-indoor-robot-platform/) · Features |
| Position control | exact position control within 3 degrees of maneuverability |  | [clearpathrobotics.com](https://clearpathrobotics.com/ridgeback-indoor-robot-platform/) · Features |
| Power | 800 W | typical use | [storage.pardot.com](https://storage.pardot.com/92812/1748526548LF9RMqfY/RIDGEBACK_DATA_SHEET_May2025.pdf) |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Door fit | fits through a standard 32 in (80 cm) door |  | [clearpathrobotics.com](https://clearpathrobotics.com/ridgeback-indoor-robot-platform/) · Features |
| Suspension | Passive suspension for floor transitions (e.g. concrete to carpet) |  | [clearpathrobotics.com](https://clearpathrobotics.com/ridgeback-indoor-robot-platform/) · Features |
| Operating environment | Indoor |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526548LF9RMqfY/RIDGEBACK_DATA_SHEET_May2025.pdf) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery chemistry | Marine-grade AGM sealed lead acid | two 8A31DTM Group-31 deep-cycle AGM batteries | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback) · Battery Charging |
| Battery voltage | 24 V | nominal | [storage.pardot.com](https://storage.pardot.com/92812/1748526548LF9RMqfY/RIDGEBACK_DATA_SHEET_May2025.pdf) |
| Battery capacity | 100 Ah |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526548LF9RMqfY/RIDGEBACK_DATA_SHEET_May2025.pdf) |
| Operating time | 15 h | with max payload | [storage.pardot.com](https://storage.pardot.com/92812/1748526548LF9RMqfY/RIDGEBACK_DATA_SHEET_May2025.pdf) |
| Battery peak power | over 2000 W | short durations | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback) · Electrical System |
| Max depth of discharge | 80 % | do not allow batteries to reach 80% DoD | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback) · Battery Charging |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charge time | 8 h | approx. | [storage.pardot.com](https://storage.pardot.com/92812/1748526548LF9RMqfY/RIDGEBACK_DATA_SHEET_May2025.pdf) |
| Charger | Integrated onboard charger; mains cord in User Bay | times out after 12 h | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback) · Battery Charging |
| Charger input | 85-270 VAC 50/60 Hz |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback) · Battery Charging |
| Min battery temperature to charge | 10 °C |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback) · Battery Charging |
| Shore power | yes |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526548LF9RMqfY/RIDGEBACK_DATA_SHEET_May2025.pdf) |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| Storage / operating temperature limits | -20 to 50 °C | batteries and robot | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback) · Battery Charging |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| LiDAR | Forward-facing 2D LiDAR included; optional rear LiDAR for 360° FOV |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback) · Shipment Contents |
| IMU | Onboard IMU (gyroscope) |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526548LF9RMqfY/RIDGEBACK_DATA_SHEET_May2025.pdf) |
| Feedback | Encoders, onboard IMU, battery status, motor currents, wheel odometry |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback) · System Specifications |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Computer | Onboard computer (Intel-based or Jetson developer kit) running Ubuntu |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback) · System Architecture |
| Microcontroller | 32-bit MCU, Gigabit Ethernet to computer (MCU at 192.168.131.2) |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback) |
| Operating system | Ubuntu |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback) |
| ROS version | ROS 2 Jazzy |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526548LF9RMqfY/RIDGEBACK_DATA_SHEET_May2025.pdf) |
| Motion planning | MoveIt motion planner; MoveIt Pro |  | [clearpathrobotics.com](https://clearpathrobotics.com/ridgeback-indoor-robot-platform/) · Tech Specs |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Communication | Ethernet, USB 3.0, RS232 |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526548LF9RMqfY/RIDGEBACK_DATA_SHEET_May2025.pdf) |
| USB | USB3 ports in User Bay (to onboard computer) |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback) · User Bay |
| Ethernet | Ethernet ports in User Bay to onboard switch; subnet 192.168.131.x/24 |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback) · User Bay |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| User power | 5 V @ 5 A; 12 V @ 7 A; 25.6 V @ 16 A | datasheet | [storage.pardot.com](https://storage.pardot.com/92812/1748526548LF9RMqfY/RIDGEBACK_DATA_SHEET_May2025.pdf) |
| User power | 20 A @ VBAT (24 V); 5 A @ 12 V; 5 A @ 5 V | user manual | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback) · System Specifications |
| Payload interface | Payload Integration Plate (e.g. UR5/UR10 arms); User Bay with user power panel |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Emergency stop | 4 red mushroom stop buttons (2 front, 2 rear) + stop reset; external motion-stop breakout on MCU |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback) · Stop Buttons |
| Max manual push speed | 0.5 m/s |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback) · Lifting and Transport |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Control modes | Kinematic (forward, sideways, rotation); individual wheel velocities |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526548LF9RMqfY/RIDGEBACK_DATA_SHEET_May2025.pdf) |
| Controller | Sony PS4 Bluetooth controller |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Body lights | 8 RGB lights (pair per corner), ROS-commandable |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback) · Body Lights |

### Transport & Storage

| Spec | Value | Note | Source |
|---|---|---|---|
| Shipping | Crate with fold-out ramp and ratchet straps |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback) · Getting Started |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Included | Onboard computer, front LiDAR, gyroscope/IMU, batteries, integrated charger, PS4 controller, quick start guide |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback) · Shipment Contents |
| Compatible accessories | Franka Panda, UR10, SICK LMS-111 lidar, rear lidar |  | [clearpathrobotics.com](https://clearpathrobotics.com/ridgeback-indoor-robot-platform/) |
| Price | Contact sales for pricing |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526548LF9RMqfY/RIDGEBACK_DATA_SHEET_May2025.pdf) |

## Documents

- [Ridgeback Data Sheet (May 2025)](https://storage.pardot.com/92812/1748526548LF9RMqfY/RIDGEBACK_DATA_SHEET_May2025.pdf)
- [Ridgeback User Manual (Clearpath docs, updated May 2025)](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback)
- [Ridgeback product page](https://clearpathrobotics.com/ridgeback-indoor-robot-platform/)

## Sources

- Official page: [clearpathrobotics.com](https://clearpathrobotics.com/ridgeback-indoor-robot-platform/)
- [storage.pardot.com](https://storage.pardot.com/92812/1748526548LF9RMqfY/RIDGEBACK_DATA_SHEET_May2025.pdf)
- [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/indoor_robots/ridgeback/user_manual_ridgeback)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-17). Source repository: https://github.com/htcrefactor/robot-catalog*
