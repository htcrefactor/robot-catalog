# Tokyo Robotics Torobo

> Torque-controlled dual-arm humanoid on an omnidirectional base for AI and contact-rich manipulation research; ROS/MoveIt compatible.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=tokyo-robotics-torobo
- Category: Humanoid
- Locomotion: Wheeled
- Manufacturer: Tokyo Robotics (Japan)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Width | 590 mm |
| Height | 1,615 mm |
| Weight | 120 kg |
| Payload | 7 kg |
| Degrees of freedom | 24 |
| Battery | 1228.8 Wh |
| Released | 2024 |
| Status | Commercial |
| ROS | yes |
| On-board compute | yes |
| Compute | Standard control PC; optional second PC with NVIDIA RTX 4070 |
| Sensors | Joint torque sensors (arms, waist), Optional head: wide-angle stereo camera, fisheye camera, depth camera, stereo microphone |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Wheeled dual-arm humanoid (omni base), not legged. Current spec (new Torobo, 2024): 1615 mm, ~120 kg. Earlier Torobo was 1660 mm; a 2024 press release says 1680 mm/125 kg — used current official page. dof: 24 = 7x2 arms + 3 waist + 3 neck + 4 base, summed from stated axes; payload 7 kg per arm, worst posture; battery_wh computed from brochure DC51.2V×24Ah

## Sources

- Official page: [robotics.tokyo](https://robotics.tokyo/technologies/torobo/)
- [robotics.tokyo](https://robotics.tokyo/data/brochure_Torobo_v2_a4_en_20240610.pdf)
- [prtimes.jp](https://prtimes.jp/main/html/rd/p/000000018.000077249.html)

Listed by these directories (discovery only, never used as a spec source):

- [droid.monster](https://droid.monster/robots/tokyo-robotics/torobo)
- [humanoidversus.com](https://humanoidversus.com/robots/tokyo-robotics-torobo2)
- [embodied.guide](https://embodied.guide/robots/tokyo-robotics-torobo/)
- [humanoid.guide](https://humanoid.guide/product/torobo/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-22). Source repository: https://github.com/htcrefactor/robot-catalog*
