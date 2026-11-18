# AgileX Robotics TRACER 2.0

> Low-profile two-wheel-differential indoor base (54–56 kg) for AGV/AMR material transport and line-side delivery development.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=agilex-tracer-2-0
- Category: Mobile platform
- Locomotion: Wheeled
- Manufacturer: AgileX Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 702 mm |
| Width | 610 mm |
| Height | 169 mm |
| Weight | 55 kg |
| Payload | 150 kg |
| Max speed | 2 m/s (7.2 km/h) |
| Runtime | 3.5 h |
| IP rating | IP22 |
| Status | Commercial |
| API | yes |
| SDK | yes |
| SDK name | AgileX UGV SDK (C++) + CAN protocol |
| ROS | yes |
| On-board compute | no |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

54 values from 2 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Manual version / firmware | Manual V1.0.0 (2025-03-20), firmware V1.0.2 |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) |
| Manufacturer address | Head office: XbotPark, Songshan Lake, Dongguan, Guangdong, China; Sales: iPark, Nanshan District, Shenzhen |  | [global.agilex.ai](https://global.agilex.ai/products/tracer-2-0-150kg-payload-indoor-mobile-robot) |
| Battery options | 24 V 30 Ah (standard); 24 V 60 Ah (optional) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 702 mm |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |
| Width | 585 mm | user manual; product page lists 610 mm | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |
| Width | 610 mm | product page | [global.agilex.ai](https://global.agilex.ai/products/tracer-2-0-150kg-payload-indoor-mobile-robot) |
| Height | 169 mm |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |
| Total weight | 54 - 56 kg |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |
| Wheelbase | 517.4 mm |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |
| Ground clearance | 27 mm |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Max speed | 2 m/s | high-speed mode; low-speed mode max 1.5 m/s | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 / 2.3 |
| Max payload | 150 kg | rated moving payload | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · Operation |
| Minimum turning radius | Can turn in place |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |
| Steering | Two-wheel differential steering |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |
| Drive motors | DC brushless hub motors, 2 × 400 W |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |
| Drive motor sensor | Magnetic encoder 2500 |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |
| Push assist mode | yes | motor assists manual pushing (RC SWA down) | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 2.3 |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Max gradeability | 8 ° |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |
| Obstacle clearance | 10 mm |  | [global.agilex.ai](https://global.agilex.ai/products/tracer-2-0-150kg-payload-indoor-mobile-robot) |
| Suspension | Swing-arm non-independent suspension (upgraded three-swing-arm structure) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |
| Operating surface | Flat indoor ground |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 2 |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery type | Lithium iron phosphate |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |
| Battery voltage | 24 V |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |
| Battery capacity | 30 Ah | optional 60 Ah | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |
| Maximum battery life | 9 h | user manual | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |
| Runtime (full load) | 3.5 h | product page | [global.agilex.ai](https://global.agilex.ai/products/tracer-2-0-150kg-payload-indoor-mobile-robot) |
| Maximum distance | 80 km | user manual | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |
| Max range | 25 km | product page | [global.agilex.ai](https://global.agilex.ai/products/tracer-2-0-150kg-payload-indoor-mobile-robot) |
| Charge threshold | charge when voltage below 22.5 V |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · Operation |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charging time | 3 h |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |
| Charger current | 10 A |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 3.2 |
| Charger input | AC 220 V |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.1 |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| IP rating | IP22 |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |
| Working temperature | -10 to 40 °C | safety section: -10 to 45 °C outdoors | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |
| Relative humidity | 30 to 80 % |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) |
| Recommended max altitude | 1,000 m |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) |
| Max day/night temperature difference | 25 °C |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) |
| Battery storage temperature | -10 to 45 °C |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) |
| Charging temperature | above 0 °C |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| ROS | TRACER 2.0 ROS package |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 3.5 |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| System interface | CAN (USB-to-CAN module included) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |
| Rear interface | Charging port; CAN + 24 V aviation expansion interface; E-stop |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 2.2 |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Tail extension power | 24 V, ≤5 A, ≤120 W |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · Electrical/extension cords |
| Top compartment | Bayonet open compartment reserved on top |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 2 |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Emergency stop | E-stop switch at rear |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 2 |
| Parking mode | Servo brake / safety contact strip |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |
| Safety contact strip | yes |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |
| Obstacle avoidance | no | no automatic obstacle avoidance sensor | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Control modes | Remote control; command (CAN/navigation) control; low/high speed modes |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 / 2.3 |
| RC transmitter | FS 2.4 GHz, up to 100 m (optional) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |
| RC range | 100 m |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.2 |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Lights | White front light (breathing/constant/off); power-level indicator ring on switch |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 2 / 2.1 |
| Voltmeter | Rear voltmeter |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Component list | Robot body, AC 220 V charger, RC transmitter (optional), 4-pin aviation plug, USB-to-CAN module |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905) · 1.1 |

## Documents

- [TRACER 2.0 User Manual V1.0.0 (2025-03)](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/TRACER_2.0_User_Manual_AgileX.pdf?v=1792611905)
- [TRACER 2.0 product page (AgileX global)](https://global.agilex.ai/products/tracer-2-0-150kg-payload-indoor-mobile-robot)

## Sources

- Official page: [global.agilex.ai](https://global.agilex.ai/products/tracer-2-0-150kg-payload-indoor-mobile-robot)
- [github.com](https://github.com/agilexrobotics/ugv_sdk)
- [github.com](https://github.com/agilexrobotics/tracer_ros2)
- [github.com](https://github.com/agilexrobotics/pyagxrobots)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-18). Source repository: https://github.com/htcrefactor/robot-catalog*
