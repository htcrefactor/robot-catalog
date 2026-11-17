# Mobile Industrial Robots (MiR) MiR600

> IP52-rated 600 kg AMR that picks up and moves pallets and heavy loads as a forklift alternative.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=mir-mir600
- Category: AMR
- Locomotion: Wheeled
- Manufacturer: Mobile Industrial Robots (MiR) (Denmark)
- Verification: not recorded

## Core specs

| Field | Value |
|---|---|
| Length | 1,350 mm |
| Width | 910 mm |
| Height | 322 mm |
| Weight | 240 kg |
| Payload | 600 kg |
| Max speed | 2 m/s (7.2 km/h) |
| Wheel diameter | 200 mm |
| Runtime | 8.33 h |
| Battery | 1,631 Wh |
| IP rating | IP52 |
| Status | Commercial |
| API | yes |
| Sensors | 2x SICK microScan3 safety laser scanners (360°), 2x 3D cameras, 8x proximity sensors |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

91 values from 1 document, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Robot type | Autonomous Mobile Robot (AMR) |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Color | RAL 7011 / Iron Gray |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Product design life | 5 years or 20 000 hours of active operation, whichever comes first |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Specification document date | 2025-09-01 |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 1,350 mm |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Width | 910 mm |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Height | 322 mm |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Weight | 240 kg |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Ground clearance | 25–27 mm |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Drive wheel diameter | 200 mm |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Caster wheel diameter | 100 mm |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Drive wheel material | Polyurethane |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Maximum payload | 600 kg |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Maximum speed | 2 m/s | with maximum payload on a flat surface (7.2 km/h) | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Maximum acceleration | 0.41 m/s² | no payload | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Maximum acceleration | 0.37 m/s² | maximum payload | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Positioning precision, docking to VL-marker | X ±2 mm; Y ±3 mm; orientation ±0.3° |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Positioning precision, docking to V-marker | X ±20 mm; Y ±20 mm; orientation 2° |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Positioning precision, docking to bar-marker | X ±10 mm; Y ±5 mm; orientation ±0.8° |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Positioning precision, docking to L-marker | X ±3 mm; Y ±3 mm; orientation ±0.3° |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Positioning precision, moving to position | X ±100 mm; Y ±83 mm; orientation ±3.4° |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Operational corridor width | 1.8 m | standard settings; 1.20 m reduced safety settings | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Corridor width for a 90° turn | 1.85 m | standard; 1.55 m reduced safety settings | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Corridor width for a U-turn | 1.85 m | standard; 1.55 m reduced safety settings | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Operational width for pivoting | 2.3 m | standard; 1.85 m reduced safety settings | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Operational doorway width | 1.65 m | standard; 1.20 m reduced safety settings | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Corridor width for two robots passing | 3.5 m | standard; 2.70 m reduced safety settings | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Marker/rack space requirements | Pallet rack: 2.70 m in front (2.40 m reduced), 0.70 m sides (0.30 m reduced); V-marker: 3.00 m in front (2.75 m reduced), 0.22–0.28 m between; bar-marker: 2.45 m in front (2.20 m reduced); VL-marker: 0.02–0.03 m between |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Floor conditions | Clean and dry |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Maximum slope at rated load | 3 % | at 0.5 m/s | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Maximum gap at rated load | 29 mm | at 0.5 m/s, 70°–90° approach | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Maximum step at rated load | 10 mm | at 0.5 m/s, 70°–90° approach | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Floor-to-wheel friction coefficient | 0.60–0.80 |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery type | Lithium-ion |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Battery weight | 11 kg |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Battery dimensions | 545 × 201 × 75 mm |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Battery cycle life | 3,000 cycles | minimum full cycles before capacity drops below 80% | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Battery voltage (nominal) | 47.7 V | minimum 42 V, maximum 54 V | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Battery voltage (maximum) | 54 V |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Battery capacity (Ah) | 34.2 Ah |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Active operation time, no payload | 10 h 45 min | 100–0% | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Active operation time, maximum payload | 8 h 20 min | 100–0% | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Active standby time | 16 h 45 min | robot idle, 100–0% | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Docking / undocking time, VL-marker | up to 12 s / up to 7 s | offsets -0.75 m X, 0.2 m Y | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Docking / undocking time, V-marker | up to 39 s / up to 5 s | offsets -0.75 m X, 0.4 m Y | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Docking / undocking time, L-marker | up to 16 s / up to 12 s | default offsets | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Docking / undocking time, bar-marker | up to 21 s / up to 14 s | default offsets | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Minimum space in front of line of charging stations | 2.8 m | standard; 2.60 m reduced safety settings | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Minimum distance between charging stations | 1.1 m |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Charging options | Charge 48V 35A; MiR Charge 48V; Battery Charger 48V 12A; Battery Charger 48V 650W 13.5A; Battery Charger 48V 1200W 13.5A; Cable Charger Lite 48V 3A |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Charging time 10–90% | 45 min | MiR Charge 48V | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Charging time 10–90% | 1 h 10 min | cable charger | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Maximum charging current | 35 A |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Charging-to-runtime ratio | 1:11 | 15 min charging → 2 h 45 min runtime | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Charging-to-runtime ratio | 1:12 | 30 min charging → 5 h 45 min runtime | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| IP rating | IP52 |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Environment | Indoor use only |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Operating ambient temperature | 5–25 °C | continuous use; maximum 40 °C for 1 hour | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Storage temperature | 0–50 °C |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Humidity | 20–95 % | non-condensing | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Optimal light conditions | Even and steady lighting; strong directional light can cause false obstacle detections |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Maximum altitude | 2,000 m |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Materials not reliably detected | Transparent, translucent, glossy, reflective and light-emitting |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Safety laser scanners | 2 (front and rear), 360° personnel detection 200 mm above ground |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| 3D cameras | 2 | for obstacles in front of robot outside the scanner plane | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Proximity sensors | 8 |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Communication protocols | REST; Modbus |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Wi-Fi | 2.4 GHz and 5 GHz, 2 external antennas |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| GPIO interface | 4 digital inputs, 4 digital outputs (M17 17-pin connector) |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Ethernet interface | 10/100 Mbit Ethernet with Modbus (M12 4-pin connector) |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Auxiliary emergency stop interface | E-stop buttons on top modules (M17 8-pin connector) |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Auxiliary safety function interface | Safety-related functions for top modules (M17 17-pin connector) |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Antenna interface | RP-SMA connector for top module |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Maximum lifting capacity | 500 kg | with MiR EU-/US-lift installed | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Power interface for top modules | 24 V and 48 V outputs (M23 6-pin connector) |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Designated use | Internal transportation of heavy loads and pallets |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| EMC | EN 61000-6-4 |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Compliant with | ISO 13849-1; ISO 12100; ISO 13850; ISO 3691-4 (except Clause 4.4, 4.9.4, 5.1, 5.2, 6 and Annex A) |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Design based on (industrial vehicle standards) | ITSDF B56-5; RIA R15.08-1 |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| TÜV safety evaluation | ISO 13849-1 (TÜV Rheinland certificate) |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Safety functions | 13 safety functions according to ISO 13849-1, certified by TÜV Rheinland |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Personnel detection safety function | Triggered when obstacles or people are detected too close to the robot |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Emergency stop | Four E-stop buttons, one in each corner; E-stop connector in electrical interface and joystick interface |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Overspeed avoidance | Prevents driving faster than predefined safety limit |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Collision avoidance | Triggered by a human or obstacle in the path of travel |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Safe guarded stop | yes |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Safe load position | Triggered if speed exceeds 0.3 m/s while lift/carrier is being lowered or raised |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Manual control in robot interface | Token-based access; one token at a time |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Audio | Speaker |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Status light | 4 LED bands indicating robot status |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |
| Signal lights | 8, indicating driving behavior and direction |  | [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf) |

## Documents

- [MiR600 Specifications (2025-09-01, MiR, distributor-hosted PDF)](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf)

## Sources

- Official page: [mobile-industrial-robots.com](https://mobile-industrial-robots.com/products/robots/mir600)
- [mobile-industrial-robots.com](https://mobile-industrial-robots.com/products/robots/mir600/specifications)
- [ai.motion.com](https://ai.motion.com/wp-content/uploads/2025/10/MiR600-Specifications-2.99.pdf)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-17). Source repository: https://github.com/htcrefactor/robot-catalog*
