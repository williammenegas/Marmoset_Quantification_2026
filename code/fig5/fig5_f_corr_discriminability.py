r"""
Figure 5, panel f: d's three views, for the correlations.

Panel id fig5_f_corr_discriminability. Title: "Example state", "All
states", "Discriminability".

Redrawn from the panel's data folder,
data/fig5/fig5_f_corr_discriminability/ (DATA below), with numpy and
matplotlib alone: what the panel shows is read from that folder, and how
the page lays it out -- the axes' rectangles in page inches, limits, ticks,
labels, titles, legends, colour maps, drawing styles, and the decoration
the data leave out (cage wireframes, category outlines, category
boundaries) -- is written below as literals, measured off the published
page.

Usage:

    python fig5_f_corr_discriminability.py [--data DIR] [--out-dir DIR]

writes fig5_f_corr_discriminability.pdf and
fig5_f_corr_discriminability.png (400 dpi), the panel cut from its page,
into figures/fig5/ (OUT below); fig5_page.py draws the whole page and
code/render_all.py every figure.
"""

from __future__ import annotations

import argparse
import csv
import os
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt                          # noqa: E402
from matplotlib.collections import (                     # noqa: E402
    LineCollection, PolyCollection,
)
from matplotlib.colors import ListedColormap             # noqa: E402
from matplotlib.lines import Line2D                      # noqa: E402
from matplotlib.offsetbox import (                       # noqa: E402
    AnchoredOffsetbox, HPacker, TextArea,
)
from matplotlib.patches import (                         # noqa: E402
    Patch, PathPatch, Polygon, Rectangle, Wedge,
)
from matplotlib.path import Path as MPath                # noqa: E402
from matplotlib.transforms import Bbox                   # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "..", "data", "fig5", "fig5_f_corr_discriminability")
OUT = os.path.join(HERE, "..", "..", "figures", "fig5")
NAME = "fig5_f_corr_discriminability"
PAGE = (8.5, 11.0)
DPI = 400
#: Whether the panel prints text of its own, listed in annotations.csv.
ANNOTATIONS = True
FONT = {'name': 'Arial',
 'letter': 12,
 'title': 8,
 'label': 7,
 'tick': 7,
 'legend': 6}
AXIS_COLOUR = '#262626'
LETTER_COLOUR = '#000000'
SPEC = {'cmaps': {}, 'shapes': {}}
PANEL = {'title': ['Example state', 'All states', 'Discriminability'],
 'headings': [],
 'partial': '',
 'subplots': [{'role': 'plot',
               'name': 'Example state Control Tablet',
               'text_style': [{'size': 6.0,
                               'colour': '#262626',
                               'ha': 'center',
                               'va': 'bottom',
                               'rotation': 0.0,
                               'weight': 'normal',
                               'zorder': 3.0,
                               'rank': 74},
                              {'size': 8.0,
                               'colour': '#262626',
                               'ha': 'center',
                               'va': 'bottom',
                               'rotation': 0.0,
                               'weight': 'normal',
                               'zorder': 3.0,
                               'rank': 76}],
               'rect': [4.6783, 6.1196, 0.66, 1.12],
               'pos': [0.5503882352941176,
                       0.3418545454545454,
                       0.0776470588235294,
                       0.10181818181818181],
               'xlim': [0.4, 2.6],
               'ylim': [-0.36393533802066025, 0.8747369139191478],
               'xscale': 'linear',
               'yscale': 'linear',
               'axis_off': False,
               'facecolor': '#ffffff',
               'frame': True,
               'zorder': 0.0,
               'spines': {'left': {'visible': True,
                                   'lw': 0.6,
                                   'colour': '#262626',
                                   'bounds': None,
                                   'position': None},
                          'right': {'visible': False,
                                    'lw': 0.6,
                                    'colour': '#262626',
                                    'bounds': None,
                                    'position': None},
                          'bottom': {'visible': True,
                                     'lw': 0.6,
                                     'colour': '#262626',
                                     'bounds': None,
                                     'position': None},
                          'top': {'visible': False,
                                  'lw': 0.6,
                                  'colour': '#262626',
                                  'bounds': None,
                                  'position': None}},
               'xticks': {'at': [1.0, 2.0],
                          'labels': ['Control', 'Tablet'],
                          'pad': 1.5,
                          'size': 2.7,
                          'width': 0.6,
                          'direction': 'out',
                          'visible': [True, False],
                          'label_visible': [True, False],
                          'labelsize': 7.0,
                          'colour': '#262626',
                          'labelcolour': '#262626',
                          'rotation': 35.0,
                          'ha': 'right',
                          'va': 'top',
                          'rotation_mode': 'anchor'},
               'yticks': {'at': [-0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0],
                          'labels': ['-0.50',
                                     '-0.25',
                                     '0.00',
                                     '0.25',
                                     '0.50',
                                     '0.75',
                                     '1.00'],
                          'pad': 1.5,
                          'size': 2.7,
                          'width': 0.6,
                          'direction': 'out',
                          'visible': [True, False],
                          'label_visible': [True, False],
                          'labelsize': 7.0,
                          'colour': '#262626',
                          'labelcolour': '#262626',
                          'rotation': 0.0,
                          'ha': 'right',
                          'va': 'center_baseline'},
               'xlabel': None,
               'ylabel': {'text': 'Correlation: State 43',
                          'size': 7.0,
                          'colour': '#262626',
                          'rotation': 90.0,
                          'pad': 4.0,
                          'ha': 'center',
                          'va': 'bottom'},
               'files': [{'file': 'example_state_control_tablet_lines.csv',
                          'kind': 'lines',
                          'style': {'zorder': 1.0,
                                    'rank': 0,
                                    'alpha': 0.5,
                                    'lw': 0.5,
                                    'colour': '#cccccc',
                                    'mfc': '#cccccc',
                                    'mec': '#cccccc',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'styles': [{'zorder': 1.0,
                                      'rank': 0,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 1,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 2,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 3,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 4,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 5,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 6,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 7,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 8,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 9,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 10,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 11,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 12,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 13,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 14,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 15,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 16,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 17,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 18,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 19,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 20,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 21,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 22,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 23,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 24,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 25,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 26,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 27,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 28,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 29,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 30,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 31,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 32,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 33,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 34,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 35,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 36,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 37,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 38,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 39,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 40,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 41,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 42,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 43,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 44,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 45,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 46,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 47,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 48,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 49,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 50,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 51,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 52,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 53,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 54,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 55,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 56,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 57,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 58,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 59,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 60,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 61,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 62,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 63,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 64,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 65,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 66,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 67,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 68,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 69,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 70,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 1.0,
                                      'rank': 71,
                                      'alpha': 0.5,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'mfc': '#cccccc',
                                      'mec': '#cccccc',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 2.0,
                                      'rank': 75,
                                      'clip': False,
                                      'lw': 0.5,
                                      'colour': '#262626',
                                      'mfc': '#262626',
                                      'mec': '#262626',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'miter'}]},
                         {'file': 'example_state_control_tablet_points.csv',
                          'kind': 'points',
                          'style': {'zorder': 3.0,
                                    'rank': 72,
                                    'lw': 1.0,
                                    'face': '#76b5a0',
                                    'area': 4.2,
                                    'one_size': True,
                                    'marker': 'o'},
                          'styles': [{'zorder': 3.0,
                                      'rank': 72,
                                      'lw': 1.0,
                                      'face': '#76b5a0',
                                      'area': 4.2,
                                      'one_size': True,
                                      'marker': 'o'},
                                     {'zorder': 3.0,
                                      'rank': 73,
                                      'lw': 1.0,
                                      'face': '#c98ecf',
                                      'area': 4.2,
                                      'one_size': True,
                                      'marker': 'o'}]}],
               'decor': [],
               'aspect': 'auto'},
              {'role': 'plot',
               'name': 'All states',
               'text_style': [{'offsetbox': {'parts': [{'text': 'Higher '
                                                                'in ',
                                                        'colour': '#262626',
                                                        'size': 6.0,
                                                        'weight': 'normal'},
                                                       {'text': 'Control',
                                                        'colour': '#5e9180',
                                                        'size': 6.0,
                                                        'weight': 'normal'}],
                                             'align': 'baseline',
                                             'pad': 0.0,
                                             'sep': 0.0,
                                             'loc': 2,
                                             'anchor': [0.6884588235294119,
                                                        0.4406181818181818,
                                                        0.0,
                                                        0.0],
                                             'box_pad': 0.0,
                                             'borderpad': 0.0,
                                             'frameon': False,
                                             'zorder': 5.0}},
                              {'offsetbox': {'parts': [{'text': 'Higher '
                                                                'with ',
                                                        'colour': '#262626',
                                                        'size': 6.0,
                                                        'weight': 'normal'},
                                                       {'text': 'Tablet',
                                                        'colour': '#a172a6',
                                                        'size': 6.0,
                                                        'weight': 'normal'}],
                                             'align': 'baseline',
                                             'pad': 0.0,
                                             'sep': 0.0,
                                             'loc': 4,
                                             'anchor': [0.8123176470588235,
                                                        0.3449090909090909,
                                                        0.0,
                                                        0.0],
                                             'box_pad': 0.0,
                                             'borderpad': 0.0,
                                             'frameon': False,
                                             'zorder': 5.0}}],
               'rect': [5.8183, 6.1196, 1.12, 1.12],
               'pos': [0.6845058823529413,
                       0.3418545454545454,
                       0.1317647058823529,
                       0.10181818181818181],
               'xlim': [-0.37551140555899915, 0.37551140555899915],
               'ylim': [-0.37551140555899915, 0.37551140555899915],
               'xscale': 'linear',
               'yscale': 'linear',
               'axis_off': False,
               'facecolor': '#ffffff',
               'frame': True,
               'zorder': 0.0,
               'spines': {'left': {'visible': True,
                                   'lw': 0.6,
                                   'colour': '#262626',
                                   'bounds': None,
                                   'position': None},
                          'right': {'visible': False,
                                    'lw': 0.6,
                                    'colour': '#262626',
                                    'bounds': None,
                                    'position': None},
                          'bottom': {'visible': True,
                                     'lw': 0.6,
                                     'colour': '#262626',
                                     'bounds': None,
                                     'position': None},
                          'top': {'visible': False,
                                  'lw': 0.6,
                                  'colour': '#262626',
                                  'bounds': None,
                                  'position': None}},
               'xticks': {'at': [-0.5, -0.25, 0.0, 0.25, 0.5],
                          'labels': ['-0.50',
                                     '-0.25',
                                     '0.00',
                                     '0.25',
                                     '0.50'],
                          'pad': 1.5,
                          'size': 2.7,
                          'width': 0.6,
                          'direction': 'out',
                          'visible': [True, False],
                          'label_visible': [True, False],
                          'labelsize': 7.0,
                          'colour': '#262626',
                          'labelcolour': '#262626',
                          'rotation': 0.0,
                          'ha': 'center',
                          'va': 'top'},
               'yticks': {'at': [-0.4,
                                 -0.2,
                                 0.0,
                                 0.20000000000000007,
                                 0.4],
                          'labels': ['-0.4', '-0.2', '0.0', '0.2', '0.4'],
                          'pad': 1.5,
                          'size': 2.7,
                          'width': 0.6,
                          'direction': 'out',
                          'visible': [True, False],
                          'label_visible': [True, False],
                          'labelsize': 7.0,
                          'colour': '#262626',
                          'labelcolour': '#262626',
                          'rotation': 0.0,
                          'ha': 'right',
                          'va': 'center_baseline'},
               'xlabel': {'text': 'Correlation, tablet',
                          'size': 7.0,
                          'colour': '#262626',
                          'rotation': 0.0,
                          'pad': 4.0,
                          'ha': 'center',
                          'va': 'top'},
               'ylabel': {'text': 'Correlation, control',
                          'size': 7.0,
                          'colour': '#262626',
                          'rotation': 90.0,
                          'pad': 4.0,
                          'ha': 'center',
                          'va': 'bottom'},
               'files': [{'file': 'all_states_lines.csv',
                          'kind': 'lines',
                          'style': {'zorder': 0.0,
                                    'rank': 0,
                                    'lw': 0.5,
                                    'ls': [0.0, [3.7, 1.6]],
                                    'colour': '#262626',
                                    'mfc': '#262626',
                                    'mec': '#262626',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'styles': [{'zorder': 0.0,
                                      'rank': 0,
                                      'lw': 0.5,
                                      'ls': [0.0, [3.7, 1.6]],
                                      'colour': '#262626',
                                      'mfc': '#262626',
                                      'mec': '#262626',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'}]},
                         {'file': 'all_states_points.csv',
                          'kind': 'points',
                          'style': {'zorder': 3.0,
                                    'rank': 3,
                                    'clip': False,
                                    'lw': 1.0,
                                    'face': '#262626',
                                    'area': 8.0,
                                    'one_size': True,
                                    'marker': 'o'},
                          'styles': [{'zorder': 3.0,
                                      'rank': 3,
                                      'clip': False,
                                      'lw': 1.0,
                                      'face': '#262626',
                                      'area': 8.0,
                                      'one_size': True,
                                      'marker': 'o'}]},
                         {'file': 'all_states_segments.csv',
                          'kind': 'segments',
                          'style': {'zorder': 1.0,
                                    'rank': 1,
                                    'lw': 0.5,
                                    'colour': '#cccccc',
                                    'edge': '#cccccc'},
                          'styles': [{'zorder': 1.0,
                                      'rank': 1,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'edge': '#cccccc'},
                                     {'zorder': 1.0,
                                      'rank': 2,
                                      'lw': 0.5,
                                      'colour': '#cccccc',
                                      'edge': '#cccccc'}]}],
               'decor': [],
               'aspect': 1.0},
              {'role': 'plot',
               'name': 'Discriminability Control Tablet',
               'text_style': [{'size': 6.0,
                               'colour': '#262626',
                               'ha': 'center',
                               'va': 'bottom',
                               'rotation': 0.0,
                               'weight': 'normal',
                               'zorder': 3.0,
                               'rank': 9},
                              {'size': 8.0,
                               'colour': '#262626',
                               'ha': 'center',
                               'va': 'bottom',
                               'rotation': 0.0,
                               'weight': 'normal',
                               'zorder': 3.0,
                               'rank': 11}],
               'rect': [7.3383, 6.1196, 0.67, 1.12],
               'pos': [0.8633294117647059,
                       0.3418545454545454,
                       0.07882352941176474,
                       0.10181818181818181],
               'xlim': [0.4, 2.6],
               'ylim': [0.0, 9.186667907895874],
               'xscale': 'linear',
               'yscale': 'linear',
               'axis_off': False,
               'facecolor': '#ffffff',
               'frame': True,
               'zorder': 0.0,
               'spines': {'left': {'visible': True,
                                   'lw': 0.6,
                                   'colour': '#262626',
                                   'bounds': None,
                                   'position': None},
                          'right': {'visible': False,
                                    'lw': 0.6,
                                    'colour': '#262626',
                                    'bounds': None,
                                    'position': None},
                          'bottom': {'visible': True,
                                     'lw': 0.6,
                                     'colour': '#262626',
                                     'bounds': None,
                                     'position': None},
                          'top': {'visible': False,
                                  'lw': 0.6,
                                  'colour': '#262626',
                                  'bounds': None,
                                  'position': None}},
               'xticks': {'at': [1.0, 2.0],
                          'labels': ['Control', 'Tablet'],
                          'pad': 1.5,
                          'size': 2.7,
                          'width': 0.6,
                          'direction': 'out',
                          'visible': [True, False],
                          'label_visible': [True, False],
                          'labelsize': 7.0,
                          'colour': '#262626',
                          'labelcolour': '#262626',
                          'rotation': 35.0,
                          'ha': 'right',
                          'va': 'top',
                          'rotation_mode': 'anchor'},
               'yticks': {'at': [0.0, 2.0, 4.0, 6.0, 8.0, 10.0],
                          'labels': ['0', '2', '4', '6', '8', '10'],
                          'pad': 1.5,
                          'size': 2.7,
                          'width': 0.6,
                          'direction': 'out',
                          'visible': [True, False],
                          'label_visible': [True, False],
                          'labelsize': 7.0,
                          'colour': '#262626',
                          'labelcolour': '#262626',
                          'rotation': 0.0,
                          'ha': 'right',
                          'va': 'center_baseline'},
               'xlabel': None,
               'ylabel': {'text': 'Average score (all states)',
                          'size': 7.0,
                          'colour': '#262626',
                          'rotation': 90.0,
                          'pad': 4.0,
                          'ha': 'center',
                          'va': 'bottom'},
               'files': [{'file': 'discriminability_control_tablet_lines.csv',
                          'kind': 'lines',
                          'style': {'zorder': 6.0,
                                    'rank': 1,
                                    'lw': 0.9,
                                    'colour': '#76b5a0',
                                    'mfc': '#76b5a0',
                                    'mec': '#76b5a0',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'styles': [{'zorder': 6.0,
                                      'rank': 1,
                                      'lw': 0.9,
                                      'colour': '#76b5a0',
                                      'mfc': '#76b5a0',
                                      'mec': '#76b5a0',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 6.0,
                                      'rank': 4,
                                      'lw': 0.9,
                                      'colour': '#c98ecf',
                                      'mfc': '#c98ecf',
                                      'mec': '#c98ecf',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 0.0,
                                      'rank': 6,
                                      'lw': 0.5,
                                      'ls': [0.0, [3.7, 1.6]],
                                      'colour': '#737373',
                                      'mfc': '#737373',
                                      'mec': '#737373',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 0.0,
                                      'rank': 7,
                                      'lw': 0.5,
                                      'ls': [0.0, [3.7, 1.6]],
                                      'colour': '#737373',
                                      'mfc': '#737373',
                                      'mec': '#737373',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 0.0,
                                      'rank': 8,
                                      'lw': 0.5,
                                      'ls': [0.0, [3.7, 1.6]],
                                      'colour': '#737373',
                                      'mfc': '#737373',
                                      'mec': '#737373',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 2.0,
                                      'rank': 10,
                                      'clip': False,
                                      'lw': 0.5,
                                      'colour': '#262626',
                                      'mfc': '#262626',
                                      'mec': '#262626',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'miter'}]},
                         {'file': 'discriminability_control_tablet_points.csv',
                          'kind': 'points',
                          'style': {'zorder': 2.0,
                                    'rank': 0,
                                    'lw': 1.0,
                                    'face': '#c1ded4',
                                    'area': 3.3,
                                    'one_size': True,
                                    'marker': 'o'},
                          'styles': [{'zorder': 2.0,
                                      'rank': 0,
                                      'lw': 1.0,
                                      'face': '#c1ded4',
                                      'area': 3.3,
                                      'one_size': True,
                                      'marker': 'o'},
                                     {'zorder': 7.0,
                                      'rank': 2,
                                      'lw': 1.0,
                                      'face': '#76b5a0',
                                      'area': 20.0,
                                      'one_size': True,
                                      'marker': 'o'},
                                     {'zorder': 2.0,
                                      'rank': 3,
                                      'lw': 1.0,
                                      'face': '#e7cce9',
                                      'area': 3.3,
                                      'one_size': True,
                                      'marker': 'o'},
                                     {'zorder': 7.0,
                                      'rank': 5,
                                      'lw': 1.0,
                                      'face': '#c98ecf',
                                      'area': 20.0,
                                      'one_size': True,
                                      'marker': 'o'}]}],
               'decor': [],
               'aspect': 'auto'}],
 'texts': [{'text': 'Example state',
            'x': 5.0083,
            'y': 5.9996,
            'size': 8.0,
            'weight': 'normal',
            'ha': 'center',
            'va': 'baseline',
            'rotation': 0.0,
            'colour': '#262626'},
           {'text': 'All states',
            'x': 6.3783,
            'y': 5.9996,
            'size': 8.0,
            'weight': 'normal',
            'ha': 'center',
            'va': 'baseline',
            'rotation': 0.0,
            'colour': '#262626'},
           {'text': 'Discriminability',
            'x': 7.6733,
            'y': 5.9996,
            'size': 8.0,
            'weight': 'normal',
            'ha': 'center',
            'va': 'baseline',
            'rotation': 0.0,
            'colour': '#262626'}],
 'legends': [],
 'letter': {'ch': 'f', 'x': 4.2283, 'baseline': 5.9996, 'top': 5.8796}}


# ---------------------------------------------------------------------------
# Reading the panel's data
# ---------------------------------------------------------------------------
def read(path):
    """(header, rows) of a CSV the data folder holds."""
    with open(path, newline="", encoding="utf-8") as fh:
        rows = list(csv.reader(fh))
    return rows[0], rows[1:]


def need(path):
    """`path`, a file the panel is drawn from: a missing one stops the
    script, so that no panel is drawn without part of its data."""
    if not path.is_file():
        hint = (" (on Windows, a path of 260 characters or more cannot be "
                "opened unless long paths are enabled)"
                if os.name == "nt" and len(str(path)) >= 260 else "")
        raise FileNotFoundError(f"missing data file: {path}{hint}")
    return path


def nums(values):
    """A column as floats; blanks and names (a categorical axis prints
    names where a matrix has numbers) as NaN."""
    out = []
    for v in values:
        try:
            out.append(float(v))
        except (TypeError, ValueError):
            out.append(np.nan)
    return np.array(out, dtype=float)


def column(header, rows, name):
    i = header.index(name)
    return [r[i] for r in rows]


def ints(header, rows, name):
    return np.array([int(float(v)) for v in column(header, rows, name)])


def matrix(path):
    """(xs, ys, M) of a matrix CSV: x centres in the header, y centres in
    the first column."""
    header, rows = read(path)
    xs = nums(header[1:])
    ys = nums([r[0] for r in rows])
    M = np.array([[float(v) if v not in ("", "nan") else np.nan
                   for v in r[1:]] for r in rows])
    return xs, ys, M


def cmap_of(key):
    """A colour map the page draws with, written out as its colours."""
    entry = SPEC["cmaps"][key]
    cm = ListedColormap(entry["colours"])
    cm.set_bad(entry["bad"])
    return cm


def rgba(values, fallback):
    """Colours for a column, "none" kept as no colour."""
    return [fallback if v == "" else v for v in values]


def ls_of(style, default="solid"):
    """A line style: a dash pattern is written as [offset, [on, off, ...]]
    and matplotlib wants it as a tuple."""
    v = style.get("ls", default)
    return (v[0], tuple(v[1])) if isinstance(v, list) else v


def marker_of(style, default="o"):
    """A marker: its name, or its outline written out as a path."""
    m = style.get("marker", default)
    if isinstance(m, dict):
        return MPath(np.array(m["verts"], dtype=float),
                     None if m["codes"] is None
                     else np.array(m["codes"], dtype=np.uint8))
    return m


def zo(style, default):
    """A style's z-order, nudged by the artist's place among its subplot's
    artists on the page ("rank"), so that artists of one z-order draw in
    the page's order, not in the order of the data files."""
    return style.get("zorder", default) + style.get("rank", 0) * 1e-9


def kw(style, *names, **extra):
    """Style literals as matplotlib keywords."""
    out = dict(extra)
    for n in names:
        if n not in style:
            continue
        v = ls_of(style) if n == "ls" else style[n]
        out[{"lw": "linewidth", "ls": "linestyle", "colour": "color",
             "face": "facecolor", "edge": "edgecolor", "ms": "markersize",
             "mew": "markeredgewidth"}.get(n, n)] = v
    return out


def line_kw(s, colour=None):
    """Keywords for a line drawn as the page draws it: width, dashes,
    markers, ends and corners."""
    out = kw(s, "lw", "ls", "ms", "alpha")
    out.update(zorder=zo(s, 2),
               solid_capstyle=s.get("capstyle", "projecting"),
               solid_joinstyle=s.get("joinstyle", "round"),
               dash_capstyle=s.get("dash_capstyle", "butt"),
               clip_on=s.get("clip", True),
               color=colour if colour is not None else s.get("colour"))
    if "marker" in s:
        out["marker"] = marker_of(s)
    for k, n in (("mfc", "markerfacecolor"), ("mec", "markeredgecolor"),
                 ("mew", "markeredgewidth"), ("drawstyle", "drawstyle"),
                 ("fillstyle", "fillstyle"), ("aa", "antialiased")):
        if k in s:
            out[n] = s[k]
    return out


def patch_kw(s, face, edge, lw_default=0.0, zorder=1):
    """Keywords for a patch drawn as the page draws it."""
    out = dict(facecolor=face, edgecolor=edge,
               linewidth=s.get("lw", lw_default), linestyle=ls_of(s),
               alpha=s.get("alpha"), zorder=zo(s, zorder),
               clip_on=s.get("clip", True))
    if "pcap" in s:
        out["capstyle"] = s["pcap"]
    if "pjoin" in s:
        out["joinstyle"] = s["pjoin"]
    if "hatch" in s:
        out["hatch"] = s["hatch"]
    if s.get("fill") is False:
        out["fill"] = False
    return out


# ---------------------------------------------------------------------------
# Drawing one file
# ---------------------------------------------------------------------------
def draw_points(ax, path, st, styles):
    header, rows = read(path)
    if not rows:
        return
    skip = ("group", "series", "category", "colour", "marker area (pt^2)")
    data = [n for n in header if n not in skip]
    x, y = nums(column(header, rows, data[0])), nums(column(header, rows,
                                                            data[1]))
    three = hasattr(ax, "get_zlim")
    # On a 3-D axes the third column is z; elsewhere it is the value a
    # colour map colours.
    z = nums(column(header, rows, data[2])) if three else None
    value = data[2] if len(data) > 2 and not three else None
    group = (ints(header, rows, "group") if "group" in header
             else np.ones(len(rows), int))
    area = (nums(column(header, rows, "marker area (pt^2)"))
            if "marker area (pt^2)" in header else None)
    # A blank colour is a marker with no fill: its outline alone shows.
    cols = (rgba(column(header, rows, "colour"), "none")
            if "colour" in header else None)
    for g in sorted(set(group.tolist())):
        m = group == g
        s = styles[g - 1] if len(styles) >= g else st
        c = ([v for v, keep in zip(cols, m) if keep] if cols
             else s.get("face", s.get("colour", "#000000")))
        if isinstance(c, list) and len(set(c)) == 1:
            # One colour for the whole group, given once: matplotlib then
            # draws the markers as the page did, each snapped to the pixel
            # grid, not as a collection of separately coloured paths.
            c = c[0]
        size = area[m] if area is not None else s.get("area", 6.0)
        if (area is not None and s.get("one_size")
                and len(np.unique(size)) == 1):
            # Likewise one size, where the page gave one.
            size = float(size[0])
        if three:
            ax.scatter(x[m], y[m], z[m], c=c, s=size,
                       marker=marker_of(s), linewidths=s.get("lw", 0.0),
                       edgecolors=s.get("edge", "none"),
                       alpha=s.get("alpha"), zorder=zo(s, 2),
                       depthshade=s.get("depthshade", False))
            continue
        opts = dict(s=size,
                    marker=marker_of(s), linewidths=s.get("lw", 0.0),
                    edgecolors=s.get("edge", "none"),
                    alpha=s.get("alpha"), zorder=zo(s, 2),
                    clip_on=s.get("clip", True))
        if "ls" in s:
            opts["linestyle"] = ls_of(s)
        if value and "cmap" in s:
            ax.scatter(x[m], y[m], c=nums(column(header, rows, value))[m],
                       cmap=cmap_of(s["cmap"]), vmin=s["clim"][0],
                       vmax=s["clim"][1], **opts)
        else:
            ax.scatter(x[m], y[m], c=c, **opts)


def draw_lines(ax, path, st, styles):
    header, rows = read(path)
    if not rows:
        return
    three = hasattr(ax, "get_zlim")
    if "line" not in header:                       # wide: one column a line
        x = nums(column(header, rows, header[0]))
        for i, n in enumerate(header[1:]):
            s = styles[i] if len(styles) > i else st
            ax.plot(x, nums(column(header, rows, n)), **line_kw(s))
        return
    line = ints(header, rows, "line")
    names = [n for n in header if n not in (
        "line", "series", "colour", "category", "marker fill",
        "marker edge")]
    x, y = nums(column(header, rows, names[0])), nums(column(header, rows,
                                                             names[1]))
    z = nums(column(header, rows, names[2])) if len(names) > 2 else None
    cols = column(header, rows, "colour") if "colour" in header else None
    fills = (column(header, rows, "marker fill") if "marker fill" in header
             else None)
    edges = (column(header, rows, "marker edge") if "marker edge" in header
             else None)
    for i, k in enumerate(sorted(set(line.tolist()))):
        m = line == k
        first = int(np.flatnonzero(m)[0])
        s = dict(styles[i] if len(styles) > i else st)
        # A marker-only line carries its colour in the marker, which is
        # what the page shows; the line colour can be the cycle's.
        if fills and fills[first]:
            s["mfc"] = fills[first]
        if edges and edges[first]:
            s["mec"] = edges[first]
        opts = line_kw(s, cols[first] if cols else None)
        if z is not None and three:
            ax.plot(x[m], y[m], z[m], **opts)
        else:
            ax.plot(x[m], y[m], **opts)


def draw_bars(ax, path, st, styles):
    header, rows = read(path)
    if not rows:
        return
    pos, thick = nums(column(header, rows, header[0])), nums(
        column(header, rows, header[1]))
    base, length = nums(column(header, rows, header[2])), nums(
        column(header, rows, header[3]))
    cols = (column(header, rows, "colour") if "colour" in header
            else [st.get("face", "#000000")] * len(rows))
    edges = (rgba(column(header, rows, "edge colour"), "none")
             if "edge colour" in header else st.get("edge", "none"))
    opts = dict(color=cols, edgecolor=edges,
                linewidth=st.get("lw", 0.0), alpha=st.get("alpha"),
                zorder=zo(st, 2), clip_on=st.get("clip", True))
    if "ls" in st:
        opts["linestyle"] = ls_of(st)
    if "pjoin" in st:
        opts["joinstyle"] = st["pjoin"]
    if "pcap" in st:
        opts["capstyle"] = st["pcap"]
    if header[1] == "bar width":
        ax.bar(pos, length, width=thick, bottom=base, align="center",
               **opts)
    else:
        ax.barh(pos, length, height=thick, left=base, align="center",
                **opts)


def draw_boxes(ax, path, st, styles):
    header, rows = read(path)
    left, right = nums(column(header, rows, header[0])), nums(
        column(header, rows, header[1]))
    bottom, top = nums(column(header, rows, header[2])), nums(
        column(header, rows, header[3]))
    fill = (rgba(column(header, rows, "fill colour"), "none")
            if "fill colour" in header
            else [st.get("face", "none")] * len(rows))
    edge = (rgba(column(header, rows, "edge colour"), "none")
            if "edge colour" in header
            else [st.get("edge", "none")] * len(rows))
    for i in range(len(rows)):
        s = styles[i] if len(styles) > i else st
        ax.add_patch(Rectangle((left[i], bottom[i]), right[i] - left[i],
                               top[i] - bottom[i],
                               **patch_kw(s, fill[i], edge[i], 0.5, 2)))


def draw_shapes(ax, path, st, styles):
    header, rows = read(path)
    if not rows:
        return
    keys = [n for n in ("shape", "part") if n in header]
    xi = header.index("vertex") + 1
    x = nums(column(header, rows, header[xi]))
    y = nums(column(header, rows, header[xi + 1]))
    fill = (rgba(column(header, rows, "fill colour"), "none")
            if "fill colour" in header else
            [st.get("face", st.get("colour", "#000000"))] * len(rows))
    edge = (rgba(column(header, rows, "edge colour"), "none")
            if "edge colour" in header
            else [st.get("edge", "none")] * len(rows))
    shape = (column(header, rows, "shape") if "shape" in header
             else ["1"] * len(rows))
    ids = [tuple(r[header.index(k)] for k in keys) for r in rows]
    order = list(dict.fromkeys(shape))
    start = 0
    for i in range(1, len(ids) + 1):
        if i == len(ids) or ids[i] != ids[start]:
            k = order.index(shape[start])
            s = styles[k] if len(styles) > k else st
            pts = np.column_stack([x[start:i], y[start:i]])
            closed = (len(pts) > 2
                      and np.allclose(pts[0], pts[-1], atol=1e-9))
            if fill[start] == "none" and not closed:
                # An open shape -- an arc, a bracket -- is a line, not a
                # polygon: closing it would cut a chord across it.
                opts = dict(color=edge[start], linewidth=s.get("lw", 0.5),
                            linestyle=ls_of(s), alpha=s.get("alpha"),
                            zorder=zo(s, 1),
                            clip_on=s.get("clip", True),
                            solid_capstyle=s.get("pcap", "butt"),
                            solid_joinstyle=s.get("pjoin", "miter"))
                ax.plot(pts[:, 0], pts[:, 1], **opts)
            elif s.get("collection"):
                p = patch_kw(s, fill[start], edge[start])
                coll = PolyCollection(
                    [pts], facecolors=p["facecolor"],
                    edgecolors=p["edgecolor"], linewidths=p["linewidth"],
                    linestyles=p["linestyle"], alpha=p["alpha"],
                    zorder=p["zorder"])
                coll.set_clip_on(p["clip_on"])
                for key in ("capstyle", "joinstyle", "hatch"):
                    if key in p:
                        getattr(coll, f"set_{key}")(p[key])
                ax.add_collection(coll, autolim=False)
            else:
                ax.add_patch(Polygon(pts, closed=True,
                                     **patch_kw(s, fill[start], edge[start])))
            start = i


def draw_wedges(ax, path, st, styles):
    header, rows = read(path)
    cx, cy = nums(column(header, rows, "centre x")), nums(
        column(header, rows, "centre y"))
    r = nums(column(header, rows, "outer radius"))
    w = nums(column(header, rows, "ring width"))
    t1 = nums(column(header, rows, "start angle (deg)"))
    t2 = nums(column(header, rows, "end angle (deg)"))
    fill = (rgba(column(header, rows, "fill colour"), "none")
            if "fill colour" in header
            else [st.get("face", "none")] * len(rows))
    edge = (rgba(column(header, rows, "edge colour"), "none")
            if "edge colour" in header
            else [st.get("edge", "none")] * len(rows))
    for i in range(len(rows)):
        s = styles[i] if len(styles) > i else st
        ax.add_patch(Wedge((cx[i], cy[i]), r[i], t1[i], t2[i],
                           width=None if np.isnan(w[i]) else w[i],
                           **patch_kw(s, fill[i], edge[i], 0.5)))


def draw_segments(ax, path, st, styles):
    header, rows = read(path)
    if not rows:
        return
    fr = [n for n in header if n.endswith(" from") and not n.startswith(
        "category")]
    to = [n for n in header if n.endswith(" to") and not n.startswith(
        "category")]
    if fr:
        segs = np.stack([np.column_stack([nums(column(header, rows, fr[0])),
                                          nums(column(header, rows, fr[1]))]),
                         np.column_stack([nums(column(header, rows, to[0])),
                                          nums(column(header, rows, to[1]))])],
                        axis=1)
    else:
        seg = ints(header, rows, "segment")
        xi = header.index("vertex") + 1
        x = nums(column(header, rows, header[xi]))
        y = nums(column(header, rows, header[xi + 1]))
        segs = [np.column_stack([x[seg == k], y[seg == k]])
                for k in sorted(set(seg.tolist()))]
    cols = (rgba(column(header, rows, "colour"), "#000000")
            if "colour" in header else st.get("colour", "#000000"))
    # Colours given outright would win over a colour map: a mapped
    # collection takes none.
    lc = LineCollection(segs, linewidths=st.get("lw", 0.5),
                        linestyles=ls_of(st), alpha=st.get("alpha"),
                        zorder=zo(st, 2),
                        **({} if "cmap" in st else {"colors": cols}))
    if "pcap" in st:
        lc.set_capstyle(st["pcap"])
    if "pjoin" in st:
        lc.set_joinstyle(st["pjoin"])
    lc.set_clip_on(st.get("clip", True))
    if "cmap" in st:
        vn = header[-1]
        lc.set_array(nums(column(header, rows, vn)))
        lc.set_cmap(cmap_of(st["cmap"]))
        lc.set_clim(*st["clim"])
    ax.add_collection(lc)


def draw_contours(ax, path, st, styles):
    header, rows = read(path)
    ids = [(r[0], r[1], r[2]) for r in rows]
    x = nums(column(header, rows, header[4]))
    y = nums(column(header, rows, header[5]))
    start = 0
    for i in range(1, len(ids) + 1):
        if i == len(ids) or ids[i] != ids[start]:
            ax.plot(x[start:i], y[start:i], **kw(st, "lw", "ls", "colour"),
                    zorder=zo(st, 2),
                    solid_capstyle=st.get("pcap", "butt"),
                    solid_joinstyle=st.get("pjoin", "round"))
            start = i


def block_extent(xs, ys, shape, extent, origin):
    """The extent a map's cells span, from their centres. A map averaged to
    print resolution (see the data folder's README) holds blocks of equal
    width but a last, shorter one, so its evenly spaced cells run past the
    extent by what that block lacks; None where the cells fill the extent
    exactly or their centres are not evenly spaced numbers."""
    out = list(extent)
    changed = False
    for centres, n, (i0, i1) in (
            (xs, shape[1], (0, 1)),
            (ys, shape[0], (3, 2) if origin == "upper" else (2, 3))):
        if n < 3 or not np.all(np.isfinite(centres)):
            continue
        step = centres[1] - centres[0]
        gaps = np.diff(centres)[:-1]
        # Even spacing, to the precision the CSV writes numbers at.
        tol = 1e-5 * float(np.max(np.abs(centres))) + 1e-4 * abs(step)
        if step == 0 or not np.allclose(gaps, step, rtol=0, atol=tol):
            continue
        start = out[i0]
        if abs(centres[0] - 0.5 * step - start) > 1e-3 * abs(step):
            continue
        end = start + n * step
        if abs(end - out[i1]) > 1e-3 * abs(step):
            out[i1] = end
            changed = True
    return out if changed else None


def draw_map(ax, path, st, styles, image):
    xs, ys, M = matrix(path)
    im = image or {}
    extent, origin = im.get("extent"), im.get("origin", "lower")
    spans = (block_extent(xs, ys, M.shape, extent, origin)
             if extent is not None else None)
    art = ax.imshow(np.ma.masked_invalid(M), extent=spans or extent,
                    origin=origin, cmap=cmap_of(st["cmap"]),
                    vmin=st["clim"][0], vmax=st["clim"][1],
                    interpolation=im.get("interpolation", "nearest"),
                    alpha=im.get("alpha"), zorder=zo(st, 0),
                    aspect="auto")
    if spans is not None:
        # Each block keeps its own width; what runs past the extent is cut.
        l, r, b, t = extent
        art.set_clip_path(Rectangle((min(l, r), min(b, t)), abs(r - l),
                                    abs(t - b), transform=ax.transData))


def draw_strip(ax, path, st, styles, image):
    header, rows = read(path)
    v = nums(column(header, rows, header[1]))
    im = image or {}
    ax.imshow(np.ma.masked_invalid(v[None, :]), extent=im.get("extent"),
              origin=im.get("origin", "lower"), cmap=cmap_of(st["cmap"]),
              vmin=st["clim"][0], vmax=st["clim"][1],
              interpolation=im.get("interpolation", "nearest"),
              zorder=zo(st, 0), aspect="auto")


def draw_image(ax, path, st, styles, image):
    im = image or {}
    # The PNG holds the picture as it prints, top row first; an image the
    # page drew from its bottom row up is turned back to that order.
    pic = plt.imread(path)
    origin = im.get("origin", "upper")
    if origin == "lower":
        pic = pic[::-1]
    ax.imshow(pic, extent=im.get("extent"), origin=origin,
              interpolation=im.get("interpolation", "nearest"),
              alpha=im.get("alpha"), zorder=zo(st, 0),
              aspect="auto")


def draw_key(ax, path, st, styles, image):
    """A hand-made colour key: its colours, in the order it prints them."""
    header, rows = read(path)
    cols = column(header, rows, "colour")
    im = image or {}
    ext = im.get("extent")
    # The key runs the way the page drew it (one row or one column); its
    # colours are in the order of the page's image, which `origin` then
    # puts the right way up.
    across = st.get("along", "x" if ext is not None and abs(
        ext[1] - ext[0]) >= abs(ext[3] - ext[2]) else "y") == "x"
    ramp = np.linspace(0.0, 1.0, len(cols))
    ax.imshow(ramp[None, :] if across else ramp[:, None],
              extent=ext, origin=im.get("origin", "lower"),
              cmap=ListedColormap(cols), vmin=0, vmax=1,
              interpolation=im.get("interpolation", "nearest"),
              zorder=zo(st, 0), aspect="auto")


def draw_ribbons(ax, path, st, styles):
    header, rows = read(path)
    if not rows:
        return
    xl = nums(column(header, rows, "x at left end"))
    xr = nums(column(header, rows, "x at right end"))
    bl = nums(column(header, rows, "bottom at left end"))
    tl = nums(column(header, rows, "top at left end"))
    br = nums(column(header, rows, "bottom at right end"))
    tr = nums(column(header, rows, "top at right end"))
    cols = column(header, rows, "colour")
    if "left box" in header:
        # A Sankey's bands: each a closed cubic Bezier path whose edges
        # leave and arrive level, the control points midway across.
        C4 = MPath.CURVE4
        codes = [MPath.MOVETO, C4, C4, C4, MPath.LINETO, C4, C4, C4,
                 MPath.CLOSEPOLY]
        for i in range(len(rows)):
            s = styles[i] if len(styles) > i else st
            x0, x1, a, b = xl[i], xr[i], bl[i], br[i]
            w = tl[i] - bl[i]
            xm = 0.5 * (x0 + x1)
            verts = [(x0, a), (xm, a), (xm, b), (x1, b), (x1, b + w),
                     (xm, b + w), (xm, a + w), (x0, a + w), (x0, a)]
            ax.add_patch(PathPatch(MPath(verts, codes),
                                   **patch_kw(s, cols[i],
                                              s.get("edge", "none"))))
        return
    t = np.linspace(0, 1, 60)
    sm = t * t * (3 - 2 * t)
    for i in range(len(rows)):
        ax.fill_between(xl[i] + (xr[i] - xl[i]) * t,
                        bl[i] + (br[i] - bl[i]) * sm,
                        tl[i] + (tr[i] - tl[i]) * sm, facecolor=cols[i],
                        alpha=st.get("alpha"), linewidth=0,
                        zorder=zo(st, 2))


def draw_steps(ax, path, st, styles):
    """Step plots: the value held between two edges, one row a step."""
    header, rows = read(path)
    if not rows:
        return
    plot = (ints(header, rows, "step plot") if "step plot" in header
            else np.ones(len(rows), int))
    names = [n for n in header if n not in ("step plot", "line colour",
                                            "fill colour")]
    lo, hi, val = (nums(column(header, rows, n)) for n in names[:3])
    lines = (column(header, rows, "line colour") if "line colour" in header
             else None)
    fills = (column(header, rows, "fill colour") if "fill colour" in header
             else None)
    for i, k in enumerate(sorted(set(plot.tolist()))):
        m = plot == k
        first = int(np.flatnonzero(m)[0])
        s = styles[i] if len(styles) > i else st
        edge = lines[first] if lines else s.get("edge", "none")
        face = fills[first] if fills else s.get("face", "none")
        ax.stairs(val[m], np.r_[lo[m], hi[m][-1]],
                  orientation=s.get("orientation", "vertical"),
                  baseline=s.get("baseline"), fill=s.get("fill", False),
                  **{k_: v for k_, v in patch_kw(s, face, edge).items()
                     if k_ != "fill"})


def draw_flows(ax, path, st, styles):
    """The Sankey's counts, left boxes by right boxes: data only; its
    ribbons and boxes draw it."""


DRAW = {"points": draw_points, "lines": draw_lines, "other_lines": draw_lines,
        "bars": draw_bars, "boxes": draw_boxes, "shapes": draw_shapes,
        "wedges": draw_wedges, "segments": draw_segments,
        "contours": draw_contours, "ribbons": draw_ribbons,
        "steps": draw_steps, "flows": draw_flows}
IMAGES = {"map": draw_map, "strip": draw_strip, "image": draw_image,
          "colour_key": draw_key}


# ---------------------------------------------------------------------------
# Laying the panel out
# ---------------------------------------------------------------------------
def place(fig, sp):
    """An axes at the rectangle the page gives it, inches from the top-left,
    set up as the page sets it up."""
    l, t, w, h = sp["rect"]
    rect = sp.get("pos") or [l / PAGE[0], 1.0 - (t + h) / PAGE[1],
                             w / PAGE[0], h / PAGE[1]]
    three = sp.get("three_d")
    ax = fig.add_axes(rect, projection="3d" if three else None)
    if sp.get("zorder") not in (None, 0):
        ax.set_zorder(sp["zorder"])
    if sp.get("facecolor"):
        ax.set_facecolor(sp["facecolor"])
    if sp.get("frame") is False:
        ax.patch.set_visible(False)
    ax.set_xscale(sp["xscale"])
    ax.set_yscale(sp["yscale"])
    # A spine moved off its edge carries its ticks with it; moving it
    # resets the ticks, so it comes before them.
    for side, s in sp["spines"].items():
        if s.get("position") and side in ax.spines:
            pos = s["position"]
            ax.spines[side].set_position(tuple(pos) if isinstance(pos, list)
                                         else pos)
    # Ticks first, limits after: setting ticks widens the limits to hold
    # them, so the page's limits have to be the last word.
    axes_ticks = [("x", sp["xticks"]), ("y", sp["yticks"])]
    if three:
        ax.set_zlim(three["zlim"])
        axes_ticks.append(("z", three["zticks"]))
    for axis, ts in axes_ticks:
        getattr(ax, f"set_{axis}ticks")(ts["at"])
        if ts["labels"]:
            getattr(ax, f"set_{axis}ticklabels")(
                ts["labels"], rotation=ts.get("rotation", 0),
                ha=ts.get("ha", "center"), va=ts.get("va", "top"),
                fontsize=ts.get("labelsize", FONT["tick"]))
        if ts.get("rotation_mode"):
            for txt in getattr(ax, f"get_{axis}ticklabels")():
                txt.set_rotation_mode(ts["rotation_mode"])
        mi = ts.get("minor")
        if not mi and not three:
            # No minor ticks on the page: a log axis would add its own.
            getattr(ax, f"set_{axis}ticks")([], minor=True)
        if mi:
            getattr(ax, f"set_{axis}ticks")(mi["at"], minor=True)
            getattr(ax, f"set_{axis}ticklabels")(
                mi["labels"] or [""] * len(mi["at"]), minor=True,
                fontsize=ts.get("labelsize", FONT["tick"]))
            ax.tick_params(axis=axis, which="minor",
                           direction=mi["direction"], length=mi["size"],
                           width=mi["width"], pad=mi["pad"],
                           color=mi["colour"] or AXIS_COLOUR,
                           **dict(zip(("bottom", "top") if axis == "x"
                                      else ("left", "right"),
                                      mi["visible"])))
        ax.tick_params(axis=axis, direction=ts.get("direction", "out"),
                       length=ts.get("size", 2.7), width=ts.get("width", 0.6),
                       pad=ts.get("pad", 1.5),
                       labelsize=ts.get("labelsize", FONT["tick"]),
                       color=ts.get("colour", AXIS_COLOUR),
                       labelcolor=ts.get("labelcolour", AXIS_COLOUR))
        sides = ("bottom", "top") if axis == "x" else ("left", "right")
        # Which sides carry ticks and labels (a 3-D axis has one side).
        if ts.get("visible") and not three:
            ax.tick_params(axis=axis, **dict(zip(sides, ts["visible"])))
        if ts.get("label_visible") and not three:
            ax.tick_params(axis=axis, **{"label" + k: v for k, v in zip(
                sides, ts["label_visible"])})
        if ts.get("label_colours"):
            texts = getattr(ax, f"get_{axis}ticklabels")()
            for txt, col in zip(texts, ts["label_colours"]):
                txt.set_color(col)
    ax.set_xlim(sp["xlim"])
    ax.set_ylim(sp["ylim"])
    # Nothing drawn afterwards may rescale them either.
    ax.set_autoscalex_on(False)
    ax.set_autoscaley_on(False)
    if three:
        ax.set_zlim(three["zlim"])
        ax.set_autoscalez_on(False)
    # The axes is placed where the page's aspect left it ("pos"), so its
    # aspect is not set again: re-fitting the box would move it by a
    # rounding error, and an image by a pixel.
    if three and sp.get("aspect") not in (None, "auto"):
        ax.set_aspect(sp["aspect"])
    for side, s in sp["spines"].items():
        if side not in ax.spines:
            continue
        ax.spines[side].set_visible(s["visible"])
        ax.spines[side].set_linewidth(s["lw"])
        ax.spines[side].set_color(s["colour"] or AXIS_COLOUR)
        if s.get("bounds"):
            ax.spines[side].set_bounds(*s["bounds"])
    ol = sp["spines"].get("outline")
    if ol and ol["visible"]:
        # A colour bar's frame: one outline round the bar, not four spines.
        ax.add_patch(Rectangle((0, 0), 1, 1, transform=ax.transAxes,
                               fill=False, linewidth=ol["lw"],
                               edgecolor=ol["colour"] or AXIS_COLOUR,
                               zorder=2.5, clip_on=False))
    for axis in ("x", "y", "z"):
        lab = sp.get(f"{axis}label") if axis != "z" else (
            (sp.get("three_d") or {}).get("zlabel"))
        if lab and hasattr(ax, f"set_{axis}label"):
            getattr(ax, f"set_{axis}label")(
                lab["text"], fontsize=lab["size"], color=lab["colour"],
                labelpad=lab["pad"])
            art = getattr(ax, f"{axis}axis").label
            if lab.get("rotation") is not None:
                art.set_rotation(lab["rotation"])
            for key, setter in (("ha", art.set_ha), ("va", art.set_va),
                                ("weight", art.set_fontweight),
                                ("linespacing", art.set_linespacing)):
                if lab.get(key):
                    setter(lab[key])
            if lab.get("coords"):
                getattr(ax, f"{axis}axis").set_label_coords(*lab["coords"])
            elif lab.get("along") is not None:
                (art.set_x if axis == "x" else art.set_y)(lab["along"])
    if sp.get("xlabel_side"):
        ax.xaxis.set_label_position(sp["xlabel_side"])
    if sp.get("ylabel_side"):
        ax.yaxis.set_label_position(sp["ylabel_side"])
    if sp.get("title"):
        ti = sp["title"]
        opts = dict(fontsize=ti["size"], color=ti["colour"],
                    fontweight=ti.get("weight", "normal"))
        if ti.get("pad") is not None:
            opts["pad"] = ti["pad"]
        if ti.get("y") is not None:
            opts["y"] = ti["y"]
        if ti.get("x") is not None:
            opts["x"] = ti["x"]
        ax.set_title(ti["text"], **opts)
    if three:
        ax.set_box_aspect(three["box_aspect"], zoom=three.get("zoom", 1.0))
        ax.view_init(*three["view"])
        trio = (ax.xaxis, ax.yaxis, ax.zaxis)
        for a, pane in zip(trio, three["panes"]):
            a.pane.set_facecolor(pane["face"])
            a.pane.set_edgecolor(pane["edge"])
            if pane.get("lw") is not None:
                a.pane.set_linewidth(pane["lw"])
            if "alpha" in pane:
                a.pane.set_alpha(pane["alpha"])
        for a, line in zip(trio, three.get("lines", [])):
            a.line.set_color(line["colour"])
            a.line.set_linewidth(line["lw"])
        for a, rot in zip(trio, three.get("rotate_label", [])):
            a.set_rotate_label(rot)
        for a, info in zip(trio, three.get("axinfo", [])):
            a._axinfo["grid"].update(info["grid"])
            tick = dict(info["tick"])
            if "linewidth" in tick:
                major, minor = tick.pop("linewidth")
                a._axinfo["tick"]["linewidth"] = {True: major, False: minor}
            a._axinfo["tick"].update(tick)
        ax.grid(three.get("grid", True))
    if sp.get("axis_off"):
        ax.set_axis_off()
    return ax


def draw_decor(ax, sp):
    """The cage wireframes, category outlines and category boundaries the
    page draws over a panel; the data folder leaves them out."""
    for d in sp.get("decor", []):
        st = dict(d["style"])
        # A contour carries its colour as an edge colour, a line as its own.
        st.setdefault("colour", st.get("edge", AXIS_COLOUR))
        opts = dict(kw(st, "lw", "ls", "colour", "alpha"),
                    zorder=zo(st, 1),
                    solid_capstyle=st.get("capstyle",
                                          st.get("pcap", "projecting")),
                    solid_joinstyle=st.get("joinstyle",
                                           st.get("pjoin", "round")),
                    dash_capstyle=st.get("dash_capstyle", "butt"),
                    clip_on=st.get("clip", True))
        if d["kind"] == "vline":
            ax.axvline(d["at"], **opts)
        elif d["kind"] == "patch":
            pts = np.array(SPEC["shapes"][d["shape"]], dtype=float)
            face = (st.get("face", "none") if st.get("filled", True)
                    else "none")
            p = patch_kw(st, face, st.get("edge", AXIS_COLOUR))
            p.pop("fill", None)
            ax.add_patch(Polygon(pts, closed=True, transform=ax.transAxes,
                                 **p))
        else:
            pts = np.array(SPEC["shapes"][d["shape"]], dtype=float)
            line, = ax.plot(pts[:, 0], pts[:, 1], **opts)
            if d.get("simplify") is False:
                # Drawn through every point, as the page drew it.
                line.get_path().should_simplify = False


def draw_annotations(ax, sp, rows, header):
    """The panel's texts that sit inside this subplot, from
    annotations.csv; their type is the page's."""
    if not rows:
        return
    sub = column(header, rows, "subplot")
    text = column(header, rows, "text")
    x, y = nums(column(header, rows, "x")), nums(column(header, rows, "y"))
    where = column(header, rows, "coordinates")
    tx = (nums(column(header, rows, "target x")) if "target x" in header
          else np.full(len(rows), np.nan))
    ty = (nums(column(header, rows, "target y")) if "target y" in header
          else np.full(len(rows), np.nan))
    styles = sp.get("text_style", [])
    k = 0
    for i in range(len(rows)):
        if sub[i] != sp["name"] or where[i] != "data":
            continue
        st = styles[k] if k < len(styles) else {}
        k += 1
        if st.get("offsetbox"):
            draw_words(ax, st["offsetbox"])
            continue
        opts = dict(fontsize=st.get("size", FONT["label"]),
                    color=st.get("colour", AXIS_COLOUR),
                    ha=st.get("ha", "left"), va=st.get("va", "baseline"),
                    rotation=st.get("rotation", 0),
                    fontweight=st.get("weight", "normal"),
                    fontstyle=st.get("style", "normal"),
                    zorder=zo(st, 3))
        for key in ("linespacing", "multialignment", "rotation_mode"):
            if key in st:
                opts[key] = st[key]
        if st.get("clip"):
            opts["clip_on"] = True
        if st.get("bbox"):
            b = st["bbox"]
            opts["bbox"] = dict(facecolor=b["face"], edgecolor=b["edge"],
                                linewidth=b["lw"], alpha=b["alpha"],
                                boxstyle=f"square,pad={b['pad']}")
        words = st.get("raw", text[i])
        # An annotation's leader line runs from its text to the point it
        # marks, `target x` and `target y` in annotations.csv.
        target = (tx[i], ty[i])
        if st.get("arrow") and np.all(np.isfinite(target)):
            ax.annotate(words, xy=target, xycoords="data",
                        xytext=(x[i], y[i]), textcoords="data",
                        arrowprops=dict(st["arrow"]), **opts)
        else:
            ax.text(x[i], y[i], words, **opts)


def draw_words(ax, ob):
    """A title in words of several colours: one text a part, set in a row
    and anchored where the page anchored it."""
    boxes = [TextArea(p["text"], textprops=dict(
        color=p["colour"], fontsize=p["size"], fontweight=p["weight"],
        fontname=FONT["name"])) for p in ob["parts"]]
    row = HPacker(children=boxes, align=ob["align"], pad=ob["pad"],
                  sep=ob["sep"])
    box = AnchoredOffsetbox(loc=ob["loc"], child=row, pad=ob["box_pad"],
                            borderpad=ob["borderpad"],
                            frameon=ob["frameon"],
                            bbox_to_anchor=Bbox.from_bounds(*ob["anchor"]),
                            bbox_transform=ax.figure.transFigure)
    box.set_zorder(ob["zorder"])
    ax.add_artist(box)


def draw_page_texts(fig):
    """The titles, counts and names the page prints around the subplots,
    and the panel's letter."""
    for t in PANEL["texts"]:
        opts = dict(fontsize=t["size"], fontweight=t["weight"], ha=t["ha"],
                    va=t["va"], rotation=t["rotation"], color=t["colour"],
                    fontstyle=t.get("style", "normal"))
        for key in ("linespacing", "multialignment", "zorder",
                    "rotation_mode"):
            if key in t:
                opts[key] = t[key]
        fig.text(t["x"] / PAGE[0], 1.0 - t["y"] / PAGE[1], t["text"], **opts)
    L = PANEL.get("letter")
    if L:
        fig.text(L["x"] / PAGE[0], 1.0 - L["baseline"] / PAGE[1],
                 f"{L['ch']})", fontsize=FONT["letter"], fontweight="bold",
                 ha="left", va="baseline", color=LETTER_COLOUR)


def draw_page_shapes(fig, folder):
    """What the panel draws on the page itself -- rules, arrows, key
    swatches -- from page_shapes.csv, in inches from the page's top-left."""
    ps = PANEL.get("page_shapes")
    if not ps:
        return
    header, rows = read(need(folder / ps["file"]))
    shape = ints(header, rows, "shape")
    part = (ints(header, rows, "part") if "part" in header
            else np.ones(len(rows), int))
    x = nums(column(header, rows, "x (in)")) / PAGE[0]
    y = 1.0 - nums(column(header, rows, "y (in)")) / PAGE[1]
    fills = (column(header, rows, "fill colour") if "fill colour" in header
             else None)
    edges = (column(header, rows, "edge colour") if "edge colour" in header
             else None)
    for k in sorted(set(shape.tolist())):
        s = ps["styles"][k - 1]
        m = shape == k
        first = int(np.flatnonzero(m)[0])
        edge = edges[first] if edges else s.get("edge", s.get("colour"))
        face = fills[first] if fills else s.get("face", "none")
        if s["type"] == "Line2D":
            fig.add_artist(Line2D(x[m], y[m], transform=fig.transFigure,
                                  **line_kw(s, edge)))
            continue
        for p in sorted(set(part[m].tolist())):
            q = m & (part == p)
            pts = np.column_stack([x[q], y[q]])
            closed = len(pts) > 2 and np.allclose(pts[0], pts[-1],
                                                  atol=1e-9)
            codes = [MPath.MOVETO] + [MPath.LINETO] * (len(pts) - 1)
            if closed:
                codes[-1] = MPath.CLOSEPOLY
            # An arrow's shaft is stroked, its head filled, as an arrow
            # patch draws them; any other closed outline takes its fill.
            filled = closed and s.get("filled", True) and face != "none"
            opts = patch_kw(s, face if filled else "none", edge)
            opts.pop("fill", None)
            # An arrow is not snapped to the pixel grid: the page's arrow
            # shafts were not quite level and so drew unsnapped; read back
            # from the file they are level, and snapping moved them half
            # a pixel. Boxes snap, as the page's did.
            snap = False if s["type"] == "FancyArrowPatch" else None
            fig.add_artist(PathPatch(MPath(pts, codes), snap=snap,
                                     transform=fig.transFigure, **opts))


def draw_legends(fig):
    for leg in PANEL["legends"]:
        handles = []
        for e in leg["entries"]:
            st = e["style"]
            if e["kind"] == "Line2D":
                handles.append(Line2D([], [], color=st.get("colour", "k"),
                                      linewidth=st.get("lw", 1.0),
                                      linestyle=ls_of(st, "-"),
                                      marker=marker_of(st, "None"),
                                      markersize=st.get("ms", 6),
                                      markerfacecolor=st.get(
                                          "mfc", st.get("face")),
                                      markeredgecolor=st.get(
                                          "mec", st.get("edge")),
                                      markeredgewidth=st.get("mew", 1.0),
                                      solid_capstyle=st.get(
                                          "capstyle", "projecting"),
                                      label=e["label"]))
            elif e["kind"] == "PathCollection":
                handles.append(Line2D([], [], linestyle="none",
                                      marker=marker_of(st),
                                      markersize=np.sqrt(st.get("area", 36)),
                                      markerfacecolor=st.get("face", "k"),
                                      markeredgecolor=st.get("edge", "none"),
                                      markeredgewidth=st.get("lw", 0.0),
                                      label=e["label"]))
            else:
                handles.append(Patch(facecolor=st.get("face", "k"),
                                     edgecolor=st.get("edge", "none"),
                                     linewidth=st.get("lw", 0.0),
                                     alpha=st.get("alpha"),
                                     label=e["label"]))
        opts = {}
        for k in ("handleheight", "markerscale", "numpoints",
                  "scatterpoints", "alignment", "markerfirst"):
            if k in leg:
                opts[k] = leg[k]
        lg = fig.legend(handles=handles, loc=leg["loc"], ncol=leg["ncol"],
                        bbox_to_anchor=tuple(leg["anchor"]),
                        bbox_transform=fig.transFigure,
                        frameon=leg["frameon"],
                        fontsize=leg["size"] or FONT["legend"],
                        borderpad=leg.get("borderpad", 0.0),
                        borderaxespad=leg.get("borderaxespad", 0.0),
                        handlelength=leg.get("handlelength", 2.0),
                        handletextpad=leg.get("handletextpad", 0.8),
                        labelspacing=leg.get("labelspacing", 0.5),
                        columnspacing=leg.get("columnspacing", 2.0),
                        title=leg.get("title"),
                        title_fontsize=leg.get("title_size"), **opts)
        for txt, e in zip(lg.get_texts(), leg["entries"]):
            if e.get("text_colour"):
                txt.set_color(e["text_colour"])
        if leg.get("frame"):
            fr = leg["frame"]
            lg.get_frame().set_facecolor(fr["face"])
            lg.get_frame().set_edgecolor(fr["edge"])
            lg.get_frame().set_linewidth(fr["lw"])
            lg.get_frame().set_alpha(fr["alpha"])


# ---------------------------------------------------------------------------
# Drawing the panel
# ---------------------------------------------------------------------------
def draw(fig, data=None):
    """Draw the panel onto a page-sized figure, at its place on the page,
    from its data folder (`DATA` unless another is given); a file missing
    from it stops the script (`need`)."""
    # Normalised, so that DATA's ".." parts do not count towards the
    # Windows path length limit.
    folder = Path(os.path.normpath(data if data else DATA))
    plt.rcParams["font.family"] = FONT["name"]
    ann = (read(need(folder / "annotations.csv")) if ANNOTATIONS
           else (None, []))
    axes = []
    for sp in PANEL["subplots"]:
        axes.append(place(fig, sp) if sp.get("draw_into") is None else None)
    for i, sp in enumerate(PANEL["subplots"]):
        ax = axes[i] if axes[i] is not None else axes[sp["draw_into"]]
        if axes[i] is None:
            # An overlay drawn over the page is drawn into the subplot whose
            # coordinates it uses, which then goes over its neighbours, as
            # the overlay did.
            ax.set_zorder(max(ax.get_zorder(), sp.get("zorder") or 0)
                          + 1e-6)
        cb = sp.get("cbar")
        if cb is not None:
            # A colour bar keys the data beside it, so the data folder
            # holds no file for it: its ramp is drawn from the colour map.
            ramp = np.linspace(0.0, 1.0, 256)
            vertical = cb["orientation"] == "vertical"
            ax.imshow(ramp[:, None] if vertical else ramp[None, :],
                      extent=[sp["xlim"][0], sp["xlim"][1],
                              sp["ylim"][0], sp["ylim"][1]],
                      origin="lower", cmap=cmap_of(cb["cmap"]), vmin=0.0,
                      vmax=1.0, aspect="auto", interpolation="bilinear",
                      zorder=0)
        images = list(sp.get("images", []))
        for f in sp["files"]:
            path = need(folder / f["file"])
            st, styles = f["style"], f.get("styles", [])
            before = set(ax.get_children())
            if f["kind"] in IMAGES:
                IMAGES[f["kind"]](ax, path, st, styles,
                                  images.pop(0) if images else None)
            elif f["kind"] in DRAW:
                DRAW[f["kind"]](ax, path, st, styles)
            # Artists the page drew as a raster (their style says so), the
            # file's artists taking its styles in order.
            new = [art for art in ax.get_children() if art not in before]
            for k, art in enumerate(new):
                if (styles[k] if k < len(styles) else st).get("rasterized"):
                    art.set_rasterized(True)
        draw_decor(ax, sp)
        if axes[i] is not None:
            draw_annotations(ax, sp, ann[1], ann[0])
        for t in sp.get("bar_texts", []):
            ax.text(t["x"], t["y"], t["text"], transform=ax.transAxes,
                    fontsize=t["size"], color=t["colour"], ha=t["ha"],
                    va=t["va"], rotation=t["rotation"],
                    fontweight=t["weight"], zorder=t["zorder"],
                    clip_on=t.get("clip", False))
    draw_page_texts(fig)
    draw_page_shapes(fig, folder)
    draw_legends(fig)
    return fig


#: Text in a PDF stays TrueType text (as on the published pages), not
#: Type 3 glyph drawings, so it can be edited and searched.
PDF_FONTS = {"pdf.fonttype": 42, "ps.fonttype": 42}
#: No creation date in a PDF, so rendering the same data again writes the
#: same bytes (a PNG carries only matplotlib's version).
PDF_METADATA = {"CreationDate": None}


def ink_box(fig, pad=0.05):
    """(box, pixels): the panel's box on the page -- every pixel the figure
    inks at DPI, plus `pad`, on whole pixels and inside the page -- in
    inches, and the page's pixels inside it.

    The figure holds this panel alone, so what it inks is the panel. Its
    tight box is not used: that measures a rotated or long x label from
    its centre and leaves out 3-D axis labels, so it cut them off, and it
    spans the whole page for an overlay drawn into a page-sized axes. The
    PNG is these pixels as they are, not a second, cropped drawing, so it
    holds exactly what the page prints there."""
    fig.set_dpi(DPI)
    fig.canvas.draw()
    rgba = np.asarray(fig.canvas.buffer_rgba())
    rows, cols = np.nonzero((rgba[..., :3] < 255).any(axis=2))
    if not len(rows):
        return "tight", None
    h, w = rgba.shape[:2]
    p = int(round(pad * DPI))
    x0, x1 = max(cols.min() - p, 0), min(cols.max() + 1 + p, w)
    y0, y1 = max(rows.min() - p, 0), min(rows.max() + 1 + p, h)
    box = Bbox.from_extents(x0 / DPI, (h - y1) / DPI, x1 / DPI,
                            (h - y0) / DPI)
    return box, rgba[y0:y1, x0:x1].copy()


def render(data=None, out_dir=None, formats=("pdf", "png")):
    """Draw the panel and write NAME.<format> into `out_dir` (`OUT`
    unless another is given): the panel cut from its page, at DPI."""
    out = Path(os.path.normpath(out_dir if out_dir else OUT))
    out.mkdir(parents=True, exist_ok=True)
    written = []
    with plt.rc_context(PDF_FONTS):
        fig = plt.figure(figsize=PAGE, facecolor="w")
        try:
            draw(fig, data)
            box, pixels = ink_box(fig)
            for ext in formats:
                path = out / f"{NAME}.{ext}"
                if ext == "png" and pixels is not None:
                    plt.imsave(path, pixels, dpi=DPI)
                else:
                    fig.savefig(path, dpi=DPI, bbox_inches=box,
                                pad_inches=0, facecolor="w",
                                metadata=(PDF_METADATA if ext == "pdf"
                                          else None))
                written.append(path)
        finally:
            plt.close(fig)
    return written


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.strip().split("\n")[0])
    ap.add_argument("--data", help="the panel's data folder "
                                   "(default: DATA, beside the code folder)")
    ap.add_argument("--out-dir",
                    help="where to write the panel (default: OUT, "
                         "figures/fig5)")
    a = ap.parse_args(argv)
    for path in render(a.data, a.out_dir):
        print(f"wrote {os.path.normpath(path)}")


if __name__ == "__main__":
    main()
