# Rainbow Robotics RBQ-10

> Korean outdoor quadruped platform for patrol, inspection, observation and research with sensor expansion.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=rainbow-robotics-rbq-10
- Category: Quadruped
- Locomotion: Legged
- Manufacturer: Rainbow Robotics (South Korea)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 980 mm |
| Width | 430 mm |
| Height | 620 mm |
| Weight | 42 kg |
| Payload | 15 kg |
| Max speed | 3.89 m/s (14.0 km/h) |
| Runtime | 2 h |
| IP rating | IP54 |
| Status | Commercial |
| Price | about KRW 75 million for the base model (Rainbow Robotics technical director to Hankyoreh, Nov 2026) |
| SDK | yes |
| Sensors | IMU, RGB + depth camera ×2, Depth camera ×4, 3D LiDAR (optional), PTZ camera 32× zoom (optional), Thermal camera (optional) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

151 values from 22 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Manufacturer | Rainbow Robotics |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/intro.html) |
| Model | RBQ 10 (RBQ10) |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/general-specification.html) · RBQ 10 table |
| Robot type | Quadruped; dynamics-based gait control and learning-based locomotion |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/intro.html) |
| Variants | RBQ quadruped (default) and wheeled RBQ (12 leg joints + 4 driven wheels) supported in simulator |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/software/simulator/overview.html) |
| External port panel versions | Version 1 (USB-C labelled VISION/MOTION, dedicated LiDAR port) and version 2 (U-PC/R-PC, gigabit 12V/LAN) |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/interface/external-port.html) |
| Software release channels | Stable (vX.Y.Z, every version kept) and nightly (vX.Y.Z-nightly, newest only) |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/software/release-note/) |
| Variants | RB-Q10 (legged), RB-Q10W (wheeled), RB-Q10A (with robotic arm) | as shown at ROBOTWORLD 2026 | [en.fnnews.com](https://en.fnnews.com/news/202611041829341672) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 98 cm |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/general-specification.html) · Dimensions (L × W × H) |
| Width | 43 cm |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/general-specification.html) · Dimensions (L × W × H) |
| Height | 62 cm |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/general-specification.html) · Dimensions (L × W × H) |
| Weight (with battery) | 42 kg |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/general-specification.html) |
| Thigh length | 330 mm | Thigh→calf joint offset 0.33 m (URDF TF) | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/hardware/physical-parameter.html) |
| Calf length | 330 mm | Calf→foot offset 0.33 m (URDF TF) | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/hardware/physical-parameter.html) |
| Hip spacing (front–rear × lateral) | 624.36 × 180 mm | Hip roll joints at x = ±0.31218 m, y = ±0.09 m from body centre; hip-to-thigh lateral offset 0.10285 m | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/hardware/physical-parameter.html) |
| Link masses | Body 16.758 kg; per leg: hip 3.669344 kg, thigh 1.80014 kg, calf 0.452 kg, foot 0.06 kg |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/hardware/physical-parameter.html) · Link Mass & Inertia |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Walking speed | 9 km/h |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/general-specification.html) |
| Max speed (running mode) | 14 km/h | Up to, in running mode | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/general-specification.html) |
| Max payload | 15 kg | Total mass of everything mounted on top of the robot | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/guides/add-on/specifications.html) |
| Leg joints | 12 | HRR/HRP/HRK, HLR/HLP/HLK, FRR/FRP/FRK, FLR/FLP/FLK | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/hardware/physical-parameter.html) |
| Supported gaits (SDK) | sitting (0), standing (1), trotting – MPC trot (3), trot_stairs (4), waving – wave/slow walk (5), docking (10) |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/guides/sdk-cpp/high-level.html) · Supported gaits |
| App motions | SIT, STAND, WALK, STAIRS, DOCKING; Model Walk, Wave, Run; AI motions in developer mode: AI Pronk, AI Bound, AI Pace, AI Run, AI 2Leg L/R/F, AI 3Leg HL |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/gui/motion-commands.html) |
| Forward velocity command (SDK joystick example) | ±1.2 m/s | vel_x max in high-level example | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/guides/sdk-cpp/high-level.html) · Joystick velocity |
| Lateral velocity command (SDK joystick example) | ±0.5 m/s |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/guides/sdk-cpp/high-level.html) · Joystick velocity |
| Yaw rate command (SDK joystick example) | ±60 deg/s |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/guides/sdk-cpp/high-level.html) · Joystick velocity |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Longitudinal slope | 45 % |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/general-specification.html) · Walking Capability |
| Lateral slope | 20 % |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/general-specification.html) · Walking Capability |
| Stairs and steps | 25 cm | Up to | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/general-specification.html) · Walking Capability |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Operating time | 2 h | Up to 4 hours | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/general-specification.html) |
| Battery | Swappable / separate charging / automatic charging support |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/general-specification.html) |
| Battery packs | 2 | Detachable, 9 Ah each | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/battery.html) |
| Battery weight | 6.2 kg | 3.1 kg × 2 | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/battery.html) |
| Battery capacity | 18 Ah | 9 Ah × 2 | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/battery.html) |
| Battery energy | 907 Wh |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/battery.html) |
| Nominal voltage | 50.4 V |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/battery.html) |
| Battery rail voltage range | 42.0–58.4 V | Raw battery voltage on 48 V ports, varies with state of charge | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/interface/port-power.html) |
| Max time battery may be left in powered-off robot | 24 h | Longer can cause irreversible damage; remove battery for storage | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/safety/battery-handling.html) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charging time | 1 h | 20 to 80 % | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/battery.html) |
| Charging voltage / current | 58.8 V / 10.5 A |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/battery.html) |
| Charging methods | Supplied RBQ10 charger (top charging port, keyed twist-lock connector); docking station (bottom port); external cable from docking station to top port |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/operation/charging.html) |
| Charging a fully discharged robot | Docking station may not charge it; connect the supplied external charger directly |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/safety/battery-handling.html) |
| Docking station | Autonomous docking station for self-docking, automatic charging and storage ('Dog House' – coming soon) |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/accessories.html) |
| Docking station weight | 15 kg |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/docking-station.html) |
| Docking station dimensions | 640 × 550 × 653.5 mm |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/docking-station.html) |
| Docking station output | 58.8 V, 10.5 A |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/docking-station.html) |
| Docking station AC input | 63 Vac / 7 A; 230 Vac / 3.3 A; 277 Vac / 2.9 A |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/docking-station.html) |
| Docking station operating temperature | -40 to +70 °C |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/docking-station.html) |
| Docking station operating humidity | 20–95 % RH | Non-condensing | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/docking-station.html) |
| Docking station storage temperature | -40 to +85 °C |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/docking-station.html) |
| Docking station storage humidity | 10–95 % RH | Non-condensing | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/docking-station.html) |
| Auto-docking start distance | 3 m | Within 3 m and front or rear camera must recognize ArUco markers | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/operation/charging.html) |
| Docking procedure | Press Docking; robot recognizes marker, docks automatically and retries on failure |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/operation/charging.html) |
| Docking station installation | Water-resistant but keep terminals dry; shaded location recommended; secure to floor with fixing holes |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/operation/charging.html) |
| Battery charging tray | Optional two-bay tray to charge packs detached from the robot |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/accessories.html) |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| Ingress protection | IP54 |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/general-specification.html) |
| Operating temperature | -20 to +43 °C |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/general-specification.html) |
| Prohibited environments | Explosive atmospheres, flammable gas, heavy dust; strong magnetic fields and excessive vibration to be avoided |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/safety/operating-environment-requirements.html) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| IMU | Built-in IMU; offset from body centre (x, y, z) = (0.00665, 0, -0.0404) m |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/hardware/specification.html) |
| Gyroscope in-run bias | 5 °/hr |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/hardware/specification.html) · IMU Sensor Specification |
| Gyroscope range | ±2,000 °/s |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/hardware/specification.html) |
| Accelerometer range | ±16 g |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/hardware/specification.html) |
| Accelerometer in-run bias | < 0.04 mg |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/hardware/specification.html) |
| IMU data update rate | 800 Hz |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/hardware/specification.html) |
| Extended Kalman filter update rate | 400 Hz |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/hardware/specification.html) |
| Built-in cameras | (RGB + Depth) × 2, Depth × 4 |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/general-specification.html) |
| Front & rear cameras | Luxonis OAK-D Pro Wide |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/cameras.html) |
| Stereo depth FOV (DFOV/HFOV/VFOV) | 150 / 127 / 79.5 ° | OAK-D Pro Wide | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/cameras.html) |
| RGB FOV – IMX378 (DFOV/HFOV/VFOV) | 120 / 95 / 93 ° |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/cameras.html) |
| RGB FOV – OV9782 (DFOV/HFOV/VFOV) | 150 / 127 / 79.5 ° |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/cameras.html) |
| Ground-view camera | Intel RealSense D430 |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/cameras.html) |
| Body camera views | Front, rear, left, right; Quad 2×2 and Panorama views |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/gui/camera-vision.html) |
| 3D LiDAR | Optional |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/general-specification.html) |
| LiDAR options | Livox MID-360 (×2 front/rear), Livox MID-360S, Ouster OS1-32 (rear deck) |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/lidar.html) |
| MID-360 / MID-360S FOV | 360° H × −7° to 52° V |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/lidar.html) |
| MID-360 range | 40 m @10 %, 70 m @80 %; 0.1 m min |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/lidar.html) |
| MID-360S range | 40 m @10 %; 0.1 m min; 100 m cut-off |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/lidar.html) |
| MID-360 / MID-360S point rate | 200,000 points/s | First return | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/lidar.html) |
| OS1-32 FOV | 360° H × 45° V (+22.5° to −22.5°) |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/lidar.html) |
| OS1-32 range | 90 m @10 %, 170 m @80 %; 0.5 m min |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/lidar.html) |
| OS1-32 point rate | 655,360 points/s | 32 channels | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/lidar.html) |
| MID-360S mounting | Rotated 90° about vertical axis; connector faces robot-left (front) / robot-right (rear) |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/lidar.html) |
| GNSS / RTK | Optional receiver (LTE/GPS module); raw NMEA 0183 GNRMC/GNGGA/GNGST on ROS 2 topic /rbq/gps/nmea; RTK fixed/float reported |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/interface/gnss.html) |
| Surveillance sensors (optional) | 2 MP 32× zoom PTZ camera and thermal camera |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/general-specification.html) |
| PTZ zoom camera | Hanwha Vision XNZ-L6320AG |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/ptz-camera.html) |
| Zoom camera resolution | Up to 1920 × 1080 (1/2.8" 2 MP CMOS) |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/ptz-camera.html) |
| Zoom camera max frame rate | 60 fps (H.265/H.264), 30 fps (MJPEG) |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/ptz-camera.html) |
| Optical zoom | 32× (4.44–142.6 mm) |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/ptz-camera.html) |
| Zoom camera FOV | H 61.8° (wide) – 2.19° (tele); V 36.2° – 1.24° |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/ptz-camera.html) |
| Thermal camera resolution | Up to 640 × 512 |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/ptz-camera.html) |
| Thermal camera FOV | 48.7 × 38.6 ° |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/ptz-camera.html) |
| Thermal measurement range | -20 to +550 °C |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/ptz-camera.html) |
| PTZ microphone | 3.5 mm external jack |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/ptz-camera.html) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Motion PC (R-PC) | Standard; robot control; not user-accessible; IP 192.168.0.10 |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/interface/network.html) |
| User PC (U-PC) options | UP Xtreme i12 (Intel Core i7 12th gen), UP Xtreme i14 (Intel Core i7 14th gen), NVIDIA Jetson AGX Orin |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/accessories.html) |
| SDK | RBQ SDK: LV0 low-level (raw IMU/encoder data; joint position/velocity/torque commands) and LV1 high-level command interface |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/software/concept.html) |
| SDK languages | C/C++, Python, ROS2 |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/software/concept.html) |
| Communication interfaces | ROS2 SDK, DDS SDK, TCP/UDP |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/software/concept.html) |
| ROS version | ROS 2 Humble (rmw_cyclonedds_cpp); no driver node needed |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/software/sdk/ros/overview.html) |
| SDK host OS | Ubuntu 22.04 (x86_64); CMake ≥ 3.22; C++17; Eclipse Cyclone DDS |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/software/sdk/cpp/overview.html) |
| Simulators | MuJoCo and Ignition Gazebo (Fortress) full-stack; Isaac Gym (Preview 4) and Isaac Lab RL training; ONNX policy deploy |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/software/simulator/overview.html) |
| URDF & CAD | URDF and CAD files available from Downloads |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/hardware/specification.html) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Wi-Fi | 2.4 GHz and 5 GHz; access point 192.168.0.1 |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/interface/network.html) |
| Robot Wi-Fi | Robot provides its own access point named RBQ_{XX} |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/operation/controller-wifi-connect.html) |
| Communication | Wi-Fi / LTE (optional) |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/general-specification.html) |
| LTE | Optional LTE/GPS module (wide-area cellular + positioning) |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/accessories.html) |
| Remote (LTE) connection | 4-digit access code registers account-assigned robots for remote use over LTE |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/gui/connection.html) |
| Network switch | Gigabit Ethernet (1 Gbps) |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/interface/network.html) |
| Onboard IPs | R-PC 192.168.0.10; U-PC 192.168.0.12 (inside robot) / 192.168.0.13 (outside) |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/interface/network.html) |
| External interfaces | 54 V, 12 V, CAN (1 ch), Gigabit LAN × 3 |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/general-specification.html) |
| Port panel | POWER, PWR-CAN, 12V-LAN ×3, LiDAR (v1 only), EMO, USB-C ×2 direct to PCs |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/interface/external-port.html) |
| USB-C | 2 × USB-C direct to User PC (VISION/U-PC) and Robot PC (MOTION/R-PC) |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/interface/external-port.html) |
| CAN | 1 channel on PWR-CAN port, connected to Robot PC |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/interface/external-port.html) |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| PTZ control range | Pan ±165°; tilt −12° to +90° |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/ptz-camera.html) |
| PTZ unit weight | 5 kg |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/ptz-camera.html) |
| PTZ unit dimensions | 160 × 160 × 320 mm |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/ptz-camera.html) |
| POWER port | 42.0–58.4 V battery power, max 5 A |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/interface/external-port.html) |
| PWR-CAN port | 42.0–58.4 V battery power + CAN, max 10 A |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/interface/external-port.html) |
| 12V-LAN port (v1) | 12 V, max 2 A, Fast Ethernet 100 Mbps |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/interface/external-port.html) |
| 12V/LAN port (v2) | 12-pin: 4 gigabit LAN pairs + 12 V, 2–3 A |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/interface/external-port.html) |
| Payload connectors | MOCO waterproof connectors (12-pin 12V+LAN, 4-pin 48V+CAN, 2-pin 48V) |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/accessories.html) |
| Mounting interface | Top rail (slot) + spring nuts (MISUMI SHNTP5-5) |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/hardware/rail-spring-nut.html) |
| Switchable power rails | EXTERN (48V), ARM·ADDON (48V); 12 V toggles: speaker amp, LiDAR, CCTV, thermal, IR LED |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/interface/port-power.html) |
| Optional accessories | PTZ camera, LiDAR MID-360/OS1-32, User-PC module, hub module, Wi-Fi module, LTE/GPS module, battery, charging tray, docking station |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/accessories.html) |

### Actuation & Joints

| Spec | Value | Note | Source |
|---|---|---|---|
| Leg DoF | 3 | Hip roll, hip pitch, knee | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/hardware/specification.html) |
| Max angular velocity (hip roll / hip pitch / knee) | 14.4 / 14.4 / 11.15 rad/s |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/hardware/specification.html) |
| Nominal torque (hip roll / hip pitch / knee) | 40 / 40 / 50 N·m |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/hardware/specification.html) |
| Max torque (hip roll / hip pitch / knee) | 104 / 104 / 140 N·m |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/hardware/specification.html) |
| Rotor inertia (hip roll / hip pitch / knee) | 0.014058265 / 0.014058265 / 0.0214816 |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/hardware/specification.html) |
| Hip roll range | Left −30° to 43°; right −43° to 30° |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/hardware/specification.html) |
| Hip pitch range | No limit |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/hardware/specification.html) |
| Knee range | −158.1° to −19.3° |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/hardware/specification.html) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Emergency stop | Physical E-stop push button on rear (all joints to High Damping); app E-STOP cuts all motor power |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/safety/emergency-stop-procedures.html) |
| Stopping distance | 1 m | Up to about 1 m on flat ground; longer on slopes/uneven floors | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/safety/emergency-stop-procedures.html) |
| Safety features | E-Stop, remote stop, speed limit, posture stabilization; auto stop on fall, low battery, app stop, mission interrupt |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/safety/emergency-stop-procedures.html) |
| Exclusion zone | 2 m | No people or animals within 2 m while operating | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/safety/general-safety-warning-precautions.html) |
| Legs after power-off | Legs do not auto-lock; may slide/roll on slopes |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/safety/emergency-stop-procedures.html) |
| Intended use | Transport and movement in industrial sites, restricted areas, supervised environments; non-contact sensing/monitoring payloads; surveillance, reconnaissance, safety management |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/safety/user-responsibility-disclaimer.html) |
| Prohibited uses | Riding/carrying people or animals, underwater/airborne, weapon or medical use, home use, hazardous materials, collaborative work; low-level joint API needs separate risk assessment |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/safety/user-responsibility-disclaimer.html) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Controller | RBQ Controller app: Android (Google Play), iPhone/iPad (App Store), Linux desktop / Steam Deck (AppImage; built-in gamepad) |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/downloads/) |
| Auto-start stages | POWER, CAN-BUS, HOMING, IMU-CHECK, START |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/operation/controller-wifi-connect.html) |
| Cruise control | R3 starts cruise; D-pad changes speed (trot gaits) |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/gui/developer-mode.html) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| PTZ speaker | Up to 25 W; 100–20,000 Hz |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/related-products/ptz-camera.html) |
| Walkie-talkie audio | Robot speaker and microphone; app listens and push-to-talk through robot speaker |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/gui/audio.html) |
| IR LED | IR LED night illumination (12 V toggle); night mode switches IR-cut filter |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/gui/maintenance.html) |
| Robot lights | Robot battery lights, robot status lights (blinking), power button status light |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/interface/external-port.html) |

### Transport & Storage

| Spec | Value | Note | Source |
|---|---|---|---|
| Case (Pelican 1730) external dimensions | 86.3 × 60.9 × 31.7 cm | 37.50 × 27.13 × 14.37 in | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/operation/packing.html) |
| Case empty weight | 20 kg | 44 lb | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/operation/packing.html) |
| People required to lift | 2 | Lift by handles, power off | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/safety/handling-and-transportation.html) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Packing list (standard) | RBQ10 ×1, battery charger ×1, spare rubber foot ×4, spare body bumper, remote controller ×1, basic tools (wrench) ×1 set |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/operation/packing.html) |
| Navigation Pack | Standard list + LiDAR module ×1 |  | [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/operation/packing.html) |
| Price | 75,000,000 KRW | about; base model, per Rainbow Robotics technical director | [hani.co.kr](https://www.hani.co.kr/arti/economy/marketing/1285758.html) |
| Status | Mass (limited) production began 2026; 300–400 units planned for 2027 |  | [hani.co.kr](https://www.hani.co.kr/arti/economy/marketing/1285758.html) |

## Documents

- [RBQ manual – full text (llms-full.txt)](https://rainbowrobotics.github.io/RBQ/llms-full.txt)
- [RBQ Series General Specifications](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/general-specification.html)
- [Hardware Specification (joints, IMU)](https://rainbowrobotics.github.io/RBQ/manual/hardware/specification.html)
- [Physical Parameter](https://rainbowrobotics.github.io/RBQ/manual/hardware/physical-parameter.html)
- [Battery](https://rainbowrobotics.github.io/RBQ/manual/related-products/battery.html)
- [Docking Station](https://rainbowrobotics.github.io/RBQ/manual/related-products/docking-station.html)
- [Cameras](https://rainbowrobotics.github.io/RBQ/manual/related-products/cameras.html)
- [LiDAR](https://rainbowrobotics.github.io/RBQ/manual/related-products/lidar.html)
- [PTZ Camera](https://rainbowrobotics.github.io/RBQ/manual/related-products/ptz-camera.html)
- [External Port Information](https://rainbowrobotics.github.io/RBQ/manual/interface/external-port.html)
- [Powering the external ports](https://rainbowrobotics.github.io/RBQ/manual/interface/port-power.html)
- [Network](https://rainbowrobotics.github.io/RBQ/manual/interface/network.html)
- [Accessories](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/accessories.html)
- [Packing](https://rainbowrobotics.github.io/RBQ/manual/operation/packing.html)
- [Charging](https://rainbowrobotics.github.io/RBQ/manual/operation/charging.html)
- [Emergency Stop Procedures](https://rainbowrobotics.github.io/RBQ/manual/safety/emergency-stop-procedures.html)
- [User Responsibility Disclaimer](https://rainbowrobotics.github.io/RBQ/manual/safety/user-responsibility-disclaimer.html)
- [SDK concept](https://rainbowrobotics.github.io/RBQ/software/concept.html)
- [ROS2 SDK overview](https://rainbowrobotics.github.io/RBQ/software/sdk/ros/overview.html)
- [Simulator overview](https://rainbowrobotics.github.io/RBQ/software/simulator/overview.html)
- [Hankyoreh – 2026 로보월드 (RBQ-10 price, 2026-11-04)](https://www.hani.co.kr/arti/economy/marketing/1285758.html)
- [Financial News – 2026 RoboWorld (RBQ series, 2026-11-04)](https://en.fnnews.com/news/202611041829341672)

## Notes

Maker page: 98 x 43 x 62 cm, 42 kg, 15 kg payload, walking 6 km/h and running 14 km/h (3.89 m/s recorded as max, the page also lists 9 km/h as the working walk), 2 h standard with up to 4 h, IP54, IMU plus RGB/depth cameras with optional 3D lidar, PTZ or thermal payloads. The KRW 75 million figure in price_note is a press remark by a Rainbow Robotics technical director, not a maker price.

## Sources

- Official page: [rainbow-robotics.com](https://rainbow-robotics.com/en/products/rbq-10)
- [rainbowrobotics.github.io](https://rainbowrobotics.github.io/RBQ/manual/product-descriptions/general-specification.html)
- [hani.co.kr](https://www.hani.co.kr/arti/economy/marketing/1285758.html)
- [rainbow-robotics.com](https://rainbow-robotics.com/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-18). Source repository: https://github.com/htcrefactor/robot-catalog*
