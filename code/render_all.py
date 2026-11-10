#!/usr/bin/env python3
"""
render_all.py -- redraw every figure panel and page from data/.

    python code/render_all.py                 # every figure
    python code/render_all.py fig1 figS3      # selected figures
    python code/render_all.py --list          # list panels without rendering
    python code/render_all.py --pages-only    # only the whole pages

Each panel script, code/<fig>/<panel id>.py, writes the panel cut from its
page to figures/<fig>/<panel id>.pdf and .png, a supplementary figure's to
supplemental_figures/<fig>/<panel id>.pdf and .png; each page script,
code/<fig>/<fig>_page.py, writes the whole page to figures/<fig>.pdf and
.png, a supplementary figure's to supplemental_figures/<fig>.pdf and .png
(paths from the repository's root). The scripts are imported by path and
run in this one process, each inside its own matplotlib rc context, so the
run imports nothing but the standard library, numpy and matplotlib; a
panel that fails is reported and the run goes on. The exit status is
non-zero if any script failed.
"""
import argparse
import importlib.util
import os
import re
import sys
import time
import traceback

# The scripts are imported by path; no bytecode is left beside them.
sys.dont_write_bytecode = True

ROOT = os.path.dirname(os.path.abspath(__file__))
ORDER = ["fig1", "fig2", "fig3", "fig4", "fig5", "fig6", "fig7", "fig8", "figS1", "figS2", "figS3", "figS4", "figS5", "figS6", "figS7", "figS8", "figS9", "figS10", "figS11", "figS12", "figS13", "figS14"]
PANEL = re.compile(r"(fig(?:S?\d+))_[a-z]_[a-z0-9_]+\.py")
#: The repository's root, where the scripts write: a main figure to
#: figures/, a supplementary figure to supplemental_figures/.
TOP = os.path.dirname(ROOT)


def out_dir(fig):
    """The folder a figure's panels and page are written to."""
    return os.path.join(TOP, "supplemental_figures" if fig.startswith("figS")
                        else "figures")


def discover(figs):
    """(fig, panel scripts, page script) for every figure in `figs`, in
    paper order; panel scripts sorted by letter."""
    out = []
    for fig in figs:
        folder = os.path.join(ROOT, fig)
        if not os.path.isdir(folder):
            continue
        panels = sorted(f for f in os.listdir(folder)
                        if PANEL.fullmatch(f) and f.startswith(fig + "_"))
        page = f"{fig}_page.py"
        out.append((fig, panels,
                    page if os.path.exists(os.path.join(folder, page))
                    else None))
    return out


def load(path):
    """A script, imported by path."""
    name = os.path.splitext(os.path.basename(path))[0]
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run(fig, script):
    """Render one script with its defaults; (ok, seconds, error)."""
    t0 = time.time()
    try:
        load(os.path.join(ROOT, fig, script)).render()
        return True, time.time() - t0, ""
    except Exception:                                    # noqa: BLE001
        return False, time.time() - t0, traceback.format_exc().strip()


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.strip().split("\n")[0])
    ap.add_argument("figs", nargs="*",
                    help="figures to render, e.g. fig1 figS3 (default: all)")
    ap.add_argument("--list", action="store_true",
                    help="list the panels and pages without rendering")
    ap.add_argument("--pages-only", action="store_true",
                    help="render only the whole pages")
    a = ap.parse_args(argv)
    unknown = [f for f in a.figs if f not in ORDER]
    if unknown:
        ap.error(f"no such figure: {', '.join(unknown)} "
                 f"(figures: {', '.join(ORDER)})")
    found = discover(a.figs or ORDER)
    if a.list:
        n = 0
        for fig, panels, page in found:
            for f in panels:
                print(f"{fig}/{f}")
                n += 1
            if page:
                print(f"{fig}/{page}  (the whole page)")
        print(f"\n{n} panels, {sum(1 for *_x, p in found if p)} pages")
        return 0
    fails, done, t0 = [], 0, time.time()
    for fig, panels, page in found:
        jobs = ([] if a.pages_only else panels) + ([page] if page else [])
        for script in jobs:
            ok, dt, err = run(fig, script)
            done += 1
            print(f"{'ok  ' if ok else 'FAIL'} {dt:6.1f}s  {fig}/{script}",
                  flush=True)
            if not ok:
                fails.append((f"{fig}/{script}", err))
    outs = []
    for fig, _panels, _page in found:
        if out_dir(fig) not in outs:
            outs.append(out_dir(fig))
    print(f"\n{done - len(fails)}/{done} scripts rendered in "
          f"{time.time() - t0:.0f}s; output in {' and '.join(outs)}")
    for name, err in fails:
        print(f"  FAIL {name}: {err.splitlines()[-1] if err else ''}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
