# JAKA Robotics JAKA S³

> Mobile manipulator: a differential-drive AMR base carrying a 6-axis JAKA arm for machine tending, handling and inspection.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=jaka-s3
- Category: AMR
- Locomotion: Wheeled
- Manufacturer: JAKA Robotics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 950 mm |
| Width | 620 mm |
| Height | 975 mm |
| Weight | 402.5 kg |
| Payload | 95 kg |
| Max speed | 1.5 m/s (5.4 km/h) |
| Degrees of freedom | 6 |
| Runtime | 8 h |
| Battery | 2,591 Wh |
| Status | Commercial |
| API | yes |
| Sensors | LiDAR x2 (diagonal layout, 270 deg), Vision camera 2592 x 1944, 360 deg safety edge, IMU |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Maker (checked 2026-11-27): the platform ships as S3-M3-12-L with 155 kg carrier capacity and 340.5 kg total weight, or S3-M3-12-B with 95 kg and 402.5 kg, so the numbers here record the B variant; 950 x 620 x 975 mm without the arm, arm reach 1327 mm, 12 kg arm payload including the end effector, 6-axis arm (dof) and a 1.8 m/s TCP speed. Differential two-wheel drive at up to 1.5 m/s (0.8 m/s recommended at rated load) and 0.3 m/s2, 3 deg / 5 % gradeability, 30 mm gap crossing, 10 mm obstacle clearance, 1000 mm turning diameter, 8 h or more of runtime, 51.2 V 50.6 Ah LiFePO4 single battery (2591 Wh derived) with 1.5 h charge from 15 % to 95 %. Two diagonal LiDARs cover 270 degrees, four emergency stops and a 360-degree safety edge are standard; TCP/IP, RS485 and Modbus TCP; JAKA Cobo pi programming. No price published.

## Sources

- Official page: [jaka.com](https://www.jaka.com/en/productDetails/JAKA_S%C2%B3_)

Listed by these directories (discovery only, never used as a spec source):

- [botupyourlife.com](https://botupyourlife.com/en/robots/jaka-s3-s3/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-27). Source repository: https://github.com/htcrefactor/robot-catalog*
