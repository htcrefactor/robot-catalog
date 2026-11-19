# Fourier GR-3

> 'Care-bot' companion humanoid for public service and care settings; DoF is up to 55 with optional 12-DoF hands; 702+234 Wh hot-swap batteries; 6.1 km/h walk converted.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=fourier-gr-3
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: Fourier (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 292 mm |
| Width | 552 mm |
| Height | 1,642 mm |
| Weight | 71 kg |
| Payload | 3 kg |
| Max speed | 1.69 m/s (6.1 km/h) |
| Degrees of freedom | 55 |
| Runtime | 3 h |
| Battery | 936 Wh |
| Status | Commercial |
| SDK | yes |
| On-board compute | yes |
| Compute | AMD Ryzen 7 8845HS, 32 GB RAM, 1 TB storage, Radeon 780M, Ubuntu 22.04 |
| Sensors | Monocular camera, 6-axis IMU, 360-degree microphone, Distributed tactile sensors (head, torso), 15 W speaker |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

78 values from 2 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Documentation version | v3.0.2 |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Form factor | full-size | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/fourier-gr3) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Height | 1,642 mm | dimensions 1642 x 552 x 292 mm | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Width | 552 mm |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Depth | 292 mm |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Arm span | 1,395 mm | up to 1759 mm with 12-DoF dexterous hand | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Lower leg + upper leg | 425 + 408 mm |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Net weight | 71 kg | ≈71 kg | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Materials | Aluminium alloy + engineering plastic + soft covering |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Height (standing) | 164 cm | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/fourier-gr3) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total actuators | 55 | up to 55 with optional 12-DoF dexterous hands | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Walking speed | 6.1 km/h |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Top speed | 1.67 m/s | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/fourier-gr3) |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Max walking gradient | 15 ° |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Nominal voltage | 46.8 V |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Rated power | 936 W | ≈936 W | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Battery type | Lithium-ion |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Battery capacity | 702 + 234 Wh | two packs | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Battery weight | 3.8 + 1.3 kg |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Runtime | 3 h | ≈3 h | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Charge limit voltage | 54.6 V |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Cycle life | ≥500 cycles | 80% DoD | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Hot-swappable battery | yes |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Single charge time | 1.5 h | ≈1.5 h | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Adapter input | 90-260 V AC, 50/60 Hz |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Adapter output | 54.6 V, 12 A max |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| Operating temperature | 0 to 45 °C |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Operating humidity | 20 to 80 % | non-condensing | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Camera | Monocular camera (OAK) |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| IMU | 6-axis (acceleration, angular velocity) |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Microphone | 360° omnidirectional pickup | echo cancellation, sound source localization | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Tactile sensors | Distributed on head and torso |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Operating system | Ubuntu 22.04 |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| CPU | AMD Ryzen 7 8845HS (8-core 16-thread) | development board E-Sports D70 | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| GPU | AMD Radeon 780M |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Cache | L3 16 MB |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Memory | 32 GB |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Storage | 1 TB |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| I/O | Type-C, USB 3.0, RJ45 |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Wired connection | Ethernet |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Wireless | Wi-Fi 6 |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Hand DoF | 6 | base hand; optional 12-DoF dexterous hand | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Single-arm payload | 3 kg | ≈3 kg | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Hands | included | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/fourier-gr3) |

### Actuation & Joints

| Spec | Value | Note | Source |
|---|---|---|---|
| Head DoF | 2 |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| DoF per arm | 7 |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Waist DoF | 3 |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| DoF per leg | 6 |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Max joint peak torque | 440 N·m |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Encoders | Dual encoders, absolute supported |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |
| Joint limit – Neck pitch | -30 to 8.5 ° | right side mirrored | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) · §6.2 |
| Joint limit – Neck yaw | ±80 ° | right side mirrored | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) · §6.2 |
| Joint limit – Shoulder pitch | ±170 ° | right side mirrored | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) · §6.2 |
| Joint limit – L shoulder roll | -15 to 110 ° | right side mirrored | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) · §6.2 |
| Joint limit – Shoulder yaw | ±105 ° | right side mirrored | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) · §6.2 |
| Joint limit – Elbow pitch | -130 to 5 ° | right side mirrored | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) · §6.2 |
| Joint limit – Wrist yaw | ±105 ° | right side mirrored | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) · §6.2 |
| Joint limit – Wrist pitch | -50 to 75 ° | right side mirrored | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) · §6.2 |
| Joint limit – L wrist roll | -60 to 70 ° | right side mirrored | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) · §6.2 |
| Joint limit – Waist pitch | -12 to 30 ° | right side mirrored | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) · §6.2 |
| Joint limit – Waist roll | ±10 ° | right side mirrored | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) · §6.2 |
| Joint limit – Waist yaw | ±150 ° | right side mirrored | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) · §6.2 |
| Joint limit – Hip pitch | ±150 ° | right side mirrored | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) · §6.2 |
| Joint limit – L hip roll | -10 to 90 ° | right side mirrored | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) · §6.2 |
| Joint limit – L hip yaw | -40 to 90 ° | right side mirrored | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) · §6.2 |
| Joint limit – Knee pitch | 0 to 135 ° | right side mirrored | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) · §6.2 |
| Joint limit – Ankle pitch | ±45 ° | right side mirrored | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) · §6.2 |
| Joint limit – Ankle roll | ±25 ° | right side mirrored | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) · §6.2 |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Teleoperation | Immersive remote control (VR headset / exoskeleton) |  | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Speaker | 15 W | up to 15 W, volume adjustable | [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Sales status | b2b-only | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/fourier-gr3) |
| Who can buy | business | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/fourier-gr3) |
| Price | 100,000 USD | list price (maker price); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/fourier-gr3) |
| Route to US | reseller | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/fourier-gr3) |
| Route to EU | reseller | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/fourier-gr3) |
| Sellers listed | 2 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/fourier-gr3) |
| Documented uses | Robotics R&D; Manipulation research; Demo / showpiece | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/fourier-gr3) |

### Payload

| Spec | Value | Note | Source |
|---|---|---|---|
| Rated payload | 3 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/fourier-gr3) |

## Documents

- [Fourier GR-3 Developer Center – Robot Overview (v3.0.2, updated 2026-09-22)](https://support.fftai.com/en/gr3/getting-started/general-information)
- [HumanoidStore datasheet – Fourier GR-3 (CC BY 4.0)](https://humanoidstore.co/robots/fourier-gr3)

## Notes

Media (2026-11-17): product render gr3-mb.png and the demo clips (walk, terrain-walk, operation, stability, ping-pong) are served from fftai.com's GR-3 page.

## Sources

- Official page: [support.fftai.com](https://support.fftai.com/en/gr3/getting-started/general-information)
- [humanoidstore.co](https://humanoidstore.co/robots/fourier-gr3)
- [fftai.com](https://www.fftai.com/grx/gr3)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-19). Source repository: https://github.com/htcrefactor/robot-catalog*
