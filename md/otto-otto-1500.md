# OTTO by Rockwell Automation (formerly OTTO Motors / Clearpath) OTTO 1500

> Heavy-duty AMR for pallet-sized loads up to 1,900 kg (capacity includes attachment) in demanding plants.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=otto-otto-1500
- Category: AMR
- Locomotion: Wheeled
- Manufacturer: OTTO by Rockwell Automation (formerly OTTO Motors / Clearpath) (United States)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 1,837 mm |
| Width | 1,283 mm |
| Height | 351 mm |
| Weight | 627 kg |
| Payload | 1,900 kg |
| Max speed | 2 m/s (7.2 km/h) |
| Runtime | 10 h |
| Battery | 4,224 Wh |
| IP rating | IP20 |
| Status | Commercial |
| Compute | Solid-state military-spec computer with dedicated GPU |
| Sensors | 4x Intel RealSense cameras, 2x SICK microScan3 safety laser scanners (360°), 6-axis IMU |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

61 values from 3 documents, checked against maker sources on 2026-11-22.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Spec sheet number | OTTO-DS001F-EN-AUG2026 |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Robot type | Heavy-duty autonomous mobile robot (AMR) |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Manufacturer | OTTO by Rockwell Automation |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Earlier version | OTTO 1500 v2 (Clearpath Robotics, 2021 data sheet) |  | [s3.amazonaws.com](https://s3.amazonaws.com/assets.ottomotors.com/pdf/OTTO1500-v2-Datasheet-210406_eng.pdf) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 1,837 mm |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Width | 1,283 mm |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Height | 351 mm |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Mass | 627 kg | 1,382 lb | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Turning radius | Turn in place |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Ground clearance | 16 mm | 0.625 in | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Ground clearance | 37.5 mm | v2 (2021) | [s3.amazonaws.com](https://s3.amazonaws.com/assets.ottomotors.com/pdf/OTTO1500-v2-Datasheet-210406_eng.pdf) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Maximum capacity | 1,900 kg | includes payload and attachment, if any | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Maximum speed | 2 m/s | 4.5 mph | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Maximum turning speed | 1.5 rad/s | 90°/s | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Maximum docking speed | 0.3 m/s | 0.7 mph | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Docking accuracy (standard) | ±10 mm (x,y); ±1° (yaw) | repeatable to 3σ | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Docking accuracy (precision upgrade) | ±5 mm (x,y); ±1° (yaw) | requires OTTO High Accuracy Docking System (HADS), sold separately | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Suspension | Passive, rocker |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Minimum aisle width (one way) | 2,209 mm | no payload (87 in); 1915 mm in earlier sheets | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Minimum aisle width (two way) | 3,570 mm | no payload (146 in) | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Traversable gap | 16 mm | 0.625 in | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Traversable gap | 31 mm | v2 (2021) | [s3.amazonaws.com](https://s3.amazonaws.com/assets.ottomotors.com/pdf/OTTO1500-v2-Datasheet-210406_eng.pdf) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery capacity | 80 Ah |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Battery capacity | 70 Ah | v2 (2021) | [s3.amazonaws.com](https://s3.amazonaws.com/assets.ottomotors.com/pdf/OTTO1500-v2-Datasheet-210406_eng.pdf) |
| Battery voltage | 52.8 V |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Runtime | 10 h | 90% to 10% | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Battery life | 3,000 cycles | full charge cycles | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Battery life | 10,000 cycles | v2 (2021); est. battery replacements over 5 yr: 0 | [s3.amazonaws.com](https://s3.amazonaws.com/assets.ottomotors.com/pdf/OTTO1500-v2-Datasheet-210406_eng.pdf) |
| Battery type | Lithium-ion | Product page "Behind the Chassis" | [ottomotors.com](https://ottomotors.com/1500) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Maximum charge rate | 80 A |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Maximum charge rate | 98 A | v2 (2021) | [s3.amazonaws.com](https://s3.amazonaws.com/assets.ottomotors.com/pdf/OTTO1500-v2-Datasheet-210406_eng.pdf) |
| Charge time | 60 min | 10% to 90% | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Charge time | 34 min | 10% to 90%, v2 (2021) | [s3.amazonaws.com](https://s3.amazonaws.com/assets.ottomotors.com/pdf/OTTO1500-v2-Datasheet-210406_eng.pdf) |
| Battery charging options | Autonomous opportunity charging (default); manual charging |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Opportunity charging | yes | autonomous, default | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Charging time | 60 minutes | Charge time 10% to 90% (product page key specifications) | [ottomotors.com](https://ottomotors.com/1500) |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| IP classification | IP20 |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Ambient temperature | 0 to 40 °C |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Humidity | 10–95 % | non-condensing | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Depth cameras | 4 | Intel RealSense | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Camera model | Intel RealSense |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Safety laser scanners | 2× SICK microScan3 (360° FOV) |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| IMU | Embedded 6-axis IMU |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Camera | 4 x 3D cameras: two forward-facing, two rear-facing | Product page "Behind the Chassis" | [ottomotors.com](https://ottomotors.com/1500) |
| LiDAR | 2 corner LiDARs giving a 360° field of view | Product page "Behind the Chassis" | [ottomotors.com](https://ottomotors.com/1500) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Computer | Solid-state military-spec computer with dedicated GPU |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| CPU | Intel i7-6700TE quad core | v2 (2021) | [s3.amazonaws.com](https://s3.amazonaws.com/assets.ottomotors.com/pdf/OTTO1500-v2-Datasheet-210406_eng.pdf) |
| RAM | 16 GB | v2 (2021) | [s3.amazonaws.com](https://s3.amazonaws.com/assets.ottomotors.com/pdf/OTTO1500-v2-Datasheet-210406_eng.pdf) |
| GPU | NVIDIA GTX 1050 | v2 (2021) | [s3.amazonaws.com](https://s3.amazonaws.com/assets.ottomotors.com/pdf/OTTO1500-v2-Datasheet-210406_eng.pdf) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Signal interface | 1× Ethernet, 1× USB 3.1, 1× HDMI, 1 CAN bus, 5 GPIO (2 safety rated), 1 interface control line |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Safety interface | Dual-channel E-stop breakout, 2 safety-rated GPIO, 1 attachment interface fault line |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Wi-Fi | 2.4 / 5 GHz (802.11 a/b/g/n/ac) | 2× long-range omnidirectional antennae | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Power interface | 24 VDC, 10 A, regulated, unswitched; 52.8 VDC nominal, 50 A, unregulated |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Intelligent braking | Redundant monitoring with safety-system interlock |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Adaptive fieldsets | Intelligent PL d rated switching fieldsets (patent-pending) |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Performance level (fieldset switching) | PL d |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| E-stop | 4 E-stops (1 per side) + user E-stop circuit interface |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Standards compliance | CE marked; ANSI/ITSDF B56.5; RIA R15.08-1; ISO 12100/13849-1/3691-4; FCC Part 15 Subpart B / ICES-003; ICES-002; EN 1175-1/60204-1 |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Manual control | Pendant-based manual control; guided autonomous control via OTTO software interface |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Charging accessories (sold separately) | Autonomous Supercharger (80 A); Manual Trickle Charger (25 A) |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=) |
| Load-handling accessories (v2) | 1500 kg hydraulic lift; 1500 kg in-line conveyor; 1900 kg load plate |  | [s3.amazonaws.com](https://s3.amazonaws.com/assets.ottomotors.com/pdf/OTTO1500-v2-Datasheet-210406_eng.pdf) |

## Documents

- [OTTO 1500 Spec Sheet OTTO-DS001F-EN-AUG2026 (OTTO by Rockwell Automation)](https://cdn.sanity.io/files/armc7p5y/production/65f37f30ec55c632329ba48e31cb7013ca96c80d.pdf?dl=)
- [OTTO 1500 v2 Data Sheet 210406 (Clearpath/OTTO Motors)](https://s3.amazonaws.com/assets.ottomotors.com/pdf/OTTO1500-v2-Datasheet-210406_eng.pdf)
- [OTTO 1500 product page (checked 2026-11-22)](https://ottomotors.com/1500)

## Notes

Checked 2026-11-22 against ottomotors.com/1500 and its data sheet: 1,900 kg payload, 10 h runtime (90% to 10%), 60 min charge (10% to 90%) and the standards list match the record.

## Sources

- Official page: [ottomotors.com](https://ottomotors.com/1500)
- [rockwellautomation.com](https://www.rockwellautomation.com/content/dam/rockwell-automation/documents/pdf/events/automate/otto-1500-data-sheet.pdf)
- [s3.amazonaws.com](https://s3.amazonaws.com/assets.ottomotors.com/pdf/OTTO1500-v2-Datasheet-210406_eng.pdf)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-28). Source repository: https://github.com/htcrefactor/robot-catalog*
