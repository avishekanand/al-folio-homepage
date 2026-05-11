#!/usr/bin/env python3
"""
Strip slide chrome (title + footer) from SVGs and write figure-only versions.
Adjusts viewBox to crop empty title/footer margins.
"""

import os
import re
import sys

SRC_DIR = "/Users/avishekanand/slides/booking-2026/booking-diagrams"
OUT_DIR = os.path.join(SRC_DIR, "figures")

os.makedirs(OUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Helper: remove a complete SVG element (text or self-closing) anchored at pos
# ---------------------------------------------------------------------------

def _find_text_elements(txt):
    """Return list of (start, end) spans for all <text>...</text> elements."""
    pattern = re.compile(r'<text\b(?:[^>]|\n)*?>(?:.*?)</text>', re.S)
    return [(m.start(), m.end(), m.group(0)) for m in pattern.finditer(txt)]

def _find_selfclosing_lines(txt):
    """Return list of (start, end, content) for all <line .../> elements."""
    pattern = re.compile(r'<line\b[^/]*/>', re.S)
    return [(m.start(), m.end(), m.group(0)) for m in pattern.finditer(txt)]


def strip_chrome(content: str, filename: str) -> str:
    """Remove title block, footer block, adjust viewBox."""

    raw = content

    # -----------------------------------------------------------------------
    # Pass 1: Remove title block.
    #
    # The title block is 2-3 elements at the TOP of the body (after the <rect>
    # background):
    #   (a) A large <text> element with font-size >= 26 and y < 130
    #   (b) An italic <text> element with y < 145  (subtitle)
    #   (c) A short <line> underline with y1=y2 < 145 and x2-x1 <= 200
    #
    # Some files put these inside a <!-- TITLE --> comment block.
    # -----------------------------------------------------------------------

    def remove_title_block(txt):
        # Build index of text elements
        texts = _find_text_elements(txt)
        title_idx = None
        for idx, (start, end, el) in enumerate(texts):
            ym = re.search(r'\by\s*=\s*["\'](\d+(?:\.\d+)?)["\']', el)
            fm = re.search(r'font-size\s*=\s*["\'](\d+(?:\.\d+)?)["\']', el)
            if ym and fm:
                y = float(ym.group(1))
                fs = float(fm.group(1))
                if y < 130 and fs >= 26:
                    title_idx = idx
                    break

        if title_idx is None:
            return txt  # no title found; skip removal

        # Remove elements from right to left to keep indices valid
        to_remove = []

        # (a) title text
        to_remove.append((texts[title_idx][0], texts[title_idx][1]))

        # (b) scan forward for italic subtitle at y < 145
        remaining = txt
        # We'll do a fresh scan after removal for cleanliness
        # Collect positions of subtitle and underline based on character offsets
        # in the ORIGINAL string
        sub_found = False
        sub_start = sub_end = -1
        ul_start = ul_end = -1

        for idx2, (start2, end2, el2) in enumerate(texts):
            if idx2 <= title_idx:
                continue
            ym2 = re.search(r'\by\s*=\s*["\'](\d+(?:\.\d+)?)["\']', el2)
            if ym2 and float(ym2.group(1)) < 145:
                if re.search(r'font-style\s*=\s*["\']italic["\']', el2, re.I):
                    sub_found = True
                    sub_start, sub_end = start2, end2
                    to_remove.append((start2, end2))
                    break

        # (c) find decorative underline <line>
        lines = _find_selfclosing_lines(txt)
        for (ls, le, lel) in lines:
            attrs = dict(re.findall(r'\b(x1|y1|x2|y2)\s*=\s*["\']([^"\']+)["\']', lel))
            try:
                y1 = float(attrs.get('y1', 999))
                y2 = float(attrs.get('y2', 999))
                x1 = float(attrs.get('x1', 0))
                x2 = float(attrs.get('x2', 999))
                if y1 == y2 and y1 < 145 and (x2 - x1) <= 200:
                    # make sure it's not a marker-end arrow line
                    if 'marker-end' not in lel:
                        to_remove.append((ls, le))
                        break
            except (ValueError, KeyError):
                pass

        # Remove sorted by position (largest offset first to avoid index drift)
        to_remove.sort(key=lambda x: x[0], reverse=True)
        for (s, e) in to_remove:
            txt = txt[:s] + txt[e:]

        return txt

    raw = remove_title_block(raw)

    # -----------------------------------------------------------------------
    # Pass 2: Remove footer block.
    #
    # Strategy A: comment-delimited blocks.
    #   Matches: <!-- FOOTER ... -->  or  <!-- ===...\n   FOOTER\n   ===... -->
    #   or <!-- footer --> etc.
    #
    # Strategy B: fallback — remove footer marker line + footer text.
    #   Footer marker line: short <line> (x2-x1 <= 200), y1 >= 600,
    #     no marker-end, stroke="#c8553d"
    #   Footer text: <text> at y >= 655 with x < 200 (left-aligned)
    #   We use y >= 655 to avoid stripping chart axis labels (y=605-648) and
    #   pipeline diagram labels (y=643).
    # -----------------------------------------------------------------------

    # 2A: Comment-delimited footer blocks.
    # Handles all these comment styles:
    #   <!-- FOOTER -->
    #   <!-- FOOTER MARK + CLOSING -->
    #   <!-- footer -->
    #   <!-- ============\n       FOOTER LINE\n       ============ -->
    #   <!-- ===== FOOTER ===== -->
    raw = re.sub(
        r'<!--[=\s]*(?:FOOTER[^-]*|footer)[^-]*-->.*?(?=<!--|</svg>|$)',
        '',
        raw,
        flags=re.S | re.I
    )

    # 2B: Fallback — remove any remaining footer-like elements.
    def remove_footer_fallback(txt):
        # Remove short footer marker <line> elements at y >= 600:
        #   - no marker-end
        #   - span <= 200px
        #   - stroke="#c8553d" (the accent color used for footer marks)
        #   - y1 = y2 >= 600
        def line_repl(m):
            el = m.group(0)
            if 'marker-end' in el:
                return m.group(0)  # keep arrows
            attrs = dict(re.findall(r'\b(x1|y1|x2|y2)\s*=\s*["\']([^"\']+)["\']', el))
            try:
                y1 = float(attrs.get('y1', 0))
                y2 = float(attrs.get('y2', 0))
                x1 = float(attrs.get('x1', 0))
                x2 = float(attrs.get('x2', 999))
                span = abs(x2 - x1)
                if y1 >= 600 and y2 >= 600 and span <= 200 and '#c8553d' in el:
                    return ''
            except (ValueError, KeyError):
                pass
            return m.group(0)

        txt = re.sub(r'<line\b[^/]*/>', line_repl, txt)

        # Remove footer <text> elements at y >= 655 with x < 200.
        # This threshold preserves:
        #   - x-axis labels at y=605 ("k (candidates retrieved, log scale)" at y=640)
        #   - pipeline box labels in slide_intro_rag at y=643
        #   - figure step descriptions in slide_p39 at y=625, y=650
        # While still catching:
        #   - footer text starting at y=660+ in most files
        def text_repl(m):
            el = m.group(1)
            ym = re.search(r'\by\s*=\s*["\'](\d+(?:\.\d+)?)["\']', el)
            xm = re.search(r'\bx\s*=\s*["\'](\d+(?:\.\d+)?)["\']', el)
            if ym and xm:
                y = float(ym.group(1))
                x = float(xm.group(1))
                if y >= 655 and x < 200:
                    return ''
            return m.group(0)

        txt = re.sub(
            r'(<text\b(?:[^>]|\n)*?>(?:.*?)</text>)',
            text_repl,
            txt,
            flags=re.S
        )
        return txt

    raw = remove_footer_fallback(raw)

    # -----------------------------------------------------------------------
    # Pass 3: Adjust the SVG viewBox and width/height.
    #
    # New viewBox: "0 130 1100 480"  (shows y=130..610 of the 1100x720 canvas)
    # New width/height: 1100 x 480
    #
    # IMPORTANT: only replace the viewBox on the <svg> element itself,
    # NOT viewBox attributes inside <marker>, <pattern>, <symbol>, or <use>.
    # -----------------------------------------------------------------------

    def update_svg_tag(txt, vb_top=130, vb_bot=610):
        vb_h = vb_bot - vb_top   # 480
        vb_w = 1100

        def svg_open_repl(m):
            svg_open = m.group(0)
            # Replace viewBox
            if 'viewBox' in svg_open:
                svg_open = re.sub(
                    r'viewBox\s*=\s*["\'][^"\']*["\']',
                    f'viewBox="0 {vb_top} {vb_w} {vb_h}"',
                    svg_open
                )
            else:
                # Insert before closing >
                svg_open = svg_open[:-1] + f' viewBox="0 {vb_top} {vb_w} {vb_h}">'
            # Replace or add width
            if re.search(r'\bwidth\s*=', svg_open):
                svg_open = re.sub(
                    r'\bwidth\s*=\s*["\'][^"\']*["\']',
                    f'width="{vb_w}"',
                    svg_open
                )
            else:
                svg_open = svg_open[:-1] + f' width="{vb_w}">'
            # Replace or add height
            if re.search(r'\bheight\s*=', svg_open):
                svg_open = re.sub(
                    r'\bheight\s*=\s*["\'][^"\']*["\']',
                    f'height="{vb_h}"',
                    svg_open
                )
            else:
                svg_open = svg_open[:-1] + f' height="{vb_h}">'
            return svg_open

        # Match the opening <svg ...> tag only — stop before any child element.
        # This is the tag that starts with <svg and ends with the first >.
        txt = re.sub(r'<svg\b[^>]*>', svg_open_repl, txt, count=1)
        return txt

    raw = update_svg_tag(raw)

    # -----------------------------------------------------------------------
    # Pass 4: Clean up stray blank lines
    # -----------------------------------------------------------------------
    raw = re.sub(r'\n{3,}', '\n\n', raw)

    return raw


def main():
    svgs = sorted(f for f in os.listdir(SRC_DIR)
                  if f.endswith('.svg') and not os.path.isdir(os.path.join(SRC_DIR, f)))

    print(f"Processing {len(svgs)} SVG files...")
    errors = []

    for fname in svgs:
        src_path = os.path.join(SRC_DIR, fname)
        out_path = os.path.join(OUT_DIR, fname)

        try:
            with open(src_path, 'r', encoding='utf-8') as f:
                content = f.read()

            result = strip_chrome(content, fname)

            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(result)

            print(f"  OK  {fname}")
        except Exception as e:
            errors.append((fname, str(e)))
            print(f"  ERR {fname}: {e}", file=sys.stderr)

    print(f"\nDone. {len(svgs) - len(errors)}/{len(svgs)} succeeded.")
    if errors:
        print("Errors:")
        for fname, err in errors:
            print(f"  {fname}: {err}")


if __name__ == '__main__':
    main()
