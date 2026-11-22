# Zebra Technologies (Fetch Robotics) Fetch Mobile Manipulator

> ROS-based research mobile manipulator with telescoping torso, 7-DoF arm and pan-tilt head for indoor manipulation research.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=zebra-fetch-mobile-manipulator
- Category: Mobile platform
- Locomotion: Wheeled
- Manufacturer: Zebra Technologies (Fetch Robotics) (United States)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Width | 508 mm |
| Height | 1,491 mm |
| Weight | 113.3 kg |
| Payload | 6 kg |
| Max speed | 1 m/s (3.6 km/h) |
| Degrees of freedom | 13 |
| Status | Commercial |
| API | yes |
| ROS | yes |
| On-board compute | yes |
| Compute | Intel i5 Haswell, 16 GB RAM, 120 GB SSD |
| Sensors | 2D laser (25 m, 220°), RGB-D camera (Primesense Carmine 1.09), 2x 6-DoF IMU |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Re-checked 2026-11-17: Zebra/Fetch have no live product page (zebra.com/us/en/products/robotics.html returns 404; Zebra sold its robotics automation business - formerly Fetch Robotics - to Skild AI, closing 2026-03-27 per Zebra's 10-Q) and the maker's documentation host docs.fetchrobotics.com no longer resolves (ERR_TUNNEL_CONNECTION_FAILED; page fetch HTTP 500), although the Wayback Machine holds a 200 snapshot of this page from 2024-04-18. Stored figures are the Fetch hardware documentation values (113.3 kg, 508 mm wide / 559 mm dia base, 1.49 m with torso up, 6 kg arm payload, 1.0 m/s, 13 DoF, i5 / 16 GB / 120 GB SSD, 3 h to 90%) plus the Fetch spec sheet copy on a reseller host; no value was changed in this pass.

## Sources

- Official page: [docs.fetchrobotics.com](https://docs.fetchrobotics.com/robot_hardware.html)
- [docs.fetchrobotics.com](https://docs.fetchrobotics.com/api_overview.html)
- [amaasia.net](https://www.amaasia.net/product%20PDF/Fetch_spec_download.pdf)

Listed by these directories (discovery only, never used as a spec source):

- [data.robo2u.com](https://data.robo2u.com/robots/fetch-mobile-manipulator)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-22). Source repository: https://github.com/htcrefactor/robot-catalog*
