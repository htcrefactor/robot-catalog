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
  "onboard_compute": null,             // true/false/null: user-accessible onboard compute
  "compute_detail": null,              // e.g. "NVIDIA Jetson Orin NX 16GB"
  "ros_support": null,                 // true/false/null
  "sensors": [],                       // short strings, e.g. "3D LiDAR", "Depth camera"
  "price_usd": null,                   // list/starting price in USD if public; else null
  "price_note": null,                  // e.g. "starting price", "from CNY 9,999"
  "official_url": null,
  "sources": [],                       // URLs actually opened that support the numbers
  "summary": ""                        // one plain sentence, what it is for
}
Rules: never guess; unknown = null. Prefer manufacturer spec pages/datasheets. Numbers as numbers.

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
