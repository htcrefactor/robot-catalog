# ROBOTIS K0

> K0 is the first open-source humanoid of ROBOTIS' AI Sapiens line: a 1.3 m, 23-DOF platform on in-house DYNAMIXEL-Q quasi-direct-drive actuators for learning-based locomotion and manipulation.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=robotis-k0
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: ROBOTIS (South Korea)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Height | 1,300 mm |
| Weight | 34 kg |
| Payload | 3 kg |
| Degrees of freedom | 23 |
| Battery | 421.2 Wh |
| Released | 2026 |
| Status | In development |
| SDK | yes |
| SDK name | Open-source stack: hardware BoM, STEP CAD, source code, simulation assets, tutorials (ROS 2) |
| ROS | yes |
| On-board compute | NVIDIA Jetson Orin NX 16GB |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Maker page: 1,300 mm height, 34 kg, 23 DOF (5 per arm, 6 per leg, 1 waist), max arm payload 3 kg, DYNAMIXEL Q actuators (QM-060 x 14, QM-080 x 9), Jetson Orin NX 16GB (up to 100 sparse INT8 TOPS), 46.8 V 9,000 mAh battery (=421.2 Wh, derived from V x Ah), Wi-Fi 5 + Bluetooth 5.0, 2 Ethernet, USB 2.0 x 2 and USB 3.0 x 2, 24 V/10 A and 12 V/10 A power outputs. Sold as a development platform, not a finished product: DYNAMIXEL-Q and the open-source release (BoM, STEP files, code, simulation, tutorials) were still being rolled out, so status is In development. Max speed, runtime and a sensor list are not published.

## Sources

- Official page: [ai.robotis.com](https://ai.robotis.com/ai_sapiens/introduction_ai_sapiens.html)
- [robotis.us](https://robotis.us/blogs/robotis-ir-pr-blog/k0-dynamixel-q)

Listed by these directories (discovery only, never used as a spec source):

- [humanoid.guide](https://humanoid.guide/product/k0-by-robotis/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-26). Source repository: https://github.com/htcrefactor/robot-catalog*
