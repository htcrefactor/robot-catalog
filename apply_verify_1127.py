#!/usr/bin/env python3
"""Verification batch 2026-11-27: fill 12 unchecked records from maker sources."""
import json, os, glob

ORDER = ["id", "name", "manufacturer", "country", "category", "locomotion", "release_year",
         "status", "length_mm", "width_mm", "height_mm", "weight_kg", "payload_kg",
         "max_speed_mps", "min_speed_mps", "wheel_diameter_mm", "wheel_count", "dof",
         "runtime_h", "battery_wh", "ip_rating", "api_support", "sdk_available", "sdk_name",
         "onboard_compute", "compute_detail", "ros_support", "sensors", "price_usd", "price_note",
         "official_url", "sources", "summary", "image_url", "image_source", "videos", "seen_on",
         "verification", "note", "price_observations"]

U = {
    "ubtech-cadebot": {
        "status": "Commercial",
        "length_mm": 550, "width_mm": 485, "height_mm": 1265,
        "weight_kg": 55, "payload_kg": 40,
        "max_speed_mps": 0.8, "min_speed_mps": 0.0,
        "runtime_h": 8, "battery_wh": 512,
        "sensors": ["Front and rear LiDAR", "RGB-D depth cameras", "Ultrasonic sensors",
                    "Infrared tray sensors", "Front camera", "Top camera"],
        "official_url": "https://www.ubtrobot.com/en/commercial/products/cadebot",
        "sources": ["https://www.ubtrobot.com/en/commercial/products/cadebot",
                    "http://www.commercial.ubtrobot.com/zh_cn/products/ubtech-cadebot-l100-open-food-delivery-robot-parameters.html",
                    "https://www.troysupply.com/static/docs/downloads/cadebot_User-Manual.pdf"],
        "summary": "Open-tray restaurant delivery robot with a 21.5-inch advertising display, laser-and-vision fused SLAM and a 6-microphone array.",
        "verification": "official",
        "note": "Maker's own pages (checked 2026-11-27) give the service modes, the 6-mic array with 5 m pickup, front-to-back LiDAR with RGB-D and ultrasonic sensing, infrared tray detection, 21.5-inch ad screen, and up to 8 h of continuous operation with automatic recharging. Dimensions, 55 kg weight, 40 kg total load and 0-0.8 m/s travel are stated in UBTECH's CADEBOT user manual for CADEBOT L100 (model XCAD101); 512 Wh is derived from that manual's 25.6 V 20 Ah pack. 4 trays at 10 kg each. The maker publishes no price.",
    },
    "orionstar-luckibot-pro": {
        "status": "Commercial",
        "length_mm": 558, "width_mm": 525, "height_mm": 1375,
        "weight_kg": 59, "payload_kg": 60,
        "max_speed_mps": 1.2, "min_speed_mps": 0.5,
        "runtime_h": 12, "battery_wh": 621,
        "sensors": ["LiDAR x1", "Depth vision camera x3", "Fisheye camera x2",
                    "Infrared camera x2", "Odometer", "IMU x1"],
        "official_url": "https://en.orionstar.com/lucki-pro.html",
        "sources": ["https://en.orionstar.com/lucki-pro.html",
                    "https://en.orionstar.com/pro_compare.html",
                    "https://www.orionstar.com/lucki-pro.html"],
        "summary": "Marketing delivery robot with a 14-inch screen, visual SLAM with 3D obstacle sensing, and 3-4 adjustable trays.",
        "verification": "official",
        "note": "Maker (checked 2026-11-27): 558 x 525 x 1375 mm, 59 kg, 3 or 4 trays of 500 x 420 mm, 15 kg per tray and 60 kg in total, 0.5-1.2 m/s adjustable, 12 h typical cruising, 4.5 h charge when switched off, 14-inch 1080p screen, Android 9.0 RobotOS on a Qualcomm 8-core chip with 8 GB RAM and 64 GB storage, centimetre-level positioning, 6-mic array, 4G and Wi-Fi 2.4/5 GHz. 621 Wh is derived from the maker's comparison page figure of 24.3 Ah at 25.55 V. The Chinese page states 16 h of operation for the same model, so the English page's 12 h is recorded. No price published.",
    },
    "orionstar-luckibot": {
        "status": "Commercial",
        "length_mm": 530, "width_mm": 500, "height_mm": 1320,
        "weight_kg": 39, "payload_kg": 40,
        "max_speed_mps": 1.2, "min_speed_mps": 0.5,
        "runtime_h": 10, "battery_wh": 382,
        "sensors": ["LiDAR x1", "Depth vision camera x1", "Infrared camera x1", "IMU x1"],
        "official_url": "https://en.orionstar.com/lucki.html",
        "sources": ["https://en.orionstar.com/lucki.html",
                    "https://en.orionstar.com/pro_compare.html"],
        "summary": "Restaurant delivery robot with 3-4 adjustable trays, dual SLAM navigation and a 10.1-inch touch screen.",
        "verification": "official",
        "note": "Maker (checked 2026-11-27): 530 x 500 x 1320 mm, 39 kg, upper trays 500 x 430 mm and bottom tray 480 x 400 mm with 210/210/280 mm clearances, 10 kg per tray and 40 kg in total, 0.5-1.2 m/s adjustable, 10 h typical cruising, 4.5 h charge when off, 10.1-inch 1200x1920 touch screen, Android 9.0 RobotOS, centimetre-level positioning, 6-mic array, 4G and Wi-Fi. 382 Wh is derived from the comparison page's 15.15 Ah at 25.2 V. This is the first-generation LuckiBot that LuckiBot Pro supersedes. No price published.",
    },
    "orionstar-greetingbot-nova": {
        "status": "Commercial",
        "length_mm": 558, "width_mm": 525, "height_mm": 1350,
        "weight_kg": 56,
        "max_speed_mps": 1.2, "min_speed_mps": 0.5,
        "runtime_h": 12,
        "sensors": ["3D LiDAR (170 deg vertical / 240 deg horizontal)",
                    "Depth camera", "13 MP head camera"],
        "official_url": "https://en.orionstar.com/nova.html",
        "sources": ["https://en.orionstar.com/nova.html",
                    "https://www.orionstar.kr/greetingbotnova"],
        "summary": "Large-language-model reception robot that greets, guides and explains in 30+ languages, with marker-free V-SLAM on a 14-inch screen.",
        "verification": "official",
        "note": "Maker (checked 2026-11-27): 558 x 525 x 1350 mm, 56 kg, 14-inch 1080p screen, 13 MP head camera, 3D LiDAR with a 170-degree field of view and 240-degree horizontal coverage, marker-free V-SLAM, auto recharge below 10 % and 12-14 h of cruising; runtime_h records the lower end of the maker's range and 4.5 h is the dock charging time. The Korean subsidiary lists the public-procurement model as OS-R-SG04 and the same 56 kg / 1,350 mm figures. No payload, battery capacity or price published.",
    },
    "orionstar-greetingbot-ad": {
        "status": "Commercial",
        "runtime_h": 8,
        "sensors": ["LiDAR with multi-sensor fusion navigation", "6-microphone 360-degree array"],
        "official_url": "https://en.orionstar.com/greetingbot-ad.html",
        "sources": ["https://en.orionstar.com/greetingbot-ad.html"],
        "summary": "Retail greeting robot that pairs a roaming 21.5-inch advertising display with a 14-inch touch screen to greet, promote and guide shoppers.",
        "verification": "official",
        "note": "Maker (checked 2026-11-27) publishes a 21.5-inch ad display plus a 14-inch touch screen, a 6-mic 360-degree array, 46+ languages, LiDAR with multi-sensor fusion at centimetre-level positioning, a 60 cm minimum aisle, an 8 A lidar-guided auto-docking fast charge, Wi-Fi 6 and 4G, and a 20 Ah NMC battery for 8-10 h; runtime_h records the lower end of that range. Overall size, weight, travel speed and battery voltage are not published, so those fields stay empty and no Wh figure is derived. No price published.",
    },
    "anseboo-fd08": {
        "status": "Commercial",
        "length_mm": 450, "width_mm": 470, "height_mm": 1430,
        "weight_kg": 60, "payload_kg": 10,
        "max_speed_mps": 1.0,
        "runtime_h": 10, "battery_wh": 672,
        "official_url": "https://www.anseboo.com/en/products/commercial-advertising-robot-indoor-display-video-ad-robot-explain-with27-inch-hd-screen-for-supermarket-shoppingmal",
        "sources": ["https://www.anseboo.com/en/products/commercial-advertising-robot-indoor-display-video-ad-robot-explain-with27-inch-hd-screen-for-supermarket-shoppingmal",
                    "https://www.anseboo.com/en/collections/delivery-robots"],
        "summary": "Indoor mobile advertising robot with a 27-inch HD screen and three 500 x 400 mm trays rated at 10 kg each.",
        "verification": "official",
        "note": "Maker (checked 2026-11-27): 450 x 470 x 1430 mm, 60 kg, Android 10 or later, Wi-Fi or 4G, a 22.4 V 30 Ah battery giving 10-15 h (672 Wh derived; runtime_h records the lower end of the range), three 500 x 400 mm trays at 10 kg each (payload_kg is the per-tray rating), up to 1 m/s, and delivery, advertising, explanation and dancing functions with a customizable voice. The maker sells it as a mobile advertising display that also carries trays; it publishes no navigation sensor, SDK or price.",
    },
    "jaka-s3": {
        "status": "Commercial",
        "length_mm": 950, "width_mm": 620, "height_mm": 975,
        "weight_kg": 402.5, "payload_kg": 95,
        "max_speed_mps": 1.5,
        "dof": 6,
        "runtime_h": 8, "battery_wh": 2591,
        "api_support": True,
        "sensors": ["LiDAR x2 (diagonal layout, 270 deg)", "Vision camera 2592 x 1944",
                    "360 deg safety edge", "IMU"],
        "official_url": "https://www.jaka.com/en/productDetails/JAKA_S%C2%B3_",
        "sources": ["https://www.jaka.com/en/productDetails/JAKA_S%C2%B3_"],
        "summary": "Mobile manipulator: a differential-drive AMR base carrying a 6-axis JAKA arm for machine tending, handling and inspection.",
        "verification": "official",
        "note": "Maker (checked 2026-11-27): the platform ships as S3-M3-12-L with 155 kg carrier capacity and 340.5 kg total weight, or S3-M3-12-B with 95 kg and 402.5 kg, so the numbers here record the B variant; 950 x 620 x 975 mm without the arm, arm reach 1327 mm, 12 kg arm payload including the end effector, 6-axis arm (dof) and a 1.8 m/s TCP speed. Differential two-wheel drive at up to 1.5 m/s (0.8 m/s recommended at rated load) and 0.3 m/s2, 3 deg / 5 % gradeability, 30 mm gap crossing, 10 mm obstacle clearance, 1000 mm turning diameter, 8 h or more of runtime, 51.2 V 50.6 Ah LiFePO4 single battery (2591 Wh derived) with 1.5 h charge from 15 % to 95 %. Two diagonal LiDARs cover 270 degrees, four emergency stops and a 360-degree safety edge are standard; TCP/IP, RS485 and Modbus TCP; JAKA Cobo pi programming. No price published.",
    },
    "jaka-lumi": {
        "status": "Commercial",
        "length_mm": 510, "width_mm": 510, "height_mm": 1460,
        "weight_kg": 95.6, "payload_kg": 2,
        "dof": 12, "ip_rating": "IP20",
        "api_support": True,
        "sensors": ["LiDAR on the chassis", "3D vision camera", "Ultrasonic obstacle avoidance"],
        "official_url": "https://www.jaka.com/en/productDetails/JAKA_Lumi",
        "sources": ["https://www.jaka.com/en/productDetails/JAKA_Lumi",
                    "https://www.jaka.com/en/newsDetail/632"],
        "summary": "Wheeled embodied-AI training platform: a differential AMR base with a lifting, rotating waist, a rotating neck and a 6-axis 2 kg arm.",
        "verification": "official",
        "note": "Maker (checked 2026-11-27): 510 x 510 x 1460-1860 mm, where height_mm records the retracted figure and the waist lifts 0-400 mm; 95.6 kg, 12 DoF in total (a 6-axis arm plus +/-160 deg waist and +/-180 deg / -5 to 35 deg neck joints), 2 kg arm payload, 800 W at 48 V DC, IP20 control cabinet, TCP/IP, Modbus TCP/RTU, PROFINET and EtherNet/IP, 7 configurable I/O ports, MuJoCo and NVIDIA Isaac Sim support, and open SDK interfaces over TCP/IP and USB (api_support). Perception is a chassis LiDAR, a 3D vision camera and ultrasonic obstacle avoidance. Maker states the platform is sold in China now with international sales pending certification. Travel speed and battery capacity are not published; no price.",
    },
    "foxtech-xtron-roban": {
        "status": "Commercial",
        "dof": 22,
        "api_support": True,
        "ros_support": True,
        "sensors": ["High-resolution cameras with a structured-light depth sensor",
                    "Microphone array", "Tactile sensors"],
        "official_url": "https://www.foxtechrobotics.com/xtron-roban-bipedal-humanoid-robot-education-research.html",
        "sources": ["https://www.foxtechrobotics.com/xtron-roban-bipedal-humanoid-robot-education-research.html",
                    "https://www.foxtechrobotics.com/robot.html"],
        "summary": "Educational bipedal humanoid with 22 degrees of freedom, vision and voice interaction, and a ROS/Linux open platform for teaching and research.",
        "verification": "official",
        "note": "Maker (checked 2026-11-27): 22 DoF for curved walking, slopes and stair climbing; high-resolution cameras with a structured-light depth sensor, microphone array and tactile sensors; multi-language speech; ROS and Linux with an API for secondary development; a ready curriculum covering control, programming, vision and motion planning. The maker's product page publishes no height, weight, payload, speed or runtime, so those fields stay empty. The same manufacturer lists the XTRON T170A and ATOM P1 Pro under its bionic range. No maker price.",
    },
    "yahboom-rosmaster-a1": {
        "status": "Commercial",
        "api_support": True,
        "sdk_available": True,
        "sdk_name": "ROS 2 Humble (Python)",
        "ros_support": True,
        "sensors": ["YDLIDAR T-mini Plus LiDAR",
                    "3D depth camera (Superior kit) or 2 MP pan-tilt camera (Standard kit)",
                    "AI voice module with microphone and speaker"],
        "official_url": "https://www.yahboom.store/products/rosmaster-a1",
        "sources": ["https://www.yahboom.store/products/rosmaster-a1",
                    "https://www.yahboom.net/study/ROSMASTER-A1"],
        "summary": "Ackermann-steering ROS 2 education rover with LiDAR, an optional depth camera and a large-model voice module on a Raspberry Pi 5 or Jetson board.",
        "verification": "official",
        "note": "Maker's store and tutorial site (checked 2026-11-27): ROS 2 Humble, an Ackermann chassis with metal 520 encoder motors, a T-mini Plus LiDAR, a 3D depth camera in the Superior kit or a 2 MP pan-tilt camera in the Standard kit, an AI voice module, a Yahboom ROS expansion board, and a choice of Raspberry Pi 5 8 GB, Jetson Nano 4 GB or Jetson Orin Nano 8 GB as the main board, with Gazebo and RViz support. The maker publishes its dimension, weight and battery table only as images, so those fields stay empty; it states no travel speed. The dated price is the maker's own store listing for the Standard kit without a main board, which the store shows next to the same kit priced with each board.",
        "price_observations": [{
            "date": "2026-11-27", "amount": 339.9, "currency": "USD", "kind": "from",
            "source": "https://www.yahboom.store/products/rosmaster-a1",
            "note": "Standard kit without a main board; the store prices the same kit higher with a Raspberry Pi 5 8 GB, Jetson Nano 4 GB or Jetson Orin Nano board, and the Superior and Ultimate kits separately",
        }],
    },
    "kompai-rf1": {
        "verification": "unconfirmed",
        "note": "Checked 2026-11-27: the maker's site no longer serves a product page - kompai.com resets the connection and www.kompai.com returns HTTP 500 - so no maker specification could be read and nothing was filled. The record keeps only what the listing that named it says. A maker page or datasheet is needed before any field is set.",
    },
    "rainbow-robotics-mixx": {
        "verification": "unconfirmed",
        "sources": ["https://rainbow-robotics.com/",
                    "https://www.hannovermesse.de/apollo/hannover_messe_2022/obs/Binary/A1163539/%5BRainbow%20Robotics%5D%20Company%20profile_EN_low.pdf"],
        "note": "Checked 2026-11-27: Rainbow Robotics' current line-up (RBC cobots, RBY mobile humanoid, RBM mobile robots, RBQ quadruped, ASTRO cells) no longer lists MIXX and the maker publishes no dimensions, payload, speed or runtime for it. The maker's own company profile presents MIXX as an F&B beverage-making/automation platform launched alongside the RB series - a fixed beverage kiosk rather than an indoor delivery robot - so this record's identity and category need an owner decision (the maker's later AI serving robot is a separate, unnamed product). Nothing was filled.",
    },
}


def main():
    seen = set()
    for path in sorted(glob.glob("data/parts/*.json")):
        data = json.load(open(path, encoding="utf-8"))
        changed = False
        out = []
        for r in data:
            upd = U.get(r["id"])
            if not upd:
                out.append(r)
                continue
            seen.add(r["id"])
            r.update(upd)
            ordered = {k: r[k] for k in ORDER if k in r}
            for k, v in r.items():
                if k not in ordered:
                    ordered[k] = v
            out.append(ordered)
            changed = True
        if changed:
            text = open(path, encoding="utf-8").read()
            trailing = "\n" if text.endswith("\n") else ""
            indent = 2 if text.split("\n")[1].startswith("  {") else 1
            with open(path, "w", encoding="utf-8") as f:
                f.write(json.dumps(out, ensure_ascii=False, indent=indent) + trailing)
            print("updated", path)
    missing = set(U) - seen
    if missing:
        raise SystemExit(f"ids not found: {sorted(missing)}")


if __name__ == "__main__":
    main()
