# AgileX Robotics BUNKER PRO 2.0

> Heavy-duty IP67 tracked chassis for industrial inspection, emergency response and material transport over rugged terrain.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=agilex-bunker-pro-2-0
- Category: Mobile platform
- Locomotion: Tracked
- Manufacturer: AgileX Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 1,080 mm |
| Width | 785 mm |
| Height | 470 mm |
| Weight | 225 kg |
| Payload | 120 kg |
| Max speed | 1.5 m/s (5.4 km/h) |
| Runtime | 2.5 h |
| IP rating | IP67 |
| Status | Commercial |
| API | yes |
| SDK | yes |
| SDK name | AgileX UGV SDK (C++) + CAN protocol |
| ROS | yes |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

55 values from 2 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Manual version | V1.0.0 (2025-05) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) |
| Manufacturer address | Head office: XbotPark, Songshan Lake, Dongguan, Guangdong, China; Sales: iPark, Nanshan District, Shenzhen |  | [global.agilex.ai](https://global.agilex.ai/products/bunker-pro) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 1,080 mm |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| Width | 785 mm |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| Height | 470 mm |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| Curb weight | 225 kg |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| Wheelbase | 575 mm |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| Track width | 150 mm | listed as Track Width (track belt) | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| Ground clearance | 120 mm | maximum | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Max loaded speed | 1.5 m/s |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| Max payload | 120 kg | rated moving payload | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · Operation |
| Minimum turning radius | Can turn in place |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| Steering | Track-type differential steering |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| Drive motors | 2 × 1800 W brushless servo motors |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| Drive motor gear ratio | 1:7.5 |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| Drive motor sensor | 2500 PPR optical incremental encoder |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Max climbing ability (unloaded) | 30 ° | capable of stair climbing | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| Climb (full load) | 25 ° |  | [global.agilex.ai](https://global.agilex.ai/products/bunker-pro) |
| Stair climbing | yes |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| Max obstacle crossing | 180 mm | user manual | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| Obstacle clearance (full load) | 150 mm | product page | [global.agilex.ai](https://global.agilex.ai/products/bunker-pro) |
| Suspension | Christie suspension & Matilda four-wheel balanced suspension |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery type | Lithium iron phosphate (LiFePO4) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| Battery voltage | 72 V |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| Battery capacity | 50 Ah |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| Normal battery voltage range | 60 - 80 V | may not operate below 55 V | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 3.1 |
| Rated endurance (fully loaded, concrete) | 2.5 h |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| Rated endurance (unloaded, concrete) | 3.5 h |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| Max distance (full load) | 15 km |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| Max distance (unloaded) | 20 km |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charging time | 2.5 h |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| Charger input | AC 220 V |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 0.1 |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| IP rating | IP67 |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| Working temperature | -20 to 60 °C |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| Relative humidity | 30 to 80 % |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · Environmental Usage Guidelines |
| Recommended max altitude | 1,000 m |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) |
| Max daily temperature variation | 25 °C | recommended | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) |
| Battery storage temperature | -10 to 45 °C |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · Battery Precautions |
| Charging temperature | above 0 °C |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| ROS | BUNKER ROS package (ugv_sdk based) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 3.5 |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| System interface | CAN (USB-to-CAN module included); RS232 also mentioned for customization |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 / 1.3 |
| Rear panel | Q1 aviation connector (CAN + 60-80 V power), power switch, charging port, antenna, E-stop, status light |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 2.1 |
| Motion feedback cycle | 20 ms | frame 0x221; system status 0x211 at 200 ms | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 3.3 |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Rear expansion power | 60-80 V, max 20 A, ≤1440 W |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 2.1 / Electrical Extension Guidelines |
| Top mounting | Standard aluminum profile rails with T-slot nuts |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 3.1 |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Emergency stop | E-stop switch on rear panel |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 2.1 |
| Braking distance | 0.7 m | unloaded, friction coefficient 0.5 | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| Obstacle avoidance | no | no automatic obstacle avoidance sensors | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Control modes | Remote control; command control (CAN) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| RC transmitter | FS 2.4 GHz, up to 200 m (optional) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |
| RC range | 200 m |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 1.2 |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Status indicator | Green >50%, yellow 25-50%, red 10-25%, slow blink <10%, fast blink fault |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 2.1 |
| Display | Rear voltage display panel |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) |

### Transport & Storage

| Spec | Value | Note | Source |
|---|---|---|---|
| Track tensioning interval | 150-200 h | bolt check after 500 h | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · Maintenance |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Product list | Robot body, AC 220 V charger, 4-pin aviation plug, USB-to-CAN module, FS remote (optional) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826) · 0.1 |

## Documents

- [BUNKER PRO 2.0 User Manual V1.0.0 (2025-05)](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/BUNKER_PRO2_USER_MANUAL_77a0e492-f6ac-40d2-8267-685e6cc76887.pdf?v=1792571826)
- [BUNKER PRO 2.0 product page (AgileX global)](https://global.agilex.ai/products/bunker-pro)

## Sources

- Official page: [global.agilex.ai](https://global.agilex.ai/products/bunker-pro)
- [github.com](https://github.com/agilexrobotics/ugv_sdk)
- [github.com](https://github.com/agilexrobotics/bunker_ros2)
- [github.com](https://github.com/agilexrobotics/pyagxrobots)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-20). Source repository: https://github.com/htcrefactor/robot-catalog*
