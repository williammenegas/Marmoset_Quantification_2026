# Automated behavioral profiling reveals baseline phenotypes in marmosets

Data and code to reproduce the figures from this paper.

## Usage

```bash
pip install -r code/requirements.txt
python code/render_all.py                  # render every panel and page
python code/render_all.py fig1 figS3       # or a subset
python code/render_all.py --list           # list panels without rendering
```

Each panel script writes a `.pdf` and a 400 dpi `.png` into `figures/<fig>/` or `supplemental_figures/<fig>/`; each page script writes the whole page to `figures/<fig>.pdf` or `supplemental_figures/<fig>.pdf` (and `.png`). Scripts can also be run individually:

```bash
cd code/fig1 && python fig1_b_label_timeseries.py
```

## Layout

```
code/
  fig1/ … fig8/          main figure panels and page scripts
  figS1/ … figS14/       supplementary figure panels and page scripts
  render_all.py          batch renderer
  requirements.txt       package versions
  README.md              index of panels and scripts
  LICENSE                MIT License
data/                    per-panel source data
figures/                 rendered main figure panels and pages
supplemental_figures/    rendered supplementary figure panels and pages
```

A panel id is `<fig>_<letter>_<name>`, e.g. `fig1_b_label_timeseries`. [`code/README.md`](code/README.md) lists every panel and its script.

## Data

Every panel script names the folder it reads from as a `DATA` constant near its top:

```python
DATA = os.path.join(HERE, "..", "..", "data", "fig1", "fig1_b_label_timeseries")
```

Each folder holds the values the panel plots (CSV, or PNG for images), a README.md describing each file, and, where the panel prints text of its own, `annotations.csv` with that text. [`data/README.md`](data/README.md) indexes the folders and gives units and conventions.

## Notes

- The scripts redraw the stored values; they do not recompute statistics.
- `fig1_a_homecage_video` and `fig2_c_model_schematic` and `figS2_a_depth_methods` and `figS9_b_spectral_profiles` and `figS9_c_call_type_examples` are artwork and have no data or script. A figure's artwork -- these panels and the parts of panels no code draws -- is one transparent image of the whole page, `data/<fig>/<fig>_artwork/artwork.png`, which the page script draws over the panels, so the rendered pages are complete; the panel renders show what code draws.
- Needs Python 3.11 or later; tested with Python 3.13.9, numpy 2.3.5 and matplotlib 3.10.6.
- The figures are set in Arial. Where Arial is not installed, matplotlib warns ("findfont: Font family 'Arial' not found") and falls back to its bundled DejaVu Sans, which sets text wider, so the renders then differ from the published pages.

## Related repositories

The homecage behavior data is produced by three separate repositories. The files in `data` hold the values each panel plots, not the pipeline's per-frame output (`hlabel_*.csv` and `hcoord_*.csv`). The repositories are listed for anyone reproducing the behavioral analysis from raw video.

[marm_behavior](https://github.com/williammenegas/marm_behavior) is the behavioral pipeline itself. One command runs six stages over overhead stereo video of four differently marked marmosets in the homecage: DeepLabCut pose estimation, per-animal body-part tracks, per-frame behavioral features, and a projection of those features into a learned behavioral cluster space. The 80 states the panels here plot are its output, in per-frame `hlabel` files.

[marm_filt](https://github.com/williammenegas/marm_filt) denoises the body-part tracks. A graph neural network with temporal convolutions, written in TensorFlow and trained on the tracks themselves, smooths each animal's skeleton over time and writes a filtered copy next to each original.

[marm_viz](https://github.com/williammenegas/marm_viz) is the general-purpose viewer for the outputs. Pointed at a recording folder it draws ten plot types, among them spatial occupancy heatmaps, smoothed density maps, ethograms, state-usage and t-SNE summaries, head-direction polar histograms, behavioral-category transition matrices and cagemate state-usage correlations. Several panels in this repository are the published form of one of those views, fixed to a single figure and cohort.

## Author

William Menegas

## License

Code: MIT License, see [LICENSE](LICENSE). Data: CC BY 4.0, see [data/LICENSE](data/LICENSE).
