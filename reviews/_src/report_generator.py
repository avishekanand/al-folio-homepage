#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Conference-report generator — turns a JSON spec into a styled HTML report
that matches the house style (the "SIGIR/ICTIR 2026" look).

Usage:
    python3 report_generator.py report_data.json out.html

Design goal: you (or Claude) only ever produce the *data* (report_data.json).
The look — colours, layout, DOI/arXiv chips, print/PDF behaviour — is fixed
here so every report comes out consistent. Do not restyle per report; edit
this file if the house style itself needs to change.

See REPORT-STYLE-GUIDE.md for the schema, the voice, and the rules
(especially: never fabricate a DOI — verify via Crossref).
"""
import json, html, sys, re

# ----------------------------------------------------------------------
# HOUSE STYLE — do not fork per report. This is the single source of truth.
# ----------------------------------------------------------------------
CSS = """
  :root{--ink:#1a1a1a;--muted:#5b6470;--line:#e4e7ec;--accent:#1f5fb0;--accent-soft:#eef4fc;--bg:#fff;--chip:#f3f5f8;}
  *{box-sizing:border-box;}
  body{margin:0;background:#f6f7f9;color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;line-height:1.5;font-size:15px;}
  .sheet{max-width:880px;margin:24px auto;background:var(--bg);padding:44px 52px;box-shadow:0 1px 3px rgba(0,0,0,.08);border-radius:6px;}
  header.masthead{border-bottom:2px solid var(--ink);padding-bottom:14px;margin-bottom:22px;}
  .kicker{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);font-weight:700;}
  h1{font-size:25px;line-height:1.2;margin:6px 0 6px;}
  .dek{color:var(--muted);font-size:14.5px;margin:0;}
  .meta{margin-top:10px;font-size:12px;color:var(--muted);}
  h2.section{font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--accent);border-top:1px solid var(--line);padding-top:16px;margin:26px 0 12px;}
  .theme{margin:0 0 16px;}
  .theme h3{font-size:16px;margin:0 0 4px;display:flex;gap:9px;align-items:baseline;}
  .num{color:var(--accent);font-weight:800;font-variant-numeric:tabular-nums;}
  .theme p{margin:2px 0 6px;}
  .anchors{font-size:12.5px;color:var(--muted);}
  .anchors b{color:var(--ink);font-weight:600;}
  .tag{display:inline-block;font-size:10px;font-weight:700;letter-spacing:.04em;padding:1px 6px;border-radius:3px;vertical-align:middle;}
  .tag.sigir{background:#e7f0fb;color:#1f5fb0;}
  .tag.ictir{background:#fdeee2;color:#b5651d;}
  .tag.icml{background:#e6f4ea;color:#1b7f4b;}
  .tag.acl{background:#fce8e6;color:#b32b23;}
  .tag.generic{background:#eceff3;color:#4a5560;}
  .callout{background:var(--accent-soft);border-left:3px solid var(--accent);padding:12px 16px;border-radius:0 5px 5px 0;margin:18px 0;font-size:13.5px;}
  .callout b{color:var(--ink);}
  .appendix h2.section{border-top:2px solid var(--ink);}
  .grp{margin:16px 0 4px;}
  .grp h3{font-size:14.5px;margin:0 0 8px;color:var(--ink);background:var(--chip);padding:6px 10px;border-radius:4px;}
  ul.papers{list-style:none;margin:0 0 14px;padding:0;}
  ul.papers li{padding:6px 0;border-bottom:1px solid var(--line);font-size:13px;}
  ul.papers li:last-child{border-bottom:none;}
  .ptitle{font-weight:600;}
  .pnote{color:var(--muted);}
  a{color:var(--accent);text-decoration:none;}
  a:hover{text-decoration:underline;}
  a.doi,a.arx,a.url{font-size:10.5px;font-weight:700;letter-spacing:.03em;padding:1px 5px;border-radius:3px;white-space:nowrap;}
  a.doi{background:#eef4fc;color:#1f5fb0;}
  a.arx{background:#f0eafc;color:#6b3fa0;}
  a.url{background:#e6f4ea;color:#1b7f4b;}
  .addrl{font-size:10px;font-weight:700;letter-spacing:.03em;padding:1px 7px;margin-left:5px;border-radius:3px;border:1px solid var(--accent);background:transparent;color:var(--accent);cursor:pointer;white-space:nowrap;vertical-align:middle;line-height:1.5;}
  .addrl:hover{background:var(--accent);color:#fff;}
  .addrl.added{border-color:var(--line);color:var(--muted);cursor:default;}
  .addrl:disabled{cursor:default;opacity:.85;}
  @media print{.addrl{display:none !important;} }
  .sources{font-size:12px;color:var(--muted);}
  .sources a{word-break:break-word;}
  footer{margin-top:26px;border-top:1px solid var(--line);padding-top:12px;font-size:11.5px;color:var(--muted);}
  @media print{body{background:#fff;}.sheet{box-shadow:none;margin:0;max-width:none;padding:0 6px;border-radius:0;}.appendix{page-break-before:always;}a{color:var(--ink);} }
  @media(max-width:620px){.sheet{padding:26px 20px;margin:0;}h1{font-size:22px;} }
"""

# ----------------------------------------------------------------------
# "Add to reading list" behaviour — baked in so every report gets it.
# Reports are served from the same origin as the reading-list app
# (avishekanand.com/reviews/... and /reading/), so they share localStorage:
# this reads the token the reading app already stored and appends the paper
# to reading.json in the private reading-data repo via the GitHub Contents API.
# No token is entered here; connect once at /reading/ and every report can push.
# ----------------------------------------------------------------------
READING_LIST_JS = r"""<script>
(function(){
  "use strict";
  var LS_CONFIG = "readinglist.config";
  var LS_CACHE  = "readinglist.cache";
  var API = "https://api.github.com";

  function b64e(s){ return btoa(unescape(encodeURIComponent(s))); }
  function b64d(b){ return decodeURIComponent(escape(atob(String(b).replace(/\n/g, "")))); }
  function cfg(){ try{ return JSON.parse(localStorage.getItem(LS_CONFIG) || "null"); }catch(e){ return null; } }
  function headers(c){
    return {
      "Authorization": "Bearer " + c.token,
      "Accept": "application/vnd.github+json",
      "X-GitHub-Api-Version": "2022-11-28"
    };
  }
  function fileURL(c){
    var path = String(c.path || "reading.json").split("/").map(encodeURIComponent).join("/");
    return API + "/repos/" + encodeURIComponent(c.owner) + "/" + encodeURIComponent(c.repo) + "/contents/" + path;
  }
  function branch(c){ return c.branch || "main"; }
  function uid(){ return "p" + Date.now().toString(36) + Math.random().toString(36).slice(2, 7); }
  function nowISO(){ return new Date().toISOString(); }
  function keyOf(p){
    var d = String(p.doi || "").trim().toLowerCase();
    if(d) return "d:" + d;
    return "t:" + String(p.title || "").trim().toLowerCase();
  }
  function emptyData(){ return { meta:{ title:"Reading list", schema:1, updated:null }, papers:[], reports:[] }; }

  function toast(msg){
    var t = document.getElementById("rl-toast");
    if(!t){
      t = document.createElement("div");
      t.id = "rl-toast";
      t.style.cssText = "position:fixed;left:50%;bottom:20px;transform:translateX(-50%);background:#1a1a1a;color:#fff;padding:9px 15px;border-radius:8px;font-size:13px;z-index:9999;opacity:0;transition:opacity .2s;max-width:90%;text-align:center;";
      document.body.appendChild(t);
    }
    t.textContent = msg;
    t.style.opacity = ".96";
    clearTimeout(t._h);
    t._h = setTimeout(function(){ t.style.opacity = "0"; }, 2800);
  }

  function getFile(c){
    return fetch(fileURL(c) + "?ref=" + encodeURIComponent(branch(c)), { headers: headers(c) }).then(function(r){
      if(r.status === 404) return { data: emptyData(), sha: null };
      if(r.status === 401) throw new Error("token rejected 401");
      if(!r.ok) throw new Error("read " + r.status);
      return r.json().then(function(j){
        var d;
        try{ d = JSON.parse(b64d(j.content)); }catch(e){ d = emptyData(); }
        if(Array.isArray(d)) d = { meta:{}, papers:d, reports:[] };
        if(!d || typeof d !== "object") d = emptyData();
        if(!d.meta || typeof d.meta !== "object") d.meta = {};
        if(!Array.isArray(d.papers)) d.papers = [];
        if(!Array.isArray(d.reports)) d.reports = [];
        return { data: d, sha: j.sha };
      });
    });
  }
  function writeFile(c, data, sha){
    var body = {
      message: "Add paper from conference report",
      content: b64e(JSON.stringify(data, null, 2)),
      branch: branch(c)
    };
    if(sha) body.sha = sha;
    return fetch(fileURL(c), { method:"PUT", headers: headers(c), body: JSON.stringify(body) }).then(function(r){
      if(!r.ok) throw new Error("write " + r.status);
      return r.json().then(function(j){ return { sha: j.content && j.content.sha }; });
    });
  }

  function appendPaper(c, obj){
    var k = keyOf(obj);
    return getFile(c).then(function(g){
      if(g.data.papers.some(function(p){ return keyOf(p) === k; }))
        return { status:"exists", data:g.data, sha:g.sha };
      g.data.papers.push(obj);
      g.data.meta.updated = nowISO();
      return writeFile(c, g.data, g.sha).then(
        function(res){ return { status:"added", data:g.data, sha:res.sha }; },
        function(err){
          if(!/ (409|422)$/.test(err.message)) throw err;   // only retry on a stale-sha conflict
          return getFile(c).then(function(g2){
            if(g2.data.papers.some(function(p){ return keyOf(p) === k; }))
              return { status:"exists", data:g2.data, sha:g2.sha };
            g2.data.papers.push(obj);
            g2.data.meta.updated = nowISO();
            return writeFile(c, g2.data, g2.sha).then(function(res2){
              return { status:"added", data:g2.data, sha:res2.sha };
            });
          });
        }
      );
    });
  }

  var known = {};
  try{
    var cache = JSON.parse(localStorage.getItem(LS_CACHE) || "null");
    if(cache && cache.data && Array.isArray(cache.data.papers))
      cache.data.papers.forEach(function(p){ known[keyOf(p)] = 1; });
  }catch(e){}

  function mark(btn, text){ btn.disabled = true; btn.textContent = text; btn.classList.add("added"); }

  function add(btn){
    var c = cfg();
    if(!c || !c.owner || !c.repo || !c.token){
      toast("Open your reading list (/reading/) and connect a token first.");
      return;
    }
    var paper;
    try{ paper = JSON.parse(btn.getAttribute("data-paper")); }catch(e){ return; }
    var now = nowISO();
    var obj = {
      id: uid(),
      title: paper.title || "",
      venue: paper.venue || "",
      theme: paper.theme || "Unsorted",
      doi: paper.doi || "",
      arxiv: paper.arxiv || null,
      url: paper.url || "",
      note: paper.note || "",
      status: "to-read",
      summary: "",
      tags: [],
      added: now,
      updated: now
    };
    var orig = btn.textContent;
    btn.disabled = true;
    btn.textContent = "Adding...";
    appendPaper(c, obj).then(function(res){
      try{ localStorage.setItem(LS_CACHE, JSON.stringify({ data: res.data, sha: res.sha })); }catch(e){}
      known[keyOf(obj)] = 1;
      if(res.status === "exists"){ mark(btn, "In list"); toast("Already in your reading list."); }
      else{ mark(btn, "Added"); toast("Added to reading list: " + obj.theme); }
    }).catch(function(err){
      btn.disabled = false;
      btn.textContent = orig;
      toast("Couldn't add - " + (err.message || "error"));
    });
  }

  document.addEventListener("DOMContentLoaded", function(){
    var btns = document.querySelectorAll(".addrl");
    for(var i = 0; i < btns.length; i++){
      (function(b){
        try{
          var p = JSON.parse(b.getAttribute("data-paper"));
          if(known[keyOf(p)]) mark(b, "In list");
        }catch(e){}
        b.addEventListener("click", function(){ add(b); });
      })(btns[i]);
    }
  });
})();
</script>"""

def esc(s): return html.escape("" if s is None else str(s), quote=True)

def _venue_cls(v):
    v = (v or "").strip().lower()
    if v.startswith("sigir"): return "sigir"
    if v.startswith("ictir"): return "ictir"
    if v.startswith("icml"):  return "icml"
    if v.startswith("acl"):   return "acl"
    if v.startswith("arxiv"): return "arxiv"
    return "generic"

def _url_label(u):
    u = (u or "").lower()
    if "icml.cc" in u:                          return "ICML"
    if "openreview" in u:                       return "OpenReview"
    if "mlr.press" in u or "proceedings.mlr" in u: return "PMLR"
    if "aclanthology" in u:                     return "ACL"
    return "PDF"

def _chip_links(doi, arxiv, url=None):
    out = ""
    if doi:   out += '<a class="doi" href="%s">DOI</a>' % esc(doi)
    if url:   out += ' <a class="url" href="%s">%s</a>' % (esc(url), esc(_url_label(url)))
    if arxiv: out += ' <a class="arx" href="%s">arXiv</a>' % esc(arxiv)
    return out

def _inline_links(doi, arxiv, url=None):
    parts = []
    if doi:   parts.append('<a href="%s">DOI</a>' % esc(doi))
    if url:   parts.append('<a href="%s">%s</a>' % (esc(url), esc(_url_label(url))))
    if arxiv: parts.append('<a href="%s">arXiv</a>' % esc(arxiv))
    return " &middot; ".join(parts)

def _anchor(a):
    # a: {title, venue, doi?, arxiv?, url?}
    v = a.get("venue","")
    tag = ('<span class="tag %s">%s</span>' % (_venue_cls(v), esc(v))) if v else ""
    links = _inline_links(a.get("doi"), a.get("arxiv"), a.get("url"))
    links = (" (%s)" % links) if links else ""
    return "%s %s%s" % (esc(a.get("title","")), tag, links)

def _plain(s):
    """Strip tags/entities from a theme name -> the label used in the reading list."""
    s = re.sub(r"<[^>]+>", "", s or "")
    return html.unescape(s).strip()

def _venue_year(venue, year):
    """Conference short-form + year, e.g. 'SIGIR 2026'."""
    v = (venue or "").strip()
    if v and year: return v + " " + year
    return v or year

def _add_button(p, venue_year, theme_plain):
    """An 'add to my reading list' button carrying the paper as JSON in a data attribute."""
    payload = {
        "title":  p.get("title","") or "",
        "venue":  venue_year or "",
        "theme":  theme_plain or "Unsorted",
        "doi":    p.get("doi","") or "",
        "arxiv":  p.get("arxiv") or "",
        "url":    p.get("url","") or "",
        "note":   p.get("note","") or "",
    }
    return ('<button class="addrl" data-paper="%s" title="Add to my reading list">+ Reading list</button>'
            % esc(json.dumps(payload, ensure_ascii=False)))

def render(data):
    meta = data.get("meta", {})
    kicker = esc(meta.get("kicker",""))
    title  = esc(meta.get("title","Conference Report"))
    dek    = meta.get("dek","")            # HTML allowed (contains <em> etc.) -> not escaped
    metaln = meta.get("meta_html","")      # HTML allowed
    year   = str(data.get("year") or meta.get("year") or "").strip()  # e.g. "2026" -> "SIGIR 2026"

    # ---- one-pager shifts ----
    shifts_heading = esc(data.get("shifts_heading","The shifts that matter"))
    shifts_html = []
    for s in data.get("shifts", []):
        anchors = " &middot; ".join(_anchor(a) for a in s.get("anchors", []))
        shifts_html.append(
            '  <div class="theme">\n'
            '    <h3><span class="num">%s</span> %s</h3>\n'
            '    <p>%s</p>\n'
            '    <p class="anchors"><b>Anchors:</b> %s</p>\n'
            '  </div>' % (esc(s.get("n","")), esc(s.get("heading","")), s.get("prose",""), anchors)
        )
    shifts_block = "\n".join(shifts_html)

    # ---- optional quieter thread ----
    thread = data.get("thread")
    thread_block = ""
    if thread:
        thread_block = ('\n  <h2 class="section">%s</h2>\n  <p style="margin-top:0;font-size:13.5px;">%s</p>'
                        % (esc(thread.get("heading","")), thread.get("html","")))

    # ---- appendix ----
    app = []
    n_by_venue = {}
    for t in data.get("themes", []):
        app.append('  <div class="grp">\n    <h3>%s &middot; %s</h3>\n    <ul class="papers">'
                   % (esc(t.get("num","")), esc(t.get("name",""))))
        theme_plain = _plain(t.get("name",""))
        for p in t.get("papers", []):
            v = p.get("venue","")
            n_by_venue[v] = n_by_venue.get(v,0)+1
            tag = ('<span class="tag %s">%s</span> ' % (_venue_cls(v), esc(v))) if v else ""
            btn = _add_button(p, _venue_year(v, year), theme_plain)
            app.append('      <li>%s<span class="ptitle">%s</span> — '
                       '<span class="pnote">%s</span> %s %s</li>'
                       % (tag, esc(p.get("title","")), esc(p.get("note","")),
                          _chip_links(p.get("doi"), p.get("arxiv"), p.get("url")), btn))
        app.append('    </ul>\n  </div>')
    appendix_block = "\n".join(app)
    n_total = sum(n_by_venue.values())

    callout = data.get("takeaway","")
    app_dek = data.get("appendix_dek","")
    sources_html = data.get("sources_html","")
    method_html = data.get("method_html","")
    foot1 = data.get("footer_onepager","Every paper cited here links to its DOI. Full appendix follows.")
    foot2 = data.get("footer_appendix","")

    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%(title)s</title>
<style>%(css)s</style>
</head>
<body>
<div class="sheet">
  <header class="masthead">
    <div class="kicker">%(kicker)s</div>
    <h1>%(title)s</h1>
    <p class="dek">%(dek)s</p>
    <div class="meta">%(metaln)s</div>
  </header>

  <div class="callout">%(callout)s</div>

  <h2 class="section">%(shifts_heading)s</h2>

%(shifts_block)s
%(thread_block)s

  <footer>%(foot1)s</footer>
</div>

<div class="sheet appendix">
  <header class="masthead">
    <div class="kicker">Appendix</div>
    <h1>%(app_title)s</h1>
    <p class="dek">%(app_dek)s</p>
  </header>

%(appendix_block)s

  <h2 class="section">Sources &amp; method note</h2>
  <p class="sources">%(sources_html)s</p>
  <p class="sources" style="margin-top:10px;">%(method_html)s</p>
  <footer>%(foot2)s</footer>
</div>
%(rl_script)s
</body>
</html>
""" % dict(
        title=title, css=CSS, kicker=kicker, dek=dek, metaln=metaln,
        callout=callout, shifts_heading=shifts_heading, shifts_block=shifts_block,
        thread_block=thread_block, foot1=esc(foot1),
        app_title=esc(data.get("appendix_title","The full list, grouped the way I sorted it")),
        app_dek=app_dek, appendix_block=appendix_block,
        sources_html=sources_html, method_html=method_html, foot2=esc(foot2),
        rl_script=READING_LIST_JS,
    )

if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "report_data.json"
    out = sys.argv[2] if len(sys.argv) > 2 else "report.html"
    with open(src, encoding="utf-8") as f:
        data = json.load(f)
    htmlout = render(data)
    with open(out, "w", encoding="utf-8") as f:
        f.write(htmlout)
    n = sum(len(t.get("papers", [])) for t in data.get("themes", []))
    print("Wrote %s — %d themes, %d papers." % (out, len(data.get("themes", [])), n))
