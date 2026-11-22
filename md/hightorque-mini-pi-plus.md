# HighTorque Robotics Mini Pi Plus

> HighTorque's 680 mm, 22-DoF research humanoid kit with self-designed servo joint modules, sold as Base (RK3588) and Pro (Jetson Orin NX) configurations.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=hightorque-mini-pi-plus
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: HighTorque Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Height | 680 mm |
| Weight | 15.4 kg |
| Payload | 10 kg |
| Max speed | 1.1 m/s (4.0 km/h) |
| Degrees of freedom | 22 |
| Runtime | 1 h |
| Battery | 97.2 Wh |
| Status | Commercial |
| Price | US$6,000 (Base US$6,000; Pro US$8,000) |
| SDK | yes |
| SDK name | HighTorque SDK |
| ROS | ROS 1 |
| On-board compute | RK3588 (Base) / NVIDIA Jetson Orin NX (Pro) |
| Sensors | Intel RealSense D435i depth camera (Pro), 8-array microphone, Speaker |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

16 values from 1 document, checked against maker sources on 2026-11-13.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Form factor | compact | configuration: Base (RK3588); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/hightorque-mini-pi-plus) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Height (standing) | 68 cm | configuration: Base (RK3588); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/hightorque-mini-pi-plus) |
| Weight | 15.4 kg | configuration: Base (RK3588); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/hightorque-mini-pi-plus) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total degrees of freedom | 22 | configuration: Base (RK3588); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/hightorque-mini-pi-plus) |
| Top speed | 1.1 m/s | configuration: Base (RK3588); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/hightorque-mini-pi-plus) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Runtime per charge | 60 min | configuration: Base (RK3588); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/hightorque-mini-pi-plus) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Hands | none | configuration: Base (RK3588); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/hightorque-mini-pi-plus) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Sales status | shipping-now | configuration: Base (RK3588); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/hightorque-mini-pi-plus) |
| Who can buy | anyone | configuration: Base (RK3588); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/hightorque-mini-pi-plus) |
| Price | 6,000 USD | configuration: Base (RK3588); list price (maker price); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/hightorque-mini-pi-plus) |
| Delivered price to US | 8,733 USD | configuration: Base (RK3588); before sales tax; route: estimate: import; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/hightorque-mini-pi-plus) |
| Delivered price to Germany | 6,825 EUR | configuration: Base (RK3588); incl. 19% VAT; route: estimate: import; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/hightorque-mini-pi-plus) |
| Route to US | direct | configuration: Base (RK3588); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/hightorque-mini-pi-plus) |
| Route to EU | direct | configuration: Base (RK3588); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/hightorque-mini-pi-plus) |
| Sellers listed | 2 | configuration: Base (RK3588); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/hightorque-mini-pi-plus) |
| Documented uses | Robotics R&D; Teaching / education; Demo / showpiece | configuration: Base (RK3588); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/hightorque-mini-pi-plus) |

## Documents

- [HumanoidStore datasheet – HighTorque Robotics Mini Pi Plus (CC BY 4.0)](https://humanoidstore.co/robots/hightorque-mini-pi-plus)

## Notes

Maker page (hightorque.cn/pi-plus): standing height 680 mm, 15.15 kg with battery, 22 DoF, payload 10 kg, max joint torque 21 N.m, 24 V working voltage, modular open architecture, SDK, multi-channel CAN FD, jumping and gait walking. Maker store: Base 6,000 USD (RK3588, 15.4 kg) and Pro 8,000 USD (Jetson Orin NX + RealSense D435i, 15.6 kg), battery 21.6 V 4500 mAh (=97 Wh derived), 60 min operating time, 1.1 m/s, ROS 1 + SDK. Conflict: 24 V on the product page vs 21.6 V / 4500 mAh pack in the store spec. The 8,000 USD Pro price was not used for price_usd (Base configuration is recorded).

## Sources

- Official page: [hightorque.cn](https://www.hightorque.cn/pi-plus/)
- [store.hightorque.cn](https://store.hightorque.cn/products/bipedal-robot-mini-pi-plus)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-22). Source repository: https://github.com/htcrefactor/robot-catalog*
