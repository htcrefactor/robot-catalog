# Clearpath Robotics (Rockwell Automation) TurtleBot 4

> Low-cost ROS 2 education and research robot built on the iRobot Create 3 base with lidar, stereo-depth camera and Raspberry Pi.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=clearpath-turtlebot-4
- Category: Mobile platform
- Locomotion: Wheeled
- Manufacturer: Clearpath Robotics (Rockwell Automation) (Canada)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 342 mm |
| Width | 339 mm |
| Height | 351 mm |
| Weight | 3.945 kg |
| Payload | 9 kg |
| Max speed | 0.46 m/s (1.7 km/h) |
| Wheel diameter | 72 mm |
| Runtime | 2.5 h |
| Battery | 26 Wh |
| Status | Commercial |
| API | yes |
| SDK | yes |
| SDK name | ROS 2 (TurtleBot 4 packages) |
| ROS | yes |
| On-board compute | yes |
| Compute | Raspberry Pi 4B 4GB |
| Sensors | 2D LiDAR (RPLIDAR A1M8), Depth camera (OAK-D-Pro) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

52 values from 6 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Variants | TurtleBot 4 (this file; OAK-D-Pro, UI board); TurtleBot 4 Lite (OAK-D-Lite, barebones) |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |
| Base platform | iRobot Create 3 |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |
| Manual version | TurtleBot 4 User Manual v2.0.1 |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 342 mm |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) · Hardware Specifications |
| Width | 339 mm |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |
| Height | 351 mm | TurtleBot 4 Lite 192 mm | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |
| Weight | 3,945 g | TurtleBot 4 Lite 3270 g | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |
| Wheel diameter | 72 mm |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |
| Ground clearance | 4.5 mm |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Max linear velocity | 0.46 m/s | without safe mode | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |
| Max linear velocity (safe mode) | 0.31 m/s |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |
| Max angular velocity | 1.9 rad/s |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |
| Max payload | 9 kg |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |
| Drive | Two wheels with current sensors and encoders + front caster (differential) |  | [iroboteducation.github.io](https://iroboteducation.github.io/create3_docs/hw/overview/) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery chemistry | Lithium ion |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |
| Battery capacity | 26 Wh |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |
| Battery nominal voltage | 14.4 V |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |
| Operation time | 2.5 - 4 h | depending on load | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |
| Available accessory power | 28.8 W | Create 3 power adapter total (RPi USB-C + VBAT aux) | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/electrical/power_budget.html) |
| Nominal power draw | 15 W | TurtleBot 4 total (13.8 W remaining) | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/electrical/power_budget.html) |
| Min recommended state of charge | 20 % | VBAT declines sharply below 20% | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/electrical/create3.html) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charging time | 2.5 h |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |
| Charging dock | Included (iRobot Home Base charging station) |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |
| Charging method | Autonomous docking via charging contacts on underside |  | [iroboteducation.github.io](https://iroboteducation.github.io/create3_docs/hw/overview/) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| LiDAR | RPLIDAR A1M8 360° 2D laser scanner |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) · Sensors |
| LiDAR range | 12 m |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) · Sensors |
| LiDAR FOV | 360 ° |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |
| Camera | Luxonis OAK-D-Pro (4K IMX214 colour + OV9282 stereo, IR dot projector and IR illumination LED, Myriad X VPU) |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) · Sensors |
| Colour sensor | 4K IMX214 |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) · Sensors |
| On-camera AI processor | Intel Myriad X VPU (OAK-D) |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) · Sensors |
| Bumper | Multizone front bumper with 7 pairs of IR proximity sensors |  | [iroboteducation.github.io](https://iroboteducation.github.io/create3_docs/hw/overview/) |
| Cliff sensors | 4 |  | [iroboteducation.github.io](https://iroboteducation.github.io/create3_docs/hw/overview/) |
| IMU | Yes (fused with optical odometry and wheel encoders) |  | [iroboteducation.github.io](https://iroboteducation.github.io/create3_docs/hw/overview/) |
| Optical floor odometry sensor | yes |  | [iroboteducation.github.io](https://iroboteducation.github.io/create3_docs/hw/overview/) |
| Wheel encoders / current sensors | yes |  | [iroboteducation.github.io](https://iroboteducation.github.io/create3_docs/hw/overview/) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| On-board computer | Raspberry Pi 4B 4GB |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |
| RAM | 4 GB |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |
| ROS 2 | ROS 2-based; manual changelogs for Galactic, Humble and Jazzy |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |
| Simulation | TurtleBot 4 Simulator (Gazebo), RViz2 |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| USB expansion | USB 3.0 Type-C ×4 (UI board), USB 3.0 Type-A ×1, USB 2.0 Type-A ×2 |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |
| Create 3 to Raspberry Pi link | USB 2.0 Type-C, up to 3 A at 5 V |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/electrical/create3.html) |
| Bluetooth | Create 3 adapter board supports Bluetooth; TurtleBot 4 controller (Bluetooth) included |  | [iroboteducation.github.io](https://iroboteducation.github.io/create3_docs/hw/overview/) |
| GPIO | 40-pin Raspberry Pi header passed through to UI board |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/electrical/rpi4.html) |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| User power | VBAT @ 300 mA; 12 V @ 300 mA; 5 V @ 500 mA; 3.3 V @ 250 mA |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |
| Create 3 VBAT connector | JST XH J7, PTC fuse 2 A |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/electrical/create3.html) |
| Top integration plate | HDPE plate, 4 × M4x0.7 round-head screws (2.5 mm hex), torque 25 N·cm; sensor tower and standoffs |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/mechanical/turtlebot4.html) |
| Create 3 mounting | Faceplate and cargo bay with regular hole pattern; two cable passthroughs |  | [iroboteducation.github.io](https://iroboteducation.github.io/create3_docs/hw/overview/) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Controller | TurtleBot 4 Bluetooth controller included (not with Lite) |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Display | 128x64 user display (OLED) |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |
| LEDs | Create 3 light ring (6 RGB); 2 user LEDs; status LEDs (power, motors, Wi-Fi, comms, battery) |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |
| Buttons | Create 3 user buttons ×2 + power button; 4 user buttons on UI board |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Included | Charging dock, TurtleBot 4 controller |  | [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html) |

## Documents

- [TurtleBot 4 User Manual — Features / Hardware Specifications (v2.0.1)](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html)
- [TurtleBot 4 User Manual — Mechanical](https://turtlebot.github.io/turtlebot4-user-manual/mechanical/turtlebot4.html)
- [TurtleBot 4 User Manual — Electrical: Create 3](https://turtlebot.github.io/turtlebot4-user-manual/electrical/create3.html)
- [TurtleBot 4 User Manual — Electrical: Raspberry Pi 4B](https://turtlebot.github.io/turtlebot4-user-manual/electrical/rpi4.html)
- [TurtleBot 4 User Manual — Power Budget](https://turtlebot.github.io/turtlebot4-user-manual/electrical/power_budget.html)
- [iRobot Create 3 Hardware Overview](https://iroboteducation.github.io/create3_docs/hw/overview/)

## Sources

- Official page: [turtlebot.github.io](https://turtlebot.github.io/turtlebot4-user-manual/overview/features.html)
- [github.com](https://github.com/turtlebot/turtlebot4)
- [github.com](https://github.com/turtlebot/turtlebot4/blob/jazzy/turtlebot4_description/urdf/standard/turtlebot4.urdf.xacro)
- [github.com](https://github.com/turtlebot/turtlebot4_simulator)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-25). Source repository: https://github.com/htcrefactor/robot-catalog*
