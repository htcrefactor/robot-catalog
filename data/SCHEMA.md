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
  "price_usd": null,                   // list/starting price in USD if public; else null
  "price_note": null,                  // e.g. "starting price", "from CNY 9,999"
  "official_url": null,
  "sources": [],                       // URLs actually opened that support the numbers
  "summary": ""                        // one plain sentence, what it is for
}
Rules: never guess; unknown = null. Prefer manufacturer spec pages/datasheets. Numbers as numbers.

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
