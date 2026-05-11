# Visual System — From Pipelines to Self-Improving Retrieval

19 figures for the Booking talk, one per substantive slide. All hand-written SVG, sized 1100×720 to match the marp 16:9 aspect.

Each figure is shipped in three formats:

- `.svg` — editable source, vector
- `.pdf` — vector, ready for LaTeX `\includegraphics`
- `.png` — 1100px raster, for slide-deck preview or markdown

If you need to regenerate the PDFs after editing an SVG:

```bash
# any of these work:
rsvg-convert -f pdf -o file.pdf file.svg
inkscape file.svg --export-type=pdf
cairosvg file.svg -o file.pdf
```

For LaTeX:

```latex
\includegraphics[width=\textwidth]{slide_p20_quam_architecture.pdf}
```

For PowerPoint / Keynote / Google Slides: insert the PDF directly, or use the SVG (modern PowerPoint supports SVG natively). PNGs are a fallback.

## Visual system

**Palette (5 colors, no others):**

| Token | Hex | Usage |
|---|---|---|
| `paper` | `#faf7f2` | Background everywhere |
| `ink` | `#1a1a1a` | Primary text, axes, neutral boxes |
| `muted` | `#6b665e` | Secondary text, captions |
| `accent` | `#c8553d` | Protagonist signal — feedback loops, "thing to notice", hero numbers |
| `cool` | `#2a4747` | Reference / upper-bound / "good evidence" / teacher signals |
| `gray` | `#b8b3a8` / `#8a857a` | Baselines, de-emphasized comparisons, candidate pools |

**Typography:** Single serif stack `Georgia, 'Times New Roman', serif`.

- Title: 32–34px regular, letter-spacing 0.2
- Italic subtitle: 16–17px italic, letter-spacing 0.3
- Body callout: 13–15px
- Small-caps category labels: 11–13px bold, letter-spacing 0.5–2.0
- Numeric labels: 11–12px

**Recurring elements:**

- Short underline below titles: `<line x1="80" y1="128" x2="200" y2="128" stroke="#1a1a1a" stroke-width="1.2"/>`
- Footer mark: same line in accent (terracotta, width 1.5) preceding the closing argument
- Subtle grid lines: `#e8e2d6` for chart backgrounds
- Box corner radius: 4px
- No gradients, no shadows, no glows

**Arrow grammar:**

- Solid black 2.0–2.4 stroke = inference / forward flow
- Dashed accent 2.4–3.0 stroke (`stroke-dasharray="8,5"` or `9,5`) = training / feedback / return paths
- Custom triangular markers, sharp-tipped, sized to clear destination boundaries

## Slide index — in PDF page order

| File | PDF page | Type | What it shows |
|---|---|---|---|
| `slide_p02_industry` | 2 | typographic | Industry track record — Amazon, Factiverse, Internet Archive |
| `slide_p08_travel_query` | 8 | mockup | Three-step travel query evolution within a session |
| `slide_p10_cascade_pipeline` | 10 | architecture | Standard 4-stage retrieval pipeline with top-1000 candidate pool |
| `slide_p11_cascade_failure` | 11 | architecture | Same pipeline; one relevant doc dropped before reranking (the failure mode) |
| `slide_p12_recall_at_k` | 12 | result chart | Three recall curves: cascade · cascade+feedback · oracle |
| `slide_p16_reform_estim_matrix` | 16 | concept | 2×2 reformulation × estimator with diagonal sweet-spot band |
| `slide_p18_embedding_vs_doc` | 18 | concept | Retriever sees a vector; reranker reads the document |
| `slide_p20_quam_architecture` | 20 | architecture | QUAM affinity-graph flow with anchor/neighbor nodes and reranker feedback |
| `slide_p21_quam_results` | 21 | result chart | QUAM Recall@50 (+12%) and Recall@1000 (+26%) bars |
| `slide_p22_synthesis` | 22 | concept | Three perspectives → one principle ("feedback turns one-shot into process") |
| `slide_p28_sunar_flow` | 28 | architecture | SUNAR with semantic-clustering uncertainty signal |
| `slide_p29_sunar_results` | 29 | result chart | SUNAR vs SELF-ASK / ReAct / SearChain on 2WikiMultihopQA & MuSiQue |
| `slide_p30_ore_flow` | 30 | architecture | ORE candidate pool with feature vectors → linear bandit → ranker |
| `slide_p31_ore_results` | 31 | result chart | Two charts: speedup (2×, 9×) and recall improvement (+30%, +58%) |
| `slide_p35a_case_concept` | 35a | concept | LinGapE dense edge-web vs CASE sparse comparison via challenger shortlist |
| `slide_p35b_case_convergence` | 35b | result chart | Convergence curves: CASE vs LinGIFA vs LinGapE, gap-index decay |
| `slide_p36_case_7x` | 36 | callout | "7× fewer LLM calls" headline number with dot-comparison |
| `slide_p39_autoir_path` | 39 | concept | Concentric loops: feedback (inner) · bridge · self-play (outer) |
| `slide_p43_self_play_loop` | 43 | architecture | The self-play closed loop — personas → inner loop → updated system → new behavior |

## Note on numeric values

All numerical results in result charts (recall percentages, F1 scores, speedup factors) are **placeholder values consistent with the slide text**, chosen to match plausible IR benchmark behavior. Each SVG has comments documenting the values and the formula used to convert values to bar heights or curve positions. To swap in real paper data, edit the SVG directly:

- For bars: change the `value` and recompute `y = base - scale * value` (formula in comments)
- For curves: edit the path `d=` attribute or regenerate via the small Python script noted in the SVG header

## Changes since first delivery

- **`slide_p20_quam_architecture` was rebuilt** to match the marp deck's actual concept (Query Affinity Modelling — a learned co-relevance graph). The previous version showed a different, generic "approximation model" pipeline.
- Overlap fixes applied to: cascade pipeline (legend repositioned outside dashed pool), reformulation matrix (quadrant labels relocated off the diagonal band), ORE flow (feedback arrow rerouted, α value labels cleared from bars), self-play loop (badge moved above terracotta-filled inner-loop circle), industry slide (INTERNET / ARCHIVE stacked on two lines).
