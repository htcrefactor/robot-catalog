# Mobile Industrial Robots (MiR) MiR1200 Pallet Jack

> Autonomous pallet jack that detects, lifts and delivers EU pallets up to 1,200 kg using AI-based perception.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=mir-mir1200-pallet-jack
- Category: AMR
- Locomotion: Wheeled
- Manufacturer: Mobile Industrial Robots (MiR) (Denmark)
- Verification: not recorded

## Core specs

| Field | Value |
|---|---|
| Length | 1,934 mm |
| Width | 820 mm |
| Height | 2,120 mm |
| Weight | 750 kg |
| Payload | 1,200 kg |
| Max speed | 1.5 m/s (5.4 km/h) |
| Runtime | 10 h |
| IP rating | IP52 |
| Status | Commercial |
| Sensors | 3x SICK safety laser scanners (360°), 5x 3D cameras, 1x 3D LiDAR, 1x ultrasonic sensor (pallet-on-fork check), AI-based pallet detection |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

74 values from 3 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Robot type | Autonomous Mobile Robot (AMR), pallet jack |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Color | RAL 7011 / Iron Gray |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Product design life | 5 years or 20 000 hours of active operation, whichever comes first |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Specification document date | 2025-09-01 | spec v2.102 | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Launch date | 2024-03-19 |  | [mobile-industrial-robots.com](https://mobile-industrial-robots.com/blog/mir1200-pallet-jack-using-ai-to-revolutionize-pallet-handling) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 1,934 mm |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Width | 820 mm |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Height | 2,120 mm |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Weight | 750 kg |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Weight distribution (no payload) | Drive wheel 500 kg; each caster wheel 150 kg; each support leg roller 100 kg |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Turning radius | 1,564 mm |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Maximum payload | 1,200 kg |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Maximum speed | 1.5 m/s | with maximum payload on a flat surface (5.4 km/h) | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Maximum acceleration | 0.3 m/s² | no payload | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Drive system | Tricycle drive (developed with Logitrans) |  | [mobile-industrial-robots.com](https://mobile-industrial-robots.com/blog/mir1200-pallet-jack-using-ai-to-revolutionize-pallet-handling) |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Operational corridor width | 2.1 m | EPAL 1 at full speed; 1.55 m at reduced speed | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Corridor width for a 90° turn | 1.9 m | EPAL 1 | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Corridor width for a U-turn | 1.95 m | EPAL 1 | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Operational width for pivoting | 2.75 m | EPAL 1 | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Operational doorway width | 1.4 m | EPAL 1 | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Corridor width for two robots passing | 3.8 m | EPAL 1 at full speed; 2.90 m at reduced speed | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Pallet space requirements (EPAL 1) | In front of floor pallets: 3.5 m (front entry) / 2.7 m (side entry); raised stations: 2.9 m; between pallets: 0.30 m side-to-side, 0.25 m end-to-end; sides 0.3 m; behind 0.35 m |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Surface deviation for pallet pick/place | ±1° | EPAL 1 | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Floor conditions | Clean and dry |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Maximum slope at rated load | 0 % |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Maximum step at rated load | 10 mm | at 0.5 m/s | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Floor-to-wheel friction coefficient | 0.60–0.80 |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery type | Lithium-ion, 3 pcs |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Number of batteries | 3 |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Battery weight | 11 kg | per battery | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Battery dimensions | 545 × 201 × 75 mm | per battery | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Battery cycle life | 3,000 cycles | minimum full cycles before capacity drops below 80% | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Battery voltage (nominal) | 47.7 V | minimum 42 V, maximum 54 V | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Battery capacity (Ah) | 102.6 Ah |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Active operation time, mixed payload | 7 h 40 min | 90–10% | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Active operation time, maximum payload | up to 10 h |  | [mobile-industrial-robots.com](https://mobile-industrial-robots.com/products/robots/mir1200-pallet-jack/specifications) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Docking / undocking time, charging station | up to 18 s / up to 9 s |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Minimum space in front of charging station | 4 m | single station; 4.60 m in front of a line of stations | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Minimum distance between charging stations | 0.6 m |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Charging options | Charge 48V 35A; Charge 48V 105A; MiR Charge 48V (requires non-reflective mat); Battery Charger 48V 12A; Battery Charger 48V 650W 13.5A; Battery Charger 48V 1200W 13.5A; Cable Charger Lite 48V 3A |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Charging-to-runtime ratio | 1:14 |  | [mobile-industrial-robots.com](https://mobile-industrial-robots.com/blog/mir1200-pallet-jack-using-ai-to-revolutionize-pallet-handling) |
| Opportunity charging | yes |  | [mobile-industrial-robots.com](https://mobile-industrial-robots.com/blog/mir1200-pallet-jack-using-ai-to-revolutionize-pallet-handling) |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| IP rating | IP52 |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Environment | Indoor use only |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Operating ambient temperature | 5–25 °C | continuous use; maximum 40 °C for 1 hour | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Storage temperature | −20 to 60 °C | 1 month; −20 to 45 °C for 3 months | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Humidity | 20–95 % | non-condensing | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Optimal light conditions | Even and steady lighting; strong directional light can cause false obstacle detections |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Materials not reliably detected | Transparent, translucent, glossy, reflective and light-emitting |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Safety laser scanners | 3 SICK scanners (front and rear), 360° personnel detection |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| 3D cameras | 5 | pallet and obstacle detection | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| 3D LiDAR | 1 on top of robot, for obstacle detection |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Ultrasonic sensor | 1 | detects pallets securely placed on forks | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Pallet detection | AI-based pallet detection |  | [mobile-industrial-robots.com](https://mobile-industrial-robots.com/blog/mir1200-pallet-jack-using-ai-to-revolutionize-pallet-handling) |
| Obstacle detection | LiDAR and 3D vision fused for floor, overhead and surrounding obstacles |  | [mobile-industrial-robots.com](https://mobile-industrial-robots.com/blog/mir1200-pallet-jack-using-ai-to-revolutionize-pallet-handling) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| AI compute module | NVIDIA Jetson AGX Orin | full perception stack accelerated on GPU | [mobile-industrial-robots.com](https://mobile-industrial-robots.com/blog/mir1200-pallet-jack-using-ai-to-revolutionize-pallet-handling) |
| Pallet detection model training data | 1.2 million+ real and synthetic images |  | [mobile-industrial-robots.com](https://mobile-industrial-robots.com/blog/mir1200-pallet-jack-using-ai-to-revolutionize-pallet-handling) |
| Fleet software | MiR Fleet; MiR Insights |  | [mobile-industrial-robots.com](https://mobile-industrial-robots.com/blog/mir1200-pallet-jack-using-ai-to-revolutionize-pallet-handling) |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Maximum lift height | 1,120 mm |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Maximum fork lifting height | 1,140 mm | as stated on product web page | [mobile-industrial-robots.com](https://mobile-industrial-robots.com/products/robots/mir1200-pallet-jack/specifications) |
| Maximum height for automatic pallet pick-up/place | 850 mm |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Fork dimensions | L 1182 mm; W 188 mm; outer-edge distance 560 mm; inner-edge distance 184 mm; height 63 mm |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Support leg dimensions | L 880 mm; H 85 mm |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Pallet types | EPAL 1 (grade A/B); EPAL 3 (grade A/B); 1250 × 1250 mm (48″×48″) carts; 45″ × 48″ nestable pallets |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Maximum payload height | 2,000 mm |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Pallet pick-up / place time | front entry: up to 40 s / 30 s; left or right entry: up to 55 s / 50 s |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Designated use | Automated driverless conveyance of heavy loads |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Maximum noise level | 77.3 dB |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Safety standards (design basis) | EN ISO 12100:2010; ISO 13849-1:2023; EN ISO 13850:2015; EN ISO 3691-4:2023 |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| EMC | EN IEC 61000-6-4:2007/A1:2011; EN IEC 61000-6-2:2005/AC:2005; EN 12895:2015+A1:2019 |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Audio | Speaker and safety buzzer |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Status light | 4 LED bands indicating robot status |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Signal lights | 4, indicating driving behavior and direction |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |
| Blue light | 1 projector, blue light 420 cm in front of the robot to alert personnel |  | [einsrobotics.com](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf) |

## Documents

- [MiR1200 Pallet Jack Specifications v2.102 (2025-09-01, MiR, distributor-hosted PDF)](https://einsrobotics.com/wp-content/uploads/2026/03/MiR1200_20Pallet_20Jack_20Specifications_202.102.pdf)
- [MiR1200 Pallet Jack specifications page (MiR)](https://mobile-industrial-robots.com/products/robots/mir1200-pallet-jack/specifications)
- [MiR1200 Pallet Jack launch press release (MiR, 2024-03-19)](https://mobile-industrial-robots.com/blog/mir1200-pallet-jack-using-ai-to-revolutionize-pallet-handling)

## Sources

- Official page: [mobile-industrial-robots.com](https://mobile-industrial-robots.com/products/robots/mir1200-pallet-jack)
- [mobile-industrial-robots.com](https://mobile-industrial-robots.com/products/robots/mir1200-pallet-jack/specifications)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-16). Source repository: https://github.com/htcrefactor/robot-catalog*
