# Rokae Helios H2

> Rokae's Helios H2 wheeled dual-arm humanoid: a lifting column, two 7-DOF force-controlled arms and a 4-wheel omnidirectional base for bin handling, sorting and assembly.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=rokae-helios-h2
- Category: Humanoid
- Locomotion: Wheeled
- Manufacturer: Rokae (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 750 mm |
| Width | 650 mm |
| Height | 1,493 mm |
| Weight | 160 kg |
| Payload | 5 kg |
| Max speed | 1.5 m/s (5.4 km/h) |
| Degrees of freedom | 23 |
| Runtime | 4 h |
| Status | Commercial |
| SDK | yes |
| SDK name | ROS 2, Python SDK |
| ROS | yes |
| On-board compute | NVIDIA Orin NX 8GB (117 TOPS) / AGX Orin 64GB (275 TOPS) / Thor T5000 |
| Sensors | 2x 3D navigation LiDAR, Head stereo camera, 3x fisheye cameras (optional), Wrist camera (optional), IMU, 4-mic circular array (optional) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Maker product page and brochure, model H2-5: 750 x 650 x 1,493-2,000 mm (the height range is the 0-2 m lift travel; the minimum standing height is entered), 160 kg (H2-10: 180 kg), 23 DOF (neck 2, waist 2, arms 7 x 2, legs 2, chassis 3), 5 kg payload per arm (10 kg option), whole-body force control with joint torque sensors, 4 drive wheels omnidirectional at 1.5 m/s, +/-10 mm docking accuracy, two 18 Ah batteries (36 Ah total; no voltage or Wh figure published, so battery_wh is left empty), 4 h runtime, 2 h charge from 10 to 90% with a 54.75 V 10 A charger, 0-45 C, 3D navigation LiDAR x 2, head stereo camera, optional fisheye x 3 / wrist camera / 4-mic array / 10 W x 2 speakers, compute choice of Orin NX 8GB 117 TOPS, AGX Orin 64GB 275 TOPS or Thor T5000, ROS 2 and Python SDK, EtherCAT in the arm chain. Payload entered as the per-arm figure; the maker publishes no whole-robot payload.

## Sources

- Official page: [rokae.com](https://www.rokae.com/cn/product/show/583/%E8%BD%AE%E5%BC%8F%E5%8F%8C%E8%87%82%E6%9C%BA%E5%99%A8%E4%BA%BAHelios.html)
- [static.rokae.com](https://static.rokae.com/Downloads/Brochure/ROKAE%20Embodied%20Intelligence%20Products.pdf)

Listed by these directories (discovery only, never used as a spec source):

- [embodied.guide](https://embodied.guide/robots/rokae-helios-h2/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-17). Source repository: https://github.com/htcrefactor/robot-catalog*
