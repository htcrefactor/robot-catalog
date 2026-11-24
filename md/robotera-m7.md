# RobotEra ROBOTERA M7

> Upper-body general-purpose humanoid with two 7-DoF arms and 12-DoF dexterous hands on an adjustable-height base, for teleoperation, data collection and manipulation tasks.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=robotera-m7
- Category: Humanoid
- Locomotion: Wheeled
- Manufacturer: RobotEra (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 675 mm |
| Width | 650 mm |
| Height | 1,810 mm |
| Weight | 70 kg |
| Payload | 10 kg |
| Degrees of freedom | 43 |
| Runtime | 4 h |
| Battery | 864 Wh |
| Status | Commercial |
| SDK | yes |
| ROS | yes |
| On-board compute | yes |
| Compute | AMD Ryzen AI 9 HX 370 (32 GB, 1 TB SSD) + optional NVIDIA Jetson AGX Orin 64GB (275 TOPS) |
| Sensors | Depth camera (head), Wrist cameras (optional), Voice module / microphone |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Official M7 manual (docs.cloud.robotera.com v1.11.0): half-body (upper-body) humanoid with no lower limbs, on a 650x675 mm base, height adjustable 1585-1810 mm. Manual intro says 42 DoF but spec table says 43 (7x2 arms, 3 waist, 2 neck, 12x2 hands) - used 43. Weight 'approximately 70 kg' (resellers quote 65 kg). Battery 57.6 V 15 Ah 864 Wh; usage 45 min-4 h depending on use. Base mobility not described in manual, so locomotion left blank. Single-arm load 10 kg. ROS2 Humble SDK.

## Sources

- Official page: [robotera.com](https://www.robotera.com/en/)
- [docs.cloud.robotera.com](https://docs.cloud.robotera.com/en/manuals/M7/v1.11.0)

Listed by these directories (discovery only, never used as a spec source):

- [botupyourlife.com](https://botupyourlife.com/en/robots/robotera-m7/)
- [embodied.guide](https://embodied.guide/robots/robotera-m7/)
- [humanoid.guide](https://humanoid.guide/product/robotera-m7/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-24). Source repository: https://github.com/htcrefactor/robot-catalog*
