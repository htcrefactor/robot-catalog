# Astrall Dynamics Hypertron-SW01

> Mid-sized quadruped for inspection, patrol and firefighting duty that carries 40 kg over all-terrain ground and runs on hot-swappable batteries.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=astrall-dynamics-hypertron-sw01
- Category: Quadruped
- Locomotion: Legged
- Manufacturer: Astrall Dynamics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 929 mm |
| Width | 556 mm |
| Height | 656 mm |
| Weight | 50 kg |
| Payload | 40 kg |
| Max speed | 8 m/s (28.8 km/h) |
| Runtime | 6 h |
| Battery | 2,166 Wh |
| IP rating | IP67 |
| Status | Commercial |
| SDK | yes |
| On-board compute | yes |
| Compute | Industrial-grade 8-core processor, 16 GB RAM / 64 GB storage |
| Sensors | Solid-state LiDAR x1 (120 deg H x 90 deg V, 30 m), RGB camera 1600 x 1296, 9-axis IMU |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Maker spec table (Shenzhen Astrall/璇玑动力, checked 2026-11-27): standing 929 x 556 x 656 mm, about 50 kg with battery, 40 kg all-terrain dynamic payload, 50 kg continuous walking payload, 120 kg short-term static standing load, 6 h no-load and 3 h with a 40 kg load, dual hot-swappable 57.6 V 18.8 Ah packs (battery_wh 2166 derived as 2 x 57.6 V x 18.8 Ah), IP67, -20 to 55 C, 25 cm continuous stair steps, 2 h fast charge to 80 %, industrial 8-core compute with 16 GB RAM and 64 GB storage, solid-state LiDAR 120 x 90 deg at 30 m, 1600 x 1296 RGB camera, 9-axis IMU, gigabit Ethernet x2 and 48 V / 240 W expansion power, open SDK. The maker's own footnotes limit the headline figures: 8 m/s is a laboratory peak and the shipping robot is capped at 1 m/s in all-terrain mode and 5-6 m/s in low-centre-of-gravity mode; 45 deg climb and 100 cm obstacle clearing are laboratory limits with 30 deg recommended; 240 N.m is a momentary peak. No price. Unlike its wheel-legged sibling T01 this one walks on feet only, so locomotion is Legged.

## Sources

- Official page: [astralldynamics.com](https://www.astralldynamics.com/en-US/product/1006.html)
- [astralldynamics.com](https://www.astralldynamics.com/product/6.html)

Listed by these directories (discovery only, never used as a spec source):

- [embodied.guide](https://embodied.guide/robots/astrall-dynamics-hypertron-sw01/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-27). Source repository: https://github.com/htcrefactor/robot-catalog*
