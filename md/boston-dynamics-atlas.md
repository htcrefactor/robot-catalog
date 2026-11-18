# Boston Dynamics Atlas (electric)

> Boston Dynamics' electric Atlas: a 1.9 m, 56-DoF humanoid built for factory part sequencing, machine tending and order fulfilment, with autonomous battery swap.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=boston-dynamics-atlas
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: Boston Dynamics (United States)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Height | 1,900 mm |
| Weight | 90 kg |
| Payload | 30 kg |
| Degrees of freedom | 56 |
| Runtime | 4 h |
| IP rating | IP67 |
| Status | Pilot |
| Sensors | Tactile fingers and palm, 360-degree camera view |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

43 values from 6 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Spec sheet revision | Rev 10/15/2026 |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf) |
| Product version unveiled | 2026-01-05 | CES 2026 | [bostondynamics.com](https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry) |
| Made in | USA | production at Boston HQ | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf) |
| Form factor | full-size | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/bostondynamics-atlas) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Height | 1.9 m | 6.2 ft | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf) |
| Weight | 90 kg | 198 lb | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf) |
| Height (standing) | 190 cm | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/bostondynamics-atlas) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Degrees of freedom | 56 |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf) |
| Weight capacity – instant | 50 kg | 110 lb | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf) |
| Weight capacity – sustained | 30 kg | 66 lb; repeated lifts | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery life | 4 h | typical use | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf) |
| Battery life with heavy lifting | 2 h |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf) |
| Self-swappable batteries | yes | navigates to charging station and swaps own battery; 24/7 operation | [bostondynamics.com](https://bostondynamics.com/blog/enterprise-robotics-redefined/) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Autonomous battery swap time | 3 min | less than three minutes | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf) |
| Charge time | 1.5 h |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf) |
| Charge power requirements | 110 V (220 V optional) |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf) |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| IP rating | IP67 | can be sprayed or wiped down | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf) |
| Operating temperature | -20 to 40 °C | -4 to 104 °F; full capabilities incl. strength | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Tactile sensing | Tactile fingers and palm |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf) |
| Camera view | 360° camera view |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Fleet software | Orbit (MES/WMS integration, fleet metrics; SOC2 Type II; cloud, on-prem or VM) |  | [bostondynamics.com](https://bostondynamics.com/blog/enterprise-robotics-redefined/) |
| AI models | Google DeepMind foundation models (partnership) |  | [bostondynamics.com](https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Workflow integrations | Barcode scanner; RFID |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Weight capacity – one-handed | 20 kg | 44 lb | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf) |
| Reach | 2.3 m | 7.5 ft | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf) |
| Hand DoF (new-generation hand) | 13 | 4 fingers, directly actuated, single actuator type; previous hand 7 DoF | [bostondynamics.com](https://bostondynamics.com/blog/robot-hands-for-modern-ai-and-real-work/) |
| Hand | Four-finger dexterous hand with tactile fingers and palm |  | [bostondynamics.com](https://bostondynamics.com/blog/robot-hands-for-modern-ai-and-real-work/) |
| Hands | included | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/bostondynamics-atlas) |

### Actuation & Joints

| Spec | Value | Note | Source |
|---|---|---|---|
| Range of motion | Continuous (fully rotational joints) |  | [bostondynamics.com](https://bostondynamics.com/atlas/) |
| Actuators | Supplied by Hyundai Mobis | limited number of motor types | [bostondynamics.com](https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Safety system | Fenceless guarding; human detection (pauses when a person is within a radius) |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf) |
| Physical safety | Padding and minimal pinch points |  | [bostondynamics.com](https://bostondynamics.com/blog/enterprise-robotics-redefined/) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Operating modes | Autonomous; VR teleoperated; tablet control |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf) |

### Transport & Storage

| Spec | Value | Note | Source |
|---|---|---|---|
| Serviceability | Modular components; field replaceable; customer self-repair certification |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf) |
| Field limb replacement | <5 min | all limbs replaceable in the field | [bostondynamics.com](https://bostondynamics.com/blog/enterprise-robotics-redefined/) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Availability | 2026 deployments fully committed (Hyundai RMAC, Google DeepMind); more customers early 2027 |  | [bostondynamics.com](https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry) |
| Sales status | b2b-only | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/bostondynamics-atlas) |
| Who can buy | restricted | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/bostondynamics-atlas) |
| Route to US | no | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/bostondynamics-atlas) |
| Route to EU | no | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/bostondynamics-atlas) |
| Sellers listed | 0 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/bostondynamics-atlas) |
| Deployment stage | pilot | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/bostondynamics-atlas) |
| Documented uses | Real work / logistics | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/bostondynamics-atlas) |

## Documents

- [Atlas spec sheet (Rev 10/15/2026)](https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf)
- [Atlas product page](https://bostondynamics.com/atlas/)
- [Enterprise Robotics, Redefined (BD blog, 2026-01-05)](https://bostondynamics.com/blog/enterprise-robotics-redefined/)
- [Boston Dynamics Unveils New Atlas Robot (press release, 2026-01-05)](https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry)
- [Robot Hands for Modern AI and Real Work (BD blog, 2026-10)](https://bostondynamics.com/blog/robot-hands-for-modern-ai-and-real-work/)
- [HumanoidStore datasheet – Boston Dynamics Atlas (CC BY 4.0)](https://humanoidstore.co/robots/bostondynamics-atlas)

## Notes

Maker Atlas spec sheet (Rev 10/15/2026, bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf): height 1.9 m, 90 kg, 56 DoF, weight capacity 50 kg instant / 30 kg sustained / 20 kg one-handed (payload_kg = the sustained figure), reach 2.3 m, battery life 4 h (2 h with heavy lifting), autonomous battery swap in 3 min with 1.5 h charge at 110 V (220 V optional), IP67, -20 to 40 C. Sensing is tactile fingers and palm plus a 360-degree camera view; a barcode scanner and RFID are listed as workflow integrations, not sensors, and fenceless guarding with human detection plus autonomous / VR-teleoperated / tablet control modes are stated. Status kept at Pilot: the maker sells into pilot plants and publishes a volume-production spec sheet, but no public price or order page exists. Price figure is the HumanoidStore listing.

## Sources

- Official page: [bostondynamics.com](https://bostondynamics.com/atlas/)
- [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2026/01/atlas-spec-sheet.pdf)
- [bostondynamics.com](https://bostondynamics.com/news/introducing-electric-atlas/)
- [humanoidstore.co](https://humanoidstore.co/robots/bostondynamics-atlas)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-18). Source repository: https://github.com/htcrefactor/robot-catalog*
