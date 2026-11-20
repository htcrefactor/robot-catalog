# Robot record schema (one JSON object per robot; file = JSON array)
{
  "id": "unitree-go2-pro",            // lowercase slug manufacturer-model
  "name": "Go2 Pro",
  "manufacturer": "Unitree Robotics",
  "country": "China",                  // manufacturer HQ country
  "category": "Quadruped",             // one of: AMR, AGV, Humanoid, Quadruped, Wheel-legged, Indoor delivery, Outdoor delivery, Mobile platform
  "locomotion": "Legged",              // one of: Wheeled, Tracked, Legged, Wheel-legged
  "release_year": 2023,
  "status": "Commercial",              // Commercial, Pre-order, Pilot, Research, Discontinued
  "length_mm": null, "width_mm": null, "height_mm": null,
  "weight_kg": null,
  "payload_kg": null,                  // rated payload
  "max_speed_mps": null,               // m/s (convert km/h ÷ 3.6)
  "min_speed_mps": null,               // only if spec states a minimum / creep speed
  "wheel_diameter_mm": null,           // drive wheel diameter (inch × 25.4); null for legged
  "wheel_count": null,
  "dof": null,                         // total actuated DoF (legged/humanoid)
  "runtime_h": null,                   // typical runtime per charge, hours
  "battery_wh": null,
  "ip_rating": null,                   // e.g. "IP54" exactly as stated; null if not stated
  "safety_standards": [],              // standards the maker states the robot is designed/certified to, in the maker's wording: "ISO 3691-4", "EN ISO 13849-1", "ANSI/ITSDF B56.5"
  "certifications": [],               // marks/certificates the maker states: "CE", "UL 3100", "FCC Part 15 Subpart B", "KC", "KIRIA outdoor mobile robot operation safety certification"
  "safety_pl": null,                  // stated performance level / safety integrity, e.g. "PL d", "SIL 2"; null if not stated
  "safety_note": null,                // qualifier on the two lists: exclusions ("ISO 3691-4 except Clause 4.4…"), scope ("for the IoT devices"), an explicit absence of certification, or a conflict between two maker documents
  "safety_source": null,              // maker URL that states these values; must also be listed in `sources`
  "api_support": null,                 // true/false/null: documented programmatic API (REST/gRPC/ROS/etc.) for customers
  "sdk_available": null,               // true/false/null: official SDK published/offered
  "sdk_name": null,
  "sdk": {                             // structured SDK facts (null when no official SDK is published)
    "languages": ["C++", "Python"],    // languages the maker's SDK is published in
    "open_source": true,               // true/false/null: SDK source published under an open-source licence
    "license": "BSD-3-Clause",         // SPDX id, or the licence's own name for a non-OSI licence
    "url": "https://github.com/…"      // maker's SDK repository or download page
  },
  "onboard_compute": null,             // true/false/null: user-accessible onboard compute
  "compute_detail": null,              // e.g. "NVIDIA Jetson Orin NX 16GB"
  "compute_soc": null,                 // chip/SoC as the maker states it, e.g. "NVIDIA Jetson AGX Orin 32GB"
  "compute_tops": null,                // AI performance in TOPS as the maker states it (number); null when not stated
  "compute_tops_precision": null,      // precision the maker states with that figure (e.g. "INT8", "FP4"); omitted when none
  "compute_memory_gb": null,           // memory of that onboard computer, GB
  "compute_source": null,              // URL of the maker page/datasheet that states these compute values
  "ros_support": null,                 // true/false/null: ROS (any distribution) support from the maker
  "ros2_support": null,                // true/false/null: official ROS 2 packages from the maker
  "ros2_url": null,                    // maker's ROS 2 packages or documentation
  "sim_models": {                      // official simulation models; omit the keys a robot has none of
    "urdf":   {"url": "https://github.com/…/Lite3.urdf", "license": "BSD-3-Clause"},
    "mjcf":   {"url": "…", "license": "…"},   // MuJoCo XML model
    "usd":    {"url": "…", "license": "…"},   // USD asset (Isaac Sim, Omniverse)
    "isaac":  {"url": "…", "license": "…"},   // official Isaac Sim / Isaac Lab integration
    "mujoco": {"url": "…", "license": "…"},   // official MuJoCo stack when no standalone MJCF file is linked
    "gazebo": {"url": "…", "license": "…"}    // official Gazebo / Ignition packages
  },
  "open_source_repos": [               // repositories the maker publishes, with licences
    {"name": "unitree_sdk2", "url": "https://github.com/unitreerobotics/unitree_sdk2", "license": "BSD-3-Clause"}
  ],
  "sensors": [],                       // short strings, e.g. "3D LiDAR", "Depth camera"
  "price_observations": [],           // dated prices from the maker or its own store (see below)
  "price_usd": null,                  // legacy single price; null on a record that has price_observations
  "price_note": null,                  // free-text price note; only kept where the legacy price is still the only one
  "official_url": null,
  "sources": [],                       // URLs actually opened that support the numbers
  "kr_distributors": [],               // Korean sales channels: [{name, kind, url}], kind = "direct" (maker's own Korean sales), "distributor" (official Korean distributor), "reseller"; url = the page that shows the channel
  "kr_note": null,                     // one short Korean-market note (sales model, availability, Korean naming)
  "name_ko": null,                     // official Korean product name from the maker's Korean page; null when the maker has none
  "manufacturer_ko": null,             // Korean name of the maker, as the maker writes it
  "summary": ""                        // one plain sentence, what it is for
}
Rules: never guess; unknown = null. Prefer manufacturer spec pages/datasheets. Numbers as numbers.

## Dated price observations (`price_observations`)
A price is a dated observation, not a standing fact: maker prices change, and a number without the
day it was checked cannot be compared with another. Each entry is

```json
{"date": "2026-11-17", "amount": 2800, "currency": "USD", "kind": "list",
 "source": "https://shop.unitree.com/products/unitree-go2",
 "note": "Go2 Pro without controller; US$3,050 with controller"}
```

- `date` — the day the price was checked on that page, `YYYY-MM-DD`. Never a date the page itself does not state.
- `amount` — the number as the page states it, in `currency`. No conversion is stored.
- `currency` — ISO 4217 code. It must have a rate in `data/fx.json` so the site can show KRW.
- `kind` — one of `list` (the price of the model or variant), `from` (a "starting at" price), `rental`
  (a hire or subscription rate), `edu` (an education-edition price).
- `source` — the maker page or the maker's own store page that states the price; it is always also in
  the record's `sources`. Never a competitor, reseller or aggregator.
- `note` — optional, omitted when empty: which variant the figure is for, what it excludes, or what
  the rental rate covers.

A variant worth its own price point gets its own observation on the same date (for example
`faraday-future-fx-aegis` carries the Aegis, Classic Pro, Classic Edu and Classic Ultra prices), so
nothing is collapsed into a range and no average is invented.

**KRW is never stored.** `data/fx.json` (`scripts/build_fx.py`) holds KRW cross rates with the ECB
reference date, and the page converts at display time, printing the rate and its date next to the
figure. That keeps the rate auditable and lets an old observation be read at today's rate.

## Legacy prices
`price_usd` / `price_note` are the single-price form this schema had before dated observations.
Records migrated to `price_observations` carry `price_usd: null` and `price_note: null`, and their
statement is kept in the observation's `note`. The field stays because a record whose price cannot
be re-established from a maker page on a known date (typically the HumanoidStore-sourced humanoids)
would otherwise lose its price: those records keep the number they have and the site shows it as a
recorded, undated price without converting it. A record must not carry both a dated observation and
the legacy figure — `scripts/validate.py` fails on that.

Developer-readiness fields (`sdk`, `ros2_support`/`ros2_url`, `sim_models`, `open_source_repos`):
- Only the maker's own repository or documentation counts. A community port, a distributor mirror or a
  third-party converter is never listed; leave the field null instead.
- `sdk_available`, `sdk_name` and `ros_support` stay the headline yes/no; `sdk` adds languages, licence
  and link. When a field is filled, its URL goes into that record's `sources`.
- `license` is the licence as the repository states it (SPDX id where one exists, otherwise its name,
  e.g. "Boston Dynamics SDK License"). `open_source` is true only for an OSI/FSF-style open licence;
  source-available SDKs such as Spot's are false.
- `sim_models` keys: `urdf`, `mjcf` (MuJoCo XML), `usd`, `isaac`, `mujoco`, `gazebo`. Add only the ones
  the maker actually publishes, each with the link and the licence of that model. No scoring or ranking.

Safety fields: fill only from a maker source (site, datasheet, manual) or a certification registry, never from a
competitor or store. Keep the maker's own wording; do not add a standard the maker does not name. When the maker
states a standard with exclusions or calls it a design principle rather than a certificate, say so in
`safety_note` — the arrays alone would overstate it. When the maker says it is not certified, that is a value too:
leave the arrays empty and record the statement in `safety_note`.

`payload class` is not a stored field: the site derives a payload band from `payload_kg` for the filter and the
table column, so no derived value is written into the data.

Korean-market fields: `name_ko`, `manufacturer_ko`, `kr_distributors` and `kr_note` come from the maker's own Korean page or an official Korean distributor's page, listed in that record's `sources`. Leave `name_ko` null when the maker publishes no Korean product name (a model number stays as it is). `kr_distributors` is a list and may be empty; when a record has an entry, `validate.py` checks name, http(s) url and kind.

## Coverage links (`seen_on`)
`seen_on` lists the pages of other catalogues, datasets or databases on which the record was found.
It is evidence that the model exists and where a competitor or an open dataset lists it — never a
source for a value in the record.

- One entry per site, that site's page for this exact robot (a per-robot page, not the site's front
  page or a list page). Add it when a sweep of that source matches the record; keep it while the
  source still lists the robot, and never delete it as a way of resolving a disagreement.
- A value seen only on such a page never enters the record. `sources` still has to hold the maker
  page behind a number, and a field the maker does not state stays null. When the other catalogue
  states a different number, the maker value stays and the other one is recorded in `notes` (see
  "Conflicts" in `AGENTS.md`).
- Third-party coverage is attributed on `data.html` and in `llms.txt` (see `README.md`, "Open data").

## Market availability and named deployments (proposal — awaiting owner review, issue #74)

**Status: proposed, not approved.** No record carries `availability` or `deployments` yet, and
`scripts/validate.py` fails any record that has either key, so the proposal cannot be filled in by
accident. The owner reviews this section first; the data lands afterwards, in its own PR.

These two fields say where a robot can be bought and who runs it. Every fact in them has to stand on
a maker or customer statement rather than on an aggregator's summary, because an availability line or
a customer name is a claim about a company, not a spec the maker publishes once.

### `availability`
```json
"availability": {
  "EU": {"status": "purchasable", "as_of": "2026-11-20", "source": "https://maker.example/eu"},
  "US": {"status": "preorder", "as_of": "2026-11-20", "source": "https://shop.maker.example/robot"},
  "CN": {"status": "not_available", "as_of": "2026-11-20", "source": "https://maker.example/"}
}
```
- Markets are exactly `EU`, `US`, `CN`. A market that was not checked is left out of the object; an
  unchecked market is never written as `not_available`.
- `status` — one of:
  - `purchasable` — orderable now through the maker or the maker's own store or dealer.
  - `preorder` — order book open, delivery later than the order.
  - `deployed_b2b` — supplied to business customers without a public order channel.
  - `prototype` — the maker shows or trials it but does not offer it for sale.
  - `discontinued` — the maker has stopped offering it in that market.
  - `not_available` — checked, and the maker offers no channel in that market.
- `as_of` is the day the page behind `source` was checked, `YYYY-MM-DD`, the same convention as a
  dated price observation. Never a date the page itself does not support.
- `source` is the maker page, the maker's own store or an official dealer page that states the
  status, and it is always also in the record's `sources`. For `not_available` it is the maker page
  or store that was checked and shows no channel.
- Availability and price are separate: availability says whether a market can be bought in, and the
  figure for that market goes in a dated `price_observations` entry with its own currency and date.

### `deployments`
```json
"deployments": [
  {"customer": "Hyundai Motor Group",
   "site": "Robotics Metaplant Application Center, Georgia, USA",
   "status": "pilot", "date": "2026-01",
   "source": "https://maker.example/news/…"}
]
```
- `customer` — the organisation as it names itself. A deployment needs a named customer; "several
  plants" or an unnamed "leading automaker" is not an entry.
- `site` — optional: the plant, campus, city or country the source names.
- `status` — one of `pilot` (trial or test), `deployed` (in productive use), `announced` (agreed,
  not yet running), `exhibit` (museum, showroom or event appearance).
- `date` — optional, `YYYY-MM`: when the deployment started or was announced as far as the source
  states it. A year alone, or a date the source does not give, stays out.
- `source` — the maker's own announcement, or the customer's own announcement or statement. Trade
  press, a competitor's dataset or an analyst note is not a source of record for a customer name;
  what such a page says can be kept in `notes` as an unconfirmed report with its date.
- A deployment is a dated fact with a named party. A framework agreement, an order of intent or a
  promised volume is not a deployment and belongs in `notes`.
- A count of deployments in another dataset ("deployments: 2") is not data for us: each entry has
  to trace to its own announcement.

### Market prices
A price stated for a market by another dataset is an observation, not a standing fact. When one is
used it goes into `price_observations` under the rules above — the date it was checked, the amount
and currency as stated, a `kind`, and a maker page or the maker's own store in `source`. A figure
only an aggregator states is not written; it can be kept in `notes` as an unconfirmed third-party
figure with the day it was seen. One price model stays in the catalog: there is no second,
market-by-market price field.

### UI, when the data lands
`robot.html` shows one availability badge per market and the deployments as a short list; every
string goes in `assets/i18n.js` in both EN and KO like the rest of the site. Nothing is scored or
ranked.

## Structured compute (`compute_*`)
The five `compute_*` fields are the filterable form of `compute_detail` (Issue #28). `compute_detail`
stays the maker's full sentence; the structured fields hold only what that sentence — or the robot's
`data/specs/<id>.json` Compute & Software rows from the same maker source — states outright.
- `compute_soc` keeps the maker's own chip wording, trimmed to the chip(s): `"NVIDIA Jetson Orin NX
  16GB"`, `"Intel Core i7-13700H"`, `"Rockchip RK3588 + NVIDIA Jetson Xavier NX"`. The chip filter
  groups these wordings into chip families in `assets/compute.js`; the grouping is UI-side, never stored.
- `compute_tops` is a **TOPS** figure only. Figures the maker states in TFLOPS (e.g. "2070 FP4 TFLOPS"
  for Jetson Thor) are a different metric and stay in `compute_detail` and the spec rows; they are not
  converted or copied into `compute_tops`.
- `compute_tops_precision` exists so a stated precision is not lost. As of 2026-11-17 no record has one:
  no maker states a precision for the TOPS figure it publishes, and the three FP4 figures in the catalog
  are TFLOPS. Omitted rather than written as null.
- `compute_memory_gb`: memory of the onboard computer named in `compute_soc`. Where the maker gives a
  range or per-computer figures, the first stated value is kept and `compute_detail` carries the rest.
- `compute_source` is the single maker URL that states these values and is always also in `sources`.
  It is null where the values come from a record's existing maker-sourced `compute_detail` but no single
  page could be re-confirmed; the record's `sources` then still apply. Never a competitor or aggregator URL.
- Machines whose maker names no chip (e.g. "8-core high-performance CPU") keep these fields null and stay
  findable through `compute_detail`.
Records with no structured compute value do not carry the value fields; readers treat a missing key as null.

## Change history (`data/history/<id>.json`)

`scripts/merge.py` diffs every record against the previous `data/robots.json` and appends what
changed to one file per robot. Never write these by hand; they are the record of the catalog, not
part of it. `scripts/build_feed.py` turns them into `feed.xml` (Atom).

```
{
  "id": "mir-mir250",
  "name": "MiR250",
  "manufacturer": "Mobile Industrial Robots (MiR)",
  "updated": "2026-11-17",                       // date of the newest event
  "events": [                                    // oldest first, newest last, capped at 100
    {"date": "2026-11-17", "type": "updated",
     "source": "https://mobile-industrial-robots.com/products/robots/mir250",
     "changes": [{"field": "payload_kg", "from": 250, "to": 260}]},
    {"date": "2026-11-19", "type": "added", "source": "...", "changes": []},
    {"date": "2026-11-20", "type": "removed", "source": null, "changes": []}
  ]
}
```

- `type` is `added` (record first appears), `updated` (at least one field differs from the last
  generated `robots.json`) or `removed` (id disappeared from `data/parts/`; the file stays).
- `changes[].field` is a record field name, `from`/`to` are the raw values (`null` = not stated).
- `source` is the record's `official_url`, else its first `sources` entry: the page behind the change.
- A second merge on the same day folds into that day's `updated` event instead of adding a new one,
  so a day of work reads as one entry.
