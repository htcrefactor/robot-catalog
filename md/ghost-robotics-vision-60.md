# Ghost Robotics Vision 60

> Rugged all-weather quadruped UGV for defense, public safety and industrial inspection with modular payloads.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=ghost-robotics-vision-60
- Category: Quadruped
- Locomotion: Legged
- Manufacturer: Ghost Robotics (United States)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 950 mm |
| Width | 570 mm |
| Height | 685 mm |
| Weight | 51 kg |
| Payload | 10 kg |
| Max speed | 2.4 m/s (8.6 km/h) |
| Degrees of freedom | 12 |
| Runtime | 3.15 h |
| IP rating | IP67 |
| Status | Commercial |
| API | yes |
| ROS | yes |
| On-board compute | yes |
| Compute | NVIDIA Xavier, 32 GB RAM, 2 TB NVMe SSD |
| Sensors | RGB camera ×5 (1080p), Intel RealSense D435 depth ×4, Dual-antenna RTK GPS |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

84 values from 3 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Manufacturer | Ghost Robotics |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.1 footer |
| Model | Vision 60 Q-UGV |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.1 |
| Robot type | Quadrupedal unmanned ground vehicle (Q-UGV), all-electric, all-weather |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.1–2 |
| Specification document | Spec sheet V3.3 (Black, 05-06-24), ©2024 Ghost Robotics |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · file name / footer |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Overall length | 950 mm | 37.5 in | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Key Dimensions |
| Overall width | 570 mm | 22.5 in | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Key Dimensions |
| Body width | 250 mm | 10 in | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Key Dimensions |
| Overall height (standing) | 685 mm | 27 in | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Key Dimensions |
| Ride height (to bottom of body) | 419 mm | 16.5 in | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Key Dimensions |
| Weight (tare) | 51 kg | 112 lb | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Weight |
| Construction | Aluminium & composites |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 General Robot Design |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Standard walk speed | 0.9 m/s | 2 mph | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Speed |
| Fast-walk speed | 1.2 m/s | Up to; 2.7 mph | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Speed |
| Sprint speed | 2.4 m/s | 4.9 mph; 'working towards 3.0 m/s (6.7 mph)'; speed depends on payload and terrain | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Speed |
| Max speed (product page) | 2.5 m/s | 'up to 2.5 meters/second (5.6 miles/hour)' – Performance Stats on product page | [ghostrobotics.io](https://www.ghostrobotics.io/vision-60) |
| Payload capacity | 10 kg | 22 lb | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Payload Capacity |
| Total DoF | 12 | 3 DoF per leg × 4 | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Actuation, Legs |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Terrain | Stairs, steep hills, rocks, swamps (wading), debris fields, steep inclines, tall grass, curbs and grated surfaces |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.1–2 |
| Stair climbing | Perception-aided stair climbing with steering assistance |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Autonomy Modes |
| Blind Mode | Proprietary 'Blind Mode' lets it navigate tall grass and unknown terrain even when vision sensors are obscured by mud, rain, snow or direct sunlight |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.1 |
| Mapping | Real-time 3D lidar-based SLAM; 3D digital twin maps, downloadable/uploadable between robots | Vision 60 Mission Control | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6821bc7f0a28f69e33d60eeb_Mission%20Control%20-%20Ghost%20Robotics_L0BuN0niHCgnrkr6RYRMH.pdf) |
| Localization | GPS-enabled (RTK) or GPS-denied (lidar SLAM) navigation |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6821bc7f0a28f69e33d60eeb_Mission%20Control%20-%20Ghost%20Robotics_L0BuN0niHCgnrkr6RYRMH.pdf) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Endurance (continuous walking) | 3.15 h | At 0.9 m/s; terrain and payload dependent | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Endurance |
| Range per charge | 10 km | Terrain and payload dependent | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Endurance |
| Range per charge (overview) | 6 mi | 'up to 6.0 miles on a single charge, depending on payload and operating conditions' | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.1 |
| Standby time | 21 h | Sitting with sensors, compute and radio on | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Endurance |
| Swappable battery | yes | Battery is a quick-swap field sub-assembly | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.1, p.2 |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charge time (standard battery) | 3 h | Approx. | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Endurance |
| Charging | All-electric direct charge |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 General Robot Design |
| Wireless charge kit | Wireless charging station for persistent 24x7 operation |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Wireless Charge Kit |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| Charging temperature | No charging below 0 °C; charging rate decreases above 40 °C |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 |
| IP rating | IP67 | Fully dust-sealed; can be submerged in up to 1 m of water for up to 30 minutes | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.1–2 |
| Operating temperature | -40 to 55 °C | -40 to 131 °F | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 |
| Cold start limit | -20 °C | Cold start not possible below -20 °C | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 |
| Weather | All-weather operation including rain, snow and sand |  | [ghostrobotics.io](https://www.ghostrobotics.io/vision-60) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| RGB cameras | 5 |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Integrated Sensors |
| RGB camera resolution | 1080p |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Integrated Sensors |
| Depth sensors | 4 |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Integrated Sensors |
| Depth sensor model | Intel RealSense D435 |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Integrated Sensors |
| GNSS | Dual-antenna RTK GPS |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Integrated Sensors |
| Camera interface | 16-channel GMSL2 on compute |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Compute |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Compute | NVIDIA® Xavier |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Compute |
| Memory (RAM) | 32 GB |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Compute |
| Storage | 2 TB NVMe SSD |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Compute |
| SDK | Ghost SDK – integrate any sensor, radio or electronics |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.1 Open Architecture |
| ROS | ROS and ROS2 |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.1, p.2 API |
| Low-level \| High-level \| Mission control API | C/C++, ROS, ROS2, MAVLink compatible, Zeno, ATAK, JSON Mission |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 |
| Low-level interface | C/C++ joint-level integration |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.1 |
| Simulator | Bullet Physics-based; Windows, Linux, Mac |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Simulator |
| Mission Control | Web-based 'single pane of glass' UI: telemetry, health and mission status; point-and-click mission planning, single-click execution, mission editor; human-readable mission scripts |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6821bc7f0a28f69e33d60eeb_Mission%20Control%20-%20Ghost%20Robotics_L0BuN0niHCgnrkr6RYRMH.pdf) |
| Mission Control hosting | Self hosted; device agnostic web interface; API support |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6821bc7f0a28f69e33d60eeb_Mission%20Control%20-%20Ghost%20Robotics_L0BuN0niHCgnrkr6RYRMH.pdf) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Wi-Fi | Integrated 2.4 and 5.8 GHz |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Communications |
| Cellular | Integrated 4G/LTE |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Communications |
| External radios | GigE switch supports any external radio including 5G, SDRs and SAT |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Communications |
| Ethernet | 3 × Ethernet |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 I/O |
| USB | 1 × USB 3.1 |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 I/O |
| Camera I/O | 6 × GMSL2 |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 I/O |
| Live video & detection | Live multi-camera and thermal video streams; real-time people and vehicle detections overlaid on map |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6821bc7f0a28f69e33d60eeb_Mission%20Control%20-%20Ghost%20Robotics_L0BuN0niHCgnrkr6RYRMH.pdf) |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Payload compensation | User-selectable payload compensation mode |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Payload Capacity |
| Modular payloads | Manipulator arm; security payload; LiDAR; low-light camera |  | [ghostrobotics.io](https://www.ghostrobotics.io/vision-60) |
| Payload power | 12 V regulated and 32–42 V unregulated |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 I/O |
| Mounting options | T-slots, M5 tapped holes or MIL-STD-1913 rails, with optional body panels |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 General Robot Design |
| Payload & configuration management | Setup of camera/sensor payloads; configuration tools for wireless docking, RTK positioning and lidar integration |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6821bc7f0a28f69e33d60eeb_Mission%20Control%20-%20Ghost%20Robotics_L0BuN0niHCgnrkr6RYRMH.pdf) |

### Actuation & Joints

| Spec | Value | Note | Source |
|---|---|---|---|
| Leg DoF | 3 |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Actuation, Legs |
| Number of legs | 4 |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.1 |
| Motors | 12 | 12-motor drive-train | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Actuation, Legs |
| Actuation | All-electric, back-drivable 12-motor drive-train |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 |
| Foot treads | Vibram® all-terrain treads, available in configurations including sand and ice |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Foot Treads |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Intended use | Defense, homeland and enterprise applications in unstructured urban and natural environments; improve situational awareness, lighten physical/cognitive workloads, increase standoff distance |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.1 |
| Application areas | Military, public safety, law enforcement, industrial inspection, construction, education, enterprise |  | [ghostrobotics.io](https://www.ghostrobotics.io/vision-60) |
| Fall recovery / inverted operation | Gets back up after slips/falls; capable of operating completely inverted |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.1, p.2 Actuation |
| Collision avoidance | Front and rear collision avoidance with static or moving obstacles |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Autonomy Modes |
| Obstacle avoidance (Mission Control) | 3D lidar detects and navigates around static and dynamic obstacles |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6821bc7f0a28f69e33d60eeb_Mission%20Control%20-%20Ghost%20Robotics_L0BuN0niHCgnrkr6RYRMH.pdf) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Tele-op controller | Samsung® Active Tab 3 standalone or combined with dual-joystick Operator Control Unit (OCU) |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 |
| Controller functions | Direct robot control, GPS path planning and diagnostics |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Tele-Op Controller |
| Autonomy modes | Perception-aided mobility; record-playback of pre-defined routes from OCU or any command-control station; Mission Control scriptable missions with reusable task-based plug-ins; footstep planning over curbs and grated surfaces |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Autonomy Modes |
| Manual control (Mission Control) | Basic manual command and control with third-party gamepads or joysticks |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6821bc7f0a28f69e33d60eeb_Mission%20Control%20-%20Ghost%20Robotics_L0BuN0niHCgnrkr6RYRMH.pdf) |
| Shared maps | Digital twin maps shared between robots so multiple units operate in the same mapped environment |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6821bc7f0a28f69e33d60eeb_Mission%20Control%20-%20Ghost%20Robotics_L0BuN0niHCgnrkr6RYRMH.pdf) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Audio | 2-way audio |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Lighting & Audio |
| Drive lights | Front & rear LED drive lights |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Lighting & Audio |
| Diagnostic lights | Side diagnostic LEDs |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Lighting & Audio |

### Transport & Storage

| Spec | Value | Note | Source |
|---|---|---|---|
| Field repair | Quick-swap sub-assemblies within minutes: legs, battery, main CPU, front & rear sensor heads |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.1–2 |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Export control classification | US ECCN EAR-99 | No ITAR restrictions | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Export Control \| HC |
| Harmonized code (HC) | 8479.50.00.00 Industrial Robots |  | [cdn.prod.website-files.com](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf) · p.2 Export Control \| HC |

## Documents

- [Ghost Robotics Vision 60 Specification Sheet V3.3 (05-06-24, ©2024)](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6805d36620e2aad6e552bb0d_SPECSHEET_V3.3%20Black%2005-06-24%20(1)_1736981609615.pdf)
- [Ghost Robotics Vision 60 product page](https://www.ghostrobotics.io/vision-60)
- [Vision 60 Mission Control datasheet (©2025)](https://cdn.prod.website-files.com/67b418349cd29a4f7829b4a5/6821bc7f0a28f69e33d60eeb_Mission%20Control%20-%20Ghost%20Robotics_L0BuN0niHCgnrkr6RYRMH.pdf)

## Notes

Ghost Robotics' own technical specifications on the Vision 60 page: 51 kg tare, 950 x 570 x 685 mm standing (250 mm body width, 419 mm ride height), 10 kg payload, standard walk 0.9 m/s with 1.2 m/s fast-walk and 2.4 m/s sprint (target 3.0), 3.15 h continuous walking at 0.9 m/s or 21 h standby, IP67, -40 to 55 C, 4G/LTE and Wi-Fi with a GigE switch. The Jetson Xavier 32 GB / 2 TB NVMe compute entry comes from the maker's spec sheet v3.3.

## Sources

- Official page: [ghostrobotics.io](https://www.ghostrobotics.io/vision-60)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-24). Source repository: https://github.com/htcrefactor/robot-catalog*
