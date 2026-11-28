# OMRON LD-300

> Compact 300 kg AMR in a 580 mm-wide footprint with dual safety scanners, wireless charging and OMRON FLOW Core fleet management.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=omron-ld-300
- Category: AMR
- Locomotion: Wheeled
- Manufacturer: OMRON (Japan)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 800 mm |
| Width | 580 mm |
| Height | 320 mm |
| Weight | 117 kg |
| Payload | 300 kg |
| Max speed | 2.1 m/s (7.6 km/h) |
| Runtime | 6.5 h |
| Battery | 1,074 Wh |
| IP rating | IP22 |
| Released | 2026 |
| Status | Pre-order |
| Sensors | Two safety laser scanners (360° coverage), Rear low LiDAR (front low laser optional) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

69 values from 3 documents, checked against maker sources on 2026-11-19.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Ordering code | 37790-10000 |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Order start | 2026-11-18 | Americas and Europe first; other regions to follow | [robotics.omron.com](https://robotics.omron.com/news/new-ld-series-amr-launch/) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Footprint (L x W) | 800 x 580 mm |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Length | 800 mm |  | [robotics.omron.com](https://robotics.omron.com/new-ld-series/) |
| Width | 580 mm |  | [robotics.omron.com](https://robotics.omron.com/new-ld-series/) |
| Height | 320 mm |  | [robotics.omron.com](https://robotics.omron.com/new-ld-series/) |
| Weight (no battery or accessories) | 117 kg |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) · Specifications p.5 |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Maximum payload capacity | 300 kg |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Maximum translational speed (forward) | 2,100 mm/s |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Maximum translational speed (reverse) | 2,100 mm/s |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Maximum translational acceleration | 1,000 mm/s² |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Maximum translational deceleration | 1,300 mm/s² |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Maximum rotational velocity | 100 °/s | reduced to 45 °/s when travelling faster than 40 mm/s | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Maximum rotational acceleration | 250 °/s² |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Maximum moment of inertia | 32.5 kg·m² |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Swing radius | 464 mm |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Turn radius | 0 mm |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Drive wheels | Non-marking polyurethane wheels with brushless DC motors |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Passive casters | Non-marking polyurethane wheels |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Stop position repeatability (single AMR) | to a position ±70 mm, ±2.5°; to standard target ±25 mm, ±2°; with HAPS ±4 mm, ±0.25°; with CAPS ±6.5 mm, ±0.5° |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Stop position repeatability (fleet) | to a position ±80 mm, ±2.5°; to standard target ±35 mm, ±2°; with HAPS ±10 mm, ±0.5°; with CAPS ±11 mm, ±0.5° |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Minimum floor flatness | FF25 (ASTM E1155) |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Minimum floor levelness | FL15 (ASTM E1155) |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Minimum floor compressive strength | 3 MPa |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Minimum coefficient of friction | Flat surfaces 0.6; inclined surfaces 0.8 |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Maximum floor resistivity | 10^8 Ω |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Maximum step traversal | 10 mm |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Maximum gap traversal | 15 / 30 mm | 15 mm gaps at any speed; 30 mm gaps only below 500 mm/s | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Maximum slope | 5° / 8.75% incline |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Minimum aisle width | 1,000 mm | aisles as narrow as 1 m | [robotics.omron.com](https://robotics.omron.com/news/new-ld-series-amr-launch/) |
| Routing | Autonomous routing by localizing with LiDAR-based safety scanner(s), based on environment mapping | no fixed guide paths, floor markers or magnetic tape | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Map making | Scan by driving the AMR through the environment and uploading the scan data to MobilePlanner |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Run time (no payload) | 7.25 h |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Run time (full payload) | 6.5 h |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Uptime ratio (run time : charge time) | 16:1 | operating between 80% and 20% state of charge | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Battery type | Lithium-ion (LiFePO4) | battery 64090-330, ordered separately | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Battery voltage | 37 to 57 VDC | 51.2 VDC nominal | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Battery capacity | 21 Ah | nominal | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Battery energy | 1,074 Wh | nominal | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Recharge time (battery 20% to 80%) | 18 min |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Charging method | Wireless inductive charging (automatic or manual) | 30 minutes or less per press release | [robotics.omron.com](https://robotics.omron.com/news/new-ld-series-amr-launch/) |
| Charge-to-runtime ratio | 1:12 |  | [robotics.omron.com](https://robotics.omron.com/news/new-ld-series-amr-launch/) |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| Ambient temperature | 5 to 40 °C |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Storage temperature | -25 to 60 °C |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Ambient humidity | 10 to 90 % | non-condensing | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Operating environment | Indoor usage only; no corrosive or explosive gas or liquid |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Altitude | 2,000 m | above mean sea level, maximum | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Ingress protection class | IP22 | NEMA Type 2 enclosure rating | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Safety laser scanner | Two safety laser scanners, 360° detection area | Class 1/M, eye-safe, per IEC 60825-1; scanning plane 175 mm above floor | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Safety scanner field of view | 360 ° |  | [robotics.omron.com](https://robotics.omron.com/new-ld-series/) |
| Supplementary laser scanners (optional) | Optional peripheral lasers (supplementary laser kit 64090-905) |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Fleet software | OMRON FLOW Core 5 (fleets of up to 100 AMRs, mixed with LD, MD, OL and HD robots) | minimum FLOW Core 5.0 | [robotics.omron.com](https://robotics.omron.com/news/new-ld-series-amr-launch/) |
| Configuration software | MobilePlanner |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Wireless communication | IEEE 802.11 b/a/g/n/ac (encryption CCMP/AES; WPA2-PSK, PEAP-MSCHAPv2, EAP-TLS) |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| RJ-45 ports | 1 for maintenance, 2 for user-supplied devices |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Digital I/O | 16 inputs and 16 outputs, configurable PNP/sourcing or NPN/sinking |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Auxiliary power (unregulated) | 37 to 57 VDC (51.2 VDC nominal); 30 A fused |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Auxiliary power (regulated) | Two outputs at 22.8 to 25.2 VDC (24 VDC nominal); 200 mA fused |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Top modules and accessories | Cart toppers, conveyors, mobile manipulators and lifts |  | [robotics.omron.com](https://robotics.omron.com/news/new-ld-series-amr-launch/) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Cleanroom rating | ISO 5 / Class 100 | associated with AMR and charging components used together | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Standards (AMR) | EN ISO 12100; EN ISO 13849-1; EN ISO 3691-4; ANSI/RIA 15.08-1; ANSI/CAN/UL 3100; EN IEC 60204-1; KS C 9610-6-2; KS C 9610-6-4; EN IEC 61326-1; EN IEC 61326-3-1; EN ISO 12895; ISO 14664-14 |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Standards (battery) | IEC 62619; UN 38.3; ANSI/CAN/UL/ULC 2271 |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Standards (charging station) | UL1564; EN IEC 62311; EN IEC 60335-2-29; EN IEC 55011; EN IEC 61000-6-2; CAN/CSA-C22.2 NO. 107.2 |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Certification markings | AMR: KC, FCC; battery: CE; charging station: CE, cMETus |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Regulatory notes | Compliant with ISO 3691-4:2023 and Regulation (EU) 2023/1230; FCC Covered List exemption under Conditional Approval (DA 26-1181, 2026-10-30) |  | [robotics.omron.com](https://robotics.omron.com/news/new-ld-series-amr-launch/) |
| E-STOP buttons | On AMR sides; additional E-STOP buttons can be added to the payload structure |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Visual indicators | Light discs on the sides; light strips on front and back |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |
| Audible indicators | One speaker and one buzzer; volume 70 to 90 dB |  | [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Shipments begin | January 2027 |  | [robotics.omron.com](https://robotics.omron.com/news/new-ld-series-amr-launch/) |

## Documents

- [LD-150 & LD-300 datasheet M146-E-01 Rev A (OMRON, Nov 2026)](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf)
- [New LD Series page (OMRON Robotics)](https://robotics.omron.com/new-ld-series/)
- [Press release: start of orders for LD-150 and LD-300 (2026-11-18)](https://robotics.omron.com/news/new-ld-series-amr-launch/)

## Notes

Announced and opened for orders 2026-11-18 (Americas and Europe first); shipments begin January 2027. Weight 117 kg is without battery or accessories. Battery (64090-330, 1,074 Wh nominal) is ordered separately. Runtime is 6.5 h at full payload (7.25 h no payload). Full-speed reverse as standard.

## Sources

- Official page: [robotics.omron.com](https://robotics.omron.com/new-ld-series/)
- [robotics.omron.com](https://robotics.omron.com/news/new-ld-series-amr-launch/)
- [robotics.omron.com](https://robotics.omron.com/wp-content/uploads/2026/11/M146-E-01_LD-150-300_Datasheet_RevA.pdf)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-28). Source repository: https://github.com/htcrefactor/robot-catalog*
