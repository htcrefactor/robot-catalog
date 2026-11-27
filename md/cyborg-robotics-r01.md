# Cyborg Robotics Cyborg-R01

> Shenzhen Cyborg's full-size bipedal industrial humanoid with 62 DoF and 20 kg dual-arm load for inspection, logistics and heavy-industry work.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=cyborg-robotics-r01
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: Cyborg Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 327 mm |
| Width | 578 mm |
| Height | 1,800 mm |
| Weight | 80 kg |
| Payload | 20 kg |
| Degrees of freedom | 62 |
| Battery | 1,440 Wh |
| Status | Commercial |
| On-board compute | yes |
| Compute | 12-core perception compute platform, 275 TOPS |
| Sensors | LiDAR, RGB-D depth camera, Fisheye camera, IMU, Six-axis force sensor |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Maker product page for the full-size biped (cyb-org.cn/index.php?id=6, checked 2026-11-17): height x width x thickness 1800 x 578 x 327 mm, 62 DoF, dual-arm load over 20 kg (payload_kg), slopes over 10 deg, 15 cm obstacles, self-recovery after a fall, 45 N.s impulse resistance, one-minute hot-swap batteries (main 48 V 15000 mAh on SE / 48 V 30000 mAh on PRO, plus a 48 V 3500 mAh backup), a 12-core 275 TOPS perception platform, LiDAR with IMU and a six-axis force sensor, fisheye plus RGB-D cameras, Wi-Fi 5 / BT 5.2 / 5G. Weight: the page table gives 75 kg (SE) and 80 kg (PRO); the PRO figure is recorded and the SE value noted here (the WRC exhibitor listing cites 70 kg). battery_wh = 48 V x 30 Ah = 1440 Wh for the PRO main pack, computed, excluding the 3.5 Ah backup. No runtime or IP rating is published.

## Sources

- Official page: [cyb-org.cn](https://www.cyb-org.cn/index.php?id=6)
- [cyb-org.cn](https://www.cyb-org.cn/index.php?id=36)

Listed by these directories (discovery only, never used as a spec source):

- [embodied.guide](https://embodied.guide/robots/cyborg-robotics-r01/)
- [humanoid.guide](https://humanoid.guide/product/cyborg-ro1/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-27). Source repository: https://github.com/htcrefactor/robot-catalog*
