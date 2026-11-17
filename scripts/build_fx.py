#!/usr/bin/env python3
"""Build data/fx.json — KRW cross rates with their date, from the ECB daily reference rates.

The site never stores a converted KRW figure: each record keeps the amount in the currency the
maker states, and the page converts it at run time with this file, so the rate and its date stay
visible next to the number. Run this when you add a dated price observation (and whenever the rate
should be refreshed), then commit data/fx.json.

    python3 scripts/build_fx.py                 # fetch the ECB daily file and write data/fx.json
    python3 scripts/build_fx.py --from-file x.xml   # use a saved copy of the same file (no network)
"""
import json, os, re, sys, datetime
import urllib.request

URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "fx.json")


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "robot-catalog/1.0 (+https://htcrefactor.github.io/robot-catalog/)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8")


def main():
    src = sys.argv[2] if len(sys.argv) > 2 and sys.argv[1] == "--from-file" else None
    xml = open(src, encoding="utf-8").read() if src else fetch(URL)

    m = re.search(r"<Cube time='([0-9-]+)'>", xml)
    if not m:
        sys.exit("no reference date in the ECB file")
    date = m.group(1)
    per_eur = {c: float(r) for c, r in re.findall(r"currency='([A-Z]{3})' rate='([0-9.]+)'", xml)}
    if "KRW" not in per_eur:
        sys.exit("KRW missing from the ECB file")

    krw_per_eur = per_eur["KRW"]
    rates = {"KRW": 1.0}
    for cur, v in sorted(per_eur.items()):
        if cur == "EUR" or cur == "KRW" or not v:
            continue
        rates[cur] = round(krw_per_eur / v, 4)
    rates["EUR"] = round(krw_per_eur, 4)

    out = {
        "source": "European Central Bank euro foreign exchange reference rates (daily)",
        "source_url": URL,
        "date": date,
        "fetched": datetime.date.today().isoformat(),
        "base": "KRW",
        "method": "rates are KRW per 1 unit, crossed from the ECB rates quoted per EUR (KRW per EUR divided by the currency per EUR)",
        "rates": dict(sorted(rates.items())),
    }
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"data/fx.json: {len(out['rates'])} currencies, ECB reference date {date}, US$1 = KRW {out['rates']['USD']}")


if __name__ == "__main__":
    main()
