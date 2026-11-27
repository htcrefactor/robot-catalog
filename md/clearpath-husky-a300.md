# Clearpath Robotics (Rockwell Automation) Husky A300

> Rugged all-terrain 4-wheel skid-steer UGV for outdoor robotics research and field prototyping, shipped with ROS 2.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=clearpath-husky-a300
- Category: Mobile platform
- Locomotion: Wheeled
- Manufacturer: Clearpath Robotics (Rockwell Automation) (Canada)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 990 mm |
| Width | 698 mm |
| Height | 372 mm |
| Weight | 80 kg |
| Payload | 100 kg |
| Max speed | 2 m/s (7.2 km/h) |
| Wheel diameter | 336 mm |
| Wheels | 4 |
| Runtime | 4 h |
| Battery | 1,024 Wh |
| IP rating | IP54 |
| Released | 2024 |
| Status | Commercial |
| API | yes |
| SDK | yes |
| SDK name | ROS 2 Jazzy (Clearpath packages) |
| ROS | yes |
| On-board compute | yes |
| Compute | Standard Intel i3-13100TE; Performance Intel i7-13700TE (GPU optional) |
| Sensors | Wheel encoders |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

139 values from 4 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery configurations | Standard 40 Ah (2 batteries); Upgraded 80 Ah (4 batteries); Extended 120 Ah (6 batteries) |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Configurations | Base platform; Husky AMP (autonomous mobile platform); Husky Observer |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Introduction / Husky AMP |
| Drive options | Rugged wheels (4WD skid steer); Casters (2 wheels + 2 casters, differential); Mecanum (holonomic) |  | [clearpathrobotics.com](https://clearpathrobotics.com/husky-a300-unmanned-ground-vehicle-robot/) · Drive Options |
| Manufacturer address | Clearpath Robotics, by Rockwell Automation, 1425 Strasburg Rd. Suite 2A, Kitchener, ON N2R 1H2, Canada |  | [clearpathrobotics.com](https://clearpathrobotics.com/husky-a300-unmanned-ground-vehicle-robot/) |
| Predecessor model | Husky A200 |  | [clearpathrobotics.com](https://clearpathrobotics.com/husky-spec-comparison/) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 990 mm |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Width | 698 mm |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Height | 372 mm |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Height | 381 mm | product page tech specs states 990 x 698 x 381 mm | [clearpathrobotics.com](https://clearpathrobotics.com/husky-a300-unmanned-ground-vehicle-robot/) · Tech Specs |
| Top plate / payload area width | 420 mm | dimension shown on top-view drawing | [storage.pardot.com](https://storage.pardot.com/92812/1728925412aC5a34ww/Husky_A300_DataSheet_Oct24.pdf) · drawing |
| Length without bumpers | 740 mm | dimension shown on top-view drawing (inner length) | [storage.pardot.com](https://storage.pardot.com/92812/1728925412aC5a34ww/Husky_A300_DataSheet_Oct24.pdf) · drawing |
| Weight | 80 kg |  | [storage.pardot.com](https://storage.pardot.com/92812/1728925412aC5a34ww/Husky_A300_DataSheet_Oct24.pdf) |
| Weight (robot mass) | 78.5 kg | 40 Ah (2-battery) configuration | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Weight (robot mass) | 93.5 kg | 80 Ah (4-battery) configuration | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Weight (robot mass) | 105 kg | 120 Ah (6-battery) configuration | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Centre of mass (X, Y, Z) | -41, 3, 70 mm | 40 Ah config, relative to base_link | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Centre of mass (X, Y, Z) | -33, 3, 70 mm | 80 Ah config, relative to base_link | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Centre of mass (X, Y, Z) | -7, 2, 70 mm | 120 Ah config, relative to base_link | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Ground clearance | 130 mm |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Wheelbase | 512 mm |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Track width | 566 mm |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Effective track (kinematics) | 0.562 m | W used in robot equations | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Robot Equations |
| Nominal tire diameter | 336 mm |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Effective tire radius | 162.5 mm | value for odometry control software | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Max speed | 2 m/s |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Max speed (off-road, no payload) | 1.5 m/s |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Suspension and Performance Limits |
| Max speed (off-road, up to 50 kg payload) | 1 m/s | payloads above 50 kg not supported off-road | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Suspension and Performance Limits |
| Max speed (controller slow mode) | 0.3 m/s | fast mode 2.0 m/s | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Connecting and Using the Controller |
| Minimum controllable speed | 0.1 m/s | control loops accurately maintain velocities as low as 0.1 m/s | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · General Warnings |
| Max payload | 100 kg |  | [storage.pardot.com](https://storage.pardot.com/92812/1728925412aC5a34ww/Husky_A300_DataSheet_Oct24.pdf) |
| Allowable payload | 101.5 kg | 40 Ah config; continuous operation on relatively flat terrain with wide turns | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Allowable payload | 86.5 kg | 80 Ah config | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Allowable payload | 75 kg | 120 Ah config | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| All-terrain payload | 50 kg | robot climbing 30° grade with high-mounted payload or turning in place in high-friction conditions | [storage.pardot.com](https://storage.pardot.com/92812/1728925412aC5a34ww/Husky_A300_DataSheet_Oct24.pdf) |
| All-terrain payload | 51.5 kg | 40 Ah config | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| All-terrain payload | 36.5 kg | 80 Ah config | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| All-terrain payload | 25 kg | 120 Ah config | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Drive power | 1,080 W | total continuous, from 4 BLDC motors | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Drive train | Four brushless (in-wheel) motors, skid-steer drive |  | [storage.pardot.com](https://storage.pardot.com/92812/1728925412aC5a34ww/Husky_A300_DataSheet_Oct24.pdf) |
| Max acceleration/deceleration (stability cone reference) | 4 m/s² | example stability cone for 100 kg payload, 2-battery config | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Stability Limits |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Max climb grade | 30 ° |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Allowable side slope | 30 ° |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Max grade (intended use environment) | 15 ° | environments free of grades greater than 15° | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Intended Use |
| Max curb height | 150 mm | max approach speed 0.1 m/s at 150 mm | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Suspension and Performance Limits |
| Max curb height at full speed/payload | 13 mm | without reducing max speed or payload | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Suspension and Performance Limits |
| Max gap / depression depth | 150 mm | do not drive across gaps or depressions more than 150 mm deep | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Operating Conditions |
| Max water/liquid depth | 130 mm | environments free of open water deeper than 130 mm | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Intended Use |
| Suspension | None |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Suspension and Performance Limits |
| Terrain | Rocky terrain, hills, mud, sand, inclement weather |  | [clearpathrobotics.com](https://clearpathrobotics.com/husky-a300-unmanned-ground-vehicle-robot/) · Features |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery chemistry | LiFePO4 |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Battery nominal voltage | 25.6 V |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Battery capacity | 1,024 Wh | 40 Ah standard | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Battery capacity | 2,048 Wh | 80 Ah upgraded | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Battery capacity | 3,072 Wh | 120 Ah extended | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Battery capacity (Ah) | 40 / 80 / 120 Ah | standard / upgraded / extended | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Battery count | 2 / 4 / 6 | 24 V LiFePO4 batteries | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Interior Features |
| Battery hot-swappable | no | batteries are not hot-swappable | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Batteries |
| Average run time | 8 h | 40 Ah; 33% driving at 2 m/s with 50 kg payload on level ground, 67% idle (user manual) | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Average run time | 16 h | 80 Ah | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Average run time | 24 h | 120 Ah | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Average run time | 4 h | standard battery, per Oct 2024 datasheet (8 h upgraded, 12 h extended) | [storage.pardot.com](https://storage.pardot.com/92812/1728925412aC5a34ww/Husky_A300_DataSheet_Oct24.pdf) |
| Standby time | 16 h | 40 Ah (32 h for 80 Ah, 48 h for 120 Ah) per user manual | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Standby time | 15 h | standard battery per Oct 2024 datasheet (30 h upgraded, 45 h extended) | [storage.pardot.com](https://storage.pardot.com/92812/1728925412aC5a34ww/Husky_A300_DataSheet_Oct24.pdf) |
| Battery power capability | over 3000 W | depending on configuration | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Electrical System |
| Battery continuous current output | 60 / 120 / 150 A | 40 / 80 / 120 Ah | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Current Limits |
| Circuit breaker value | 100 A |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Current Limits |
| Motor continuous current | 17 A | per motor | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Current Limits |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charge time (standard charger, North America) | 4 / 8 / 12 h | 40 / 80 / 120 Ah | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Charge time (standard charger, Europe) | 5 / 10 / 15 h | 40 / 80 / 120 Ah | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Charge time (650 W charger) | 1h45m / 3h30m / 5h15m | 40 / 80 / 120 Ah | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Charge time (1200 W charger) | not supported / 2 / 3 h | 40 / 80 / 120 Ah | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Charge time (wireless charger) | 2 / 2 / 3 h | 40 / 80 / 120 Ah | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Charge time (datasheet) | 3-4 / 7-8 / 8-10 h | standard / upgraded / extended | [storage.pardot.com](https://storage.pardot.com/92812/1728925412aC5a34ww/Husky_A300_DataSheet_Oct24.pdf) |
| Standard charger (North America) | Henryuan PSY27710000, 277 W, 27.7 V, 10.0 A | indoor use only | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Manual/Wired Charging |
| Standard charger (Europe) | Mean Well NPB-240-24TB, 222 W, 27.7 V, 8.0 A | indoor use only; validated against IEC 61010-1 | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Manual/Wired Charging |
| Upgraded charger 650 W | Delta-Q IC650, 650 W, 27.7 V, 23.5 A | indoor or outdoor (IP66) | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Manual/Wired Charging |
| Upgraded charger 1200 W | Delta-Q IC1200, 27.7 V, 43.3 A | indoor or outdoor (IP66); manual table lists power as 650 W | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Manual/Wired Charging |
| Charging methods | Manual wired charger; optional wireless charging kit (dock); autonomous wireless charger with OutdoorNav (Husky Observer) |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Charging |
| Wireless charging coil alignment | within 30 mm | mobile coil to stationary coil for maximum charge rate | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Wireless Charging |
| Dock available | yes | optional wireless charging docking station | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Wireless Charging |
| Shore power | yes | charger provides shore power (excluding drive motors) | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Battery Charge Port |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| IP rating | IP54 |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Operating temperature | -20 to 40 °C | must be powered on at minimum 0 °C | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Storage temperature | -20 to 60 °C |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Charging temperature | 0 to 40 °C |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Operating humidity | 0 to 85 %RH | non-condensing | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Max altitude | 2,000 m |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Intended Use |
| Pollution degree | 1, 2 or 3 (per IEC 61010-1) |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Intended Use |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| IMU | 6-axis IMU (standard), upgrade options available |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · IMU |
| Feedback | Battery, motor currents, odometry/encoders, connectivity, emergency stop status, diagnostics |  | [clearpathrobotics.com](https://clearpathrobotics.com/husky-spec-comparison/) |
| Temperature monitoring | Motors, motor drivers (MCU/PCB), batteries, MCU, fan controller, DC/DC converters |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Thermal Limits |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| CPU (standard) | Intel Core i3-13100TE |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| CPU (performance) | Intel Core i7-13700TE | GPU optional | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| GPU | Optional |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| Computer form factor | Mini-ITX (Intel-based); Jetson-based computer also possible |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Computer / System Architecture |
| Microcontroller | 32-bit MCU (power, lights, screen, monitoring), Ethernet link to computer |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · System Architecture |
| Operating system | Ubuntu |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · System Architecture |
| ROS version | ROS 2 Jazzy |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Using ROS |
| Autonomy software (AMP/Observer) | OutdoorNav |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Husky AMP |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Communication | Ethernet, USB, remote control, Wi-Fi |  | [storage.pardot.com](https://storage.pardot.com/92812/1728925412aC5a34ww/Husky_A300_DataSheet_Oct24.pdf) |
| Ethernet | Gigabit Ethernet debug port; internal network switch for payloads |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Debug Ports / Network Switch |
| USB | USB 3.0 Type-A debug port; optional USB hub |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Debug Ports |
| Video output | HDMI debug port |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Debug Ports |
| Default robot IP | 192.168.131.1 |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Robot Network Connection |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| User power 12 V | 10 A |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| User power 24 V | 5 A |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| User power VBAT | 5 A |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| User power large VBAT | 40 A | optional upgrade (High Power Expansion Kit) | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Technical Specifications |
| User power breakouts | 8 |  | [clearpathrobotics.com](https://clearpathrobotics.com/husky-spec-comparison/) |
| Payload interface | Large universal mounting plate, user electrical breakouts, cable passthrough ports |  | [clearpathrobotics.com](https://clearpathrobotics.com/husky-a300-unmanned-ground-vehicle-robot/) · Build & Expand |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Emergency stop | Front and rear E-stop buttons (PLc per ISO 13849); rear door interlock (PLc); optional wireless E-stop |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Safety System Functionality |
| Performance level | E-stop PLc; electrical braking on E-stop PLa (ISO 13849) |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Safety System Functionality |
| Braking | Electrical (resistive) brake on E-stop |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Emergency Stop Braking Limits |
| Stopping distance | 0.5 m | 0 kg, 0°, high friction, default deceleration | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Stopping Distances |
| Stopping distance | 0.7 m | 100 kg, 0°, high friction | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Stopping Distances |
| Stopping distance | 0.5 m | 0 kg, 15°, high friction | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Stopping Distances |
| Stopping distance | 1 m | 100 kg, 15°, high friction | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Stopping Distances |
| E-stop terminal speed on incline | 0.75 m/s or less (0 kg, 15°); 1.5 m/s or less (100 kg, 15°); 0 m/s on level |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Emergency Stop Braking Limits |
| Max noise | 80 dBA | at 10 cm from robot | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Personal Protective Equipment |
| Obstacle avoidance (base) | no | base robot has no personnel detection or obstacle avoidance | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Safety |
| Safety standards | ISO 12100 risk assessment; ISO 13849 (E-stop functions); IEC 61010-1 |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) |
| Compliance (US/Canada) | FCC Part 15 Subpart B; FCC Part 18; ICES-002; ICES-003 |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Standards Compliance |
| Compliance (CE) | CE: EN 61326-1:2013; EN 61010-1:2010 (+A1:2019); EN 301 489-1 V1.9.2; EN 301 893 V2.1.1; EN 300 328 V2.2.2 |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Standards Compliance |
| Compliance (AU/NZ) | EN 55032:2015; AS/NZS 4268:2017; AS/NZS 4024.1204:2019; EN 50566:2017 |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Standards Compliance |
| Compliance (Korea) | KS 3124:2020; KS 3126:2020; KS C 9610-6-2:2019; KS C 9610-6-4:2022 |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Standards Compliance |
| Other approvals | India WPC Equipment Type Approval; Singapore; Japan listed |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Standards Compliance |
| Intended use | Indoor and outdoor research labs and light industrial environments for inspection, materials transport, manipulation; trained personnel, constantly monitored |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Intended Use |
| Prohibited uses | Explosive atmospheres; near vertical drops >150 mm, fast-moving people/vehicles, children, glass/transparent floors or walls; carrying passengers |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Intended Use / Safety |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Controller | PS4 controller included (PS5 supported) |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Connecting and Using the Controller |
| Teleop modes | Slow (0.3 m/s) and fast (2.0 m/s) enable buttons |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Status lights | 4 programmable LED lights (2 front, 2 rear), programmable via ROS |  | [clearpathrobotics.com](https://clearpathrobotics.com/husky-a300-unmanned-ground-vehicle-robot/) |
| Display | 3.70-inch e-ink display (battery, charge, Wi-Fi, Ethernet, micro-ROS, error status) |  | [clearpathrobotics.com](https://clearpathrobotics.com/husky-spec-comparison/) |

### Transport & Storage

| Spec | Value | Note | Source |
|---|---|---|---|
| Lifting | Two-person lift via bumper bars (no payload) or lifting straps; never one-person lift |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Husky Lift Points |
| Shipping | Wooden crate (front panel as ramp, 14 mm hex bolts) |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Unboxing |
| Storage | Charge ≥50% and breaker OFF for storage >2 days; power on every 3 months, recharge if <20% |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) · Storage |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Included accessories | PS4 controller, battery charger |  | [storage.pardot.com](https://storage.pardot.com/92812/1728925412aC5a34ww/Husky_A300_DataSheet_Oct24.pdf) |
| Packages | Husky AMP (OutdoorNav); Manipulator Package (Franka Research 3, ROS 2/MoveIt 2); Vision Package (2x ZED2/ZED X, Ouster OS1-64) |  | [clearpathrobotics.com](https://clearpathrobotics.com/husky-a300-unmanned-ground-vehicle-robot/) · Packages |
| Optional kits | Wireless E-stop kit; wireless charging kit; high power expansion kit; GPU; USB hub; upgraded IMU |  | [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky) |
| Price | Contact sales for pricing |  | [storage.pardot.com](https://storage.pardot.com/92812/1728925412aC5a34ww/Husky_A300_DataSheet_Oct24.pdf) |

## Documents

- [Husky A300 Data Sheet (Oct 2024)](https://storage.pardot.com/92812/1728925412aC5a34ww/Husky_A300_DataSheet_Oct24.pdf)
- [Husky A300 User Manual (Clearpath docs, updated Jul 2026)](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky)
- [Husky A300 product page](https://clearpathrobotics.com/husky-a300-unmanned-ground-vehicle-robot/)
- [Husky Spec Comparison A300 vs A200](https://clearpathrobotics.com/husky-spec-comparison/)

## Sources

- Official page: [clearpathrobotics.com](https://clearpathrobotics.com/husky-a300-unmanned-ground-vehicle-robot/)
- [storage.pardot.com](https://storage.pardot.com/92812/1728925412aC5a34ww/Husky_A300_DataSheet_Oct24.pdf)
- [clearpathrobotics.com](https://clearpathrobotics.com/husky-spec-comparison/)
- [docs.clearpathrobotics.com](https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/husky/a300/user_manual_husky)
- [github.com](https://github.com/clearpathrobotics/clearpath_robot)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-27). Source repository: https://github.com/htcrefactor/robot-catalog*
