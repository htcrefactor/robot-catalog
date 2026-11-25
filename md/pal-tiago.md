# PAL Robotics TIAGo

> Modular ROS-based mobile manipulator with lifting torso and 7-DoF arm, widely used for research and service robotics.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=pal-tiago
- Category: Mobile platform
- Locomotion: Wheeled
- Manufacturer: PAL Robotics (Spain)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 540 mm |
| Width | 540 mm |
| Height | 1,450 mm |
| Weight | 70 kg |
| Payload | 3 kg |
| Max speed | 1 m/s (3.6 km/h) |
| Degrees of freedom | 12 |
| Runtime | 4 h |
| Battery | 720 Wh |
| Status | Commercial |
| API | yes |
| SDK | yes |
| SDK name | PAL OS SDK (ROS/ROS 2) |
| ROS | yes |
| Sensors | Laser range-finder, Sonars, IMU, RGB-D camera, Stereo microphones, Wrist force/torque sensor (optional) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

PAL product page, 2024 datasheet and PAL OS docs. Height = top of torso-lift range (110-145 cm); footprint Ø54 cm used for length/width. Weight 70 kg (datasheet; docs list 60-72 kg by config). Runtime 4-5 h with 1 battery (8-10 h with 2), lower bound used. DoF 12 = base 2 + torso 1 + arm 7 + head 2.

## Sources

- Official page: [pal-robotics.com](https://pal-robotics.com/robot/tiago)
- [pal-robotics.com](http://pal-robotics.com/wp-content/uploads/2024/04/Datasheet-TIAGo.pdf)
- [docs.pal-robotics.com](https://docs.pal-robotics.com/sdk/24.09/hardware/tiago/hardware-overview.html)
- [github.com](https://github.com/pal-robotics/tiago_robot)
- [github.com](https://github.com/pal-robotics/tiago_robot/blob/humble-devel/tiago_description/robots/tiago.urdf.xacro)
- [github.com](https://github.com/pal-robotics/tiago_simulation)

Listed by these directories (discovery only, never used as a spec source):

- [data.robo2u.com](https://data.robo2u.com/robots/pal-robotics-tiago)
- [roboticsrankings.com](https://roboticsrankings.com/robots/pal-robotics-tiago/)
- [embodied.guide](https://embodied.guide/robots/pal-robotics-tiago/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-25). Source repository: https://github.com/htcrefactor/robot-catalog*
