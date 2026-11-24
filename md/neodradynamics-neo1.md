# NeodraDynamics Neo1

> 4-metre hydraulic-electric hybrid 'super humanoid' for heavy lifting in nuclear, deep-sea, rescue and heavy-manufacturing work.

- Catalog page: https://htcrefactor.github.io/robot-catalog/robot.html?id=neodradynamics-neo1
- Category: Humanoid
- Locomotion: Legged
- Manufacturer: NeodraDynamics (China)
- Verification: official — checked against a maker source

## Core specs

| Field | Value |
|---|---|
| Height | 4,000 mm |
| Weight | 1,200 kg |
| Payload | 600 kg |
| Degrees of freedom | 41 |
| Released | 2026 |

Fields the maker does not publish are left out here — the catalog never fills a value by guess. Prices are list or starting prices where the maker states one.

## Full spec sheet

The full spec sheet for this robot is still being researched; the catalog core fields above are every value recorded so far.

## Notes

Maker page (NeodraDynamics / Qingzhuo Power, Beijing) and the maker's PR of 14 Oct 2026: 4 m, ~1.2 t, 41 full-body active DOF, 7DOF arms x2, 15DOF hands x2, 300 kg single-arm / 600 kg dual-arm payload, -50~300°C, EtherCAT/CANopen. Conflict: the maker's own PR (PR Newswire, 14 Oct 2026) states a 500 kg dual-arm payload; product page value (600 kg) used. Shown at WRC Aug 2026 and CIIF Oct 2026 with JD Industrial; no price or delivery date -> status left out. Scope review (#16, 2026-11-17): kept as an in-scope Humanoid. Mobility is unproven rather than excluded: the maker calls it a full-body humanoid and press breakdowns of the 41 joints count 12 in the legs and feet, but no maker video or text shows it walking or balancing, it was exhibited tethered and script-controlled, and the company told press that walking on legs is not the priority for industrial use and that the plan is to fit the arms on a wheeled base. Locomotion is left at the existing 'Legged' value but is not maker-stated: it follows from the maker calling it a humanoid and from press breakdowns of the joints, so it should be treated as unconfirmed until a maker source or footage shows it moving. If only demonstrated-mobile robots are to count as in scope, Neo1 (with Meta Max) is the pair to reconsider.

## Sources

- Official page: [neodradynamics.com](https://neodradynamics.com/neo1_product_en.html)
- [prnewswire.com](https://www.prnewswire.com/news-releases/neodradynamics-showcases-4-meter--1-2-ton-neo1-heavy-duty-hydraulic-robot-with-jd-industrial-at-ciif-hydraulicelectric-hybrid-solves-realworld-4d-industrial-challenges-302908332.html)

Listed by these directories (discovery only, never used as a spec source):

- [data.robo2u.com](https://data.robo2u.com/robots/neodradynamics-neo1)
- [embodied.guide](https://embodied.guide/robots/neodradynamics-neo1/)
- [humanoid.guide](https://humanoid.guide/product/neo1/)

---

*Robot Catalog — generated from data/robots.json (last merged 2026-11-24). Source repository: https://github.com/htcrefactor/robot-catalog*
