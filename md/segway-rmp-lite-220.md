# Segway Robotics (Segway-Ninebot) RMP Lite 220

> IP65 differential hub-motor chassis for indoor/outdoor delivery, patrol and AGV builds; base of NVIDIA's Carter reference robot.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=segway-rmp-lite-220
- Category: Mobile platform
- Locomotion: Wheeled
- Manufacturer: Segway Robotics (Segway-Ninebot) (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 730 mm |
| Width | 499 mm |
| Height | 280 mm |
| Weight | 33 kg |
| Payload | 50 kg |
| Max speed | 3 m/s (10.8 km/h) |
| Wheel diameter | 280 mm |
| Runtime | 10 h |
| Battery | 1,152 Wh |
| IP rating | IP65 |
| Status | Commercial |
| API | yes |
| SDK | yes |
| SDK name | Segway RMP SDK (C/C++, ROS; UART/CAN) |
| ROS | yes |
| Sensors | IMU, Wheel encoders |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

74 values from 4 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Manufacturer | Segway-Ninebot (Segway Robotics) |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · cover |
| Robot type | Mobile robot chassis (Robot Mobile Platform) for indoor/outdoor distribution, inspection, service, cleaning and warehousing AGV |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · General Information |
| Manual version | RMP Lite 220 User Manual v1.0 (©2021) |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) |
| US address (Segway Robotics) | 98 Spit Brook STE 2203, Nashua, NH 03062 |  | [robotics.segway.com](https://robotics.segway.com/for-developers/) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 730 mm |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Width | 499 mm | spec sheet | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Width | 500 mm | user manual Appendix I | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · Appendix I Table 1 |
| Height | 280 mm |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Axle base / wheelbase | 513.5 mm |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Wheelbase (track) | 413 mm | spec sheet labels this "Wheelbase" | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Tread | 414 mm | user manual Appendix I | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · Appendix I Table 1 |
| Ground clearance | 69 mm | spec sheet | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Ground clearance | 68 mm | user manual Appendix I | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · Appendix I Table 1 |
| Tire size | 280 mm | 11 in hub-motor wheel | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Tire size | 11 in (280 mm) hub motor |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Weight | 33 kg | spec sheet | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Weight (with battery) | 27.2 kg | user manual Appendix I (differs from 33 kg on spec sheet) | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · Appendix I Table 1 |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Standard / nominal load | 50 kg |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Max speed | 3 m/s |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Max steering speed | 3 rad/s |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Minimum turning radius | 0 m |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Drive | FWD, differential steering | manual: front drive, differential steering | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Drive motors | Hub motors (11 in) |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Driving wheels | 11 in high-adhesion pneumatic tire with drainage grooves, good shock absorption |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · §1.2 Table 1 |
| Universal (caster) wheel | Super artificial rubber, lightweight, shock absorbing |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · §1.2 Table 1 |
| Braking acceleration | 0.5 g |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Obstacle crossing | 5 cm | spec sheet "Obstacle Avoidance 5cm/8°/Speed bump" | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Obstacle surmounting | 4 cm | user manual Appendix I | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · Appendix I Table 1 |
| Slope | 8 ° |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Traversable features | Speed bumps / deceleration zones; indoor and outdoor |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Suspension travel | 4 mm (rear) | manual lists "4mm rear overhang" | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery capacity | 1,152 Wh |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Battery voltage | 48 V |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Battery capacity | 20 / 24 Ah | spec sheet lists 48V 20Ah/24Ah | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Battery | 24 Ah | user manual: 48V 24Ah | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · Appendix I Table 1 |
| Range | 80 km | at max load, 3 m/s (as published) | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Runtime | 10 h | "10 hours of non-stop service" | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Swappable battery | yes | quick battery change; battery lock with matching key | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charging | Manual charging; swappable battery; provided with automatic charging interface |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Charging method | Manual line charging / quick battery change | user manual; only the supplied charger may be used | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · Appendix I Table 1 |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| IP rating | IP65 | spec sheet | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Protection level | IPX5 | user manual Appendix I | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · Appendix I Table 1 |
| Environment | Indoor and outdoor |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| IMU | Integrated IMU (gyroscope + accelerometer); frame XYZ = right/front/up |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · §2.2.1 Table 4 |
| Feedback data | Encoder, Hall, IMU | manual: magnetic encoder, Hall, IMU | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery & chassis telemetry | SoC (%), charging status, voltage (mV), current (mA), temperature (°C) readable via API |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · §2.2.1 Table 6 |
| SDK | C/C++ dynamic libraries (libctrl_x86_64.so, libctrl_arm64-v8a.so) + header Comm_ctrl_navigation.h; ROS package | host platforms x86_64 and arm64 | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · §2.1 Table 3 |
| Supported API | C/C++, ROS |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| ROS | ROS node "SmartCar" (segwayrmp, segway_msgs packages); ROS support package on GitHub |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · §1.3.4, §2.2.2 |
| Compatible software | ROS and NVIDIA Isaac |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| 3D model | Gazebo, Rviz models with tutorial cases |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| API functions | Speed command (set_cmd_vel, m/s & rad/s), forward/backward/angular speed limits, load state, hang mode, power-off, error codes, battery, mileage, firmware versions, IAP |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · §2.2.1 Table 6 |
| Firmware update | IAP online upgrade of central control board and motor board from the upper computer over serial or CAN |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · §3 |
| Isaac feature pack | RMP Lite ISAAC Feature Pack (data interface between chassis and upper computer) |  | [robotics.segway.com](https://robotics.segway.com/for-developers/) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Interface | UART, CAN |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Connectors | 8-pin (CANH, CANL, TX, RX, GND, 5V, GND, S.B PPM remote receiver) AWG26; 2-pin upper-system power (Power+/Power−) AWG16 |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · Appendix III |
| ROS feedback rate | 40 Hz | Speed_fb, Ticks_fb, Odom, Imu topics; battery/mode/error topics 1 Hz | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · §2.2.2 Table 7 |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Host computer power | 48 V, 400 W |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Host computer supply voltage | 48 V DC |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Upper computer power supply ports | Two upper-computer power supply ports; one rated max 10 A |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · §1.2 Table 1 items 10, 12 |
| Mounting holes | Mounting holes to install upper equipment |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · §1.2 Table 1 item 5 |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Applications | Indoor/outdoor delivery, patrolling, service, cleaning (disinfecting), AGV (warehouse), special application robots |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Braking distance | 0.9 m | no load, from 3 m/s (spec sheet) | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Braking distance | 0.95 m | no load, from 3 m/s (user manual Appendix I) | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · Appendix I Table 1 |
| Braking method | Electronic brake |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Emergency stop | E-stop button on chassis; e-stop switch on remote control |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · §1.2, §1.3.3 |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Control | Remote control, host (upper) computer control |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Remote control | T8FB transmitter with paired receiver (PPM); max linear/angular velocity knobs, enable and e-stop switches |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · §1.3 |
| Chassis modes | Locked, Control, Push, Emergency stop, Error | load >20 kg: switch to full-load (overload) control parameters via set_chassis_load_state | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · Appendix I Table 2 |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Buttons | Emergency stop button, push-to-move button, power button |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Status indication | Power on/off indicator, platform base status, control source indication, battery level, charging status |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Buzzer | Beep on boot / shutdown prompts |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf) · §1.2 Table 1 |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Extension kit | Light strip, ultrasonic sensor, bumper, infrared sensor, sensor mounting rod |  | [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf) |
| Availability | Listed on Segway Robotics RMP product page (request demo / more information) |  | [robotics.segway.com](https://robotics.segway.com/rmp/) |

## Documents

- [Segway RMP Lite 220 Specifications (Segway Robotics PDF)](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf)
- [Segway RMP Lite 220 User Manual v1.0 (Segway-Ninebot, 54 pp.)](https://robotics.segway.com/wp-content/uploads/2023/10/RMP220-User-Manual-v1.0.pdf)
- [Segway Robotics RMP product page](https://robotics.segway.com/rmp/)
- [Segway Robotics For Developers page](https://robotics.segway.com/for-developers/)

## Sources

- Official page: [robotics.segway.com](https://robotics.segway.com/rmp)
- [robotics.segway.com](https://robotics.segway.com/wp-content/uploads/2021/04/Segway-RMP-220Lite-Specs.pdf)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-19). Source repository: https://github.com/htcrefactor/robot-catalog*
