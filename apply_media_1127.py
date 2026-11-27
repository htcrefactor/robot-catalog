#!/usr/bin/env python3
"""Media sweep 2026-11-27: add two robots found in this week's coverage, refresh one."""
import json

ORDER = ["id", "name", "manufacturer", "country", "category", "locomotion", "release_year",
         "status", "length_mm", "width_mm", "height_mm", "weight_kg", "payload_kg",
         "max_speed_mps", "min_speed_mps", "wheel_diameter_mm", "wheel_count", "dof",
         "runtime_h", "battery_wh", "ip_rating", "api_support", "sdk_available", "sdk_name",
         "onboard_compute", "compute_detail", "ros_support", "sensors", "price_usd", "price_note",
         "official_url", "sources", "summary", "image_url", "image_source", "videos", "seen_on",
         "verification", "note", "notes", "price_observations"]

BASE = {"release_year": None, "status": None, "length_mm": None, "width_mm": None, "height_mm": None,
        "weight_kg": None, "payload_kg": None, "max_speed_mps": None, "min_speed_mps": None,
        "wheel_diameter_mm": None, "wheel_count": None, "dof": None, "runtime_h": None,
        "battery_wh": None, "ip_rating": None, "api_support": None, "sdk_available": None,
        "sdk_name": None, "onboard_compute": None, "compute_detail": None, "ros_support": None,
        "sensors": [], "price_usd": None, "price_note": None, "official_url": None, "sources": [],
        "summary": "", "image_url": None, "image_source": None, "videos": [], "seen_on": [],
        "verification": None}


def rec(**kw):
    r = dict(BASE)
    r.update(kw)
    return {k: r[k] for k in ORDER if k in r}


SW01 = rec(
    id="astrall-dynamics-hypertron-sw01",
    name="Hypertron-SW01",
    manufacturer="Astrall Dynamics",
    country="China",
    category="Quadruped",
    locomotion="Legged",
    status="Commercial",
    length_mm=929, width_mm=556, height_mm=656,
    weight_kg=50, payload_kg=40,
    max_speed_mps=8,
    runtime_h=6, battery_wh=2166,
    ip_rating="IP67",
    sdk_available=True,
    onboard_compute=True,
    compute_detail="Industrial-grade 8-core processor, 16 GB RAM / 64 GB storage",
    sensors=["Solid-state LiDAR x1 (120 deg H x 90 deg V, 30 m)",
             "RGB camera 1600 x 1296",
             "9-axis IMU"],
    official_url="https://www.astralldynamics.com/en-US/product/1006.html",
    sources=["https://www.astralldynamics.com/en-US/product/1006.html",
             "https://www.astralldynamics.com/product/6.html"],
    summary="Mid-sized quadruped for inspection, patrol and firefighting duty that carries 40 kg over all-terrain ground and runs on hot-swappable batteries.",
    seen_on=["https://embodied.guide/robots/astrall-dynamics-hypertron-sw01/"],
    verification="official",
    note="Maker spec table (Shenzhen Astrall/璇玑动力, checked 2026-11-27): standing 929 x 556 x 656 mm, about 50 kg with battery, 40 kg all-terrain dynamic payload, 50 kg continuous walking payload, 120 kg short-term static standing load, 6 h no-load and 3 h with a 40 kg load, dual hot-swappable 57.6 V 18.8 Ah packs (battery_wh 2166 derived as 2 x 57.6 V x 18.8 Ah), IP67, -20 to 55 C, 25 cm continuous stair steps, 2 h fast charge to 80 %, industrial 8-core compute with 16 GB RAM and 64 GB storage, solid-state LiDAR 120 x 90 deg at 30 m, 1600 x 1296 RGB camera, 9-axis IMU, gigabit Ethernet x2 and 48 V / 240 W expansion power, open SDK. The maker's own footnotes limit the headline figures: 8 m/s is a laboratory peak and the shipping robot is capped at 1 m/s in all-terrain mode and 5-6 m/s in low-centre-of-gravity mode; 45 deg climb and 100 cm obstacle clearing are laboratory limits with 30 deg recommended; 240 N.m is a momentary peak. No price. Unlike its wheel-legged sibling T01 this one walks on feet only, so locomotion is Legged.",
)

IX = rec(
    id="simplexity-ix",
    name="iX",
    manufacturer="Simplexity Robotics",
    country="China",
    category="Humanoid",
    locomotion="Wheeled",
    release_year=2026,
    status="In development",
    length_mm=670, width_mm=548, height_mm=1060,
    weight_kg=160, payload_kg=3,
    max_speed_mps=1.5,
    dof=24,
    runtime_h=4.5, battery_wh=1650,
    sdk_available=True,
    onboard_compute="NVIDIA Jetson Orin NX 16GB 157 TOPS (standard) / NVIDIA Thor 64GB 730 TOPS (Pro)",
    sensors=["Head: 1 wide-angle camera + 3 fisheye cameras",
             "Chest RGBD camera",
             "2 wrist wide-angle cameras",
             "LiDAR x2",
             "8 ultrasonic sensors",
             "IMU"],
    official_url="https://www.simplexityrobotics.com/products/ix",
    sources=["https://www.simplexityrobotics.com/products/ix",
             "https://www.simplexityrobotics.com/"],
    summary="Wheeled humanoid for lobbies and public service work: 24 active DoF, a 540 mm lifting waist, two 7-DoF force-controlled arms and a four-wheel-steering base.",
    seen_on=["https://embodied.guide/robots/simplexity-ix/"],
    verification="official",
    note="Maker product page (checked 2026-11-27): 1,060-1,700 mm tall (height_mm is the minimum; the waist travels 540 mm) x 548 mm wide x 670 mm long, 160 kg, 24 active DoF excluding hands (2 neck, 7 per arm, 5 waist and lower body, 3 chassis), 3 kg payload at full extension, four-wheel steering and four-wheel drive at 1.5 m/s, 30 deg slope, two batteries totalling 1,650 Wh for about 4-5 h (4.5 h entered), 2 h charge per bay, 48 V DC, head wide-angle plus three fisheye cameras, chest RGBD, two wrist cameras, two LiDARs, eight ultrasonic sensors, four microphones and two speakers, Wi-Fi/Bluetooth/4G/5G, full SDK with EtherCAT, CAN FD and RS-485 buses. The maker's sheet gives two different arm figures - an 850 mm maximum working radius in the headline block against 650 mm working radius and 650 mm span in the arm table - and the note above keeps the headline; arm weight is likewise listed as both 6.5 kg and 8 kg. The page headline says NVIDIA Thor while the table ships Orin NX 16 GB as standard and Thor as the Pro option. Unveiled 2026-11-23 and not yet shipping; no price.",
)


def reorder(r):
    return {k: r[k] for k in ORDER if k in r} | {k: v for k, v in r.items() if k not in ORDER}


def main():
    # 1) add the two new records at the end of their category files
    for path, new in (("data/parts/quadruped.json", SW01), ("data/parts/humanoid.json", IX)):
        data = json.load(open(path, encoding="utf-8"))
        if any(r["id"] == new["id"] for r in data):
            raise SystemExit(f"{new['id']} already present in {path}")
        data.append(new)
        write(path, data)

    # 2) refresh Foundation Phantom MKII: the maker page now names the generation
    path = "data/parts/humanoid.json"
    data = json.load(open(path, encoding="utf-8"))
    for i, r in enumerate(data):
        if r["id"] != "foundation-phantom-mk2":
            continue
        r["status"] = "In development"
        r["weight_kg"] = 88.5
        r["payload_kg"] = 90
        r["dof"] = 29
        r["runtime_h"] = 4
        r["battery_wh"] = 3000
        r["ip_rating"] = "IP67"
        r["summary"] = ("Foundation's Phantom MKII: a 1.83 m, 88.5 kg biped rated to carry 200 lb (90 kg) "
                        "through factories, mines, ports and the frontlines.")
        r["sources"] = ["https://foundation.bot/phantom", "https://foundation.bot/press"]
        r["verification"] = "official"
        r["note"] = ("Maker's Phantom page (checked 2026-11-27) now names the generation: the press kit is headed "
                     "'Phantom MKII and Cortex II', and the page lists 6.0 ft (1830 mm), 195 lb (88.5 kg), a 200 lb / 90 kg "
                     "close-carry payload, 4-6 h runtime (runtime_h is the lower end), 29 DoF, a 3 kWh battery, IP67, and "
                     "modular joints that swap in the field. Height and weight are published in feet and pounds, so the "
                     "metric values are conversions. The maker states specifications describe shipping capability and are "
                     "subject to change, with production planned for 2027; no price, unit count or customer is published. "
                     "The payload is a close-carry rating and has no independent test.")
        break
    write(path, data)


def write(path, data):
    text = open(path, encoding="utf-8").read()
    trailing = "\n" if text.endswith("\n") else ""
    indent = 2 if text.split("\n")[1].startswith("  {") else 1
    open(path, "w", encoding="utf-8").write(json.dumps(data, ensure_ascii=False, indent=indent) + trailing)
    print("wrote", path, len(data), "records")


if __name__ == "__main__":
    main()
