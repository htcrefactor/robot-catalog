# AgileX Robotics RANGER MINI 3.0

> Four-wheel-drive, four-wheel-steer omnidirectional base for delivery, logistics and indoor-outdoor AMR development.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=agilex-ranger-mini-3-0
- Category: Mobile platform
- Locomotion: Wheeled
- Manufacturer: AgileX Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 720 mm |
| Width | 500 mm |
| Height | 345 mm |
| Weight | 73 kg |
| Payload | 120 kg |
| Max speed | 2 m/s (7.2 km/h) |
| Wheels | 4 |
| Runtime | 3 h |
| Battery | 1,152 Wh |
| IP rating | IP54 |
| Status | Commercial |
| API | yes |
| SDK | yes |
| SDK name | AgileX UGV SDK (C++) + CAN protocol |
| ROS | yes |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

60 values from 2 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Manual version | V1.0.1 (2024-10-09) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) |
| Manufacturer address | Head office: XbotPark, Songshan Lake, Dongguan, Guangdong, China; Sales: iPark, Nanshan District, Shenzhen |  | [global.agilex.ai](https://global.agilex.ai/products/ranger-mini-3) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 720 mm |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| Width | 500 mm |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| Height | 345 mm |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| Total weight | 75 kg | user manual | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| Weight | 73 kg | product page | [global.agilex.ai](https://global.agilex.ai/products/ranger-mini-3) |
| Axle track | 494 mm |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| Front/rear track (wheelbase) | 370 mm | listed as front/rear track | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| Ground clearance | 105 mm |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Max speed | 7.2 km/h |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| Max speed | 2 m/s | product page | [global.agilex.ai](https://global.agilex.ai/products/ranger-mini-3) |
| Max payload | 120 kg |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · Operation Precautions |
| Minimum turning radius | 0 mm (spin mode); 810 mm (Ackermann mode) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| Steering | 4-wheel drive, 4-wheel steering |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| Motion modes | Front-and-rear Ackermann; spin (in place); oblique/lateral (steering up to 90°); parking (X-lock) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 2.3 |
| Drive motors | 4 × 350 W hub motors |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| Steering motors | 4 × 100 W, reduction 1:51, dual encoder |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| Drive motor reduction ratio | 1:4.428 |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| Drive motor sensor | Encoder |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| Linear speed command range | ±2000 mm/s | ±1000 mm/s when steering angle >20° | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 3.2 |
| Spin speed command range | ±3.259 rad/s | ±3259 × 0.001 rad/s | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 3.2 |
| Max steering angle | ±0.698 rad (Ackermann); ±1.571 rad (oblique) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 3.2 |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Max climbing ability | 15 ° | with 25 kg load (user manual) | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| Climb | 20 ° | product page | [global.agilex.ai](https://global.agilex.ai/products/ranger-mini-3) |
| Crossing width | 120 mm |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| Obstacle clearance | 75 mm |  | [global.agilex.ai](https://global.agilex.ai/products/ranger-mini-3) |
| Suspension | Independent suspension; solid tires with swing arms |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 / 2 |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery type | Lithium iron phosphate |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| Battery voltage | 48 V |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| Battery capacity | 24 Ah |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| Normal battery voltage range | 45 - 54 V |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 3.1 |
| Battery quick-swap | yes | battery panel on right side | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 3.1 |
| Maximum endurance | 7 h | user manual | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| Runtime (full load) | 3 h | product page | [global.agilex.ai](https://global.agilex.ai/products/ranger-mini-3) |
| Maximum travel | 35 km | user manual | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| Max range (full load) | 15 km | product page | [global.agilex.ai](https://global.agilex.ai/products/ranger-mini-3) |
| Low battery behaviour | <15% SOC lights flash; <10% cuts external and drive power |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 2.1 |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charging time | 1.5 h |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| Charger current | 10 A |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 3.1 |
| Charger input | AC 220 V |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.1 |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| IP rating | IP54 |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| Working temperature | -10 to 40 °C |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| Battery storage temperature | -10 to 40 °C |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · Battery |
| Charging temperature | above 0 °C |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) |
| Recommended max altitude | 1,000 m |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) |
| Max day/night temperature difference | 25 °C |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| ROS | RANGER MINI 3.0 ROS package |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 3.3 |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Communication interface | CAN (USB-to-CAN module included) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| Rear expansion connector | Circular 4-pin connector: power (42-54.6 V, ≤15 A) + CAN |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 2.2 |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Tail extension power | 42-54.6 V, ≤15 A, ≤720 W |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 2.2 / Precautions |
| Top mounting | Standard aluminum extension bracket |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 2 |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Emergency stop | Emergency stop button |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · Safety |
| Parking type | Electronic brake |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| Obstacle avoidance | no | no automatic obstacle avoidance sensors | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Control modes | Remote control; command control (CAN) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| RC transmitter | FS 2.4 GHz, limit distance 100 m (optional) |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |
| RC range | 100 m |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.2 |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Lights | Front and rear lights (flash at low battery); RC switchable |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Product list | Body, AC 220 V charger, 4-pin aviation plug, FS remote (optional), USB-to-CAN module |  | [cdn.shopify.com](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920) · 1.1 |

## Documents

- [RANGER MINI 3.0 User Manual V1.0.1 (2024-10)](https://cdn.shopify.com/s/files/1/0551/0630/6141/files/RANGER_MINI_3.0_USER_MANUAL_56669f58-ac26-4984-8aed-4ab40f7b6c74.pdf?v=1792566920)
- [RANGER MINI 3.0 product page (AgileX global)](https://global.agilex.ai/products/ranger-mini-3)

## Sources

- Official page: [global.agilex.ai](https://global.agilex.ai/products/ranger-mini-3)
- [agilex.ai](https://www.agilex.ai/products/ranger-mini)
- [github.com](https://github.com/agilexrobotics/ugv_sdk)
- [github.com](https://github.com/agilexrobotics/ranger_ros2)
- [github.com](https://github.com/agilexrobotics/pyagxrobots)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-26). Source repository: https://github.com/htcrefactor/robot-catalog*
