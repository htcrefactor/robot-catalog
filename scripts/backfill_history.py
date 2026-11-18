"""Backfill data/history/<id>.json from the repository's own git history (issue #66).

scripts/merge.py records history only for the change it is merging, and it only started doing
that on 2026-11-18 (#27). Everything the catalog changed before that — imports, verification
batches, renames, the HumanoidStore replacement, compute/safety/KO/price fields — happened in
data/parts commits and is therefore in git but missing from data/history.

This one-off script replays those commits. For every first-parent commit that touched
data/parts it loads every data/parts/*.json at that commit and at the previous such commit,
indexes them by id, and diffs them with merge.field_changes() — the same function merge.py
uses — so the events are what merge.py would have written had it been running then:

  added    a record id that was not in the previous commit
  updated  a record id whose fields differ from the previous commit (field-level from/to)
  removed  a record id that was in the previous commit and is not in this one

Each event carries the commit's date (%cs), the record's source (official_url, else its first
sources URL, as merge.source_of()), and the short sha of the commit that produced it. Events of
the same robot and day fold into one, exactly like merge.record_event() does, and a robot's
file is capped at HISTORY_LIMIT events.

Renames and merges (#11) show up as removed + added, because no id survives them. When a commit
message names the move as `old-id → new-id` the event says so in `note`.

data/parts is only read, through git; no record is changed.

Safe to re-run: events are rebuilt from git, never appended, so a second run writes byte-identical
files and git reports no diff. If an existing history file holds an event this run cannot
reproduce (for example one merge.py recorded after the backfill), the run stops instead of
dropping it; --force overrides that.

Usage:
  python3 scripts/backfill_history.py [--ref main] [--dry-run] [--force]
"""
import argparse
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HISTORY_DIR = os.path.join(ROOT, "data", "history")
PARTS = "data/parts"

sys.path.insert(0, os.path.join(ROOT, "scripts"))
from merge import HISTORY_LIMIT, field_changes, source_of  # noqa: E402

# `old-id → new-id` inside a commit message (#11 renames and merges).
RENAME_RE = re.compile(r"([a-z0-9][a-z0-9.-]*)\s*(?:→|->)\s*([a-z0-9][a-z0-9.-]*)")


def git(*args):
    res = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    if res.returncode:
        raise SystemExit(f"git {' '.join(args)} failed: {res.stderr.strip()}")
    return res.stdout


def commits(ref):
    """First-parent commits that touched data/parts, oldest first: [(sha, date, message)]."""
    out = git("log", "--first-parent", "--reverse",
              "--format=%x1e%H%x1f%cs%x1f%B", ref, "--", PARTS)
    found = []
    for chunk in out.split("\x1e"):
        if not chunk.strip():
            continue
        sha, date, body = chunk.split("\x1f", 2)
        found.append((sha.strip(), date.strip(), body))
    return found


def parts_at(commit):
    """id -> record, from every data/parts JSON file at that commit."""
    records = {}
    for path in git("ls-tree", "-r", "--name-only", commit, PARTS + "/").split():
        if not path.endswith(".json"):
            continue
        for record in json.loads(git("show", f"{commit}:{path}")):
            records[record["id"]] = record
    return records


def renames_in(message, removed, added):
    """old id -> new id pairs the commit message names, limited to ids this commit moved."""
    pairs = {}
    for old, new in RENAME_RE.findall(message or ""):
        if old in removed and new in added:
            pairs[old] = new
    return pairs


def event(date, kind, source, commit, changes, note=None):
    out = {"date": date, "type": kind, "source": source, "commit": commit}
    if note:
        out["note"] = note
    out["changes"] = changes
    return out


def add_event(history, rid, record, ev, date):
    """Append one event to an in-memory history entry.

    Same rules as merge.record_event(): a same-day `updated` event folds into the day's last
    one (field set merged, a field back at its old value dropped, source of the newest event
    kept), a fold also takes the newest commit, and the file keeps the last HISTORY_LIMIT events.
    """
    data = history.setdefault(rid, {"id": rid, "events": []})
    if record:
        data["name"] = record.get("name")
        data["manufacturer"] = record.get("manufacturer")
    data["updated"] = date
    events = data["events"]
    last = events[-1] if events else None
    if last and last.get("date") == date and last.get("type") == ev["type"] == "updated":
        merged = {c["field"]: c for c in last.get("changes") or []}
        for c in ev["changes"]:
            if c["field"] in merged:
                merged[c["field"]]["to"] = c["to"]
                if merged[c["field"]]["from"] == merged[c["field"]]["to"]:
                    del merged[c["field"]]
            else:
                merged[c["field"]] = c
        last["changes"] = list(merged.values())
        if not last["changes"]:
            events.pop()
        if ev.get("source"):
            last["source"] = ev["source"]
        if ev.get("commit"):
            last["commit"] = ev["commit"]
    else:
        events.append(ev)
    data["events"] = events[-HISTORY_LIMIT:]


def build(ref):
    """Replay every commit: id -> {"id", "name", "manufacturer", "updated", "events"}."""
    history = {}
    previous = {}
    walked = commits(ref)
    for sha, date, message in walked:
        current = parts_at(sha)
        short = sha[:7]
        added = set(current) - set(previous)
        removed = set(previous) - set(current)
        renamed = renames_in(message, removed, added)
        back = {new: old for old, new in renamed.items()}
        for rid in sorted(added):
            note = f"renamed from {back[rid]} in this commit" if rid in back else None
            add_event(history, rid, current[rid],
                      event(date, "added", source_of(current[rid]), short, [], note), date)
        for rid in sorted(set(current) & set(previous)):
            changes = field_changes(previous[rid], current[rid])
            if not changes:
                continue
            add_event(history, rid, current[rid],
                      event(date, "updated", source_of(current[rid]), short, changes), date)
        for rid in sorted(removed):
            note = f"renamed to {renamed[rid]} in this commit" if rid in renamed else None
            # no record to read a name from: keep the one the file already has
            add_event(history, rid, None,
                      event(date, "removed", None, short, [], note), date)
        previous = current
    return history, walked


def dumps(data):
    # merge.py's layout, so a file written here and one written by a later merge read the same
    order = ("id", "name", "manufacturer", "updated", "events")
    out = {k: data[k] for k in order if k in data}
    out.update({k: v for k, v in data.items() if k not in out})
    return json.dumps(out, ensure_ascii=False, indent=1) + "\n"


def event_key(ev):
    return (str(ev.get("date")), str(ev.get("type")),
            json.dumps(ev.get("changes"), sort_keys=True, ensure_ascii=False))


def unreproducible(path, data, rebuilt):
    """Events in an existing file that this run would not write again."""
    keys = {event_key(e) for e in rebuilt}
    return [e for e in data.get("events") or [] if event_key(e) not in keys]


def main(argv):
    ap = argparse.ArgumentParser(description="Backfill data/history from git history.")
    ap.add_argument("--ref", default="main", help="branch whose first-parent history to walk (default: main)")
    ap.add_argument("--dry-run", action="store_true", help="report what would change, write nothing")
    ap.add_argument("--force", action="store_true", help="overwrite history files holding events this run cannot reproduce")
    args = ap.parse_args(argv)

    history, walked = build(args.ref)
    if not walked:
        raise SystemExit(f"no commit touched {PARTS} on {args.ref}: nothing to backfill")

    os.makedirs(HISTORY_DIR, exist_ok=True)
    written = unchanged = 0
    dropped = []
    for rid in sorted(history):
        data = history[rid]
        path = os.path.join(HISTORY_DIR, f"{rid}.json")
        text = dumps(data)
        old = None
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                old_text = f.read()
            old = json.loads(old_text) if old_text.strip() else None
            if old_text == text:
                unchanged += 1
                continue
            lost = unreproducible(path, old, data["events"])
            if lost:
                dropped.append((rid, lost))
                continue
        if not args.dry_run:
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write(text)
        written += 1

    if dropped:
        for rid, lost in dropped:
            print(f"data/history/{rid}.json holds {len(lost)} event(s) this backfill cannot reproduce"
                  f" (first: {lost[0].get('date')} {lost[0].get('type')}); left untouched")
        if not args.force:
            raise SystemExit("stopped: rerun with --force to overwrite those files, or move them aside")

    stale = sorted(p[:-5] for p in os.listdir(HISTORY_DIR)
                   if p.endswith(".json") and p[:-5] not in history)
    for rid in stale:
        print(f"data/history/{rid}.json: no commit on {args.ref} has that id (not written)")

    events = sum(len(d["events"]) for d in history.values())
    dates = sorted({e["date"] for d in history.values() for e in d["events"]})
    print(f"{len(walked)} commits {walked[0][1]}..{walked[-1][1]} ({args.ref}) -> "
          f"{len(history)} history files, {events} events "
          f"({sum(1 for d in history.values() for e in d['events'] if e['type'] == 'added')} added, "
          f"{sum(1 for d in history.values() for e in d['events'] if e['type'] == 'updated')} updated, "
          f"{sum(1 for d in history.values() for e in d['events'] if e['type'] == 'removed')} removed)")
    verb = "would write" if args.dry_run else "wrote"
    print(f"{verb} {written} files, {unchanged} already up to date"
          + (f", {len(stale)} orphan files skipped" if stale else ""))


if __name__ == "__main__":
    main(sys.argv[1:])
