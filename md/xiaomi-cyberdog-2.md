# Xiaomi CyberDog 2

> Small open-source bionic robot dog for developers and enthusiasts, sold in mainland China.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=xiaomi-cyberdog-2
- Category: Quadruped
- Locomotion: Legged
- Manufacturer: Xiaomi (China)
- Verification: not recorded

## Core specs

| Field | Value |
|---|---|
| Length | 562 mm |
| Width | 339 mm |
| Height | 481 mm |
| Weight | 8.9 kg |
| Max speed | 1.6 m/s (5.8 km/h) |
| Degrees of freedom | 12 |
| Runtime | 1.5 h |
| Released | 2023 |
| Status | Commercial |
| Price | CNY 12,999 at China launch (about US$1,785 per New Atlas) |
| ROS | yes |
| On-board compute | yes |
| Compute | NVIDIA Jetson NX chip with dual co-processors, 8 GB RAM, 16 GB storage; Ubuntu + ROS 2 |
| Sensors | Intel RealSense depth camera, AI interaction camera, RGB camera, Fisheye camera, ToF sensor, Laser (LiDAR) sensor, 4-mic array, Touch sensor |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

110 values from 3 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Manufacturer | Xiaomi |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) |
| Model | MS2242CN | CyberDog 2 仿生四足机器人 | [mi.com](https://www.mi.com/cyberdog2/specs) · 基本信息 |
| CMIIT ID (robot) | 2023AP9860 |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 产品参数 image (img8) |
| Robot type | Small, lightweight bionic quadruped robot (仿生四足机器人) |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 三、产品简介 |
| Unveiled | 2023-08-14 | 2023 Lei Jun annual speech | [m.cls.cn](https://m.cls.cn/detail/1432577) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length (standing) | 562 mm |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 基本信息 |
| Width (standing) | 339 mm |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 基本信息 |
| Height (standing) | 481 mm |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 基本信息 |
| Lying down (L × W × H) | 603 × 339 × 300 mm |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 基本信息 |
| Height (lying down) | 300 mm |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 基本信息 |
| Weight (with battery) | 8.9 ± 0.5 kg | Xiaomi lab test data | [mi.com](https://www.mi.com/cyberdog2/specs) · 基本信息 |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Total DoF | 12 |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 基本信息 |
| Max payload | 1 kg |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 运动性能 |
| Max forward speed | 1.6 m/s | Lab-measured max forward speed | [mi.com](https://www.mi.com/cyberdog2/specs) · 运动性能 |
| Supported gaits | Slow walk, fast walk, jog, variable-frequency, quadruped bounding run, four-leg pronk, posture display (慢走丨快走丨小跑丨变频丨四足跳跑丨四腿蹦跳丨姿态展示) |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 运动性能 |
| Actions | Stand, lie down, sit, bow, head turn, hip wiggle, stretch, push-up, enhanced stand-up, shake right hand, shake left hand, ballet, moonwalk, jump in place, standing long jump, spin-jump left, spin-jump right, bow with heart, leash walk (19) |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 运动性能 更多能力 |
| Dynamic balance | yes |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 运动性能 |
| Backflip / consecutive backflip | Supported; requires ~1.5 m clear behind (backflip) or ~4 m (consecutive backflips) |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 五(一)(12), 五(四)(13) |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Unsuitable surfaces | Do not use on uneven ground, steep slopes, mud, loose material, gravel, wet/slippery floors, ice, puddles, complex grass; indoors use rubber mats/carpet |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 五(一)(3)(5) |
| Autonomy | Visual follow and navigation (do not work in low light); UWB tag follow with remote |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 五(四)(2), 七 |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery model | DH21050CXM |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 电池参数 (img10) |
| Battery type | Rechargeable lithium-ion polymer |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 电池参数 |
| Nominal voltage | 21.6 V |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 电池参数 |
| Charge limit voltage | 24.9 V |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 电池参数 |
| Rated capacity | 4,500 mAh |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 电池参数 |
| Rated energy | 97.2 Wh |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 电池参数 |
| Runtime | 90 min | Approx.; combined test of lying down, standing, static posture display and stable walking on normal ground | [mi.com](https://www.mi.com/cyberdog2/specs) · 电池参数 |
| Battery protection | Balanced charging; over-voltage, under-voltage, over-current, short-circuit and over-temperature protection |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 电池参数 |
| Battery standards | GB31241-2014; UN38.3 |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 电池参数 |
| Swappable battery | no | Built-in, non-removable; do not disassemble | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 五(三)【注意】 |
| Low battery indication | Head/tail lights red meteor effect when battery < 20 % |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 指示灯状态说明 (img16) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charging time | 90 min | Approx. | [mi.com](https://www.mi.com/cyberdog2/specs) · 电池参数 |
| Power adapter model | MDY-13-EU |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 电源适配器 |
| Adapter input | 100–240 V~ 50/60 Hz 3.0 A |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 电源适配器 |
| Adapter output | 20 V ⎓ 10.5 A max |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 电源适配器 |
| Adapter standards | GB 17625.1-2012; GB 4943.1-2011; GB/T 9254.1-2021 |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 电源适配器 |
| Charging | Official adapter + fast-charge cable into back charging port (CHARGER) while robot lies prone; auto-stops when full; do not charge > 24 h |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 四.1, 五(三)(9)(10) |

### Environment & Protection

| Spec | Value | Note | Source |
|---|---|---|---|
| Recommended charging temperature | 0 to 40 °C |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 四.1 充电说明 |
| Operating temperature | 0 to 40 °C |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 其它参数 |
| Storage temperature limits | -10 to 45 °C | Never store above 45 °C or below -10 °C | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 五(五)(8) |
| Water resistance | Not waterproof – do not immerse or wash with strong water jets |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 五(一)(6) |
| Prohibited weather | Strong wind, snow, rain, thunderstorms, fog; strong EMI or poor signal areas |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 五(一)(4)(9)(10) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Depth camera | Intel® RealSense™ D430 |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 视觉感知系统 |
| AI interaction camera | 13 MP |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 视觉感知系统 |
| RGB camera | 1 MP |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 视觉感知系统 |
| Fisheye camera FOV | 146 ° |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 视觉感知系统 |
| Laser sensor | YDLIDAR TG30 |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 视觉感知系统 |
| ToF | ToF sensors (head front and belly) |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 传感器配置 (img3, img4) |
| Ultrasonic sensor | Chest-mounted ultrasonic sensor |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 传感器配置 (img3) |
| Touch sensor | Head touch area |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 传感器 |
| Microphones | MIC |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 传感器 |
| IMU | yes |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 传感器 |
| UWB | UWB (remote tag positioning) |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 传感器 |
| Sensor count | 19 | Per Xiaomi at launch | [m.cls.cn](https://m.cls.cn/detail/1432577) |
| Sensors | Intel RealSense D430 depth camera, touch sensor, fisheye camera, TG30 laser sensor, RGB camera, ultrasonic sensor, AI interaction camera, ToF, MIC, UWB, IMU |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 传感器 |

### Compute & Software

| Spec | Value | Note | Source |
|---|---|---|---|
| CPU | 6-core NVIDIA Carmel ARM v8.2 64-bit |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 处理器和储存 |
| GPU | 384-core NVIDIA Volta with 48 Tensor Cores |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 处理器和储存 |
| Memory (RAM) | 8 GB 128-bit LPDDR4x |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 处理器和储存 |
| eMMC | 16 GB eMMC 5.1 |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 处理器和储存 |
| SD card | 32 GB Class 10 industrial grade |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 处理器和储存 |
| AI processor | 21 TOPS | Plus motion-control and voice-interaction processors | [m.cls.cn](https://m.cls.cn/detail/1432577) |
| Operating system | Ubuntu 18.04 + ROS2 |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 操作系统 |
| ROS version | ROS 2 |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 操作系统 |
| Visual programming | App visual programming; 50+ modules | Module count per launch report | [m.cls.cn](https://m.cls.cn/detail/1432577) |
| Open source | System code, structural drawings, function interfaces open; 100+ open interfaces |  | [m.cls.cn](https://m.cls.cn/detail/1432577) |
| Motor control frequency | 20 kHz |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 电机参数 |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Wi-Fi | IEEE 802.11 a/b/g/n/ac |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 无线配置 |
| Bluetooth | 5.0 |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 无线配置 |
| External interface | Type-C × 1 |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 外置接口 |
| Motor communication | CAN 2.0 |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 电机参数 |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Expansion slot | Expansion interface slot (扩展接口槽) on back |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 部件名称 (img1) |

### Actuation & Joints

| Spec | Value | Note | Source |
|---|---|---|---|
| Leg DoF | 3 |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 基本信息 |
| Joint motor | Xiaomi CyberGear micro-actuator ×12 |  | [m.cls.cn](https://m.cls.cn/detail/1432577) |
| Motor dimensions | Φ80.5 × 36.5 mm |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 电机参数 (img12) |
| Motor weight | 317 ± 3 g |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 电机参数 |
| Motor rated voltage | 24 V | Working voltage 16–28 VDC | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 电机参数 |
| Motor max current | 23 ± 10 % A |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 电机参数 |
| Motor max torque | ±12 N·m |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 电机参数 |
| Motor max speed | 296 ± 10 % rpm |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 电机参数 |
| Encoder resolution | 14 bit |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 电机参数 |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Fall recovery | yes | 倒地恢复 | [mi.com](https://www.mi.com/cyberdog2/specs) · 运动性能 |
| Fall protection | yes | 摔倒保护 | [mi.com](https://www.mi.com/cyberdog2/specs) · 运动性能 |
| Braking distance | May exceed 1 m |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 五(一)(1) |
| Clearance before power-on | 2 m |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 四.2 |
| Intended use | Companion/entertainment, performance, science education, learning and industry development |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 三 |
| User age | 18+ only; keep away from children |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 一、法律声明 |
| Prohibited uses | Public roads, crowded places, cargo transport, carrying/launching dangerous objects, surveillance, sensitive facilities |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 五(四)(六) |
| Hazardous substances disclosure | SJ/T 11364 table; lead exceeds GB/T 26572 limit in circuit boards, metal parts, battery |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · img14 |

### Controls & Operation

| Spec | Value | Note | Source |
|---|---|---|---|
| Controllers | Android app (Mi account), Bluetooth remote (joystick + UWB tag), voice |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 四.3, 七 |
| App platform | Android only |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 四.3 注 |
| UWB tag follow | Robot follows the Bluetooth remote's UWB tag; started via app or voice |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 七 |
| Remote model | MS2241CNUB | CMIIT ID 2022DP17442 | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 遥控器参数 (img13) |
| Remote dimensions | 71.5 × 28.5 × 21.3 mm |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 遥控器参数 |
| Remote weight | 21.6 g |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 遥控器参数 |
| Remote battery | Li-ion polymer 227 mAh, 3.87 V, 0.87 Wh; charge limit 4.45 V |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 遥控器参数 |
| Remote runtime | 24 h remote mode; 7 h follow mode |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 遥控器参数 |
| Remote charge time | 1.5 h |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 遥控器参数 |
| Remote button functions | Hold 2 s on/off; single press battery; double press switch gait; double press + hold 3 s pairing; triple press tag follow on/off |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · img22 |
| Power button hold time | 3 s | 10 s forces shutdown | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 四.2 |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Speaker | yes |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 部件名称 (img1) |
| Display | Mini LED display on head |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 部件名称 (img2) |
| Head & tail lights | Blue meteor: normal; red meteor: battery < 20 %; orange slow blink: QR network pairing; orange sequential: follow on; blue sequential: charging; red fast blink: shutting down |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 指示灯状态说明 (img16) |
| Voice interaction | XiaoAI (小爱同学) voice technology; wake word 铁蛋铁蛋 |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 语音系统 |
| Voice commands | Back/forward + steps, turn in place, follow me, high-five, sit, shake hands, jump, switch hand, wag tail, ballet, moonwalk, shake head, nod, New-Year bow |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 语音指令词 (img17) |

### Transport & Storage

| Spec | Value | Note | Source |
|---|---|---|---|
| Long-term storage (> 3 months) | 20–25 °C, 0–60 % RH, charge ≤ 80 % (30–50 % best); recharge if < 20 %; cycle every ~3 months |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 五(五)(11)(12) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Package contents | Robot ×1; Bluetooth remote (joystick + UWB tag) ×1; power adapter + fast-charge cable ×1; hex screwdriver ×1; stickers ×2; manual ×1; legal notice ×1 |  | [mi.com](https://www.mi.com/cyberdog2/specs) · 包装清单 |
| Launch price | 12,999 CNY | Purchase requires qualification review | [m.cls.cn](https://m.cls.cn/detail/1432577) |
| Warranty | 7-day return/exchange, 8–15-day exchange/repair, free repair thereafter within warranty; foot pads are consumables |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 八 |
| Sales region | Mainland China only (excl. HK, Macau, Taiwan) |  | [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html) · 八(五)2 |
| CyberGear motor sold separately | 499 CNY |  | [m.cls.cn](https://m.cls.cn/detail/1432577) |

## Documents

- [Xiaomi CyberDog 2 参数页 (mi.com specs)](https://www.mi.com/cyberdog2/specs)
- [CyberDog 2 产品说明书 (official user manual, incl. spec-table images img8–img16)](https://agreement.cyberdog.xiaomi.com/guide.html)
- [科创板日报: 小米新一代机器狗“铁蛋二号”问世 (2023-08-15)](https://m.cls.cn/detail/1432577)

## Sources

- Official page: [mi.com](https://www.mi.com/cyberdog2)
- [newatlas.com](https://newatlas.com/robotics/xiaomi-cyberdog-2/)
- [agreement.cyberdog.xiaomi.com](https://agreement.cyberdog.xiaomi.com/guide.html)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-16). Source repository: https://github.com/htcrefactor/robot-catalog*
