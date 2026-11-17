# Fourier GR-1

> Fourier's first mass-produced full-size bipedal humanoid, a 1.65 m, 55 kg research and service platform with FSA actuators.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=fourier-gr-1
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: Fourier (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 320 mm |
| Width | 515 mm |
| Height | 1,650 mm |
| Weight | 55 kg |
| Payload | 3 kg |
| Max speed | 1.39 m/s (5.0 km/h) |
| Degrees of freedom | 44 |
| Battery | 460 Wh |
| Released | 2023 |
| Status | Commercial |
| SDK | yes |
| On-board compute | yes |
| Compute | Intel i7-13700H (20 threads) |
| Sensors | Intel RealSense depth camera, IMU, Ring microphone |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Skeleton official_url (support.fftai.com/en/docs/.../GR-1_Introduction/) now 404s. Values from Fourier's own GR-1 brochure PDF (Feb 2024, fftai branding; hosted on edit.site CDN): standing size 1650 x 515 x 320 mm, ~55 kg (Pro ~60 kg), 5 km/h (=1.39 m/s), 3 kg single-hand payload, 44 actuators (GR-1, dexterous hands; GR-1L 34), 460 Wh battery, i7-13700H compute, RealSense depth camera, IMU, ring mic, 230 N·m peak torque. DoF conflict: brochure text says 'up to 54 DoF' (with 11-DoF hands) vs 44 elsewhere - used 44 (spec-table actuator count). Unveiled 2023; since succeeded by GR-2/GR-3. SDK (Python/C++) offered.

## Sources

- Official page: [fftai.com](https://fftai.com/products-gr1.html)
- [static-gcs.edit.site](https://static-gcs.edit.site/users-files/75329df683dc786c44cd1ae27c78c5f8/fourier-gr-1-humanoid-robot-introduction-3.pdf?dl=1)

Listed by these directories (discovery only, never used as a spec source):

- [botupyourlife.com](https://botupyourlife.com/en/robots/fourier-gr-1/)
- [data.robo2u.com](https://data.robo2u.com/robots/fourier-intelligence-gr-1)
- [humanoidversus.com](https://humanoidversus.com/robots/fourier-gr-1)
- [humanoid.guide](https://humanoid.guide/product/gr-1/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-16). Source repository: https://github.com/htcrefactor/robot-catalog*
