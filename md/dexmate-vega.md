# Dexmate Vega

> Dexmate's general-purpose wheeled humanoid sold as a development platform: two 7-DoF arms on a 3-DoF torso and omni-directional base, with a 20 h battery and Python/C++/Rust APIs.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=dexmate-vega
- Category: Humanoid
- Locomotion: Wheeled
- Manufacturer: Dexmate (United States)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 660 mm |
| Width | 560 mm |
| Height | 660 mm |
| Weight | 135 kg |
| Payload | 5 kg |
| Degrees of freedom | 23 |
| Runtime | 20 h |
| Status | Commercial |
| Price | list price on the maker's own shop (shop.dexmate.ai), hardware only; checked 2026-11 |
| API | yes |
| SDK | yes |
| SDK name | Python, C++ and Rust APIs with SimReady URDF/USD models and fleet management (DexHub) |
| On-board compute | yes |
| Compute | NVIDIA Jetson AGX Thor |
| Sensors | Stereo RGB camera (head), 2 LiDAR (front and rear), 4 RGB cameras (base) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

14 values from 1 document, checked against maker sources on 2026-11-13.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Form factor | wheeled (bimanual torso on a wheeled base) | configuration: Vega 1 Pro; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/dexmate-vega) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Weight | 135 kg | configuration: Vega 1 Pro; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/dexmate-vega) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total degrees of freedom | 24 | configuration: Vega 1 Pro; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/dexmate-vega) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Runtime per charge | 1,200 min | configuration: Vega 1 Pro; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/dexmate-vega) |

### Manipulation

| Spec | Value | Note | Source |
|---|---|---|---|
| Hands | optional | configuration: Vega 1 Pro; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/dexmate-vega) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Sales status | shipping-now | configuration: Vega 1 Pro; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/dexmate-vega) |
| Who can buy | anyone | configuration: Vega 1 Pro; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/dexmate-vega) |
| Price | 75,000 USD | configuration: Vega 1 Pro; list price (maker price); HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/dexmate-vega) |
| Delivered price to US | 75,101 USD | configuration: Vega 1 Pro; before sales tax; route: estimate: domestic delivery; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/dexmate-vega) |
| Route to US | direct | configuration: Vega 1 Pro; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/dexmate-vega) |
| Route to EU | unclear | configuration: Vega 1 Pro; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/dexmate-vega) |
| Sellers listed | 1 | configuration: Vega 1 Pro; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/dexmate-vega) |
| Documented uses | Robotics R&D | configuration: Vega 1 Pro; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/dexmate-vega) |

### Payload

| Spec | Value | Note | Source |
|---|---|---|---|
| Rated payload | 5 kg | configuration: Vega 1 Pro; HumanoidStore open data (CC BY 4.0), checked 2026-10 | [humanoidstore.co](https://humanoidstore.co/robots/dexmate-vega) |

## Documents

- [HumanoidStore datasheet – Dexmate Vega (CC BY 4.0)](https://humanoidstore.co/robots/dexmate-vega)

## Notes

Maker product page and its own shop (shop.dexmate.ai): 'Vega 1 Pro' is a general-purpose wheeled humanoid, 23 DoF (arms 14 = 7 each, torso 3, head 3, base 3), 135 kg (298 lb), 5 kg (10+ lb) per arm in any pose (payload_kg = per-arm), floor-to-2.2 m reach, folded 0.66 x 0.56 x 0.66 m and 2.50 m max height with arms raised, 20 h operation per charge, NVIDIA Jetson AGX Thor compute, Python/C++/Rust APIs, SimReady URDF/USD, fleet management, VR and exoskeleton teleoperation, stereo RGB head camera, front and rear LiDAR, 4 base RGB cameras, optional F/T sensing. Maker prices it at USD 75,000 hardware-only on its own shop (end effectors and AI not included), which replaces the HumanoidStore figure. The maker calls out that no autonomy is bundled.

## Sources

- Official page: [dexmate.com](https://www.dexmate.com/product/vega-1-pro)
- [shop.dexmate.ai](https://shop.dexmate.ai/products/vega)
- [humanoidstore.co](https://humanoidstore.co/robots/dexmate-vega)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-18). Source repository: https://github.com/htcrefactor/robot-catalog*
