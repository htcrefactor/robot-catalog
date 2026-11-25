# Ogadjet (XGO) XGO-Rider2

> Luwu Dynamics' desktop wheel-legged robot: two FOC hub wheels plus two leg servos give it omnidirectional, self-balancing motion and an adjustable 116-158 mm stance, run by a Raspberry Pi CM5 with an ESP32 motion controller.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=ogadjet-xgo-rider2
- Category: Wheel-legged
- Locomotion: Wheel-legged
- Manufacturer: Ogadjet (XGO) (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 135 mm |
| Width | 118 mm |
| Height | 116 mm |
| Weight | 0.56 kg |
| Wheel diameter | 48 mm |
| Wheels | 2 |
| Degrees of freedom | 4 |
| Runtime | 2 h |
| Battery | 10.36 Wh |
| SDK | yes |
| SDK name | Open ESP32 motion-controller SDK |
| ROS | yes |
| On-board compute | yes |
| Compute | Raspberry Pi CM5 (2 GB) + ESP32 co-processor |
| Sensors | 5 MP OV5647 camera, Dual MEMS microphone array, 8 ohm 2 W speaker, IMU, 2.0-inch IPS display (320 x 240) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Maker pages checked 2026-11-25: 135 x 118 x 116-158 mm (height adjustable, 116 mm taken as the height value), 560 g, two FOC brushless hub motors (48 mm, D 48 mm x H 20 mm) plus two 4.5 kg.cm magnetic-encoder serial-bus leg servos, 1400 mAh 2S 18500 pack (10.36 Wh computed as 7.4 V x 1.4 Ah), Raspberry Pi CM5 2 GB with ESP32 co-processor, 5 MP OV5647 camera, dual MEMS microphones and a 2 W speaker, USB-C charging, Python and ROS development, open ESP32 motion firmware under Apache 2.0. Runtime is stated as about 2 h in the maker's wiki and about 1 h on the product page, so the wiki figure is used and both are recorded here; top speed and payload are not published.

## Sources

- Official page: [xgorobot.com](https://www.xgorobot.com/en/rider.html)
- [wiki.xgorobot.com](https://wiki.xgorobot.com/kb/the-xgo-series-robot/cmpgp22gn000bfk659hf250en)
- [shop.xgorobot.com](https://shop.xgorobot.com/products/xgo-rider-world-s-first-desktop-wheel-legged-robot-with-ai)

Listed by these directories (discovery only, never used as a spec source):

- [botupyourlife.com](https://botupyourlife.com/en/robots/ogadjet-xgo-rider2/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-25). Source repository: https://github.com/htcrefactor/robot-catalog*
