# Muks Robotics Spaceo Pro

> Muks Robotics' wheeled enterprise humanoid with adjustable height for pick-and-place, inspection and material transport in factories and warehouses.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=muks-spaceo-pro
- Category: Humanoid
- Locomotion: Wheeled
- Manufacturer: Muks Robotics (India)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 450 mm |
| Width | 450 mm |
| Height | 1,625 mm |
| Weight | 60 kg |
| Payload | 5 kg |
| Max speed | 1.5 m/s (5.4 km/h) |
| Degrees of freedom | 20 |
| Runtime | 4 h |
| Battery | 1,152 Wh |
| Status | Pilot |
| On-board compute | yes |
| Compute | NVIDIA Jetson AGX Orin (~275 TOPS) + Ryzen 7, 16GB RAM |
| Sensors | Intel RealSense depth camera, 3x 5MP RGB camera, 4-mic array |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

WHEELED, not legged: maker spec lists 2 base DoF and an integrated base trolley (wheeled enterprise humanoid). Height adjustable 1625-2100 mm (height_mm set to min 1625). 200 kg is the base-trolley load; per-arm payload 5 kg (payload_kg=5). Battery 25.6 V 45 Ah LiFePO4 = 1152 Wh (computed). Maker spec says 6 DoF per arm; older maker page (spaceo-pro-2) and pitch deck say 7 DoF/arm, 65 kg, 2 m/s, 5 h — current page values used. Available for pilots.

## Sources

- Official page: [muksrobotics.com](https://muksrobotics.com/spaceo-pro)

Listed by these directories (discovery only, never used as a spec source):

- [data.robo2u.com](https://data.robo2u.com/robots/muks-robotics-spaceo-pro)
- [embodied.guide](https://embodied.guide/robots/muks-robotics-spaceo-pro/)
- [humanoid.guide](https://humanoid.guide/product/spaceo-pro/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-28). Source repository: https://github.com/htcrefactor/robot-catalog*
