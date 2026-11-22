# UBTECH Robotics Walker S2

> UBTECH's second-generation industrial humanoid, the first able to swap its own battery for 24/7 work, aimed at automotive and smart-factory tasks with a 15 kg dual-arm payload across a 0-1.8 m workspace.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=ubtech-walker-s2
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: UBTECH Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Height | 1,760 mm |
| Weight | 70 kg |
| Payload | 15 kg |
| Degrees of freedom | 52 |
| Runtime | 2.5 h |
| Released | 2025 |
| Status | Commercial |
| API | yes |
| SDK | yes |
| SDK name | UBTECH Walker S2 ROS 2 SDK |
| ROS | yes |
| On-board compute | yes |
| Compute | x86 (Intel i7 class) + NVIDIA Jetson Orin; Ubuntu + ROSA 2.0 |
| Sensors | Depth camera, Six-axis force/torque sensor, IMU, Fisheye camera, 4-microphone array and 4-inch circular display |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

140 values from 3 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| SDK document version | V1.0 (2025-10-31) |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) |
| Form factor | full-size | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/ubtech-walker-s2) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Height | 176 cm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.1 |
| Arm span | 177 cm | excluding dexterous hand | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.1 |
| Weight | 70 kg | excluding dexterous hand | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.1 |
| Height (standing) | 176 cm | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/ubtech-walker-s2) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total degrees of freedom | 42 | 42 integrated joint motors incl. 3rd-gen hands | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1 |
| Payload capacity | 15 kg | max 15 kg for both arms | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.1 |
| Top speed | 2 m/s | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/ubtech-walker-s2) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Power supply | Li-ion battery |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) |
| Battery voltage | 48 V DC |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) |
| Comprehensive endurance | 2.5 h |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) |
| Autonomous hot-swap battery | yes | dual-battery, dual-arm self-swap | [ubtrobot.com](https://www.ubtrobot.com/en/humanoid/products/walker-s2) |
| Dual-battery mode | Switchable dual-battery / single-battery working mode |  | [ubtrobot.com](https://www.ubtrobot.com/en/humanoid/products/walker-s2) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charging voltage / current | DC 54 V / 8 A |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.1 |
| Autonomous battery swap time | 3 min | within 3 minutes | [ubtrobot.com](https://www.ubtrobot.com/en/humanoid/products/walker-s2) |
| Battery swap station | yes | chooses swap or charge mode by task priority | [ubtrobot.com](https://www.ubtrobot.com/en/humanoid/products/walker-s2) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| RGB-D cameras | Orbbec Gemini 2L x2 | body back and waist front | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §5.3 |
| Head stereo vision | Pure RGB binocular stereo (passive), deep-learning depth |  | [ubtrobot.com](https://www.ubtrobot.com/en/humanoid/products/walker-s2) |
| Fisheye cameras | Left/right fisheye cameras |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §5.4 |
| 6-axis force sensors | Left and right arm 6-axis F/T |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) |
| IMU | Motion IMU + Orin IMU |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) |
| Microphone array | yes |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Computing configuration | x86 + NVIDIA Jetson Orin |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.1 |
| Operating system | Ubuntu + ROSA 2.0 | Orin: Ubuntu 20.04.6; x86: Ubuntu 22.04.4 | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.1, §3.4.1 |
| ROS 2 | yes | ROS 2 SDK in Docker container | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §3.2 |
| ROS 2 distribution | Humble |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §3.4.1 |
| SDK examples | C++ |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) |
| SDK | UBTECH Walker S2 ROS 2 SDK (motor, force sensor, IMU, camera, battery, audio, hand interfaces) | Mac/Windows dev not supported | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §3.2 |
| Cloud platform | UBTECH cloud: fault detection, OTA, MQTT task scheduling, multi-robot collaboration |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §3.1.1 |
| Intelligent OTA update | yes |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Ethernet | yes | robot Ethernet port, 192.168.11.x | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §2.3 |
| Onboard computer IPs | 192.168.11.2 / 192.168.11.3 |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| DoF per hand | 6 | 3rd-generation dexterous hand; fingertips passive | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) |
| Lifting workspace | 0-1.8 m | handles 15 kg payload within 0-1.8 m workspace | [ubtrobot.com](https://www.ubtrobot.com/en/humanoid/products/walker-s2) |
| Hand linear drive speed | 25 (rated) / 39 (max) mm/s | 3rd-gen hand linear drives | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) |
| Hand drive thrust | 45.53 (rated) / 100 (peak) N |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) |
| Four-finger palmar rotation | 88.92 ° | fingertip passive rotation 93.06° | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) |
| Thumb flexion | 58 ° | fingertip passive 60° | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) |
| Thumb abduction | 65.34 ° |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) |
| Hands | included | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/ubtech-walker-s2) |

### Actuation & Joints

| Spec | Value | Note | Source |
|---|---|---|---|
| Head DoF | 2 |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) |
| DoF per arm | 7 | shoulder, elbow, wrist | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) |
| Waist DoF | 2 | pitch + yaw | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) |
| DoF per leg | 6 | hip, knee, ankle | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) |
| Waist rotation | ±162 ° | product page; SDK table lists waist yaw ±160° | [ubtrobot.com](https://www.ubtrobot.com/en/humanoid/products/walker-s2) |
| Waist pitch (product page) | 125 ° | pitch angle for deep squat / stoop lifting | [ubtrobot.com](https://www.ubtrobot.com/en/humanoid/products/walker-s2) |
| Head pitch – range | -39 to 29 ° |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Head pitch – rated speed | 30 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Head pitch – max speed | 50 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Head pitch – rated torque | 3 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Head pitch – peak torque | 4.5 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Head yaw – range | -94 to 94 ° |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Head yaw – rated speed | 30 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Head yaw – max speed | 50 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Head yaw – rated torque | 3 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Head yaw – peak torque | 4.5 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Shoulder pitch – range | -162 to 162 ° | left side; right mirrored | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Shoulder pitch – rated speed | 20 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Shoulder pitch – max speed | 30 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Shoulder pitch – rated torque | 27 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Shoulder pitch – peak torque | 80 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Shoulder roll – range | -106 to 5 ° | left side; right mirrored | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Shoulder roll – rated speed | 20 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Shoulder roll – max speed | 30 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Shoulder roll – rated torque | 27 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Shoulder roll – peak torque | 80 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Shoulder yaw – range | -166 to 166 ° | left side; right mirrored | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Shoulder yaw – rated speed | 20 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Shoulder yaw – max speed | 30 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Shoulder yaw – rated torque | 17 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Shoulder yaw – peak torque | 45 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Elbow roll – range | -150 to 0 ° | left side; right mirrored | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Elbow roll – rated speed | 20 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Elbow roll – max speed | 30 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Elbow roll – rated torque | 17 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Elbow roll – peak torque | 45 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Elbow yaw – range | -167 to 167 ° | left side; right mirrored | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Elbow yaw – rated speed | 20 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Elbow yaw – max speed | 30 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Elbow yaw – rated torque | 17 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Elbow yaw – peak torque | 20 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Wrist pitch – range | -91 to 91 ° | left side; right mirrored | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Wrist pitch – rated speed | 20 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Wrist pitch – max speed | 30 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Wrist pitch – rated torque | 17 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Wrist pitch – peak torque | 20 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Wrist roll – range | -114 to 114 ° | left side; right mirrored | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Wrist roll – rated speed | 20 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Wrist roll – max speed | 30 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Wrist roll – rated torque | 17 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Wrist roll – peak torque | 20 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Waist pitch – range | -89 to 35 ° |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Waist pitch – rated speed | 15 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Waist pitch – max speed | 20 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Waist pitch – rated torque | 79 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Waist pitch – peak torque | 265 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Waist yaw – range | -160 to 160 ° |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Waist yaw – rated speed | 20 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Waist yaw – max speed | 37 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Waist yaw – rated torque | 35 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Waist yaw – peak torque | 85 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Hip roll – range | -23 to 44 ° | left side; right mirrored | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Hip roll – rated speed | 50 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Hip roll – max speed | 80 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Hip roll – rated torque | 75 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Hip roll – peak torque | 225 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Hip yaw – range | -60 to 45 ° | left side; right mirrored | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Hip yaw – rated speed | 50 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Hip yaw – max speed | 80 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Hip yaw – rated torque | 22 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Hip yaw – peak torque | 65 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Hip pitch – range | -30 to 109 ° | left side; right mirrored | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Hip pitch – rated speed | 50 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Hip pitch – max speed | 80 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Hip pitch – rated torque | 75 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Hip pitch – peak torque | 225 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Knee – range | -129 to 3 ° | left side; right mirrored | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Knee – rated speed | 50 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Knee – max speed | 80 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Knee – rated torque | 75 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Knee – peak torque | 225 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Ankle (inside/outside drive) – range | -68 to 38 / -38 to 68 ° | left side; right mirrored | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Ankle (inside/outside drive) – rated speed | 50 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Ankle (inside/outside drive) – max speed | 80 rpm |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Ankle (inside/outside drive) – rated torque | 22 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |
| Ankle (inside/outside drive) – peak torque | 65 N·m |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.2 |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Emergency stop | Button on robot back |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §2.1 |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Control modes | Remote controller modes incl. force-control mode and task flow |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) |
| Boot time | 1 min | approximately | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §2.2 |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Interactive screen | 4-inch round interactive screen |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) · §1.1 |
| Battery status indicator | yes | leg LEDs indicate startup complete | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) |
| Speaker | Built-in, TTS playback |  | [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Sales status | b2b-only | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/ubtech-walker-s2) |
| Who can buy | business | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/ubtech-walker-s2) |
| Route to US | unclear | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/ubtech-walker-s2) |
| Route to EU | reseller | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/ubtech-walker-s2) |
| Sellers listed | 3 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/ubtech-walker-s2) |
| Deployment stage | pilot | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/ubtech-walker-s2) |
| Documented uses | Real work / logistics | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/ubtech-walker-s2) |

## Documents

- [UBTECH Walker S2 SDK Secondary Development Document [External] V1.0 (2025-10-31)](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf)
- [UBTECH Walker S2 product page](https://www.ubtrobot.com/en/humanoid/products/walker-s2)
- [HumanoidStore datasheet – UBTech Robotics Walker S2 (CC BY 4.0)](https://humanoidstore.co/robots/ubtech-walker-s2)

## Notes

Maker figures (product page and Walker S2 Product Manual V1.0, 2025-09-23): 176 cm, 70 kg without hands, 177 cm arm span, 6 DoF per leg, 2 waist, 2 head and 7 per arm excluding the hand, 15 kg dual-arm payload, x86 plus Jetson Orin, depth camera, six-axis force/torque, IMU, fisheye, 4-inch round screen, 48 V DC lithium battery charged at 54 V / 8 A, 2.5 h runtime, Ubuntu + ROSA 2.0, waist +/-162 deg, 125 deg body pitch, autonomous battery swap in under 3 minutes. Total DoF is recorded as 52 = 30 body (12 legs, 2 waist, 2 head, 14 arms) plus 22 hands; the maker does not state a single total.

## Sources

- Official page: [ubtrobot.com](https://www.ubtrobot.com/en/humanoid/products/walker-s2)
- [a.storyblok.com](https://a.storyblok.com/f/298593/x/1329253096/ubtech-walker-s2-sdk-secondary-development-document-external.pdf)
- [ubtrobot.com](https://www.ubtrobot.com/cn/humanoid/products/walker-s2)
- [cdn.robotshop.com](https://cdn.robotshop.com/media/U/Ubt/RB-Ubt-37/pdf/ubtech-walker-s2-product%20manual.pdf)
- [humanoidstore.co](https://humanoidstore.co/robots/ubtech-walker-s2)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-22). Source repository: https://github.com/htcrefactor/robot-catalog*
