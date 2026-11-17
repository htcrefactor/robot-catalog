# KUKA KMR iisy

> KUKA autonomous mobile cobot combining a SLAM-navigating platform (up to 200 kg) with an LBR iisy arm for machine tending, pick-and-place and cleanroom logistics.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=kuka-kmr-iisy
- Category: Mobile platform
- Locomotion: Wheeled
- Manufacturer: KUKA (Germany)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 1,120 mm |
| Width | 695 mm |
| Height | 700 mm |
| Weight | 425 kg |
| Payload | 200 kg |
| Max speed | 1.5 m/s (5.4 km/h) |
| Degrees of freedom | 6 |
| Runtime | 8 h |
| IP rating | IP54 |
| Released | 2023 |
| Status | Commercial |
| Sensors | Safety laser scanners (LiDAR), 3D cameras (obstacles up to 2 m), Joint torque sensors |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Mobile manipulator: differential-drive platform plus integrated LBR iisy 6-axis cobot (11 or 15 kg arm payload). payload_kg = platform capacity 200 kg (my.KUKA lists rated payload 200 kg for KMR iisy-2; a CR C+ variant lists 100 kg). Dimensions/weight from KUKA's my.KUKA product page for KMR iisy-2 (1120 x 695 x 700 mm, 425 kg, 8 h max operating time) - seen in search excerpt of the maker portal, not opened; main product page (opened) confirms 695 x 1120 mm platform, 1.5 m/s, IP54, ISO cleanroom class 3. Launched 2023 (press release July 2023). dof = 6 (arm only).

## Sources

- Official page: [kuka.com](https://www.kuka.com/en-de/products/amr-autonomous-mobile-robotics/mobile-robot-systems/kmr-iisy-autonomous-mobile-cobot)

Listed by these directories (discovery only, never used as a spec source):

- [data.robo2u.com](https://data.robo2u.com/robots/kuka-kmr-iisy)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-16). Source repository: https://github.com/htcrefactor/robot-catalog*
