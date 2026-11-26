# Anigon FA-L

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=anigon-fa-l
- Category: Humanoid
- Locomotion: Wheeled
- Manufacturer: Anigon (Switzerland)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Height | 1,890 mm |
| Max speed | 1.5 m/s (5.4 km/h) |
| Degrees of freedom | 28 |
| Status | Pilot |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

21 values from 2 documents, checked against maker sources on 2026-11-22.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Model | ANIGON FA-L series |  | [anigon.ch](https://anigon.ch/robot-platform) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Overall height | 189 cm | Reference specification | [anigon.ch](https://anigon.ch/robot-platform) |
| Arm span | 65 cm | Reference specification | [anigon.ch](https://anigon.ch/robot-platform) |
| Overall height | 1,870 mm | Aimbo co-founder post (2026-03-03) — differs from anigon.ch (189 cm) | [linkedin.com](https://www.linkedin.com/posts/roland-wulz_aimboag-anigon-humanoidrobotics-activity-7434565450275160064-INDD) |
| Weight | 166 kg | Aimbo co-founder post (2026-03-03); anigon.ch gives no weight | [linkedin.com](https://www.linkedin.com/posts/roland-wulz_aimboag-anigon-humanoidrobotics-activity-7434565450275160064-INDD) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total degrees of freedom | 28 | Full body | [anigon.ch](https://anigon.ch/robot-platform) |
| Top speed | 1.5 m/s | Subject to operating mode and site policy | [anigon.ch](https://anigon.ch/robot-platform) |
| Base type | Adaptive lifting mobile base |  | [anigon.ch](https://anigon.ch/robot-platform) |
| Rated payload | 6 kg | Single arm, rated (co-founder post) | [linkedin.com](https://www.linkedin.com/posts/roland-wulz_aimboag-anigon-humanoidrobotics-activity-7434565450275160064-INDD) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Swappable battery | yes | Dual hot-swap battery system | [anigon.ch](https://anigon.ch/robot-platform) |
| Number of batteries | 2 | Dual hot-swap batteries | [anigon.ch](https://anigon.ch/robot-platform) |
| Continuous operation | 24/7 with battery rotation, maintenance and duty-cycle planning |  | [anigon.ch](https://anigon.ch/robot-platform) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Joint sensors | Integrated joint torque sensors; full force-controlled compliance |  | [anigon.ch](https://anigon.ch/robot-platform) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Chipset | Integrated edge compute controller (compute backpack) with separate safety control unit | Local inference; safety-critical control separated from model execution | [anigon.ch](https://anigon.ch/robot-platform) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Integration interfaces | ERP, MES and WMS interfaces |  | [anigon.ch](https://anigon.ch/robot-platform) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Arm payload (peak) | 10 kg | Single arm, max (co-founder post) | [linkedin.com](https://www.linkedin.com/posts/roland-wulz_aimboag-anigon-humanoidrobotics-activity-7434565450275160064-INDD) |
| Arm reach | 650 mm | Arm reach ≥ 650 mm (co-founder post) | [linkedin.com](https://www.linkedin.com/posts/roland-wulz_aimboag-anigon-humanoidrobotics-activity-7434565450275160064-INDD) |
| Repeatability | 0.1 mm | ± value (co-founder post) | [linkedin.com](https://www.linkedin.com/posts/roland-wulz_aimboag-anigon-humanoidrobotics-activity-7434565450275160064-INDD) |
| Max TCP speed | 2 m/s | Max TCP speed (co-founder post) | [linkedin.com](https://www.linkedin.com/posts/roland-wulz_aimboag-anigon-humanoidrobotics-activity-7434565450275160064-INDD) |

### Actuation & Joints

| Spec | Value | Note | Source |
|---|---|---|---|
| DoF per arm | 7 |  | [anigon.ch](https://anigon.ch/robot-platform) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Holding brake | Electromagnetic holding brake | Plus sensitive collision detection and response | [anigon.ch](https://anigon.ch/robot-platform) |

## Documents

- [ANIGON FA-L robot platform page](https://anigon.ch/robot-platform)
- [Aimbo AG co-founder LinkedIn post, 2026-03-03](https://www.linkedin.com/posts/roland-wulz_aimboag-anigon-humanoidrobotics-activity-7434565450275160064-INDD)

## Notes

Maker site anigon.ch/robot-platform (checked 2026-11-22): 189 cm, 28 DoF (7 per arm), 1.5 m/s max (subject to operating mode and site policy), dual hot-swap batteries. A March 2026 post by an Aimbo co-founder (maker of the Anigon brand) gives 1,870 mm and 166 kg instead; the site value is kept and the post values are separate rows in the full specs.

## Sources

- Official page: [anigon.ch](https://anigon.ch/)
- [anigon.ch](https://anigon.ch/robot-platform)
- [linkedin.com](https://www.linkedin.com/posts/roland-wulz_aimboag-anigon-humanoidrobotics-activity-7434565450275160064-INDD)

Listed by these directories (discovery only, never used as a spec source):

- [embodied.guide](https://embodied.guide/robots/anigon-fa-l/)
- [humanoid.guide](https://humanoid.guide/product/anigon/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-26). Source repository: https://github.com/htcrefactor/robot-catalog*
