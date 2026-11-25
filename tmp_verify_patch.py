import json, glob, os

TODAY = "2026-11-25"

INDENT = {"data/parts/platform.json": 1, "data/parts/quadruped.json": 1, "data/parts/wheel-legged.json": 1}

def patch(path, rid, fn):
    recs = json.load(open(path))
    for r in recs:
        if r["id"] == rid:
            fn(r)
            json.dump(recs, open(path, "w"), ensure_ascii=False, indent=INDENT.get(path, 2))
            open(path, "a").write("\n")
            print("patched", rid)
            return
    raise SystemExit("missing " + rid)

# ---------------- 1. iRobot Create 3 ----------------
def f(r):
    r.update({
        "release_year": 2022, "status": "Commercial",
        "payload_kg": 9, "max_speed_mps": 0.46, "wheel_count": 2,
        "battery_wh": 26, "api_support": True,
        "sdk_available": True, "sdk_name": "iRobot Education Python 3 SDK",
        "sdk": {"languages": ["Python"], "open_source": None, "license": None,
                "url": "https://iroboteducation.github.io/create3_docs/"},
        "ros_support": True, "ros2_support": True,
        "ros2_url": "https://iroboteducation.github.io/create3_docs/",
        "sensors": ["IMU", "Downward optical flow odometry sensor", "Wheel encoders",
                    "4 IR cliff sensors", "7 pairs of IR proximity sensors (bumper zoned)",
                    "6-LED RGB ring", "Speaker"],
        "official_url": "https://iroboteducation.github.io/create3_docs/",
        "sources": ["https://iroboteducation.github.io/create3_docs/hw/mechanical/",
                    "https://iroboteducation.github.io/create3_docs/hw/electrical/",
                    "https://iroboteducation.github.io/create3_docs/hw/overview/",
                    "https://iroboteducation.github.io/create3_docs/api/safety/",
                    "https://media.irobot.com/2022-04-05-In-Celebration-of-National-Robotics-Week,-iRobot-Launches-the-Create-R-3-Educational-Robot"],
        "summary": "iRobot's Create 3 educational mobile robot: a Roomba i3-based differential drive platform with ROS 2 and a Python SDK, 9 kg payload and a 26 Wh pack, built for teaching mobile robotics.",
        "verification": "official",
        "price_observations": [{"date": "2022-04-05", "amount": 299, "currency": "USD", "kind": "list",
                                "source": "https://media.irobot.com/2022-04-05-In-Celebration-of-National-Robotics-Week,-iRobot-Launches-the-Create-R-3-Educational-Robot",
                                "note": "Launch price for the US and Canada (CAD 399); the release is the only maker page opened that states a price"}],
        "note": "Values from iRobot's own Create 3 documentation and 2022 launch release (checked 2026-11-25): maximum recommended payload 9 kg over the centre of gravity, true top speed 0.46 m/s with the safety override fully disabled (the robot limits itself to 0.306 m/s while cliff safety is active), 26 Wh 4S lithium-ion pack (nominal 14.4 V) shared with Roomba e/i series, differential drive with two wheels plus a front caster, sensors as listed, ROS 2 and the iRobot Education Python 3 SDK both stated by the maker. Weight and body dimensions are not given as text in the maker's documentation and are left empty. Price is the 2022 launch figure; no current maker price page was opened."
    })

# ---------------- 2. Petoi Quaddle ----------------
def f2(r):
    r.update({
        "status": "Pre-order", "dof": 4, "ros_support": True,
        "sensors": ["Gyroscope", "PIR sensor", "Gesture, light and IR distance sensors (Scout)",
                    "Optional AI vision module"],
        "official_url": "https://www.petoi.com/pages/quaddle-educational-robot-kit",
        "sources": ["https://www.petoi.com/pages/quaddle-educational-robot-kit",
                    "https://guide.petoi.com/product/quaddle-under-construction"],
        "price_observations": [
            {"date": TODAY, "amount": 179, "currency": "USD", "kind": "list",
             "source": "https://www.petoi.com/pages/quaddle-educational-robot-kit",
             "note": "Quaddle Builder Plus MSRP; late-pledge price US$154"},
            {"date": TODAY, "amount": 219, "currency": "USD", "kind": "list",
             "source": "https://www.petoi.com/pages/quaddle-educational-robot-kit",
             "note": "Quaddle Buddy MSRP (adds open-domain AI conversation); late-pledge price US$189"},
            {"date": TODAY, "amount": 269, "currency": "USD", "kind": "list",
             "source": "https://www.petoi.com/pages/quaddle-educational-robot-kit",
             "note": "Quaddle Scout MSRP (adds gesture, light and IR distance sensors); late-pledge price US$229"}],
        "summary": "Petoi's 4-servo desk quadruped kit: an open-source, omnidirectional walker assembled without soldering and programmed with blocks, MicroPython, Python, C++ or ROS, sold as Builder Plus, Buddy and Scout.",
        "verification": "official",
        "note": "Maker pages checked 2026-11-25: four feedback servos, one motor per leg driving shoulder and knee, backward-compatible OpenCat firmware (Petoi says it will open-source the Quaddle code before delivery), two ESP32-S3 boards (motion, and AI on Buddy/Scout) with a Raspberry Pi Zero socket, gyroscope and PIR on every model, gesture/light/IR distance sensors and an optional AI vision module on Scout, blocks/MicroPython/Python/C++/ROS programming. Dimensions, weight, battery capacity and speed are not published on the maker's pages and are left empty. Status Pre-order: the Kickstarter campaign is funded and the maker sells late pledges at US$154/189/229 against the MSRPs listed here."
    })

# ---------------- 3. Yahboom DOGZILLA S2 ----------------
def f3(r):
    r.update({
        "dof": 12, "ros_support": True, "ros2_support": True,
        "ros2_url": "https://github.com/YahboomTechnology/DOGZILLA",
        "sdk_available": True, "sdk_name": "Yahboom DOGZILLA ROS 2 / Python repository",
        "official_url": "https://github.com/YahboomTechnology/DOGZILLA",
        "open_source_repos": [{"name": "YahboomTechnology/DOGZILLA",
                              "url": "https://github.com/YahboomTechnology/DOGZILLA"}],
        "sensors": ["HD camera", "MS200 LiDAR (S2 only)", "Voice interaction module (S2 only)",
                    "IMU", "Servo angle feedback"],
        "sources": ["https://github.com/YahboomTechnology/DOGZILLA",
                    "https://www.yahboom.store/blogs/news/build-robotics-project-with-raspberrypi-robotdog"],
        "summary": "Yahboom's 12-DoF desktop robot dog for Raspberry Pi 5: an aluminium-bodied quadruped with ROS 2 Humble and Python support, adding a LiDAR and a voice module on the S2 configuration.",
        "verification": "official",
        "note": "Maker repository and Yahboom's own store checked 2026-11-25: 12 DoF driven by 12 programmable metal bus servos (4.5 kg.cm), aluminium alloy frame, Raspberry Pi 5 as controller on raspios-bookworm + Docker + ROS 2 Humble, Python programming, IMU and servo-angle feedback, RVIZ and Gazebo simulation; the HD camera, MS200 LiDAR and voice module are listed for the S2 version only. Dimensions, weight, battery and runtime are not stated on the maker's current pages — a reseller table quotes 972 g, 246 x 145 x 195 mm and a 7.4 V 2500 mAh pack, which is not a maker figure and is not used here. battery capacity and runtime left empty."
    })

# ---------------- 4. XGO-Rider2 ----------------
def f4(r):
    r.update({
        "length_mm": 135, "width_mm": 118, "height_mm": 116, "weight_kg": 0.56,
        "wheel_count": 2, "wheel_diameter_mm": 48, "dof": 4,
        "runtime_h": 2.0, "battery_wh": 10.36,
        "onboard_compute": True, "compute_detail": "Raspberry Pi CM5 (2 GB) + ESP32 co-processor",
        "compute_soc": "Raspberry Pi CM5",
        "ros_support": True,
        "sdk_available": True, "sdk_name": "Open ESP32 motion-controller SDK",
        "sensors": ["5 MP OV5647 camera", "Dual MEMS microphone array", "8 ohm 2 W speaker",
                    "IMU", "2.0-inch IPS display (320 x 240)"],
        "official_url": "https://www.xgorobot.com/en/rider.html",
        "sources": ["https://www.xgorobot.com/en/rider.html",
                    "https://wiki.xgorobot.com/kb/the-xgo-series-robot/cmpgp22gn000bfk659hf250en",
                    "https://shop.xgorobot.com/products/xgo-rider-world-s-first-desktop-wheel-legged-robot-with-ai"],
        "summary": "Luwu Dynamics' desktop wheel-legged robot: two FOC hub wheels plus two leg servos give it omnidirectional, self-balancing motion and an adjustable 116-158 mm stance, run by a Raspberry Pi CM5 with an ESP32 motion controller.",
        "verification": "official",
        "note": "Maker pages checked 2026-11-25: 135 x 118 x 116-158 mm (height adjustable, 116 mm taken as the height value), 560 g, two FOC brushless hub motors (48 mm, D 48 mm x H 20 mm) plus two 4.5 kg.cm magnetic-encoder serial-bus leg servos, 1400 mAh 2S 18500 pack (10.36 Wh computed as 7.4 V x 1.4 Ah), Raspberry Pi CM5 2 GB with ESP32 co-processor, 5 MP OV5647 camera, dual MEMS microphones and a 2 W speaker, USB-C charging, Python and ROS development, open ESP32 motion firmware under Apache 2.0. Runtime is stated as about 2 h in the maker's wiki and about 1 h on the product page, so the wiki figure is used and both are recorded here; top speed and payload are not published."
    })

# ---------------- 5. Robotnik RB-WATCHER ----------------
def f5(r):
    r.update({
        "status": "Commercial",
        "length_mm": 731, "width_mm": 614, "height_mm": 904, "weight_kg": 73,
        "payload_kg": 50, "max_speed_mps": 2.5, "wheel_count": 4,
        "runtime_h": 5.0, "battery_wh": 720, "ip_rating": "IP54",
        "ros_support": True,
        "sensors": ["3D LiDAR", "RGBD camera", "Bi-spectral pan-tilt-zoom camera (thermal + 30x optical zoom)",
                    "Microphone", "Speakers", "GPS (RTK)", "IMU"],
        "official_url": "https://robotnik.eu/products/mobile-robots/rb-watcher",
        "sources": ["https://robotnik.eu/products/mobile-robots/rb-watcher",
                    "https://robotnik.eu/wp-content/uploads/2024/07/Robotnik_Datasheet_RB-WATCHER_2024_EN.pdf"],
        "summary": "Robotnik's RB-WATCHER is an indoor/outdoor inspection and security AMR: a 4-wheel skid or mecanum platform carrying a thermal pan-tilt-zoom camera, 3D LiDAR and a microphone for autonomous patrolling, thermal inspection and anomaly alerts.",
        "verification": "official",
        "note": "Values from Robotnik's 2024 RB-WATCHER datasheet and product page (checked 2026-11-25): 731 x 614 x 904 mm, 73 kg, 50 kg payload, up to 2.5 m/s, IP54, up to 5 h of continuous operation, 48 V 15 Ah LiFePO4 pack (720 Wh computed as V x Ah), four 500 W traction motors, ROS architecture, 3D SLAM and RTK GPS localisation. An earlier (2023) brochure gives 790 x 614 x 856 mm and 62 kg; the newer datasheet values are used and the difference is recorded here."
    })

# ---------------- 6. PAL Robotics StockBot ----------------
def f6(r):
    r.update({
        "status": "Commercial",
        "length_mm": 460, "width_mm": 460, "height_mm": 1830,
        "runtime_h": 10.0,
        "sensors": ["3D cameras", "Laser 2D", "2 RAIN RFID readers", "8 RAIN RFID antennas"],
        "official_url": "https://pal-robotics.com/robot/stockbot/",
        "sources": ["https://pal-robotics.com/robot/stockbot/",
                    "https://pal-robotics.com/wp-content/uploads/2024/12/StockBot-datasheet-EN.pdf"],
        "summary": "PAL Robotics' StockBot is a fully autonomous retail inventory robot: 8 RAIN RFID antennas and 3D cameras scan shelves and locate items to about 0.5 m, reporting stock accuracy of about 99% without closing the store.",
        "verification": "official",
        "note": "Values from PAL Robotics' StockBot page and 2024 datasheet (checked 2026-11-25): 46 x 46 x 183 cm, two RAIN RFID readers with eight antennas (EPC Gen2 / ISO 18000-6C), 3D cameras for navigation and a 2D laser, autonomous dock charging, ERP/WMS integration through an API. Autonomy and charging figures differ between the two maker documents — the page says about 10 h of use and a 5 h recharge, the datasheet says 12 h of continuous use and a 4 h recharge — so 10 h is used and both are recorded here; capture height is 2.4 m in the datasheet and up to 4 m on the page. Weight, speed and payload are not published."
    })

# ---------------- 7. Bear Robotics Servi ----------------
def f7(r):
    r.update({
        "status": "Commercial",
        "length_mm": 430, "width_mm": 445, "height_mm": 1046,
        "payload_kg": 30, "max_speed_mps": 1.2, "min_speed_mps": 0.1,
        "runtime_h": 10.0,
        "certifications": ["NSF"],
        "safety_source": "https://www.bearrobotics.ai/servi",
        "sensors": ["LiDAR", "Cameras", "Tray weight sensors"],
        "official_url": "https://www.bearrobotics.ai/servi",
        "sources": ["https://www.bearrobotics.ai/servi"],
        "summary": "Bear Robotics' Servi is a restaurant delivery robot: a LiDAR-navigated tray carrier that runs food and buses tables for a 10-12 hour shift, carrying 10 kg per tray and 30 kg in total.",
        "verification": "official",
        "note": "Values from Bear Robotics' Servi page (checked 2026-11-25): 44.5 x 43 x 104.6 cm, drive speed 0.1-1.2 m/s, 2 trays plus 1 bus tub, 10 kg per tray and 66 lb (30 kg) total, battery life 10-12 h with a 4 h wall-charger recharge, 7-inch screen, NSF-certified, LiDAR and cameras with real-time rerouting, internal weight sensors for auto return. Runtime is given as a 10-12 h range, 10 h used as the value. The same page also lists Servi mini (98 cm, 1 tray, 44 lb total); this record is the full-size Servi. Weight is not published."
    })

# ---------------- 8. Pudu BellaBot Pro ----------------
def f8(r):
    r.update({
        "status": "Commercial",
        "length_mm": 570, "width_mm": 550, "height_mm": 1290, "weight_kg": 55,
        "payload_kg": 40, "max_speed_mps": 1.2, "min_speed_mps": 0.2,
        "runtime_h": 11.0,
        "sensors": ["2 front cameras", "3 RGBD sensors", "1 LiDAR"],
        "official_url": "https://www.pudurobotics.com/en/products/bellabotpro",
        "sources": ["https://www.pudurobotics.com/en/products/bellabotpro"],
        "summary": "Pudu Robotics' BellaBot Pro is a restaurant delivery and advertising robot: four 10 kg trays under an 18.5-inch ad screen, VSLAM plus LiDAR navigation and 360-degree obstacle sensing in a 65 cm-wide footprint.",
        "verification": "official",
        "note": "Values from Pudu's BellaBot Pro product page (checked 2026-11-25): 570 x 550 x 1290 mm, 55 kg, 40 kg total load (10 kg per tray, four adjustable trays), cruise speed 0.2-1.2 m/s, run-time 11 h with no load, 4.5 h charging, 10.1-inch operation screen plus 18.5-inch advertising screen, VSLAM + marker + LiDAR SLAM navigation, 65 cm path clearance, two forward cameras, three RGBD sensors and one radar/LiDAR for front-chassis coverage; 25.6 Ah battery capacity is stated without a pack voltage, so no Wh figure is stored. The same page's comparison table gives BellaBot 13 h of run-time and 70 cm clearance. Weight-bearing tray size 410 x 500 mm."
    })

# ---------------- 9. temi V3 ----------------
def f9(r):
    r.update({
        "status": "Commercial", "release_year": 2021,
        "length_mm": 450, "width_mm": 350, "height_mm": 1000, "weight_kg": 12,
        "payload_kg": 3, "max_speed_mps": 1.0, "wheel_count": 2,
        "runtime_h": 8.0, "api_support": True,
        "sdk_available": True, "sdk_name": "temi SDK",
        "sdk": {"languages": [], "open_source": None, "license": None,
                "url": "https://www.robotemi.com/product/temi/"},
        "onboard_compute": True, "compute_detail": "ARM hexa-core (dual Cortex-A72 + quad Cortex-A53), Android 11",
        "ros_support": None,
        "sensors": ["360-degree LiDAR", "2 depth cameras", "13 MP RGB camera", "IMU",
                    "6 time-of-flight sensors", "4-microphone array"],
        "official_url": "https://www.robotemi.com/product/temi/",
        "sources": ["https://www.robotemi.com/product/temi/",
                    "https://www.robotemi.com/robots/",
                    "https://www.robotemi.com/faq/"],
        "summary": "temi V3 is temi's 100 cm autonomous personal assistant robot: a two-wheel, zero-turn-radius platform with a 13.3-inch screen, 360-degree LiDAR navigation, an open Android SDK and about 8 hours of battery.",
        "verification": "official",
        "note": "Values from temi's product, robots and FAQ pages (checked 2026-11-25): 100 x 35 x 45 cm, 12 kg, two 50 W direct-drive brushless wheels with zero turn radius and up to 1 m/s, 13.3-inch 1920 x 1080 display, 360-degree LiDAR with two depth cameras, a 13 MP RGB camera, IMU and six time-of-flight sensors, ARM hexa-core computers running Android 11 with a full SDK for third-party apps, about 8 h of operation per charge with a roughly 3 h full charge, tray load 3 kg and a 30 x 25 cm tray. The maker's spec page describes temi (the V3 hardware per its own manuals list and tray note); ROS support is not stated."
    })

# ---------------- 10. KEENON T5 ----------------
def f10(r):
    r.update({
        "name": "DINERBOT T5",
        "sources": ["https://www.keenon.com/en/about/", "https://www.keenon.com/en"],
        "summary": "KEENON's DINERBOT T5, the 2019 first-generation delivery robot that began the company's overseas expansion; KEENON no longer publishes a product page or spec sheet for it.",
        "verification": "unconfirmed",
        "note": "Checked 2026-11-25: KEENON's current product pages cover DINERBOT T3/T8/T9/T10/T11, BUTLERBOT W3 and the X and S series, and there is no T5 product page or datasheet on the maker's site (keenon.com/en/product/T5 returns 404). The maker's own history page still records that DINERBOT T5 and T6 launched in 2019 and its customer cases name T5 units in service, so the model exists, but no maker document states its specifications — every value is left empty and the record stays marked unconfirmed rather than deleted. Name follows the maker's DINERBOT naming used on its other records."
    })

# ---------------- 11. Simbe Tally 4.0 ----------------
def f11(r):
    r.update({
        "status": "Commercial", "release_year": 2026, "runtime_h": 12.0,
        "onboard_compute": True,
        "compute_detail": "NVIDIA edge AI platform (CUDA, TensorRT, DOCA Argus)",
        "sensors": ["Ultra-high-resolution camera suite", "Intel RealSense depth cameras",
                    "Dual fisheye 360-degree cameras"],
        "official_url": "https://www.simberobotics.com/platform",
        "sources": ["https://www.simberobotics.com/about/newsroom/simbe-unveils-tally-4-0-the-next-generation-of-autonomous-retail-robot-powering-store-intelligence-via-physical-ai",
                    "https://www.simberobotics.com/platform"],
        "summary": "Simbe's Tally 4.0 is the fourth generation of its shelf-scanning retail robot: up to 12 hours of autonomous operation, a high-resolution camera suite with RealSense depth and 360-degree fisheye coverage, and NVIDIA edge AI that turns shelf images into stock and pricing data.",
        "verification": "official",
        "note": "Values from Simbe's Tally 4.0 launch release (2026-01-12) and platform page (checked 2026-11-25): up to 12 h of operation with shorter charging cycles, ultra-high-resolution and specialty cameras, RealSense depth cameras, dual fisheye cameras for 360-degree capture, NVIDIA CUDA/TensorRT/DOCA Argus edge computing, optional Tally RFID (up to 100K+ EPCs per run), night scanning, and availability to Simbe customers from mid-2026. The maker states the robot runs at less than a third of human walking speed but publishes no numeric speed, and gives no weight, dimensions or payload, so those stay empty. Tally Spot and Tally RFID are described as separate offerings on the same platform."
    })

# ---------------- 12. isento pib.Pro ----------------
def f12(r):
    r.update({
        "ros_support": True,
        "sensors": ["3D vision camera", "LiDAR"],
        "official_url": "https://pib.rocks/en/pib-pro/",
        "sources": ["https://pib.rocks/en/pib-pro/", "https://pib.rocks/"],
        "summary": "pib.Pro is isento's ready-to-ship open-source humanoid platform, the professional step up from the 3D-printable pib: stronger actuators and payload, 3D vision and LiDAR, onboard AI and a modular ROS-based stack, sold through a pilot-partner programme.",
        "verification": "official",
        "note": "Maker pages checked 2026-11-25: pib.Pro is described as Europe's first open, ready-to-ship humanoid platform, GDPR-compliant and modular, with stronger hardware and higher payload than pib, advanced 3D vision, LiDAR, onboard AI, and ROS software modules developed by its community; it is offered to pilot customers rather than sold as a catalogue product. The maker publishes no numeric specifications (height, weight, payload, speed, runtime, degrees of freedom, battery) for pib.Pro, so every value is left empty — figures circulating on aggregator sites are not maker values and are not used. pib, the 3D-printable predecessor, is a separate maker project."
    })

patch("data/parts/platform.json", "irobot-create-3", f)
patch("data/parts/quadruped.json", "petoi-quaddle", f2)
patch("data/parts/quadruped.json", "yahboom-dogzilla-s2", f3)
patch("data/parts/wheel-legged.json", "ogadjet-xgo-rider2", f4)
patch("data/parts/amr-agv.json", "robotnik-rb-watcher", f5)
patch("data/parts/amr-agv.json", "pal-stockbot", f6)
patch("data/parts/delivery.json", "bear-robotics-servi", f7)
patch("data/parts/delivery.json", "pudu-bellabot-pro", f8)
patch("data/parts/delivery.json", "temi-v3", f9)
patch("data/parts/delivery.json", "keenon-t5", f10)
patch("data/parts/amr-agv.json", "simbe-tally-4", f11)
patch("data/parts/humanoid.json", "isento-pib-pro", f12)
