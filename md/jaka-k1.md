# JAKA Robotics K1

> JAKA's K1 seven-axis dual-arm platform for dual-arm assembly and embodied-AI data collection.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=jaka-k1
- Category: Humanoid
- Manufacturer: JAKA Robotics
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Payload | 5 kg |
| Max speed | 1 m/s (3.6 km/h) |
| Status | Commercial |
| SDK | yes |
| SDK name | JAKA SDK / direct teaching |
| On-board compute | JAKA RoboHub controller (Intel Core i3/i5/i7 12th-13th gen, optional NVIDIA RTX 3050) |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Maker hardware manual (JAKA K1, V01): a 7-axis dual-arm collaborative platform - per arm 5 kg payload, 14 kg mass, 976 mm working radius, repeatability +/-0.05 mm, TCP max 1 m/s, 48 V DC supply, RoboHub controller with Intel Core i12/i13 CPU, EtherCAT. Dual-arm synchronised control (SyncPath, SyncForce, SyncCalib, SelfAware). DoF field left empty because the maker states 7 axes per arm, not a whole-body count; no height, weight or runtime for a complete robot is published. SCOPE: K1 has no mobile base - it is a bench-mounted dual-arm platform, which AGENTS.md section 3 excludes as arms/cobots; kept here unchanged (no deletion) and flagged for an owner scope decision. The wheeled K1W and legged K1L are separate models.

## Sources

- Official page: [jaka.com](https://www.jaka.com/)
- [jaka.com](https://www.jaka.com/profile/upload/2026/02/06/20260206111400A037.pdf)

Listed by these directories (discovery only, never used as a spec source):

- [humanoid.guide](https://humanoid.guide/product/jaka-k1/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-27). Source repository: https://github.com/htcrefactor/robot-catalog*
