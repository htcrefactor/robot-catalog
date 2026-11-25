# Noetix Robotics Bumi

> Noetix's small consumer humanoid, sold in China as Bumi and internationally as Boomy: 98 cm, about 17 kg, 21 DoF, 2-3 h of use, graphical coding plus an open SDK on the international edition.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=noetix-bumi
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: Noetix Robotics (China)
- Verification: official — checked against a maker source
- Data source: Maker sources (verified 2026-11-17)

## Core specs

| Field | Value |
|---|---|
| Height | 980 mm |
| Weight | 17 kg |
| Max speed | 0.5 m/s (1.8 km/h) |
| Degrees of freedom | 21 |
| Runtime | 3 h |
| Battery | 244.8 Wh |
| Status | Commercial |
| API | yes |
| SDK | yes |
| SDK name | Noetix Boomy open SDK |
| ROS | yes |
| On-board compute | yes |
| Compute | NVIDIA Jetson Orin NX (Boomy EDU) |
| Sensors | RGB camera, Intel RealSense D435i depth camera (Boomy EDU), Microphone array, Speaker |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

15 values from 1 document, checked against maker sources on 2026-11-13.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Form factor | compact | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/noetix-bumi) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Height (standing) | 98 cm | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/noetix-bumi) |
| Weight | 17 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/noetix-bumi) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total degrees of freedom | 21 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/noetix-bumi) |
| Top speed | 0.5 m/s | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/noetix-bumi) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Runtime per charge | 120 min | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/noetix-bumi) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Hands | none | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/noetix-bumi) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Sales status | shipping-now | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/noetix-bumi) |
| Who can buy | restricted | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/noetix-bumi) |
| Price | 1,400 USD | list price (maker price); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/noetix-bumi) |
| Delivered price to US | 2,322 USD | before sales tax; route: estimate: import; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/noetix-bumi) |
| Route to US | reseller | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/noetix-bumi) |
| Route to EU | no | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/noetix-bumi) |
| Sellers listed | 1 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/noetix-bumi) |
| Documented uses | Teaching / education; Learn and tinker; Demo / showpiece | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/noetix-bumi) |

## Documents

- [HumanoidStore datasheet – Noetix Robotics Bumi (CC BY 4.0)](https://humanoidstore.co/robots/noetix-bumi)

## Variants

- **Boomy (international edition)** — International, Kickstarter edition of Bumi: same 21-DoF body, launched 2026-11-24. Noetix's own Boomy page and release give 97 cm, up to 1 m/s and 2-3 h; the China Bumi page gives 98 cm, 0.5 m/s and up to 3 h. Not a separate model. ([maker page](https://boomy.noetixrobotics.com/))

## Notes

Noetix product page and WRC 2026 profile (checked 2026-11-17): 98 cm, about 17 kg, 21 DoF (6 per leg, 4 per arm, 1 waist), 0.5 m/s, 2-3 h on a 48 V 5.1 Ah quick-release pack (244.8 Wh computed as V x Ah), camera and IMU, 6 TOPS motion board. The Pro edition adds high-dynamic dance; the EDU Pro adds a Jetson Orin Nano Super. International edition (Boomy, launched 2026-11-24 on Kickstarter) per Noetix's own Boomy page and release: 97 cm, up to 1 m/s, 2-3 h, 21 DoF split as 4 per arm / 6 per leg / 1 waist, open SDK with block coding, Python and C++, ROS 2 development, EDU adds an NVIDIA Jetson Orin NX (117 TOPS) and an Intel RealSense D435i, Wi-Fi/Bluetooth/OTA, built-in ChatGPT voice AI (requires internet), 3D-printable STP shell files. The China Bumi page states 98 cm and a 0.5 m/s lower-limb travel speed; those values stay in the fields. China retail price CNY 9,998 (JD Noetix flagship store, 2026-11) is not a dated observation from a page checked here.

## Sources

- Official page: [noetixrobotics.com](http://www.noetixrobotics.com/en/detail/Bumi/)
- [webuildhumanoids.com](https://webuildhumanoids.com/compare/noetix-bumi-vs-noetix-n2)
- [noetixrobotics.com](https://www.noetixrobotics.com)
- [boomy.noetixrobotics.com](https://boomy.noetixrobotics.com/)
- [newswire.com](https://www.newswire.com/news/noetix-robotics-introduces-noetix-boomy-a-programmable-humanoid-robot-22891909)
- [kickstarter.com](https://www.kickstarter.com/projects/noetixrobotics/noetix-boomy-your-first-programmable-humanoid-robot)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-25). Source repository: https://github.com/htcrefactor/robot-catalog*
