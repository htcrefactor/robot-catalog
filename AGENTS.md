# AGENTS.md — rules for every agent working on Robot Catalog

Several AI agents (Hark, Codex, Claude Code and others) work on this repo at once. Coordination happens in **GitHub Issues**. Read this file before touching anything.

## 1. Claim before you work
- Pick an open issue labelled `status:ready`. Never work on a task that has no issue; open one first.
- Claim it: comment `Claimed by <agent-name>` and swap `status:ready` for `status:in-progress`. If someone else already claimed it, choose another issue.
- One agent per issue. Large tasks are split into batch issues (for example, verification batches by id range); claim one batch, not the whole list.
- A claim older than 48 hours with no commit or comment can be taken over. Comment first.
- When you're done, open a PR that says `Closes #N`, then set `status:review`. If you're blocked, set `status:blocked` and explain why in a comment.

## 2. Ownership of data files
- Source of truth: `data/parts/*.json` (one file per category, plus `misc.json`). `data/robots.json` and `sitemap.xml` are **generated**; never edit them by hand.
- After changing parts, run `python3 scripts/merge.py --notes "<what changed>"`, `python3 scripts/build_sitemap.py` and `python3 scripts/validate.py`. CI (.github/workflows/validate.yml) runs the same check on every PR and blocks an unexplained drop in robot count (add the label `count-drop-ok` only for an explained merge or move).
- **Edit records by `id` only.** Never replace a whole parts file with an older or remote copy. Merge by id. On 2026-11-15, 734 records were lost when a sync overwrote local files.
- **Count check:** record the robot count before and after your change and put both numbers in the PR. Any drop must be explained (a merge or a move), never accidental.
- Keep PRs small and focused on one issue. Rebase on `main` before opening the PR.

## 3. Data rules (from the owner)
- **Scope:** mobile robots only. Categories are AMR, AGV, Humanoid, Quadruped, Wheel-legged, Indoor delivery, Outdoor delivery, Mobile platform and Misc.
- **Excluded:** arms, cobots, hands, exoskeletons, vacuums, lawn, pool and window robots, drones, toys, cars and robotaxis, and static or companion robots.
- **Misc:** a robot a competitor lists that isn't a standalone mobile robot goes to `misc.json` with `original_category` and `misc_reason`. Don't delete it.
- **Include every in-scope model any competitor lists**, even if its spec fields stay empty.
- **Specs come from official maker sources only:** the maker's site, datasheet, press release, manual or lab paper. Never fill a field from a competitor or aggregator. If no official value exists, leave the field empty.
- **Conflicts:** keep the official maker value and record the other value in `notes`.
- **`verification`:** use `official` (checked against a maker source), `unconfirmed` (no maker source found) or `null` (unchecked). Never drop an unconfirmed record; keep it and mark it.
- **Derived values** (for example Wh computed as V×Ah) must say so in `notes`.
- **Duplicates or variants:** keep one record and add the other as an entry in its `variants` list (see Walker X / Panda Robot).
- Every changed record lists its URLs in `sources`.
- No scoring or ranking fields. Comparison features are deferred.

## 4. Site code
- Static site: `index.html`, `robot.html`, `table.html`, `specs.html`, `dashboard.html`, `changelog.html` and `assets/*.js`. No build step besides the scripts above.
- Every UI string goes in `assets/i18n.js` in both EN and KO.
- Categories are defined in `assets/app.js` (`CATS`, `CAT_COLORS`) and their KO labels in `VALUE_KO`.

## 5. Hark's scheduled jobs
Hark runs automated jobs on this data: a daily sweep at 12:00 KST and verification batches. Issues they own are labelled `agent:hark`. Don't claim those issues.
