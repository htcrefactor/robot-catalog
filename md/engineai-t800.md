# EngineAI T800

> EngineAI's heavy-duty industrial humanoid with 450 N.m leg joints and an active-cooled leg for sustained work, sold in Basic, Open Source, Pro and Max editions.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=engineai-t800
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: EngineAI (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Height | 1,730 mm |
| Weight | 85 kg |
| Max speed | 3 m/s (10.8 km/h) |
| Degrees of freedom | 29 |
| Runtime | 2 h |
| Battery | 1,220 Wh |
| Status | Commercial |
| Price | list 25000 USD, per HumanoidStore (maker publishes no list price), checked 2026-10 |
| API | yes |
| SDK | yes |
| SDK name | EngineAI open platform SDK/API (T800 docs) |
| On-board compute | yes |
| Compute | 8-core CPU base (NEZHA module) plus NVIDIA Jetson AGX Orin 64GB, 256 GB SSD |
| Sensors | Self-developed stereo camera (head), 3D LiDAR |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

14 values from 1 document, checked against maker sources on 2026-11-13.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Form factor | full-size | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-t800) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Height (standing) | 173 cm | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-t800) |
| Weight | 75 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-t800) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total degrees of freedom | 25 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-t800) |
| Top speed | 2 m/s | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-t800) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Runtime per charge | 240 min | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-t800) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Hands | optional | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-t800) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Sales status | shipping-now | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-t800) |
| Who can buy | anyone | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-t800) |
| Price | 25,000 USD | list price (maker price); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-t800) |
| Route to US | unclear | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-t800) |
| Route to EU | unclear | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-t800) |
| Sellers listed | 2 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-t800) |
| Documented uses | Demo / showpiece | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/engineai-t800) |

## Documents

- [HumanoidStore datasheet – EngineAI T800 (CC BY 4.0)](https://humanoidstore.co/robots/engineai-t800)

## Notes

Maker product page and open-platform documentation: 173 cm, 75-85 kg by configuration (84.5 kg with battery as the Developer Edition), 25 DoF in the basic edition (5 per arm, 6 per leg, 1 waist, 2 neck) rising to 43 (Pro) and 46 (Max) with 7-DoF dexterous hands, leg joint peak torque 450 N.m, forward walking 0-1.5 m/s with hardware supporting up to <3 m/s, 20 cm steps and 20 deg slopes, 1.22 kWh ternary lithium battery with 2 h standard runtime and 2.5 h charging, AGX Orin 64GB with 256 GB SSD, stereo camera plus 3D LiDAR, secondary development supported. The marketing page quotes 3-5 h battery life while the documentation states 2 h standard - documentation value recorded and the range noted. Maker publishes no list price, so the HumanoidStore figure stands with its own label.

## Sources

- Official page: [en.engineai.com.cn](https://en.engineai.com.cn/product-t800)
- [en.engineai.com.cn](https://en.engineai.com.cn/open/docs/t800/t800/robot-specifications-electrical-interfaces)
- [humanoidstore.co](https://humanoidstore.co/robots/engineai-t800)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-27). Source repository: https://github.com/htcrefactor/robot-catalog*
