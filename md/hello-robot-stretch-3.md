# Hello Robot Stretch 3

> Lightweight differential-drive mobile manipulator with lift and telescoping arm for in-home and assistive manipulation research.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=hello-robot-stretch-3
- Category: Mobile platform
- Locomotion: Wheeled
- Manufacturer: Hello Robot (United States)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 340 mm |
| Width | 330 mm |
| Height | 1,410 mm |
| Weight | 24.5 kg |
| Payload | 2 kg |
| Wheel diameter | 101.6 mm |
| Runtime | 2 h |
| Status | Commercial |
| Price | US$24,950 (list price on manufacturer product page) |
| API | yes |
| SDK | yes |
| SDK name | Python SDK + ROS 2 |
| ROS | yes |
| On-board compute | yes |
| Compute | Intel NUC 12 |
| Sensors | Head RGB-D camera, Gripper RGB-D camera, Navigation 2D laser, Microphone array, IMU |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

60 values from 2 documents, checked against maker sources on 2026-11-04.

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Footprint | 33 x 34 cm |  | [hello-stretch3.com](https://hello-stretch3.com/stretch-3-product) |
| Size (W x D x H) | 33 x 34 x 141 cm |  | [hello-stretch3.com](https://hello-stretch3.com/stretch-3-product) · product page |
| Height | 141 cm |  | [hello-stretch3.com](https://hello-stretch3.com/stretch-3-product) · product page |
| Weight | 24.5 kg |  | [hello-stretch3.com](https://hello-stretch3.com/stretch-3-product) · product page |
| Drive wheel diameter | 4 in | urethane rubber, shore 60A | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Base |
| Omni wheel (caster) diameter | 50 mm | passive omniwheel | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Base |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Payload (including gripper) | 2 kg |  | [hello-stretch3.com](https://hello-stretch3.com/stretch-3-product) · product page |
| Manipulator DoF | 7 | 2 DoF base, 1 lift, 1 telescoping arm, 3 wrist | [hello-stretch3.com](https://hello-stretch3.com/stretch-3-product) |
| Base drive | Two-wheel differential drive with passive omniwheel caster |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Base |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Runtime | 2 - 5 h | 5 h light CPU; 2 h high CPU | [hello-stretch3.com](https://hello-stretch3.com/stretch-3-product) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charge port rating | 12 V / 7 A charger |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Trunk |
| Charging dock | Optional charging dock; docking charge port on base |  | [hello-stretch3.com](https://hello-stretch3.com/stretch-3-product) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Head depth camera | Intel RealSense D435if (pan-tilt) |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Head |
| Head wide-angle RGB camera | Arducam B0385 + LK001 |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Head |
| Gripper depth camera | Intel RealSense D405 |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Gripper |
| LiDAR | RP-Lidar A1 laser range finder (navigation) |  | [hello-stretch3.com](https://hello-stretch3.com/stretch-3-product) |
| Microphone array | ReSpeaker Mic Array v2.0, 4 MEMS mics on 64.61 mm circle, 12 RGB LED ring |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Head |
| Base IMU | 9-DoF BNO085 |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Base IMU |
| Cliff sensors | 4 × Sharp GP2Y0A51SK0F, analog, range 2-15 cm |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Base |
| Wrist accelerometer | 3-axis ADXL343 (bump/tap detection) |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Wrist Accelerometer |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| On-board computer | Intel NUC 12 |  | [hello-stretch3.com](https://hello-stretch3.com/stretch-3-product) |
| SDK | Stretch Body Python SDK |  | [hello-stretch3.com](https://hello-stretch3.com/stretch-3-product) |
| ROS | ROS 2 (Nav2, Octomap integration) |  | [hello-stretch3.com](https://hello-stretch3.com/stretch-3-product) |
| Off-board GPU | Remote GPU via Wi-Fi or Ethernet; optional Wi-Fi access point |  | [hello-stretch3.com](https://hello-stretch3.com/stretch-3-product) |
| Wrist microcontroller | Atmel SAMD21G18A (Arduino Zero compatible) expansion header, 3V3 TTL (DIO, analog, SPI, I2C, UART) |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Wrist Expansion Header |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Wi-Fi | Wi-Fi 6E |  | [hello-stretch3.com](https://hello-stretch3.com/stretch-3-product) |
| Bluetooth | yes |  | [hello-stretch3.com](https://hello-stretch3.com/stretch-3-product) |
| Ethernet | Trunk Ethernet port to computer NIC |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Trunk |
| USB | Trunk 4-port USB 3.0 hub (powered 5 V); head USB 2.0-A 5 V@500 mA; shoulder USB 2.0-A; wrist USB 2.0-A 5 V@500 mA |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) |
| HDMI | Trunk HDMI to computer |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Trunk |
| Servo bus | Dynamixel X-Series TTL bus at wrist |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Dexterous Wrist |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Aux 12 V | Head and shoulder JST XHP-2 12 V@3 A fused; trunk 12 V access plug (unregulated battery voltage); wrist 12 V@500 mA |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) |
| Mount points | Base 6 × M4 inserts (max 7 mm depth); head 3 × M4; shoulder 4 × M4 (max 7 mm) |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) |
| Shoulder delivery tray | yes | with 40x40 mm ArUco tag | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Lift |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Arm reach | 0.52 m | telescoping arm, 5 aluminum links on rollers | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Arm |
| Recommended max arm payload | 2 kg |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Arm |
| Manipulator type | Cartesian: prismatic vertical lift + telescoping horizontal arm; stop-on-contact guarded behavior |  | [hello-stretch3.com](https://hello-stretch3.com/stretch-3-product) |
| Lift drive | Closed-loop stepper motor, low gear-ratio belt drive; lift brake (Stretch 3) | arm descends fully in ~2 min after power off | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Lift |
| Arm drive | Stepper motor, closed-loop control with current sensing (contact sensitivity) |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Arm |
| Wrist DoF | 3 (yaw, pitch, roll) — DexWrist 3 |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Dexterous Wrist |
| Wrist yaw range | +256 / -76 ° | Dynamixel XC430-W240-T | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Wrist Yaw |
| Wrist pitch range | +20 / -90 ° | Dynamixel XM540-W270-T | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Wrist Pitch |
| Wrist roll range | +172.5 / -172.5 ° | Dynamixel XM430-W350-T | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Wrist Roll |
| Gripper | Stretch Compliant Gripper (spring grasper), Dynamixel XL430-W250-T; power and pinch grasp; fingertip ArUco tags |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Gripper |
| Gripper weight | 240 g |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Gripper |
| Tool interface | Push-button quick-disconnect tool interface |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) |

### Actuation & Joints

| Spec | Value | Note | Source |
|---|---|---|---|
| Other DoF | 1 DoF gripper; 2 DoF head (pan/tilt) |  | [hello-stretch3.com](https://hello-stretch3.com/stretch-3-product) |
| Head pan range | 346 (-234 to 112) ° |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Pan Tilt |
| Head tilt range | 115 (-25 to 90) ° |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Pan Tilt |
| Head actuators | Dynamixel XL430-W250-T + XC430-W240-T |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Pan Tilt |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Runstop | Illuminated runstop button on head (pauses base, lift, arm) |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Runstop |
| Compliance | FCC Class A compliant (product page); hardware guide: exempt digital device per FCC 47 CFR 15.103(c), not certified as consumer device |  | [hello-stretch3.com](https://hello-stretch3.com/stretch-3-product) |
| Intended use | Research of mobile manipulation by experienced users; not for general consumer home use |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Disclaimer |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Teleoperation | Gamepad / web browser / dexterous teleop |  | [hello-stretch3.com](https://hello-stretch3.com/stretch-3-product) |
| Autonomy demos | Navigation (Nav2), FUNMAP, dynamic grasping, YOLOv8 reference code |  | [hello-stretch3.com](https://hello-stretch3.com/stretch-3-product) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Speakers | Head speakers with volume control |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Head |
| LEDs | Trunk LED light bar (battery voltage); ReSpeaker 12 RGB LED ring; illuminated power switch |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) |

### Transport & Storage

| Spec | Value | Note | Source |
|---|---|---|---|
| Transport | Roll by mast; two-person lift; original foam/cardboard packaging with head cage for shipping |  | [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md) · Transporting the Robot |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Price | 24,950 USD | list price | [hello-stretch3.com](https://hello-stretch3.com/stretch-3-product) |
| Included | Gripper, computer, sensors, software |  | [hello-stretch3.com](https://hello-stretch3.com/stretch-3-product) |

## Documents

- [Stretch 3 Hardware Guide (hello-robot/stretch_hardware_guides)](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md)
- [Stretch 3 product page](https://hello-stretch3.com/stretch-3-product)

## Sources

- Official page: [hello-stretch3.com](https://hello-stretch3.com/stretch-3-product)
- [github.com](https://github.com/hello-robot/stretch_hardware_guides/blob/master/docs/hardware_guide_stretch_3.md)
- [github.com](https://github.com/hello-robot/stretch_body)
- [github.com](https://github.com/hello-robot/stretch_ros2)
- [github.com](https://github.com/hello-robot/stretch_urdf)
- [github.com](https://github.com/hello-robot/stretch_mujoco)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-18). Source repository: https://github.com/htcrefactor/robot-catalog*
