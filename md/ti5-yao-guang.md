# Ti5 Robot T170A "Yao Guang"

> Ti5 Robot's lightweight 1.7 m bipedal humanoid built on its in-house high-torque joint modules, shown at WAIC 2024.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=ti5-yao-guang
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: Ti5 Robot (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Height | 1,700 mm |
| Weight | 48 kg |
| Payload | 3 kg |
| Degrees of freedom | 44 |
| Released | 2024 |
| On-board compute | yes |
| Compute | Jetson AGX Orin 64 GB dev kit (flagship); Jetson Orin Nano 8 GB (standard) |
| Sensors | Depth camera Intel RealSense D435i (flagship), High-precision attitude sensor (IMU) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

RENAME: 'Yao Guang' (瑶光) is the name of a unit of Ti5's second-gen T170A humanoid launched at WAIC 4 Jul 2024 (maker news ti5robot.com/h-nd-39.html, read via search excerpt; page now 404). Maker release: 1.7 m, 48 kg, 44 DoF, 5 kg single-hand load, NVIDIA Jetson AGX Orin 64GB, LiDAR + binocular cameras. Maker's current English site (ti5robotics.com) lists T170A and newer T170A V2/T170C/T140A; a 2025 maker EN page (seen in excerpts) also cites dual-arm load 20-40 kg, five RealSense cameras, 6-mic array — newer config, not filled. Status left blank (superseded by T170A V2 likely). Maker model page opened 2026-11-17 (ti5robotics.com .../T170A.html): 48 kg, 1.5 m arm span, 44 active DoF, 32 joint motors, single-arm load 3 kg, hand 6 active DoF (0.5 kg standard / 3 kg flagship), 18-bit encoders, 48 V 10 Ah battery, CAN/EtherCAT, dual-arm API; standard model Jetson Orin Nano 8 GB, flagship Jetson AGX Orin 64 GB dev kit + RealSense D435i + 2x six-axis force sensors. CONFLICT: the 2024 WAIC release (now 404) said 5 kg single-hand load; the current maker page says 3 kg single-arm, which is stored. Height 1.7 m comes from the T170A naming/2024 release; the current page's parameter table omits height. Note the maker site serves swapped pages (T170A-V2.html returns the T170A table), so page-to-model mapping was taken from the printed heading.

## Sources

- Official page: [ti5robotics.com](https://www.ti5robotics.com/products/Humanoid-Robot-Actuator/T170A.html)
- [ti5robotics.com](https://www.ti5robotics.com/products/Humanoid-Robot-Actuator)

Listed by these directories (discovery only, never used as a spec source):

- [data.robo2u.com](https://data.robo2u.com/robots/ti5-robot-yao-guang)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-25). Source repository: https://github.com/htcrefactor/robot-catalog*
