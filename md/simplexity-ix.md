# Simplexity Robotics iX

> Wheeled humanoid for lobbies and public service work: 24 active DoF, a 540 mm lifting waist, two 7-DoF force-controlled arms and a four-wheel-steering base.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=simplexity-ix
- Category: Humanoid
- Locomotion: Wheeled
- Manufacturer: Simplexity Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 670 mm |
| Width | 548 mm |
| Height | 1,060 mm |
| Weight | 160 kg |
| Payload | 3 kg |
| Max speed | 1.5 m/s (5.4 km/h) |
| Degrees of freedom | 24 |
| Runtime | 4.5 h |
| Battery | 1,650 Wh |
| Released | 2026 |
| Status | In development |
| SDK | yes |
| On-board compute | NVIDIA Jetson Orin NX 16GB 157 TOPS (standard) / NVIDIA Thor 64GB 730 TOPS (Pro) |
| Sensors | Head: 1 wide-angle camera + 3 fisheye cameras, Chest RGBD camera, 2 wrist wide-angle cameras, LiDAR x2, 8 ultrasonic sensors, IMU |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Maker product page (checked 2026-11-27): 1,060-1,700 mm tall (height_mm is the minimum; the waist travels 540 mm) x 548 mm wide x 670 mm long, 160 kg, 24 active DoF excluding hands (2 neck, 7 per arm, 5 waist and lower body, 3 chassis), 3 kg payload at full extension, four-wheel steering and four-wheel drive at 1.5 m/s, 30 deg slope, two batteries totalling 1,650 Wh for about 4-5 h (4.5 h entered), 2 h charge per bay, 48 V DC, head wide-angle plus three fisheye cameras, chest RGBD, two wrist cameras, two LiDARs, eight ultrasonic sensors, four microphones and two speakers, Wi-Fi/Bluetooth/4G/5G, full SDK with EtherCAT, CAN FD and RS-485 buses. The maker's sheet gives two different arm figures - an 850 mm maximum working radius in the headline block against 650 mm working radius and 650 mm span in the arm table - and the note above keeps the headline; arm weight is likewise listed as both 6.5 kg and 8 kg. The page headline says NVIDIA Thor while the table ships Orin NX 16 GB as standard and Thor as the Pro option. Unveiled 2026-11-23 and not yet shipping; no price.

## Sources

- Official page: [simplexityrobotics.com](https://www.simplexityrobotics.com/products/ix)
- [simplexityrobotics.com](https://www.simplexityrobotics.com/)

Listed by these directories (discovery only, never used as a spec source):

- [embodied.guide](https://embodied.guide/robots/simplexity-ix/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-27). Source repository: https://github.com/htcrefactor/robot-catalog*
