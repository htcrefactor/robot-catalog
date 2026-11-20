# ANYbotics ANYmal (Gen D)

> Autonomous IP67 legged robot for routine visual, thermal and acoustic inspection in industrial plants.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=anybotics-anymal-d
- Category: Quadruped
- Locomotion: Legged
- Manufacturer: ANYbotics (Switzerland)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 930 mm |
| Width | 530 mm |
| Height | 890 mm |
| Weight | 50 kg |
| Payload | 10 kg |
| Max speed | 1.3 m/s (4.7 km/h) |
| Runtime | 1.5 h |
| Battery | 932.4 Wh |
| IP rating | IP67 |
| Status | Commercial |
| API | yes |
| ROS | yes |
| On-board compute | yes |
| Compute | 2× 8th Gen Intel Core i7 (6-core), 2× 8 GB RAM, 2× 240 GB SSD, Ubuntu 20.04 |
| Sensors | LiDAR (16-channel), Depth cameras, Tele-operation cameras, Zoom camera (20× optical, payload), Thermal camera (payload), Ultrasonic microphone (payload), Spotlight |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

112 values from 2 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Manufacturer | ANYbotics AG |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) |
| Manufacturer address | Hagenholzstrasse 83a, 8050 Zürich, Switzerland |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.12 |
| Model | ANYmal (Generation D) |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.1 |
| Data sheet document number | ANY-TECR-000082-00 | V.1 – May 2022 | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.12 |
| Robot type | Autonomous legged industrial inspection robot |  | [anybotics.com](https://www.anybotics.com/robotics/anymal/) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 930 mm |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Width | 530 mm | default walking | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Height (standing) | 890 mm | default walking | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Height (lying on ground) | 470 mm | lying on ground | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Weight | 50 kg | robot without inspection payload | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Weight | 55.7 kg | with Inspection Payload | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Maximum walking speed | 1.3 m/s | rough or slippery terrain may reduce walking speed | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Recommended walking speed | 0.75 m/s | recommended for safe and efficient operation | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Omnidirectional motion | yes | steps sideways and turns in place | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.3 |
| Positioning accuracy | centimeter accuracy | knows its absolute location with centimeter accuracy | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.3 |
| Payload (nominal) | 10 kg | under nominal conditions | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.10 |
| Maximum payload | 15 kg | with reduced performance, e.g. walking speed and operating time | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.10 |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Step | 250 mm |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.3 |
| Maximum stair inclination | 45 ° | climbing and descending industrial stairs | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.3 |
| Maximum stair rise | 230 mm |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.3 |
| Minimum stair run | 210 mm |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.3 |
| Minimum stair width | 800 mm |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.3 |
| Stair types | Open risers; grated steps |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.3 |
| Narrow space | 600 mm |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.3 |
| Slope | ±30 ° |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.3 |
| Gap | 300 mm |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.3 |
| Suspended (low clearance) | 600 mm | listed as 'Suspended 600 mm' in mobility highlights; product page: 'Crawl in low positions' | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.3 |
| Surface compatibility | Metal, concrete, gratings/checkerboards, gravel, dirty, wet and slippery floors | industrial floor | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Navigation | Autonomous navigation between waypoints along the shortest path; dynamic route planning/re-planning; works without internet connection |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.4 |
| Deployment / mapping | Show & Go (manual guiding through the plant) or import of CAD/BIM models |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.4 |
| Localization | LiDAR-based localization & mapping | onboard LiDAR used for mapping, localization and collision avoidance up to 100 m | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery type | Swappable Li-ion battery |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Battery swappable | yes |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Battery certification | UN 38.3 |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Battery capacity | 932.4 Wh |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Running time | 90–120 min | on a full charge | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Range per charge | 4 km | on a full charge | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Range per charge | 2 km | up to 2 km for a typical inspection mission, depending on payload weight and number of inspection points | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Battery dimensions | 466 × 136 × 78 mm | L/W/H | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Battery weight | 5.5 kg |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Recharge time | 3 h | full charge | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Recharge time | 100 min | 70 % quick charge | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Charging methods | Battery charged in the robot, outside the robot, or automatically with the docking station |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.8 |
| Charger power supply | 110–240 V / 50–60 Hz |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.8 |
| Charger ingress protection | IP65 |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.8 |
| Charger cable length | 5 m | 16.4 ft | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.8 |
| Charger dimensions | 145 × 300 × 124 mm | L/W/H | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.8 |
| Charger weight | 3.5 kg |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.8 |
| Docking station | yes | permits the robot to recharge itself after missions; additional docking stations extend mission range | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.8 |
| Automatic return to dock | yes | robot navigates to docking station when battery is low and resumes mission after charging | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.4 |
| Docking station ingress protection | IP65 |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.8 |
| Docking station required space for charging | 1000 × 800 mm | L/W | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.8 |
| Docking station dimensions | 145 × 300 × 124 mm | L/W/H as stated in the datasheet | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.8 |
| Docking station weight | 1.4 kg |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.8 |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| Ingress protection | IP67 | fully protected against water and dust; operates in humid and dusty conditions | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Operating temperature | 0 to 40 °C | specified | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Operating temperature | −10 to 50 °C | typical | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Lighting requirements | No light required for autonomous operation and inspection; low light (min. 20 lux) needed for automatic docking and tele-operation | day & night | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| LiDAR | 16-channel 3D LiDAR, 360° |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| LiDAR point rate | 300,000 points/s | full sweep at 10 Hz | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| LiDAR range | 0.4–100 m | 3 cm accuracy (typical) | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| LiDAR field of view | 360 × 15.0 to −15.0 ° | horizontal × vertical | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Depth cameras | 6 |  | [anybotics.com](https://www.anybotics.com/robotics/anymal/) |
| Depth camera range | 0.3–3 m |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Depth camera FOV | 87.3 × 58.1 × 95.3 ° | horizontal / vertical / diagonal; Class 1 laser product under EN/IEC 60825-1 Ed. 3 (2014) | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Tele-operation cameras | 2 | optical tele-operation cameras | [anybotics.com](https://www.anybotics.com/robotics/anymal/) |
| Tele-operation camera resolution | 1440 × 1080 px |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Tele-operation camera FOV | 110 × 76.5 × 117.7 ° | horizontal / vertical / diagonal | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Zoom camera resolution | 1920 × 1080 @ 15 FPS (default); 3840 × 2160 @ 30 FPS (maximum) | inspection payload; datasheet lists 1080 × 1920 px FullHD default, 2160 × 3840 px QFHD/4K max | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.6 |
| Zoom camera optical zoom | 20× | 70.2° to 4.1° horizontal FOV | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.6 |
| Thermal camera | 336 × 256 px, 46° horizontal FOV, radiometric | inspection payload | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.6 |
| Thermal measurement range | −40 to +550 °C | radiometry | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.6 |
| Ultrasonic microphone | 0–384 kHz sampling frequency | inspection payload; audible and ultrasonic frequencies | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.6 |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Computers | 2× 8th Gen Intel Core i7 (6-core) |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Memory (RAM) | 2× 8 GB |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Hard disks | 2× 240 GB SSD |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Operating system | Ubuntu 20.04 |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| API | gRPC-based ANYmal API (server); on-robot API based on ROS with C++ plugins for inspection modules |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.10 |
| ROS support | yes | on-robot API based on open-source ROS | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.10 |
| Server software | ANYmal Server (on-premise or cloud): data sync, mission control, API for third-party data portals |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.8 |
| Data security | Enterprise WPA2 Wi-Fi supported; file transfers encrypted by TLS 1.2; live data protected by VPN; authorization via TLS certificates |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.10 |
| Inspection report formats | PDF or XML |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.8 |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Wi-Fi | Built-in module 2.4 / 5 GHz, 802.11ac wave2; access point or client mode |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| 4G LTE | Add-on module, LTE Cat.12 |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| USB | USB link with Type-C connector | interface on robot platform | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.10 |
| Ethernet | M12 X-coded Ethernet link to onboard network | interface on robot platform | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.10 |
| Time sync | Time sync trigger | interface on robot platform | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.10 |
| Inspection payload data links | RS232; RS485 | additional interface on inspection payload | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.10 |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Pan-tilt range of motion | Pan ±165°, tilt −90°/+180° | inspection payload | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.6 |
| Pan-tilt speed | 340 °/s |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.6 |
| Inspection payload dimensions | 229 × 177 × 246 mm | L/W/H | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.6 |
| Inspection payload weight | 5.7 kg |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.6 |
| Payload electrical power | Regulated 12 VDC / 3 A; 2× 12 V / 1 A; unregulated battery voltage (30.4–50.4 VDC) / 3 A |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.10 |
| Mechanical interface | 12× M4 screw holes |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.10 |
| Payload weight | 10 kg | up to 10 kg under nominal conditions, up to 15 kg with reduced performance | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.10 |
| Optional sensors | Acoustic imager (Sorama) for gas leaks / partial discharge; up to two gas concentration sensors (Honeywell) |  | [anybotics.com](https://www.anybotics.com/robotics/anymal/) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| LiDAR laser class | Class 1 eye-safe per IEC 60825-1:2007 & 2014, 905 nm |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.7 |
| Emergency stop (robot) | Push button on the robot disconnects complete power supply; ISO 13849-1:2015 Category 3 PL c |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.10 |
| Remote control emergency stop | Push button on remote control disables the actuators; ISO 13849-1:2015 Category 3 PL c |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.10 |
| Performance level | PL c, Category 3 (ISO 13849-1:2015) | both emergency stop functions | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.10 |
| Compliance | CE marked: Machinery Directive 2006/42/EC, EMC Directive 2014/30/EU, Low Voltage Directive 2014/35/EU, Radio Equipment Directive 2014/53/EU, RoHS 2011/65/EU |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.10 |
| Compliance marks | FCC, CE and Anatel compliant |  | [anybotics.com](https://www.anybotics.com/robotics/anymal/) |
| Collision avoidance modes | Stop & Go (stops before obstacles, resumes when cleared); Obstacle Avoidance (reroutes or replans); safe stop near cliffs |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.4 |
| Protective stop | Protective stop button in Operator GUI |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.9 |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Remote control | Ruggedized tablet |  | [anybotics.com](https://www.anybotics.com/robotics/anymal/) |
| Operator GUI | Mission panel, robot status bar, protective stop, 3D visualization, inspection window, sensor panel; Mission Editor with rule-based logic |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.9 |
| Autonomy features | Full autonomy: mission control & robot behavior, localization & mapping, path planning & motion control, inspection intelligence, autonomous recharging |  | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.8 |
| Tele-operation | yes | via Operator PC GUI over Wi-Fi or LTE | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.8 |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Spotlight | 1895 lm continuous; 3790 lm for short time | inspection payload | [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf) · p.6 |
| Warning light | Warning light indicates the need to keep safety distance when robot is in operation |  | [anybotics.com](https://www.anybotics.com/robotics/anymal/) |

### Transport & Storage

| Spec | Value | Note | Source |
|---|---|---|---|
| Safety handles | Safety handles for ergonomic and safe transportation |  | [anybotics.com](https://www.anybotics.com/robotics/anymal/) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Included | Charger, docking station, ruggedized tablet for remote control, transportation box | "More than a robot" | [anybotics.com](https://www.anybotics.com/robotics/anymal/) |

## Documents

- [ANYmal Technical Specifications, Generation D (V.1, May 2022, ANY-TECR-000082-00)](https://www.anybotics.com/anymal-technical-specifications.pdf)
- [ANYbotics ANYmal product page](https://www.anybotics.com/robotics/anymal/)

## Notes

ANYmal technical specifications (V.1 May 2022) and the Apr 2024 sheet: 930x530x890 mm walking, 50 kg (55.7 kg with inspection payload), payload up to 10 kg nominal (15 kg with reduced performance), 1.3 m/s max (0.75 m/s recommended), 90-120 min on 932.4 Wh, IP67, 2x 8th-gen Intel Core i7 with 2x 8 GB RAM and 2x 240 GB SSD, Ubuntu 20.04, 16-channel lidar plus depth and tele-operation cameras, ANYmal API.

## Sources

- Official page: [anybotics.com](https://www.anybotics.com/robotics/anymal/)
- [anybotics.com](https://www.anybotics.com/anymal-technical-specifications.pdf)
- [github.com](https://github.com/ANYbotics/anymal_d_simple_description/blob/master/urdf/anymal.urdf)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-20). Source repository: https://github.com/htcrefactor/robot-catalog*
