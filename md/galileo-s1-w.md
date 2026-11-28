# Galileo (Tianjin) S1-W

> Large industrial wheel-legged robot (85 kg, IP67) with 40 kg payload, >60 km range and 110 cm step capability.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=galileo-s1-w
- Category: Wheel-legged
- Locomotion: Wheel-legged
- Manufacturer: Galileo (Tianjin) (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 1,100 mm |
| Width | 450 mm |
| Height | 810 mm |
| Weight | 85 kg |
| Payload | 40 kg |
| Max speed | 6 m/s (21.6 km/h) |
| Runtime | 6 h |
| Battery | 2,880 Wh |
| IP rating | IP67 |
| Status | Commercial |
| On-board compute | yes |
| Compute | x86 or domestic low-power ARM CPU |
| Sensors | LiDAR (40 m), Depth camera, FLIR thermal camera (optional payload) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Specs from Galileo (Tianjin) official product brochure (maker PDF hosted on WRC exhibitor site); product also listed on official site galileotimes.com. max_speed is stated limit (极限) speed; runtime range 4 h (20 kg load) – 6 h, upper value used; max payload 120 kg. Re-checked 2026-11-17: maker's own product page opened (galileotimes.com, Galileo Tianjin's product site, contacts @galileotime.com). Its current parameter table for this model reads - S1-W (wheel-legged) column: 1200x550x760 mm, 128 kg, 60Ah/3540 Wh dual battery 59 V, 0-6 m/s, 30 cm steps + 110 cm platform, 2.5-4 h, 100 kg continuous walking load, 170 kg standing load, IP67. The stored numbers come from Galileo's 2025 product manual (maker PDF) and are LOWER/lighter than the current page (C1 660x320x470 mm /15 kg vs 765x410x475 mm /22 kg; E1 1000x420x600 mm /38 kg vs 1000x452x550 mm /52 kg; S1 1100x450x700 mm /60 kg vs 1200x550x650 mm /118 kg), i.e. the page appears to describe the 2026 line-up. Stored values kept so this PR does not silently rewrite specs; the current-page figures are recorded here for the owner to choose between.

## Sources

- Official page: [galileotimes.com](https://www.galileotimes.com/galileo-intelligent-bionic-quadruped-robot-s1-wseries-industrial-grade-product/)
- [worldrobotconference.com](https://www.worldrobotconference.com/profile/robot/download/2025/07/08/Galileo-%E6%99%BA%E8%83%BD%E4%BB%BF%E7%94%9F%E5%9B%9B%E8%B6%B3%E6%9C%BA%E5%99%A8%E4%BA%BA%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C_20250708115131A101.pdf)
- [galileotimes.com](https://www.galileotimes.com/news/2026wrc-galileo-releases-dual-new-products-with-full-range-mobile-technology-to-create-a-new-paradigm-of-intelligent-land-based-vehicles/)

Listed by these directories (discovery only, never used as a spec source):

- [embodied.guide](https://embodied.guide/robots/galileo-s1-w/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-28). Source repository: https://github.com/htcrefactor/robot-catalog*
