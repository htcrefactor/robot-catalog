## What is missing

`table.html` and `specs.html` already carry the "Maker-verified only" toggle (`verified_only`, `verified_n`), but the home page (`index.html`) — the first screen a visitor sees — has no way to narrow the grid to records checked against a maker source, and no badge telling a visitor that a card's values are unconfirmed.

## Plan

- Add the same "Maker-verified only" checkbox to the home grid controls, sharing the state in the URL (`ver=1`) like the page's other filters, so a verified-only view can be linked.
- Show the existing `pv_unconfirmed` label on a card whose record is not `verification: official`, with the tooltip already defined (`pv_unchecked_t` / `pv_unconfirmed_t`).
- Reuse existing i18n keys (EN + KO), no new strings.
- No scoring, no ranking, no change to the data schema.
