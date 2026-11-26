# Robotis OP3

> ROBOTIS OP3 is the XM430-based successor to OP2 with an Intel i3 NUC and ROS 2 support, the current miniature humanoid platform for research and education.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=robotis-op3
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: Robotis (South Korea)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Degrees of freedom | 20 |
| Battery | 36.6 Wh |
| Released | 2017 |
| Status | Commercial |
| SDK | yes |
| SDK name | ROS 2, DYNAMIXEL SDK, C++, Open Platform source |
| ROS | yes |
| On-board compute | Intel NUC Core i3 dual core (8 GB DDR4, 128-250 GB M.2 SSD) + OpenCR (ARM Cortex-M7) |
| Sensors | Logitech C920 HD Pro camera, 3-axis gyroscope, 3-axis accelerometer, 3-axis magnetometer |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

16 values from 1 document, checked against maker sources on 2026-11-13.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Form factor | desktop-size | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-op3) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Height (standing) | 51 cm | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-op3) |
| Weight | 3.5 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-op3) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total degrees of freedom | 20 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-op3) |
| Top speed | 0.24 m/s | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-op3) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Runtime per charge | 30 min | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-op3) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Hands | none | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-op3) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Sales status | shipping-now | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-op3) |
| Who can buy | anyone | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-op3) |
| Price | 11,969 USD | list price (maker price); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-op3) |
| Delivered price to US | 13,585 USD | before sales tax; route: estimate: import; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-op3) |
| Delivered price to Germany | 12,813 EUR | incl. 19% VAT; route: estimate: import; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-op3) |
| Route to US | direct | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-op3) |
| Route to EU | direct | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-op3) |
| Sellers listed | 2 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-op3) |
| Documented uses | Robotics R&D; Teaching / education; Learn and tinker | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/robotis-op3) |

## Documents

- [HumanoidStore datasheet – Robotis OP3 (CC BY 4.0)](https://humanoidstore.co/robots/robotis-op3)

## Notes

Maker page and e-manual: about 510 mm, about 3.5 kg without the skin cover, 20 actuator modules (6 DOF leg x 2, 3 DOF arm x 2, 2 DOF neck), DYNAMIXEL XM430-W350-R, Intel NUC with Core i3 dual core, 8 GB DDR4 and a 128 GB (maker store page) / 250 GB (e-manual) M.2 SSD, OpenCR management controller (ARM Cortex-M7), Logitech C920 1080p camera, 3-axis gyro/accelerometer/magnetometer, 1,800 mAh 3-cell 11.1 V LiPo with about 30 minutes of operation (36.6 Wh derived), 4 buttons, RGB LED x 1 and LED x 3, speaker, HDMI/DP. The 2025 re-release was rebuilt for ROS 2. The 11,969 USD price was a HumanoidStore figure with no maker price and was removed; the maker sells by inquiry. Walking speed is not stated on the maker pages, so max speed is left empty.

## Sources

- Official page: [en.robotis.com](https://en.robotis.com/model/page.php?co_id=prd_op3)
- [github.com](https://github.com/ROBOTIS-GIT/emanual/blob/master/docs/en/platform/op3/introduction.md)
- [humanoidstore.co](https://humanoidstore.co/robots/robotis-op3)
- [robotis.com](https://www.robotis.com/ko/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-26). Source repository: https://github.com/htcrefactor/robot-catalog*
