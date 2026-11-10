r"""
Figure S12, panel a: one animal's cell maps under the tablet.

Panel id figS12_a_example_tablet. Title: "Example animal: tablet (n = 2
sessions)".

Redrawn from the panel's data folder, data/figS12/figS12_a_example_tablet/
(DATA below), with numpy and matplotlib alone: what the panel shows is read
from that folder, and how the page lays it out -- the axes' rectangles in
page inches, limits, ticks, labels, titles, legends, colour maps, drawing
styles, and the decoration the data leave out (cage wireframes, category
outlines, category boundaries) -- is written below as literals, measured
off the published page.

Usage:

    python figS12_a_example_tablet.py [--data DIR] [--out-dir DIR]

writes figS12_a_example_tablet.pdf and figS12_a_example_tablet.png (400
dpi), the panel cut from its page, into supplemental_figures/figS12/ (OUT
below); figS12_page.py draws the whole page and code/render_all.py every
figure.
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
DATA = os.path.join(HERE, "..", "..", "data", "figS12", "figS12_a_example_tablet")
OUT = os.path.join(HERE, "..", "..", "supplemental_figures", "figS12")
NAME = "figS12_a_example_tablet"
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
SPEC = {'cmaps': {'cmap0': {'colours': ['#ffffffff',
                                 '#fefeffff',
                                 '#fefeffff',
                                 '#fdfdffff',
                                 '#fdfcfeff',
                                 '#fcfcfeff',
                                 '#fcfbfeff',
                                 '#fbfafeff',
                                 '#fbfafeff',
                                 '#faf9feff',
                                 '#faf8feff',
                                 '#f9f8fdff',
                                 '#f9f7fdff',
                                 '#f8f6fdff',
                                 '#f7f6fdff',
                                 '#f7f5fdff',
                                 '#f6f4fdff',
                                 '#f6f4fdff',
                                 '#f5f3fdff',
                                 '#f5f3fcff',
                                 '#f4f2fcff',
                                 '#f4f1fcff',
                                 '#f3f1fcff',
                                 '#f3f0fcff',
                                 '#f2effcff',
                                 '#f1effcff',
                                 '#f1eefbff',
                                 '#f0edfbff',
                                 '#f0edfbff',
                                 '#efecfbff',
                                 '#efebfbff',
                                 '#eeebfbff',
                                 '#eeeafbff',
                                 '#ede9faff',
                                 '#ede9faff',
                                 '#ece8faff',
                                 '#ebe7faff',
                                 '#ebe7faff',
                                 '#eae6faff',
                                 '#eae6faff',
                                 '#e9e5f9ff',
                                 '#e9e4f9ff',
                                 '#e8e4f9ff',
                                 '#e8e3f9ff',
                                 '#e7e2f9ff',
                                 '#e7e2f9ff',
                                 '#e6e1f9ff',
                                 '#e5e0f8ff',
                                 '#e5e0f8ff',
                                 '#e4dff8ff',
                                 '#e4def8ff',
                                 '#e3def8ff',
                                 '#e3ddf8ff',
                                 '#e2dcf8ff',
                                 '#e2dcf7ff',
                                 '#e1dbf7ff',
                                 '#e1dbf7ff',
                                 '#e0daf7ff',
                                 '#dfd9f7ff',
                                 '#dfd9f7ff',
                                 '#ded8f6ff',
                                 '#ded7f6ff',
                                 '#ddd7f6ff',
                                 '#ddd6f6ff',
                                 '#dcd5f6ff',
                                 '#dcd5f6ff',
                                 '#dbd4f6ff',
                                 '#dad4f5ff',
                                 '#dad3f5ff',
                                 '#d9d2f5ff',
                                 '#d9d2f5ff',
                                 '#d8d1f5ff',
                                 '#d8d0f5ff',
                                 '#d7d0f5ff',
                                 '#d7cff4ff',
                                 '#d6cef4ff',
                                 '#d5cef4ff',
                                 '#d5cdf4ff',
                                 '#d4cdf4ff',
                                 '#d4ccf4ff',
                                 '#d3cbf4ff',
                                 '#d3cbf3ff',
                                 '#d2caf3ff',
                                 '#d2c9f3ff',
                                 '#d1c9f3ff',
                                 '#d0c8f3ff',
                                 '#d0c7f3ff',
                                 '#cfc7f2ff',
                                 '#cfc6f2ff',
                                 '#cec6f2ff',
                                 '#cec5f2ff',
                                 '#cdc4f2ff',
                                 '#cdc4f2ff',
                                 '#ccc3f2ff',
                                 '#cbc2f1ff',
                                 '#cbc2f1ff',
                                 '#cac1f1ff',
                                 '#cac1f1ff',
                                 '#c9c0f1ff',
                                 '#c9bff1ff',
                                 '#c8bff1ff',
                                 '#c7bef0ff',
                                 '#c7bdf0ff',
                                 '#c6bdf0ff',
                                 '#c6bcf0ff',
                                 '#c5bbf0ff',
                                 '#c5bbf0ff',
                                 '#c4baefff',
                                 '#c3baefff',
                                 '#c3b9efff',
                                 '#c2b8efff',
                                 '#c2b8efff',
                                 '#c1b7efff',
                                 '#c1b7eeff',
                                 '#c0b6eeff',
                                 '#bfb5eeff',
                                 '#bfb5eeff',
                                 '#beb4eeff',
                                 '#beb3eeff',
                                 '#bdb3eeff',
                                 '#bdb2edff',
                                 '#bcb2edff',
                                 '#bbb1edff',
                                 '#bbb0edff',
                                 '#bab0edff',
                                 '#baafedff',
                                 '#b9aeecff',
                                 '#b9aeecff',
                                 '#b8adecff',
                                 '#b7adecff',
                                 '#b7acecff',
                                 '#b6abecff',
                                 '#b6abecff',
                                 '#b5aaebff',
                                 '#b5aaebff',
                                 '#b4a9ebff',
                                 '#b3a8ebff',
                                 '#b3a8ebff',
                                 '#b2a7ebff',
                                 '#b2a6eaff',
                                 '#b1a6eaff',
                                 '#b0a5eaff',
                                 '#b0a5eaff',
                                 '#afa4eaff',
                                 '#afa3eaff',
                                 '#aea3e9ff',
                                 '#ada2e9ff',
                                 '#ada2e9ff',
                                 '#aca1e9ff',
                                 '#aca0e9ff',
                                 '#aba0e9ff',
                                 '#ab9fe8ff',
                                 '#aa9ee8ff',
                                 '#a99ee8ff',
                                 '#a99de8ff',
                                 '#a89de8ff',
                                 '#a89ce8ff',
                                 '#a79be8ff',
                                 '#a69be7ff',
                                 '#a69ae7ff',
                                 '#a59ae7ff',
                                 '#a599e7ff',
                                 '#a498e7ff',
                                 '#a398e7ff',
                                 '#a397e6ff',
                                 '#a297e6ff',
                                 '#a296e6ff',
                                 '#a195e6ff',
                                 '#a095e6ff',
                                 '#a094e6ff',
                                 '#9f94e5ff',
                                 '#9e93e5ff',
                                 '#9e92e5ff',
                                 '#9d92e5ff',
                                 '#9d91e5ff',
                                 '#9c91e5ff',
                                 '#9b90e4ff',
                                 '#9b8fe4ff',
                                 '#9a8fe4ff',
                                 '#9a8ee4ff',
                                 '#998ee4ff',
                                 '#988de4ff',
                                 '#988ce3ff',
                                 '#978ce3ff',
                                 '#968be3ff',
                                 '#968be3ff',
                                 '#958ae3ff',
                                 '#9589e3ff',
                                 '#9489e2ff',
                                 '#9388e2ff',
                                 '#9388e2ff',
                                 '#9287e2ff',
                                 '#9186e2ff',
                                 '#9186e2ff',
                                 '#9085e1ff',
                                 '#9085e1ff',
                                 '#8f84e1ff',
                                 '#8e84e1ff',
                                 '#8e83e1ff',
                                 '#8d82e1ff',
                                 '#8c82e0ff',
                                 '#8c81e0ff',
                                 '#8b81e0ff',
                                 '#8a80e0ff',
                                 '#8a7fe0ff',
                                 '#897fe0ff',
                                 '#887edfff',
                                 '#887edfff',
                                 '#877ddfff',
                                 '#867cdfff',
                                 '#867cdfff',
                                 '#857bdfff',
                                 '#847bdeff',
                                 '#847adeff',
                                 '#837adeff',
                                 '#8379deff',
                                 '#8278deff',
                                 '#8178deff',
                                 '#8077ddff',
                                 '#8077ddff',
                                 '#7f76ddff',
                                 '#7e75ddff',
                                 '#7e75ddff',
                                 '#7d74ddff',
                                 '#7c74dcff',
                                 '#7c73dcff',
                                 '#7b73dcff',
                                 '#7a72dcff',
                                 '#7a71dcff',
                                 '#7971dcff',
                                 '#7870dbff',
                                 '#7870dbff',
                                 '#776fdbff',
                                 '#766fdbff',
                                 '#756edbff',
                                 '#756ddaff',
                                 '#746ddaff',
                                 '#736cdaff',
                                 '#736cdaff',
                                 '#726bdaff',
                                 '#716bdaff',
                                 '#706ad9ff',
                                 '#7069d9ff',
                                 '#6f69d9ff',
                                 '#6e68d9ff',
                                 '#6e68d9ff',
                                 '#6d67d9ff',
                                 '#6c67d8ff',
                                 '#6b66d8ff',
                                 '#6b65d8ff',
                                 '#6a65d8ff',
                                 '#6964d8ff',
                                 '#6864d8ff',
                                 '#6863d7ff',
                                 '#6763d7ff',
                                 '#6662d7ff'],
                     'bad': '#00000000'},
           'cmap1': {'colours': ['#ffffffff',
                                 '#fffeffff',
                                 '#fefefeff',
                                 '#fefdfeff',
                                 '#fefcfeff',
                                 '#fdfcfeff',
                                 '#fdfbfdff',
                                 '#fdfafdff',
                                 '#fcfafdff',
                                 '#fcf9fdff',
                                 '#fcf9fcff',
                                 '#fcf8fcff',
                                 '#fbf7fcff',
                                 '#fbf7fcff',
                                 '#fbf6fbff',
                                 '#faf5fbff',
                                 '#faf5fbff',
                                 '#faf4faff',
                                 '#f9f3faff',
                                 '#f9f3faff',
                                 '#f9f2faff',
                                 '#f8f2f9ff',
                                 '#f8f1f9ff',
                                 '#f8f0f9ff',
                                 '#f7f0f9ff',
                                 '#f7eff8ff',
                                 '#f7eef8ff',
                                 '#f6eef8ff',
                                 '#f6edf7ff',
                                 '#f6ecf7ff',
                                 '#f5ecf7ff',
                                 '#f5ebf7ff',
                                 '#f5eaf6ff',
                                 '#f4eaf6ff',
                                 '#f4e9f6ff',
                                 '#f4e9f6ff',
                                 '#f4e8f5ff',
                                 '#f3e7f5ff',
                                 '#f3e7f5ff',
                                 '#f3e6f5ff',
                                 '#f2e5f4ff',
                                 '#f2e5f4ff',
                                 '#f2e4f4ff',
                                 '#f1e3f3ff',
                                 '#f1e3f3ff',
                                 '#f1e2f3ff',
                                 '#f0e2f3ff',
                                 '#f0e1f2ff',
                                 '#f0e0f2ff',
                                 '#efe0f2ff',
                                 '#efdff2ff',
                                 '#efdef1ff',
                                 '#eedef1ff',
                                 '#eeddf1ff',
                                 '#eeddf1ff',
                                 '#eddcf0ff',
                                 '#eddbf0ff',
                                 '#eddbf0ff',
                                 '#ecdaefff',
                                 '#ecd9efff',
                                 '#ecd9efff',
                                 '#ebd8efff',
                                 '#ebd7eeff',
                                 '#ebd7eeff',
                                 '#ead6eeff',
                                 '#ead6eeff',
                                 '#ead5edff',
                                 '#e9d4edff',
                                 '#e9d4edff',
                                 '#e9d3ecff',
                                 '#e8d2ecff',
                                 '#e8d2ecff',
                                 '#e8d1ecff',
                                 '#e7d0ebff',
                                 '#e7d0ebff',
                                 '#e7cfebff',
                                 '#e7cfebff',
                                 '#e6ceeaff',
                                 '#e6cdeaff',
                                 '#e6cdeaff',
                                 '#e5cceaff',
                                 '#e5cbe9ff',
                                 '#e5cbe9ff',
                                 '#e4cae9ff',
                                 '#e4cae8ff',
                                 '#e4c9e8ff',
                                 '#e3c8e8ff',
                                 '#e3c8e8ff',
                                 '#e3c7e7ff',
                                 '#e2c6e7ff',
                                 '#e2c6e7ff',
                                 '#e2c5e7ff',
                                 '#e1c5e6ff',
                                 '#e1c4e6ff',
                                 '#e1c3e6ff',
                                 '#e0c3e5ff',
                                 '#e0c2e5ff',
                                 '#e0c1e5ff',
                                 '#dfc1e5ff',
                                 '#dfc0e4ff',
                                 '#dfc0e4ff',
                                 '#debfe4ff',
                                 '#debee4ff',
                                 '#debee3ff',
                                 '#ddbde3ff',
                                 '#ddbce3ff',
                                 '#ddbce3ff',
                                 '#dcbbe2ff',
                                 '#dcbbe2ff',
                                 '#dcbae2ff',
                                 '#dbb9e1ff',
                                 '#dbb9e1ff',
                                 '#dbb8e1ff',
                                 '#dab7e1ff',
                                 '#dab7e0ff',
                                 '#d9b6e0ff',
                                 '#d9b6e0ff',
                                 '#d9b5e0ff',
                                 '#d8b4dfff',
                                 '#d8b4dfff',
                                 '#d8b3dfff',
                                 '#d7b2deff',
                                 '#d7b2deff',
                                 '#d7b1deff',
                                 '#d6b1deff',
                                 '#d6b0ddff',
                                 '#d6afddff',
                                 '#d5afddff',
                                 '#d5aeddff',
                                 '#d5addcff',
                                 '#d4addcff',
                                 '#d4acdcff',
                                 '#d4acdbff',
                                 '#d3abdbff',
                                 '#d3aadbff',
                                 '#d3aadbff',
                                 '#d2a9daff',
                                 '#d2a8daff',
                                 '#d2a8daff',
                                 '#d1a7daff',
                                 '#d1a7d9ff',
                                 '#d1a6d9ff',
                                 '#d0a5d9ff',
                                 '#d0a5d9ff',
                                 '#d0a4d8ff',
                                 '#cfa3d8ff',
                                 '#cfa3d8ff',
                                 '#cfa2d7ff',
                                 '#cea2d7ff',
                                 '#cea1d7ff',
                                 '#cea0d7ff',
                                 '#cda0d6ff',
                                 '#cd9fd6ff',
                                 '#cd9fd6ff',
                                 '#cc9ed6ff',
                                 '#cc9dd5ff',
                                 '#cb9dd5ff',
                                 '#cb9cd5ff',
                                 '#cb9bd4ff',
                                 '#ca9bd4ff',
                                 '#ca9ad4ff',
                                 '#ca9ad4ff',
                                 '#c999d3ff',
                                 '#c998d3ff',
                                 '#c998d3ff',
                                 '#c897d3ff',
                                 '#c896d2ff',
                                 '#c896d2ff',
                                 '#c795d2ff',
                                 '#c795d1ff',
                                 '#c794d1ff',
                                 '#c693d1ff',
                                 '#c693d1ff',
                                 '#c692d0ff',
                                 '#c592d0ff',
                                 '#c591d0ff',
                                 '#c590d0ff',
                                 '#c490cfff',
                                 '#c48fcfff',
                                 '#c38ecfff',
                                 '#c38eceff',
                                 '#c38dceff',
                                 '#c28dceff',
                                 '#c28cceff',
                                 '#c28bcdff',
                                 '#c18bcdff',
                                 '#c18acdff',
                                 '#c189cdff',
                                 '#c089ccff',
                                 '#c088ccff',
                                 '#c088ccff',
                                 '#bf87cbff',
                                 '#bf86cbff',
                                 '#bf86cbff',
                                 '#be85cbff',
                                 '#be85caff',
                                 '#bd84caff',
                                 '#bd83caff',
                                 '#bd83caff',
                                 '#bc82c9ff',
                                 '#bc81c9ff',
                                 '#bc81c9ff',
                                 '#bb80c8ff',
                                 '#bb80c8ff',
                                 '#bb7fc8ff',
                                 '#ba7ec8ff',
                                 '#ba7ec7ff',
                                 '#ba7dc7ff',
                                 '#b97cc7ff',
                                 '#b97cc7ff',
                                 '#b87bc6ff',
                                 '#b87bc6ff',
                                 '#b87ac6ff',
                                 '#b779c5ff',
                                 '#b779c5ff',
                                 '#b778c5ff',
                                 '#b677c5ff',
                                 '#b677c4ff',
                                 '#b676c4ff',
                                 '#b576c4ff',
                                 '#b575c4ff',
                                 '#b474c3ff',
                                 '#b474c3ff',
                                 '#b473c3ff',
                                 '#b373c2ff',
                                 '#b372c2ff',
                                 '#b371c2ff',
                                 '#b271c2ff',
                                 '#b270c1ff',
                                 '#b26fc1ff',
                                 '#b16fc1ff',
                                 '#b16ec1ff',
                                 '#b06ec0ff',
                                 '#b06dc0ff',
                                 '#b06cc0ff',
                                 '#af6cbfff',
                                 '#af6bbfff',
                                 '#af6abfff',
                                 '#ae6abfff',
                                 '#ae69beff',
                                 '#ae68beff',
                                 '#ad68beff',
                                 '#ad67beff',
                                 '#ac67bdff',
                                 '#ac66bdff',
                                 '#ac65bdff',
                                 '#ab65bcff',
                                 '#ab64bcff',
                                 '#ab63bcff',
                                 '#aa63bcff',
                                 '#aa62bbff',
                                 '#a962bbff',
                                 '#a961bbff',
                                 '#a960bbff',
                                 '#a860baff',
                                 '#a85fbaff'],
                     'bad': '#00000000'},
           'cmap2': {'colours': ['#ffffffff',
                                 '#fffeffff',
                                 '#fffefeff',
                                 '#fffdfeff',
                                 '#fffdfdff',
                                 '#fffcfdff',
                                 '#fffbfdff',
                                 '#fffbfcff',
                                 '#fffafcff',
                                 '#fffafbff',
                                 '#fff9fbff',
                                 '#fff8faff',
                                 '#fff8faff',
                                 '#fff7faff',
                                 '#fff7f9ff',
                                 '#fff6f9ff',
                                 '#fff5f8ff',
                                 '#fff5f8ff',
                                 '#fff4f8ff',
                                 '#fff4f7ff',
                                 '#fff3f7ff',
                                 '#fff2f6ff',
                                 '#fff2f6ff',
                                 '#fff1f6ff',
                                 '#fff1f5ff',
                                 '#fff0f5ff',
                                 '#ffeff4ff',
                                 '#ffeff4ff',
                                 '#ffeef4ff',
                                 '#ffeef3ff',
                                 '#ffedf3ff',
                                 '#ffecf2ff',
                                 '#ffecf2ff',
                                 '#ffebf2ff',
                                 '#ffebf1ff',
                                 '#ffeaf1ff',
                                 '#ffe9f0ff',
                                 '#ffe9f0ff',
                                 '#ffe8f0ff',
                                 '#ffe8efff',
                                 '#ffe7efff',
                                 '#ffe6eeff',
                                 '#ffe6eeff',
                                 '#ffe5edff',
                                 '#ffe5edff',
                                 '#ffe4edff',
                                 '#ffe3ecff',
                                 '#ffe3ecff',
                                 '#ffe2ebff',
                                 '#ffe2ebff',
                                 '#ffe1ebff',
                                 '#ffe0eaff',
                                 '#ffe0eaff',
                                 '#ffdfe9ff',
                                 '#ffdee9ff',
                                 '#ffdee9ff',
                                 '#ffdde8ff',
                                 '#ffdde8ff',
                                 '#ffdce7ff',
                                 '#ffdbe7ff',
                                 '#ffdbe7ff',
                                 '#ffdae6ff',
                                 '#ffdae6ff',
                                 '#ffd9e5ff',
                                 '#ffd8e5ff',
                                 '#ffd8e5ff',
                                 '#ffd7e4ff',
                                 '#ffd7e4ff',
                                 '#ffd6e3ff',
                                 '#ffd5e3ff',
                                 '#ffd5e3ff',
                                 '#ffd4e2ff',
                                 '#ffd4e2ff',
                                 '#ffd3e1ff',
                                 '#ffd2e1ff',
                                 '#ffd2e1ff',
                                 '#ffd1e0ff',
                                 '#ffd1e0ff',
                                 '#ffd0dfff',
                                 '#ffcfdfff',
                                 '#ffcfdfff',
                                 '#ffcedeff',
                                 '#ffcedeff',
                                 '#ffcdddff',
                                 '#ffccddff',
                                 '#ffccddff',
                                 '#ffcbdcff',
                                 '#ffcbdcff',
                                 '#ffcadbff',
                                 '#ffc9dbff',
                                 '#ffc9dbff',
                                 '#ffc8daff',
                                 '#ffc7daff',
                                 '#ffc7d9ff',
                                 '#ffc6d9ff',
                                 '#ffc6d9ff',
                                 '#ffc5d8ff',
                                 '#ffc4d8ff',
                                 '#ffc4d7ff',
                                 '#ffc3d7ff',
                                 '#ffc3d7ff',
                                 '#ffc2d6ff',
                                 '#ffc1d6ff',
                                 '#ffc1d5ff',
                                 '#ffc0d5ff',
                                 '#ffc0d5ff',
                                 '#ffbfd4ff',
                                 '#ffbed4ff',
                                 '#febed3ff',
                                 '#febdd3ff',
                                 '#febcd3ff',
                                 '#febcd2ff',
                                 '#febbd2ff',
                                 '#febbd1ff',
                                 '#febad1ff',
                                 '#feb9d1ff',
                                 '#feb9d0ff',
                                 '#feb8d0ff',
                                 '#feb8d0ff',
                                 '#feb7cfff',
                                 '#feb6cfff',
                                 '#feb6ceff',
                                 '#feb5ceff',
                                 '#feb4ceff',
                                 '#feb4cdff',
                                 '#feb3cdff',
                                 '#fdb3ccff',
                                 '#fdb2ccff',
                                 '#fdb1ccff',
                                 '#fdb1cbff',
                                 '#fdb0cbff',
                                 '#fdb0caff',
                                 '#fdafcaff',
                                 '#fdaecaff',
                                 '#fdaec9ff',
                                 '#fdadc9ff',
                                 '#fdacc8ff',
                                 '#fdacc8ff',
                                 '#fdabc8ff',
                                 '#fdabc7ff',
                                 '#fdaac7ff',
                                 '#fca9c6ff',
                                 '#fca9c6ff',
                                 '#fca8c6ff',
                                 '#fca7c5ff',
                                 '#fca7c5ff',
                                 '#fca6c5ff',
                                 '#fca6c4ff',
                                 '#fca5c4ff',
                                 '#fca4c3ff',
                                 '#fca4c3ff',
                                 '#fca3c3ff',
                                 '#fca2c2ff',
                                 '#fca2c2ff',
                                 '#fba1c1ff',
                                 '#fba0c1ff',
                                 '#fba0c1ff',
                                 '#fb9fc0ff',
                                 '#fb9fc0ff',
                                 '#fb9ebfff',
                                 '#fb9dbfff',
                                 '#fb9dbfff',
                                 '#fb9cbeff',
                                 '#fb9bbeff',
                                 '#fb9bbeff',
                                 '#fb9abdff',
                                 '#fa9abdff',
                                 '#fa99bcff',
                                 '#fa98bcff',
                                 '#fa98bcff',
                                 '#fa97bbff',
                                 '#fa96bbff',
                                 '#fa96baff',
                                 '#fa95baff',
                                 '#fa94baff',
                                 '#fa94b9ff',
                                 '#fa93b9ff',
                                 '#f992b9ff',
                                 '#f992b8ff',
                                 '#f991b8ff',
                                 '#f991b7ff',
                                 '#f990b7ff',
                                 '#f98fb7ff',
                                 '#f98fb6ff',
                                 '#f98eb6ff',
                                 '#f98db5ff',
                                 '#f98db5ff',
                                 '#f88cb5ff',
                                 '#f88bb4ff',
                                 '#f88bb4ff',
                                 '#f88ab4ff',
                                 '#f889b3ff',
                                 '#f889b3ff',
                                 '#f888b2ff',
                                 '#f887b2ff',
                                 '#f887b2ff',
                                 '#f886b1ff',
                                 '#f785b1ff',
                                 '#f785b0ff',
                                 '#f784b0ff',
                                 '#f783b0ff',
                                 '#f783afff',
                                 '#f782afff',
                                 '#f781afff',
                                 '#f781aeff',
                                 '#f680aeff',
                                 '#f67fadff',
                                 '#f67fadff',
                                 '#f67eadff',
                                 '#f67dacff',
                                 '#f67dacff',
                                 '#f67cacff',
                                 '#f67babff',
                                 '#f67babff',
                                 '#f57aaaff',
                                 '#f579aaff',
                                 '#f579aaff',
                                 '#f578a9ff',
                                 '#f577a9ff',
                                 '#f576a9ff',
                                 '#f576a8ff',
                                 '#f575a8ff',
                                 '#f474a7ff',
                                 '#f474a7ff',
                                 '#f473a7ff',
                                 '#f472a6ff',
                                 '#f472a6ff',
                                 '#f471a5ff',
                                 '#f470a5ff',
                                 '#f46fa5ff',
                                 '#f36fa4ff',
                                 '#f36ea4ff',
                                 '#f36da4ff',
                                 '#f36da3ff',
                                 '#f36ca3ff',
                                 '#f36ba2ff',
                                 '#f36aa2ff',
                                 '#f36aa2ff',
                                 '#f269a1ff',
                                 '#f268a1ff',
                                 '#f267a1ff',
                                 '#f267a0ff',
                                 '#f266a0ff',
                                 '#f2659fff',
                                 '#f2649fff',
                                 '#f1649fff',
                                 '#f1639eff',
                                 '#f1629eff',
                                 '#f1619eff',
                                 '#f1619dff',
                                 '#f1609dff',
                                 '#f15f9cff',
                                 '#f05e9cff',
                                 '#f05e9cff',
                                 '#f05d9bff',
                                 '#f05c9bff'],
                     'bad': '#00000000'},
           'cmap3': {'colours': ['#ffffffff',
                                 '#fffffeff',
                                 '#fffefeff',
                                 '#fffefdff',
                                 '#fffdfdff',
                                 '#fffdfcff',
                                 '#fffcfcff',
                                 '#fffcfbff',
                                 '#fffbfbff',
                                 '#fffbfaff',
                                 '#fffbfaff',
                                 '#fffaf9ff',
                                 '#fffaf8ff',
                                 '#fff9f8ff',
                                 '#fff9f7ff',
                                 '#fff8f7ff',
                                 '#fff8f6ff',
                                 '#fff7f6ff',
                                 '#fff7f5ff',
                                 '#fff7f5ff',
                                 '#fff6f4ff',
                                 '#fff6f4ff',
                                 '#fff5f3ff',
                                 '#fff5f2ff',
                                 '#fff4f2ff',
                                 '#fff4f1ff',
                                 '#fff3f1ff',
                                 '#fff3f0ff',
                                 '#fff3f0ff',
                                 '#fff2efff',
                                 '#fff2efff',
                                 '#fff1eeff',
                                 '#fff1eeff',
                                 '#fff0edff',
                                 '#fff0edff',
                                 '#ffefecff',
                                 '#ffefebff',
                                 '#ffefebff',
                                 '#ffeeeaff',
                                 '#ffeeeaff',
                                 '#ffede9ff',
                                 '#ffede9ff',
                                 '#ffece8ff',
                                 '#ffece8ff',
                                 '#ffebe7ff',
                                 '#ffebe7ff',
                                 '#ffebe6ff',
                                 '#ffeae6ff',
                                 '#ffeae5ff',
                                 '#ffe9e4ff',
                                 '#ffe9e4ff',
                                 '#ffe8e3ff',
                                 '#ffe8e3ff',
                                 '#ffe7e2ff',
                                 '#ffe7e2ff',
                                 '#ffe7e1ff',
                                 '#ffe6e1ff',
                                 '#ffe6e0ff',
                                 '#ffe5e0ff',
                                 '#ffe5dfff',
                                 '#ffe4dfff',
                                 '#ffe4deff',
                                 '#ffe4deff',
                                 '#ffe3ddff',
                                 '#ffe3dcff',
                                 '#ffe2dcff',
                                 '#ffe2dbff',
                                 '#ffe1dbff',
                                 '#ffe1daff',
                                 '#ffe0daff',
                                 '#ffe0d9ff',
                                 '#ffe0d9ff',
                                 '#ffdfd8ff',
                                 '#ffdfd8ff',
                                 '#ffded7ff',
                                 '#ffded7ff',
                                 '#ffddd6ff',
                                 '#ffddd6ff',
                                 '#ffdcd5ff',
                                 '#ffdcd5ff',
                                 '#ffdcd4ff',
                                 '#ffdbd3ff',
                                 '#ffdbd3ff',
                                 '#ffdad2ff',
                                 '#ffdad2ff',
                                 '#ffd9d1ff',
                                 '#ffd9d1ff',
                                 '#ffd8d0ff',
                                 '#ffd8d0ff',
                                 '#ffd8cfff',
                                 '#ffd7cfff',
                                 '#ffd7ceff',
                                 '#ffd6ceff',
                                 '#ffd6cdff',
                                 '#ffd5cdff',
                                 '#ffd5ccff',
                                 '#ffd4ccff',
                                 '#ffd4cbff',
                                 '#ffd4cbff',
                                 '#ffd3caff',
                                 '#ffd3c9ff',
                                 '#ffd2c9ff',
                                 '#ffd2c8ff',
                                 '#ffd1c8ff',
                                 '#ffd1c7ff',
                                 '#ffd0c7ff',
                                 '#ffd0c6ff',
                                 '#ffd0c6ff',
                                 '#ffcfc5ff',
                                 '#ffcfc5ff',
                                 '#ffcec4ff',
                                 '#ffcec4ff',
                                 '#ffcdc3ff',
                                 '#ffcdc3ff',
                                 '#ffccc2ff',
                                 '#ffccc2ff',
                                 '#ffccc1ff',
                                 '#ffcbc1ff',
                                 '#ffcbc0ff',
                                 '#ffcac0ff',
                                 '#ffcabfff',
                                 '#ffc9beff',
                                 '#ffc9beff',
                                 '#ffc8bdff',
                                 '#ffc8bdff',
                                 '#ffc8bcff',
                                 '#ffc7bcff',
                                 '#ffc7bbff',
                                 '#ffc6bbff',
                                 '#ffc6baff',
                                 '#ffc5baff',
                                 '#ffc5b9ff',
                                 '#ffc4b9ff',
                                 '#ffc4b8ff',
                                 '#ffc4b8ff',
                                 '#ffc3b7ff',
                                 '#ffc3b7ff',
                                 '#ffc2b6ff',
                                 '#ffc2b6ff',
                                 '#ffc1b5ff',
                                 '#ffc1b5ff',
                                 '#ffc0b4ff',
                                 '#ffc0b4ff',
                                 '#ffc0b3ff',
                                 '#ffbfb3ff',
                                 '#ffbfb2ff',
                                 '#ffbeb2ff',
                                 '#ffbeb1ff',
                                 '#ffbdb1ff',
                                 '#ffbdb0ff',
                                 '#ffbcb0ff',
                                 '#ffbcafff',
                                 '#ffbcaeff',
                                 '#ffbbaeff',
                                 '#ffbbadff',
                                 '#ffbaadff',
                                 '#ffbaacff',
                                 '#ffb9acff',
                                 '#ffb9abff',
                                 '#ffb8abff',
                                 '#ffb8aaff',
                                 '#ffb8aaff',
                                 '#ffb7a9ff',
                                 '#ffb7a9ff',
                                 '#ffb6a8ff',
                                 '#ffb6a8ff',
                                 '#ffb5a7ff',
                                 '#ffb5a7ff',
                                 '#ffb4a6ff',
                                 '#ffb4a6ff',
                                 '#ffb4a5ff',
                                 '#ffb3a5ff',
                                 '#ffb3a4ff',
                                 '#ffb2a4ff',
                                 '#ffb2a3ff',
                                 '#ffb1a3ff',
                                 '#ffb1a2ff',
                                 '#ffb0a2ff',
                                 '#ffb0a1ff',
                                 '#ffb0a1ff',
                                 '#ffafa0ff',
                                 '#ffafa0ff',
                                 '#ffae9fff',
                                 '#ffae9fff',
                                 '#ffad9eff',
                                 '#ffad9eff',
                                 '#ffac9dff',
                                 '#ffac9dff',
                                 '#ffab9cff',
                                 '#ffab9cff',
                                 '#ffab9bff',
                                 '#ffaa9bff',
                                 '#ffaa9aff',
                                 '#ffa99aff',
                                 '#ffa999ff',
                                 '#ffa899ff',
                                 '#ffa898ff',
                                 '#ffa798ff',
                                 '#ffa797ff',
                                 '#ffa797ff',
                                 '#ffa696ff',
                                 '#ffa696ff',
                                 '#ffa595ff',
                                 '#ffa595ff',
                                 '#ffa494ff',
                                 '#ffa494ff',
                                 '#ffa393ff',
                                 '#ffa393ff',
                                 '#ffa292ff',
                                 '#ffa292ff',
                                 '#ffa291ff',
                                 '#ffa191ff',
                                 '#ffa190ff',
                                 '#ffa090ff',
                                 '#ffa08fff',
                                 '#ff9f8fff',
                                 '#fe9f8eff',
                                 '#fe9e8eff',
                                 '#fe9e8dff',
                                 '#fe9d8dff',
                                 '#fe9d8cff',
                                 '#fe9d8cff',
                                 '#fe9c8bff',
                                 '#fe9c8bff',
                                 '#fe9b8aff',
                                 '#fe9b8aff',
                                 '#fe9a89ff',
                                 '#fe9a89ff',
                                 '#fd9988ff',
                                 '#fd9988ff',
                                 '#fd9887ff',
                                 '#fd9887ff',
                                 '#fd9886ff',
                                 '#fd9786ff',
                                 '#fd9785ff',
                                 '#fd9685ff',
                                 '#fd9684ff',
                                 '#fd9584ff',
                                 '#fd9583ff',
                                 '#fd9483ff',
                                 '#fc9482ff',
                                 '#fc9382ff',
                                 '#fc9381ff',
                                 '#fc9381ff',
                                 '#fc9280ff',
                                 '#fc9280ff',
                                 '#fc917fff',
                                 '#fc917fff',
                                 '#fc907eff',
                                 '#fc907eff',
                                 '#fb8f7dff',
                                 '#fb8f7dff',
                                 '#fb8e7cff',
                                 '#fb8e7cff',
                                 '#fb8d7bff',
                                 '#fb8d7bff'],
                     'bad': '#00000000'},
           'cmap4': {'colours': ['#ffffffff',
                                 '#fffffeff',
                                 '#fffefeff',
                                 '#fffefdff',
                                 '#fffefcff',
                                 '#fffefcff',
                                 '#fffdfbff',
                                 '#fffdfbff',
                                 '#fffdfaff',
                                 '#fffdf9ff',
                                 '#fffcf9ff',
                                 '#fffcf8ff',
                                 '#fffcf7ff',
                                 '#fffcf7ff',
                                 '#fffbf6ff',
                                 '#fffbf5ff',
                                 '#fffbf5ff',
                                 '#fffbf4ff',
                                 '#fffaf3ff',
                                 '#fffaf3ff',
                                 '#fffaf2ff',
                                 '#fffaf2ff',
                                 '#fff9f1ff',
                                 '#fff9f0ff',
                                 '#fff9f0ff',
                                 '#fff9efff',
                                 '#fff8eeff',
                                 '#fff8eeff',
                                 '#fff8edff',
                                 '#fff8ecff',
                                 '#fff7ecff',
                                 '#fff7ebff',
                                 '#fff7ebff',
                                 '#fff7eaff',
                                 '#fff6e9ff',
                                 '#fff6e9ff',
                                 '#fff6e8ff',
                                 '#fff6e7ff',
                                 '#fff5e7ff',
                                 '#fff5e6ff',
                                 '#fff5e5ff',
                                 '#fff5e5ff',
                                 '#fff4e4ff',
                                 '#fff4e4ff',
                                 '#fff4e3ff',
                                 '#fff4e2ff',
                                 '#fff3e2ff',
                                 '#fff3e1ff',
                                 '#fff3e0ff',
                                 '#fff3e0ff',
                                 '#fff2dfff',
                                 '#fff2deff',
                                 '#fff2deff',
                                 '#fff2ddff',
                                 '#fff1ddff',
                                 '#fff1dcff',
                                 '#fff1dbff',
                                 '#fff1dbff',
                                 '#fff0daff',
                                 '#fff0d9ff',
                                 '#fff0d9ff',
                                 '#fff0d8ff',
                                 '#fff0d8ff',
                                 '#ffefd7ff',
                                 '#ffefd6ff',
                                 '#ffefd6ff',
                                 '#ffefd5ff',
                                 '#ffeed4ff',
                                 '#ffeed4ff',
                                 '#ffeed3ff',
                                 '#ffeed2ff',
                                 '#ffedd2ff',
                                 '#ffedd1ff',
                                 '#ffedd1ff',
                                 '#ffedd0ff',
                                 '#ffeccfff',
                                 '#ffeccfff',
                                 '#ffecceff',
                                 '#ffeccdff',
                                 '#ffebcdff',
                                 '#ffebccff',
                                 '#ffebccff',
                                 '#ffebcbff',
                                 '#ffeacaff',
                                 '#ffeacaff',
                                 '#ffeac9ff',
                                 '#ffeac8ff',
                                 '#ffe9c8ff',
                                 '#ffe9c7ff',
                                 '#ffe9c6ff',
                                 '#ffe9c6ff',
                                 '#ffe8c5ff',
                                 '#ffe8c5ff',
                                 '#ffe8c4ff',
                                 '#ffe8c3ff',
                                 '#ffe7c3ff',
                                 '#ffe7c2ff',
                                 '#ffe7c1ff',
                                 '#ffe7c1ff',
                                 '#ffe6c0ff',
                                 '#ffe6c0ff',
                                 '#ffe6bfff',
                                 '#ffe6beff',
                                 '#ffe5beff',
                                 '#ffe5bdff',
                                 '#ffe5bcff',
                                 '#ffe5bcff',
                                 '#ffe4bbff',
                                 '#ffe4bbff',
                                 '#ffe4baff',
                                 '#ffe4b9ff',
                                 '#ffe3b9ff',
                                 '#ffe3b8ff',
                                 '#ffe3b7ff',
                                 '#ffe3b7ff',
                                 '#ffe2b6ff',
                                 '#ffe2b6ff',
                                 '#ffe2b5ff',
                                 '#ffe2b4ff',
                                 '#ffe1b4ff',
                                 '#ffe1b3ff',
                                 '#ffe1b2ff',
                                 '#ffe1b2ff',
                                 '#ffe1b1ff',
                                 '#ffe0b0ff',
                                 '#ffe0b0ff',
                                 '#ffe0afff',
                                 '#ffe0afff',
                                 '#ffdfaeff',
                                 '#ffdfadff',
                                 '#ffdfadff',
                                 '#ffdfacff',
                                 '#ffdeabff',
                                 '#ffdeabff',
                                 '#ffdeaaff',
                                 '#ffdeaaff',
                                 '#ffdda9ff',
                                 '#ffdda8ff',
                                 '#ffdda8ff',
                                 '#ffdda7ff',
                                 '#ffdca6ff',
                                 '#ffdca6ff',
                                 '#ffdca5ff',
                                 '#ffdca5ff',
                                 '#ffdba4ff',
                                 '#ffdba3ff',
                                 '#ffdba3ff',
                                 '#ffdba2ff',
                                 '#ffdaa1ff',
                                 '#ffdaa1ff',
                                 '#ffdaa0ff',
                                 '#ffdaa0ff',
                                 '#ffd99fff',
                                 '#ffd99eff',
                                 '#ffd99eff',
                                 '#ffd99dff',
                                 '#ffd99cff',
                                 '#ffd89cff',
                                 '#ffd89bff',
                                 '#ffd89bff',
                                 '#ffd89aff',
                                 '#ffd799ff',
                                 '#ffd799ff',
                                 '#ffd798ff',
                                 '#ffd797ff',
                                 '#ffd697ff',
                                 '#ffd696ff',
                                 '#ffd696ff',
                                 '#ffd695ff',
                                 '#ffd594ff',
                                 '#ffd594ff',
                                 '#ffd593ff',
                                 '#ffd592ff',
                                 '#ffd492ff',
                                 '#ffd491ff',
                                 '#ffd491ff',
                                 '#ffd490ff',
                                 '#ffd38fff',
                                 '#ffd38fff',
                                 '#ffd38eff',
                                 '#ffd38dff',
                                 '#ffd38dff',
                                 '#ffd28cff',
                                 '#ffd28bff',
                                 '#ffd28bff',
                                 '#ffd28aff',
                                 '#ffd18aff',
                                 '#ffd189ff',
                                 '#ffd188ff',
                                 '#ffd188ff',
                                 '#ffd087ff',
                                 '#ffd086ff',
                                 '#ffd086ff',
                                 '#ffd085ff',
                                 '#ffcf85ff',
                                 '#ffcf84ff',
                                 '#ffcf83ff',
                                 '#ffcf83ff',
                                 '#ffce82ff',
                                 '#ffce81ff',
                                 '#ffce81ff',
                                 '#ffce80ff',
                                 '#ffce7fff',
                                 '#ffcd7fff',
                                 '#ffcd7eff',
                                 '#ffcd7eff',
                                 '#ffcd7dff',
                                 '#ffcc7cff',
                                 '#ffcc7cff',
                                 '#ffcc7bff',
                                 '#ffcc7aff',
                                 '#ffcb7aff',
                                 '#ffcb79ff',
                                 '#ffcb78ff',
                                 '#ffcb78ff',
                                 '#ffca77ff',
                                 '#ffca77ff',
                                 '#ffca76ff',
                                 '#ffca75ff',
                                 '#ffc975ff',
                                 '#ffc974ff',
                                 '#ffc973ff',
                                 '#ffc973ff',
                                 '#ffc972ff',
                                 '#ffc871ff',
                                 '#ffc871ff',
                                 '#ffc870ff',
                                 '#ffc86fff',
                                 '#ffc76fff',
                                 '#ffc76eff',
                                 '#ffc76dff',
                                 '#ffc76dff',
                                 '#ffc66cff',
                                 '#ffc66cff',
                                 '#ffc66bff',
                                 '#ffc66aff',
                                 '#ffc56aff',
                                 '#ffc569ff',
                                 '#ffc568ff',
                                 '#ffc568ff',
                                 '#ffc567ff',
                                 '#ffc466ff',
                                 '#ffc466ff',
                                 '#ffc465ff',
                                 '#ffc464ff',
                                 '#ffc364ff',
                                 '#ffc363ff',
                                 '#ffc362ff',
                                 '#ffc362ff',
                                 '#fec261ff',
                                 '#fec260ff',
                                 '#fec260ff',
                                 '#fec25fff',
                                 '#fec15eff',
                                 '#fec15eff',
                                 '#fec15dff'],
                     'bad': '#00000000'}},
 'shapes': {'shape0': [[-237.8, -237.8],
                       [237.8, -237.8],
                       [237.8, 237.8],
                       [-237.8, 237.8],
                       [-237.8, -237.8]],
            'shape1': [[-410.0, -410.0], [-237.8, -237.8]],
            'shape2': [[410.0, -410.0], [237.8, -237.8]],
            'shape3': [[410.0, 410.0], [237.8, 237.8]],
            'shape4': [[-410.0, 410.0], [-237.8, 237.8]]}}
PANEL = {'title': ['Example animal: tablet (n = 2 sessions)'],
 'headings': [],
 'partial': '',
 'subplots': [{'role': 'plot',
               'name': 'Climb',
               'text_style': [],
               'rect': [2.6714, 1.0704, 0.8, 0.8],
               'pos': [0.31428235294117646,
                       0.8299636363636365,
                       0.09411764705882353,
                       0.07272727272727275],
               'xlim': [-410.0, 410.0],
               'ylim': [-410.0, 410.0],
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
                          'right': {'visible': True,
                                    'lw': 0.6,
                                    'colour': '#262626',
                                    'bounds': None,
                                    'position': None},
                          'bottom': {'visible': True,
                                     'lw': 0.6,
                                     'colour': '#262626',
                                     'bounds': None,
                                     'position': None},
                          'top': {'visible': True,
                                  'lw': 0.6,
                                  'colour': '#262626',
                                  'bounds': None,
                                  'position': None}},
               'xticks': {'at': [], 'labels': []},
               'yticks': {'at': [], 'labels': []},
               'xlabel': None,
               'ylabel': None,
               'files': [{'file': 'climb_map.csv',
                          'kind': 'map',
                          'style': {'zorder': 0.0,
                                    'rank': 0,
                                    'cmap': 'cmap0',
                                    'clim': [0.0, 0.001461733]},
                          'styles': [{'zorder': 0.0,
                                      'rank': 0,
                                      'cmap': 'cmap0',
                                      'clim': [0.0, 0.001461733]}]}],
               'decor': [{'kind': 'line',
                          'shape': 'shape0',
                          'style': {'zorder': 4.0,
                                    'rank': 1,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'colour': '#404040',
                                    'mfc': '#404040',
                                    'mec': '#404040',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'what': 'cage_lines'},
                         {'kind': 'line',
                          'shape': 'shape1',
                          'style': {'zorder': 4.0,
                                    'rank': 2,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'colour': '#404040',
                                    'mfc': '#404040',
                                    'mec': '#404040',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'what': 'cage_lines'},
                         {'kind': 'line',
                          'shape': 'shape2',
                          'style': {'zorder': 4.0,
                                    'rank': 3,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'colour': '#404040',
                                    'mfc': '#404040',
                                    'mec': '#404040',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'what': 'cage_lines'},
                         {'kind': 'line',
                          'shape': 'shape3',
                          'style': {'zorder': 4.0,
                                    'rank': 4,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'colour': '#404040',
                                    'mfc': '#404040',
                                    'mec': '#404040',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'what': 'cage_lines'},
                         {'kind': 'line',
                          'shape': 'shape4',
                          'style': {'zorder': 4.0,
                                    'rank': 5,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'colour': '#404040',
                                    'mfc': '#404040',
                                    'mec': '#404040',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'what': 'cage_lines'}],
               'aspect': 1.0,
               'images': [{'cmap': 'cmap0',
                           'clim': [0.0, 0.001461733],
                           'extent': [-410.0, 410.0, -410.0, 410.0],
                           'origin': 'lower',
                           'interpolation': 'bilinear',
                           'zorder': 0.0,
                           'alpha': None}]},
              {'role': 'plot',
               'name': 'Active',
               'text_style': [],
               'rect': [3.5714, 1.0704, 0.8, 0.8],
               'pos': [0.420164705882353,
                       0.8299636363636365,
                       0.09411764705882353,
                       0.07272727272727275],
               'xlim': [-410.0, 410.0],
               'ylim': [-410.0, 410.0],
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
                          'right': {'visible': True,
                                    'lw': 0.6,
                                    'colour': '#262626',
                                    'bounds': None,
                                    'position': None},
                          'bottom': {'visible': True,
                                     'lw': 0.6,
                                     'colour': '#262626',
                                     'bounds': None,
                                     'position': None},
                          'top': {'visible': True,
                                  'lw': 0.6,
                                  'colour': '#262626',
                                  'bounds': None,
                                  'position': None}},
               'xticks': {'at': [], 'labels': []},
               'yticks': {'at': [], 'labels': []},
               'xlabel': None,
               'ylabel': None,
               'files': [{'file': 'active_map.csv',
                          'kind': 'map',
                          'style': {'zorder': 0.0,
                                    'rank': 0,
                                    'cmap': 'cmap1',
                                    'clim': [0.0, 0.001461733]},
                          'styles': [{'zorder': 0.0,
                                      'rank': 0,
                                      'cmap': 'cmap1',
                                      'clim': [0.0, 0.001461733]}]}],
               'decor': [{'kind': 'line',
                          'shape': 'shape0',
                          'style': {'zorder': 4.0,
                                    'rank': 1,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'colour': '#404040',
                                    'mfc': '#404040',
                                    'mec': '#404040',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'what': 'cage_lines'},
                         {'kind': 'line',
                          'shape': 'shape1',
                          'style': {'zorder': 4.0,
                                    'rank': 2,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'colour': '#404040',
                                    'mfc': '#404040',
                                    'mec': '#404040',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'what': 'cage_lines'},
                         {'kind': 'line',
                          'shape': 'shape2',
                          'style': {'zorder': 4.0,
                                    'rank': 3,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'colour': '#404040',
                                    'mfc': '#404040',
                                    'mec': '#404040',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'what': 'cage_lines'},
                         {'kind': 'line',
                          'shape': 'shape3',
                          'style': {'zorder': 4.0,
                                    'rank': 4,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'colour': '#404040',
                                    'mfc': '#404040',
                                    'mec': '#404040',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'what': 'cage_lines'},
                         {'kind': 'line',
                          'shape': 'shape4',
                          'style': {'zorder': 4.0,
                                    'rank': 5,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'colour': '#404040',
                                    'mfc': '#404040',
                                    'mec': '#404040',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'what': 'cage_lines'}],
               'aspect': 1.0,
               'images': [{'cmap': 'cmap1',
                           'clim': [0.0, 0.001461733],
                           'extent': [-410.0, 410.0, -410.0, 410.0],
                           'origin': 'lower',
                           'interpolation': 'bilinear',
                           'zorder': 0.0,
                           'alpha': None}]},
              {'role': 'plot',
               'name': 'Alone',
               'text_style': [],
               'rect': [4.4714, 1.0704, 0.8, 0.8],
               'pos': [0.5260470588235294,
                       0.8299636363636365,
                       0.09411764705882353,
                       0.07272727272727275],
               'xlim': [-410.0, 410.0],
               'ylim': [-410.0, 410.0],
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
                          'right': {'visible': True,
                                    'lw': 0.6,
                                    'colour': '#262626',
                                    'bounds': None,
                                    'position': None},
                          'bottom': {'visible': True,
                                     'lw': 0.6,
                                     'colour': '#262626',
                                     'bounds': None,
                                     'position': None},
                          'top': {'visible': True,
                                  'lw': 0.6,
                                  'colour': '#262626',
                                  'bounds': None,
                                  'position': None}},
               'xticks': {'at': [], 'labels': []},
               'yticks': {'at': [], 'labels': []},
               'xlabel': None,
               'ylabel': None,
               'files': [{'file': 'alone_map.csv',
                          'kind': 'map',
                          'style': {'zorder': 0.0,
                                    'rank': 0,
                                    'cmap': 'cmap2',
                                    'clim': [0.0, 0.001461733]},
                          'styles': [{'zorder': 0.0,
                                      'rank': 0,
                                      'cmap': 'cmap2',
                                      'clim': [0.0, 0.001461733]}]}],
               'decor': [{'kind': 'line',
                          'shape': 'shape0',
                          'style': {'zorder': 4.0,
                                    'rank': 1,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'colour': '#404040',
                                    'mfc': '#404040',
                                    'mec': '#404040',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'what': 'cage_lines'},
                         {'kind': 'line',
                          'shape': 'shape1',
                          'style': {'zorder': 4.0,
                                    'rank': 2,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'colour': '#404040',
                                    'mfc': '#404040',
                                    'mec': '#404040',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'what': 'cage_lines'},
                         {'kind': 'line',
                          'shape': 'shape2',
                          'style': {'zorder': 4.0,
                                    'rank': 3,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'colour': '#404040',
                                    'mfc': '#404040',
                                    'mec': '#404040',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'what': 'cage_lines'},
                         {'kind': 'line',
                          'shape': 'shape3',
                          'style': {'zorder': 4.0,
                                    'rank': 4,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'colour': '#404040',
                                    'mfc': '#404040',
                                    'mec': '#404040',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'what': 'cage_lines'},
                         {'kind': 'line',
                          'shape': 'shape4',
                          'style': {'zorder': 4.0,
                                    'rank': 5,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'colour': '#404040',
                                    'mfc': '#404040',
                                    'mec': '#404040',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'what': 'cage_lines'}],
               'aspect': 1.0,
               'images': [{'cmap': 'cmap2',
                           'clim': [0.0, 0.001461733],
                           'extent': [-410.0, 410.0, -410.0, 410.0],
                           'origin': 'lower',
                           'interpolation': 'bilinear',
                           'zorder': 0.0,
                           'alpha': None}]},
              {'role': 'plot',
               'name': 'Soc-act',
               'text_style': [],
               'rect': [5.3714, 1.0704, 0.8, 0.8],
               'pos': [0.631929411764706,
                       0.8299636363636365,
                       0.09411764705882353,
                       0.07272727272727275],
               'xlim': [-410.0, 410.0],
               'ylim': [-410.0, 410.0],
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
                          'right': {'visible': True,
                                    'lw': 0.6,
                                    'colour': '#262626',
                                    'bounds': None,
                                    'position': None},
                          'bottom': {'visible': True,
                                     'lw': 0.6,
                                     'colour': '#262626',
                                     'bounds': None,
                                     'position': None},
                          'top': {'visible': True,
                                  'lw': 0.6,
                                  'colour': '#262626',
                                  'bounds': None,
                                  'position': None}},
               'xticks': {'at': [], 'labels': []},
               'yticks': {'at': [], 'labels': []},
               'xlabel': None,
               'ylabel': None,
               'files': [{'file': 'soc_act_map.csv',
                          'kind': 'map',
                          'style': {'zorder': 0.0,
                                    'rank': 0,
                                    'cmap': 'cmap3',
                                    'clim': [0.0, 0.001461733]},
                          'styles': [{'zorder': 0.0,
                                      'rank': 0,
                                      'cmap': 'cmap3',
                                      'clim': [0.0, 0.001461733]}]}],
               'decor': [{'kind': 'line',
                          'shape': 'shape0',
                          'style': {'zorder': 4.0,
                                    'rank': 1,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'colour': '#404040',
                                    'mfc': '#404040',
                                    'mec': '#404040',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'what': 'cage_lines'},
                         {'kind': 'line',
                          'shape': 'shape1',
                          'style': {'zorder': 4.0,
                                    'rank': 2,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'colour': '#404040',
                                    'mfc': '#404040',
                                    'mec': '#404040',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'what': 'cage_lines'},
                         {'kind': 'line',
                          'shape': 'shape2',
                          'style': {'zorder': 4.0,
                                    'rank': 3,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'colour': '#404040',
                                    'mfc': '#404040',
                                    'mec': '#404040',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'what': 'cage_lines'},
                         {'kind': 'line',
                          'shape': 'shape3',
                          'style': {'zorder': 4.0,
                                    'rank': 4,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'colour': '#404040',
                                    'mfc': '#404040',
                                    'mec': '#404040',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'what': 'cage_lines'},
                         {'kind': 'line',
                          'shape': 'shape4',
                          'style': {'zorder': 4.0,
                                    'rank': 5,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'colour': '#404040',
                                    'mfc': '#404040',
                                    'mec': '#404040',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'what': 'cage_lines'}],
               'aspect': 1.0,
               'images': [{'cmap': 'cmap3',
                           'clim': [0.0, 0.001461733],
                           'extent': [-410.0, 410.0, -410.0, 410.0],
                           'origin': 'lower',
                           'interpolation': 'bilinear',
                           'zorder': 0.0,
                           'alpha': None}]},
              {'role': 'plot',
               'name': 'Soc-rest',
               'text_style': [],
               'rect': [6.2714, 1.0704, 0.8, 0.8],
               'pos': [0.7378117647058824,
                       0.8299636363636365,
                       0.09411764705882353,
                       0.07272727272727275],
               'xlim': [-410.0, 410.0],
               'ylim': [-410.0, 410.0],
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
                          'right': {'visible': True,
                                    'lw': 0.6,
                                    'colour': '#262626',
                                    'bounds': None,
                                    'position': None},
                          'bottom': {'visible': True,
                                     'lw': 0.6,
                                     'colour': '#262626',
                                     'bounds': None,
                                     'position': None},
                          'top': {'visible': True,
                                  'lw': 0.6,
                                  'colour': '#262626',
                                  'bounds': None,
                                  'position': None}},
               'xticks': {'at': [], 'labels': []},
               'yticks': {'at': [], 'labels': []},
               'xlabel': None,
               'ylabel': None,
               'files': [{'file': 'soc_rest_map.csv',
                          'kind': 'map',
                          'style': {'zorder': 0.0,
                                    'rank': 0,
                                    'cmap': 'cmap4',
                                    'clim': [0.0, 0.001461733]},
                          'styles': [{'zorder': 0.0,
                                      'rank': 0,
                                      'cmap': 'cmap4',
                                      'clim': [0.0, 0.001461733]}]}],
               'decor': [{'kind': 'line',
                          'shape': 'shape0',
                          'style': {'zorder': 4.0,
                                    'rank': 1,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'colour': '#404040',
                                    'mfc': '#404040',
                                    'mec': '#404040',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'what': 'cage_lines'},
                         {'kind': 'line',
                          'shape': 'shape1',
                          'style': {'zorder': 4.0,
                                    'rank': 2,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'colour': '#404040',
                                    'mfc': '#404040',
                                    'mec': '#404040',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'what': 'cage_lines'},
                         {'kind': 'line',
                          'shape': 'shape2',
                          'style': {'zorder': 4.0,
                                    'rank': 3,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'colour': '#404040',
                                    'mfc': '#404040',
                                    'mec': '#404040',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'what': 'cage_lines'},
                         {'kind': 'line',
                          'shape': 'shape3',
                          'style': {'zorder': 4.0,
                                    'rank': 4,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'colour': '#404040',
                                    'mfc': '#404040',
                                    'mec': '#404040',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'what': 'cage_lines'},
                         {'kind': 'line',
                          'shape': 'shape4',
                          'style': {'zorder': 4.0,
                                    'rank': 5,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'colour': '#404040',
                                    'mfc': '#404040',
                                    'mec': '#404040',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'what': 'cage_lines'}],
               'aspect': 1.0,
               'images': [{'cmap': 'cmap4',
                           'clim': [0.0, 0.001461733],
                           'extent': [-410.0, 410.0, -410.0, 410.0],
                           'origin': 'lower',
                           'interpolation': 'bilinear',
                           'zorder': 0.0,
                           'alpha': None}]}],
 'texts': [{'text': 'Example animal:\ntablet\n(n = 2 sessions)',
            'x': 1.2914,
            'y': 1.0704,
            'size': 7.0,
            'weight': 'normal',
            'ha': 'left',
            'va': 'top',
            'rotation': 0.0,
            'colour': '#262626'},
           {'text': 'Climb',
            'x': 3.0714,
            'y': 0.9904,
            'size': 7.0,
            'weight': 'normal',
            'ha': 'center',
            'va': 'baseline',
            'rotation': 0.0,
            'colour': '#4d4aa1'},
           {'text': 'Active',
            'x': 3.9714,
            'y': 0.9904,
            'size': 7.0,
            'weight': 'normal',
            'ha': 'center',
            'va': 'baseline',
            'rotation': 0.0,
            'colour': '#7e478b'},
           {'text': 'Alone',
            'x': 4.8714,
            'y': 0.9904,
            'size': 7.0,
            'weight': 'normal',
            'ha': 'center',
            'va': 'baseline',
            'rotation': 0.0,
            'colour': '#b44574'},
           {'text': 'Soc-act',
            'x': 5.7714,
            'y': 0.9904,
            'size': 7.0,
            'weight': 'normal',
            'ha': 'center',
            'va': 'baseline',
            'rotation': 0.0,
            'colour': '#bc6a5c'},
           {'text': 'Soc-rest',
            'x': 6.6714,
            'y': 0.9904,
            'size': 7.0,
            'weight': 'normal',
            'ha': 'center',
            'va': 'baseline',
            'rotation': 0.0,
            'colour': '#be9146'}],
 'legends': [],
 'letter': {'ch': 'a', 'x': 1.0414, 'baseline': 0.9904, 'top': 0.8704}}


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
                         "supplemental_figures/figS12)")
    a = ap.parse_args(argv)
    for path in render(a.data, a.out_dir):
        print(f"wrote {os.path.normpath(path)}")


if __name__ == "__main__":
    main()
