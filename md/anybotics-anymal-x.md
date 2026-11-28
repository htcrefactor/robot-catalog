# ANYbotics ANYmal X

> ATEX Zone 1/2 explosion-protected version of ANYmal for autonomous inspection in oil, gas and chemical plants.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=anybotics-anymal-x
- Category: Quadruped
- Locomotion: Legged
- Manufacturer: ANYbotics (Switzerland)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Runtime | 3 h |
| IP rating | IP65 |
| Released | 2026 |
| Status | Pilot |
| API | yes |
| Sensors | Zoom camera, Thermal camera (640x512 radiometric), Acoustic imager, Microphone, Gas sensing module (optional) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

71 values from 2 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Manufacturer | ANYbotics AG |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) |
| Manufacturer address | Hagenholzstrasse 83a, 8050 Zürich, Switzerland |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · back page |
| Robot type | Explosion-protected autonomous legged inspection robot |  | [anybotics.com](https://www.anybotics.com/robotics/anymal-x/) |
| Specification document date | V1, 10/2026 | specifications are preliminary and subject to change | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 960 mm | preliminary specification, subject to change | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Width | 596 mm | preliminary specification, subject to change | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Height | 1,015 mm | preliminary specification, subject to change | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Weight | 92 kg | preliminary specification, subject to change | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Typical walking speed | 0.6 m/s |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Maximum walking speed | < 1.3 m/s |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Stair speed | > 0.1 m/s |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Stairs | 45 ° | up and down; only verified stair configurations in Zone 1; stairs must have guardrails | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Maximum stair rise | 230 mm |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Minimum stair run | 210 mm |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Stair types | Open risers and grated steps |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Inclines and declines | 20 ° | up to | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Obstacle step-over | 250 mm | up to; on approved inspection routes | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Passage width | 80 cm | ≥ 80 cm | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Corridor width for a 90° turn | 1 m | 90° turn in a 1 m corridor | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Overhead clearance | 60 cm | as low as 60 cm (robot crouches) | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Surface compatibility | Gratings, gravel, concrete, metal, wet and oily surfaces; multiple levels |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.6 |
| Ex-Zone floor requirement | Conductive floors | in Ex-Zones | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Navigation | Onboard navigation and route replanning; stored missions continue offline |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.6 |
| Site mapping | Import point clouds or handheld scans in Shift Maps |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.6 |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery type | Lithium-ion |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Battery rated voltage | 42.9 V | DC | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Battery capacity | 28 Ah |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Battery energy | 1.2 kWh |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Battery runtime | > 3 h | per charge | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Battery management | Battery monitoring disconnects power when temperature, voltage or current limits are exceeded |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.5 |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Docking | Autonomous; dock installed in a sheltered location in a non-hazardous area; missions resume after charging |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Station footprint | Docking station approx. 1 × 2 m; nitrogen refill station approx. 1 × 2 m (2 × 2 m combined) |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Charging temperature | 0 to 45 °C |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Charging location | Outside the hazardous area only, using the ANYbotics charging system; keep 2 m radius around charging robot free of flammable material |  | [anybotics.com](https://www.anybotics.com/robotics/anymal-x/) |
| Nitrogen supply | Purity ≥ 99.9 %; oxygen content ≤ 0.1 % | supplied through the nitrogen refill station | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| Lighting | Operates in full darkness, 0 lux; visual inspection uses onboard illumination |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Ex certification | ATEX; Zones 1 and 2; Gas Group IIB; T4; EPL Gb; Category 2G | IECEx certification will be available with first production | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Maximum surface temperature | 135 °C | temperature class T4 | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.5 |
| Explosion protection | Flameproof enclosures; pressurization (nitrogen overpressure, monitored); intrinsic safety; battery management |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.5 |
| Ingress protection | IP65 | robot | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Ingress protection | IP67 | inspection payload | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Continuous operating ambient temperature | −10 to 50 °C |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Storage / transport temperature | −10 to 50 °C |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Humidity | 5–95 % | operating, non-condensing | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Rain | Operates in light (< 4 mm/h) and moderate (< 16 mm/h) rain |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Altitude | 0–2,000 m | above sea level | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Obstacle detection | ≥ 5 cm wide, ≥ 25 cm tall; ground clutter < 5 cm passable |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Visual (zoom camera) | Zoom camera; visual change and object detection; advanced instrument readout | inspection payload | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Thermal camera | 640 × 512 radiometric imaging | inspection payload | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Acoustic imager | Acoustic imager for gas and air leak localization | inspection payload | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Microphone | Microphone recordings for spectral analysis and mechanical fault screening | inspection payload | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Gas sensing (optional module) | Combustible: LEL (HC), CH4, C3H8; toxic/process: H2S, NH3, CO, CO2, Cl2, SF6, SO2; atmospheric: O2; optional R134a, NO, NO2; up to 2 sensors | gas measurements support inspection and are not a safety-rated alarm function | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Robot software | Localization, mapping, path planning, motion control and diagnostics on board |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Operations platform | ANYbotics Shift (Maps, Fleet, Insight, Connect) with inspection intelligence |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| API | REST API for data landing, mission triggering, scheduling and monitoring, robot health and environment setup |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.7 |
| Hosting | Managed cloud, customer-hosted cloud or on-premises |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Information security | ISO 27001-certified ISMS; single sign-on, role-based access, encryption in transit and at rest |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.7 |
| Offline operation | Stored missions continue offline with data buffered on board; sync with Shift when connectivity returns | remote assistance requires connectivity | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.6 |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Wi-Fi | Wi-Fi 6, 2.4 / 5 GHz |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Cellular | 5G / 4G LTE |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Inspection payload dimensions | 193 × 251 × 267 mm |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Inspection payload weight | 6.95 kg |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Inspection payload interfaces | USB and Ethernet | pan-tilt unit, IP67 | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Certification | ATEX EU-type examination certificate issued by Bureau Veritas (notified body) for Zones 1 and 2 | IECEx will be available with first production | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.5 |
| Excluded use | Zone 0; IIC gases including hydrogen and acetylene; explosive dust atmospheres |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.5 |
| Emergency stop | Hardware button immediately cuts power to the robot’s actuators |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.11 |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Control tablet | ATEX-rated control tablet | supports setup and robot control in approved hazardous areas; shows gas warnings with optional gas module | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.11 |
| Tele-assist | Remote assistance for mission exceptions |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.11 |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Active warning light | Indicates actuators are powered on; personnel keep at least 2 m away while the light is active |  | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.11 |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Intended service life | 3 years | post-sale, for the robot and safety-relevant components | [info.anybotics.com](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf) · p.10 |
| Solution components | Docking station, charger, nitrogen refill station, ATEX-rated control tablet and ANYbotics Shift |  | [anybotics.com](https://www.anybotics.com/robotics/anymal-x/) |

## Documents

- [ANYmal X brochure & technical specifications (V1, 10/2026, preliminary)](https://info.anybotics.com/hubfs/Technical%20Documents/ANYmalX_Brochure_web.pdf)
- [ANYbotics ANYmal X product page (incl. FAQ)](https://www.anybotics.com/robotics/anymal-x/)

## Notes

Maker page: ATEX-certified for Zones 1 and 2 (IIB, T4, category 2G) with IECEx to follow first production; over 3 h battery runtime with autonomous docking; stairs to 45 deg (230 mm rise / 210 mm run); IP65 robot, IP67 payload; Wi-Fi 6 and 5G/4G; continuous ambient -10 to 50 C; 0 lux navigation. Overall mass and dimensions are not published.

## Sources

- Official page: [anybotics.com](https://www.anybotics.com/robotics/anymal-x/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-28). Source repository: https://github.com/htcrefactor/robot-catalog*
