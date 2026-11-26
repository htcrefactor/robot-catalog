# AI² Robotics AlphaBot 2

> Wheeled dual-arm general-purpose robot driven by AI² Robotics' GOVLA vision-language-action model for automotive, semiconductor, biotech and public-service tasks.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=ai2-robotics-alphabot-2
- Category: Humanoid
- Locomotion: Wheeled
- Manufacturer: AI² Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Height | 1,800 mm |
| Weight | 135 kg |
| Payload | 4 kg |
| Max speed | 1.5 m/s (5.4 km/h) |
| Min speed | 0.1 m/s |
| Wheels | 2 |
| Degrees of freedom | 22 |
| Runtime | 6 h |
| Battery | 1,440 Wh |
| Released | 2025 |
| Status | Commercial |
| API | yes |
| SDK | yes |
| SDK name | AlphaBotCore SDK (C++/Python) |
| On-board compute | yes |
| Compute | NVIDIA Jetson AGX Orin 64GB |
| Sensors | RealSense D435 (head, chest, back), RealSense D405 (wrists), Linear 4-mic array |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Wheeled dual-arm humanoid (differential chassis, folding lift legs). Launch release said 34+ DoF incl. end effectors; hardware docs say 22 DoF excl. end effectors — used docs. spec: runtime 4–6 h (max used); battery_wh computed from 48V×30Ah; payload 4 kg rated per arm; wheel_count = 2 drive wheels (differential)

## Sources

- Official page: [docs.ai2robotics.com](https://docs.ai2robotics.com/en/alphabot2/hardware/architecture/)
- [docs.ai2robotics.com](https://docs.ai2robotics.com/en/start/product-introduction)
- [ai2robotics.com](https://ai2robotics.com/en/%E6%99%BA%E5%B9%B3%E6%96%B9%E5%8F%91%E5%B8%83%E5%85%A8%E6%96%B0%E4%B8%80%E4%BB%A3%E6%99%BA%E8%83%BD%E6%9C%BA%E5%99%A8%E4%BA%BAalphabot-2%E5%BC%80%E5%90%AFagi%E7%BB%88%E7%AB%AF%E6%96%B0/)

Listed by these directories (discovery only, never used as a spec source):

- [humanoidversus.com](https://humanoidversus.com/robots/ai2-robotics-alphabot-2)
- [embodied.guide](https://embodied.guide/robots/ai2-robotics-alphabot-2/)
- [humanoid.guide](https://humanoid.guide/product/alphabot-2/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-26). Source repository: https://github.com/htcrefactor/robot-catalog*
