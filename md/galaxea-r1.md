# Galaxea Dynamics R1

> Galaxea's wheeled dual-arm research platform: the R1 Pro pairs a 6-DoF omni chassis with two 7-DoF arms and a 4-DoF torso for real-world data collection and embodied AI.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=galaxea-r1
- Category: Humanoid
- Locomotion: Wheeled
- Manufacturer: Galaxea Dynamics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Width | 675 mm |
| Height | 1,700 mm |
| Weight | 126 kg |
| Payload | 5 kg |
| Degrees of freedom | 26 |
| Battery | 1,680 Wh |
| Status | Commercial |
| Price | US$39,999 (R1 series price on the maker's product page, direct purchase not enabled) |
| SDK | yes |
| On-board compute | yes |
| Compute | NVIDIA Jetson AGX Orin 32GB (200 TOPS), 1 TB SSD |
| Sensors | 2 monocular cameras (head), 2 optional wrist cameras, 2 IMU (chest, chassis), 360-degree LiDAR (chassis) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

16 values from 1 document, checked against maker sources on 2026-11-13.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Form factor | wheeled (bimanual torso on a wheeled base) | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galaxea-r1) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Height (standing) | 170 cm | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galaxea-r1) |
| Weight | 96 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galaxea-r1) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total degrees of freedom | 24 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galaxea-r1) |
| Top speed | 1.5 m/s | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galaxea-r1) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Hands | optional | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galaxea-r1) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Sales status | shipping-now | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galaxea-r1) |
| Who can buy | business | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galaxea-r1) |
| Price | 44,500 USD | list price (maker price); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galaxea-r1) |
| Delivered price to US | 63,882 USD | before sales tax; route: estimate: import; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galaxea-r1) |
| Delivered price to Germany | 49,646 EUR | incl. 19% VAT; route: estimate: import; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galaxea-r1) |
| Route to US | reseller | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galaxea-r1) |
| Route to EU | reseller | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galaxea-r1) |
| Sellers listed | 4 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galaxea-r1) |
| Documented uses | Robotics R&D; Manipulation research | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galaxea-r1) |

### Payload

| Spec | Value | Note | Source |
|---|---|---|---|
| Rated payload | 3.5 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/galaxea-r1) |

## Documents

- [HumanoidStore datasheet – Galaxea Dynamics R1 (CC BY 4.0)](https://humanoidstore.co/robots/galaxea-r1)

## Notes

Maker product page and documentation (R1 series, R1 Pro 2026): the record describes the R1 Pro variant - 1700 x 675 x 126 mm, 126 kg with battery, 26 DoF (7 per arm, 1 gripper, 4 torso, 6 chassis), 3.5 kg rated / 5 kg peak payload per arm at 0.6 m, 0-2000 mm vertical workspace, chassis 1.5 m/s omni-directional, 48 V 35 Ah battery (1680 Wh), NVIDIA Jetson AGX Orin 32GB at 200 TOPS with 1 TB SSD, two head monocular cameras, optional wrist depth/fisheye cameras, chest and chassis IMUs and a 360-degree LiDAR. The same page lists the smaller R1 Lite (1281 x 596 x 670 mm, 96 kg, 23+ DoF, 6-DoF arms, Intel i9-12900HK). The page shows USD 39,999 for the series but states the product is not currently available for direct purchase; the earlier HumanoidStore figure was 44,500.

## Sources

- Official page: [galaxea-dynamics.com](https://galaxea-dynamics.com/products/galaxea-r1-series-pioneering-wheeled-dual-arm-robotics)
- [galaxea-ai.com](https://www.galaxea-ai.com/en/product2.html)
- [docs.galaxea-dynamics.com](https://docs.galaxea-dynamics.com/R1Pro/en/docs/2026/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-22). Source repository: https://github.com/htcrefactor/robot-catalog*
