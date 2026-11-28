# Booster Robotics T2

> Booster Robotics' 1.4 m flagship embodied-development humanoid (31 DoF, 3 m/s walking, 375 TOPS) sold with an education configuration.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=booster-t2
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: Booster Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Height | 1,400 mm |
| Weight | 42 kg |
| Payload | 10 kg |
| Max speed | 3 m/s (10.8 km/h) |
| Degrees of freedom | 31 |
| Runtime | 2 h |
| Battery | 480 Wh |
| Status | Commercial |
| On-board compute | yes |
| Compute | High-performance ARM processor, 375 TOPS AI compute |
| Sensors | Binocular camera (head), Binocular camera (waist), Microphone array, Speaker, LiDAR (optional) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

38 values from 3 documents, checked against maker sources on 2026-11-14.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Form factor | mid-size | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t2) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Height (standing) | 140 cm | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t2) |
| Weight | 42 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t2) |
| Height (standing) | 1.4 m | approx. (Booster) | [docs.booster.tech](https://docs.booster.tech/zh-CN/docs/product-manual/t2/getting-started/specifications) |
| Weight | 42 kg | approx.; E1/P1 base config; gripper/dexterous-hand versions ~43 kg | [docs.booster.tech](https://docs.booster.tech/zh-CN/docs/product-manual/t2/getting-started/specifications) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total degrees of freedom | 31 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t2) |
| Top speed | 3 m/s | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t2) |
| Total degrees of freedom | 31 | base config (Booster) | [docs.booster.tech](https://docs.booster.tech/zh-CN/docs/product-manual/t2/getting-started/specifications) |
| Max payload | 10 kg | varies significantly with arm posture | [docs.booster.tech](https://docs.booster.tech/zh-CN/docs/product-manual/t2/getting-started/specifications) |
| Top speed | 3 m/s | maker spec | [docs.booster.tech](https://docs.booster.tech/zh-CN/docs/product-manual/t2/getting-started/specifications) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Runtime per charge | 120 min | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t2) |
| Battery voltage | 48 V |  | [docs.booster.tech](https://docs.booster.tech/zh-CN/docs/product-manual/t2/getting-started/specifications) |
| Battery capacity | 10 Ah |  | [docs.booster.tech](https://docs.booster.tech/zh-CN/docs/product-manual/t2/getting-started/specifications) |
| Runtime per charge | 2 h | continuous walking | [docs.booster.tech](https://docs.booster.tech/zh-CN/docs/product-manual/t2/getting-started/specifications) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| AI compute | 375 TOPS | Education edition: high-performance ARM processor | [docs.booster.tech](https://docs.booster.tech/zh-CN/docs/product-manual/t2/getting-started/specifications) |
| Chipset | NVIDIA Jetson Thor T5000 (2070 TFLOPS AI) | Professional edition | [docs.booster.tech](https://docs.booster.tech/zh-CN/docs/product-manual/t2/getting-started/specifications) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Wi-Fi | Wi-Fi 6 |  | [docs.booster.tech](https://docs.booster.tech/zh-CN/docs/product-manual/t2/getting-started/specifications) |
| Bluetooth | Bluetooth 5.2 |  | [docs.booster.tech](https://docs.booster.tech/zh-CN/docs/product-manual/t2/getting-started/specifications) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Hands | optional | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t2) |

### Actuation & Joints

| Spec | Value | Note | Source |
|---|---|---|---|
| DoF per leg | 6 |  | [docs.booster.tech](https://docs.booster.tech/zh-CN/docs/product-manual/t2/getting-started/specifications) |
| DoF per arm | 7 |  | [docs.booster.tech](https://docs.booster.tech/zh-CN/docs/product-manual/t2/getting-started/specifications) |
| Waist DoF | 3 |  | [docs.booster.tech](https://docs.booster.tech/zh-CN/docs/product-manual/t2/getting-started/specifications) |
| Head DoF | 2 |  | [docs.booster.tech](https://docs.booster.tech/zh-CN/docs/product-manual/t2/getting-started/specifications) |
| Max joint torque | 140 N·m |  | [docs.booster.tech](https://docs.booster.tech/zh-CN/docs/product-manual/t2/getting-started/specifications) |
| Joint output bearing | Industrial-grade crossed roller bearings |  | [docs.booster.tech](https://docs.booster.tech/zh-CN/docs/product-manual/t2/getting-started/specifications) |
| Motor | High-speed internal-rotor PMSM |  | [docs.booster.tech](https://docs.booster.tech/zh-CN/docs/product-manual/t2/getting-started/specifications) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Sales status | shipping-now | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t2) |
| Who can buy | anyone | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t2) |
| Price | 27,060 EUR | list price (reseller price); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t2) |
| Price (USD equivalent) | 37,999 USD | EUR list price at ECB reference rate; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t2) |
| Delivered price to US | 37,999 USD | before sales tax; route: seller: Maverick Drone; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t2) |
| Delivered price to Germany | 26,835 EUR | incl. 19% VAT; route: seller: Generation Robots; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t2) |
| Route to US | reseller | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t2) |
| Route to EU | reseller | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t2) |
| Sellers listed | 3 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t2) |
| Documented uses | Robotics R&D; Teaching / education; Learn and tinker; Demo / showpiece | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t2) |
| Warranty | 1 year | extended warranty available | [docs.booster.tech](https://docs.booster.tech/zh-CN/docs/product-manual/t2/getting-started/specifications) |

### Payload

| Spec | Value | Note | Source |
|---|---|---|---|
| Rated payload | 10 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/booster-t2) |

## Documents

- [HumanoidStore datasheet – Booster Robotics T2 (CC BY 4.0)](https://humanoidstore.co/robots/booster-t2)
- [Booster T2 product page](https://www.booster.tech/booster-t2/)
- [Booster T2 manual: specifications](https://docs.booster.tech/zh-CN/docs/product-manual/t2/getting-started/specifications)

## Notes

Maker product page (booster.tech/booster-t2, Specifications tab): standing height ~1.4 m (140 cm), weight ~42 kg, 31 DoF (6 per leg, 7 per arm, 3 waist, 2 head), max dual-arm payload 10 kg, max peak torque 140 N.m, walking speed 3 m/s, battery 48 V 10 Ah with 2 h of continuous walking (battery_wh = 48x10 = 480 Wh, computed), magnetic charging port that allows charging while in use, 375 TOPS ARM compute, head and waist binocular cameras, optional wrist camera, mic array + speaker, Wi-Fi 6 / BT 5.2, optional LiDAR. payload_kg is the maker's maximum dual-arm payload, not a whole-body rated load. Maker publishes no runtime figure beyond the walking 2 h, no IP rating and no price; price is the HumanoidStore reseller figure.

## Sources

- Official page: [booster.tech](https://www.booster.tech/booster-t2/)
- [docs.booster.tech](https://docs.booster.tech/zh-CN/docs/product-manual/t2/getting-started/specifications)
- [humanoidstore.co](https://humanoidstore.co/robots/booster-t2)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-28). Source repository: https://github.com/htcrefactor/robot-catalog*
