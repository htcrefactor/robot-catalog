# Seegrid Lift CR1

> Autonomous lift truck that moves and stacks pallets up to 4,000 lb to 15 ft without floor infrastructure.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=seegrid-lift-cr1
- Category: AMR
- Locomotion: Wheeled
- Manufacturer: Seegrid (United States)
- Verification: not recorded

## Core specs

| Field | Value |
|---|---|
| Payload | 1,814 kg |
| Max speed | 2.24 m/s (8.1 km/h) |
| Status | Commercial |
| Sensors | 5x 2D and 3D LiDAR sensors (layered safety), 3D computer vision payload detection |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

37 values from 3 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Manufacturer | Seegrid Corporation |  | [seegrid.com](https://seegrid.com/news/seegrid-unveils-new-lift-cr1-at-modex-2024) |
| Robot type | Autonomous lift truck AMR |  | [seegrid.com](https://seegrid.com/news/seegrid-unveils-new-lift-cr1-at-modex-2024) |
| Model name | CR1 = "Cab Reach" |  | [seegrid.com](https://seegrid.com/news/seegrid-unveils-new-lift-cr1-at-modex-2024) |
| Former name | Palion Lift CR1 |  | [web.archive.org](http://web.archive.org/web/20240529173544/https://seegrid.com/autonomous-mobile-robots/palion-lift-cr1/) |
| Unveiled | 2024-02-15, MODEX 2024 (booth C7685) |  | [seegrid.com](https://seegrid.com/news/seegrid-unveils-new-lift-cr1-at-modex-2024) |
| Position in line | Seegrid's second lift AMR, after Lift RS1 (launched Dec 2022) |  | [seegrid.com](https://seegrid.com/news/seegrid-unveils-new-lift-cr1-at-modex-2024) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Width | 50 in | legacy spec block (May 2024) | [web.archive.org](http://web.archive.org/web/20240529173544/https://seegrid.com/autonomous-mobile-robots/palion-lift-cr1/) |
| Length | 92 in | forks retracted; legacy spec block (May 2024) | [web.archive.org](http://web.archive.org/web/20240529173544/https://seegrid.com/autonomous-mobile-robots/palion-lift-cr1/) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Payload capacity | 4,000 lb |  | [seegrid.com](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr) |
| Maximum automatic speed | 5 mph | forward | [seegrid.com](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr) |
| Maximum automatic speed, reverse | 0.7 mph | legacy page lists "Reverse -0.7 mph" | [web.archive.org](http://web.archive.org/web/20240529173544/https://seegrid.com/autonomous-mobile-robots/palion-lift-cr1/) |
| Wheels | Polyurethane |  | [web.archive.org](http://web.archive.org/web/20240529173544/https://seegrid.com/autonomous-mobile-robots/palion-lift-cr1/) |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Navigation | Infrastructure-free LiDAR SLAM with Grid Engine localization; dynamic path planning |  | [seegrid.com](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr) |
| Localization | Grid Engine localization |  | [seegrid.com](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charging | Auto-Charge (synchronized self-charging scheduled via Fleet Central) |  | [seegrid.com](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr) |
| Automatic charging | Auto-Charge automates scheduling, dispatch and charging for 24/7 operation |  | [seegrid.com](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| LiDAR sensors | 5 | 2D and 3D LiDAR, layered safety | [seegrid.com](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr) |
| LiDAR | Layered 2D & 3D LiDAR sensors |  | [seegrid.com](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr) |
| Payload detection | 3D computer vision payload detection; handles misaligned and non-standard pallets with real-time alignment adjustment |  | [seegrid.com](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr) |
| Perception | 3D computer vision with sensor fusion; same core LiDAR/SLAM and 3D vision suite as Lift RS1 |  | [seegrid.com](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Fleet software | Seegrid Fleet Central |  | [seegrid.com](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Interoperability | VDA5050 supported (Seegrid announcement linked from CR1 page) | company-wide statement | [seegrid.com](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr) |
| Information security | Seegrid ISMS certified ISO/IEC 27001:2022 | company-level certification | [seegrid.com](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr) |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Max lift height | 15 ft | mast supports future higher heights | [seegrid.com](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr) |
| Reach | 180 in | legacy spec block | [web.archive.org](http://web.archive.org/web/20240529173544/https://seegrid.com/autonomous-mobile-robots/palion-lift-cr1/) |
| Forks | ITA rated; 42 in standard, 36–72 in optional |  | [seegrid.com](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Personnel detection | Safety-rated personnel detection system |  | [seegrid.com](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr) |
| Secondary detection | Secondary 3D object detection system |  | [web.archive.org](http://web.archive.org/web/20240529173544/https://seegrid.com/autonomous-mobile-robots/palion-lift-cr1/) |
| Emergency stop buttons | 3 |  | [seegrid.com](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr) |
| Warning system | Acoustic warning system |  | [seegrid.com](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr) |
| Workflows | Inbound to bulk storage, parts to line (pick from floor or staging up to 6 ft), inbound, outbound, cross docking; Autonomous Buffer Management (ABM), vertical storage |  | [seegrid.com](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Autonomy | Sliding Scale Autonomy (hybrid of AMR agility and AGV predictability); real-time route changes |  | [seegrid.com](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr) |
| Manual operation | Hybrid: off-the-shelf chassis with Seegrid technology allows manual or autonomous operation |  | [seegrid.com](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr) |
| Operator compartment | Protected ride-on compartment |  | [web.archive.org](http://web.archive.org/web/20240529173544/https://seegrid.com/autonomous-mobile-robots/palion-lift-cr1/) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Status lights | LED lightbar |  | [seegrid.com](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Award | Modern Material Handling 2024 Readers' Choice Product of the Year |  | [seegrid.com](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr) |
| Fork options | 36 in – 72 in forks |  | [seegrid.com](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr) |

## Documents

- [Seegrid Lift CR1 AMR product page](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr)
- [Seegrid press release: Lift CR1 unveiled at MODEX 2024 (2024-02-15)](https://seegrid.com/news/seegrid-unveils-new-lift-cr1-at-modex-2024)
- [Seegrid Palion Lift CR1 page, archived 2024-05-29 (Wayback Machine)](http://web.archive.org/web/20240529173544/https://seegrid.com/autonomous-mobile-robots/palion-lift-cr1/)

## Sources

- Official page: [seegrid.com](https://seegrid.com/autonomous-mobile-robots/lift-cr1-amr)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-20). Source repository: https://github.com/htcrefactor/robot-catalog*
