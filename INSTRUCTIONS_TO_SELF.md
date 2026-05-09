# Instructions to self — hosting an HTML talk on the homepage

This file is excluded from the Jekyll build (see `_config.yml` `exclude:` list)
and is **not** published anywhere on `avishekanand.com`. Edit freely.

The homepage is built by Netlify on every push to `main`. The talks dropdown
lives under the **submenus** menu, with `_pages/talks.md` as the landing page.

---

## Quick recipe — add a new HTML talk

Assume the source is a self-contained Marp/HTML deck plus its asset folders,
e.g. on the slides machine:

```
~/slides/<talk-slug>/
├── <talk-slug>.html
├── <talk-slug>.pdf            (optional — for a PDF download link)
├── <talk-slug>-diagrams/      (.svg files)
└── figs/                      (.png/.pdf referenced from the HTML)
```

You only need what `<talk-slug>.html` references. You do **not** need the
`.md` source, the `bib/`, `_anim/` PDFs, or per-step `.pdf` files.

### 1. Copy the talk into the repo

```bash
cd ~/Projects/al-folio-homepage/al-folio-homepage
cp -R ~/slides/<talk-slug> assets/html/<talk-slug>
```

The folder must live under `assets/html/`. Jekyll serves everything in
`assets/` as-is; no extra config needed.

### 2. Sanity-check the asset references

Open `assets/html/<talk-slug>/<talk-slug>.html` and confirm the `src=`/`href=`
paths are **relative** (e.g. `<talk-slug>-diagrams/foo.svg`, `figs/bar.png`).
Absolute paths from the slides machine will break.

```bash
grep -oE 'src="[^"]*"|href="[^"]*"' \
  assets/html/<talk-slug>/<talk-slug>.html | sort -u | head
```

### 3. Add an entry to the talks page

Edit `_pages/talks.md` and add a `<li>` under the right year heading.
Use the `relative_url` filter so `jekyll-minifier` doesn't strip the
`.html` extension (it will, otherwise — found this out the hard way):

```markdown
<li>
  <strong>Talk title</strong><br>
  <a href="{{ '/assets/html/<talk-slug>/<talk-slug>.html' | relative_url }}">View slides (HTML)</a>
  &nbsp;·&nbsp;
  <a href="{{ '/assets/html/<talk-slug>/<talk-slug>.pdf' | relative_url }}">PDF</a>
</li>
```

If the talk has no slides URL yet, just include the `<strong>title</strong>`
line — you can add links later.

### 4. (Optional) Add a news entry

For visibility on the homepage, add a file to `_news/` like:

```markdown
---
layout: post
date: YYYY-MM-DD 00:00:00-0000
inline: true
related_posts: false
---

🎤 New talk: [Talk title]({{ '/assets/html/<talk-slug>/<talk-slug>.html' | relative_url }})
```

### 5. Commit and push

```bash
git add assets/html/<talk-slug> _pages/talks.md _news/<entry>.md
git commit -m "Add <talk-slug> talk"
git push origin main
```

Netlify rebuilds automatically. The talk is live at:

- `https://avishekanand.com/assets/html/<talk-slug>/<talk-slug>.html`
- `https://avishekanand.com/assets/html/<talk-slug>/<talk-slug>.pdf`
- listed under `https://avishekanand.com/talks/`

---

## Where the navbar dropdown is configured

`_pages/dropdown.md` controls the **submenus** menu. To add or reorder
children:

```yaml
children:
  - title: publications
    permalink: /publications/
  - title: divider
  - title: talks
    permalink: /talks/
  - title: divider
  - title: projects
    permalink: /projects/
  - title: divider
  - title: blog
    permalink: /blog/
```

`title: divider` renders the horizontal separator between groups.

---

## Deployment notes

- **Where it deploys from**: Netlify, on `push` to `main`. Not GitHub Pages
  (the repo's `pages-build-deployment` workflow is broken — `Unknown tag 'toc'` —
  and `deploy.yml` also fails on a `Gemfile.lock` platform mismatch). Both are
  red on every push and can be ignored as long as Netlify is green.
- **Custom domain**: `avishekanand.com` is served from Netlify (not from
  `avishekanand.github.io/al-folio-homepage`). No `CNAME` file in the repo.
- **Cache**: Netlify edge caches the HTML; if a change isn't visible after
  ~2 min, hard-refresh or hit `https://www.avishekanand.com/?cb=$(date +%s)`
  to bust the cache.

---

## Single-file alternative (no asset folders)

If you'd rather upload one self-contained file with no folders:

```bash
cd ~/slides/<talk-slug>
brew install monolith    # one-time
monolith <talk-slug>.html -o <talk-slug>-bundled.html
```

`<talk-slug>-bundled.html` has every image base64-inlined. Copy it into
`assets/html/` and link to it directly — no companion folders needed.
