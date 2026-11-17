# Clearpath Robotics (Rockwell Automation) Jackal

> Small, fast, weatherproof 4x4 field-robotics research UGV with onboard PC, GPS and IMU integrated with ROS 2.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=clearpath-jackal
- Category: Mobile platform
- Locomotion: Wheeled
- Manufacturer: Clearpath Robotics (Rockwell Automation) (Canada)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 508 mm |
| Width | 430 mm |
| Height | 250 mm |
| Weight | 17 kg |
| Payload | 20 kg |
| Max speed | 2 m/s (7.2 km/h) |
| Wheel diameter | 194 mm |
| Wheels | 4 |
| Runtime | 4 h |
| Battery | 332 Wh |
| IP rating | IP62 |
| Status | Commercial |
| API | yes |
| SDK | yes |
| SDK name | ROS 2 Jazzy (Clearpath packages) |
| ROS | yes |
| On-board compute | yes |
| Compute | Standard Intel i3-9100TE 16GB; Performance Intel i7-9700TE 16GB |
| Sensors | GPS, IMU, Wheel encoders |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

63 values from 3 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Manufacturer address | Clearpath Robotics, by Rockwell Automation, 1425 Strasburg Rd. Suite 2A, Kitchener, ON N2R 1H2, Canada |  | [clearpathrobotics.com](https://clearpathrobotics.com/jackal-small-unmanned-ground-vehicle/) |
| Computer configurations | Standard (Intel i3-9100TE) ; Performance (Intel i7-9700TE) |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 508 mm |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| Width | 430 mm |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| Height | 250 mm |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| Internal storage dimensions | 250 x 100 x 85 mm |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| Weight | 17 kg |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| Ground clearance | 65 mm |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| Wheel diameter | 194 mm |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal) · Exterior Features |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Max speed | 2 m/s |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| Minimum controllable speed | 0.1 m/s | control loops accurately maintain velocities as low as 0.1 m/s | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal) · Safety Considerations |
| Max payload | 20 kg |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| All-terrain payload | 10 kg |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| Drive power | 500 W |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| Drive train | High-torque 4x4 drivetrain, skid steer, aluminum chassis |  | [clearpathrobotics.com](https://clearpathrobotics.com/jackal-small-unmanned-ground-vehicle/) · Features |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Terrain | All-terrain, indoor or outdoor |  | [clearpathrobotics.com](https://clearpathrobotics.com/jackal-small-unmanned-ground-vehicle/) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery chemistry | Lithium ion |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| Battery capacity | 332 Wh | datasheet | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| Battery capacity | 270 Wh | user manual / shipment contents | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal) · System Specifications |
| Battery nominal voltage | 25.6 V | VBAT nominal | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal) · System Specifications |
| Battery maker | AllCell Technologies (for Clearpath); integrated overcurrent, overdischarge and short-circuit protection |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal) · Battery Charging |
| Battery removable | yes | lift lid and remove battery for external charging | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal) · Battery Charging |
| Run time (basic usage) | 8 h |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| Run time (heavy usage) | 2 h |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| Run time (basic usage) | 4 h | product page states 4 h | [clearpathrobotics.com](https://clearpathrobotics.com/jackal-small-unmanned-ground-vehicle/) · Tech Specs |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charge time | 4 h |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| Charger input | 110-220 VAC |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal) · Shipment Contents |
| Charging method | Internal via weather-sealed charge port under rear fender (when powered down) or external with battery removed; optional wireless charging kit |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal) |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| IP rating | IP62 |  | [clearpathrobotics.com](https://clearpathrobotics.com/jackal-small-unmanned-ground-vehicle/) · Features |
| Operating temperature | -20 to 45 °C | product page | [clearpathrobotics.com](https://clearpathrobotics.com/jackal-small-unmanned-ground-vehicle/) · Features |
| Operating temperature | -19 to 45 °C | user manual | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal) · System Specifications |
| Battery storage/operating limits | -19 to 60 °C | battery pack must not be stored or operated outside this range | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal) · Battery Charging |
| Operating environment | Indoor or outdoor |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| GPS | Integrated GPS receiver |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| IMU | Integrated gyroscope and accelerometer | internal magnetometer available but not recommended | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal) |
| Feedback | Battery and motor current, wheel velocity and travel (odometry) |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| CPU (standard) | Intel Core i3-9100TE | 16 GB RAM, 250 GB SSD | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| CPU (performance) | Intel Core i7-9700TE | 16 GB RAM, 250 GB SSD | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| RAM | 16 GB | both configurations | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| Storage | 250 GB | SSD | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| GPU | Optional (Mini-ITX performance computer and GPU upgrades) |  | [clearpathrobotics.com](https://clearpathrobotics.com/jackal-small-unmanned-ground-vehicle/) · Packages |
| Computer | Intel-based computer or Jetson developer kit running Ubuntu |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal) · System Architecture |
| Microcontroller | 32-bit MCU (IO, power monitoring, motor control, IMU/GPS), Full Speed USB serial CDC to computer, rosserial |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal) · System Architecture |
| Operating system | Ubuntu |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal) |
| ROS version | ROS 2 Jazzy |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| Simulation | Gazebo model, RViz, URDF |  | [clearpathrobotics.com](https://clearpathrobotics.com/jackal-small-unmanned-ground-vehicle/) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Communication | Ethernet, USB 3.0, RS232 |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| Wi-Fi | Wi-Fi adapter included |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| Bluetooth | yes |  | [clearpathrobotics.com](https://clearpathrobotics.com/jackal-small-unmanned-ground-vehicle/) · Features |
| Cable passthrough | Compressed-foam cable management port |  | [clearpathrobotics.com](https://clearpathrobotics.com/jackal-small-unmanned-ground-vehicle/) · Features |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| User power | 5 V @ 5 A; 12 V @ 10 A; 24 V @ 20 A | datasheet | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| User power | 16 A @ VBAT (25.6 V); 7 A @ 12 V; 5 A @ 5 V | user manual | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal) · System Specifications |
| Mounting pattern | 80 mm pattern on lid; accessory mounting plates |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal) · Exterior Features |
| User power connectors | Fused 4-pin Molex or plug-in screw terminal block |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal) · Interior Features |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Stop button | Motion Stop button on rear HMI panel (toggles motors engaged/disengaged) |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal) · Motion Stop Buttons |
| Max manual push speed | 0.5 m/s |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal) · Lifting and Transport |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Control modes | Kinematic (velocity, angular velocity); open-loop motor voltage; wheel velocity |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| Controller | Sony PS4 Bluetooth controller (L1 deadman, R1 full speed) |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| HMI indicators | Motion stop, comms, Wi-Fi, battery, power LEDs; four corner LEDs |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal) · HMI Details |

### Transport & Storage

| Spec | Value | Note | Source |
|---|---|---|---|
| Air travel | Consult airline lithium battery rules; carry-on recommended |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal) · Battery Charging |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Included | Wireless game controller, GPS, IMU, on-board computer, Wi-Fi adapter, accessory mounting plates, battery, 110-220 VAC charger |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |
| Packages | Manipulation (Kinova Gen3 lite, Intel D435); Vision (ZED 2i, 3D lidar); OutdoorNav Starter Kit (2x D435f, Phidget IMU, u-blox ZED-F9P); IndoorNav (2x 2D lidar); Wireless Charging Kit |  | [clearpathrobotics.com](https://clearpathrobotics.com/jackal-small-unmanned-ground-vehicle/) · Packages |
| Price | Contact sales for pricing |  | [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf) |

## Documents

- [Jackal Data Sheet (May 2025)](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf)
- [Jackal User Manual (Clearpath docs, updated Aug 2025)](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal)
- [Jackal UGV product page](https://clearpathrobotics.com/jackal-small-unmanned-ground-vehicle/)

## Sources

- Official page: [clearpathrobotics.com](https://clearpathrobotics.com/jackal-small-unmanned-ground-vehicle/)
- [storage.pardot.com](https://storage.pardot.com/92812/1748526832JH1SIJ41/JACKAL_DATA_SHEET_May2025.pdf)
- [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-17). Source repository: https://github.com/htcrefactor/robot-catalog*
