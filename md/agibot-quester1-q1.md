# AgiBot QUESTER1 (Q1)

> Backpack-sized personal/educational humanoid with 22 compliant joints, open SDK/HDK and ROS/ROS2 compatibility, sold as PrimeBOT Q1.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=agibot-quester1-q1
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: AgiBot (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Height | 880 mm |
| Weight | 16 kg |
| Degrees of freedom | 22 |
| Released | 2025 |
| Status | Commercial |
| SDK | yes |
| ROS | yes |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

16 values from 1 document, checked against maker sources on 2026-11-22.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Model | PrimeBOT Q1 (启元Q1) and Q1 Explorer Edition (启元Q1 探索版) | Two editions listed | [primebot.com](https://www.primebot.com/q1.html) |
| Color | Star Gray; Star White; Sakura Pink | Q1 Explorer Edition colours | [primebot.com](https://www.primebot.com/q1.html) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Overall height | 88 cm | "88cm golden height" | [primebot.com](https://www.primebot.com/q1.html) |
| Weight (with battery) | 16 kg | "约16kg" including battery | [primebot.com](https://www.primebot.com/q1.html) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total degrees of freedom | 22 | Arm 4x2 + leg 6x2 + waist 2 | [primebot.com](https://www.primebot.com/q1.html) |
| Locomotion control | Mixture-of-experts RL locomotion model with force/position hybrid control (walking, posing, fall recovery, dynamic performance) |  | [primebot.com](https://www.primebot.com/q1.html) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Secondary development | Open SDK, HDK and API; PrimeToolkit skill development platform; joint-level motion-control interface; official base locomotion model open-sourced | Developer section (items marked * on page) | [primebot.com](https://www.primebot.com/q1.html) |
| ROS | Compatible with ROS/ROS2 ecosystem | Page wording; no package link given | [primebot.com](https://www.primebot.com/q1.html) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Rear panel | USB Type-A x1; USB Type-C x1; RJ45 x1; power port 12 V/5 A x1 | Expansion interfaces | [primebot.com](https://www.primebot.com/q1.html) |

### Actuation & Joints

| Spec | Value | Note | Source |
|---|---|---|---|
| DoF per arm | 4 |  | [primebot.com](https://www.primebot.com/q1.html) |
| DoF per leg | 6 |  | [primebot.com](https://www.primebot.com/q1.html) |
| Waist DoF | 2 |  | [primebot.com](https://www.primebot.com/q1.html) |
| Joint type | Quasi-direct-drive (QDD) joints with 22 compliant force-controlled DoF | Ring-gear motor integrated with housing | [primebot.com](https://www.primebot.com/q1.html) |
| Joint masses | 260 g | Powder-metallurgy ring-gear motor + housing, 2.5 mm hollow wiring | [primebot.com](https://www.primebot.com/q1.html) |
| Peak joint torque density | 85 N·m/kg | Peak torque density | [primebot.com](https://www.primebot.com/q1.html) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Product list | Power adapter; carrying bag (方舟携行包); original battery |  | [primebot.com](https://www.primebot.com/q1.html) |

## Documents

- [PrimeBOT Q1 product page, overview and specs](https://www.primebot.com/q1.html)

## Notes

Maker product page is PrimeBOT "启元Q1" (primebot.com/q1.html): 88 cm, about 16 kg with battery, 22 DoF (arm 4x2 + leg 6x2 + waist 2), open SDK/HDK, ROS/ROS2 ecosystem compatible. Unveiled 2025-12-31 by AgiBot co-founder Peng Zhihui; launch coverage quoted ~80 cm, which the product page does not support. agibot.com has no Q1 page.

## Sources

- Official page: [primebot.com](https://www.primebot.com/q1.html)

Listed by these directories (discovery only, never used as a spec source):

- [humanoid.guide](https://humanoid.guide/product/quester1-q1/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-25). Source repository: https://github.com/htcrefactor/robot-catalog*
