# Rainbow Robotics RB-Y1

> Rainbow Robotics' wheeled dual-arm humanoid research platform: 24 DOF all-in-one mobile manipulator with 7-DOF arms, 6-DOF leg/torso and a rolling base.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=rainbow-rby1
- Category: Humanoid
- Locomotion: Wheeled
- Manufacturer: Rainbow Robotics (South Korea)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 690 mm |
| Width | 600 mm |
| Height | 1,400 mm |
| Weight | 131 kg |
| Payload | 3 kg |
| Max speed | 1.5 m/s (5.4 km/h) |
| Degrees of freedom | 24 |
| Battery | 1,250 Wh |
| Released | 2024 |
| Status | Commercial |
| SDK | yes |
| SDK name | RB-Y1 SDK (ROS 2, dual-PC architecture) |
| ROS | yes |
| On-board compute | Dual PC (Robot PC + User PC) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

15 values from 1 document, checked against maker sources on 2026-11-13.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Form factor | wheeled (bimanual torso on a wheeled base) | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/rainbow-rby1) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Height (standing) | 140 cm | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/rainbow-rby1) |
| Weight | 131 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/rainbow-rby1) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total degrees of freedom | 24 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/rainbow-rby1) |
| Top speed | 1.5 m/s | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/rainbow-rby1) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Runtime per charge | 180 min | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/rainbow-rby1) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Hands | optional | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/rainbow-rby1) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Sales status | shipping-now | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/rainbow-rby1) |
| Who can buy | anyone | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/rainbow-rby1) |
| Price | 80,000 USD | list price (maker price); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/rainbow-rby1) |
| Route to US | no | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/rainbow-rby1) |
| Route to EU | unclear | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/rainbow-rby1) |
| Sellers listed | 1 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/rainbow-rby1) |
| Documented uses | Robotics R&D; Manipulation research; Teaching / education | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/rainbow-rby1) |

### Payload

| Spec | Value | Note | Source |
|---|---|---|---|
| Rated payload | 6 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/rainbow-rby1) |

## Documents

- [HumanoidStore datasheet – Rainbow Robotics RB-Y1 (CC BY 4.0)](https://humanoidstore.co/robots/rainbow-rby1)

## Notes

Maker spec table (English product page + RB-Y1 developer docs): 600 x 690 x 1,400 mm (W x D x H), 131 kg in Model A (mobile base 51 kg; Model M with mecanum base is 170 kg), 3 kg payload per arm, 600 mm arm reach to the wrist, 1.5 m/s drive speed, 24 DOF in Model A (wheel 1 x 2, torso/leg 6, arm 7 x 2, head 2) and 26 DOF in Model M (wheel 1 x 4), +/-0.05 mm arm repeatability, 48 VDC, 50 V 25 Ah battery = 1,250 Wh per the maker table (the docs page prints 1,270 Wh). Price: the maker publishes no price; the 80,000 USD in this record came from HumanoidStore and was removed. Runtime is not published by the maker (the earlier 3 h figure was reseller-sourced and was removed). Maker notes no vision camera is included (the wrist 'camera' is a motor pulley).

## Sources

- Official page: [rainbow-robotics.com](https://rainbow-robotics.com/en/products/rb-y1/)
- [rainbowrobotics.github.io](https://rainbowrobotics.github.io/rby1-dev/hardware/overview.html)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-17). Source repository: https://github.com/htcrefactor/robot-catalog*
