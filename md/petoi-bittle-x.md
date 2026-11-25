# Petoi Bittle X

> Palm-sized open-source, voice-controlled ESP32 robot dog kit for STEM education and hobby robotics, programmable in blocks, C++ and Python.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=petoi-bittle-x
- Category: Quadruped
- Locomotion: Legged
- Manufacturer: Petoi (United States)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 190 mm |
| Weight | 0.353 kg |
| Payload | 0.45 kg |
| Degrees of freedom | 9 |
| Runtime | 1 h |
| Battery | 7.4 Wh |
| Status | Commercial |
| SDK | yes |
| SDK name | OpenCat (C++/Arduino), OpenCat Python API, Petoi Coding Blocks |
| On-board compute | yes |
| Compute | BiBoard ESP32-WROOM-32D (optional Raspberry Pi mount) |
| Sensors | 6-axis IMU, Voice command module (mic) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Maker spec page: standing dimensions 190 x 153 x 107 mm (axis order not labelled; only length_mm filled), weight 269-353 g depending on version/arm (older spec page: 200 x 110 x 110 mm, 265-290 g). 9 servo joints (8 legs + 1 neck) = 9 DoF. Battery 7.4 V 1000 mAh (= 7.4 Wh), ~1 h runtime. Maker FAQ (search excerpt) says it carries 1 lb (~0.45 kg) - filled; FAQ speed '2 body lengths/s, or 40 mm/s' is internally inconsistent - not filled. Price not read from an opened maker page (aggregator says $319 kit) - not filled. Variants: Bittle X, Bittle X V2, Bittle X V2+Arm.

## Sources

- Official page: [petoi.com](https://www.petoi.com/products/petoi-robot-dog-bittle-x-voice-controlled)
- [petoi.com](https://www.petoi.com/pages/robot-dog-bittle-x-technical-specifications)
- [github.com](https://github.com/PetoiCamp/OpenCat-Quadruped-Robot)
- [github.com](https://github.com/PetoiCamp/ros_opencat/blob/ros1/petoi_ROS_model_docs/bittle_ros/bittle_description/urdf/bittle.xacro)
- [github.com](https://github.com/PetoiCamp/ros_opencat)

Listed by these directories (discovery only, never used as a spec source):

- [data.robo2u.com](https://data.robo2u.com/robots/petoi-bittle-x)
- [roboticsrankings.com](https://roboticsrankings.com/robots/petoi-bittle-x/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-25). Source repository: https://github.com/htcrefactor/robot-catalog*
