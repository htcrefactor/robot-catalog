# Hyundai Motor Group (Robotics LAB) MobED Pro

> Production autonomous mobility platform using eccentric Drive-and-Lift wheel modules for posture control over curbs (100–200 mm) and slopes; Ethernet API, follow-me; unveiled iREX Dec 2025 with sales scheduled H1 2026.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=hyundai-mobed-pro
- Category: Wheel-legged
- Locomotion: Wheel-legged
- Manufacturer: Hyundai Motor Group (Robotics LAB) (South Korea)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 1,150 mm |
| Width | 750 mm |
| Height | 650 mm |
| Weight | 88 kg |
| Payload | 47 kg |
| Max speed | 2.8 m/s (10.1 km/h) |
| Wheels | 4 |
| Runtime | 4 h |
| Battery | 1,470 Wh |
| IP rating | IP54 |
| Released | 2025 |
| Status | Pre-order |
| API | yes |
| Sensors | LiDAR, Camera, Radar |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

47 values from 2 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Variants | MobED Pro; MobED Basic |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Sales start | H1 2026 (scheduled) | unveiled iREX 2025, 3 Dec 2025 | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Width | ≤750 mm |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Length | ≤1150 mm |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Height | ≤650 mm | incl. antenna | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Height | ≤510 mm | Robotics LAB product page (current), incl. antenna | [robotics.hyundai.com](https://robotics.hyundai.com/en/unveiled-robots/mobile/mobedNew.do) |
| Tare weight | ≤88 kg | press release Dec 2025 | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Weight | 83 ± 1.5% kg | Robotics LAB product page (current) | [robotics.hyundai.com](https://robotics.hyundai.com/en/unveiled-robots/mobile/mobedNew.do) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Maximum payload | ≤47 kg |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Structure | 360° rotating eccentric structure; Drive-and-Lift (DnL) modules integrate drive, steering, braking, posture | eccentric rotation radius 100 mm | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Eccentric rotation radius | 100 mm |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Wheels | 4 independently controlled wheels | https://robotics.hyundai.com/en/unveiled-robots/mobile/mobedNew.do | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Driving postures | Outward deployment, inward deployment, backward, forward |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Max speed | 2.8 m/s | 10 km/h; other postures | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Max speed (inward posture) | 0.3 m/s | inward deployment posture | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Maximum slope | ±10 ° | slopes over 10° automatically avoided | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Curb clearance height | 100–200 mm | curb location specified by user when creating map | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Max slope (autonomous) | ±8 ° | manual ±10°; product page | [robotics.hyundai.com](https://robotics.hyundai.com/en/unveiled-robots/mobile/mobedNew.do) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Rated capacity | 1.47 kWh |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Battery pack voltage | 36–49.2 V |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Rated discharge current | 33.6 A |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Operating time | ≥4 h | BMS SOC 90% → 10% | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charging time | ≤2.5 h | BMS SOC 10% → 90% | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Charging method | Manual charger, charging station (automatic charging module sold separately) |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Auto charging station | Shape-recognition-based automatic charging station | https://robotics.hyundai.com/en/unveiled-robots/mobile/mobedNew.do | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| Operating temperature | 0 to 40 °C |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Charging temperature | 1 to 35 °C |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Storage temperature | 0 to 40 °C |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Ingress protection | IP54 |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Functional safety sensor | Radar |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| LiDAR | 2 | LiDAR-camera fusion | [robotics.hyundai.com](https://robotics.hyundai.com/en/unveiled-robots/mobile/mobedNew.do) |
| Depth cameras | 3 |  | [robotics.hyundai.com](https://robotics.hyundai.com/en/unveiled-robots/mobile/mobedNew.do) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Software update & diagnostics | Wired update, diagnostic scanner |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Customization | Universal mounting rails and APIs for attachments |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| API | Ethernet |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Streaming | Supported | https://robotics.hyundai.com/en/unveiled-robots/mobile/mobedNew.do | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Top module mechanical | Mounting rail |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Top module port | DB37 connector (communication and power) | https://robotics.hyundai.com/en/unveiled-robots/mobile/mobedNew.do | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Top module power | 24 V 300 W / 48 V 500 W | press release | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Top module power | 18–25 V, 10 A (max 250 W) | Robotics LAB product page | [robotics.hyundai.com](https://robotics.hyundai.com/en/unveiled-robots/mobile/mobedNew.do) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery certification | UL2271 |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Certifications | CE (ISO 13482 / ISO 3691-4), UL (UL3100 / UL3300) |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Charging station certification | IEC / UL / KC 60335, KC / CE / FCC |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Drive modes | Autonomous (Autonomous, Smart Assist) / Manual (Basic, Freestyle, Zigzag) |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Autonomy | AI navigation: obstacle recognition/avoidance, predictive navigation, route generation, moving-object tracking, follow-me mode, self-mapping |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Controller | Wide touchscreen controller with 3D UI/UX |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Warranty | 1 year |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |

## Documents

- [Hyundai Motor Group newsroom – MobED at iREX 2025 (spec table)](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082)
- [Hyundai Robotics LAB – MobED product page (spec table, KR)](https://robotics.hyundai.com/en/unveiled-robots/mobile/mobedNew.do)

## Notes

Hyundai Motor Group press release at iREX 2025 (3 Dec 2025) specification table: Pro up to 750 x 1150 x 650 mm incl. antenna, tare weight up to 88 kg, maximum payload up to 47 kg, autonomous (Autonomous/Smart Assist) plus manual modes, up to 0.3 m/s in inward posture and up to 2.8 m/s otherwise, 1.47 kWh at 36-49.2 V, >=4 h, charge <=2 h 30 min, IP54, 0-40 C, Ethernet API. Sensor set from the HMG Journal piece: GPS, two 3D LiDARs, three cameras, eight radars and an IMU.

## Sources

- Official page: [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082)
- [hyundaimotorgroup.com](https://www.hyundaimotorgroup.com/en/story/mobed-next-gen-mobility-robot-platform)
- [robotics.hyundai.com](https://robotics.hyundai.com/story/log/view.do?seq=181)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-26). Source repository: https://github.com/htcrefactor/robot-catalog*
