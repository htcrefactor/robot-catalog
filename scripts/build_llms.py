#!/usr/bin/env python3
"""Build the AI-facing views of the catalog for LLM agents (issue #25).

Run after scripts/merge.py, next to scripts/build_sitemap.py, whenever robots are added or updated.
GitHub Pages serves the files as they are in the repo (.nojekyll), so these are generated here and
committed together with the data change.

  llms.txt        site summary plus one link per robot — the index an agent reads first
  llms-full.txt    every robot's core specs and sources in a single file
  md/<id>.md       one robot per file: core specs, full spec sheet with a source on every value

Every file is written from data/robots.json and data/specs/*.json only, with no clock of its own
(the date shown is the merge date already in robots.json), so re-running on unchanged data
produces byte-identical output.
"""
import glob
import json
import os
import re
from urllib.parse import urlparse

BASE = "https://htcrefactor.github.io/robot-catalog/"
REPO = "https://github.com/htcrefactor/robot-catalog"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Category order used by the site (assets/app.js CATS).
CATS = ["AMR", "AGV", "Humanoid", "Quadruped", "Wheel-legged",
        "Indoor delivery", "Outdoor delivery", "Mobile platform", "Misc"]

# Full-spec group order used by the site (assets/specs-i18n.js GROUPS), plus the legacy Payload group.
GROUPS = ["Identity", "Dimensions & Mass", "Mobility & Performance", "Terrain & Navigation Limits",
          "Power & Battery", "Charging & Docking", "Environment & Protection", "Sensors & Perception",
          "Compute & Software", "Connectivity & Interfaces", "Payload & Mounting", "Manipulation",
          "Actuation & Joints", "Safety & Compliance", "Controls & Operation", "Audio, Lights & HMI",
          "Transport & Storage", "Commercial", "Payload"]

VERIFICATION = {
    "official": "official — checked against a maker source",
    "unconfirmed": "unconfirmed — no maker source found yet",
    None: "not recorded",
}


def load():
    data = json.load(open(os.path.join(ROOT, "data", "robots.json"), encoding="utf-8"))
    specs = {}
    for path in glob.glob(os.path.join(ROOT, "data", "specs", "*.json")):
        spec = json.load(open(path, encoding="utf-8"))
        specs[spec["id"]] = spec
    return data, specs


def host(url):
    try:
        return urlparse(url).netloc.replace("www.", "") or url
    except ValueError:
        return url


def cell(value):
    """One table cell: no newlines, pipes escaped."""
    return re.sub(r"\s+", " ", str(value)).strip().replace("|", "\\|")


def link(url, text=None):
    return "[%s](%s)" % (cell(text if text else host(url)), url)


def number(value):
    if isinstance(value, bool):
        return "yes" if value else "no"
    if isinstance(value, float):
        value = int(value) if value.is_integer() else round(value, 4)
    return "{:,}".format(value) if isinstance(value, int) else str(value)


def plain(value):
    """A sentence on one line, safe inside a bullet."""
    return re.sub(r"\s+", " ", str(value)).strip()


# A dated price observation is shown in the currency the maker states, with the date, the kind of
# price and the maker / maker-store link it came from. No KRW figure is written here: the site
# converts at run time from data/fx.json, so the export never stores a rate or a second currency.
PRICE_SIGNS = {"USD": "US$", "EUR": "€", "KRW": "₩", "CNY": "CN¥", "JPY": "¥", "GBP": "£"}
PRICE_KINDS = {"list": "list price", "from": "starting price", "rental": "rental rate", "edu": "education price"}


def money(amount, currency):
    sign = PRICE_SIGNS.get(currency)
    text = number(amount)
    return sign + text if sign else "%s %s" % (text, currency)


def price_observation_text(o):
    """`US$339.90 · starting price · 2026-11-27 · [yahboom.store](https://…) (note)`"""
    parts = [money(o.get("amount"), o.get("currency")), PRICE_KINDS.get(o.get("kind"), o.get("kind") or "price"),
             str(o.get("date") or "undated")]
    if o.get("source"):
        parts.append(link(o["source"]))
    text = " · ".join(p for p in parts if p)
    if o.get("note"):
        text += " (%s)" % plain(o["note"])
    return text


def core_rows(r):
    """The record's own spec fields, in the order the site shows them. Absent values are left out."""
    rows = []

    def put(label, value, unit=""):
        if value is None or value == "" or value == []:
            return
        if isinstance(value, bool):
            text = "yes" if value else "no"
        elif isinstance(value, (int, float)):
            text = number(value) + (" " + unit if unit else "")
        else:
            text = str(value)
        rows.append((label, text))

    put("Length", r.get("length_mm"), "mm")
    put("Width", r.get("width_mm"), "mm")
    put("Height", r.get("height_mm"), "mm")
    put("Weight", r.get("weight_kg"), "kg")
    put("Payload", r.get("payload_kg"), "kg")
    if r.get("max_speed_mps") is not None:
        speed = number(r["max_speed_mps"])
        rows.append(("Max speed", "%s m/s (%s km/h)" % (speed, round(r["max_speed_mps"] * 3.6, 1))))
    put("Min speed", r.get("min_speed_mps"), "m/s")
    put("Wheel diameter", r.get("wheel_diameter_mm"), "mm")
    put("Wheels", r.get("wheel_count"))
    put("Degrees of freedom", r.get("dof"))
    put("Runtime", r.get("runtime_h"), "h")
    put("Battery", r.get("battery_wh"), "Wh")
    put("IP rating", r.get("ip_rating"))
    if r.get("release_year"):
        rows.append(("Released", str(r["release_year"])))
    put("Status", r.get("status"))
    if r.get("price_usd") is not None:
        price = "US$" + number(r["price_usd"])
        if r.get("price_note"):
            price += " (%s)" % plain(r["price_note"])
        rows.append(("Price", price))
    elif r.get("price_note"):
        rows.append(("Price", plain(r["price_note"])))
    for o in sorted(r.get("price_observations") or [],
                    key=lambda o: (str(o.get("date") or ""), ["from", "list", "rental", "edu"].index(o.get("kind"))
                                   if o.get("kind") in ("from", "list", "rental", "edu") else 9)):
        rows.append(("Price", price_observation_text(o)))
    put("API", r.get("api_support"))
    put("SDK", r.get("sdk_available"))
    put("SDK name", r.get("sdk_name"))
    put("ROS", r.get("ros_support"))
    put("On-board compute", r.get("onboard_compute"))
    put("Compute", r.get("compute_detail"))
    put("Sensors", ", ".join(r.get("sensors") or []))
    return rows


def spec_table(spec):
    """Full spec sheet grouped like the robot page: one row per published value, with its source."""
    groups = {}
    for s in spec.get("specs") or []:
        groups.setdefault(s.get("group") or "Other", []).append(s)
    order = [g for g in GROUPS if g in groups] + sorted(g for g in groups if g not in GROUPS)
    out = []
    for g in order:
        out.append("### " + g)
        out.append("")
        out.append("| Spec | Value | Note | Source |")
        out.append("|---|---|---|---|")
        for s in groups[g]:
            label = s.get("label") or s.get("key") or ""
            value = s.get("value")
            if isinstance(value, bool):
                value = "yes" if value else "no"
            elif isinstance(value, (int, float)):
                value = number(value)
            else:
                value = plain(value if value is not None else "")
            if s.get("unit") and str(s["unit"]).strip():
                value = (value + " " + str(s["unit"]).strip()).strip()
            note = plain(s.get("note") or "")
            source = ""
            if s.get("source"):
                source = link(s["source"])
                if s.get("ref"):
                    source += " · " + cell(s["ref"])
            out.append("| %s | %s | %s | %s |" % (cell(label), cell(value), cell(note), source))
        out.append("")
    return out


def robot_md(r, meta, spec):
    out = []
    a = out.append
    a("# %s %s" % (r["manufacturer"], r["name"]))
    a("")
    if r.get("summary"):
        a("> " + plain(r["summary"]))
        a("")
    a("- Catalog page: %srobot.html?id=%s" % (BASE, r["id"]))
    a("- Category: %s" % r["category"])
    if r.get("locomotion"):
        a("- Locomotion: %s" % r["locomotion"])
    a("- Manufacturer: %s%s" % (r["manufacturer"], " (%s)" % r["country"] if r.get("country") else ""))
    a("- Verification: %s" % VERIFICATION.get(r.get("verification"), r.get("verification")))
    if r.get("data_source"):
        a("- Data source: %s" % plain(r["data_source"]))
    a("")
    if r.get("misc_reason"):
        a("**Why Misc:** %s" % plain(r["misc_reason"]))
        a("")
        if r.get("original_category"):
            a("Listed by others as: %s" % plain(r["original_category"]))
            a("")

    a("## Core specs")
    a("")
    rows = core_rows(r)
    if rows:
        a("| Field | Value |")
        a("|---|---|")
        for label, value in rows:
            a("| %s | %s |" % (cell(label), cell(value)))
    else:
        a("No core field is published for this robot yet.")
    a("")
    a("Fields the maker does not publish are left out here — the catalog never fills a value by guess. "
      "Prices are list or starting prices where the maker states one.")
    a("")

    if spec and spec.get("specs"):
        docs = spec.get("documents") or []
        a("## Full spec sheet")
        a("")
        header = "%d values" % len(spec["specs"])
        if docs:
            header += " from %d document%s" % (len(docs), "" if len(docs) == 1 else "s")
        if spec.get("checked"):
            header += ", checked against maker sources on %s" % spec["checked"]
        a(header + ".")
        a("")
        out.extend(spec_table(spec))
        if docs:
            a("## Documents")
            a("")
            for d in docs:
                if d.get("url"):
                    a("- %s" % link(d["url"], d.get("title") or d["url"]))
            a("")
    else:
        a("## Full spec sheet")
        a("")
        a("The full spec sheet for this robot is still being researched; the catalog core fields above "
          "are every value recorded so far.")
        a("")

    if r.get("variants"):
        a("## Variants")
        a("")
        for v in r["variants"]:
            text = "- **%s**" % plain(v.get("name") or v.get("id") or "")
            if v.get("note"):
                text += " — " + plain(v["note"])
            if v.get("url"):
                text += " ([maker page](%s))" % v["url"]
            a(text)
        a("")

    if r.get("note"):
        a("## Notes")
        a("")
        a(plain(r["note"]))
        a("")

    a("## Sources")
    a("")
    official = r.get("official_url")
    listed = []
    if official:
        a("- Official page: %s" % link(official))
        listed.append(official)
    for url in r.get("sources") or []:
        if url not in listed:
            a("- %s" % link(url))
            listed.append(url)
    if not listed:
        a("- No source URL recorded for this robot yet.")
    if r.get("seen_on"):
        a("")
        a("Listed by these directories (discovery only, never used as a spec source):")
        a("")
        for s in r["seen_on"]:
            a("- %s" % link(s))
    a("")
    a("---")
    a("")
    a("*Robot Catalog — generated from data/robots.json (last merged %s). Source repository: %s*"
      % (meta.get("updated") or "unknown", REPO))
    a("")
    return "\n".join(out)


def short_summary(r, limit=110):
    s = plain(r.get("summary") or "")
    if len(s) <= limit:
        return s
    cut = s[:limit].rsplit(" ", 1)[0].rstrip(",;:")
    return cut + "…"


def build_llms(data, specs):
    robots = data["robots"]
    meta = data["meta"]
    cats = [c for c in CATS if any(r["category"] == c for r in robots)]
    makers = len({r["manufacturer"] for r in robots})
    official = sum(1 for r in robots if r.get("verification") == "official")
    with_specs = sum(1 for r in robots if specs.get(r["id"], {}).get("specs"))

    out = []
    a = out.append
    a("# Robot Catalog")
    a("")
    a("> Open catalog of %d mobile robots in %d categories — humanoids, quadrupeds, AMRs, AGVs, "
      "wheel-legged robots, delivery robots and development platforms — each with its published "
      "specs and the maker source behind every value." % (len(robots), len(cats)))
    a("")
    a("Robot Catalog is a static, bilingual (English/Korean) catalog of mobile robots by %d makers. "
      "Every value comes from the maker's own page, datasheet, manual, press release or lab paper and "
      "is linked on the robot's page; where the maker states nothing the field stays empty rather than "
      "being estimated. The catalog records published specs only — there is no scoring, no rating and "
      "no ranking." % makers)
    a("")
    a("- Robots: %d. %d records are verified against a maker source, %d carry a full spec sheet."
      % (len(robots), official, with_specs))
    a("- One page per robot: %srobot.html?id=<id>" % BASE)
    a("- One Markdown file per robot, with the full spec sheet and a source on every value: "
      "%smd/<id>.md" % BASE)
    a("- Data last merged: %s." % (meta.get("updated") or "unknown"))
    a("- To cite a spec, link the robot's page and the maker document printed next to the value in "
      "its Markdown file.")
    a("- Attribution: some humanoid prices and sales status come from HumanoidStore open data "
      "(CC BY 4.0, humanoidstore.co); the records that use it say so in their Markdown file.")
    a("")
    a("## Pages")
    a("")
    a("- [All robots](%sindex.html): every robot as a card, filterable by category and searchable by "
      "name or maker." % BASE)
    a("- [Mega table](%stable.html): every robot and every field in one sortable table, with CSV download."
      % BASE)
    a("- [Dashboard](%sdashboard.html): speed, payload, wheel diameter, IP rating and feature coverage "
      "across the catalog." % BASE)
    a("- [All specs](%sspecs.html): every spec field in the catalog, with the robots that publish it."
      % BASE)
    a("- [Full catalog in one file](%sllms-full.txt): every robot's core specs and sources in a single "
      "text file." % BASE)
    a("- [Full spec sheets as JSON](%sdata/specs/): one file per robot, keyed by the same id."
      % BASE)
    a("")
    a("## Robots")
    a("")
    for c in cats:
        group = sorted((r for r in robots if r["category"] == c),
                       key=lambda r: (r["manufacturer"].lower(), r["name"].lower()))
        a("### %s (%d)" % (c, len(group)))
        a("")
        for r in group:
            line = "- [%s %s](%smd/%s.md): %s" % (r["manufacturer"], r["name"], BASE, r["id"],
                                                   short_summary(r) or r["category"])
            a(line)
        a("")
    a("## Optional")
    a("")
    a("- [Data schema](%sdata/SCHEMA.md): what each record field means, and how unknown values are "
      "recorded." % BASE)
    a("- [Raw records](%sdata/robots.json): every robot as JSON — the file the site reads."
      % BASE)
    a("- [Contributor and agent rules](%sAGENTS.md): scope, source rules and the per-issue workflow."
      % BASE)
    a("- [Changelog](%schangelog.html): what changed in the data and when." % BASE)
    a("")
    return "\n".join(out)


def build_llms_full(data, specs):
    robots = data["robots"]
    meta = data["meta"]
    cats = [c for c in CATS if any(r["category"] == c for r in robots)]
    out = []
    a = out.append
    a("# Robot Catalog — full catalog")
    a("")
    a("> Every robot in Robot Catalog (%d) with its core specs and sources, in one file. Values are as "
      "the maker publishes them; fields the maker does not publish are left out rather than estimated."
      % len(robots))
    a("")
    a("- Canonical site: %s" % BASE)
    a("- Index for agents: %sllms.txt" % BASE)
    a("- Per-robot Markdown with the full spec sheet and a source on every value: %smd/<id>.md" % BASE)
    a("- Generated from data/robots.json, last merged %s. No scoring, no ranking."
      % (meta.get("updated") or "unknown"))
    a("")
    for c in cats:
        group = sorted((r for r in robots if r["category"] == c),
                       key=lambda r: (r["manufacturer"].lower(), r["name"].lower()))
        a("## %s (%d)" % (c, len(group)))
        a("")
        for r in group:
            a("### %s %s" % (r["manufacturer"], r["name"]))
            a("")
            a("- id: `%s`" % r["id"])
            a("- Page: %srobot.html?id=%s" % (BASE, r["id"]))
            a("- Markdown: %smd/%s.md" % (BASE, r["id"]))
            facts = [r["category"]]
            if r.get("locomotion"):
                facts.append(r["locomotion"])
            if r.get("status"):
                facts.append(r["status"])
            if r.get("country"):
                facts.append(r["country"])
            if r.get("release_year"):
                facts.append("released %s" % r["release_year"])
            a("- " + " · ".join(facts))
            if r.get("summary"):
                a("- Summary: " + plain(r["summary"]))
            rows = core_rows(r)
            if rows:
                a("- Specs: " + "; ".join("%s %s" % (label, value) for label, value in rows))
            sources = []
            if r.get("official_url"):
                sources.append(r["official_url"])
            sources += [s for s in (r.get("sources") or []) if s != r.get("official_url")]
            a("- Sources: " + (", ".join(sources) if sources else "none recorded"))
            a("")
    return "\n".join(out)


def write(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)


def main():
    data, specs = load()
    meta = {"updated": data["meta"].get("updated")}
    robots = data["robots"]

    md_dir = os.path.join(ROOT, "md")
    os.makedirs(md_dir, exist_ok=True)
    written = set()
    for r in robots:
        path = os.path.join(md_dir, r["id"] + ".md")
        write(path, robot_md(r, meta, specs.get(r["id"])))
        written.add(r["id"] + ".md")
    # Drop Markdown for robots that no longer exist.
    removed = 0
    for name in os.listdir(md_dir):
        if name.endswith(".md") and name not in written:
            os.remove(os.path.join(md_dir, name))
            removed += 1

    llms = write(os.path.join(ROOT, "llms.txt"), build_llms(data, specs))
    full = write(os.path.join(ROOT, "llms-full.txt"), build_llms_full(data, specs))
    print("%d robots, %d spec sheets" % (len(robots), len(specs)))
    print("llms.txt: %d chars" % llms)
    print("llms-full.txt: %d chars" % full)
    print("md/: %d files%s" % (len(written), ", %d removed" % removed if removed else ""))


if __name__ == "__main__":
    main()
