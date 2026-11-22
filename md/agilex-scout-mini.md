# AgileX Robotics SCOUT MINI

> Compact 4WD hub-motor differential base for outdoor navigation research, sensor integration and mobile manipulation.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=agilex-scout-mini
- Category: Mobile platform
- Locomotion: Wheeled
- Manufacturer: AgileX Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 612 mm |
| Width | 580 mm |
| Height | 245 mm |
| Weight | 23 kg |
| Payload | 10 kg |
| Max speed | 1.5 m/s (5.4 km/h) |
| Wheels | 4 |
| Runtime | 1 h |
| Battery | 360 Wh |
| IP rating | IP22 |
| Status | Commercial |
| API | yes |
| SDK | yes |
| SDK name | AgileX UGV SDK (C++) + CAN protocol |
| ROS | yes |
| On-board compute | no |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

56 values from 2 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Manufacturer address | Head office: XbotPark, Songshan Lake, Dongguan, Guangdong, China; Sales: iPark, Nanshan District, Shenzhen |  | [global.agilex.ai](https://global.agilex.ai/products/scout-mini) |
| Wheel options | Standard off-road wheels; Mecanum wheels (lateral motion in Mecanum mode) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 / 3.3 |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 612 mm |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |
| Width | 580 mm |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |
| Height | 245 mm |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |
| Kerb weight | 23 kg |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |
| Axle track | 451 mm |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |
| Front/rear track (wheelbase) | 490 mm | listed as front/rear track | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |
| Ground clearance | 115 mm |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Max speed | 1.5 m/s |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |
| Max payload | 10 kg |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · Operation |
| Minimum turning radius | 0 mm |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |
| Steering | Four-wheel differential steering; independent four-wheel drive |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |
| Drive motors | DC brushless hub motors, 4 × 250 W (Mecanum wheel version 150 W) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |
| Drive motor reduction ratio | 1:4.3 |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |
| Drive motor sensor | Hall |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |
| Linear speed command range | ±1500 mm/s | CAN motion command | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 3.3 |
| Angular speed command range | ±2.523 rad/s | CAN command range ±2523 × 0.001 rad/s | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 3.3 |
| Lateral speed command range | ±3000 mm/s | Mecanum mode only | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 3.3 |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Max gradeability | 15 ° | user manual | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |
| Climb (full load) | 20 ° | product page; text also cites up to 22° | [global.agilex.ai](https://global.agilex.ai/products/scout-mini) |
| Obstacle clearance | 40 mm |  | [global.agilex.ai](https://global.agilex.ai/products/scout-mini) |
| Suspension | Independent suspension with rocker arm; filled solid tires |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 / 2 |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery type | Lithium battery |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |
| Battery voltage | 24 V |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |
| Battery capacity | 15 Ah |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |
| Full-charge voltage | 29.2 V |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 3.2 |
| Maximum endurance | 3 h | user manual | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |
| Runtime (full load) | 1 h | product page | [global.agilex.ai](https://global.agilex.ai/products/scout-mini) |
| Maximum travel | 35 km | user manual | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |
| Max range (full load) | 8 km | product page | [global.agilex.ai](https://global.agilex.ai/products/scout-mini) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charging time | 2 h | manual table; text: ~1.5 h from 22 V with 10 A charger | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 / 3.2 |
| Charger current | 10 A |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 3.2 |
| Charger input | AC 220 V |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.1 |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| IP rating | IP22 | custom IP protection available | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |
| Working temperature | -10 to 40 °C | safety section states -10 to 45 °C | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |
| Relative humidity | 30 to 80 % |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) |
| Max altitude | 1,000 m | recommended | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) |
| Max day/night temperature difference | 25 °C |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) |
| Battery storage temperature | -10 to 45 °C |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) |
| Charging temperature | above 0 °C |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| SDK | AgileX UGV SDK + CAN protocol |  | [global.agilex.ai](https://global.agilex.ai/products/scout-mini) |
| ROS | ROS 1 / ROS 2 driver support |  | [global.agilex.ai](https://global.agilex.ai/products/scout-mini) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Communication interface | CAN (USB-to-CAN adapter included) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |
| Rear panel | Aviation extension interface (power + CAN), voltage display module, power switch, charging interface |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 2.2 |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Extension power limit | ≤5 A, ≤120 W |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · Precautions for electrical external extension |
| Top mounting | Standard aluminum extension support on top |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 2 |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Obstacle avoidance | no | no automatic obstacle avoidance sensor | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) |
| Anti-collision | Front anti-collision fence |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 2 |
| Parking type | Servo brake / anti-collision tube |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Control modes | Remote control mode; command control mode |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |
| RC transmitter | FS 2.4 GHz, limit distance 100 m |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |
| RC range | 100 m |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.2 |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Lights | White front width light (RC/command switchable, brightness 0-100); ring power indicator |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 2.1 |
| Display | Tail power display (battery capacity and voltage) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 2.1 |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Product list | Robot body, AC 220 V charger, 4-pin aviation male plug, USB-to-CAN, RC transmitter |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734) · 1.1 |

## Documents

- [SCOUT MINI User Manual (AgileX)](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734)
- [SCOUT MINI product page (AgileX global)](https://global.agilex.ai/products/scout-mini)

## Sources

- Official page: [global.agilex.ai](https://global.agilex.ai/products/scout-mini)
- [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_MINI_USER_MANUAL_AgileX.pdf?v=1792636734)
- [github.com](https://github.com/agilexrobotics/ugv_sdk)
- [github.com](https://github.com/agilexrobotics/pyagxrobots)
- [github.com](https://github.com/agilexrobotics/scout_ros)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-22). Source repository: https://github.com/htcrefactor/robot-catalog*
