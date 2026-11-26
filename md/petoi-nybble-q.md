# Petoi Nybble Q

> Open-source 3D-printed robot cat for teaching legged locomotion and physical AI, sold pre-assembled with 11 servo joints.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=petoi-nybble-q
- Category: Quadruped
- Locomotion: Legged
- Manufacturer: Petoi (United States)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 240 mm |
| Width | 115 mm |
| Height | 150 mm |
| Weight | 0.433 kg |
| Degrees of freedom | 11 |
| Runtime | 0.75 h |
| Battery | 7.4 Wh |
| Status | Commercial |
| SDK | yes |
| SDK name | OpenCat Python API, Arduino IDE, Petoi Coding Blocks |
| On-board compute | yes |
| Compute | BiBoard V1 (ESP32-WROOM-32D, 520 KB SRAM, 4 MB flash); a Raspberry Pi can be mounted on the board |
| Sensors | 6-axis IMU (MPU6050 or ICM42670), Ultrasonic distance sensor, Voice microphone |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Petoi spec page: standing 240 x 115 x 150 mm, 403–433 g depending on the servo set (0.433 kg kept as the upper figure), 11 joints (2 head, 1 tail, 8 legs), BiBoard V1 with ESP32-WROOM-32D. Product page: 7.4 V 1,000 mAh Li-ion pack, so battery_wh is the derived 7.4 V x 1 Ah = 7.4 Wh, and about 45 minutes of walking per charge (0.75 h). OpenCat is the maker's open-source framework, also the Python and Arduino entry point.

## Sources

- Official page: [petoi.com](https://www.petoi.com/products/petoi-nybble-q-robot-cat)
- [petoi.com](https://www.petoi.com/pages/robot-cat-nybble-q-technical-specifications)

Listed by these directories (discovery only, never used as a spec source):

- [botupyourlife.com](https://botupyourlife.com/en/robots/petoi-nybble-q/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-26). Source repository: https://github.com/htcrefactor/robot-catalog*
