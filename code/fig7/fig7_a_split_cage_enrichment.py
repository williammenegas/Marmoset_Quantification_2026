r"""
Figure 7, panel a: the recording split (alternating, early vs late) and the cage locations enriched in each group, each map marking where its stimulus stands.

Panel id fig7_a_split_cage_enrichment. Title: "Alternating", "Early vs
late", "Cage locations enriched in each cluster-based group", "Box",
"Intruder", "Mask".

Redrawn from the panel's data folder,
data/fig7/fig7_a_split_cage_enrichment/ (DATA below), with numpy and
matplotlib alone: what the panel shows is read from that folder, and how
the page lays it out -- the axes' rectangles in page inches, limits, ticks,
labels, titles, legends, colour maps, drawing styles, and the decoration
the data leave out (cage wireframes, category outlines, category
boundaries) -- is written below as literals, measured off the published
page.

Usage:

    python fig7_a_split_cage_enrichment.py [--data DIR] [--out-dir DIR]

writes fig7_a_split_cage_enrichment.pdf and
fig7_a_split_cage_enrichment.png (400 dpi), the panel cut from its page,
into figures/fig7/ (OUT below); fig7_page.py draws the whole page and
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
DATA = os.path.join(HERE, "..", "..", "data", "fig7", "fig7_a_split_cage_enrichment")
OUT = os.path.join(HERE, "..", "..", "figures", "fig7")
NAME = "fig7_a_split_cage_enrichment"
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
                                 '#feffffff',
                                 '#fefefeff',
                                 '#fdfefeff',
                                 '#fcfdfdff',
                                 '#fcfdfdff',
                                 '#fbfdfcff',
                                 '#fbfcfcff',
                                 '#fafcfbff',
                                 '#f9fbfbff',
                                 '#f9fbfaff',
                                 '#f8fbfaff',
                                 '#f7faf9ff',
                                 '#f7faf9ff',
                                 '#f6f9f8ff',
                                 '#f6f9f8ff',
                                 '#f5f9f7ff',
                                 '#f4f8f7ff',
                                 '#f4f8f6ff',
                                 '#f3f7f6ff',
                                 '#f2f7f5ff',
                                 '#f2f7f5ff',
                                 '#f1f6f4ff',
                                 '#f1f6f4ff',
                                 '#f0f5f3ff',
                                 '#eff5f3ff',
                                 '#eff5f2ff',
                                 '#eef4f2ff',
                                 '#edf4f1ff',
                                 '#edf3f1ff',
                                 '#ecf3f0ff',
                                 '#ecf3f0ff',
                                 '#ebf2efff',
                                 '#eaf2efff',
                                 '#eaf1eeff',
                                 '#e9f1eeff',
                                 '#e8f1edff',
                                 '#e8f0edff',
                                 '#e7f0edff',
                                 '#e7efecff',
                                 '#e6efecff',
                                 '#e5efebff',
                                 '#e5eeebff',
                                 '#e4eeeaff',
                                 '#e3edeaff',
                                 '#e3ede9ff',
                                 '#e2ede9ff',
                                 '#e1ece8ff',
                                 '#e1ece8ff',
                                 '#e0ece7ff',
                                 '#e0ebe7ff',
                                 '#dfebe6ff',
                                 '#deeae6ff',
                                 '#deeae5ff',
                                 '#ddeae5ff',
                                 '#dce9e4ff',
                                 '#dce9e4ff',
                                 '#dbe8e3ff',
                                 '#dbe8e3ff',
                                 '#dae8e2ff',
                                 '#d9e7e2ff',
                                 '#d9e7e1ff',
                                 '#d8e6e1ff',
                                 '#d7e6e0ff',
                                 '#d7e6e0ff',
                                 '#d6e5dfff',
                                 '#d6e5dfff',
                                 '#d5e4deff',
                                 '#d4e4deff',
                                 '#d4e4ddff',
                                 '#d3e3ddff',
                                 '#d2e3dcff',
                                 '#d2e2dcff',
                                 '#d1e2dbff',
                                 '#d1e2dbff',
                                 '#d0e1dbff',
                                 '#cfe1daff',
                                 '#cfe0daff',
                                 '#cee0d9ff',
                                 '#cde0d9ff',
                                 '#cddfd8ff',
                                 '#ccdfd8ff',
                                 '#cbded7ff',
                                 '#cbded7ff',
                                 '#caded6ff',
                                 '#caddd6ff',
                                 '#c9ddd5ff',
                                 '#c8dcd5ff',
                                 '#c8dcd4ff',
                                 '#c7dcd4ff',
                                 '#c6dbd3ff',
                                 '#c6dbd3ff',
                                 '#c5dad2ff',
                                 '#c5dad2ff',
                                 '#c4dad1ff',
                                 '#c3d9d1ff',
                                 '#c3d9d0ff',
                                 '#c2d8d0ff',
                                 '#c1d8cfff',
                                 '#c1d8cfff',
                                 '#c0d7ceff',
                                 '#c0d7ceff',
                                 '#bfd6cdff',
                                 '#bed6cdff',
                                 '#bed6ccff',
                                 '#bdd5ccff',
                                 '#bcd5cbff',
                                 '#bcd4cbff',
                                 '#bbd4caff',
                                 '#bbd4caff',
                                 '#bad3c9ff',
                                 '#b9d3c9ff',
                                 '#b9d2c9ff',
                                 '#b8d2c8ff',
                                 '#b7d2c8ff',
                                 '#b7d1c7ff',
                                 '#b6d1c7ff',
                                 '#b6d0c6ff',
                                 '#b5d0c6ff',
                                 '#b4d0c5ff',
                                 '#b4cfc5ff',
                                 '#b3cfc4ff',
                                 '#b2cec4ff',
                                 '#b2cec3ff',
                                 '#b1cec3ff',
                                 '#b0cdc2ff',
                                 '#b0cdc2ff',
                                 '#afccc1ff',
                                 '#afccc1ff',
                                 '#aeccc0ff',
                                 '#adcbc0ff',
                                 '#adcbbfff',
                                 '#accabfff',
                                 '#abcabeff',
                                 '#abcabeff',
                                 '#aac9bdff',
                                 '#aac9bdff',
                                 '#a9c8bcff',
                                 '#a8c8bcff',
                                 '#a8c8bbff',
                                 '#a7c7bbff',
                                 '#a6c7baff',
                                 '#a6c7baff',
                                 '#a5c6b9ff',
                                 '#a5c6b9ff',
                                 '#a4c5b8ff',
                                 '#a3c5b8ff',
                                 '#a3c5b8ff',
                                 '#a2c4b7ff',
                                 '#a1c4b7ff',
                                 '#a1c3b6ff',
                                 '#a0c3b6ff',
                                 '#a0c3b5ff',
                                 '#9fc2b5ff',
                                 '#9ec2b4ff',
                                 '#9ec1b4ff',
                                 '#9dc1b3ff',
                                 '#9cc1b3ff',
                                 '#9cc0b2ff',
                                 '#9bc0b2ff',
                                 '#9bbfb1ff',
                                 '#9abfb1ff',
                                 '#99bfb0ff',
                                 '#99beb0ff',
                                 '#98beafff',
                                 '#97bdafff',
                                 '#97bdaeff',
                                 '#96bdaeff',
                                 '#95bcadff',
                                 '#95bcadff',
                                 '#94bbacff',
                                 '#94bbacff',
                                 '#93bbabff',
                                 '#92baabff',
                                 '#92baaaff',
                                 '#91b9aaff',
                                 '#90b9a9ff',
                                 '#90b9a9ff',
                                 '#8fb8a8ff',
                                 '#8fb8a8ff',
                                 '#8eb7a7ff',
                                 '#8db7a7ff',
                                 '#8db7a6ff',
                                 '#8cb6a6ff',
                                 '#8bb6a6ff',
                                 '#8bb5a5ff',
                                 '#8ab5a5ff',
                                 '#8ab5a4ff',
                                 '#89b4a4ff',
                                 '#88b4a3ff',
                                 '#88b3a3ff',
                                 '#87b3a2ff',
                                 '#86b3a2ff',
                                 '#86b2a1ff',
                                 '#85b2a1ff',
                                 '#85b1a0ff',
                                 '#84b1a0ff',
                                 '#83b19fff',
                                 '#83b09fff',
                                 '#82b09eff',
                                 '#81af9eff',
                                 '#81af9dff',
                                 '#80af9dff',
                                 '#80ae9cff',
                                 '#7fae9cff',
                                 '#7ead9bff',
                                 '#7ead9bff',
                                 '#7dad9aff',
                                 '#7cac9aff',
                                 '#7cac99ff',
                                 '#7bab99ff',
                                 '#7aab98ff',
                                 '#7aab98ff',
                                 '#79aa97ff',
                                 '#79aa97ff',
                                 '#78a996ff',
                                 '#77a996ff',
                                 '#77a995ff',
                                 '#76a895ff',
                                 '#75a894ff',
                                 '#75a794ff',
                                 '#74a794ff',
                                 '#74a793ff',
                                 '#73a693ff',
                                 '#72a692ff',
                                 '#72a592ff',
                                 '#71a591ff',
                                 '#70a591ff',
                                 '#70a490ff',
                                 '#6fa490ff',
                                 '#6fa48fff',
                                 '#6ea38fff',
                                 '#6da38eff',
                                 '#6da28eff',
                                 '#6ca28dff',
                                 '#6ba28dff',
                                 '#6ba18cff',
                                 '#6aa18cff',
                                 '#6aa08bff',
                                 '#69a08bff',
                                 '#68a08aff',
                                 '#689f8aff',
                                 '#679f89ff',
                                 '#669e89ff',
                                 '#669e88ff',
                                 '#659e88ff',
                                 '#649d87ff',
                                 '#649d87ff',
                                 '#639c86ff',
                                 '#639c86ff',
                                 '#629c85ff',
                                 '#619b85ff',
                                 '#619b84ff',
                                 '#609a84ff',
                                 '#5f9a83ff',
                                 '#5f9a83ff'],
                     'bad': '#ffffff00'},
           'cmap1': {'colours': ['#ffffffff',
                                 '#fffeffff',
                                 '#fefeffff',
                                 '#fefdfeff',
                                 '#fefdfeff',
                                 '#fdfcfeff',
                                 '#fdfcfeff',
                                 '#fcfbfdff',
                                 '#fcfbfdff',
                                 '#fcfafdff',
                                 '#fbfafdff',
                                 '#fbf9fdff',
                                 '#fbf9fcff',
                                 '#faf8fcff',
                                 '#faf8fcff',
                                 '#faf7fcff',
                                 '#f9f7fbff',
                                 '#f9f6fbff',
                                 '#f8f6fbff',
                                 '#f8f5fbff',
                                 '#f8f5fbff',
                                 '#f7f4faff',
                                 '#f7f4faff',
                                 '#f7f3faff',
                                 '#f6f3faff',
                                 '#f6f2f9ff',
                                 '#f6f2f9ff',
                                 '#f5f1f9ff',
                                 '#f5f1f9ff',
                                 '#f4f0f9ff',
                                 '#f4f0f8ff',
                                 '#f4eff8ff',
                                 '#f3eff8ff',
                                 '#f3eef8ff',
                                 '#f3eef7ff',
                                 '#f2edf7ff',
                                 '#f2edf7ff',
                                 '#f2ecf7ff',
                                 '#f1ecf7ff',
                                 '#f1ebf6ff',
                                 '#f1ebf6ff',
                                 '#f0eaf6ff',
                                 '#f0eaf6ff',
                                 '#efe9f5ff',
                                 '#efe9f5ff',
                                 '#efe8f5ff',
                                 '#eee8f5ff',
                                 '#eee7f5ff',
                                 '#eee7f4ff',
                                 '#ede6f4ff',
                                 '#ede6f4ff',
                                 '#ede5f4ff',
                                 '#ece5f3ff',
                                 '#ece4f3ff',
                                 '#ebe4f3ff',
                                 '#ebe3f3ff',
                                 '#ebe3f3ff',
                                 '#eae2f2ff',
                                 '#eae2f2ff',
                                 '#eae1f2ff',
                                 '#e9e1f2ff',
                                 '#e9e0f1ff',
                                 '#e9e0f1ff',
                                 '#e8dff1ff',
                                 '#e8dff1ff',
                                 '#e7def1ff',
                                 '#e7def0ff',
                                 '#e7ddf0ff',
                                 '#e6ddf0ff',
                                 '#e6dcf0ff',
                                 '#e6dcefff',
                                 '#e5dbefff',
                                 '#e5dbefff',
                                 '#e5daefff',
                                 '#e4daefff',
                                 '#e4d9eeff',
                                 '#e3d9eeff',
                                 '#e3d8eeff',
                                 '#e3d8eeff',
                                 '#e2d7edff',
                                 '#e2d7edff',
                                 '#e2d6edff',
                                 '#e1d6edff',
                                 '#e1d5edff',
                                 '#e1d5ecff',
                                 '#e0d4ecff',
                                 '#e0d4ecff',
                                 '#dfd3ecff',
                                 '#dfd3ebff',
                                 '#dfd2ebff',
                                 '#ded2ebff',
                                 '#ded1ebff',
                                 '#ded1ebff',
                                 '#ddd0eaff',
                                 '#ddd0eaff',
                                 '#ddcfeaff',
                                 '#dccfeaff',
                                 '#dccee9ff',
                                 '#dccee9ff',
                                 '#dbcde9ff',
                                 '#dbcde9ff',
                                 '#dacce9ff',
                                 '#dacce8ff',
                                 '#dacbe8ff',
                                 '#d9cbe8ff',
                                 '#d9cae8ff',
                                 '#d9cae7ff',
                                 '#d8c9e7ff',
                                 '#d8c9e7ff',
                                 '#d8c8e7ff',
                                 '#d7c8e7ff',
                                 '#d7c7e6ff',
                                 '#d6c7e6ff',
                                 '#d6c6e6ff',
                                 '#d6c6e6ff',
                                 '#d5c5e5ff',
                                 '#d5c5e5ff',
                                 '#d5c4e5ff',
                                 '#d4c4e5ff',
                                 '#d4c3e4ff',
                                 '#d4c3e4ff',
                                 '#d3c2e4ff',
                                 '#d3c2e4ff',
                                 '#d2c1e4ff',
                                 '#d2c1e3ff',
                                 '#d2c0e3ff',
                                 '#d1c0e3ff',
                                 '#d1bfe3ff',
                                 '#d1bfe2ff',
                                 '#d0bee2ff',
                                 '#d0bee2ff',
                                 '#d0bde2ff',
                                 '#cfbde2ff',
                                 '#cfbce1ff',
                                 '#cebce1ff',
                                 '#cebbe1ff',
                                 '#cebbe1ff',
                                 '#cdbae0ff',
                                 '#cdbae0ff',
                                 '#cdb9e0ff',
                                 '#ccb9e0ff',
                                 '#ccb8e0ff',
                                 '#ccb8dfff',
                                 '#cbb7dfff',
                                 '#cbb7dfff',
                                 '#cab6dfff',
                                 '#cab6deff',
                                 '#cab5deff',
                                 '#c9b5deff',
                                 '#c9b4deff',
                                 '#c9b4deff',
                                 '#c8b3ddff',
                                 '#c8b3ddff',
                                 '#c8b2ddff',
                                 '#c7b2ddff',
                                 '#c7b1dcff',
                                 '#c6b1dcff',
                                 '#c6b0dcff',
                                 '#c6b0dcff',
                                 '#c5afdcff',
                                 '#c5afdbff',
                                 '#c5aedbff',
                                 '#c4aedbff',
                                 '#c4addbff',
                                 '#c4addaff',
                                 '#c3acdaff',
                                 '#c3acdaff',
                                 '#c3abdaff',
                                 '#c2abdaff',
                                 '#c2aad9ff',
                                 '#c1aad9ff',
                                 '#c1a9d9ff',
                                 '#c1a9d9ff',
                                 '#c0a8d8ff',
                                 '#c0a8d8ff',
                                 '#c0a7d8ff',
                                 '#bfa7d8ff',
                                 '#bfa6d8ff',
                                 '#bfa6d7ff',
                                 '#bea5d7ff',
                                 '#bea5d7ff',
                                 '#bda4d7ff',
                                 '#bda4d6ff',
                                 '#bda3d6ff',
                                 '#bca3d6ff',
                                 '#bca2d6ff',
                                 '#bca2d6ff',
                                 '#bba1d5ff',
                                 '#bba1d5ff',
                                 '#bba0d5ff',
                                 '#baa0d5ff',
                                 '#ba9fd4ff',
                                 '#b99fd4ff',
                                 '#b99ed4ff',
                                 '#b99ed4ff',
                                 '#b89dd4ff',
                                 '#b89dd3ff',
                                 '#b89cd3ff',
                                 '#b79cd3ff',
                                 '#b79bd3ff',
                                 '#b79bd2ff',
                                 '#b69ad2ff',
                                 '#b69ad2ff',
                                 '#b599d2ff',
                                 '#b599d2ff',
                                 '#b598d1ff',
                                 '#b498d1ff',
                                 '#b497d1ff',
                                 '#b497d1ff',
                                 '#b396d0ff',
                                 '#b396d0ff',
                                 '#b395d0ff',
                                 '#b295d0ff',
                                 '#b294d0ff',
                                 '#b194cfff',
                                 '#b193cfff',
                                 '#b193cfff',
                                 '#b092cfff',
                                 '#b092ceff',
                                 '#b091ceff',
                                 '#af91ceff',
                                 '#af90ceff',
                                 '#af90ceff',
                                 '#ae8fcdff',
                                 '#ae8fcdff',
                                 '#ad8ecdff',
                                 '#ad8ecdff',
                                 '#ad8dccff',
                                 '#ac8dccff',
                                 '#ac8cccff',
                                 '#ac8cccff',
                                 '#ab8bccff',
                                 '#ab8bcbff',
                                 '#ab8acbff',
                                 '#aa8acbff',
                                 '#aa89cbff',
                                 '#aa89caff',
                                 '#a988caff',
                                 '#a988caff',
                                 '#a887caff',
                                 '#a887caff',
                                 '#a886c9ff',
                                 '#a786c9ff',
                                 '#a785c9ff',
                                 '#a785c9ff',
                                 '#a684c8ff',
                                 '#a684c8ff',
                                 '#a683c8ff',
                                 '#a583c8ff',
                                 '#a582c8ff',
                                 '#a482c7ff',
                                 '#a481c7ff',
                                 '#a481c7ff',
                                 '#a380c7ff',
                                 '#a380c6ff',
                                 '#a37fc6ff'],
                     'bad': '#ffffff00'},
           'cmap2': {'colours': ['#ffffffff',
                                 '#fffffeff',
                                 '#fefefeff',
                                 '#fefefdff',
                                 '#fefdfcff',
                                 '#fdfdfcff',
                                 '#fdfcfbff',
                                 '#fdfcfaff',
                                 '#fcfbf9ff',
                                 '#fcfbf9ff',
                                 '#fcfaf8ff',
                                 '#fbfaf7ff',
                                 '#fbf9f7ff',
                                 '#fbf9f6ff',
                                 '#faf9f5ff',
                                 '#faf8f5ff',
                                 '#faf8f4ff',
                                 '#f9f7f3ff',
                                 '#f9f7f3ff',
                                 '#f8f6f2ff',
                                 '#f8f6f1ff',
                                 '#f8f5f0ff',
                                 '#f7f5f0ff',
                                 '#f7f4efff',
                                 '#f7f4eeff',
                                 '#f6f4eeff',
                                 '#f6f3edff',
                                 '#f6f3ecff',
                                 '#f5f2ecff',
                                 '#f5f2ebff',
                                 '#f5f1eaff',
                                 '#f4f1eaff',
                                 '#f4f0e9ff',
                                 '#f4f0e8ff',
                                 '#f3efe8ff',
                                 '#f3efe7ff',
                                 '#f3eee6ff',
                                 '#f2eee5ff',
                                 '#f2eee5ff',
                                 '#f2ede4ff',
                                 '#f1ede3ff',
                                 '#f1ece3ff',
                                 '#f1ece2ff',
                                 '#f0ebe1ff',
                                 '#f0ebe1ff',
                                 '#f0eae0ff',
                                 '#efeadfff',
                                 '#efe9dfff',
                                 '#efe9deff',
                                 '#eee9ddff',
                                 '#eee8dcff',
                                 '#eee8dcff',
                                 '#ede7dbff',
                                 '#ede7daff',
                                 '#ece6daff',
                                 '#ece6d9ff',
                                 '#ece5d8ff',
                                 '#ebe5d8ff',
                                 '#ebe4d7ff',
                                 '#ebe4d6ff',
                                 '#eae3d6ff',
                                 '#eae3d5ff',
                                 '#eae3d4ff',
                                 '#e9e2d3ff',
                                 '#e9e2d3ff',
                                 '#e9e1d2ff',
                                 '#e8e1d1ff',
                                 '#e8e0d1ff',
                                 '#e8e0d0ff',
                                 '#e7dfcfff',
                                 '#e7dfcfff',
                                 '#e7deceff',
                                 '#e6decdff',
                                 '#e6decdff',
                                 '#e6ddccff',
                                 '#e5ddcbff',
                                 '#e5dccbff',
                                 '#e5dccaff',
                                 '#e4dbc9ff',
                                 '#e4dbc8ff',
                                 '#e4dac8ff',
                                 '#e3dac7ff',
                                 '#e3d9c6ff',
                                 '#e3d9c6ff',
                                 '#e2d8c5ff',
                                 '#e2d8c4ff',
                                 '#e2d8c4ff',
                                 '#e1d7c3ff',
                                 '#e1d7c2ff',
                                 '#e0d6c2ff',
                                 '#e0d6c1ff',
                                 '#e0d5c0ff',
                                 '#dfd5bfff',
                                 '#dfd4bfff',
                                 '#dfd4beff',
                                 '#ded3bdff',
                                 '#ded3bdff',
                                 '#ded3bcff',
                                 '#ddd2bbff',
                                 '#ddd2bbff',
                                 '#ddd1baff',
                                 '#dcd1b9ff',
                                 '#dcd0b9ff',
                                 '#dcd0b8ff',
                                 '#dbcfb7ff',
                                 '#dbcfb6ff',
                                 '#dbceb6ff',
                                 '#daceb5ff',
                                 '#dacdb4ff',
                                 '#dacdb4ff',
                                 '#d9cdb3ff',
                                 '#d9ccb2ff',
                                 '#d9ccb2ff',
                                 '#d8cbb1ff',
                                 '#d8cbb0ff',
                                 '#d8cab0ff',
                                 '#d7caafff',
                                 '#d7c9aeff',
                                 '#d7c9adff',
                                 '#d6c8adff',
                                 '#d6c8acff',
                                 '#d6c7abff',
                                 '#d5c7abff',
                                 '#d5c7aaff',
                                 '#d5c6a9ff',
                                 '#d4c6a9ff',
                                 '#d4c5a8ff',
                                 '#d3c5a7ff',
                                 '#d3c4a7ff',
                                 '#d3c4a6ff',
                                 '#d2c3a5ff',
                                 '#d2c3a5ff',
                                 '#d2c2a4ff',
                                 '#d1c2a3ff',
                                 '#d1c2a2ff',
                                 '#d1c1a2ff',
                                 '#d0c1a1ff',
                                 '#d0c0a0ff',
                                 '#d0c0a0ff',
                                 '#cfbf9fff',
                                 '#cfbf9eff',
                                 '#cfbe9eff',
                                 '#cebe9dff',
                                 '#cebd9cff',
                                 '#cebd9cff',
                                 '#cdbc9bff',
                                 '#cdbc9aff',
                                 '#cdbc99ff',
                                 '#ccbb99ff',
                                 '#ccbb98ff',
                                 '#ccba97ff',
                                 '#cbba97ff',
                                 '#cbb996ff',
                                 '#cbb995ff',
                                 '#cab895ff',
                                 '#cab894ff',
                                 '#cab793ff',
                                 '#c9b793ff',
                                 '#c9b792ff',
                                 '#c9b691ff',
                                 '#c8b690ff',
                                 '#c8b590ff',
                                 '#c7b58fff',
                                 '#c7b48eff',
                                 '#c7b48eff',
                                 '#c6b38dff',
                                 '#c6b38cff',
                                 '#c6b28cff',
                                 '#c5b28bff',
                                 '#c5b18aff',
                                 '#c5b18aff',
                                 '#c4b189ff',
                                 '#c4b088ff',
                                 '#c4b088ff',
                                 '#c3af87ff',
                                 '#c3af86ff',
                                 '#c3ae85ff',
                                 '#c2ae85ff',
                                 '#c2ad84ff',
                                 '#c2ad83ff',
                                 '#c1ac83ff',
                                 '#c1ac82ff',
                                 '#c1ac81ff',
                                 '#c0ab81ff',
                                 '#c0ab80ff',
                                 '#c0aa7fff',
                                 '#bfaa7fff',
                                 '#bfa97eff',
                                 '#bfa97dff',
                                 '#bea87cff',
                                 '#bea87cff',
                                 '#bea77bff',
                                 '#bda77aff',
                                 '#bda67aff',
                                 '#bda679ff',
                                 '#bca678ff',
                                 '#bca578ff',
                                 '#bba577ff',
                                 '#bba476ff',
                                 '#bba476ff',
                                 '#baa375ff',
                                 '#baa374ff',
                                 '#baa273ff',
                                 '#b9a273ff',
                                 '#b9a172ff',
                                 '#b9a171ff',
                                 '#b8a171ff',
                                 '#b8a070ff',
                                 '#b8a06fff',
                                 '#b79f6fff',
                                 '#b79f6eff',
                                 '#b79e6dff',
                                 '#b69e6dff',
                                 '#b69d6cff',
                                 '#b69d6bff',
                                 '#b59c6aff',
                                 '#b59c6aff',
                                 '#b59b69ff',
                                 '#b49b68ff',
                                 '#b49b68ff',
                                 '#b49a67ff',
                                 '#b39a66ff',
                                 '#b39966ff',
                                 '#b39965ff',
                                 '#b29864ff',
                                 '#b29864ff',
                                 '#b29763ff',
                                 '#b19762ff',
                                 '#b19662ff',
                                 '#b19661ff',
                                 '#b09560ff',
                                 '#b0955fff',
                                 '#af955fff',
                                 '#af945eff',
                                 '#af945dff',
                                 '#ae935dff',
                                 '#ae935cff',
                                 '#ae925bff',
                                 '#ad925bff',
                                 '#ad915aff',
                                 '#ad9159ff',
                                 '#ac9059ff',
                                 '#ac9058ff',
                                 '#ac9057ff',
                                 '#ab8f56ff',
                                 '#ab8f56ff',
                                 '#ab8e55ff',
                                 '#aa8e54ff',
                                 '#aa8d54ff',
                                 '#aa8d53ff',
                                 '#a98c52ff',
                                 '#a98c52ff',
                                 '#a98b51ff',
                                 '#a88b50ff',
                                 '#a88a50ff',
                                 '#a88a4fff'],
                     'bad': '#ffffff00'}},
 'shapes': {'shape0': [[-290.0, -290.0],
                       [290.0, -290.0],
                       [290.0, 290.0],
                       [-290.0, 290.0],
                       [-290.0, -290.0]],
            'shape1': [[-500.0, -500.0], [-290.0, -290.0]],
            'shape2': [[500.0, -500.0], [290.0, -290.0]],
            'shape3': [[500.0, 500.0], [290.0, 290.0]],
            'shape4': [[-500.0, 500.0], [-290.0, 290.0]],
            'shape5': [[0.3193274, 0.0104],
                       [0.4707726, 0.0104],
                       [0.47599506, 0.010568466],
                       [0.48088058, 0.011073866],
                       [0.48542918, 0.011916198],
                       [0.48964084, 0.013095463],
                       [0.49351556, 0.01461166],
                       [0.49705336, 0.016464791],
                       [0.50025422, 0.018654854],
                       [0.50311815, 0.02118185],
                       [0.50564515, 0.024045779],
                       [0.50783521, 0.027246641],
                       [0.50968834, 0.030784435],
                       [0.51120454, 0.034659162],
                       [0.5123838, 0.038870823],
                       [0.51322613, 0.043419416],
                       [0.51373153, 0.048304941],
                       [0.5139, 0.0535274],
                       [0.5139, 0.1260726],
                       [0.51373153, 0.13129506],
                       [0.51322613, 0.13618058],
                       [0.5123838, 0.14072918],
                       [0.51120454, 0.14494084],
                       [0.50968834, 0.14881556],
                       [0.50783521, 0.15235336],
                       [0.50564515, 0.15555422],
                       [0.50311815, 0.15841815],
                       [0.50025422, 0.16094515],
                       [0.49705336, 0.16313521],
                       [0.49351556, 0.16498834],
                       [0.48964084, 0.16650454],
                       [0.48542918, 0.1676838],
                       [0.48088058, 0.16852613],
                       [0.47599506, 0.16903153],
                       [0.4707726, 0.1692],
                       [0.3193274, 0.1692],
                       [0.31410494, 0.16903153],
                       [0.30921942, 0.16852613],
                       [0.30467082, 0.1676838],
                       [0.30045916, 0.16650454],
                       [0.29658444, 0.16498834],
                       [0.29304664, 0.16313521],
                       [0.28984578, 0.16094515],
                       [0.28698185, 0.15841815],
                       [0.28445485, 0.15555422],
                       [0.28226479, 0.15235336],
                       [0.28041166, 0.14881556],
                       [0.27889546, 0.14494084],
                       [0.2777162, 0.14072918],
                       [0.27687387, 0.13618058],
                       [0.27636847, 0.13129506],
                       [0.2762, 0.1260726],
                       [0.2762, 0.0535274],
                       [0.27636847, 0.048304941],
                       [0.27687387, 0.043419416],
                       [0.2777162, 0.038870823],
                       [0.27889546, 0.034659162],
                       [0.28041166, 0.030784435],
                       [0.28226479, 0.027246641],
                       [0.28445485, 0.024045779],
                       [0.28698185, 0.02118185],
                       [0.28984578, 0.018654854],
                       [0.29304664, 0.016464791],
                       [0.29658444, 0.01461166],
                       [0.30045916, 0.013095462],
                       [0.30467082, 0.011916198],
                       [0.30921942, 0.011073866],
                       [0.31410494, 0.010568466],
                       [0.3193274, 0.0104],
                       [0.3193274, 0.0104]],
            'shape6': [[0.5843274, 0.5954],
                       [0.7025726, 0.5954],
                       [0.70779506, 0.59556847],
                       [0.71268058, 0.59607387],
                       [0.71722918, 0.5969162],
                       [0.72144084, 0.59809546],
                       [0.72531556, 0.59961166],
                       [0.72885336, 0.60146479],
                       [0.73205422, 0.60365485],
                       [0.73491815, 0.60618185],
                       [0.73744515, 0.60904578],
                       [0.73963521, 0.61224664],
                       [0.74148834, 0.61578444],
                       [0.74300454, 0.61965916],
                       [0.7441838, 0.62387082],
                       [0.74502613, 0.62841942],
                       [0.74553153, 0.63330494],
                       [0.7457, 0.6385274],
                       [0.7457, 0.7104726],
                       [0.74553153, 0.71569506],
                       [0.74502613, 0.72058058],
                       [0.7441838, 0.72512918],
                       [0.74300454, 0.72934084],
                       [0.74148834, 0.73321556],
                       [0.73963521, 0.73675336],
                       [0.73744515, 0.73995422],
                       [0.73491815, 0.74281815],
                       [0.73205422, 0.74534515],
                       [0.72885336, 0.74753521],
                       [0.72531556, 0.74938834],
                       [0.72144084, 0.75090454],
                       [0.71722918, 0.7520838],
                       [0.71268058, 0.75292613],
                       [0.70779506, 0.75343153],
                       [0.7025726, 0.7536],
                       [0.5843274, 0.7536],
                       [0.57910494, 0.75343153],
                       [0.57421942, 0.75292613],
                       [0.56967082, 0.7520838],
                       [0.56545916, 0.75090454],
                       [0.56158444, 0.74938834],
                       [0.55804664, 0.74753521],
                       [0.55484578, 0.74534515],
                       [0.55198185, 0.74281815],
                       [0.54945485, 0.73995422],
                       [0.54726479, 0.73675336],
                       [0.54541166, 0.73321556],
                       [0.54389546, 0.72934084],
                       [0.5427162, 0.72512918],
                       [0.54187387, 0.72058058],
                       [0.54136847, 0.71569506],
                       [0.5412, 0.7104726],
                       [0.5412, 0.6385274],
                       [0.54136847, 0.63330494],
                       [0.54187387, 0.62841942],
                       [0.5427162, 0.62387082],
                       [0.54389546, 0.61965916],
                       [0.54541166, 0.61578444],
                       [0.54726479, 0.61224664],
                       [0.54945485, 0.60904578],
                       [0.55198185, 0.60618185],
                       [0.55484578, 0.60365485],
                       [0.55804664, 0.60146479],
                       [0.56158444, 0.59961166],
                       [0.56545916, 0.59809546],
                       [0.56967082, 0.5969162],
                       [0.57421942, 0.59607387],
                       [0.57910494, 0.59556847],
                       [0.5843274, 0.5954],
                       [0.5843274, 0.5954]],
            'shape7': [[0.4481274, 0.0259],
                       [0.5663726, 0.0259],
                       [0.57159506, 0.026068466],
                       [0.57648058, 0.026573866],
                       [0.58102918, 0.027416198],
                       [0.58524084, 0.028595463],
                       [0.58911556, 0.03011166],
                       [0.59265336, 0.031964791],
                       [0.59585422, 0.034154854],
                       [0.59871815, 0.03668185],
                       [0.60124515, 0.039545779],
                       [0.60343521, 0.042746641],
                       [0.60528834, 0.046284435],
                       [0.60680454, 0.050159162],
                       [0.6079838, 0.054370823],
                       [0.60882613, 0.058919416],
                       [0.60933153, 0.063804941],
                       [0.6095, 0.0690274],
                       [0.6095, 0.1409726],
                       [0.60933153, 0.14619506],
                       [0.60882613, 0.15108058],
                       [0.6079838, 0.15562918],
                       [0.60680454, 0.15984084],
                       [0.60528834, 0.16371556],
                       [0.60343521, 0.16725336],
                       [0.60124515, 0.17045422],
                       [0.59871815, 0.17331815],
                       [0.59585422, 0.17584515],
                       [0.59265336, 0.17803521],
                       [0.58911556, 0.17988834],
                       [0.58524084, 0.18140454],
                       [0.58102918, 0.1825838],
                       [0.57648058, 0.18342613],
                       [0.57159506, 0.18393153],
                       [0.5663726, 0.1841],
                       [0.4481274, 0.1841],
                       [0.44290494, 0.18393153],
                       [0.43801942, 0.18342613],
                       [0.43347082, 0.1825838],
                       [0.42925916, 0.18140454],
                       [0.42538444, 0.17988834],
                       [0.42184664, 0.17803521],
                       [0.41864578, 0.17584515],
                       [0.41578185, 0.17331815],
                       [0.41325485, 0.17045422],
                       [0.41106479, 0.16725336],
                       [0.40921166, 0.16371556],
                       [0.40769546, 0.15984084],
                       [0.4065162, 0.15562918],
                       [0.40567387, 0.15108058],
                       [0.40516847, 0.14619506],
                       [0.405, 0.1409726],
                       [0.405, 0.0690274],
                       [0.40516847, 0.063804941],
                       [0.40567387, 0.058919416],
                       [0.4065162, 0.054370823],
                       [0.40769546, 0.050159162],
                       [0.40921166, 0.046284435],
                       [0.41106479, 0.042746641],
                       [0.41325485, 0.039545779],
                       [0.41578185, 0.03668185],
                       [0.41864578, 0.034154854],
                       [0.42184664, 0.031964791],
                       [0.42538444, 0.03011166],
                       [0.42925916, 0.028595462],
                       [0.43347082, 0.027416198],
                       [0.43801942, 0.026573866],
                       [0.44290494, 0.026068466],
                       [0.4481274, 0.0259],
                       [0.4481274, 0.0259]],
            'shape8': [[0.3193274, 0.0104],
                       [0.4707726, 0.0104],
                       [0.47599506, 0.010568466],
                       [0.48088058, 0.011073866],
                       [0.48542918, 0.011916198],
                       [0.48964084, 0.013095463],
                       [0.49351556, 0.01461166],
                       [0.49705336, 0.016464791],
                       [0.50025422, 0.018654854],
                       [0.50311815, 0.02118185],
                       [0.50564515, 0.024045779],
                       [0.50783521, 0.027246641],
                       [0.50968834, 0.030784435],
                       [0.51120454, 0.034659163],
                       [0.5123838, 0.038870823],
                       [0.51322613, 0.043419416],
                       [0.51373153, 0.048304941],
                       [0.5139, 0.0535274],
                       [0.5139, 0.1260726],
                       [0.51373153, 0.13129506],
                       [0.51322613, 0.13618058],
                       [0.5123838, 0.14072918],
                       [0.51120454, 0.14494084],
                       [0.50968834, 0.14881556],
                       [0.50783521, 0.15235336],
                       [0.50564515, 0.15555422],
                       [0.50311815, 0.15841815],
                       [0.50025422, 0.16094515],
                       [0.49705336, 0.16313521],
                       [0.49351556, 0.16498834],
                       [0.48964084, 0.16650454],
                       [0.48542918, 0.1676838],
                       [0.48088058, 0.16852613],
                       [0.47599506, 0.16903153],
                       [0.4707726, 0.1692],
                       [0.3193274, 0.1692],
                       [0.31410494, 0.16903153],
                       [0.30921942, 0.16852613],
                       [0.30467082, 0.1676838],
                       [0.30045916, 0.16650454],
                       [0.29658444, 0.16498834],
                       [0.29304664, 0.16313521],
                       [0.28984578, 0.16094515],
                       [0.28698185, 0.15841815],
                       [0.28445485, 0.15555422],
                       [0.28226479, 0.15235336],
                       [0.28041166, 0.14881556],
                       [0.27889546, 0.14494084],
                       [0.2777162, 0.14072918],
                       [0.27687387, 0.13618058],
                       [0.27636847, 0.13129506],
                       [0.2762, 0.1260726],
                       [0.2762, 0.0535274],
                       [0.27636847, 0.048304941],
                       [0.27687387, 0.043419416],
                       [0.2777162, 0.038870823],
                       [0.27889546, 0.034659163],
                       [0.28041166, 0.030784435],
                       [0.28226479, 0.027246641],
                       [0.28445485, 0.024045779],
                       [0.28698185, 0.02118185],
                       [0.28984578, 0.018654854],
                       [0.29304664, 0.016464791],
                       [0.29658444, 0.01461166],
                       [0.30045916, 0.013095463],
                       [0.30467082, 0.011916198],
                       [0.30921942, 0.011073866],
                       [0.31410494, 0.010568466],
                       [0.3193274, 0.0104],
                       [0.3193274, 0.0104]],
            'shape9': [[0.4481274, 0.0259],
                       [0.5663726, 0.0259],
                       [0.57159506, 0.026068466],
                       [0.57648058, 0.026573866],
                       [0.58102918, 0.027416198],
                       [0.58524084, 0.028595463],
                       [0.58911556, 0.03011166],
                       [0.59265336, 0.031964791],
                       [0.59585422, 0.034154854],
                       [0.59871815, 0.03668185],
                       [0.60124515, 0.039545779],
                       [0.60343521, 0.042746641],
                       [0.60528834, 0.046284435],
                       [0.60680454, 0.050159163],
                       [0.6079838, 0.054370823],
                       [0.60882613, 0.058919416],
                       [0.60933153, 0.063804941],
                       [0.6095, 0.0690274],
                       [0.6095, 0.1409726],
                       [0.60933153, 0.14619506],
                       [0.60882613, 0.15108058],
                       [0.6079838, 0.15562918],
                       [0.60680454, 0.15984084],
                       [0.60528834, 0.16371556],
                       [0.60343521, 0.16725336],
                       [0.60124515, 0.17045422],
                       [0.59871815, 0.17331815],
                       [0.59585422, 0.17584515],
                       [0.59265336, 0.17803521],
                       [0.58911556, 0.17988834],
                       [0.58524084, 0.18140454],
                       [0.58102918, 0.1825838],
                       [0.57648058, 0.18342613],
                       [0.57159506, 0.18393153],
                       [0.5663726, 0.1841],
                       [0.4481274, 0.1841],
                       [0.44290494, 0.18393153],
                       [0.43801942, 0.18342613],
                       [0.43347082, 0.1825838],
                       [0.42925916, 0.18140454],
                       [0.42538444, 0.17988834],
                       [0.42184664, 0.17803521],
                       [0.41864578, 0.17584515],
                       [0.41578185, 0.17331815],
                       [0.41325485, 0.17045422],
                       [0.41106479, 0.16725336],
                       [0.40921166, 0.16371556],
                       [0.40769546, 0.15984084],
                       [0.4065162, 0.15562918],
                       [0.40567387, 0.15108058],
                       [0.40516847, 0.14619506],
                       [0.405, 0.1409726],
                       [0.405, 0.0690274],
                       [0.40516847, 0.063804941],
                       [0.40567387, 0.058919416],
                       [0.4065162, 0.054370823],
                       [0.40769546, 0.050159163],
                       [0.40921166, 0.046284435],
                       [0.41106479, 0.042746641],
                       [0.41325485, 0.039545779],
                       [0.41578185, 0.03668185],
                       [0.41864578, 0.034154854],
                       [0.42184664, 0.031964791],
                       [0.42538444, 0.03011166],
                       [0.42925916, 0.028595463],
                       [0.43347082, 0.027416198],
                       [0.43801942, 0.026573866],
                       [0.44290494, 0.026068466],
                       [0.4481274, 0.0259],
                       [0.4481274, 0.0259]],
            'shape10': [[0.4481274, 0.0259],
                        [0.5663726, 0.0259],
                        [0.57159506, 0.026068466],
                        [0.57648058, 0.026573866],
                        [0.58102918, 0.027416198],
                        [0.58524084, 0.028595463],
                        [0.58911556, 0.03011166],
                        [0.59265336, 0.031964791],
                        [0.59585422, 0.034154854],
                        [0.59871815, 0.03668185],
                        [0.60124515, 0.039545779],
                        [0.60343521, 0.042746641],
                        [0.60528834, 0.046284435],
                        [0.60680454, 0.050159163],
                        [0.6079838, 0.054370823],
                        [0.60882613, 0.058919416],
                        [0.60933153, 0.063804941],
                        [0.6095, 0.0690274],
                        [0.6095, 0.1409726],
                        [0.60933153, 0.14619506],
                        [0.60882613, 0.15108058],
                        [0.6079838, 0.15562918],
                        [0.60680454, 0.15984084],
                        [0.60528834, 0.16371556],
                        [0.60343521, 0.16725336],
                        [0.60124515, 0.17045422],
                        [0.59871815, 0.17331815],
                        [0.59585422, 0.17584515],
                        [0.59265336, 0.17803521],
                        [0.58911556, 0.17988834],
                        [0.58524084, 0.18140454],
                        [0.58102918, 0.1825838],
                        [0.57648058, 0.18342613],
                        [0.57159506, 0.18393153],
                        [0.5663726, 0.1841],
                        [0.4481274, 0.1841],
                        [0.44290494, 0.18393153],
                        [0.43801942, 0.18342613],
                        [0.43347082, 0.1825838],
                        [0.42925916, 0.18140454],
                        [0.42538444, 0.17988834],
                        [0.42184664, 0.17803521],
                        [0.41864578, 0.17584515],
                        [0.41578185, 0.17331815],
                        [0.41325485, 0.17045422],
                        [0.41106479, 0.16725336],
                        [0.40921166, 0.16371556],
                        [0.40769546, 0.15984084],
                        [0.4065162, 0.15562918],
                        [0.40567387, 0.15108058],
                        [0.40516847, 0.14619506],
                        [0.405, 0.1409726],
                        [0.405, 0.0690274],
                        [0.40516847, 0.063804941],
                        [0.40567387, 0.058919416],
                        [0.4065162, 0.054370823],
                        [0.40769546, 0.050159162],
                        [0.40921166, 0.046284435],
                        [0.41106479, 0.042746641],
                        [0.41325485, 0.039545779],
                        [0.41578185, 0.03668185],
                        [0.41864578, 0.034154854],
                        [0.42184664, 0.031964791],
                        [0.42538444, 0.03011166],
                        [0.42925916, 0.028595463],
                        [0.43347082, 0.027416198],
                        [0.43801942, 0.026573866],
                        [0.44290494, 0.026068466],
                        [0.4481274, 0.0259],
                        [0.4481274, 0.0259]]}}
PANEL = {'title': ['Alternating',
           'Early vs late',
           'Cage locations enriched in each cluster-based group',
           'Box',
           'Intruder',
           'Mask'],
 'headings': [],
 'partial': '',
 'subplots': [{'role': 'plot',
               'name': 'Alternating',
               'text_style': [],
               'rect': [0.5213, 0.5287, 0.82, 0.275],
               'pos': [0.06132941176470588,
                       0.9269363636363637,
                       0.09647058823529411,
                       0.025000000000000022],
               'xlim': [-1.5, 13.5],
               'ylim': [-0.4509090909090909, 0.5490909090909091],
               'xscale': 'linear',
               'yscale': 'linear',
               'axis_off': False,
               'facecolor': '#ffffff',
               'frame': True,
               'zorder': 0.0,
               'spines': {'left': {'visible': False,
                                   'lw': 0.6,
                                   'colour': '#262626',
                                   'bounds': None,
                                   'position': ['outward', 2.0]},
                          'right': {'visible': False,
                                    'lw': 0.6,
                                    'colour': '#262626',
                                    'bounds': None,
                                    'position': None},
                          'bottom': {'visible': True,
                                     'lw': 0.6,
                                     'colour': '#262626',
                                     'bounds': None,
                                     'position': ['outward', 2.0]},
                          'top': {'visible': False,
                                  'lw': 0.6,
                                  'colour': '#262626',
                                  'bounds': None,
                                  'position': None}},
               'xticks': {'at': [0.0, 3.0, 6.0, 9.0, 12.0],
                          'labels': ['0', '3', '6', '9', '12'],
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
               'yticks': {'at': [], 'labels': []},
               'xlabel': {'text': 'Time (months)',
                          'size': 7.0,
                          'colour': '#262626',
                          'rotation': 0.0,
                          'pad': 4.0,
                          'ha': 'center',
                          'va': 'top'},
               'ylabel': None,
               'files': [{'file': 'alternating_lines.csv',
                          'kind': 'lines',
                          'style': {'zorder': 1.0,
                                    'rank': 0,
                                    'lw': 0.5,
                                    'colour': '#b8b8b8',
                                    'mfc': '#b8b8b8',
                                    'mec': '#b8b8b8',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'styles': [{'zorder': 1.0,
                                      'rank': 0,
                                      'lw': 0.5,
                                      'colour': '#b8b8b8',
                                      'mfc': '#b8b8b8',
                                      'mec': '#b8b8b8',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 3.0,
                                      'rank': 1,
                                      'lw': 1.5,
                                      'ls': 'None',
                                      'colour': '#1f77b4',
                                      'mfc': '#404040',
                                      'mec': '#404040',
                                      'marker': 'o',
                                      'ms': 5.0,
                                      'mew': 0.8,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 3.0,
                                      'rank': 2,
                                      'lw': 1.5,
                                      'ls': 'None',
                                      'colour': '#ff7f0e',
                                      'mfc': 'none',
                                      'mec': '#404040',
                                      'marker': 'o',
                                      'ms': 5.0,
                                      'mew': 0.8,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 3.0,
                                      'rank': 3,
                                      'lw': 1.5,
                                      'ls': 'None',
                                      'colour': '#2ca02c',
                                      'mfc': '#404040',
                                      'mec': '#404040',
                                      'marker': 'o',
                                      'ms': 5.0,
                                      'mew': 0.8,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 3.0,
                                      'rank': 4,
                                      'lw': 1.5,
                                      'ls': 'None',
                                      'colour': '#d62728',
                                      'mfc': 'none',
                                      'mec': '#404040',
                                      'marker': 'o',
                                      'ms': 5.0,
                                      'mew': 0.8,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 3.0,
                                      'rank': 5,
                                      'lw': 1.5,
                                      'ls': 'None',
                                      'colour': '#9467bd',
                                      'mfc': '#404040',
                                      'mec': '#404040',
                                      'marker': 'o',
                                      'ms': 5.0,
                                      'mew': 0.8,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'}]}],
               'decor': [],
               'aspect': 'auto'},
              {'role': 'plot',
               'name': 'Early vs late',
               'text_style': [],
               'rect': [1.8853, 0.5287, 0.82, 0.275],
               'pos': [0.2218,
                       0.9269363636363637,
                       0.09647058823529409,
                       0.025000000000000022],
               'xlim': [-1.5, 13.5],
               'ylim': [-0.5, 0.5],
               'xscale': 'linear',
               'yscale': 'linear',
               'axis_off': False,
               'facecolor': '#ffffff',
               'frame': True,
               'zorder': 0.0,
               'spines': {'left': {'visible': False,
                                   'lw': 0.6,
                                   'colour': '#262626',
                                   'bounds': None,
                                   'position': ['outward', 2.0]},
                          'right': {'visible': False,
                                    'lw': 0.6,
                                    'colour': '#262626',
                                    'bounds': None,
                                    'position': None},
                          'bottom': {'visible': True,
                                     'lw': 0.6,
                                     'colour': '#262626',
                                     'bounds': None,
                                     'position': ['outward', 2.0]},
                          'top': {'visible': False,
                                  'lw': 0.6,
                                  'colour': '#262626',
                                  'bounds': None,
                                  'position': None}},
               'xticks': {'at': [0.0, 3.0, 6.0, 9.0, 12.0],
                          'labels': ['0', '3', '6', '9', '12'],
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
               'yticks': {'at': [], 'labels': []},
               'xlabel': {'text': 'Time (months)',
                          'size': 7.0,
                          'colour': '#262626',
                          'rotation': 0.0,
                          'pad': 4.0,
                          'ha': 'center',
                          'va': 'top'},
               'ylabel': None,
               'files': [{'file': 'early_vs_late_lines.csv',
                          'kind': 'lines',
                          'style': {'zorder': 1.0,
                                    'rank': 0,
                                    'lw': 0.5,
                                    'colour': '#b8b8b8',
                                    'mfc': '#b8b8b8',
                                    'mec': '#b8b8b8',
                                    'ms': 6.0,
                                    'mew': 1.0,
                                    'capstyle': 'projecting',
                                    'joinstyle': 'round'},
                          'styles': [{'zorder': 1.0,
                                      'rank': 0,
                                      'lw': 0.5,
                                      'colour': '#b8b8b8',
                                      'mfc': '#b8b8b8',
                                      'mec': '#b8b8b8',
                                      'ms': 6.0,
                                      'mew': 1.0,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 3.0,
                                      'rank': 1,
                                      'lw': 1.5,
                                      'ls': 'None',
                                      'colour': '#1f77b4',
                                      'mfc': '#404040',
                                      'mec': '#404040',
                                      'marker': 'o',
                                      'ms': 5.0,
                                      'mew': 0.8,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 3.0,
                                      'rank': 2,
                                      'lw': 1.5,
                                      'ls': 'None',
                                      'colour': '#ff7f0e',
                                      'mfc': '#404040',
                                      'mec': '#404040',
                                      'marker': 'o',
                                      'ms': 5.0,
                                      'mew': 0.8,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 3.0,
                                      'rank': 3,
                                      'lw': 1.5,
                                      'ls': 'None',
                                      'colour': '#2ca02c',
                                      'mfc': '#404040',
                                      'mec': '#404040',
                                      'marker': 'o',
                                      'ms': 5.0,
                                      'mew': 0.8,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 3.0,
                                      'rank': 4,
                                      'lw': 1.5,
                                      'ls': 'None',
                                      'colour': '#d62728',
                                      'mfc': 'none',
                                      'mec': '#404040',
                                      'marker': 'o',
                                      'ms': 5.0,
                                      'mew': 0.8,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'},
                                     {'zorder': 3.0,
                                      'rank': 5,
                                      'lw': 1.5,
                                      'ls': 'None',
                                      'colour': '#9467bd',
                                      'mfc': 'none',
                                      'mec': '#404040',
                                      'marker': 'o',
                                      'ms': 5.0,
                                      'mew': 0.8,
                                      'capstyle': 'projecting',
                                      'joinstyle': 'round'}]}],
               'decor': [],
               'aspect': 'auto'},
              {'role': 'plot',
               'name': 'Box Group 1',
               'text_style': [],
               'rect': [0.5234, 1.5984, 0.7188, 0.7188],
               'pos': [0.06157647058823529,
                       0.7893454545454546,
                       0.08456470588235293,
                       0.0653454545454546],
               'xlim': [-500.0, 500.0],
               'ylim': [-500.0, 500.0],
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
               'files': [{'file': 'box_group_1_map.csv',
                          'kind': 'map',
                          'style': {'zorder': 0.0,
                                    'rank': 0,
                                    'cmap': 'cmap0',
                                    'clim': [0.0, 1.5]},
                          'styles': [{'zorder': 0.0,
                                      'rank': 0,
                                      'cmap': 'cmap0',
                                      'clim': [0.0, 1.5]}]}],
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
                          'what': 'cage_lines'},
                         {'kind': 'patch',
                          'shape': 'shape5',
                          'style': {'zorder': 6.0,
                                    'rank': 6,
                                    'clip': False,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'face': '#e6e7e8',
                                    'edge': '#414042',
                                    'pcap': 'butt',
                                    'pjoin': 'miter',
                                    'fill': True,
                                    'filled': True},
                          'what': 'stim_box'}],
               'aspect': 1.0,
               'images': [{'cmap': 'cmap0',
                           'clim': [0.0, 1.5],
                           'extent': [-500.0, 500.0, -500.0, 500.0],
                           'origin': 'lower',
                           'interpolation': 'nearest',
                           'zorder': 0.0,
                           'alpha': None}]},
              {'role': 'plot',
               'name': 'Intruder 1',
               'text_style': [],
               'rect': [1.2974923, 1.5984, 0.7188, 0.7188],
               'pos': [0.15264615384615385,
                       0.7893454545454546,
                       0.08456470588235296,
                       0.0653454545454546],
               'xlim': [-500.0, 500.0],
               'ylim': [-500.0, 500.0],
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
               'files': [{'file': 'intruder_1_map.csv',
                          'kind': 'map',
                          'style': {'zorder': 0.0,
                                    'rank': 0,
                                    'cmap': 'cmap0',
                                    'clim': [0.0, 1.5]},
                          'styles': [{'zorder': 0.0,
                                      'rank': 0,
                                      'cmap': 'cmap0',
                                      'clim': [0.0, 1.5]}]}],
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
                          'what': 'cage_lines'},
                         {'kind': 'patch',
                          'shape': 'shape6',
                          'style': {'zorder': 6.0,
                                    'rank': 6,
                                    'clip': False,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'face': '#e6e7e8',
                                    'edge': '#414042',
                                    'pcap': 'butt',
                                    'pjoin': 'miter',
                                    'fill': True,
                                    'filled': True},
                          'what': 'stim_box'}],
               'aspect': 1.0,
               'images': [{'cmap': 'cmap0',
                           'clim': [0.0, 1.5],
                           'extent': [-500.0, 500.0, -500.0, 500.0],
                           'origin': 'lower',
                           'interpolation': 'nearest',
                           'zorder': 0.0,
                           'alpha': None}]},
              {'role': 'plot',
               'name': 'Mask 1',
               'text_style': [],
               'rect': [2.0715846, 1.5984, 0.7188, 0.7188],
               'pos': [0.2437158371040724,
                       0.7893454545454546,
                       0.08456470588235293,
                       0.0653454545454546],
               'xlim': [-500.0, 500.0],
               'ylim': [-500.0, 500.0],
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
               'files': [{'file': 'mask_1_map.csv',
                          'kind': 'map',
                          'style': {'zorder': 0.0,
                                    'rank': 0,
                                    'cmap': 'cmap0',
                                    'clim': [0.0, 1.5]},
                          'styles': [{'zorder': 0.0,
                                      'rank': 0,
                                      'cmap': 'cmap0',
                                      'clim': [0.0, 1.5]}]}],
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
                          'what': 'cage_lines'},
                         {'kind': 'patch',
                          'shape': 'shape7',
                          'style': {'zorder': 6.0,
                                    'rank': 6,
                                    'clip': False,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'face': '#e6e7e8',
                                    'edge': '#414042',
                                    'pcap': 'butt',
                                    'pjoin': 'miter',
                                    'fill': True,
                                    'filled': True},
                          'what': 'stim_box'}],
               'aspect': 1.0,
               'images': [{'cmap': 'cmap0',
                           'clim': [0.0, 1.5],
                           'extent': [-500.0, 500.0, -500.0, 500.0],
                           'origin': 'lower',
                           'interpolation': 'nearest',
                           'zorder': 0.0,
                           'alpha': None}]},
              {'role': 'colorbar',
               'name': 'Mask 1 colour bar',
               'text_style': [],
               'rect': [2.8641077, 1.5984, 0.046076923, 0.7188],
               'pos': [0.3369538461538462,
                       0.7893454545454546,
                       0.005420814479637992,
                       0.0653454545454546],
               'xlim': [0.0, 1.0],
               'ylim': [0.0, 1.5],
               'xscale': 'linear',
               'yscale': 'linear',
               'axis_off': False,
               'facecolor': '#ffffff',
               'frame': True,
               'zorder': 0.0,
               'spines': {'left': {'visible': False,
                                   'lw': 0.8,
                                   'colour': '#000000',
                                   'bounds': None,
                                   'position': None},
                          'right': {'visible': True,
                                    'lw': 0.6,
                                    'colour': '#262626',
                                    'bounds': [0.0, 1.5],
                                    'position': ['outward',
                                                 1.843076923076923]},
                          'bottom': {'visible': False,
                                     'lw': 0.8,
                                     'colour': '#000000',
                                     'bounds': None,
                                     'position': None},
                          'top': {'visible': False,
                                  'lw': 0.8,
                                  'colour': '#000000',
                                  'bounds': None,
                                  'position': None},
                          'outline': {'visible': True,
                                      'lw': 0.5,
                                      'colour': '#000000',
                                      'bounds': None,
                                      'position': None}},
               'xticks': {'at': [], 'labels': []},
               'yticks': {'at': [0.0, 0.75, 1.5],
                          'labels': ['0', '0.75', '1.5'],
                          'pad': 1.3823077,
                          'size': 2.4881538,
                          'width': 0.6,
                          'direction': 'out',
                          'visible': [False, True],
                          'label_visible': [False, True],
                          'labelsize': 6.4507692,
                          'colour': '#000000',
                          'labelcolour': '#000000',
                          'rotation': 0.0,
                          'ha': 'left',
                          'va': 'center_baseline'},
               'xlabel': None,
               'ylabel': None,
               'files': [],
               'decor': [],
               'ylabel_side': 'right',
               'aspect': 'auto',
               'bar_texts': [],
               'cbar': {'cmap': 'cmap0',
                        'clim': [0.0, 1.5],
                        'orientation': 'vertical'}},
              {'role': 'plot',
               'name': 'Box Group 2',
               'text_style': [],
               'rect': [0.5234, 2.4277846, 0.7188, 0.7188],
               'pos': [0.06157647058823529,
                       0.7139468531468531,
                       0.08456470588235293,
                       0.0653454545454546],
               'xlim': [-500.0, 500.0],
               'ylim': [-500.0, 500.0],
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
               'files': [{'file': 'box_group_2_map.csv',
                          'kind': 'map',
                          'style': {'zorder': 0.0,
                                    'rank': 0,
                                    'cmap': 'cmap1',
                                    'clim': [0.0, 1.5]},
                          'styles': [{'zorder': 0.0,
                                      'rank': 0,
                                      'cmap': 'cmap1',
                                      'clim': [0.0, 1.5]}]}],
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
                          'what': 'cage_lines'},
                         {'kind': 'patch',
                          'shape': 'shape8',
                          'style': {'zorder': 6.0,
                                    'rank': 6,
                                    'clip': False,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'face': '#e6e7e8',
                                    'edge': '#414042',
                                    'pcap': 'butt',
                                    'pjoin': 'miter',
                                    'fill': True,
                                    'filled': True},
                          'what': 'stim_box'}],
               'aspect': 1.0,
               'images': [{'cmap': 'cmap1',
                           'clim': [0.0, 1.5],
                           'extent': [-500.0, 500.0, -500.0, 500.0],
                           'origin': 'lower',
                           'interpolation': 'nearest',
                           'zorder': 0.0,
                           'alpha': None}]},
              {'role': 'plot',
               'name': 'Intruder 2',
               'text_style': [],
               'rect': [1.2974923, 2.4277846, 0.7188, 0.7188],
               'pos': [0.15264615384615385,
                       0.7139468531468531,
                       0.08456470588235296,
                       0.0653454545454546],
               'xlim': [-500.0, 500.0],
               'ylim': [-500.0, 500.0],
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
               'files': [{'file': 'intruder_2_map.csv',
                          'kind': 'map',
                          'style': {'zorder': 0.0,
                                    'rank': 0,
                                    'cmap': 'cmap1',
                                    'clim': [0.0, 1.5]},
                          'styles': [{'zorder': 0.0,
                                      'rank': 0,
                                      'cmap': 'cmap1',
                                      'clim': [0.0, 1.5]}]}],
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
                          'what': 'cage_lines'},
                         {'kind': 'patch',
                          'shape': 'shape6',
                          'style': {'zorder': 6.0,
                                    'rank': 6,
                                    'clip': False,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'face': '#e6e7e8',
                                    'edge': '#414042',
                                    'pcap': 'butt',
                                    'pjoin': 'miter',
                                    'fill': True,
                                    'filled': True},
                          'what': 'stim_box'}],
               'aspect': 1.0,
               'images': [{'cmap': 'cmap1',
                           'clim': [0.0, 1.5],
                           'extent': [-500.0, 500.0, -500.0, 500.0],
                           'origin': 'lower',
                           'interpolation': 'nearest',
                           'zorder': 0.0,
                           'alpha': None}]},
              {'role': 'plot',
               'name': 'Mask 2',
               'text_style': [],
               'rect': [2.0715846, 2.4277846, 0.7188, 0.7188],
               'pos': [0.2437158371040724,
                       0.7139468531468531,
                       0.08456470588235293,
                       0.0653454545454546],
               'xlim': [-500.0, 500.0],
               'ylim': [-500.0, 500.0],
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
               'files': [{'file': 'mask_2_map.csv',
                          'kind': 'map',
                          'style': {'zorder': 0.0,
                                    'rank': 0,
                                    'cmap': 'cmap1',
                                    'clim': [0.0, 1.5]},
                          'styles': [{'zorder': 0.0,
                                      'rank': 0,
                                      'cmap': 'cmap1',
                                      'clim': [0.0, 1.5]}]}],
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
                          'what': 'cage_lines'},
                         {'kind': 'patch',
                          'shape': 'shape9',
                          'style': {'zorder': 6.0,
                                    'rank': 6,
                                    'clip': False,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'face': '#e6e7e8',
                                    'edge': '#414042',
                                    'pcap': 'butt',
                                    'pjoin': 'miter',
                                    'fill': True,
                                    'filled': True},
                          'what': 'stim_box'}],
               'aspect': 1.0,
               'images': [{'cmap': 'cmap1',
                           'clim': [0.0, 1.5],
                           'extent': [-500.0, 500.0, -500.0, 500.0],
                           'origin': 'lower',
                           'interpolation': 'nearest',
                           'zorder': 0.0,
                           'alpha': None}]},
              {'role': 'colorbar',
               'name': 'Mask 2 colour bar',
               'text_style': [],
               'rect': [2.8641077, 2.4277846, 0.046076923, 0.7188],
               'pos': [0.3369538461538462,
                       0.7139468531468531,
                       0.005420814479637992,
                       0.0653454545454546],
               'xlim': [0.0, 1.0],
               'ylim': [0.0, 1.5],
               'xscale': 'linear',
               'yscale': 'linear',
               'axis_off': False,
               'facecolor': '#ffffff',
               'frame': True,
               'zorder': 0.0,
               'spines': {'left': {'visible': False,
                                   'lw': 0.8,
                                   'colour': '#000000',
                                   'bounds': None,
                                   'position': None},
                          'right': {'visible': True,
                                    'lw': 0.6,
                                    'colour': '#262626',
                                    'bounds': [0.0, 1.5],
                                    'position': ['outward',
                                                 1.843076923076923]},
                          'bottom': {'visible': False,
                                     'lw': 0.8,
                                     'colour': '#000000',
                                     'bounds': None,
                                     'position': None},
                          'top': {'visible': False,
                                  'lw': 0.8,
                                  'colour': '#000000',
                                  'bounds': None,
                                  'position': None},
                          'outline': {'visible': True,
                                      'lw': 0.5,
                                      'colour': '#000000',
                                      'bounds': None,
                                      'position': None}},
               'xticks': {'at': [], 'labels': []},
               'yticks': {'at': [0.0, 0.75, 1.5],
                          'labels': ['0', '0.75', '1.5'],
                          'pad': 1.3823077,
                          'size': 2.4881538,
                          'width': 0.6,
                          'direction': 'out',
                          'visible': [False, True],
                          'label_visible': [False, True],
                          'labelsize': 6.4507692,
                          'colour': '#000000',
                          'labelcolour': '#000000',
                          'rotation': 0.0,
                          'ha': 'left',
                          'va': 'center_baseline'},
               'xlabel': None,
               'ylabel': None,
               'files': [],
               'decor': [],
               'ylabel_side': 'right',
               'aspect': 'auto',
               'bar_texts': [],
               'cbar': {'cmap': 'cmap1',
                        'clim': [0.0, 1.5],
                        'orientation': 'vertical'}},
              {'role': 'plot',
               'name': 'Box Group 3',
               'text_style': [],
               'rect': [0.5234, 3.2571692, 0.7188, 0.7188],
               'pos': [0.06157647058823529,
                       0.6385482517482517,
                       0.08456470588235293,
                       0.0653454545454546],
               'xlim': [-500.0, 500.0],
               'ylim': [-500.0, 500.0],
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
               'files': [{'file': 'box_group_3_map.csv',
                          'kind': 'map',
                          'style': {'zorder': 0.0,
                                    'rank': 0,
                                    'cmap': 'cmap2',
                                    'clim': [0.0, 1.5]},
                          'styles': [{'zorder': 0.0,
                                      'rank': 0,
                                      'cmap': 'cmap2',
                                      'clim': [0.0, 1.5]}]}],
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
                          'what': 'cage_lines'},
                         {'kind': 'patch',
                          'shape': 'shape8',
                          'style': {'zorder': 6.0,
                                    'rank': 6,
                                    'clip': False,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'face': '#e6e7e8',
                                    'edge': '#414042',
                                    'pcap': 'butt',
                                    'pjoin': 'miter',
                                    'fill': True,
                                    'filled': True},
                          'what': 'stim_box'}],
               'aspect': 1.0,
               'images': [{'cmap': 'cmap2',
                           'clim': [0.0, 1.5],
                           'extent': [-500.0, 500.0, -500.0, 500.0],
                           'origin': 'lower',
                           'interpolation': 'nearest',
                           'zorder': 0.0,
                           'alpha': None}]},
              {'role': 'plot',
               'name': 'Intruder 3',
               'text_style': [],
               'rect': [1.2974923, 3.2571692, 0.7188, 0.7188],
               'pos': [0.15264615384615385,
                       0.6385482517482517,
                       0.08456470588235296,
                       0.0653454545454546],
               'xlim': [-500.0, 500.0],
               'ylim': [-500.0, 500.0],
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
               'files': [{'file': 'intruder_3_map.csv',
                          'kind': 'map',
                          'style': {'zorder': 0.0,
                                    'rank': 0,
                                    'cmap': 'cmap2',
                                    'clim': [0.0, 1.5]},
                          'styles': [{'zorder': 0.0,
                                      'rank': 0,
                                      'cmap': 'cmap2',
                                      'clim': [0.0, 1.5]}]}],
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
                          'what': 'cage_lines'},
                         {'kind': 'patch',
                          'shape': 'shape6',
                          'style': {'zorder': 6.0,
                                    'rank': 6,
                                    'clip': False,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'face': '#e6e7e8',
                                    'edge': '#414042',
                                    'pcap': 'butt',
                                    'pjoin': 'miter',
                                    'fill': True,
                                    'filled': True},
                          'what': 'stim_box'}],
               'aspect': 1.0,
               'images': [{'cmap': 'cmap2',
                           'clim': [0.0, 1.5],
                           'extent': [-500.0, 500.0, -500.0, 500.0],
                           'origin': 'lower',
                           'interpolation': 'nearest',
                           'zorder': 0.0,
                           'alpha': None}]},
              {'role': 'plot',
               'name': 'Mask 3',
               'text_style': [],
               'rect': [2.0715846, 3.2571692, 0.7188, 0.7188],
               'pos': [0.2437158371040724,
                       0.6385482517482517,
                       0.08456470588235293,
                       0.0653454545454546],
               'xlim': [-500.0, 500.0],
               'ylim': [-500.0, 500.0],
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
               'files': [{'file': 'mask_3_map.csv',
                          'kind': 'map',
                          'style': {'zorder': 0.0,
                                    'rank': 0,
                                    'cmap': 'cmap2',
                                    'clim': [0.0, 1.5]},
                          'styles': [{'zorder': 0.0,
                                      'rank': 0,
                                      'cmap': 'cmap2',
                                      'clim': [0.0, 1.5]}]}],
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
                          'what': 'cage_lines'},
                         {'kind': 'patch',
                          'shape': 'shape10',
                          'style': {'zorder': 6.0,
                                    'rank': 6,
                                    'clip': False,
                                    'lw': 0.5,
                                    'ls': [0.0, [2.4, 1.8]],
                                    'face': '#e6e7e8',
                                    'edge': '#414042',
                                    'pcap': 'butt',
                                    'pjoin': 'miter',
                                    'fill': True,
                                    'filled': True},
                          'what': 'stim_box'}],
               'aspect': 1.0,
               'images': [{'cmap': 'cmap2',
                           'clim': [0.0, 1.5],
                           'extent': [-500.0, 500.0, -500.0, 500.0],
                           'origin': 'lower',
                           'interpolation': 'nearest',
                           'zorder': 0.0,
                           'alpha': None}]},
              {'role': 'colorbar',
               'name': 'Mask 3 colour bar',
               'text_style': [],
               'rect': [2.8641077, 3.2571692, 0.046076923, 0.7188],
               'pos': [0.3369538461538462,
                       0.6385482517482517,
                       0.005420814479637992,
                       0.0653454545454546],
               'xlim': [0.0, 1.0],
               'ylim': [0.0, 1.5],
               'xscale': 'linear',
               'yscale': 'linear',
               'axis_off': False,
               'facecolor': '#ffffff',
               'frame': True,
               'zorder': 0.0,
               'spines': {'left': {'visible': False,
                                   'lw': 0.8,
                                   'colour': '#000000',
                                   'bounds': None,
                                   'position': None},
                          'right': {'visible': True,
                                    'lw': 0.6,
                                    'colour': '#262626',
                                    'bounds': [0.0, 1.5],
                                    'position': ['outward',
                                                 1.843076923076923]},
                          'bottom': {'visible': False,
                                     'lw': 0.8,
                                     'colour': '#000000',
                                     'bounds': None,
                                     'position': None},
                          'top': {'visible': False,
                                  'lw': 0.8,
                                  'colour': '#000000',
                                  'bounds': None,
                                  'position': None},
                          'outline': {'visible': True,
                                      'lw': 0.5,
                                      'colour': '#000000',
                                      'bounds': None,
                                      'position': None}},
               'xticks': {'at': [], 'labels': []},
               'yticks': {'at': [0.0, 0.75, 1.5],
                          'labels': ['0', '0.75', '1.5'],
                          'pad': 1.3823077,
                          'size': 2.4881538,
                          'width': 0.6,
                          'direction': 'out',
                          'visible': [False, True],
                          'label_visible': [False, True],
                          'labelsize': 6.4507692,
                          'colour': '#000000',
                          'labelcolour': '#000000',
                          'rotation': 0.0,
                          'ha': 'left',
                          'va': 'center_baseline'},
               'xlabel': None,
               'ylabel': None,
               'files': [],
               'decor': [],
               'ylabel_side': 'right',
               'aspect': 'auto',
               'bar_texts': [],
               'cbar': {'cmap': 'cmap2',
                        'clim': [0.0, 1.5],
                        'orientation': 'vertical'}}],
 'texts': [{'text': 'Alternating',
            'x': 0.9646,
            'y': 0.4757,
            'size': 7.0,
            'weight': 'normal',
            'ha': 'center',
            'va': 'baseline',
            'rotation': 0.0,
            'colour': '#262626'},
           {'text': 'Early vs late',
            'x': 2.2743,
            'y': 0.4757,
            'size': 7.0,
            'weight': 'normal',
            'ha': 'center',
            'va': 'baseline',
            'rotation': 0.0,
            'colour': '#262626'},
           {'text': 'Cage locations enriched in each cluster-based group',
            'x': 1.7709,
            'y': 1.4127,
            'size': 7.0,
            'weight': 'normal',
            'ha': 'center',
            'va': 'baseline',
            'rotation': 0.0,
            'colour': '#262626'},
           {'text': 'Box',
            'x': 0.8828,
            'y': 1.5523231,
            'size': 6.4507692,
            'weight': 'normal',
            'ha': 'center',
            'va': 'baseline',
            'rotation': 0.0,
            'colour': '#262626'},
           {'text': 'Intruder',
            'x': 1.6568923,
            'y': 1.5523231,
            'size': 6.4507692,
            'weight': 'normal',
            'ha': 'center',
            'va': 'baseline',
            'rotation': 0.0,
            'colour': '#262626'},
           {'text': 'Mask',
            'x': 2.4309846,
            'y': 1.5523231,
            'size': 6.4507692,
            'weight': 'normal',
            'ha': 'center',
            'va': 'baseline',
            'rotation': 0.0,
            'colour': '#262626'},
           {'text': 'Group 1',
            'x': 0.43124615,
            'y': 1.9578,
            'size': 6.4507692,
            'weight': 'normal',
            'ha': 'center',
            'va': 'center',
            'rotation': 90.0,
            'colour': '#3e6556'},
           {'text': 'Group 2',
            'x': 0.43124615,
            'y': 2.7871846,
            'size': 6.4507692,
            'weight': 'normal',
            'ha': 'center',
            'va': 'center',
            'rotation': 90.0,
            'colour': '#5f4a73'},
           {'text': 'Group 3',
            'x': 0.43124615,
            'y': 3.6165692,
            'size': 6.4507692,
            'weight': 'normal',
            'ha': 'center',
            'va': 'center',
            'rotation': 90.0,
            'colour': '#7e683b'}],
 'legends': [{'entries': [{'label': 'Half 1',
                           'style': {'zorder': 2.0,
                                     'lw': 1.5,
                                     'ls': 'None',
                                     'colour': '#1f77b4',
                                     'mfc': '#404040',
                                     'mec': '#404040',
                                     'marker': 'o',
                                     'ms': 5.0,
                                     'mew': 0.8,
                                     'capstyle': 'projecting',
                                     'joinstyle': 'round'},
                           'kind': 'Line2D',
                           'text_colour': '#000000'},
                          {'label': 'Half 2',
                           'style': {'zorder': 2.0,
                                     'lw': 1.5,
                                     'ls': 'None',
                                     'colour': '#1f77b4',
                                     'mfc': 'none',
                                     'mec': '#404040',
                                     'marker': 'o',
                                     'ms': 5.0,
                                     'mew': 0.8,
                                     'capstyle': 'projecting',
                                     'joinstyle': 'round'},
                           'kind': 'Line2D',
                           'text_colour': '#000000'}],
              'loc': 'upper left',
              'ncol': 1,
              'size': 6.0,
              'anchor': [0.3356823529411765,
                         0.9407545454545456,
                         0.0,
                         0.0],
              'frameon': False,
              'borderpad': 0.0,
              'borderaxespad': 0.0,
              'handlelength': 1.0,
              'handletextpad': 0.2,
              'labelspacing': 0.97,
              'columnspacing': 2.0,
              'handleheight': 0.7,
              'markerscale': 1.0,
              'numpoints': 1,
              'scatterpoints': 1}],
 'letter': {'ch': 'a', 'x': 0.3332, 'baseline': 0.4265, 'top': 0.3065}}


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
                         "figures/fig7)")
    a = ap.parse_args(argv)
    for path in render(a.data, a.out_dir):
        print(f"wrote {os.path.normpath(path)}")


if __name__ == "__main__":
    main()
