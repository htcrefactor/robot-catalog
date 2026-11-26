# Starship Technologies Starship delivery robot

> Six-wheeled insulated sidewalk robot delivering groceries and food within about 2 miles, the most deployed fleet worldwide.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=starship-delivery-robot
- Category: Outdoor delivery
- Locomotion: Wheeled
- Manufacturer: Starship Technologies (United States)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Weight | 38 kg |
| Max speed | 1.78 m/s (6.4 km/h) |
| Wheels | 6 |
| Runtime | 18 h |
| Status | Commercial |
| Price | weight ~38 kg without cargo and speed ~6.4 km/h are approximate per FAQ; carries up to three shopping bags |
| Sensors | 12 cameras (incl. time-of-flight), Radar, Ultrasonic sensors |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

26 values from 2 documents, checked against maker sources on 2026-11-04.

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Weight (empty) | approx. 38 kg | without cargo (83 lb) | [starship.xyz](https://www.starship.xyz/faq/) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Speed | ~6.4 km/h | ~4 mph; speed of a walking pedestrian | [starship.xyz](https://www.starship.xyz/faq/) |
| Wheels | 6 | six wheels with bogie system | [starship.xyz](https://www.starship.xyz/our-robots/) |
| Suspension | Bogie system |  | [starship.xyz](https://www.starship.xyz/our-robots/) |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Curbs | Climbs and dismounts curbs | 6-wheel bogie | [starship.xyz](https://www.starship.xyz/our-robots/) |
| Surfaces | Sidewalks/pavements, pedestrianised areas; road and driveway crossings at mapped crossing points |  | [starship.xyz](https://www.starship.xyz/faq/) |
| Localization | Computer vision + GPS, proprietary mapping | "to the nearest inch" | [starship.xyz](https://www.starship.xyz/faq/) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Runtime | 18 h | single charge | [starship.xyz](https://www.starship.xyz/our-robots/) |
| Delivery radius | generally within 2 miles of stores | varies by area | [starship.xyz](https://www.starship.xyz/faq/) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charging | Wireless charging installations (overnight, onsite) |  | [starship.xyz](https://www.starship.xyz/our-robots/) |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| Weather | All weather incl. rain and snow; winter wheels |  | [starship.xyz](https://www.starship.xyz/our-robots/) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Cameras | 12 | including time-of-flight | [starship.xyz](https://www.starship.xyz/our-robots/) |
| Radar | yes |  | [starship.xyz](https://www.starship.xyz/our-robots/) |
| Ultrasonic sensors | yes |  | [starship.xyz](https://www.starship.xyz/our-robots/) |
| Time-of-flight | yes |  | [starship.xyz](https://www.starship.xyz/faq/) |
| Object detection range | up to 200 ft |  | [starship.xyz](https://www.starship.xyz/faq/) |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Integration API | Delivery by Starship API for partners |  | [starship.xyz](https://www.starship.xyz/faq/) |
| On-device safety | Critical safety functions run locally even without internet |  | [starship.xyz](https://www.starship.xyz/our-robots/) |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Capacity | up to three shopping bags | insulated interior (not heated/refrigerated) | [starship.xyz](https://www.starship.xyz/our-robots/) |
| Insulated cargo lining | yes | keeps hot, cold and frozen items at temperature | [starship.xyz](https://www.starship.xyz/faq/) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Obstacle behavior | Slows for adjacent objects, full stop for objects in front |  | [starship.xyz](https://www.starship.xyz/faq/) |
| Anti-tamper | Siren on tampering; tracked location; lid locked, opened via customer app |  | [starship.xyz](https://www.starship.xyz/faq/) |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Autonomy level | Level 4 (since 2018), >99% autonomous, remote assistance on standby |  | [starship.xyz](https://www.starship.xyz/our-robots/) |
| Remote assistance | Human remote assistants via low-resolution obfuscated video feed |  | [starship.xyz](https://www.starship.xyz/faq/) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Lights | LEDs and reflectors on flag; headlights; rear indicators | night lights visible ≥ 500 ft | [starship.xyz](https://www.starship.xyz/faq/) |
| Audio | Audio alert system; plays music on delivery |  | [starship.xyz](https://www.starship.xyz/faq/) |

## Documents

- [Our Robots (Starship Technologies)](https://www.starship.xyz/our-robots/)
- [FAQ (Starship Technologies)](https://www.starship.xyz/faq/)

## Notes

Maker pages: our-robots lists 12 cameras including time-of-flight, radar, ultrasonic sensors, six wheels with a bogie system, 18 h battery and up to three shopping bags; the FAQ states approx. 38 kg without cargo and ~4 mph (6.4 km/h). Battery capacity and dimensions are not published.

## Sources

- Official page: [starship.xyz](https://www.starship.xyz/our-robots/)
- [starship.xyz](https://www.starship.xyz/faq/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-26). Source repository: https://github.com/htcrefactor/robot-catalog*
