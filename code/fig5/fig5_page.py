r"""
Figure 5: the whole page, redrawn from data/fig5/.

Each panel's script draws into a page-sized figure at its own place on the
page; this runs them all onto one figure and saves the page at its real
size (US Letter).

Usage:

    python fig5_page.py [--data DIR] [--out-dir DIR]

writes fig5.pdf and fig5.png (400 dpi) into figures/ (OUT below).
"""

from __future__ import annotations

import argparse
import importlib.util
import os
import sys

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt                          # noqa: E402

# The panel scripts are imported by path; no bytecode is left beside them.
sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "..", "data", "fig5")
OUT = os.path.join(HERE, "..", "..", "figures")
NAME = "fig5"
PAGE = (8.5, 11.0)
DPI = 400
FONT_NAME = 'Arial'
LETTER_SIZE = 12
LETTER_COLOUR = '#000000'
PANELS = ['fig5_a_session_tsne',
 'fig5_b_category_rasters',
 'fig5_c_state_usage',
 'fig5_d_usage_discriminability',
 'fig5_e_state_corr',
 'fig5_f_corr_discriminability']
PASTED_LETTERS = []
PLACEHOLDERS = []
ARTWORK = None


def panel(pid):
    """A panel's script, imported by path."""
    path = os.path.join(HERE, pid + ".py")
    spec = importlib.util.spec_from_file_location(pid, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def draw(fig, data=None):
    """Every panel of the page onto one page-sized figure, from the
    figure's data folder (`DATA` unless another is given)."""
    root = os.path.normpath(data if data else DATA)
    for pid in PANELS:
        panel(pid).draw(fig, os.path.join(root, pid))
    # A pasted panel's letter, and any words standing in a space left
    # empty: page text, so no panel script carries them.
    for L in PASTED_LETTERS:
        fig.text(L["x"] / PAGE[0], 1.0 - L["baseline"] / PAGE[1],
                 f"{L['ch']})", fontsize=LETTER_SIZE, fontweight="bold",
                 ha="left", va="baseline", color=LETTER_COLOUR,
                 fontname=FONT_NAME)
    for p in PLACEHOLDERS:
        fig.text(p["x"] / PAGE[0], 1.0 - p["y"] / PAGE[1], p["text"],
                 fontsize=p["size"], color=p["colour"], ha=p["ha"],
                 va=p["va"], fontname=FONT_NAME)
    if ARTWORK:
        # The page's artwork, which no code draws: one transparent image of
        # the whole page, over the panels.
        ax = fig.add_axes((0.0, 0.0, 1.0, 1.0), zorder=10)
        ax.imshow(plt.imread(os.path.join(root, ARTWORK)),
                  extent=(0.0, 1.0, 0.0, 1.0), aspect="auto",
                  interpolation="none")
        ax.set_axis_off()
    return fig


def render(data=None, out_dir=None, formats=("pdf", "png")):
    """Draw the page and write NAME.<format> into `out_dir` (`OUT` unless
    another is given), at its real size (US Letter)."""
    out = os.path.normpath(out_dir if out_dir else OUT)
    os.makedirs(out, exist_ok=True)
    written = []
    # Text in the PDF stays TrueType text, as on the published pages.
    with plt.rc_context({"pdf.fonttype": 42, "ps.fonttype": 42}):
        fig = plt.figure(figsize=PAGE, facecolor="w")
        try:
            draw(fig, data)
            for ext in formats:
                path = os.path.join(out, f"{NAME}.{ext}")
                # No creation date in a PDF, so a re-render writes the same
                # bytes.
                fig.savefig(path, dpi=DPI, facecolor="w", bbox_inches=None,
                            pad_inches=0,
                            metadata=({"CreationDate": None} if ext == "pdf"
                                      else None))
                written.append(path)
        finally:
            plt.close(fig)
    return written


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.strip().split("\n")[0])
    ap.add_argument("--data", help="the figure's data folder (default: "
                                   "DATA, beside the code folder)")
    ap.add_argument("--out-dir",
                    help="where to write the page (default: OUT, "
                         "figures)")
    a = ap.parse_args(argv)
    for path in render(a.data, a.out_dir):
        print(f"wrote {os.path.normpath(path)}")


if __name__ == "__main__":
    main()
