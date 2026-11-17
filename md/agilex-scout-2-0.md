# AgileX Robotics SCOUT 2.0

> Heavy-duty four-wheel-differential off-road UGV chassis for outdoor patrol, inspection, agriculture and field research builds.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=agilex-scout-2-0
- Category: Mobile platform
- Locomotion: Wheeled
- Manufacturer: AgileX Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 930 mm |
| Width | 699 mm |
| Height | 337 mm |
| Weight | 67 kg |
| Payload | 50 kg |
| Max speed | 1.67 m/s (6.0 km/h) |
| Wheels | 4 |
| Runtime | 2.5 h |
| Battery | 720 Wh |
| IP rating | IP22 |
| Status | Commercial |
| API | yes |
| SDK | yes |
| SDK name | AgileX UGV SDK (C++) + CAN protocol |
| ROS | yes |
| On-board compute | no |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

66 values from 2 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Manual version | V2.0.4 (2023-12-10) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · Document version |
| Manufacturer address | Head office: XbotPark, Songshan Lake, Dongguan, Guangdong, China; Sales: iPark, Nanshan District, Shenzhen |  | [global.agilex.ai](https://global.agilex.ai/products/scout-2-0) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 930 mm |  | [global.agilex.ai](https://global.agilex.ai/products/scout-2-0) · Technical Specifications |
| Width | 699 mm |  | [global.agilex.ai](https://global.agilex.ai/products/scout-2-0) |
| Height | 337 mm | product page; manual lists 349 mm | [global.agilex.ai](https://global.agilex.ai/products/scout-2-0) |
| Height | 349 mm | user manual L×W×H 930 × 699 × 349 | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 1.2 |
| Weight | 67 kg | chassis body 67±1 kg | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 1.2 |
| Wheelbase | 498 mm |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 1.2 |
| Front/rear wheel track | 583 mm | listed as front/rear wheel base | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 1.2 |
| Ground clearance | 115 mm | product page | [global.agilex.ai](https://global.agilex.ai/products/scout-2-0) |
| Ground clearance | 135 mm | user manual | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 1.2 |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Max speed | 1.67 m/s |  | [global.agilex.ai](https://global.agilex.ai/products/scout-2-0) |
| Max speed | 1.5 km/h | as printed in user manual table (unit as stated) | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 1.2 |
| Max payload | 50 kg |  | [global.agilex.ai](https://global.agilex.ai/products/scout-2-0) |
| Minimum turning radius | Can turn in place |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 1.2 |
| Steering | Four-wheel differential steering |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 1.2 |
| Drive motors | DC brushless, 4 × 400 W |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 1.2 |
| Drive motor reduction ratio | 1:40 |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 1.2 |
| Drive motor sensor | Magnetic encoder 2500 (lines) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 1.2 |
| Linear speed command range | ±1500 mm/s | CAN motion command effective value | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 3.3.3 |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Max climb | 30 ° |  | [global.agilex.ai](https://global.agilex.ai/products/scout-2-0) |
| Obstacle clearance | 110 mm |  | [global.agilex.ai](https://global.agilex.ai/products/scout-2-0) · Technical Specifications |
| Gap crossing | 200 mm |  | [global.agilex.ai](https://global.agilex.ai/products/scout-2-0) |
| Suspension | Front and rear double-rocker (double-wishbone) independent suspension |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 1.2 |
| Tire pressure | 1.8 - 2.0 bar | inflatable rubber tyres | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · Maintenance |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery type | Lithium battery (ternary; LiFePO4 version also referenced) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 1.2 / 3.2.1 |
| Battery voltage | 24 V |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 1.2 |
| Battery capacity | 30 Ah |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 1.2 |
| Full-charge voltage | 29.2 V | ternary lithium; 26.8 V for LiFePO4 | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 3.2.1 |
| Battery replaceable | yes | detachable battery (8 bottom screws, XT60) | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 3.2.2 |
| Runtime (full load) | 2.5 h |  | [global.agilex.ai](https://global.agilex.ai/products/scout-2-0) |
| Maximum battery life | 8 h |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 1.2 |
| Max range | 15 km |  | [global.agilex.ai](https://global.agilex.ai/products/scout-2-0) |
| Low battery alarm | <15% or <24 V beeper alarm; <10% or <23 V cuts drive and extension power |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 2.1 |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charging time | 3 h | from 22 V with 10 A charger | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 1.2 / 3.2.1 |
| Charger current | 10 A |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 3.2 |
| Charger input | AC 220 V |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 1.1 |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| IP rating | IP22 | customizable | [global.agilex.ai](https://global.agilex.ai/products/scout-2-0) |
| Operating temperature | -10 to 40 °C | manual safety section also states -10 to 45 °C | [global.agilex.ai](https://global.agilex.ai/products/scout-2-0) |
| Relative humidity | 30 to 80 % |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · Operational environment |
| Max altitude | 1,000 m | recommended | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · Operational environment |
| Max day/night temperature difference | 25 °C | recommended | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · Operational environment |
| Battery storage temperature | -10 to 45 °C |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · Attention / Battery |
| Charging temperature | above 0 °C |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) |
| Rain | Not waterproof (standard version); avoid rain, snow, standing water |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| SDK | ugv_sdk (C++) | github.com/agilexrobotics/ugv_sdk | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 3.6 |
| ROS | ROS 1 / ROS 2 integration (scout_ros package) |  | [global.agilex.ai](https://global.agilex.ai/products/scout-2-0) |
| Simulation | Gazebo |  | [global.agilex.ai](https://global.agilex.ai/products/scout-2-0) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| CAN bus | CAN, 500 kbit/s; USB-to-CAN module included |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 3.7 |
| External connectors | Top: three 4-pin aviation connectors + one DB9 (RS232); rear: CAN + 24 V aviation interface, DB9 | RS232 support instructions removed in V2.0.3 | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 2.2 |
| Command timeout | 500 ms | stops if no control frame received | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 4 Q&A |
| Status feedback cycle | 20 ms | system status frame 0x211 | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 3.3.3 |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Top extension power | 24 V, ≤10 A, ≤240 W |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · Electrical/extension cords |
| Rear extension power | ≤10 A, ≤240 W; combined top+rear ≤300 W |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) |
| Top compartment | Bayonet open compartment reserved on top; interfaces for LiDAR, RTK/INS, arms, charging docks |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Emergency stop | E-stop buttons on both sides |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 2 |
| Obstacle avoidance | no | no automatic obstacle avoidance sensor fitted | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) |
| Anti-collision | Anti-collision beams around body |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 2 |
| Parking mode | Servo brake / anti-collision tube |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 1.2 |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Control modes | Remote control; CAN command control |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 1.2 |
| RC transmitter | FS RC transmitter, 2.4 GHz, up to 100 m (optional) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 1.2 / 2.3 |
| RC range | 100 m |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 1.2 |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Lights | White front light, red rear light; 3 modes (normally closed/open, breathing) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 2.5 |
| Beeper | Low-battery alarm beeper |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 2.1 |
| Voltmeter | Rear voltmeter, 1 V accuracy |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 2.1 |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Component list | Robot body, AC 220 V charger, 4-pin aviation plug (male), USB-to-CAN module, RC transmitter (optional) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361) · 1.1 |

## Documents

- [SCOUT 2.0 User Manual V2.0.4 (2023.12)](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361)
- [SCOUT 2.0 product page (AgileX global)](https://global.agilex.ai/products/scout-2-0)

## Sources

- Official page: [global.agilex.ai](https://global.agilex.ai/products/scout-2-0)
- [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/SCOUT_2.0_USER_MANUAL.pdf?v=1787960361)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-17). Source repository: https://github.com/htcrefactor/robot-catalog*
