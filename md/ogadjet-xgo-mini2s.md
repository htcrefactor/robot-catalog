# Ogadjet (XGO) XGO-Mini2S

> Luwu Intelligence's research-grade desktop quadruped: 16 DoF with a 4-DoF arm, magnetic-encoder servos at 0.01 deg control resolution and a Raspberry Pi CM5 for ROS development.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=ogadjet-xgo-mini2s
- Category: Quadruped
- Locomotion: Legged
- Manufacturer: Ogadjet (XGO) (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 270 mm |
| Width | 150 mm |
| Height | 180 mm |
| Weight | 0.915 kg |
| Degrees of freedom | 16 |
| Runtime | 2 h |
| Battery | 28.12 Wh |
| Status | Commercial |
| API | yes |
| SDK | yes |
| SDK name | xgolib (Python) / open serial protocol |
| ROS | yes |
| On-board compute | yes |
| Compute | Raspberry Pi CM5 (4 GB) + ESP32 motion controller |
| Sensors | 5 MP OV5647 camera, Dual MEMS microphone array, 8 ohm 2 W speaker, 6-axis IMU, Joint position sensors, 2.0-inch IPS display (320 x 240) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Maker wiki checked 2026-11-28 (shared lite3/mini2S page): 270 x 150 x 180 mm default standing, 915 g, 16 DoF (12 leg joints + 4-DoF arm), 18650 2S 3800 mAh pack (28.12 Wh computed as 7.4 V x 3.8 Ah), 4.5 kg.cm magnetic-encoder servos with 0-360 deg range and 0.01 deg control resolution, Raspberry Pi CM5 4 GB with ESP32, silicone + ABS feet, supplied 8.4 V 4 A DC charger (USB-C charging is not allowed), about 2 hours runtime, Python and ROS development. Top speed and payload are not published. The maker has no separate mini2S product page on xgorobot.com (404); the wiki is the current source.

## Sources

- Official page: [wiki.xgorobot.com](https://wiki.xgorobot.com/kb/the-xgo-series-robot/cmpidwcrq000jhjqr5awou1iy?model=lite3)
- [xgorobot.com](https://www.xgorobot.com/)

Listed by these directories (discovery only, never used as a spec source):

- [botupyourlife.com](https://botupyourlife.com/en/robots/ogadjet-xgo-mini2s/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-28). Source repository: https://github.com/htcrefactor/robot-catalog*
