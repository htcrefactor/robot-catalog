# Diden Robotics Diden Spider (Spider 30)

> Magnetic-foot quadruped that climbs steel walls and ceilings inside ship blocks to carry welding and inspection tools.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=diden-robotics-diden-spider
- Category: Quadruped
- Locomotion: Legged
- Manufacturer: Diden Robotics (South Korea)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Payload | 30 kg |
| Released | 2026 |
| Status | Commercial |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

34 values from 6 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Manufacturer | DIDEN ROBOTICS Co., Ltd. (Seongdong-gu, Seoul, South Korea) |  | [robotworld.or.kr](https://robotworld.or.kr/visitors/pop_list_of_exhibitors.php?idx=1431) |
| Robot type | Quadruped work robot with electro-permanent-magnet (EPM) magnetic feet, specialized for shipyards |  | [robotworld.or.kr](https://robotworld.or.kr/visitors/pop_list_of_exhibitors.php?idx=1431) |
| Model | Diden Spider (also called Spider 30) |  | [didenrobotics.com](https://www.didenrobotics.com/en/resources-all/nvidia-gtc-2026-spider-30) |
| Unveiled | Launch date 1 June 2026; first public showing in Korea at ROBOTWORLD 2026 (4 Nov 2026) |  | [robotworld.or.kr](https://robotworld.or.kr/visitors/pop_list_of_exhibitors.php?idx=1431) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Overall length | 958 mm |  | [eweek.com](https://www.eweek.com/news/news-diden-spider-30-magnetic-robot-shipyards-south-korea-apac/) |
| Overall width | 460 mm |  | [eweek.com](https://www.eweek.com/news/news-diden-spider-30-magnetic-robot-shipyards-south-korea-apac/) |
| Overall height | 494 mm |  | [eweek.com](https://www.eweek.com/news/news-diden-spider-30-magnetic-robot-shipyards-south-korea-apac/) |
| Weight | 45 kg |  | [eweek.com](https://www.eweek.com/news/news-diden-spider-30-magnetic-robot-shipyards-south-korea-apac/) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Max payload | 30 kg | manipulator / task-module payload, including at 90° vertical orientation | [robotworld.or.kr](https://robotworld.or.kr/visitors/pop_list_of_exhibitors.php?idx=1431) |
| Max speed | 0.1 m/s | stated by eWeek ('up to'); not found on a Diden page | [eweek.com](https://www.eweek.com/news/news-diden-spider-30-magnetic-robot-shipyards-south-korea-apac/) |
| Towing capacity | 40 kg | stable gait while towing a 40 kg load | [robotworld.or.kr](https://robotworld.or.kr/visitors/pop_list_of_exhibitors.php?idx=1431) |
| Degrees of freedom | 12 | 12 actuators in four legs | [eweek.com](https://www.eweek.com/news/news-diden-spider-30-magnetic-robot-shipyards-south-korea-apac/) |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Obstacle clearance | 400 mm |  | [en.fnnews.com](https://en.fnnews.com/news/202611041829341672) |
| Max surface inclination | 90 ° | moves on vertical steel walls and ceilings | [robotworld.or.kr](https://robotworld.or.kr/visitors/pop_list_of_exhibitors.php?idx=1431) |
| Surface types | Ferrous steel structures incl. curved surfaces, vertical walls and ceilings |  | [robotworld.or.kr](https://robotworld.or.kr/visitors/pop_list_of_exhibitors.php?idx=1431) |
| Stiffener crossing | Crosses 3 consecutive longitudinal stiffeners inside hull blocks | field-validated | [robotworld.or.kr](https://robotworld.or.kr/visitors/pop_list_of_exhibitors.php?idx=1431) |
| Access-hole traversal | Autonomously passes hull-block access holes in about 1 min (36 trials, 0 failures) |  | [robotworld.or.kr](https://robotworld.or.kr/visitors/pop_list_of_exhibitors.php?idx=1431) |
| Floor-to-wall transition time | < 30 s | per Diden as reported by eWeek | [eweek.com](https://www.eweek.com/news/news-diden-spider-30-magnetic-robot-shipyards-south-korea-apac/) |
| Navigation | Autonomous navigation and path planning without prior maps; real-time state estimation |  | [didenrobotics.com](https://www.didenrobotics.com/en/resources-all/nvidia-gtc-2026-spider-30) |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| Operating temperature | -10 to 60 °C |  | [eweek.com](https://www.eweek.com/news/news-diden-spider-30-magnetic-robot-shipyards-south-korea-apac/) |
| Connector ingress protection | IP54 | power and communications connectors | [eweek.com](https://www.eweek.com/news/news-diden-spider-30-magnetic-robot-shipyards-south-korea-apac/) |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Task modules | Manipulators, welding equipment, inspection equipment |  | [didenrobotics.com](https://www.didenrobotics.com/en/products) |

### Actuation & Joints

| Spec | Value | Note | Source |
|---|---|---|---|
| Foot type | Electro-permanent magnet (EPM) magnetic feet; holds without power, pulse toggles ON/OFF |  | [didenrobotics.com](https://www.didenrobotics.com/en/resources-all/nvidia-gtc-2026-spider-30) |
| Magnetic adhesion force | 2,200 N | per 1,000 g magnet | [robotworld.or.kr](https://robotworld.or.kr/visitors/pop_list_of_exhibitors.php?idx=1431) |
| Magnetic adhesion force | 1,500 N | 'up to'; figure reported by eWeek citing Diden (conflicts with 2,200 N exhibitor listing) | [eweek.com](https://www.eweek.com/news/news-diden-spider-30-magnetic-robot-shipyards-south-korea-apac/) |
| Magnetic adhesion force | 200+ kgf | wall adhesion force (robot) | [robotworld.or.kr](https://robotworld.or.kr/visitors/pop_list_of_exhibitors.php?idx=1431) |
| Magnet ON/OFF switching time | 10 ms | exhibitor listing; '100× faster than commercial' | [robotworld.or.kr](https://robotworld.or.kr/visitors/pop_list_of_exhibitors.php?idx=1431) |
| Magnet ON/OFF switching time | 7 ms | 'as little as'; reported by eWeek | [eweek.com](https://www.eweek.com/news/news-diden-spider-30-magnetic-robot-shipyards-south-korea-apac/) |
| Magnet mass | 1,000 g | per foot magnet | [robotworld.or.kr](https://robotworld.or.kr/visitors/pop_list_of_exhibitors.php?idx=1431) |
| Peak torque density | 194 N·m/kg | in-house actuator, peak instantaneous | [robotworld.or.kr](https://robotworld.or.kr/visitors/pop_list_of_exhibitors.php?idx=1431) |
| Joint motors | 12 actuators (in-house, hollow shaft, high-ratio planetary reducer) |  | [eweek.com](https://www.eweek.com/news/news-diden-spider-30-magnetic-robot-shipyards-south-korea-apac/) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Intended use | Welding and inspection inside ship blocks; ship maintenance, high-rise and plant work |  | [robotworld.or.kr](https://robotworld.or.kr/visitors/pop_list_of_exhibitors.php?idx=1431) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Status | Supply contracts with 2 Korean shipyards and 1 European shipyard | per Hankyoreh, Nov 2026 | [hani.co.kr](https://www.hani.co.kr/arti/economy/marketing/1285758.html) |
| Status | Field deployment completed at major Korean shipyards; welds applied to vessels in production |  | [didenrobotics.com](https://www.didenrobotics.com/en/resources-all/nvidia-gtc-2026-spider-30) |

## Documents

- [ROBOTWORLD 2026 exhibitor page – DIDEN ROBOTICS (product sheet)](https://robotworld.or.kr/visitors/pop_list_of_exhibitors.php?idx=1431)
- [Diden Robotics blog – Physical AI Walks the Wall (Spider 30, Apr 2026)](https://www.didenrobotics.com/en/resources-all/nvidia-gtc-2026-spider-30)
- [Diden Robotics – Products](https://www.didenrobotics.com/en/products)
- [eWeek – Spider 30 (2026-10-01)](https://www.eweek.com/news/news-diden-spider-30-magnetic-robot-shipyards-south-korea-apac/)
- [Financial News – 2026 RoboWorld (2026-11-04)](https://en.fnnews.com/news/202611041829341672)
- [Hankyoreh – 2026 로보월드 (2026-11-04)](https://www.hani.co.kr/arti/economy/marketing/1285758.html)

## Notes

Maker sources (products page and the GTC 2026 article) state a 30 kg payload and electro-permanent magnet feet with pulse switching, and report field deployment at Korean shipyards with welds applied to production vessels. Mass, dimensions, joint count, IP rating and speed are not published on the maker's site; press reports (eWeek, Oct 2026) give 958 x 460 x 494 mm, 45 kg, 12 actuators, 0.1 m/s and IP54 connectors, and those values are cleared here rather than asserted.

## Sources

- Official page: [didenrobotics.com](https://www.didenrobotics.com/en/products)
- [didenrobotics.com](https://www.didenrobotics.com/en/resources-all/nvidia-gtc-2026-spider-30)
- [robotworld.or.kr](https://robotworld.or.kr/visitors/pop_list_of_exhibitors.php?idx=1431)
- [eweek.com](https://www.eweek.com/news/news-diden-spider-30-magnetic-robot-shipyards-south-korea-apac/)
- [en.fnnews.com](https://en.fnnews.com/news/202611041829341672)
- [didenrobotics.com](https://www.didenrobotics.com/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-20). Source repository: https://github.com/htcrefactor/robot-catalog*
