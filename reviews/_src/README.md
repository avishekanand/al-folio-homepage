# Conference reports pipeline

Generates the report pages in `../` (SIGIR/ICTIR, ICML, ACL) and the cross-conference
**by-topic** view. The same build runs at deploy time, so the published pages always
match these sources.

## Files
- `topics.json` — **canonical research-topic taxonomy** (topics, interest tiers, and the
  alias names a report may use for each topic). Single source of truth.
- `topics_page.json` — one-pager prose for the by-topic view.
- `<venue>_<year>_data.json` — one per conference report. `"output"` → regenerated;
  `"aggregate_only": true` (e.g. SIGIR, authored elsewhere) → only feeds the by-topic view.
- `report_generator.py` — house-style HTML renderer (don't restyle per report).
- `build_topics.py` — the orchestrator.
- `RESEARCH-TOPICS.md` — **generated** from `topics.json` (don't hand-edit).

## Add a conference (the whole idea)
1. Author `reviews/_src/<venue>_<year>_data.json`, naming each **appendix theme** from
   `topics.json` (its `name` or an `alias`) so every paper is classified into the shared
   topic taxonomy. Need a genuinely new topic? Add it to `topics.json` first.
2. `python3 reviews/_src/build_topics.py --out reviews` (or just push — CI does it).
   Regenerates the report **and** the by-topic view in the house style; **fails loudly**
   if a theme isn't a known topic, so the topic view can't drift.
3. Commit & push.

## Commands
    python3 reviews/_src/build_topics.py --out reviews           # build everything
    python3 reviews/_src/build_topics.py --out reviews --check   # dry-run: fail if stale/unmapped
