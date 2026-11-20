# ROBOTIS DARwIn-OP

> DARwIn-OP, the open-platform miniature humanoid ROBOTIS built with the University of Pennsylvania, became the standard small-size robot for RoboCup research and education.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=robotis-darwin-op
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: ROBOTIS (South Korea)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Height | 454.5 mm |
| Weight | 2.9 kg |
| Max speed | 0.24 m/s (0.9 km/h) |
| Degrees of freedom | 20 |
| Released | 2010 |
| Status | Discontinued |
| SDK | yes |
| SDK name | Open Platform: source code (SourceForge), ROBOTIS e-manual, ROBOTIS Framework |
| On-board compute | Intel Atom Z530 1.6 GHz (fit-PC2) |
| Sensors | Camera, 3-axis gyroscope, 3-axis accelerometer, 2x detection microphone |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Maker product page and e-manual: 20 actuator modules (6 DOF leg x 2, 3 DOF arm x 2, 2 DOF neck), DYNAMIXEL MX-28 actuators with metallic gears (the academic-edition datasheet lists RX-28M), CM-730 sub-controller (ARM Cortex-M3 STM32F103RE), Intel Atom Z530 1.6 GHz PC with 4 GB flash, default walking speed 24.0 cm/s at 0.25 s per step, 3-axis gyro and accelerometer, two microphones, battery good for about 30 minutes with hot-swap support, 3 Mbps DYNAMIXEL bus. Height 454.5 mm and weight 2.9 kg are from the ROBOTIS DARwIn-OP academic-edition datasheet (SKU 905-0012-310); the maker page shows the same figures in an image table. Line is discontinued. No payload or IP rating is published.

## Sources

- Official page: [en.robotis.com](https://en.robotis.com/model/page.php?co_id=prd_op)
- [emanual.robotis.com](https://emanual.robotis.com/docs/en/platform/op/getting_started/)

Listed by these directories (discovery only, never used as a spec source):

- [humanoidversus.com](https://humanoidversus.com/robots/robotis-darwin-op)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-20). Source repository: https://github.com/htcrefactor/robot-catalog*
