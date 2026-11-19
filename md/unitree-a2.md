# Unitree Robotics A2

> Mid-size industrial quadruped with hot-swappable dual batteries for inspection, logistics and rescue.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=unitree-a2
- Category: Quadruped
- Locomotion: Legged
- Manufacturer: Unitree Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 820 mm |
| Width | 440 mm |
| Height | 570 mm |
| Weight | 42 kg |
| Payload | 25 kg |
| Max speed | 3.7 m/s (13.3 km/h) |
| Degrees of freedom | 12 |
| Runtime | 3 h |
| Battery | 907.2 Wh |
| IP rating | IP56 |
| Status | Commercial |
| Price | contact sales |
| SDK | yes |
| On-board compute | yes |
| Compute | 8-core CPU (platform) + Intel Core i7 (user development); optional compute expansion dock |
| Sensors | LiDAR, HD camera, Microphone array |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

67 values from 1 document, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Manufacturer | Unitree Robotics (Hangzhou Yushu Technology Co., Ltd.) |  | [unitree.com](https://www.unitree.com/A2) |
| Variants | A2 (contact sales); A2-PRO (custom industry solutions); wheel-leg option (A2-W) |  | [unitree.com](https://www.unitree.com/A2) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length (standing) | 820 mm | 820 × 440 × 570 mm | [unitree.com](https://www.unitree.com/A2) |
| Width (standing) | 440 mm |  | [unitree.com](https://www.unitree.com/A2) |
| Height (standing) | 570 mm |  | [unitree.com](https://www.unitree.com/A2) |
| Length (lying prone) | 720 mm | 720 × 550 × 220 mm | [unitree.com](https://www.unitree.com/A2) |
| Width (lying prone) | 550 mm |  | [unitree.com](https://www.unitree.com/A2) |
| Height (lying prone) | 220 mm |  | [unitree.com](https://www.unitree.com/A2) |
| Material | Aluminum alloy + high-strength engineering plastic |  | [unitree.com](https://www.unitree.com/A2) |
| Weight (without battery) | 35 kg | about | [unitree.com](https://www.unitree.com/A2) |
| Weight (with battery) | 42 kg | about | [unitree.com](https://www.unitree.com/A2) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Degrees of freedom (joint motors) | 12 |  | [unitree.com](https://www.unitree.com/A2) |
| Max standing load | 100 kg | about | [unitree.com](https://www.unitree.com/A2) |
| Continuous walking load | 25 kg | about; ideally approx. 35 kg | [unitree.com](https://www.unitree.com/A2) |
| Speed | 0–3.7 m/s | up to ~5 m/s | [unitree.com](https://www.unitree.com/A2) |
| Maximum speed | 5 m/s | ~5 m/s | [unitree.com](https://www.unitree.com/A2) |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Slope walking capability | 45 ° | about | [unitree.com](https://www.unitree.com/A2) |
| Stair climbing, max step height | 30 cm |  | [unitree.com](https://www.unitree.com/A2) |
| Max climb height | 0.5–1 m | about | [unitree.com](https://www.unitree.com/A2) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Supply voltage | 50.4 V |  | [unitree.com](https://www.unitree.com/A2) |
| Power supply | Dual slots, dual batteries | hot-swappable dual batteries; swap without stopping | [unitree.com](https://www.unitree.com/A2) |
| Hot-swappable batteries | yes | dual-battery parallel design | [unitree.com](https://www.unitree.com/A2) |
| Battery capacity (single) | 453.6 Wh | single battery 9000 mAh | [unitree.com](https://www.unitree.com/A2) |
| Battery capacity (dual) | 907.2 Wh | dual batteries 18000 mAh | [unitree.com](https://www.unitree.com/A2) |
| Battery capacity (single) | 9,000 mAh |  | [unitree.com](https://www.unitree.com/A2) |
| Battery life (no load) | > 5 h | continuous walking, approx. 20 km | [unitree.com](https://www.unitree.com/A2) |
| Battery life (25 kg load) | > 3 h | continuous walking, approx. 12.5 km | [unitree.com](https://www.unitree.com/A2) |
| Range (no load) | 20 km | approx. | [unitree.com](https://www.unitree.com/A2) |
| Range (25 kg load) | 12.5 km | approx. | [unitree.com](https://www.unitree.com/A2) |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| Operating temperature | −20 to 55 °C | reliable triple power system | [unitree.com](https://www.unitree.com/A2) |
| Ingress protection | IP56 | A2 | [unitree.com](https://www.unitree.com/A2) |
| Ingress protection | IP56–IP67 | A2-PRO; core components rated IP67 | [unitree.com](https://www.unitree.com/A2) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Microphone | Microphone array |  | [unitree.com](https://www.unitree.com/A2) |
| GPS | Optional (A2); expanded/included (A2-PRO) |  | [unitree.com](https://www.unitree.com/A2) |
| LiDAR | 1 | A2: LiDAR ×1 + HD camera ×1 | [unitree.com](https://www.unitree.com/A2) |
| LiDAR | 2 | A2-PRO: LiDAR ×2 (front & rear industrial LiDARs) + HD camera ×1 | [unitree.com](https://www.unitree.com/A2) |
| HD camera | 1 | HD camera + front light to detect environment ahead | [unitree.com](https://www.unitree.com/A2) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Control & compute (platform) | 8-core high-performance CPU | standard | [unitree.com](https://www.unitree.com/A2) |
| Control & compute (user development) | Intel Core i7 | standard | [unitree.com](https://www.unitree.com/A2) |
| Optional compute | High computing power expansion dock | optional | [unitree.com](https://www.unitree.com/A2) |
| Smart OTA upgrade | Continuous upgrades |  | [unitree.com](https://www.unitree.com/A2) |
| Secondary development | Supported | see Secondary Development Manual | [unitree.com](https://www.unitree.com/A2) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Wi-Fi | Wi-Fi 6 |  | [unitree.com](https://www.unitree.com/A2) |
| Bluetooth | 5.2 |  | [unitree.com](https://www.unitree.com/A2) |
| 4G | Optional (A2); expanded/included (A2-PRO) |  | [unitree.com](https://www.unitree.com/A2) |
| RS485 | 2 port |  | [unitree.com](https://www.unitree.com/A2) |
| CAN | 2 port |  | [unitree.com](https://www.unitree.com/A2) |
| Gigabit Ethernet | 2 port |  | [unitree.com](https://www.unitree.com/A2) |
| USB 3.0 Type-C (8-core CPU) | 2 ports |  | [unitree.com](https://www.unitree.com/A2) |
| USB 3.0 Type-C (Intel Core i7) | 2 ports |  | [unitree.com](https://www.unitree.com/A2) |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Power output | 12V / 24V / BAT |  | [unitree.com](https://www.unitree.com/A2) |

### Actuation & Joints

| Spec | Value | Note | Source |
|---|---|---|---|
| Joint motors | 12 |  | [unitree.com](https://www.unitree.com/A2) |
| Joint bearings | Industrial-grade crossed roller bearings (high precision, high load capacity) |  | [unitree.com](https://www.unitree.com/A2) |
| Joint motors | Low-inertia, high-speed inner rotor PMSM (enhanced response & heat dissipation) |  | [unitree.com](https://www.unitree.com/A2) |
| Max joint torque | 180 N·m | about | [unitree.com](https://www.unitree.com/A2) |
| Range of motion (body) | −58 to 58 ° |  | [unitree.com](https://www.unitree.com/A2) |
| Range of motion (thigh) | −134 to 180 / −89 to 225 ° |  | [unitree.com](https://www.unitree.com/A2) |
| Range of motion (shank) | −158 to −30 ° |  | [unitree.com](https://www.unitree.com/A2) |
| Joint encoder | Dual encoders |  | [unitree.com](https://www.unitree.com/A2) |
| Cooling system | Local air cooling |  | [unitree.com](https://www.unitree.com/A2) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Safety note | Complex structure and powerful dynamics; users must keep a safe distance at all times | footnote [4] | [unitree.com](https://www.unitree.com/A2) |
| Intended use | Civilian robot; dangerous modifications or hazardous use prohibited |  | [unitree.com](https://www.unitree.com/A2) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Wireless vector follow module | Optional (A2); expanded/included (A2-PRO) |  | [unitree.com](https://www.unitree.com/A2) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Speaker | yes |  | [unitree.com](https://www.unitree.com/A2) |
| Front light | yes |  | [unitree.com](https://www.unitree.com/A2) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Warranty | 12 months | see Product Warranty Manual | [unitree.com](https://www.unitree.com/A2) |
| Price | Contact sales |  | [unitree.com](https://www.unitree.com/A2) |

## Documents

- [Unitree A2 product page (A2 parameter table, A2 / A2-PRO)](https://www.unitree.com/A2)

## Notes

Unitree A2 page (checked 2026-11-17): standing 820 x 440 x 570 mm, 42 kg with battery (35 kg without), 12 joint motors, single battery 9000 mAh (453.6 Wh) and dual 18000 mAh (907.2 Wh) - the 907.2 Wh recorded is the dual-battery figure; walking load about 25 kg (ideally ~35 kg), standing load about 100 kg; battery life >5 h without load / >3 h with 25 kg (the 3 h recorded is the loaded figure); speed 0-3.7 m/s (up to ~5 m/s in special configuration); IP56 on A2, IP56-IP67 on A2 Pro. A2 Pro adds a second LiDAR and wireless-vector follow module.

## Sources

- Official page: [unitree.com](https://www.unitree.com/A2)
- [github.com](https://github.com/unitreerobotics/unitree_sdk2)
- [github.com](https://github.com/unitreerobotics/unitree_ros/blob/master/robots/a2_description/urdf/a2.urdf)
- [github.com](https://github.com/unitreerobotics/unitree_ros/blob/master/robots/a2_description/a2.xml)
- [github.com](https://github.com/unitreerobotics/unitree_sdk2_python)
- [github.com](https://github.com/unitreerobotics/unitree_ros)
- [github.com](https://github.com/unitreerobotics/unitree_ros2)
- [github.com](https://github.com/unitreerobotics/unitree_mujoco)
- [younginmobility.com](https://www.younginmobility.com/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-19). Source repository: https://github.com/htcrefactor/robot-catalog*
