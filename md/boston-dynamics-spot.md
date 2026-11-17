# Boston Dynamics Spot

> Agile industrial quadruped for autonomous inspection, data capture and hazardous-area response, extendable with payloads and an arm.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=boston-dynamics-spot
- Category: Quadruped
- Locomotion: Legged
- Manufacturer: Boston Dynamics (United States)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 1,100 mm |
| Width | 500 mm |
| Height | 610 mm |
| Weight | 33.8 kg |
| Max speed | 1.6 m/s (5.8 km/h) |
| Runtime | 1.5 h |
| Battery | 564 Wh |
| IP rating | IP54 |
| Status | Commercial |
| API | yes |
| SDK | yes |
| SDK name | Spot SDK (Python client + gRPC/protobuf API) |
| Sensors | 360° terrain-sensing cameras (4 m range) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

319 values from 4 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Hardware model (P/N) | 04-00143531-001 | Spot hardware model covered by IFU 5.1.5 | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.1 p.6 |
| Hardware model (P/N) | 04-00143531-401 | Model with red E-Stop button and A/V warning system | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.1 p.6; §1.5.1 p.10 |
| Hardware model (P/N) | 04-00143531-601 | Model with A/V warning system | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.1 p.6; §2.7 p.22 |
| Hardware model (P/N) | 04-00143531-611 | Model with A/V warning system | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.1 p.6; §2.7 p.22 |
| Model number location | Label inside Spot's battery compartment |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.7 p.22 |
| Software version | 5.1 | IFU Version 5.1.5 Original Instructions, April 2026 | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.1 p.6 |
| Manufacturer | Boston Dynamics, Inc., 200 Smith St., Waltham, MA 02451, USA; +1 617-868-5600 |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.2 p.6 |
| Robot type | Quadruped (four-legged) legged robot | Oblong rectangular body housing computers, cameras and other components | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.3 p.7; §1.5.1 p.10 |
| Serial number format | BD-XXXXXXXX; first digit = year of production (from 2018: 8, 9, then 0 = 2020) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.29 |
| Label part number | 04-00385327-001 |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §7.2 p.143 (label image) |
| Country of origin | Designed in Massachusetts, made in USA |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §7.2 p.143 (label image) |
| Hardware variants covered | 04-00143531-001; -401 (E-Stop button + A/V warning); -601 (A/V warning); -611 (A/V warning) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.1 p.6; §2.5.4 p.19; §2.7 p.22 |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 1,100 mm |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.10 |
| Width | 500 mm |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.10 |
| Default height (walking) | 610 mm |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.10 |
| Height (sitting) | 191 mm |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.10 |
| Max height (walking) | 700 mm |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.10 |
| Min height (walking) | 520 mm |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.10 |
| Net mass (with battery) | 33.8 kg |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.10 |
| Net mass (with battery), datasheet | 32.7 kg | Datasheet updated 05/22/2024 (IFU 5.1.5: 33.8 kg) | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.2 Base Robot |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Degrees of freedom | 12 |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.10 |
| Max nominal speed | 1.6 m/s | Forward velocity of the body under nominal environmental/navigational conditions; individual legs can move faster | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.10 |
| Gaits and locomotion modes | Walk (trot, default); Crawl (three feet always on ground); Quick-step slip prevention; Stairs Mode (automatic) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.4.1 p.15 |
| Max velocity, speed setting Fast | 1.6 m/s | Manual operation, Walk gait | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.4.2 p.16 |
| Max velocity, speed setting Med (default) | 0.9 m/s | Manual operation, Walk gait | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.4.2 p.16 |
| Max velocity, speed setting Slow | 0.5 m/s | Manual operation, Walk gait | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.4.2 p.16 |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Minimum coefficient of friction | 0.4 | Nominal surface condition | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.27 |
| Debris/uneven surface height variation | 25 cm | Nominal: height variations up to 25 cm | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.27 |
| Minimum surface stiffness | 8 kN/m | Avoid soft or pliable surfaces below this | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.27 |
| Minimum height of overhanging obstacles | 70 cm |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.28 |
| Minimum doorway, gap or corridor width | 60 cm | Forward/reverse direction of travel | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.28 |
| Minimum space to turn around (rotate in place) | 122 x 122 cm | L x W | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.28 |
| Maximum slope pitch | 30 ° | +/- 30 degrees | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.28 |
| Maximum height of negative obstacles (step up or down) | 35 cm | Elevated ground | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.28 |
| Max lateral motion of walking surface | 5 cm | Elevated ground must be stable: less than 5 cm lateral motion | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.28 |
| Minimum stairway width | 64 cm |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.28 |
| Maximum stairway pitch | 45 ° | +/- 45 degrees | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.28 |
| Maximum stair step height | 22 cm |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.28 |
| Stair side barriers | At least 50 cm high, gaps no more than 30 cm wide |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.28 |
| Stair direction of travel | Straight (no curvature or turns except on flat landings) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.28 |
| Min stair runout space at top and bottom | 122 x 122 cm | L x W (L = direction of travel) | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.28 |
| Min straight landing (no turn) | 122 x 64 cm | L x W | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.28 |
| Min landing, 90° turn between flights | 122 x 122 cm | L x W | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.28 |
| Min landing, 180° turn between flights | 122 x 244 cm | L x W | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.28 |
| Obstacle height step-over threshold | 30 cm | Objects shorter than 30 cm: Spot attempts to step on/over; taller: attempts to avoid | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.2 p.30 |
| Surfaces that may interfere with navigation | Reflective (mirrored) surfaces; transparent objects/barriers; bright ambient light or dark matte surfaces; repeating patterns of vertical lines; grated floors |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.2 p.30 |
| Minimum fiducials to start automatic mode | 1 | At least one for initial localization; one at each Autowalk start; not required for manual operation | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.9.1 p.71; §4.9.4 p.73 |
| Ideal wall-mounted fiducial height | 45 to 60 cm | Above ground | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.9.4 p.73 |
| Fiducial spacing in feature-poor areas | 3 m | Every 3 m in long hallways or open fields; one at each intersection | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.9.4 p.73 |
| Navigation method | Vision-based navigation with AprilTag fiducials and visual features; lidar attachments may replace/supplement and need fewer fiducials |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.9.4 p.73-74 |
| Ground Height Detection obstacle height | 30 cm | Helps navigate over obstacles approximately 30 cm or less | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.8.1.7 p.105 |
| Path planner range, Short range (default) | 2 m | Uses data within 2 m; may deviate 1.5 m from route if blocked | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.9.2.2 p.124 |
| Path planner range, Long range | 8 m | Uses data within 8 m (live only, or live + recorded); may deviate 3 m from route if blocked | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.9.2.2 p.124 |
| Max route deviation when blocked, short range | 1.5 m |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.9.2.2 p.124 |
| Max route deviation when blocked, long range | 3 m |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.9.2.2 p.124 |
| Stair traversal rules | Climb forward straight up; always descend rear-first; no turning or side-stepping on stairs; grated, open-riser or transparent stairs pose perception challenges | Stay >=2 m from bottom of stairs/inclines with Spot active | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.10 p.126-128 |
| Max step height | 300 mm | Product page 'Locomotion' figure (IFU nominal step up/down for elevated ground: 35 cm; stairs: 22 cm) | [bostondynamics.com](https://bostondynamics.com/products/spot/) · Spot Specifications > Base Robot > Locomotion |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery capacity | 564 Wh |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.10 |
| Max battery voltage | 58.8 V |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.10 |
| Typical runtime | 90 min | Approximately | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.10 |
| Typical runtime when powering attachments | 60 min | Approximately | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.11 |
| Standby time | 180 min | Spot powered, motors off | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.10 |
| Battery mass | 5.2 kg |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.11 |
| Power supply design | Separated extra low voltage (SELV), <60 VDC; meets IEC 60204-1 (electrical equipment) and IEC 62133 (batteries) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.9.2 p.31 |
| Battery certifications | UN 38.3 transportation testing; CB Certification to IEC 62133; drop tested with no electrolyte leakage | Cells fully enclosed in sealed enclosure | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.9.5 p.35 |
| Max time battery may be left in powered-off robot | 24 h | Batteries left in a powered-off robot >24 h may be damaged beyond repair (unless on Power Supply or powered Dock) | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §3.3.1 p.47 |
| Battery chemistry | Lithium-ion |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §3.3.1 p.47 |
| Battery state-of-charge indicator | Push-button LED bar indicator on battery |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §3.3.1 p.47 |
| Removable battery | Yes - removable lithium-ion battery pack, inserted into rear of battery compartment with latching handle |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.3 p.59; §4.3.1 p.60 |
| Battery charge as shipped | <30 % | Charge every new battery to 100% promptly; over-discharged batteries may not be repairable | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.3 p.59 |
| Battery location | Compartment in bottom panel; SoC button with five LED indicators on battery face |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.1 p.75 |
| Battery dimensions (L x W x H) | 324 x 168 x 93 mm |  | [bostondynamics.com](https://bostondynamics.com/products/spot/) · Spot Specifications > Battery & Payload |
| Max battery internal operating temperature | 75 °C |  | [support.bostondynamics.com](https://support.bostondynamics.com/s/article/spot-specifications) · Power table |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Spot Power Supply power output | 400 W |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.10 |
| Max charge current | 7 A |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.10 |
| Time to charge (Spot Dock) | 50 min | Approximately 50 min to 80% at 25 °C Spot Dock ambient | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.11 |
| Time to charge (Spot Dock) | 120 min | Approximately 2 h to 100% at 25 °C Spot Dock ambient | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.11 |
| Time to charge (Spot Dock) | 150 min | Approximately 2.5 h to 80% at 35 °C Spot Dock ambient | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.11 |
| Time to charge (Spot Dock) | 210 min | Approximately 3.5 h to 100% at 35 °C Spot Dock ambient | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.11 |
| Time to charge (Spot Power Supply) | 60 min | Approximately 1 hour | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.11 |
| Charging methods | Battery removed, with Spot Power Supply; installed in Spot, with Spot Power Supply; installed in Spot, on Spot Dock | Only BD Spot Dock or Spot Power Supply; do not operate Spot while connected to Power Supply | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.3.3 p.61-63 |
| Docking station | Spot Dock - recharging station with Ethernet pass-through | Installed on level ground | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.4 p.64 |
| Spot Dock clear space, front | 1,200 mm |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.4 p.64 |
| Spot Dock clear space, sides | 600 mm | Rear value left blank in source | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.4 p.64 |
| Docking procedure | Autonomous: orient rear to dock, walk backward, align with fixtures, lower body onto charging pins on rear tower, lift legs and power off motors; undock: unfold legs, stand, walk forward | Uses perception system to recognize dock; dock pins connect power and Ethernet | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.7 p.93 |
| Dock fiducial detection distance | 4 m | Generally within 4 m the dock fiducial is highlighted on controller | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.7.1 p.95 |
| Autonomous recharging in missions | Start/end mission at any included dock; recharge between looping/scheduled missions; auto return to dock on low battery; configurable target charge levels |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.7.2 p.96 |
| Mission docking behavior settings | Minimum charge for undocking; charge to return to dock (set significantly lower) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.9.2.2 p.123 |
| Spot Dock dimensions (L x W x H) | 1140 x 414 x 403 mm |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.2 Spot Dock |
| Spot Dock mass | 22.9 kg |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.2 Spot Dock |
| Spot Dock input | 90-277 V AC |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.2 Spot Dock |
| Spot Dock output | 58 V at 12 A |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.2 Spot Dock |
| Spot Dock charge time range | 2 to 3.5 h | Varies with ambient temperature (25 °C: 50 min to 80%, 2 h to 100%; 35 °C: 2.5 h / 3.5 h) | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.2 Spot Dock |
| Spot Dock operating temperature | 0 to 35 °C | Ambient light required; bolt/tie-down mounting locations | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.2 Spot Dock |
| Spot Dock connectivity | Gigabit Ethernet passthrough to robot |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.2 Spot Dock |
| Spot Dock certification | cTUVus certified to UL 1564 and CSA C22.2 No. 107.2 |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.2 Spot Dock |
| Charger input | 100-240 V AC, 50/60 Hz, 8 A max | Spot Power Supply | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.2 Charger |
| Charger output | 35-58.2 V DC, 12 A max | Spot Power Supply | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.2 Charger |
| Charger dimensions (L x W x H) | 380 x 315 x 178 mm |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.2 Charger |
| Charger mass | 7.5 kg |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.2 Charger |
| Charger operating temperature | 0 to 45 °C |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.2 Charger |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| Minimum ambient light for clear camera visuals | 50 lux |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.28 |
| Dynamic range of ambient light | 68 dB |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.28 |
| Lighting interference | High-contrast light including IR wavelengths (e.g. sunlight) may interfere with obstacle detection |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.28 |
| Ingress protection | IP54 |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.29 |
| Operating ambient temperature | -20 to 45 °C | Serial numbers BD-80010001 to BD-93650001 and BD-00010001 to BD-41199999 | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.29 |
| Operating ambient temperature | -20 to 55 °C | Serial numbers BD-41200001 and higher | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.29 |
| Maximum humidity | 99 % RH | Non-condensing | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.1 p.29 |
| Energy sources that may interfere with navigation | Near-IR (780-2500 nm) light sources pointed at Spot; high-contrast light with IR wavelengths (e.g. sunlight) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.2 p.30 |
| Water resistance | Resistant to light sprays of water; must not be sprayed with water jets or submerged (permanent damage) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §6.2.1 p.134 |
| Terrain sensing lighting requirement | >2 lux | Product page figure; IFU: 50 lux for clear camera visuals | [bostondynamics.com](https://bostondynamics.com/products/spot/) · Spot Specifications > Terrain Sensing |
| Minimum power-on temperature | 0 °C | Robot must be powered on at a minimum of 0 °C (operating range -20 to 55 °C) | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.2 Environment |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Camera functions | Black-and-white or color fisheye; range (depth); infrared |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.11 |
| Number of optical cameras | 5 | front-left, front-right, left, right, rear; for image capture, fiducial recognition, displaying surroundings | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.11 |
| Overall optical field of view | 360 ° |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.11 |
| Number of depth cameras | 5 stereo pairs | front-left, front-right, left, right, rear; for robot perception and obstacle avoidance | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.11 |
| Overall depth camera field of view | 90 ° | Approximately, in each direction; gaps near the hips where FOV does not overlap | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.11 |
| Depth camera range | 2 m | Approximately | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.11 |
| Camera (obstacle) sensing range | 2 m | Cannot detect obstacles directly above Spot; gaps at rear corners | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.2 p.29 |
| Minimum obstacle area/width | 3 cm |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.8.2 p.30 |
| Fiducial tag family | AprilTag Tag36h11 | Printed on white non-glossy US letter-size sheets (preferably rigid); outdoor: acrylic adhesive white vinyl with matte laminate | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.3 p.7; §4.9.2 p.72 |
| Default fiducial image size | 146 mm | Square; custom size ranges configurable in Admin Console (start ID, end ID, image size; reboot to apply) | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.3 p.7; §4.9.2-4.9.3 p.72-73 |
| Fiducial ID ranges | 1-299 localization (automatic operation); 520-549 Spot Dock IDs; 580-584 Spot Dock IDs for Spot Station; 585-586 mission interrupts | Fiducials outside these ranges should not be used; 500-series reserved | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.9.1 p.71; §4.9.4 p.74 |
| Top-down view | Simulated top-down view of environment from body camera images and depth data |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.8.1.4 p.101 |
| Joint sensors | Load cell sensors and joint position sensors for hip and knee joints | Tested/recalibrated by SpotCheck | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §6.3 p.135 |
| Camera calibration panel | Flat board approx. 118.5 x 50 cm with 18 evenly spaced fiducials on black background and 'Up' arrows; mounted vertically (bottom edge <=5 cm from floor) or within 5° of vertical; Spot ~1 m in front, rear camera facing |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §6.3.2 p.138-139 |
| Terrain sensing range | 4 m | Product page figure; IFU gives depth camera range approx. 2 m | [bostondynamics.com](https://bostondynamics.com/products/spot/) · Spot Specifications > Terrain Sensing |
| Terrain sensing horizontal field of view | 360 ° |  | [bostondynamics.com](https://bostondynamics.com/products/spot/) · Spot Specifications > Terrain Sensing |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| Admin Console | Web server hosted locally on Spot; browser-based (Chrome) system settings; accessible from Spot App | Pages: User Management, Network Setup, Software Update, Spot License, Logs, About, Payloads, General Settings, Battery, WiFi Dashboard, Visualizer | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.5 p.64; §4.5.2 p.65-66 |
| Admin Console functions | User management; network setup and diagnostics; software update; license install; log management/upload, image logging toggle; rename; cumulative runtime data; payload config; auto log upload toggle; fiducial size/ranges; factory reset; battery health metrics; WiFi connection history; limb/payload visualizer |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.5.2 p.65-66 |
| Spot license | License files required for Spot operation, installed via Admin Console |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.5.2 p.65 |
| Software support policy | Current and previous minor releases (e.g. x.1 and x.0) plus all patch versions | Do not skip intermediate major/minor releases | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.8 p.69 |
| Software update method | Upload .bde file via Admin Console (Spot on Dock or Power Supply); tablet Spot App updates bundled with robot software | Downloads at support.bostondynamics.com/s/spot/downloads | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.8.1 p.70; §4.8.2 p.70 |
| Tablet app software | Spot App (.apk) for Android; updates bundled with robot software or manual install via USB/download |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.8.2 p.70-71 |
| Attachment software updates | Per-attachment versions with compatibility chart on Spot Downloads page |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.8.3 p.71 |
| Diagnostic log capture | REPORT BUG: previous 30 s of operational data; START LOG: up to 10 min of new data (continues up to 21 s after controller connection loss) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.8.1.8 p.106 |
| Factory reset | Admin Console > General Settings; ~5 min; resets accounts, network, nickname, payloads, logs, data; keeps software version and license; optional Zeroize SSD |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §6.4 p.140-141 |
| Storage | SSD (writable portion can be zeroized on factory reset) | Capacity not stated | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §6.4 p.140 |
| API / SDK | Spot API for third-party control, sensor reading and attachment communication (dev.bostondynamics.com) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §9 p.146 |
| Additional API licenses | Joint-level control API (research, lab use); Choreography API (performances: preset moves library + custom animations) | Outside intended use; regulatory declarations no longer apply | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §9 p.146; §9.1-9.2 p.147 |
| SDK language | Python SDK | Flexible API and Python SDK | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.1 Features |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Wi-Fi | Enterprise Wi-Fi, 2.4 GHz and 5 GHz, 802.11b/g/n and 802.11ac |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.12 |
| Ethernet | 1000Base-T |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.12 |
| Radio module | Wi-Fi radio module; meets requirements for intentional radiators |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.9.3.2 p.33 |
| Supported network types | Wi-Fi (own access point or join enterprise Wi-Fi); Ethernet (1 rear port, or Dock pass-through - one at a time); LTE (additional hardware); mesh radio (additional hardware) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.6 p.66-67 |
| Ethernet ports | 1 | At rear of Spot; Dock pass-through is electrically identical - use only one | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.6 p.66 |
| Cellular | LTE - requires additional hardware |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.6 p.67 |
| Mesh radio | Requires additional hardware |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.6 p.67 |
| Default Wi-Fi mode | Access Point (Spot hosts its own Wi-Fi network); SSID and password on label in battery compartment | Switch Client->AP by pressing motor lockout button 6 times | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.6.1 p.67 |
| Default robot IP (Wi-Fi) | 192.168.80.3 | Admin Console at https://192.168.80.3 | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.6.1 p.67; §4.5.1 p.65 |
| Default robot IP (Ethernet) | 10.0.0.3 | Netmask 255.255.255.0; Admin Console at https://10.0.0.3 | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.6.1 p.67; §4.5.1 p.65 |
| Default Ethernet netmask | 255.255.255.0 | Direct wired connection | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.6.1 p.67 |
| Network check | Built-in suite of network checks (e.g. DNS) via Admin Console |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.6.3 p.68 |
| Rear panel controls and ports | Charging port with cover (top-center); power button, motor lockout button, Ethernet port with cap (lower, left to right) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.1 p.75 |
| FCC ID | 2AG87ACM-DB-2M-R2 | From nameplate | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §7.2 p.143 (label image) |
| ISED Canada (IC) ID | ACMDB2MR2 | CAN ICES-003(A)/NMB-3(A) | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §7.2 p.143 (label image) |
| Other radio approvals on label | KC R-R-BDi-4-00143531-001; Japan radio R 210-155198; ICASA TA-2021-1635; IMDA DA105282 |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §7.2 p.143 (label image) |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Max recommended attachment mass | 20.43 kg | Best when centered directly on top of body; tall, off-center or cantilevered payloads may impact performance even below limit | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.11 |
| Max power per payload port | 150 W |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.11 |
| Payload ports (attachment I/Os) | 2 | Mirrored (front and rear) | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.11 |
| T-slot rail bolt size | M5 x 1.0 |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.2 p.11 |
| Radio antenna co-location threshold | 20 cm | Multiple radio modules on attachments must have antennas >20 cm apart or be tested as co-located | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.2.1 p.51 |
| Mounting rails | Aluminum T-slot rails along top left and top right edges of body; accept T-slot nuts such as Misumi HNTR5-5 |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.2.2 p.52 |
| Payload port locations | Forward and rear payload ports provide power and data |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.2.2 p.52 |
| Mounting rail spacing (across body) | 160 / 176 mm | Dimensions shown in mounting drawing between rails (inner/outer) | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.2.2 p.53 (figure) |
| Rail bolt positions from frontmost rail bolt | 0, 83, 166, 249, 332, 415 mm mm | Origin = frontmost rail bolt; also 207.5 mm and 476.5 mm reference marks in drawing | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.2.2 p.53 (figure) |
| Payload mount reference frame | Origin at frontmost rail bolt on centerline; +x forward, +y left, +z up | Per figure | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.2.2 p.53 (figure) |
| Max recommended body-mounted attachment width | 190 mm | Avoid hip-adjacent zones (125 mm clear width between hip zones up to 70 mm height shown in figure) | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.2.2 p.53 |
| Max recommended body-mounted attachment length | 850 mm | Overhang front/rear reduces maneuverability | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.2.2 p.54 |
| Attachment mass distribution | 20.43 kg total combined over top of body; best with combined CoM between front and rear hips, ideally centered; keep CoM low for self-right |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.2.2 p.54-55 |
| Tools to mount an attachment | Cross-head screwdriver; 4 mm hex wrench/Allen key |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.2.3.1 p.55 |
| Tools to mount/remove an attachment | 2 mm hex wrench/Allen key (T-slot nut set screw) | In addition to cross-head screwdriver and 4 mm hex key | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.2.3.1 p.56; §4.2.4.1 p.57 |
| Attachment mounting screw torque | 5 N·m | Machine screws into T-slot nuts; do not over-tighten | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.2.3.1 p.56 |
| Attachment mounting screws | M5 machine screws into T-slot nuts; some attachments use locating pins in top panel holes |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.2.4.1 p.57 |
| Payload port connection | Ribbon-cable connector fastened with screws; unused ports must be capped (Spot cannot operate with an exposed payload port) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.2.3.1 p.56; §4.2.4.1 p.57 |
| Payload software configuration | Configured in Admin Console Payloads page (some auto-register; front or rear mount configs); attach/detach toggle in Spot App; stored configs reused |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.2.3.2 p.56-57; §4.2.4.2 p.58 |
| Payload interface documentation | Payload Developer Guide; Robot Electrical Interface (dev.bostondynamics.com/docs/payload/) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · Appendix A p.144 |
| Payload max weight (product page) | 14 kg | Marketing payload capacity on product page and datasheet; IFU §1.5.2 gives max recommended attachment mass 20.43 kg | [bostondynamics.com](https://bostondynamics.com/products/spot/) · Spot Specifications > Payload Mounting |
| Payload mounting area (L x W x H) | 850 x 240 x 270 mm |  | [bostondynamics.com](https://bostondynamics.com/products/spot/) · Spot Specifications > Payload Mounting |
| Payload port connector | DB25 (2 ports) |  | [bostondynamics.com](https://bostondynamics.com/products/spot/) · Spot Specifications > Payload Mounting |
| Payload port supply voltage | 35 to 58.8 V DC | Unregulated DC, 150 W per port | [bostondynamics.com](https://bostondynamics.com/products/spot/) · Spot Specifications > Payload Mounting |
| Payload integration | Software API and hardware interface control document available |  | [bostondynamics.com](https://bostondynamics.com/products/spot/) · Spot Specifications > Payload Mounting |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Spot Arm | Optional actuated attachment (Spot Arm with gripper and gripper camera); SpotCheck recalibrates gripper and checks arm joint sensors | Requires separate risk assessment; see Spot Arm Information for Use | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.2.1 p.51; §6.3.3 p.140 |

### Actuation & Joints

| Spec | Value | Note | Source |
|---|---|---|---|
| Motors per leg | 3 | Three motors in each leg | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.3 p.7; §2.1 p.13 |
| Number of legs | 4 |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.1 p.10 |
| Leg joint layout | Ball joint at hip (upper leg to body); hinged knee (upper to lower leg); rounded foot with rubberized pad |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.1 p.10 |
| Foot type | Rounded foot with rubberized pad |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.1 p.10 |
| Foot treads | Replaceable foot treads; inspect regularly |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §6.2 p.133 |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| E-Stop button | Red E-Stop button at top rear right corner of body (model 04-00143531-401 only); press to activate, twist clockwise to release | Emergency Stop function compliant with ISO 13850; triggers safety-related stop | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.5.1 p.10; §2.5.4 p.19-20 |
| Intended use | Professional use of locomotion and carrying capabilities in industrial, restricted or supervised environments; in dedicated, demarcated areas; attachments for sensing, monitoring or other non-contact interaction | Not intended for collaborative applications (concurrent human-robot activity sharing space/equipment) | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.2 p.13 |
| Explicitly prohibited uses | Underwater and airborne applications; Use as a weapon or to enable any weapon; Use as or enabling a Certified Medical Device (healthcare facility access subject to limitations); Personal care, medical treatment or life-critical applications; Use in home environments; Transportation of persons or animals; Transportation of hazardous materials or substances; Intentionally harming any person; Any illegal purpose; Use as a climbing aid; Interfering with Spot's sensors or altering environment to impair sensors or locomotion |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.2 p.14 |
| Operational stop triggers | Signal loss; fall detection (motors de-energized, 'smart freeze'); low battery (sits, motors off); controller input; mission interrupt signal (fiducial-triggered) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.5.1 p.17 |
| Keep-out distance at bottom of active staircase | 2 m | Do not stand on stairs, below open rails, or within 2 m of the bottom of a staircase where Spot is active | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.5.1 p.17 |
| Safety-related stop category | Stop Category 0 (EN IEC 60204-1), de-energizes all motors | Triggered when contact on safe input I1 is opened | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.5.2 p.18 |
| Max response time of stopping function | 200 ms |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.5.2 p.18 |
| Safe input | I1 = pin 19 on payload port; use only one port (front or rear); default 6-19 pair normally closed (NC); reset when 6-19 pair closed | Spot will not work without a cap or properly configured attachment on each port; with a cap the stopping function is disabled | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.5.2 p.18 |
| Stopping safety function | ISO 13849-1:2023 Category 1, Performance Level c |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.5.2 p.18 |
| PFHd of stopping function | 1.1E-6 1/h |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.5.2 p.18 |
| Max stopping distance (safety-related stop) | 1 m | On flat ground; can increase on uneven/sloped surfaces | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.5.3 p.19 |
| Emergency Stop standard | ISO 13850 | Additional E-Stop devices may be fitted via payload-port safe input | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.5.4 p.20 |
| Obstacle avoidance | Perception system of five depth cameras (two front, one rear, one each side); gaps extend at 45° from each hip, front gaps close ~2 m from robot; rear gaps extend past depth range |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.6 p.21 |
| Default minimum distance to obstacles | 7.5 cm | Approximately | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.6 p.21 |
| Max additional obstacle avoidance cushion | 50 cm | Set in Robot Controls panel | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.6 p.21 |
| Indicator photobiological safety | IEC 62471 |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.7.1 p.23 |
| Risk assessment methodology | ISO 12100 |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.9 p.30 |
| Foreseeable hazardous exposure duration | <1 min per interaction (automatic mode); <10% of total usage time (restricted access areas); several minutes up to 1 h (manual mode) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.9.1 p.31; §2.9.6.1 p.37 |
| Low-occurrence condition exposure limit | 25 % | Low occurrence does not hold when qualified personnel present >25% of total usage time or affected people up to 25% | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.9.6.1 p.37 |
| EMC emission | IEC 61000-6-4 (heavy industrial environments) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.9.3.1 p.33 |
| EMC immunity | IEC 61000-6-2 (industrial environments) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.9.3.1 p.33 |
| ESD immunity level | +/-4 kV direct contact, +/-8 kV air discharge | IEC 61000-6-2 | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.9.3.1 p.33 |
| RF immunity level | 10 V/m 80-1000 MHz; 3 V/m 1-6 GHz | IEC 61000-6-2 | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.9.3.1 p.33 |
| Laser class | Class 1 Laser Product (EN/IEC 60825-1 Ed. 2 (2007) and Ed. 3 (2014)) | Five stereo camera systems contain a Class 1 laser projection system | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.9.3.3 p.33 |
| Airborne noise | Determined by operating environment (e.g. much quieter on padded carpet than on metal stairs); no fixed figure given |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.9.4 p.34 |
| Accidental impact duration while walking | <100 ms | Short event followed by recoil; impacts only with lower body (feet and lower legs) | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.9.6.1 p.36 |
| Minimum timeframe for accelerations/pattern changes | 1 s | Accelerations and any change of pattern do not occur in a timeframe shorter than 1 second | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.9.6.1 p.38 |
| Fall severity elevation threshold | 1,100 mm | Elevation <1100 mm: low-severity minor impacts with lower body; >1100 mm: high severity possible | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.9.6.2 p.38-39 |
| Flat/non-elevated ground reference | 300 mm | Elevation <300 mm reference situation for accidental impacts | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.9.6.1 p.36 |
| Leg state after de-energization | Legs are not locked during and after motor de-energization; body lowered in control before full de-energization when possible |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.9.6.3 p.39-40 |
| Hip pivot joint pinch point depth | 5 cm | Approximately 5 cm beneath external surface of hips and legs, single finger-size gap; severity moderate, occurrence low | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.9.7 p.41 |
| Pinch points | Hip pivot joint (finger-size gap, moderate severity, low occurrence); hip rolling joint (wide surface, low severity); knee joints | Keep hands away from knee and hip joints except when grabbing handles | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.9.7 p.41; §3.2.1 p.44-45 |
| Clearance around Spot for setup/operation | 2 m | At least 2 m in all directions | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.1 p.48 |
| Controller stop commands | STOP (immediately suspends motion); CUT POWER (fully de-energizes motors; via button shortcut or STOP twice) | Take precedence over all active commands | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.4 p.87-88 |
| Clearance required for self-right / fall recovery | 1 m | Clear 1 m radius around Spot | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.11 p.129; §5.12 p.129 |
| Recommended bystander distance | 2 m | Stay >=2 m from Spot at all times; always give right of way; do not enter staircases/confined spaces where Spot is active | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.15 p.132 |
| Markings | CE (EU); UKCA; FCC; ISED Canada; RCM (R-NZ); KC (Korea); Japan radio (MIC/TELEC); ICASA (South Africa); IMDA (Singapore) | Nameplate/label in battery compartment | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §7.1 p.143; §7.2 p.143 (label image) |
| EU directives (DoC) | Machinery Directive 2006/42/EC; EMC Directive 2014/30/EU; Radio Equipment Directive 2014/53/EU | EU DoC dated Jan 9, 2024; applies to s/n BD-33390001 or higher | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §7.1 p.142-143 |
| Harmonized standards - Machinery Directive | EN ISO 12100:2010; EN 60204-1:2018; EN IEC 62133-2:2017; EN IEC 60825-1:2014/A11:2020 |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §7.1 p.143 |
| Harmonized standards - EMC Directive | EN 61000-6-4:2007/A1:2011; EN 61000-6-2:2005/AC:2005 |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §7.1 p.143 |
| Harmonized standards - Radio Equipment Directive | ETSI EN 301 489-1 V2.2.3 (2019-11); ETSI EN 301 489-17 V3.2.4 (2020-09); EN 55032:2012 |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §7.1 p.143 |
| Other standards referenced | ISO 13849-1:2023; ISO 13850; IEC 60204-1; IEC 62471; IEC 62133; IEC 61000-6-2; IEC 61000-6-4; EN/IEC 60825-1; ISO 12100; ISO/TR 22053:2021; ANSI B11.0-2020; UN 38.3 |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §1.3 p.7; §2.5 p.18-20; §2.7.1 p.23; §2.9 p.30-35 |
| EU authorized representative / technical file | Alura Group BV, Kroonwiel 2, 6003 BT Weert, The Netherlands |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §7.1 p.142; §7.2 p.143 |
| EU DoC serial scope | s/n BD-33390001 or higher; models 04-00143531-001/-401/-601/-611 |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §7.1 p.142 |
| Joint-level/choreography API clearance | 2 m | Full-separation safeguards at min 2 m (joint-level); >=2 m clear space on flat, stable, high-friction surface (choreography); use wireless E-Stop | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §9.1-9.2 p.147 |
| Collision avoidance | Maintains set distance from stationary objects |  | [bostondynamics.com](https://bostondynamics.com/products/spot/) · Spot Specifications > Terrain Sensing |
| EMC (US) | FCC Part 15B |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.2 Safety and Compliance, United States |
| Radio equipment (US) | Incorporates a FCC Part 68 certified radio system (as stated) |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.2 Safety and Compliance, United States |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Modes of operation | Manual (remote controller with camera view); Automatic (Autowalk mission record and replay) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.3 p.14 |
| Installation requirements | No special installation fixtures (no anchoring, anti-vibration pads); setup on flat, stable, clean surface |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.1 p.48 |
| User accounts | Default user and admin accounts (credentials on battery-compartment label); roles: Admin (manage users, update software), Limited Access (no user/software/network/factory-reset changes, no automatic operation, no data download, screenshots or Admin Console) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.7 p.68; §4.7.1 p.69 |
| Controller | Spot tablet controller: handheld touchscreen Android computer running Spot App (ships with Spot); or Orbit browser application on a computer | Tablet or compatible device with Spot App required to record missions | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.2 p.78; §5.2.1 p.79 |
| Multiple controllers | Multiple controllers can pair simultaneously to observe; only one operates at a time; control can be passed (TAKE CONTROL) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.2.2 p.79-80 |
| Signal-loss behavior | Manual: halt with motors on and wait (or AutoReturn if enabled); Automatic: continue mission; limited by controller supervision setting |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.2.3.1 p.81-82 |
| Controller supervision timeout, STRICT (default) | 9 s | Then operational stop (sit, motors off) | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.2.3.2 p.82 |
| Controller supervision timeout, MODERATE | 30 s |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.2.3.2 p.82 |
| Controller supervision timeout, UNSUPERVISED | 18.2 h |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.2.3.2 p.82 |
| AutoReturn max backtrack radius | 20 m | Configurable; disabled by default; manual operation only | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.2.3.3 p.83 |
| Startup sequence | 1) Power on computers (hold power 2 s); 2) reset motor lockout; 3) start motors from remote controller |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.3 p.85; §5.3.1 p.86 |
| Power button hold time to boot | 2 s |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.3.1 p.86 |
| Boot time (fans spin while computers boot) | 2 min | Approximately | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.3.1 p.86 |
| Automatic mode triggers | Operator command; scheduled mission; software on Spot/attachment/external networked device; signal loss with AutoReturn | Motors may start/restart automatically in automatic mode | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.5.1 p.91 |
| Spot App controls | Menu; Modes (Drive, Autowalk); Cameras (Robot cameras, Top Down, Off); Controller (gamepad joysticks or Touch-to-Go); Motor Status; Robot Controls; Robot Health; Comms Status; Battery Status (incl. Roll Over); STOP |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.8.1 p.96-108 |
| Spot App main menu | About; Admin Console; Download Data; Actions/Inspections; Settings (Comms, Tablet language/temperature units); Profiles; Utilities (Attach Payloads incl. payload port power on/off, Odometer, SpotCheck, SpotMetrics); Disconnect |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.8.1.2 p.98-99 |
| Odometer | Cumulative operating statistics such as steps taken and distance traveled |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.8.1.2 p.99 |
| Robot Controls navigation settings | Obstacle avoidance on/off; obstacle cushion; Stairs Mode (auto/force/prevent); Walk on Grated Floor (auto-detect); Descend Stairs Before Power Off; Ground Height Detection; Stair/Surface Edge Avoidance; Avoid Negative Obstacles; Autowalk Avoid Ground Clutter; Step Height; Ground Friction |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.8.1.7 p.104-105 |
| Drive mode controls | Left joystick translate; right joystick rotate; Touch-to-Go; height slider; speed slider (SLOW/MED/FAST); pose selector (Sit, Stand with roll/pitch/yaw/height, Self Right); gait selector (Walk, Crawl); Add Action |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.8.2.1 p.109-110 |
| Autowalk path tolerance, WIDE PATH (default) | 3 m | May deviate up to 3 m from recorded route to avoid obstacles | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.8.2.2 p.110 |
| Autowalk path tolerance, STRICT PATH | 25 cm | Body center kept within a 25 cm corridor along recorded path | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.8.2.2 p.110 |
| Mission software | Autowalk: record route map and actions with Spot App (requires >=1 fiducial), replay automatically with looping/scheduling, docking actions, Return to Dock with auto reroute |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.8.3 p.112-113 |
| Autowalk recording features | Add Actions/Inspections; add any number of docks (each once per mission); pause/resume; Undo (2 s hold timer, not reversible); extend missions with branches and loops |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.8.3.1-5.8.4 p.114-118 |
| Mission replay scheduling | Play now or play later (scheduled; requires >=1 Spot Dock in mission; tablet must stay connected); Once or Loop at interval; play forever option |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.9.1 p.118-120 |
| Mission route options | Take shortcuts; enable/disable actions; re-order actions; edit actions |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.9.2.1 p.121 |
| Navigation/action failure behavior | Prompt timeout; retry count; failure behavior after retries |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.9.2.2 p.123 |
| Mission playback options | Replace actions with short sleeps; force strict path following; path planner range; patience (wait before reroute); force ground clutter avoidance; goal distance; self-right attempts cap |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.9.2.2 p.124 |
| Mission interrupts | Fiducial 585 = safe power off (sit, motors off); fiducial 586 = return to dock and terminate mission; Security Patrol (person detected -> photo + alert; requires Spot CAM and EAP2 payloads) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.9.2.2 p.125 |
| Mission prompt responses | Try again; try to reroute; skip; return to dock and terminate mission |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.9.3 p.126 |
| Self right | Semi-automatic Self Right from side or back to sit; requires >=1 m clear space and stable level surface; autonomous self-right during missions (attempts cappable) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.11 p.128-129; §5.9.2.2 p.124 |
| Shutdown | Sit, Motor Power OFF, press motor lockout, hold power button 2 s, disconnect in Spot App |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.14 p.131 |
| Exterior cleaning | Camera windows: non-abrasive cloth with glass cleaner (anti-static lens brush for abrasive particles); body: magic eraser or mild detergent; no bleach or strong solvents |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §6.2.1 p.134 |
| Preventive maintenance inspection interval | Monthly | Inspect foot treads (replace when worn), cooling fans, cameras, legs, joints, ports | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §6.2 p.133; §6.2.2 p.134 |
| Joint calibration interval | 30 days | Robot operational time (not calendar days); after 30 days without joint recalibration a fault requires running joint calibration & camera check | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §6.3 p.135 |
| SpotCheck routines | Joint calibration and camera check (2-3 min); camera calibration (~15 min, requires calibration panel); revert to previous joint calibration (one backup) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §6.3-6.3.2 p.134-139 |
| Joint calibration & camera check duration | 2 to 3 min |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §6.3.1 p.136 |
| Camera calibration duration | 15 min | About | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §6.3.2 p.139 |
| Calibration clear radius | 1.5 m | Flat, manufactured, non-reflective floor; no bright lights; 2 m around and above for Spot with Arm | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §6.3.1 p.136; §6.3.3 p.140 |
| Fleet / browser control software | Orbit browser application (operate, Autowalk missions, data upload) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.2 p.78; Appendix A p.144-145 |
| Teleoperation | Manual remote driving using live images from Spot's cameras on the tablet controller (Spot App) or Orbit |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.3 p.14; §5.2 p.78 |
| Autonomy features | Autonomous charging; dynamic replanning around new obstacles; self-righting after falls; repeatable autonomous missions launched from Spot Dock |  | [bostondynamics.com](https://bostondynamics.com/products/spot/) · 'Reliable' section; datasheet p.1 |
| Tablet dimensions (H x W x D) | 127 x 214 x 10 mm |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.2 Tablet |
| Tablet weight | 426 g |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.2 Tablet |
| Tablet touchscreen | 8 in diagonal, 1920 x 1200 | Joystick add-on available | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.2 Tablet |
| Tablet ingress protection | IP65 |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.2 Tablet |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| A/V warning system | 5 ground-projecting light indicators, a buzzer and a speaker; disabled by default; config persists across reboots | Models 04-00143531-401, -601, -611 | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.7 p.22 |
| Warning indicators count and location | 5 | 1 on front body panel; 2 on bottom panel between front hips; 2 between rear hips; multi-color, brightness auto-adapts to ambient light; off when tilted/rolled >90° | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.7.1 p.23 |
| Max indicator illuminance, front panel | 1,030 lux | Measured on floor, stand position | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.7.1 p.23 |
| Max indicator illuminance, front and rear hips | 1,010 lux | Measured on floor, stand position | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.7.1 p.23 |
| Buzzer tone frequency | 5,333 Hz |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.7.2 p.23 |
| Buzzer max sound pressure level | 110 dBA | At 1 m in front of Spot; volume adjustable | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.7.2 p.23 |
| Speaker max volume | 80 dB | Measured 1 m in front of Spot; adjustable | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.7.3 p.23 |
| Warning color palettes | DEFAULT (green/amber/red/white); ALTERNATE (blue/red/...) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.7.4 p.23-26 |
| Warning light pattern rates | Slow blink 0.7 Hz; fast blink 1.4 Hz; flash brief at 1.4 Hz; pulse = continuous brighter/dimmer oscillation |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.7.4 p.25 |
| Recommended buzzer level | 80 dBA | Not higher than 80 dBA recommended; max only for very loud environments | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.9.4 p.34 |
| Power / motor lockout button lights | Power button blue when computers on; motor lockout red when lockout reset (slow blink), fast blink while motors starting, steady red when started |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.1.1 p.75; §5.3.2 p.86; §5.3.3 p.87 |
| Robot status lights (front panel) | Yellow = booting; moving rainbow = ready to connect; solid blue = lockout engaged/safe to handle; filling blue = charging; solid blue with gap = plugged/docked no battery; slow blink green = controller connected; fast blink green = motors turning on; solid green = motors on; draining orange = low battery; blinking orange = serious error/perception fault | Match A/V indicator color when warning system active | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.1.2 p.76-78 |
| A/V warning system settings | Enable/disable; indicator brightness; buzzer volume; color palette (Spot App > Settings > Audio/Visual) |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §5.6 p.92-93 |
| Robot rename | Robot can be renamed via Admin Console About page |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §4.5.2 p.66 |
| Max light projection distance | 1.8 m | In front of robot | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.2 Audio & Visual Signals |
| Audio & visual signals | Pre-configured behaviors for manual and autonomous operations |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.2 Audio & Visual Signals |

### Transport & Storage

| Spec | Value | Note | Source |
|---|---|---|---|
| Robot shipping case dimensions (L x W x H) | 927 x 546 x 464 mm | Holds Spot robot and Spot tablet controller | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §3.1.1 p.43 |
| Robot shipping case empty weight | 20.4 kg |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §3.1.1 p.43 |
| Robot shipping case + robot combined weight | 47.6 kg |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §3.1.1 p.43 |
| Power Supply shipping case dimensions (L x W x H) | 559 x 432 x 432 mm | Holds charger and up to two batteries | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §3.1.2 p.43 |
| Power Supply shipping case empty weight | 9.2 kg |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §3.1.2 p.43 |
| Power Supply case + charger + one battery | 18.1 kg |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §3.1.2 p.43 |
| Power Supply case + charger + two batteries | 22.7 kg |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §3.1.2 p.44 |
| Carry handles | One handle at each hip joint (4) to lift, carry and roll Spot |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §3.2.2 p.45 |
| People required to lift | 2 | One at front, one at rear; by handles when sitting upright, or by lower legs when flipped on back; power off first | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §3.2.3 p.45 |
| Handling PPE | Safety footwear recommended; hearing protection may be recommended depending on buzzer volume |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §3.2.4 p.46 |
| Robot storage conditions | -40 to 75 °C; 30-70% RH; dry location, in case or at Spot Dock |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §3.3 p.46 |
| Robot storage temperature | -40 to 75 °C |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §3.3 p.46 |
| Robot storage relative humidity | 30 to 70 % |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §3.3 p.46 |
| Battery storage temperature | -30 to 25 °C |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §3.3.1 p.46 |
| Max battery state of charge for shipping | 30 % | US/international regulations for Li-ion batteries of this size, any shipping method; 1 LED bar = <30% SOC | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §3.3.1 p.47 |
| Power case dimensions (L x W x H), datasheet | 810 x 530 x 300 mm | Includes two batteries and charger (IFU 5.1.5: 559 x 432 x 432 mm) | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.2 Travel Cases |
| Power case net weight, datasheet | 28 kg | Includes two batteries and charger | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.2 Travel Cases |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Service and repair | No user servicing/repair; via Boston Dynamics Support (provide serial number and issue description) | https://support.bostondynamics.com/s/contactsupport | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §6.1 p.133 |
| Included accessories (per IFU) | Spot tablet controller (ships in robot case); camera calibration panel |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §3.1.1 p.43; §5.2.1 p.79; §6.3 p.135 |
| Optional accessories (per IFU) | Spot Dock; Spot Power Supply; Spot Arm; Spot CAM; EAP2 (lidar payload); Spot Station; LTE and mesh radio hardware; additional E-Stop devices |  | [d3cjkvgbik1jtv.cloudfront.net](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf) · §2.5.4 p.20; §4.6 p.67; §4.9.1 p.71; §5.9.2.2 p.125; Appendix A p.144 |
| Robots in customer hands | Over 1,500 | As stated on product page (accessed 2026-11-04) | [bostondynamics.com](https://bostondynamics.com/products/spot/) · 'Reliable' section |
| Warranty | One-year limited warranty; premium service via Spot Care subscription |  | [bostondynamics.com](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf) · p.1 Learn with Training and Support |

## Documents

- [Spot Instructions for Use, Safety and Operations Manual, Version 5.1.5 (April 2026)](https://d3cjkvgbik1jtv.cloudfront.net/translations/spot-5_1/spot-user-manual-en.pdf)
- [Spot product page (Boston Dynamics)](https://bostondynamics.com/products/spot/)
- [Spot specifications datasheet (updated 05/22/2024), linked from product page](https://bostondynamics.com/wp-content/uploads/2020/10/spot-specifications.pdf)
- [Boston Dynamics Support Center: Spot Specifications](https://support.bostondynamics.com/s/article/spot-specifications)

## Notes

Maker product page specifications: length 1100 mm, width 500 mm, walking height 610 mm, 33.8 kg with battery, 1.6 m/s, +/-30 deg slope, 300 mm step, IP54, -20 to 55 C, 564 Wh battery, 90 min average runtime and 60 min recharge, 360 deg perception. Payload is not stated on the page (its 20.43 kg figure is the Spot Arm's max lift), so the catalogue's 14 kg payload is cleared rather than asserted.

## Sources

- Official page: [bostondynamics.com](https://bostondynamics.com/products/spot/)
- [dev.bostondynamics.com](https://dev.bostondynamics.com/)
- [github.com](https://github.com/boston-dynamics/spot-sdk)
- [bostondynamics.com](https://bostondynamics.com/blog/expanding-our-reach-in-korea/)
- [spot.clobot.co.kr](https://spot.clobot.co.kr/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-17). Source repository: https://github.com/htcrefactor/robot-catalog*
