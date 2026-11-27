# Devanthro Robody

> Munich-based Devanthro's teleoperated care robot: a soft-skinned wheeled humanoid that a remote operator or family member drives through a VR headset in a patient's home.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=devanthro-robody
- Category: Humanoid
- Locomotion: Wheeled
- Manufacturer: Devanthro (Germany)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Height | 1,650 mm |
| Weight | 60 kg |
| Payload | 1.5 kg |
| Degrees of freedom | 15 |
| Runtime | 6 h |
| Status | Commercial |
| ROS | yes |
| On-board compute | yes |
| Compute | NVIDIA Jetson Orin + Orin Nano |
| Sensors | 4K fisheye RGB camera, mm-wave radar, Stereo microphone |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

13 values from 1 document, checked against maker sources on 2026-11-13.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Form factor | wheeled (bimanual torso on a wheeled base) | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/devanthro-robody) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Height (standing) | 165 cm | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/devanthro-robody) |
| Weight | 60 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/devanthro-robody) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total degrees of freedom | 15 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/devanthro-robody) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Runtime per charge | 360 min | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/devanthro-robody) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Hands | fixed-grippers | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/devanthro-robody) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Sales status | b2b-only | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/devanthro-robody) |
| Who can buy | business | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/devanthro-robody) |
| Route to US | no | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/devanthro-robody) |
| Route to EU | reseller | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/devanthro-robody) |
| Sellers listed | 1 | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/devanthro-robody) |
| Documented uses | Household help | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/devanthro-robody) |

### Payload

| Spec | Value | Note | Source |
|---|---|---|---|
| Rated payload | 1.5 kg | HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/devanthro-robody) |

## Documents

- [HumanoidStore datasheet – Devanthro Robody (CC BY 4.0)](https://humanoidstore.co/robots/devanthro-robody)

## Notes

Maker technology page (devanthro.com/technology): height 1.65 m, 60 kg, 6-DoF arms with 1.5 kg payload each (payload_kg = per arm), 3-DoF neck, two-finger gripper, QDD plus Dynamixel actuators, differential drive, 6 h runtime with self-docking, 4K fisheye RGB camera, mm-wave radar, stereo mic, NVIDIA Jetson Orin + Orin Nano compute, ROS2 middleware. 15 DoF recorded as the sum of the maker's published joints (2 arms x 6 + 3 neck); the base and face are not given DoF counts. The robot is sold to care providers, not consumers, and the maker publishes no price. Teleoperated today with increasing AI autonomy.

## Sources

- Official page: [devanthro.com](https://www.devanthro.com/technology/)
- [devanthro.com](https://www.devanthro.com/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-27). Source repository: https://github.com/htcrefactor/robot-catalog*
