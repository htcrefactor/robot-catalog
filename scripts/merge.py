"""Merge data/parts/*.json into data/robots.json (what the site reads) and record per-robot history.

Every merge compares each record with the previous data/robots.json and appends field-level
events (old -> new, date, source) to data/history/<id>.json, then rebuilds feed.xml.
History is additive: a robot's file keeps its past events (newest last, capped at 100) and is
never rewritten from scratch, so a rename, a filled-in spec or a removal stays on record.

Usage: python3 scripts/merge.py [--notes "<what changed>"] [--date YYYY-MM-DD]
--date only exists to make a run reproducible (tests); it defaults to today.
"""
import datetime, glob, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HISTORY_DIR = os.path.join(ROOT, "data", "history")
HISTORY_LIMIT = 100


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def merge():
    robots = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "data", "parts", "*.json"))):
        for r in load(path):
            robots[r["id"]] = r

    built = os.path.join(ROOT, "data", "robots.json")
    previous = {}
    if os.path.exists(built):
        previous = {r["id"]: r for r in load(built).get("robots", [])}
    return robots, previous


def field_changes(old, new):
    """Field-level diff of one record: what a reader would want to see change."""
    changes = []
    for key in sorted(set(old) | set(new)):
        before, after = old.get(key), new.get(key)
        if before == after:
            continue
        changes.append({"field": key, "from": before, "to": after})
    return changes


def source_of(record):
    if record.get("official_url"):
        return record["official_url"]
    sources = record.get("sources") or []
    return sources[0] if sources else None


def record_event(rid, record, event, date):
    """Append one event to data/history/<id>.json, folding a same-day update into the last one."""
    os.makedirs(HISTORY_DIR, exist_ok=True)
    path = os.path.join(HISTORY_DIR, f"{rid}.json")
    data = {}
    if os.path.exists(path):
        data = load(path)
    data["id"] = rid
    if record:
        data["name"] = record.get("name")
        data["manufacturer"] = record.get("manufacturer")
    data["updated"] = date
    events = data.setdefault("events", [])
    last = events[-1] if events else None
    if last and last.get("date") == date and last.get("type") == event["type"] == "updated":
        merged = {c["field"]: c for c in last.get("changes") or []}
        for c in event["changes"]:
            if c["field"] in merged:
                merged[c["field"]]["to"] = c["to"]
                if merged[c["field"]]["from"] == merged[c["field"]]["to"]:
                    del merged[c["field"]]
            else:
                merged[c["field"]] = c
        last["changes"] = list(merged.values())
        if not last["changes"]:
            events.pop()
        if event.get("source"):
            last["source"] = event["source"]
    else:
        events.append(event)
    data["events"] = events[-HISTORY_LIMIT:]
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
        f.write("\n")


def record_changes(robots, previous, date):
    changed = []
    for rid, record in robots.items():
        old = previous.get(rid)
        if old is None:
            event = {"date": date, "type": "added", "source": source_of(record), "changes": []}
        else:
            changes = field_changes(old, record)
            if not changes:
                continue
            event = {"date": date, "type": "updated", "source": source_of(record), "changes": changes}
        record_event(rid, record, event, date)
        changed.append(rid)
    for rid in previous:
        if rid not in robots:
            record_event(rid, None, {"date": date, "type": "removed", "source": None, "changes": []}, date)
            changed.append(rid)
    return changed


def main(argv):
    date = datetime.date.today().isoformat()
    if "--date" in argv:
        date = argv[argv.index("--date") + 1]
        datetime.date.fromisoformat(date)  # fail loudly on a bad date
    robots, previous = merge()
    out = {"meta": {"updated": date, "count": len(robots)},
           "robots": sorted(robots.values(), key=lambda r: (r["category"], r["manufacturer"], r["name"]))}
    with open(os.path.join(ROOT, "data", "robots.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write("\n")
    changed = record_changes(robots, previous, date)
    sys.path.insert(0, os.path.join(ROOT, "scripts"))
    import build_feed
    build_feed.write()
    print(f"{len(robots)} robots, {len(changed)} changed, history and feed.xml updated")


if __name__ == "__main__":
    main(sys.argv[1:])
