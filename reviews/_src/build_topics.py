#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_topics.py — keep the conference reports and the cross-conference
"by topic" view consistent, and generate RESEARCH-TOPICS.md.

What it does, from the source files next to it:
  - topics.json          canonical taxonomy (topics, tiers, aliases)  [source of truth]
  - topics_page.json     one-pager content for the by-topic view
  - <venue>_..._data.json  one per conference report (auto-discovered)

It will:
  1. Map every report's appendix themes -> a canonical topic (by name or alias,
     ignoring case / spacing / &-vs-&amp;). It FAILS LOUDLY if any theme is
     unmapped, so adding a conference can never silently create an orphan topic.
  2. Regenerate each report that declares an "output" (via report_generator).
  3. Aggregate every report's papers by canonical topic (dedup by title),
     core topics first then peripheral, and render the by-topic page.
  4. Regenerate RESEARCH-TOPICS.md from topics.json so the doc can't drift.

Usage:
  python3 build_topics.py [--out DIR] [--check]
    --out DIR   where to write the .html (default: alongside the sources)
    --check     don't write; exit 1 if any output would change or a theme is
                unmapped (use in CI to gate a push)

Only the Python standard library + report_generator.py are needed.
"""
import os, sys, json, glob, re, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import report_generator as rg   # noqa: E402

# fields that report_generator HTML-escapes (must hold raw text, not entities)
_ESC_TOP = ["shifts_heading", "appendix_title", "appendix_dek",
            "footer_onepager", "footer_appendix"]

def norm(s):
    """Normalize a theme name for matching: lowercase, &amp;->&, collapse spaces."""
    s = (s or "").replace("&amp;", "&")
    return re.sub(r"\s+", " ", s).strip().lower()

def deentity(s):
    return s.replace("&amp;", "&") if isinstance(s, str) else s

def fix_escaped(d):
    """Defensively de-double-escape the auto-escaped fields of a report dict."""
    m = d.get("meta", {})
    for k in ("kicker", "title"):
        if k in m: m[k] = deentity(m[k])
    for k in _ESC_TOP:
        if k in d: d[k] = deentity(d[k])
    for s in d.get("shifts", []):
        s["heading"] = deentity(s.get("heading", ""))
        for a in s.get("anchors", []):
            a["title"] = deentity(a.get("title", ""))
    if d.get("thread"):
        d["thread"]["heading"] = deentity(d["thread"].get("heading", ""))
    for t in d.get("themes", []):
        t["name"] = deentity(t.get("name", ""))
        for p in t.get("papers", []):
            p["title"] = deentity(p.get("title", ""))
            if "note" in p: p["note"] = deentity(p["note"])
    return d

def load_taxonomy():
    tx = json.load(open(os.path.join(HERE, "topics.json"), encoding="utf-8"))
    topics = tx["topics"]
    name2key = {}
    for t in topics:
        for nm in [t["name"]] + t.get("aliases", []):
            name2key[norm(nm)] = t["key"]
    by_key = {t["key"]: t for t in topics}
    order = [t["key"] for t in topics]          # taxonomy order
    return tx, topics, by_key, name2key, order

# files that match *_data.json but are NOT conference report sources
_NOT_REPORTS = {"topics_page.json", "topics_data.json"}

def discover_reports():
    """All *_data.json next to this script (the per-conference sources)."""
    out = []
    for p in sorted(glob.glob(os.path.join(HERE, "*_data.json"))):
        if os.path.basename(p) in _NOT_REPORTS:
            continue
        out.append(p)
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=HERE)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    tx, topics, by_key, name2key, order = load_taxonomy()
    reports = discover_reports()
    if not reports:
        sys.exit("no *_data.json reports found next to build_topics.py")

    # ---- 1. load reports, map themes, collect aggregation ----
    buckets = {t["key"]: [] for t in topics}
    seen = set()
    unmapped = {}            # theme -> [report files]
    loaded = []              # (path, dict)
    for path in reports:
        d = fix_escaped(json.load(open(path, encoding="utf-8")))
        loaded.append((path, d))
        for t in d.get("themes", []):
            key = name2key.get(norm(t.get("name", "")))
            if key is None:
                unmapped.setdefault(t.get("name", ""), []).append(os.path.basename(path))
                continue
            for p in t.get("papers", []):
                tk = norm(p.get("title", ""))
                if not tk or tk in seen:
                    continue
                seen.add(tk)
                buckets[key].append({k: v for k, v in p.items() if v})

    if unmapped:
        print("ERROR: report themes not found in topics.json (add the topic or an alias):",
              file=sys.stderr)
        for name, files in sorted(unmapped.items()):
            print("  - %r  (in %s)" % (name, ", ".join(sorted(set(files)))), file=sys.stderr)
        sys.exit(2)

    changed = []

    def emit(html_str, out_name):
        dest = os.path.join(args.out, out_name)
        old = open(dest, encoding="utf-8").read() if os.path.exists(dest) else None
        if old != html_str:
            changed.append(out_name)
            if not args.check:
                open(dest, "w", encoding="utf-8").write(html_str)

    # ---- 2. regenerate each report that declares an output ----
    for path, d in loaded:
        if d.get("output"):
            emit(rg.render(d), d["output"])

    # ---- 3. build the by-topic view ----
    page = json.load(open(os.path.join(HERE, "topics_page.json"), encoding="utf-8"))
    core = [k for k in order if by_key[k]["tier"] == "core"]
    peri = [k for k in order if by_key[k]["tier"] == "peripheral"]
    themes = []
    n = 0
    for key in core + peri:
        ps = buckets[key]
        if not ps:
            continue
        n += 1
        t = by_key[key]
        ps.sort(key=lambda p: (p.get("venue", ""), p.get("title", "").lower()))
        name = t["name"]
        if t["tier"] == "peripheral":
            name += " &nbsp;·&nbsp; <span style=\"font-weight:400;color:var(--muted)\">less central</span>"
        themes.append({"num": str(n), "name": name, "papers": ps})
    page["themes"] = themes
    emit(rg.render(page), page.get("output", "by-topic.html"))
    total = sum(len(buckets[k]) for k in buckets)

    # ---- 4. regenerate RESEARCH-TOPICS.md from topics.json ----
    md = render_topics_md(tx)
    md_path = os.path.join(HERE, "RESEARCH-TOPICS.md")
    old = open(md_path, encoding="utf-8").read() if os.path.exists(md_path) else None
    if old != md:
        changed.append("RESEARCH-TOPICS.md")
        if not args.check:
            open(md_path, "w", encoding="utf-8").write(md)

    # ---- report ----
    print("reports: %d | topics with papers: %d | unique papers: %d"
          % (len(reports), n, total))
    if args.check:
        if changed:
            print("OUT OF DATE (run build_topics.py): " + ", ".join(changed), file=sys.stderr)
            sys.exit(1)
        print("check: everything up to date.")
    else:
        print("wrote: " + (", ".join(changed) if changed else "(no changes)"))

def render_topics_md(tx):
    L = []
    L.append("# Research topics — the taxonomy I sort conferences into")
    L.append("")
    L.append("> **Generated from `topics.json` by `build_topics.py` — do not edit by hand.** "
             "Edit `topics.json`, then run the build.")
    L.append("")
    L.append("A single, reusable list of the research directions I track, each with a one- or two-line "
             "note on *why I care*. The conference reports name their appendix themes from this list "
             "(or an alias below), and the cross-conference [`by-topic view`](/reviews/by-topic.html) "
             "is aggregated from it.")
    L.append("")
    L.append("Tags: **[IR]** retrieval venues · **[ML]** ICML/NeurIPS-style · **[NLP]** ACL/EMNLP-style. "
             "**○ peripheral** = tracked but weighted down (kept, not dropped). Override: methods that "
             "transfer to ranking — distillation, learnt/dense representations — stay core.")
    L.append("")
    L.append("---")
    secs = tx["sections"]
    topics = tx["topics"]
    # display in section order A,B,C,D,E then by numeric part of key
    def keynum(k):
        m = re.search(r"\d+", k)
        return int(m.group()) if m else 0
    for sec in ["A", "B", "C", "D", "E"]:
        st = [t for t in topics if t["section"] == sec]
        if not st:
            continue
        st.sort(key=lambda t: keynum(t["key"]))
        L.append("")
        L.append("## %s. %s" % (sec, secs[sec]))
        L.append("")
        for t in st:
            tags = "".join("[%s]" % x for x in t.get("tags", []))
            mark = " · **○ peripheral**" if t["tier"] == "peripheral" else ""
            L.append("%d. **%s** — %s%s" % (keynum(t["key"]), t["name"], tags, mark))
            L.append("   %s" % t["desc"])
            if t.get("aliases"):
                L.append("   <br><sub>report aliases: %s</sub>"
                         % "; ".join("“%s”" % a for a in t["aliases"]))
            L.append("")
    L.append("---")
    L.append("")
    L.append("### Adding a conference")
    L.append("1. Write `<venue>_<year>_data.json` next to `build_topics.py`, naming each appendix "
             "theme from the list above (or add an alias to `topics.json`).")
    L.append("2. Run `python3 build_topics.py` — it regenerates the report, the by-topic view and this "
             "file, and **fails** if any theme isn't a known topic.")
    L.append("3. Commit. CI rebuilds and redeploys.")
    L.append("")
    return "\n".join(L)

if __name__ == "__main__":
    main()
