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
  "compute_detail": null,              // e.g. "NVIDIA Jetson Orin NX 16GB" (the maker's wording, kept as-is)
  "compute_soc": null,                 // chip/SoC as the maker states it, e.g. "NVIDIA Jetson AGX Orin 32GB"
  "compute_tops": null,                // AI performance in TOPS as the maker states it (number); null when not stated
  "compute_tops_precision": null,      // precision the maker states with that figure (e.g. "INT8", "FP4"); omitted when none
  "compute_memory_gb": null,           // memory of that onboard computer, GB
  "compute_source": null,              // URL of the maker page/datasheet that states these compute values
  "ros_support": null,                 // true/false/null
  "sensors": [],                       // short strings, e.g. "3D LiDAR", "Depth camera"
  "price_usd": null,                   // list/starting price in USD if public; else null
  "price_note": null,                  // e.g. "starting price", "from CNY 9,999"
  "official_url": null,
  "sources": [],                       // URLs actually opened that support the numbers
  "summary": ""                        // one plain sentence, what it is for
}
Rules: never guess; unknown = null. Prefer manufacturer spec pages/datasheets. Numbers as numbers.

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
