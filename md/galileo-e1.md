# Galileo (Tianjin) E1

> Medium industrial quadruped (38 kg, IP67) with 20 kg payload, 4.95 m/s top speed and LiDAR navigation for security inspection.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=galileo-e1
- Category: Quadruped
- Locomotion: Legged
- Manufacturer: Galileo (Tianjin) (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Length | 1,000 mm |
| Width | 420 mm |
| Height | 600 mm |
| Weight | 38 kg |
| Payload | 20 kg |
| Max speed | 4.95 m/s (17.8 km/h) |
| Runtime | 4 h |
| Battery | 1,200 Wh |
| IP rating | IP67 |
| Status | Commercial |
| On-board compute | yes |
| Compute | x86 or domestic low-power ARM CPU |
| Sensors | LiDAR (40 m), Depth camera, FLIR thermal camera (optional payload) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Specs from Galileo (Tianjin) official product brochure (maker PDF hosted on WRC exhibitor site); product also listed on official site galileotimes.com. max_speed is stated limit (极限) speed; runtime range 2–4 h, upper value used; max payload 85 kg. Re-checked 2026-11-17: maker's own product page opened (galileotimes.com, Galileo Tianjin's product site, contacts @galileotime.com). Its current parameter table for this model reads - E1 (legged) column: 1000x452x550 mm, 52 kg, 30Ah/1440 Wh 48 V, 0-3.5 m/s, climb 80 cm platform, 2.5-4.5 h, 30 kg continuous walking load, 100 kg standing load, >16 km, IP67. The stored numbers come from Galileo's 2025 product manual (maker PDF) and are LOWER/lighter than the current page (C1 660x320x470 mm /15 kg vs 765x410x475 mm /22 kg; E1 1000x420x600 mm /38 kg vs 1000x452x550 mm /52 kg; S1 1100x450x700 mm /60 kg vs 1200x550x650 mm /118 kg), i.e. the page appears to describe the 2026 line-up. Stored values kept so this PR does not silently rewrite specs; the current-page figures are recorded here for the owner to choose between.

## Sources

- Official page: [galileotimes.com](https://www.galileotimes.com/galileo-intelligent-bionic-quadruped-robot-e1-w-series-industrial-grade-product/)
- [worldrobotconference.com](https://www.worldrobotconference.com/profile/robot/download/2025/07/08/Galileo-%E6%99%BA%E8%83%BD%E4%BB%BF%E7%94%9F%E5%9B%9B%E8%B6%B3%E6%9C%BA%E5%99%A8%E4%BA%BA%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C_20250708115131A101.pdf)
- [galileotimes.com](https://www.galileotimes.com/news/2026wrc-galileo-releases-dual-new-products-with-full-range-mobile-technology-to-create-a-new-paradigm-of-intelligent-land-based-vehicles/)

Listed by these directories (discovery only, never used as a spec source):

- [embodied.guide](https://embodied.guide/robots/galileo-e1/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-19). Source repository: https://github.com/htcrefactor/robot-catalog*
