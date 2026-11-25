# GENISOM AI (ZsiBot) Genisom L2-W

> 27 kg wheel-legged variant of the Gangben L2 quadruped: IP66, 16 kg payload, up to 5.5 h runtime, LiDAR+GNSS navigation.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=genisom-gangben-l2-w
- Category: Wheel-legged
- Locomotion: Wheel-legged
- Manufacturer: GENISOM AI (ZsiBot) (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 760 mm |
| Width | 450 mm |
| Height | 500 mm |
| Weight | 27 kg |
| Payload | 16 kg |
| Max speed | 3.7 m/s (13.3 km/h) |
| Degrees of freedom | 12 |
| Runtime | 5.5 h |
| Battery | 756 Wh |
| IP rating | IP66 |
| Status | Commercial |
| SDK | yes |
| Compute | 8-core high-performance CPU |
| Sensors | Stereo camera (2.07 MP x2), IMU, UWB (GLUE omnidirectional following) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Official URL is the 钢镚 L2 page, whose spec table lists L2 (point-foot), L2-W (wheel-legged) and L2-W Ultra; values here are L2-W. Limit speed 5 m/s; payload ≈16 kg (150 kg static). '¥39,999 起' on page is the L2 family starting price, not specific to L2-W, so price left null. 756 Wh battery stated on page (spec table lists 15000 mAh). Re-checked 2026-11-17: the L2 product page (opened) carries a per-variant spec table with an explicit L2-W column - standing 760x450x500 mm, prone 780x550x190 mm, 27 kg with battery, ~16 kg continuous payload (150 kg static), 3.7 m/s max / 5 m/s limit, 25 cm continuous stairs, 40 deg slope, 5.5 h no-load / 3.5 h full-load, 20 km / 12 km range, 756 Wh (15000 mAh), 1.5 h charge, 12 joint motors / 95 N.m, 4G, UWB, stereo camera, IP66, -20~55 C. CORRECTION: LiDAR and GNSS/RTK are NOT in the L2-W column (the 96-line LiDAR x2 and RTK are L2-W Ultra only), so they were removed from sensors; dof filled with the 12 joint motors. The page's marketing copy ('RoamerX ... LiDAR + GNSS', '720 deg fusion sensing') describes the family, not the L2-W configuration.

## Sources

- Official page: [genisomai.com](https://www.genisomai.com/product-robot/L2)

Listed by these directories (discovery only, never used as a spec source):

- [embodied.guide](https://embodied.guide/robots/genisom-gangben-l2-w/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-25). Source repository: https://github.com/htcrefactor/robot-catalog*
