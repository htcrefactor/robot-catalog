# SIASUN Robot & Automation DUCO

> DUCO (多可), SIASUN's embodied-AI brand, sells its humanoid line as the BR-MR73A wheeled humanoid and the BR-DR73 half-body robot, both built on the same dual 7-axis force-controlled arm platform.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=siasun-duco
- Category: Humanoid
- Locomotion: Wheeled
- Manufacturer: SIASUN Robot & Automation (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Status | Commercial |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

The record is brand-level ('DUCO'), and DUCO is the embodied-intelligence brand of SIASUN subsidiary Zhongke Xinsong (中科新松), so no single model's specs were written into the record. Maker product page for the 类人形 series: BR-MR73A wheeled humanoid and BR-DR73 half-body (fixed pedestal) share dual 7-DOF force-controlled arms with 630 mm working radius, +/-0.05 mm repeatability and 800 mm/s TCP speed; the table gives one variant 17 DOF (head 2, arms 7 x 2, waist 1) and 24 DOF (head 2, arms 7 x 2, waist 4, chassis 4) for the other, 5 kg per arm (8 kg with both), 800-1,450 mm or 800-2,000 mm working height, Orin AGX 200/275 TOPS, head depth camera plus front/rear torso cameras and microphone array, 1.2 m/s with laser SLAM and +/-5 mm docking, ROS 2 and Python SDK, one variant running continuously with no battery and the other giving about 6 h. CONFLICT: the maker's blog gives the BR-MR73A a 3 kg arm payload and 1.2 m/s while the product table gives 5 kg per arm / 8 kg dual, and the table's variant columns do not line up with the model names, so the per-model mapping is uncertain. The humanoid.guide figures (~30-35 DOF, ~150-160 cm, ~90-110 kg, 85,000 USD) are unverified and were not used.

## Sources

- Official page: [ducorobots.cn](https://www.ducorobots.cn/prodetail/48.html)
- [blog.ducorobots.cn](https://blog.ducorobots.cn/products/jushen-zhineng-jiqiren-zhongke-xinsong-qudong-zhineng-zhizao-de-hexin-zhineng-ti)

Listed by these directories (discovery only, never used as a spec source):

- [humanoid.guide](https://humanoid.guide/product/duco/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-17). Source repository: https://github.com/htcrefactor/robot-catalog*
