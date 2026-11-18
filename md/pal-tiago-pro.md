# PAL Robotics TIAGo Pro

> Open-source ROS 2 dual-arm mobile manipulator with an omnidirectional base and expressive head for embodied-AI and HRI research and applied development.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=pal-tiago-pro
- Category: Humanoid
- Locomotion: Wheeled
- Manufacturer: PAL Robotics (Spain)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 720 mm |
| Width | 500 mm |
| Height | 1,550 mm |
| Weight | 80 kg |
| Payload | 3 kg |
| Degrees of freedom | 23 |
| Runtime | 4 h |
| Status | Commercial |
| SDK | yes |
| SDK name | PAL SDK (Docker image) |
| ROS | yes |
| On-board compute | yes |
| Compute | Intel i5, 16 GB RAM, 512 GB SSD (optional i7/32 GB, optional NVIDIA Jetson) |
| Sensors | 2x 2D LiDAR (10 m, 360°), RGB-D head camera, Joint torque sensing (arms), 4-mic array, Optional wrist 6-axis F/T sensor |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Category correction: TIAGo Pro is a WHEELED mobile manipulator (omnidirectional 4x mecanum base, dual 7-DoF arms, lifting torso), not a humanoid; PAL lists it under 'Mobile Manipulators' -> suggest category 'Mobile platform'. Height is a range 1200-1550 mm (lifting torso); height_mm set to max 1550. Payload 3 kg is PER ARM (excluding end-effector). Footprint 500 x 720 mm (which is length vs width not stated; length_mm=720, width_mm=500 assumed by orientation). Autonomy 4 h. No max speed, battery Wh, IP rating or price published. Release year not stated on spec page (PAL's 'Introducing TIAGo Pro' blog dates from 2023 but not opened).

## Sources

- Official page: [pal-robotics.com](https://pal-robotics.com/robot/tiago-pro/)
- [pal-robotics.com](https://pal-robotics.com/datasheet/tiago-pro/)
- [github.com](https://github.com/pal-robotics/tiago_pro_robot)
- [github.com](https://github.com/pal-robotics/tiago_pro_robot/blob/humble-devel/tiago_pro_description/robots/tiago_pro.urdf.xacro)
- [github.com](https://github.com/pal-robotics/tiago_pro_simulation)

Listed by these directories (discovery only, never used as a spec source):

- [data.robo2u.com](https://data.robo2u.com/robots/pal-robotics-tiago-pro)
- [roboticsrankings.com](https://roboticsrankings.com/robots/pal-robotics-tiago-pro/)
- [embodied.guide](https://embodied.guide/robots/pal-robotics-tiago-pro/)
- [humanoid.guide](https://humanoid.guide/product/tiago-pro/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-18). Source repository: https://github.com/htcrefactor/robot-catalog*
