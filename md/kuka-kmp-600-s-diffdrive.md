# KUKA KMP 600-S diffDrive

> IP54 differential-drive lifting platform KUKA markets as an AGV for 600 kg production intralogistics on laser-mapped routes.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=kuka-kmp-600-s-diffdrive
- Category: AGV
- Locomotion: Wheeled
- Manufacturer: KUKA (Germany)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 1,000 mm |
| Width | 750 mm |
| Height | 353 mm |
| Weight | 246 kg |
| Payload | 600 kg |
| Max speed | 2 m/s (7.2 km/h) |
| Runtime | 8 h |
| IP rating | IP54 |
| Status | Commercial |
| API | yes |
| Sensors | Front and rear safety laser scanners, Optional 3D obstacle detection camera |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

59 values from 3 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Model | KMP 600S-2 diffDrive |  | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Data sheet document number | 0000-406-703 / V1.1 / 27.09.2022 |  | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Manufacturer address | KUKA Deutschland GmbH, Zugspitzstrasse 140, 86165 Augsburg, Germany |  | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Robot type | Automated guided vehicle (AGV) / mobile platform with differential drive |  | [kuka.com](https://www.kuka.com/-/media/kuka-corporate/countries/nordic/documents/amr---autonomous-mobile-robotics.pdf) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 1,000 mm |  | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Width | 750 mm |  | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Height | 353 mm |  | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Wheel diameter | 250 mm |  | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Weight | approx. 264 kg | excludes optional lifting system | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Weight | 246 kg | as stated in KUKA AMR brochure | [kuka.com](https://www.kuka.com/-/media/kuka-corporate/countries/nordic/documents/amr---autonomous-mobile-robotics.pdf) |
| Permissible total weight | 880 kg |  | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Rated payload | 600 kg |  | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Travel speed, longitudinal | 2 m/s | without load; full speed in all directions per brochure | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Travel speed, longitudinal | 1.5 m/s | with load | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Rotational velocity | 0.37 rad/s | turning on the spot | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Maximum acceleration | 0.75 m/s² | data sheet; brochure states 1.25 m/s² | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Maximum acceleration | 1.25 m/s² | as stated in KUKA AMR brochure | [kuka.com](https://www.kuka.com/-/media/kuka-corporate/countries/nordic/documents/amr---autonomous-mobile-robotics.pdf) |
| Maximum braking deceleration | 1.25 m/s² | data sheet; brochure states 1.5 m/s² | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Maximum braking deceleration | 1.5 m/s² | as stated in KUKA AMR brochure | [kuka.com](https://www.kuka.com/-/media/kuka-corporate/countries/nordic/documents/amr---autonomous-mobile-robotics.pdf) |
| Pose accuracy | ±10 mm | line-guided motion: ±10 mm X/Y, ±0.5° theta | [kuka.com](https://www.kuka.com/-/media/kuka-corporate/countries/nordic/documents/amr---autonomous-mobile-robotics.pdf) |
| Pose accuracy, orientation | ±0.5 ° | line-guided motion | [mav.industrie.de](https://mav.industrie.de/wp-content/uploads/2/3/230322_MAV-Final.pdf) |
| Drive | Differential drive |  | [mav.industrie.de](https://mav.industrie.de/wp-content/uploads/2/3/230322_MAV-Final.pdf) |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Maximum height of floor irregularities | 5 mm |  | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Maximum gap width | 35 mm |  | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Maximum track gradient | 3 % | at max payload | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Required floor strength | C 30/37 concrete grade |  | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Navigation | SLAM navigation based on laser scanners and pre-generated environment map |  | [mav.industrie.de](https://mav.industrie.de/wp-content/uploads/2/3/230322_MAV-Final.pdf) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Number of batteries | 1 |  | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Battery voltage (DC) | 51.1 V | 48 VDC nominal per KUKA presentation | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Capacity per battery | 35 Ah |  | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Battery type | Lithium-ion |  | [mav.industrie.de](https://mav.industrie.de/wp-content/uploads/2/3/230322_MAV-Final.pdf) |
| Operating time | 8 h | at SoH 100%, standard motion operation | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charging time | 1.5 h | SoC 0% to 100% | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Charging time | 2 hours | as stated in KUKA AMR brochure | [kuka.com](https://www.kuka.com/-/media/kuka-corporate/countries/nordic/documents/amr---autonomous-mobile-robotics.pdf) |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| Protection rating (IEC 60529) | IP54 | without 3D camera | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Air humidity | 5–95 % |  | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Ambient temperature during operation | 0 to 45 °C | 273 K to 318 K | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Ambient temperature during storage/transport | 0 to 45 °C |  | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Laser scanners | 2 (front and rear) |  | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| 3D cameras (optional) | 2 | front and rear, optional | [mav.industrie.de](https://mav.industrie.de/wp-content/uploads/2/3/230322_MAV-Final.pdf) |
| 3D obstacle detection height range | 30 mm to 2.10 m above ground | optional 3D object detection | [kuka.com](https://www.kuka.com/-/media/kuka-corporate/countries/nordic/documents/amr---autonomous-mobile-robotics.pdf) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Programming | Java |  | [kuka.com](https://www.kuka.com/-/media/kuka-corporate/countries/nordic/documents/amr---autonomous-mobile-robotics.pdf) |
| Fleet management | Fleet manager software for the entire KUKA AGV portfolio |  | [kuka.com](https://www.kuka.com/-/media/kuka-corporate/countries/nordic/documents/amr---autonomous-mobile-robotics.pdf) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Interfaces | 48 VDC, 24 VDC, EtherCAT, I/O, STO |  | [kuka.com](https://www.kuka.com/-/media/kuka-corporate/countries/nordic/documents/amr---autonomous-mobile-robotics.pdf) |
| EtherCAT | yes |  | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| PROFINET | no |  | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Lift height | 60 mm | optional lifting system | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Duration of lifting cycle | 4.4 s | data sheet; brochure: up to 60 mm in under 3 s | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Lift position sensing system | yes |  | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Logic power supply | 24 V / 7.5 A |  | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Application power supply | 48 V / 15 A |  | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Sound level | < 75 dB(A) |  | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Emergency stops on vehicle | 4 |  | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Safety zones | 8 configurable safety zones front and rear; protective field adapts to speed and direction |  | [kuka.com](https://www.kuka.com/-/media/kuka-corporate/countries/nordic/documents/amr---autonomous-mobile-robotics.pdf) |
| Safety category / performance level | Category 3 / PL d |  | [mav.industrie.de](https://mav.industrie.de/wp-content/uploads/2/3/230322_MAV-Final.pdf) |
| Certification | UL certificate from TÜV Rheinland; FCC option |  | [mav.industrie.de](https://mav.industrie.de/wp-content/uploads/2/3/230322_MAV-Final.pdf) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Manual control | Wireless controller for commissioning; manual control for trained personnel only |  | [kuka.com](https://www.kuka.com/-/media/kuka-corporate/countries/nordic/documents/amr---autonomous-mobile-robotics.pdf) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Optical signal | LED strip |  | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |
| Acoustic signal | yes | reduced speed and acoustic alarm when reversing | [5.imimg.com](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf) |

## Documents

- [KMP 600S-2 diffDrive data sheet 0000-406-703 V1.1 (KUKA, 2022, reseller-hosted)](http://5.imimg.com/data5/SELLER/Doc/2024/7/432594759/YF/ZB/DY/111358936/kuka-agv-kmp-600-2.pdf)
- [AMR – Autonomous mobile robotics brochure (KUKA Nordic)](https://www.kuka.com/-/media/kuka-corporate/countries/nordic/documents/amr---autonomous-mobile-robotics.pdf)
- [KUKA Mobile Robotics presentation, 23.03.2023 (MAV conference)](https://mav.industrie.de/wp-content/uploads/2/3/230322_MAV-Final.pdf)

## Notes

Checked 2026-11-19 against the KUKA AMR brochure: 1,000x750x353 mm, 246 kg, 600 kg rated payload, 2 m/s, battery at least 8 h all match.

## Sources

- Official page: [kuka.com](https://www.kuka.com/en-gb/products/amr-autonomous-mobile-robotics/mobile-platforms/kmp-600-s-diffdrive)
- [kuka.com](https://www.kuka.com/-/media/kuka-corporate/countries/nordic/documents/amr---autonomous-mobile-robotics.pdf)
- [kuka.com](https://www.kuka.com/ko-kr/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-20). Source repository: https://github.com/htcrefactor/robot-catalog*
