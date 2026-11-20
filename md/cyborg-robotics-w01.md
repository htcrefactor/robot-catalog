# Cyborg Robotics Cyborg-W01

> Cyborg's wheeled industrial humanoid on a rotating chassis with 53 DoF, 15 kg dual-arm load and a 5 h battery for plant inspection and material handling.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=cyborg-robotics-w01
- Category: Humanoid
- Locomotion: Wheeled
- Manufacturer: Cyborg Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 585 mm |
| Width | 710 mm |
| Height | 1,600 mm |
| Weight | 170 kg |
| Payload | 15 kg |
| Max speed | 1 m/s (3.6 km/h) |
| Degrees of freedom | 53 |
| Runtime | 5 h |
| Battery | 1,680 Wh |
| Status | Commercial |
| On-board compute | yes |
| Compute | 12-core perception compute platform, 275 TOPS |
| Sensors | Monocular camera, RGB-D depth camera, LiDAR, 3D camera, Six-axis force sensor, IMU, Infrared sensor, Ultrasonic radar |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Maker product page (cyb-org.cn/index.php?id=4): 710 x 585 x 1600 mm (recorded width 710, length 585), 170 kg, 53 total DoF (chassis 3, waist 2, 7 per arm, 16 per dexterous hand), 835 mm single-arm reach and 0-2 m working range, 562 N.m max joint torque, 7.5 kg per arm (15 kg dual-arm, payload_kg), chassis max speed 1 m/s with +/-1 cm navigation accuracy, 5 h battery runtime, 12-core 275 TOPS perception platform, monocular + RGB-D + 3D cameras, LiDAR, infrared, ultrasonic radar, six-axis force sensor, IMU, 4-mic array with noise-reduction board, Wi-Fi 5 / BT 5.2 / 5G, USB 3.0 / gigabit Ethernet / DP. The 14 Nov 2025 launch post (cyb-org.cn/index.php?id=38) states a 48 V 35000 mAh battery (battery_wh = 48x35 = 1680 Wh, computed) and quotes 51 DoF while the product page says 53 and an April 2026 post says 53 - maker pages disagree, product page value recorded.

## Sources

- Official page: [cyb-org.cn](https://www.cyb-org.cn/index.php?id=4)
- [cyb-org.cn](https://www.cyb-org.cn/index.php?id=38)

Listed by these directories (discovery only, never used as a spec source):

- [embodied.guide](https://embodied.guide/robots/cyborg-robotics-w01/)
- [humanoid.guide](https://humanoid.guide/product/cyborg-wo1/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-20). Source repository: https://github.com/htcrefactor/robot-catalog*
