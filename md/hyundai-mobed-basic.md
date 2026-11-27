# Hyundai Motor Group (Robotics LAB) MobED Basic

> R&D version of MobED without pre-installed autonomy (manual drive, RS422 API) built on the eccentric Drive-and-Lift wheel modules; sales scheduled H1 2026.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=hyundai-mobed-basic
- Category: Wheel-legged
- Locomotion: Wheel-legged
- Manufacturer: Hyundai Motor Group (Robotics LAB) (South Korea)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 1,150 mm |
| Width | 750 mm |
| Height | 430 mm |
| Weight | 78 kg |
| Payload | 57 kg |
| Max speed | 2.8 m/s (10.1 km/h) |
| Wheels | 4 |
| Runtime | 4 h |
| Battery | 1,470 Wh |
| IP rating | IP54 |
| Released | 2025 |
| Status | Pre-order |
| API | yes |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

42 values from 2 documents, checked against maker sources on 2026-11-04.

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
| Height | ≤430 mm | press release Dec 2025 | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Height | ≤420 mm | Robotics LAB product page (current) | [robotics.hyundai.com](https://robotics.hyundai.com/en/unveiled-robots/mobile/mobedNew.do) |
| Tare weight | ≤78 kg | press release Dec 2025 | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Weight | 76 ± 1.5% kg | Robotics LAB product page (current) | [robotics.hyundai.com](https://robotics.hyundai.com/en/unveiled-robots/mobile/mobedNew.do) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Maximum payload | ≤57 kg |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Structure | 360° rotating eccentric structure; Drive-and-Lift (DnL) modules integrate drive, steering, braking, posture | eccentric rotation radius 100 mm | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Eccentric rotation radius | 100 mm |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Wheels | 4 independently controlled wheels | https://robotics.hyundai.com/en/unveiled-robots/mobile/mobedNew.do | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Driving postures | Outward deployment, inward deployment, backward, forward |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Max speed | 2.8 m/s | 10 km/h; other postures | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Max speed (inward posture) | 0.3 m/s | inward deployment posture | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Maximum slope | ±10 ° | operation at user discretion | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Curb clearance height | 100–200 mm |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |

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
| Charging method | Manual charger |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |

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

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Software update & diagnostics | Wired update, diagnostic scanner |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Customization | Universal mounting rails and APIs for attachments |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| API | RS422 |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Streaming | Not included | https://robotics.hyundai.com/en/unveiled-robots/mobile/mobedNew.do | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Top module mechanical | Mounting rail |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Top module port | DB37 connector (communication and power) | https://robotics.hyundai.com/en/unveiled-robots/mobile/mobedNew.do | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Top module power | 24 V 300 W / 48 V 500 W | press release | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Top module power | 18–25 V, 12 A (max 300 W) | Robotics LAB product page | [robotics.hyundai.com](https://robotics.hyundai.com/en/unveiled-robots/mobile/mobedNew.do) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery certification | UL2271 |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Certifications | In progress |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Charging station certification | IEC / UL / KC 60335, KC / CE / FCC |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Drive modes | Manual (Basic, Freestyle, Zigzag) |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |
| Autonomy | Not included; custom autonomous driving kit can be installed on top module |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Warranty | 1 year |  | [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082) |

## Documents

- [Hyundai Motor Group newsroom – MobED at iREX 2025 (spec table)](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082)
- [Hyundai Robotics LAB – MobED product page (spec table, KR)](https://robotics.hyundai.com/en/unveiled-robots/mobile/mobedNew.do)

## Notes

Hyundai Motor Group press release at iREX 2025 (3 Dec 2025) specification table: Basic up to 750 x 1150 x 430 mm, tare weight up to 78 kg, maximum payload up to 57 kg, manual drive only (Basic/Freestyle/Zigzag, no autonomous mode), up to 2.8 m/s outside the inward posture, battery rated capacity 1.47 kWh at 36-49.2 V, operating time >=4 h (BMS 90->10 %), charge <=2 h 30 min, IP54, 0-40 C, RS422 API, no pre-installed autonomy. No degrees of freedom are published.

## Sources

- Official page: [hyundai.com](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001082)
- [robotics.hyundai.com](https://robotics.hyundai.com/story/log/view.do?seq=181)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-27). Source repository: https://github.com/htcrefactor/robot-catalog*
