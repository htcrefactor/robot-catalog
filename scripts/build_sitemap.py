#!/usr/bin/env python3
"""Build sitemap.xml for the Robot Catalog (GitHub Pages project site).
Run after scripts/merge.py whenever robots are added or updated."""
import json, os
from urllib.parse import quote
from xml.sax.saxutils import escape

BASE = "https://htcrefactor.github.io/robot-catalog/"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data = json.load(open(os.path.join(ROOT, "data", "robots.json"), encoding="utf-8"))
updated = data["meta"].get("updated")

urls = [(BASE, "1.0"), (BASE + "chips.html", "0.8"), (BASE + "table.html", "0.8"),
        (BASE + "specs.html", "0.8"), (BASE + "data.html", "0.8"), (BASE + "dashboard.html", "0.6")]
for r in sorted(data["robots"], key=lambda r: r["id"]):
    urls.append((BASE + "robot.html?id=" + quote(r["id"]), "0.7"))

out = ['<?xml version="1.0" encoding="UTF-8"?>',
       '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for loc, pri in urls:
    lm = f"<lastmod>{updated}</lastmod>" if updated else ""
    out.append(f"  <url><loc>{escape(loc)}</loc>{lm}<priority>{pri}</priority></url>")
out.append("</urlset>")
open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print(f"sitemap.xml: {len(urls)} URLs")
