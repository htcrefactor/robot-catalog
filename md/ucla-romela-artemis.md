# UCLA RoMeLa ARTEMIS

> UCLA RoMeLa's open-source full-size bipedal research humanoid with proprioceptive actuators, built for fast walking, running and RoboCup soccer.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=ucla-romela-artemis
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: UCLA RoMeLa (United States)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Height | 1,400 mm |
| Weight | 37 kg |
| Max speed | 2.1 m/s (7.6 km/h) |
| Degrees of freedom | 20 |
| Battery | 399.6 Wh |
| Released | 2023 |
| Status | Research |
| On-board compute | yes |
| Compute | HP Elite Mini 800 G9 (Intel i7-12700T) + NVIDIA RTX 3050 Ti |
| Sensors | ZED 2 stereo camera, MicroStrain 3DM-CV7 IMU, Foot toe/heel contact sensors with per-foot 6-axis IMU |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Maker = UCLA RoMeLa (academic research lab, not a company). Values from RoMeLa's own open-source paper (IEEE Humanoids 2025, artemis.romela.org): 140 cm, 37 kg, 20 active DoF (5/leg, 4/arm, 2 head), walks up to 2.1 m/s and runs. Conflicts in other maker-side sources: UCLA press (2023) 4 ft 8 in / 85 lb (1422 mm / 38.6 kg); team RoboCup spec sheet 1.5 m / 45 kg, 0.5 m/s untethered - newest paper values used. Battery: 99.9 Wh 22.2 V modules, typically four on board (~400 Wh total, computed). Open-sourced CAD, URDF, actuator and controller components; simulators Gazebo and MuJoCo. Not for sale.

## Sources

- Official page: [artemis.romela.org](https://artemis.romela.org/)
- [artemis.romela.org](https://artemis.romela.org/static/pdfs/artemis_final.pdf)

Listed by these directories (discovery only, never used as a spec source):

- [data.robo2u.com](https://data.robo2u.com/robots/ucla-romela-artemis)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-24). Source repository: https://github.com/htcrefactor/robot-catalog*
