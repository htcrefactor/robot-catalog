# OMRON LD-250

> 250 kg natural-feature-navigation AMR for transport between workstations, lines and storage.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=omron-ld-250
- Category: AMR
- Locomotion: Wheeled
- Manufacturer: OMRON (Japan)
- Verification: not recorded

## Core specs

| Field | Value |
|---|---|
| Length | 969 mm |
| Height | 383 mm |
| Weight | 148 kg |
| Payload | 250 kg |
| Max speed | 1.2 m/s (4.3 km/h) |
| Runtime | 10 h |
| Battery | 1,843 Wh |
| IP rating | IP20 |
| Status | Commercial |
| API | yes |
| Sensors | Front safety laser scanner (240°, PLd), Low front laser (126°), Rear ToF sensors, Optional side lasers (270°) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

76 values from 1 document, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Ordering codes (LD-250) | 37222-00000 (no docking kit); 37222-00002 (docking kit); 37222-10004 (docking kit + pendant) |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) · Ordering Information p.1 |
| Ordering codes (LD-250 ESD) | 37222-20000; 37222-20002; 37222-20004 |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) · p.1 |
| Variants | LD-250; LD-250 ESD (IEC 61340-5-1 compliant for electrostatic-sensitive environments) |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Datasheet catalog number | I828-E-17 |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 969 mm |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) · Dimensions p.10 |
| Width | 720 mm |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) · p.10 |
| Height (to mounting surface) | 380 mm |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) · p.10 |
| Ground clearance (lowest point) | 40 mm | dimension drawing | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) · p.10 |
| Weight (with battery) | 148 kg |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Maximum payload | 250 kg |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Maximum speed | 1,200 mm/s |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Maximum rotation speed | 120 °/s |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Stop position repeatability (single AMR) | to a position ±75 mm; to standard target ±25 mm, ±2°; with CAPS ±8 mm, ±0.5°; with HAPS ±8 mm, ±0.4° | default parameters, LD-built map | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Stop position repeatability (fleet) | to a position ±100 mm; to standard target ±35 mm, ±2°; with CAPS ±14 mm, ±0.6°; with HAPS ±10 mm, ±0.6° |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Drive wheel material | Aluminum with polyurethane tread |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Passive caster material | Elastomer (polyurethane) |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Floor requirements | No water, oil or dirt; minimum flatness FF25 (ACI 117) |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Traversable step | 10 mm | 600 mm/s recommended; routine driving over steps should be avoided | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Traversable gap | 15 mm | at maximum speed | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Maximum slope | 1.7° / 3% |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Minimum floor compressive strength | 5 MPa |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Maximum floor resistivity | 10^8 Ω |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Routing | Autonomous routing by localizing with safety scanning laser based on environment mapping |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Map making | Scan by manually driving the AMR; upload to MobilePlanner |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Run time (no payload) | 13 h approx. |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Run time (full payload) | 10 h approx. |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Battery type | Lithium-ion (LiFePO4) | ordering code 20452-700, ordered separately | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Battery weight | 19 kg |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Battery voltage | 22 to 30 VDC | 25.6 VDC nominal | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Battery capacity | 72 Ah | cell nominal | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Recharge cycles | approx. 2000 cycles | ~80% capacity remaining after 100% DoD at 15–35 °C | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Battery removable | yes | removable, rechargeable | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Recharge time | 2 h 10 min | 20% to 80% | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Charging method | Automatic (docking station) or manual |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Docking station power | 100–240 VAC, 50–60 Hz; 8 A; 800 W |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Docking station | 5–40 °C; 5–95% RH; 8.2 kg; wall bracket, floor or floor plate mounting; 495 × 406 mm free-standing footprint |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| Ambient temperature | 5 to 40 °C |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Ambient humidity | 5–95 % | non-condensing | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Operating environment | Indoor only; no excessive dust, no corrosive gas or liquid; direct sunlight may cause safety laser false positives |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Dust / smoke | Accumulated dust < 37 µm must not exceed 10 mL/m²; avoid smoke |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Ingress protection | IP20 |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Maximum altitude | 1,000 m | 2000 m if ambient operating temperature ≤ 35 °C | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Battery ingress protection | IP20 |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Low front laser | One Class 1 laser at front, 126° field of view |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Supplementary laser scanners (optional) | Two Class 1 lasers, 270° FOV, on sides of payload structure, user-mounted |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Safety scanning laser | One at front, Class 1, PL d per ISO 13849-1, 240° field of view |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Rear sensing | Time-of-flight (ToF) sensors |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| High Accuracy Positioning System (HAPS) | Magnetic floor tape (25 mm) sensor; IP64; −40 to 85 °C; single 21374-100 / double 21374-000 for LD-250 |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Acuity localization camera (optional) | 140° FOV; 12 VDC; 3.3 W max |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Fleet software | FLOW Core / Fleet Operations Workspace; fleet manager supervises up to 100 vehicles; FLOW iQ optional |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Minimum software version | FLOW Core 4.0 |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Configuration software | MobilePlanner (Windows 10/11 64-bit; tablet edition Android 9+ / iOS 10+) |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Integration APIs | ARCL (Advanced Robotics Command Language); Fleet Operations Workspace Core Integration Toolkit MQTT API |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Software licenses | CAPS (Cell Alignment Positioning System); Cycle Time Optimization; Unified Fleet; FLOW iQ |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Wireless | IEEE 802.11 a/b/g |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Ethernet | One general-purpose shielded Auto-MDIX port |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Serial | Two serial communication interfaces |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Digital I/O | 16 inputs, 16 outputs |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Audio | Digital audio in/out |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Auxiliary power | 5 VDC 1 A; 12 VDC 1 A; 20 VDC 1 A switched; 22–30 VDC (25.6 nominal) 4 A switched; 10 A switched; 10 A safe switched (10 A switched + safe share one 10 A fuse) |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Standards (AMR) | CAN/UL 3100; EN ISO 12100; EN ISO 13849-1; EN 60204-1; ANSI B56.5; EN 61000-6-2; EN 61000-6-4; EN ISO 3691-4 (except 4.1.15b, 4.8.2.6 items 6–7, 4.12, 4.14); KN 61000-6-2; KN 61000-6-4 |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Standards (battery) | UN 38.3; ANSI/CAN/UL/ULC 2271 |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Standards (docking station) | UL 1012; CSA C22.2.107.2 |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Cleanroom rating | ISO 5 / Class 100 (AMR, battery and docking station) |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Certification marking | AMR: cULus, KC; docking station: cULus; battery: cRUus |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Performance level (safety laser) | PL d | ISO 13849-1 | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Laser class | Class 1 |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| E-STOP buttons | One at operator panel, one on each side; additional can be added to payload structure |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Operator buttons | ON, OFF, brake-release, keyed mode selection |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Pendant (joystick) | 0.55 kg, IP56, 3.0 m cable; for manual driving and map creation (13558-000) |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Audible indicators | Two speakers; additional buzzers can be added |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Visual indicators | Light discs on sides; additional indicators can be added |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Operator display | 3.5 in TFT, 320 × 240 px colour |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Included items | Operator panel jumper plug; two SMA rubber-duck antennas; labels; USB drive with docs/software; printed user's manual |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Optional items | Mobile I/O Box; HAPS; magnetic tape; RS232 splitter; Acuity localization; supplementary laser scanner kit; docking station 12477-000; antenna extension kit; battery power cable; pendant; digital I/O terminal block; top plate LD-250 20458-002 (ESD 20458-202); rear-facing laser bundle 21446-000 |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |
| Warranty | 12 months from date of sale |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf) |

## Documents

- [LD Series Autonomous Mobile Robots datasheet I828-E-17 (OMRON)](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf)

## Sources

- Official page: [robotics.omron.com](https://robotics.omron.com/products/mobile-robots/ld-series/ld-250/)
- [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i828_ld-series_mobile_robot_datasheet_en.pdf)
- [omron.co.kr](https://www.omron.co.kr/)
- [robotics.omron.com](https://robotics.omron.com/ko/products/mobile-robots/ld-series/ld-250/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-17). Source repository: https://github.com/htcrefactor/robot-catalog*
