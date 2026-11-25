# OTTO by Rockwell Automation (formerly OTTO Motors / Clearpath) OTTO 100

> Compact all-metal AMR with an integrated lift for moving boxes, bins and carts up to 150 kg in manufacturing.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=otto-otto-100
- Category: AMR
- Locomotion: Wheeled
- Manufacturer: OTTO by Rockwell Automation (formerly OTTO Motors / Clearpath) (United States)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 740 mm |
| Width | 550 mm |
| Height | 308 mm |
| Weight | 107 kg |
| Payload | 150 kg |
| Max speed | 2 m/s (7.2 km/h) |
| Runtime | 6 h |
| Battery | 924 Wh |
| IP rating | IP20 |
| Status | Commercial |
| Sensors | Hokuyo safety laser scanner, 3D camera (90° front), ToF rear sensor (90°), Inductive cart-detect sensor |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

51 values from 3 documents, checked against maker sources on 2026-11-22.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Spec sheet number | OTTO-DS001F-EN-MAR2026 |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Robot type | Autonomous mobile robot (AMR) for boxes, bins and carts |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Manufacturer | OTTO by Rockwell Automation |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Earlier version | OTTO 100 v2.5 (Clearpath Robotics, 2022 data sheet) |  | [amrobotics.eu](https://www.amrobotics.eu/wp-content/uploads/2022/12/OTTO-100-v2.5-Data-Sheet-3.pdf) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 740 mm |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Width | 550 mm |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Height | 308 mm |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Mass | 107 kg | 236 lb | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Turning radius | Turn in place |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Ground clearance | 6 mm | 0.25 in | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Maximum capacity | 150 kg | includes payload, attachments and cart, if any | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Maximum speed | 2 m/s | 4.5 mph | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Maximum turning speed | 1.25 rad/s | 75°/s | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Maximum docking speed | 0.3 m/s | 0.7 mph | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Docking precision (standard) | ±10 mm (x,y); ±1° (yaw) | see OMM; v2.5 sheet: repeatable to 3σ | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Docking precision (upgrade) | ±5 mm (x,y); ±1° (yaw) | requires OTTO High Accuracy Docking System (HADS), sold separately | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Suspension | Fixed, rigid |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Minimum aisle width (one way) | 1,099 mm | 43 in | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Minimum aisle width (two way) | 1,975 mm | 78 in | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Floor obstacle | 13 mm | 0.5 in | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Traversable gap | 13 mm | v2.5 data sheet | [amrobotics.eu](https://www.amrobotics.eu/wp-content/uploads/2022/12/OTTO-100-v2.5-Data-Sheet-3.pdf) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery capacity | 35 Ah |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Battery capacity | 40 Ah | v2.5 (2022) | [amrobotics.eu](https://www.amrobotics.eu/wp-content/uploads/2022/12/OTTO-100-v2.5-Data-Sheet-3.pdf) |
| Battery voltage | 26.4 V |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Runtime | 6 h | 90% to 10% | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Battery life | 10,000 cycles | full charge cycles | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Battery life | 3,000 cycles | v2.5 (2022) | [amrobotics.eu](https://www.amrobotics.eu/wp-content/uploads/2022/12/OTTO-100-v2.5-Data-Sheet-3.pdf) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Maximum charge rate | 98 A |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Maximum charge rate | 40 A | v2.5 (2022) | [amrobotics.eu](https://www.amrobotics.eu/wp-content/uploads/2022/12/OTTO-100-v2.5-Data-Sheet-3.pdf) |
| Charge time | 18 min | 10% to 90% | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Charge time | 60 min | 10% to 90%, v2.5 (2022) | [amrobotics.eu](https://www.amrobotics.eu/wp-content/uploads/2022/12/OTTO-100-v2.5-Data-Sheet-3.pdf) |
| Battery charging options | Autonomous opportunity charging (default); manual charging |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Opportunity charging | yes | autonomous, default | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| IP classification | IP20 |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Temperature | 20 to 40 °C | as printed on spec sheet | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Humidity | 0–95 % | non-condensing | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Safety laser scanner | Hokuyo safety laser scanner |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| 3D camera | 3D camera with 90° front coverage |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Rear ToF sensor | ToF rear sensor with 90° reverse coverage |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Cart detect sensor | Inductive cart detect sensor |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Signal interface | 1× Ethernet, 1× USB 3.0, 1× serial RS-232 |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Safety interface | 2× E-stop extension, 8× digital IO, 2× dry-contact relays, 1× auxiliary monitor contact |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Wi-Fi | 2.4 / 5 GHz (802.11 a/b/g/n/ac) |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Integrated lift | 62 mm stroke, 150 kg capacity |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Lift stroke | 62 mm |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Power interface | 26.4 VDC, 12 A max, unregulated |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| E-stop | 2 E-stops (front and back) + user E-stop circuit interface |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Standards compliance | CE marked; ANSI/ITSDF B56.5; RIA R15.08-1; ISO 12100/13849-1/3691-4; FCC Part 15 Subpart B / ICES-003; ICES-002; EN 1175-1/60204-1 |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Manual control | Guided autonomous control via OTTO software interface |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Charging accessories (sold separately) | Autonomous Supercharger (98 A); Manual Trickle Charger (25 A) |  | [cdn.sanity.io](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=) |
| Load-handling accessories (v2.5) | Staging Cart (130 kg); Magnetic Line Follower |  | [amrobotics.eu](https://www.amrobotics.eu/wp-content/uploads/2022/12/OTTO-100-v2.5-Data-Sheet-3.pdf) |

## Documents

- [OTTO 100 Spec Sheet OTTO-DS001F-EN-MAR2026 (OTTO by Rockwell Automation)](https://cdn.sanity.io/files/armc7p5y/production/ec1dac3528cb906c23589c86c036b565f27e36cf.pdf?dl=)
- [OTTO 100 v2.5 Data Sheet (Clearpath, 2022, distributor-hosted)](https://www.amrobotics.eu/wp-content/uploads/2022/12/OTTO-100-v2.5-Data-Sheet-3.pdf)
- [OTTO 100 product page (checked 2026-11-22)](https://ottomotors.com/100/)

## Notes

Checked 2026-11-22 against ottomotors.com/100 and its data sheet: 150 kg payload and the standards/marks list match the record.

## Sources

- Official page: [ottomotors.com](https://ottomotors.com/100/)
- [rockwellautomation.com](https://www.rockwellautomation.com/content/dam/rockwell-automation/documents/pdf/events/automate/otto-100-datasheet.pdf)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-24). Source repository: https://github.com/htcrefactor/robot-catalog*
