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
