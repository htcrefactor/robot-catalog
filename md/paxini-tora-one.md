# PaXini Tech TORA ONE

> PaXini's wheeled dual-arm humanoid with tactile-sensing dexterous hands for logistics, healthcare, manufacturing and service tasks.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=paxini-tora-one
- Category: Humanoid
- Locomotion: Wheeled
- Manufacturer: PaXini Tech (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Height | 1,860 mm |
| Payload | 5 kg |
| Max speed | 0.6 m/s (2.2 km/h) |
| Degrees of freedom | 53 |
| Runtime | 8 h |
| Status | Commercial |
| Sensors | 5x RGB camera, 2x RGBD camera, LiDAR (laser SLAM), 2280 ITPU tactile sensing units |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

WHEELED humanoid (wheeled chassis, not legged): maker chassis spec max 0.6 m/s, 0.4 rad/s turn, 2 cm obstacles, 7 deg slope. Height variable 1.46 m (waist folded) to 1.86 m (extended) — height_mm set to extended 1860. 53 DoF = 21 body + 32 hands (16/hand, 13 active + 3 passive). Payload = rated 5 kg per arm straight-arm. Battery 40 Ah (voltage not stated, so no Wh), 6 h charge, 8 h runtime. CONFLICT: older maker subdomain (tac-flow.paxini.com) lists 47 DoF, 6 kg/arm, 1 m/s chassis, 7824 tactile channels — current paxini.com/en/robot values used. Sold via maker mall ('contact to buy'); no public price.

## Sources

- Official page: [paxini.com](https://paxini.com/en/robot)

Listed by these directories (discovery only, never used as a spec source):

- [data.robo2u.com](https://data.robo2u.com/robots/paxini-technology-tora-one)
- [droid.monster](https://droid.monster/robots/paxini/tora-one)
- [embodied.guide](https://embodied.guide/robots/paxini-tora-one/)
- [humanoid.guide](https://humanoid.guide/product/toraone/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-16). Source repository: https://github.com/htcrefactor/robot-catalog*
