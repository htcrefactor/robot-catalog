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

Safety fields: fill only from a maker source (site, datasheet, manual) or a certification registry, never from a
competitor or store. Keep the maker's own wording; do not add a standard the maker does not name. When the maker
states a standard with exclusions or calls it a design principle rather than a certificate, say so in
`safety_note` — the arrays alone would overstate it. When the maker says it is not certified, that is a value too:
leave the arrays empty and record the statement in `safety_note`.

`payload class` is not a stored field: the site derives a payload band from `payload_kg` for the filter and the
table column, so no derived value is written into the data.
