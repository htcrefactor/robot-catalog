# Hikrobot Q7-1000E (MR-Q7-1000CE-E1(HI)(CE))

> Latent (under-ride) lifting robot that carries racks up to 1,000 kg on a 2D-code floor grid (1.8 m/s at rated load).

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=hikrobot-q7-1000e
- Category: AGV
- Locomotion: Wheeled
- Manufacturer: Hikrobot (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 1,150 mm |
| Width | 820 mm |
| Height | 254 mm |
| Weight | 178 kg |
| Payload | 1,000 kg |
| Max speed | 2 m/s (7.2 km/h) |
| Runtime | 8 h |
| Status | Commercial |
| Sensors | Front laser obstacle avoidance (20 m), Side ultrasonic sensors, Pneumatic bumper strip, Downward vision for 2D-code navigation |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

47 values from 4 documents, checked against maker sources on 2026-11-04.

### Identity

| Spec | Value | Note | Source |
|---|---|---|---|
| Robot type | Latent mobile robot (LMR), lifts and carries racks/shelves |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Model numbers (CE) | MR-Q7-1000LE-EI(CE) (laser SLAM); MR-Q7-1000CE-EI(CE) (2D code); MR-Q7-1000VE-EI(CE) (visual SLAM) |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Model numbers (wiki main models) | MR-Q7-1000CE-E4(MF) (material code 307302442); MR-Q7-1000LE-E2(MC) (307306012) |  | [wiki-lmr.rms.hikrobotics.com](https://wiki-lmr.rms.hikrobotics.com/AMR/LMR/Q7/Q7-1000E/Quick-Start/Q7-1000E-parameters) |
| Material code (MR-Q7-1000CE-E1(HI)(CE)) | 307301735 |  | [pdf.directindustry.com](https://pdf.directindustry.com/pdf/hikrobot/latent-mobile-robot-mr-q7-1000e-hl-ce/242099-1031638.html) |

### Dimensions & Mass

| Spec | Value | Note | Source |
|---|---|---|---|
| Length | 1,150 mm |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Width | 820 mm |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Height | 254 mm | CE datasheet; 252 mm per Hikrobot wiki (E4/E2 models); 256 mm in 2023 catalog | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Rotation diameter | 1,200 mm |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Chassis above the ground | 25 mm |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Weight | 178 kg | CE datasheet; 167 kg per Hikrobot wiki (E4/E2 models); 185 kg in 2023 catalog | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |

### Mobility & Performance

| Spec | Value | Note | Source |
|---|---|---|---|
| Rated load | 1,000 kg |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Rated running speed (empty) | 2 m/s |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Rated running speed (rated load) | 1.8 m/s |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Rated acceleration (empty) | 1 m/s² |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Rated acceleration (rated load) | 0.6 m/s² | CE datasheet; 0.5 m/s² per Hikrobot wiki | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Rotation speed (empty) | 200 °/s |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Rotation speed (rated load) | 60 °/s | CE datasheet; 100°/s per Hikrobot wiki | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Location accuracy | ±10 mm | 2D code model; ±20 mm for laser-SLAM E2 model per wiki; ideal conditions | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Location angle accuracy | ±1 ° | ±2° for laser-SLAM E2 model per wiki | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Drive | Dual-wheel differential drive (forward, backward, rotation) |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |

### Terrain & Navigation Limits

| Spec | Value | Note | Source |
|---|---|---|---|
| Navigation mode | Laser SLAM / 2D barcode / visual SLAM (ground texture); inertial + 2D code | depends on model variant | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Gradeability | 4 ° | CE datasheet; 3° per Hikrobot wiki | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |

### Power & Battery

| Spec | Value | Note | Source |
|---|---|---|---|
| Battery type | LiFePO4 |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Rated voltage | 48 V |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Charge cycles | 1,500 cycles | full charge/discharge | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Run time | 8 h | rated condition | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |

### Charging & Docking

| Spec | Value | Note | Source |
|---|---|---|---|
| Charge time | ≤ 1.5 h | full charge after full discharge | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Charging mode | Automatic wired charging via charge station; rear charging; TE-type connector |  | [wiki-lmr.rms.hikrobotics.com](https://wiki-lmr.rms.hikrobotics.com/AMR/LMR/Q7/Q7-1000E/Quick-Start/Q7-1000E-parameters) |
| Charging connector height above ground | 130 mm |  | [wiki-lmr.rms.hikrobotics.com](https://wiki-lmr.rms.hikrobotics.com/AMR/LMR/Q7/Q7-1000E/Quick-Start/Q7-1000E-parameters) |
| Charging station model | MR-RA-CH-48/30B-CI(CE) |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Auto-charge / smart power management | Multi-level electrical threshold, auto-charge, self-return to work after charging |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |

### Sensors & Perception

| Spec | Value | Note | Source |
|---|---|---|---|
| Front laser obstacle avoidance | Scanning angle 260°; installation height 182 mm |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Front laser max. detection range | 20 m |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Side ultrasonic obstacle avoidance | One each on left and right; height 188 mm; opening angle H 80° / V 34°; range 0.2–1 m | CE version | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Bumper strip detection | Pneumatic bumper strips, front and rear |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |

### Connectivity & Interfaces

| Spec | Value | Note | Source |
|---|---|---|---|
| Wireless communication | Wi-Fi with seamless roaming |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |

### Payload & Mounting

| Spec | Value | Note | Source |
|---|---|---|---|
| Lifting tray dimension | 1030 × 770 mm |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Lifting height | 60 mm |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Lifting speed | 20 mm/s |  | [wiki-lmr.rms.hikrobotics.com](https://wiki-lmr.rms.hikrobotics.com/AMR/LMR/Q7/Q7-1000E/Quick-Start/Q7-1000E-parameters) |
| Lifting type | Electric |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |

### Safety & Compliance

| Spec | Value | Note | Source |
|---|---|---|---|
| Emergency stop button | Front and rear |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Certification | CE |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Safety standard | ISO 3691-4:2020 |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Typical applications | Automobile, consumer electronics, manufacturing, logistics, food, medicine |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |

### Audio, Lights & HMI

| Spec | Value | Note | Source |
|---|---|---|---|
| Human-machine interaction | Touch screen; sound and indicator lights |  | [dev-images.bluestarinc-emea.com](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf) |
| Sound and light alarm | yes |  | [wiki-lmr.rms.hikrobotics.com](https://wiki-lmr.rms.hikrobotics.com/AMR/LMR/Q7/Q7-1000E/Quick-Start/Q7-1000E-parameters) |

### Commercial

| Spec | Value | Note | Source |
|---|---|---|---|
| Accessories | Charge station (MR-RA-CH-48/30B-C7(S)); slope M-70; external debugging cable 50 cm |  | [pdf.directindustry.com](https://pdf.directindustry.com/pdf/hikrobot/latent-mobile-robot-mr-q7-1000e-hl-ce/242099-1031638.html) |

## Documents

- [MR-Q7-1000LE-EI(CE) Latent Mobile Robot datasheet (Hikrobot, distributor-hosted)](https://dev-images.bluestarinc-emea.com/pdf/4753-datasheet.pdf)
- [Q7-1000E main model parameters (Hikrobot LMR wiki)](https://wiki-lmr.rms.hikrobotics.com/AMR/LMR/Q7/Q7-1000E/Quick-Start/Q7-1000E-parameters)
- [Latent Mobile Robot MR-Q7-1000E(HI)(CE) catalog (Hikrobot on DirectIndustry)](https://pdf.directindustry.com/pdf/hikrobot/latent-mobile-robot-mr-q7-1000e-hl-ce/242099-1031638.html)
- [Hikrobot Mobile Robot Product Catalog R.101.EN.23Q1.1](https://www.mbintell.com/assets/doc/Hikrobot%20Mobile%20Robot%20Product%20Catalog_R.101.EN.23Q1.1.pdf)

## Notes

Checked 2026-11-19: record values come from the maker datasheet and Hikrobot LMR wiki parameter page already listed in sources; no conflicts found.

## Sources

- Official page: [hikrobotics.com](https://www.hikrobotics.com/en/mobilerobot/LMR/)
- [pdf.directindustry.com](https://pdf.directindustry.com/pdf/hikrobot/latent-mobile-robot-mr-q7-1000e-hl-ce/242099-1031638.html)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-22). Source repository: https://github.com/htcrefactor/robot-catalog*
