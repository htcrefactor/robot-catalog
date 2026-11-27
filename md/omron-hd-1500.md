# OMRON HD-1500

> Heavy-duty AMR for pallets and large assemblies up to 1,500 kg with 360° safety coverage.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=omron-hd-1500
- Category: AMR
- Locomotion: Wheeled
- Manufacturer: OMRON (Japan)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Weight | 506 kg |
| Payload | 1,500 kg |
| Max speed | 1.8 m/s (6.5 km/h) |
| Runtime | 9 h |
| Battery | 3,590 Wh |
| IP rating | IP20 |
| Status | Commercial |
| API | yes |
| Compute | Internally mounted OMRON NX102 controller (Ethernet access) |
| Sensors | 2x safety laser scanners (360°), 2x low lasers, Optional supplementary laser scanners |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

81 values from 1 document, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Ordering codes | 37483-00000 (no HAPS); 37483-10004 (with charging station, pendant, top plate); 37483-00200 (double HAPS); 37483-10204 (double HAPS + charging station, pendant, top plate) |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) · Ordering Information p.1 |
| Datasheet catalog number | I855 |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 1,696 mm |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) · Dimensions p.7 |
| Width | 1,195 mm |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) · p.7 |
| Height | 370 mm |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) · p.7 |
| Weight (with battery) | 506 kg |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Swing radius | 982 mm |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Turn radius | 0 mm |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Maximum payload capacity | 1,500 kg |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Maximum translational speed | 1,800 mm/s | forward and reverse | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Maximum reverse speed | 1,800 mm/s |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Maximum rotational speed | 60 °/s | reduced to 45°/s above 300 mm/s | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Maximum translational acceleration | 900 mm/s² |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Maximum rotational acceleration/deceleration | 150 °/s² |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Stop position repeatability (single AMR) | to a position ±70 mm, ±2°; to standard target ±25 mm, ±2°; HAPS ±8 mm, ±0.4°; CAPS ±5 mm, ±0.4° |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Stop position repeatability (fleet) | to a position ±75 mm, ±2°; to standard target ±35 mm, ±2°; HAPS ±10 mm, ±0.75°; CAPS ±16 mm, ±0.5° |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Drive wheel material | Non-marking, static-dissipative polyurethane on steel rim |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Passive caster material | Non-marking polyurethane on cast iron rim |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Floor requirements | No water, oil or dirt; minimum flatness FF25 (ACI 117) |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Traversable step | 10 mm | recommended 500 mm/s forward, 400 mm/s reverse | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Traversable gap | 20 mm |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Maximum slope | 5° / 8.75% |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Minimum floor compressive strength | 5 MPa |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Minimum coefficient of friction | 0.6 |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Routing | Autonomous routing by localizing with safety scanning laser based on environment mapping; capable of full reverse navigation |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Map making | Drive AMR through environment; upload scan data to MobilePlanner |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Run time (no payload) | 12.5 h | auxiliary power draw affects run time | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Run time (full payload) | 9 h |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Battery type | Lithium-ion (LiFePO4) | ordering code 68330-000, ordered separately | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Battery voltage | 48 to 57 VDC | 52.8 VDC nominal | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Battery capacity | 68 Ah | nominal | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Charge cycles | approx. 8000 cycles | ~80% capacity after 100% DoD at 23 °C | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Battery removable | yes |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Recharge time | 24 min | 20% to 80% | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Charging method | Automatic or manual |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Battery operating temperature | 5 to 40 °C |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Charging station input | 3-phase 200–240 VAC 50/60 Hz (Delta/Wye) or 380–415 VAC 50/60 Hz (Wye); input current 25 A |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Charging station power | 7.75 kW consumption; 6.84 kW max output; 40–57 VDC; 120 A nominal output (fused 150 A) |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Charging station | Power supply box 108 kg; docking target 27 kg; IP20 (IP10 charging pads); 5–40 °C; ISO 5 cleanroom |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| Ambient temperature | 5 to 40 °C |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Storage temperature | −20 to 60 °C |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Ambient humidity | 5–95 % | non-condensing | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Operating environment | Indoor only; no corrosive or explosive gas or liquid; no ionizing radiation |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Altitude | 2,000 m | maximum | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Ingress protection | IP20 |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Dust / smoke | Accumulated dust < 37 µm must not exceed 1.5 mL/m²; avoid smoke |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Enclosure rating | Type 1 |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Low lasers | Two, detect obstacles below the safety scanner plane |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Supplementary laser scanners (optional) | Two optional, for object detection in the vertical plane (kit 68945-030) |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Safety scanning lasers | Two, 360° detection around AMR; scan plane 181 mm above floor |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| High Accuracy Positioning System (HAPS) | Magnetic tape sensor, IP64, −40 to 85 °C; single 68925-010 / double 68925-020 |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Internal controller | OMRON NX102 unit (internally mounted) |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Fleet software | FLOW Core / Fleet Operations Workspace; FLOW iQ optional; Unified Fleet license |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Minimum software version | FLOW Core 4.0 |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Configuration software | MobilePlanner (Windows 10/11 64-bit; tablet edition Android 9+ / iOS 10+) |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Integration APIs | ARCL; Fleet Operations Workspace Core Integration Toolkit MQTT API |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Wireless | IEEE 802.11 a/b/g; two integrated antennas |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Ethernet | One RJ-45 port for maintenance and access to internal NX102 unit |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Digital I/O | 8 PNP (sourcing) inputs; 8 PNP (sourcing) outputs |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Analog I/O | 4 inputs and 4 outputs, −10 to 10 VDC |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Audio | Digital audio out |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Safety interfaces | Dual-channel E-stop inputs/outputs; dual-channel safety outputs; dual-channel protective stop inputs |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Maximum moment of inertia | 490 kg·m² |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Auxiliary power (unregulated) | 48 to 57 VDC (52.8 nominal); 50 A fused |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Auxiliary power (regulated) | 23 to 25 VDC; two channels fused at 1.6 A |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Cleanroom rating | ISO 5 / Class 100 | AMR and charging components as a complete system | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Standards (AMR) | EN ISO 12100; EN ISO 13849-1; EN 60204-1; EN ISO 10218-1; EN 61326-3-1; EN 61326-1; EN ISO 3691-4; EN 12895; CAN/CSA Z434; CAN/UL 3100; KS C 9610-6-2; KS C 9610-6-4 |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Standards (battery) | ANSI/CAN/UL/ULC 2271; UN 38.3 |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Standards (charging station) | UL 1012; CAN/CSA C22.2.107.2; EN 61204-7; EN 62477-1 |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Certification markings | AMR: cTUVus, KC; battery: cURus, CE; power supply box: cTUVus; docking target: cTUVus |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Laser class | Class 1M, eye-safe (IEC 60825-1, 21 CFR 1040.10/1040.11) |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Safety laser scanner zone sets | Safety-rated alternate zone inputs toggle default/alternate configurations |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| E-STOP buttons | Five on AMR (sides and operator panel); additional can be added to payload |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Operator panel controls | E-STOP; ON/OFF; brake release; pendant port; maintenance port; main disconnect switch |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Pendant | Handheld, three-position enabling switch; 0–40 °C; IP30; for manual driving/map creation (68940-000L) |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Visual indicators | Light discs on sides; light strips front and back; additional indicators can be added |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Audible indicators | Two speakers; additional buzzers can be added |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Operator panel display | 178 mm diagonal LCD |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Included items | Labels; USB drive with docs/software; printed safety/unpacking/declaration docs; lift kit (straps and hardware) |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Optional items | Supplementary laser scanner kit 68945-030; Mobile I/O Box 23419-802; top plate kit 68950-000; pendant 68940-000L; power supply box 73990-000; docking target 68910-000; battery 68330-000; antenna extension kit 68955-000; HAPS |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |
| Warranty | 12 months from date of sale |  | [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf) |

## Documents

- [HD-1500 Autonomous Mobile Robots datasheet I855 (OMRON)](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf)

## Notes

Checked 2026-11-19 against OMRON datasheet I855: 506 kg with battery, 1,500 kg, 1.8 m/s, 9 h at full payload (12.5 h no payload), IP20 match. Maker datasheet text gives no L x W x H, so those stay empty.

## Sources

- Official page: [robotics.omron.com](https://robotics.omron.com/products/mobile-robots/hd-series/hd-1500)
- [assets.omron.eu](https://assets.omron.eu/downloads/latest/datasheet/en/i855_hd-series_mobile_robot_datasheet_en.pdf)
- [omron.co.kr](https://www.omron.co.kr/)
- [robotics.omron.com](https://robotics.omron.com/ko/products/mobile-robots/ld-series/ld-250/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-27). Source repository: https://github.com/htcrefactor/robot-catalog*
