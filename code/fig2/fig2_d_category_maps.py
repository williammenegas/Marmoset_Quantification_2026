r"""
Figure 2, panel d: where each category happens, and all of them on one map.

Panel id fig2_d_category_maps. Title: "Model output", "Climbing", "Active",
"Alone", "Social active", "Social resting".

Redrawn from the panel's data folder, data/fig2/fig2_d_category_maps/ (DATA
below), with numpy and matplotlib alone: what the panel shows is read from
that folder, and how the page lays it out -- the axes' rectangles in page
inches, limits, ticks, labels, titles, legends, colour maps, drawing
styles, and the decoration the data leave out (cage wireframes, category
outlines, category boundaries) -- is written below as literals, measured
off the published page.

Partly drawn by code. The dashed circle marking the bed, labelled "Bed" on
the first map, is artwork pasted in Illustrator; not drawn by code: the
data hold no bed position.

Usage:

    python fig2_d_category_maps.py [--data DIR] [--out-dir DIR]

writes fig2_d_category_maps.pdf and fig2_d_category_maps.png (400 dpi), the
panel cut from its page, into figures/fig2/ (OUT below); fig2_page.py draws
the whole page and code/render_all.py every figure.
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
DATA = os.path.join(HERE, "..", "..", "data", "fig2", "fig2_d_category_maps")
OUT = os.path.join(HERE, "..", "..", "figures", "fig2")
NAME = "fig2_d_category_maps"
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
SPEC = {'cmaps': {'cmap0': {'colours': ['#440154ff',
                                 '#440256ff',
                                 '#450457ff',
                                 '#450559ff',
                                 '#46075aff',
                                 '#46085cff',
                                 '#460a5dff',
                                 '#460b5eff',
                                 '#470d60ff',
                                 '#470e61ff',
                                 '#471063ff',
                                 '#471164ff',
                                 '#471365ff',
                                 '#481467ff',
                                 '#481668ff',
                                 '#481769ff',
                                 '#48186aff',
                                 '#481a6cff',
                                 '#481b6dff',
                                 '#481c6eff',
                                 '#481d6fff',
                                 '#481f70ff',
                                 '#482071ff',
                                 '#482173ff',
                                 '#482374ff',
                                 '#482475ff',
                                 '#482576ff',
                                 '#482677ff',
                                 '#482878ff',
                                 '#482979ff',
                                 '#472a7aff',
                                 '#472c7aff',
                                 '#472d7bff',
                                 '#472e7cff',
                                 '#472f7dff',
                                 '#46307eff',
                                 '#46327eff',
                                 '#46337fff',
                                 '#463480ff',
                                 '#453581ff',
                                 '#453781ff',
                                 '#453882ff',
                                 '#443983ff',
                                 '#443a83ff',
                                 '#443b84ff',
                                 '#433d84ff',
                                 '#433e85ff',
                                 '#423f85ff',
                                 '#424086ff',
                                 '#424186ff',
                                 '#414287ff',
                                 '#414487ff',
                                 '#404588ff',
                                 '#404688ff',
                                 '#3f4788ff',
                                 '#3f4889ff',
                                 '#3e4989ff',
                                 '#3e4a89ff',
                                 '#3e4c8aff',
                                 '#3d4d8aff',
                                 '#3d4e8aff',
                                 '#3c4f8aff',
                                 '#3c508bff',
                                 '#3b518bff',
                                 '#3b528bff',
                                 '#3a538bff',
                                 '#3a548cff',
                                 '#39558cff',
                                 '#39568cff',
                                 '#38588cff',
                                 '#38598cff',
                                 '#375a8cff',
                                 '#375b8dff',
                                 '#365c8dff',
                                 '#365d8dff',
                                 '#355e8dff',
                                 '#355f8dff',
                                 '#34608dff',
                                 '#34618dff',
                                 '#33628dff',
                                 '#33638dff',
                                 '#32648eff',
                                 '#32658eff',
                                 '#31668eff',
                                 '#31678eff',
                                 '#31688eff',
                                 '#30698eff',
                                 '#306a8eff',
                                 '#2f6b8eff',
                                 '#2f6c8eff',
                                 '#2e6d8eff',
                                 '#2e6e8eff',
                                 '#2e6f8eff',
                                 '#2d708eff',
                                 '#2d718eff',
                                 '#2c718eff',
                                 '#2c728eff',
                                 '#2c738eff',
                                 '#2b748eff',
                                 '#2b758eff',
                                 '#2a768eff',
                                 '#2a778eff',
                                 '#2a788eff',
                                 '#29798eff',
                                 '#297a8eff',
                                 '#297b8eff',
                                 '#287c8eff',
                                 '#287d8eff',
                                 '#277e8eff',
                                 '#277f8eff',
                                 '#27808eff',
                                 '#26818eff',
                                 '#26828eff',
                                 '#26828eff',
                                 '#25838eff',
                                 '#25848eff',
                                 '#25858eff',
                                 '#24868eff',
                                 '#24878eff',
                                 '#23888eff',
                                 '#23898eff',
                                 '#238a8dff',
                                 '#228b8dff',
                                 '#228c8dff',
                                 '#228d8dff',
                                 '#218e8dff',
                                 '#218f8dff',
                                 '#21908dff',
                                 '#21918cff',
                                 '#20928cff',
                                 '#20928cff',
                                 '#20938cff',
                                 '#1f948cff',
                                 '#1f958bff',
                                 '#1f968bff',
                                 '#1f978bff',
                                 '#1f988bff',
                                 '#1f998aff',
                                 '#1f9a8aff',
                                 '#1e9b8aff',
                                 '#1e9c89ff',
                                 '#1e9d89ff',
                                 '#1f9e89ff',
                                 '#1f9f88ff',
                                 '#1fa088ff',
                                 '#1fa188ff',
                                 '#1fa187ff',
                                 '#1fa287ff',
                                 '#20a386ff',
                                 '#20a486ff',
                                 '#21a585ff',
                                 '#21a685ff',
                                 '#22a785ff',
                                 '#22a884ff',
                                 '#23a983ff',
                                 '#24aa83ff',
                                 '#25ab82ff',
                                 '#25ac82ff',
                                 '#26ad81ff',
                                 '#27ad81ff',
                                 '#28ae80ff',
                                 '#29af7fff',
                                 '#2ab07fff',
                                 '#2cb17eff',
                                 '#2db27dff',
                                 '#2eb37cff',
                                 '#2fb47cff',
                                 '#31b57bff',
                                 '#32b67aff',
                                 '#34b679ff',
                                 '#35b779ff',
                                 '#37b878ff',
                                 '#38b977ff',
                                 '#3aba76ff',
                                 '#3bbb75ff',
                                 '#3dbc74ff',
                                 '#3fbc73ff',
                                 '#40bd72ff',
                                 '#42be71ff',
                                 '#44bf70ff',
                                 '#46c06fff',
                                 '#48c16eff',
                                 '#4ac16dff',
                                 '#4cc26cff',
                                 '#4ec36bff',
                                 '#50c46aff',
                                 '#52c569ff',
                                 '#54c568ff',
                                 '#56c667ff',
                                 '#58c765ff',
                                 '#5ac864ff',
                                 '#5cc863ff',
                                 '#5ec962ff',
                                 '#60ca60ff',
                                 '#63cb5fff',
                                 '#65cb5eff',
                                 '#67cc5cff',
                                 '#69cd5bff',
                                 '#6ccd5aff',
                                 '#6ece58ff',
                                 '#70cf57ff',
                                 '#73d056ff',
                                 '#75d054ff',
                                 '#77d153ff',
                                 '#7ad151ff',
                                 '#7cd250ff',
                                 '#7fd34eff',
                                 '#81d34dff',
                                 '#84d44bff',
                                 '#86d549ff',
                                 '#89d548ff',
                                 '#8bd646ff',
                                 '#8ed645ff',
                                 '#90d743ff',
                                 '#93d741ff',
                                 '#95d840ff',
                                 '#98d83eff',
                                 '#9bd93cff',
                                 '#9dd93bff',
                                 '#a0da39ff',
                                 '#a2da37ff',
                                 '#a5db36ff',
                                 '#a8db34ff',
                                 '#aadc32ff',
                                 '#addc30ff',
                                 '#b0dd2fff',
                                 '#b2dd2dff',
                                 '#b5de2bff',
                                 '#b8de29ff',
                                 '#bade28ff',
                                 '#bddf26ff',
                                 '#c0df25ff',
                                 '#c2df23ff',
                                 '#c5e021ff',
                                 '#c8e020ff',
                                 '#cae11fff',
                                 '#cde11dff',
                                 '#d0e11cff',
                                 '#d2e21bff',
                                 '#d5e21aff',
                                 '#d8e219ff',
                                 '#dae319ff',
                                 '#dde318ff',
                                 '#dfe318ff',
                                 '#e2e418ff',
                                 '#e5e419ff',
                                 '#e7e419ff',
                                 '#eae51aff',
                                 '#ece51bff',
                                 '#efe51cff',
                                 '#f1e51dff',
                                 '#f4e61eff',
                                 '#f6e620ff',
                                 '#f8e621ff',
                                 '#fbe723ff',
                                 '#fde725ff'],
                     'bad': '#00000000'},
           'cmap1': {'colours': ['#ffffffff',
                                 '#fefeffff',
                                 '#fefeffff',
                                 '#fdfdffff',
                                 '#fdfdfeff',
                                 '#fcfcfeff',
                                 '#fbfbfeff',
                                 '#fbfbfeff',
                                 '#fafafeff',
                                 '#faf9feff',
                                 '#f9f9fdff',
                                 '#f8f8fdff',
                                 '#f8f8fdff',
                                 '#f7f7fdff',
                                 '#f7f6fdff',
                                 '#f6f6fdff',
                                 '#f5f5fcff',
                                 '#f5f5fcff',
                                 '#f4f4fcff',
                                 '#f4f3fcff',
                                 '#f3f3fcff',
                                 '#f2f2fcff',
                                 '#f2f1fcff',
                                 '#f1f1fbff',
                                 '#f1f0fbff',
                                 '#f0f0fbff',
                                 '#efeffbff',
                                 '#efeefbff',
                                 '#eeeefbff',
                                 '#eeedfaff',
                                 '#ededfaff',
                                 '#ececfaff',
                                 '#ecebfaff',
                                 '#ebebfaff',
                                 '#ebeafaff',
                                 '#eae9faff',
                                 '#e9e9f9ff',
                                 '#e9e8f9ff',
                                 '#e8e8f9ff',
                                 '#e8e7f9ff',
                                 '#e7e6f9ff',
                                 '#e6e6f9ff',
                                 '#e6e5f8ff',
                                 '#e5e5f8ff',
                                 '#e5e4f8ff',
                                 '#e4e3f8ff',
                                 '#e3e3f8ff',
                                 '#e3e2f8ff',
                                 '#e2e1f7ff',
                                 '#e2e1f7ff',
                                 '#e1e0f7ff',
                                 '#e0e0f7ff',
                                 '#e0dff7ff',
                                 '#dfdef7ff',
                                 '#dfdef7ff',
                                 '#deddf6ff',
                                 '#ddddf6ff',
                                 '#dddcf6ff',
                                 '#dcdbf6ff',
                                 '#dcdbf6ff',
                                 '#dbdaf6ff',
                                 '#dad9f5ff',
                                 '#dad9f5ff',
                                 '#d9d8f5ff',
                                 '#d9d8f5ff',
                                 '#d8d7f5ff',
                                 '#d7d6f5ff',
                                 '#d7d6f4ff',
                                 '#d6d5f4ff',
                                 '#d6d5f4ff',
                                 '#d5d4f4ff',
                                 '#d4d3f4ff',
                                 '#d4d3f4ff',
                                 '#d3d2f4ff',
                                 '#d3d1f3ff',
                                 '#d2d1f3ff',
                                 '#d1d0f3ff',
                                 '#d1d0f3ff',
                                 '#d0cff3ff',
                                 '#d0cef3ff',
                                 '#cfcef2ff',
                                 '#cecdf2ff',
                                 '#cecdf2ff',
                                 '#cdccf2ff',
                                 '#cdcbf2ff',
                                 '#cccbf2ff',
                                 '#cbcaf2ff',
                                 '#cbc9f1ff',
                                 '#cac9f1ff',
                                 '#cac8f1ff',
                                 '#c9c8f1ff',
                                 '#c8c7f1ff',
                                 '#c8c6f1ff',
                                 '#c7c6f0ff',
                                 '#c7c5f0ff',
                                 '#c6c5f0ff',
                                 '#c5c4f0ff',
                                 '#c5c3f0ff',
                                 '#c4c3f0ff',
                                 '#c4c2efff',
                                 '#c3c1efff',
                                 '#c2c1efff',
                                 '#c2c0efff',
                                 '#c1c0efff',
                                 '#c1bfefff',
                                 '#c0beefff',
                                 '#bfbeeeff',
                                 '#bfbdeeff',
                                 '#bebdeeff',
                                 '#bebceeff',
                                 '#bdbbeeff',
                                 '#bcbbeeff',
                                 '#bcbaedff',
                                 '#bbb9edff',
                                 '#bbb9edff',
                                 '#bab8edff',
                                 '#b9b8edff',
                                 '#b9b7edff',
                                 '#b8b6ecff',
                                 '#b8b6ecff',
                                 '#b7b5ecff',
                                 '#b6b5ecff',
                                 '#b6b4ecff',
                                 '#b5b3ecff',
                                 '#b5b3ecff',
                                 '#b4b2ebff',
                                 '#b3b1ebff',
                                 '#b3b1ebff',
                                 '#b2b0ebff',
                                 '#b2b0ebff',
                                 '#b1afebff',
                                 '#b0aeeaff',
                                 '#b0aeeaff',
                                 '#afadeaff',
                                 '#afaceaff',
                                 '#aeaceaff',
                                 '#adabeaff',
                                 '#adabeaff',
                                 '#acaae9ff',
                                 '#aca9e9ff',
                                 '#aba9e9ff',
                                 '#aaa8e9ff',
                                 '#aaa8e9ff',
                                 '#a9a7e9ff',
                                 '#a9a6e8ff',
                                 '#a8a6e8ff',
                                 '#a7a5e8ff',
                                 '#a7a4e8ff',
                                 '#a6a4e8ff',
                                 '#a6a3e8ff',
                                 '#a5a3e7ff',
                                 '#a4a2e7ff',
                                 '#a4a1e7ff',
                                 '#a3a1e7ff',
                                 '#a3a0e7ff',
                                 '#a2a0e7ff',
                                 '#a19fe7ff',
                                 '#a19ee6ff',
                                 '#a09ee6ff',
                                 '#a09de6ff',
                                 '#9f9ce6ff',
                                 '#9e9ce6ff',
                                 '#9e9be6ff',
                                 '#9d9be5ff',
                                 '#9d9ae5ff',
                                 '#9c99e5ff',
                                 '#9b99e5ff',
                                 '#9b98e5ff',
                                 '#9a98e5ff',
                                 '#9a97e4ff',
                                 '#9996e4ff',
                                 '#9896e4ff',
                                 '#9895e4ff',
                                 '#9794e4ff',
                                 '#9794e4ff',
                                 '#9693e4ff',
                                 '#9593e3ff',
                                 '#9592e3ff',
                                 '#9491e3ff',
                                 '#9491e3ff',
                                 '#9390e3ff',
                                 '#9290e3ff',
                                 '#928fe2ff',
                                 '#918ee2ff',
                                 '#918ee2ff',
                                 '#908de2ff',
                                 '#8f8ce2ff',
                                 '#8f8ce2ff',
                                 '#8e8be2ff',
                                 '#8e8be1ff',
                                 '#8d8ae1ff',
                                 '#8c89e1ff',
                                 '#8c89e1ff',
                                 '#8b88e1ff',
                                 '#8b88e1ff',
                                 '#8a87e0ff',
                                 '#8986e0ff',
                                 '#8986e0ff',
                                 '#8885e0ff',
                                 '#8884e0ff',
                                 '#8784e0ff',
                                 '#8683dfff',
                                 '#8683dfff',
                                 '#8582dfff',
                                 '#8581dfff',
                                 '#8481dfff',
                                 '#8380dfff',
                                 '#8380dfff',
                                 '#827fdeff',
                                 '#827edeff',
                                 '#817edeff',
                                 '#807ddeff',
                                 '#807cdeff',
                                 '#7f7cdeff',
                                 '#7f7bddff',
                                 '#7e7bddff',
                                 '#7d7addff',
                                 '#7d79ddff',
                                 '#7c79ddff',
                                 '#7c78ddff',
                                 '#7b78dcff',
                                 '#7a77dcff',
                                 '#7a76dcff',
                                 '#7976dcff',
                                 '#7975dcff',
                                 '#7874dcff',
                                 '#7774dcff',
                                 '#7773dbff',
                                 '#7673dbff',
                                 '#7672dbff',
                                 '#7571dbff',
                                 '#7471dbff',
                                 '#7470dbff',
                                 '#7370daff',
                                 '#736fdaff',
                                 '#726edaff',
                                 '#716edaff',
                                 '#716ddaff',
                                 '#706cdaff',
                                 '#706cdaff',
                                 '#6f6bd9ff',
                                 '#6e6bd9ff',
                                 '#6e6ad9ff',
                                 '#6d69d9ff',
                                 '#6d69d9ff',
                                 '#6c68d9ff',
                                 '#6b68d8ff',
                                 '#6b67d8ff',
                                 '#6a66d8ff',
                                 '#6a66d8ff',
                                 '#6965d8ff',
                                 '#6864d8ff',
                                 '#6864d7ff',
                                 '#6763d7ff',
                                 '#6763d7ff',
                                 '#6662d7ff'],
                     'bad': '#00000000'},
           'cmap2': {'colours': ['#ffffffff',
                                 '#fffeffff',
                                 '#fefefeff',
                                 '#fefdfeff',
                                 '#fefcfeff',
                                 '#fdfcfeff',
                                 '#fdfbfdff',
                                 '#fdfbfdff',
                                 '#fcfafdff',
                                 '#fcf9fdff',
                                 '#fcf9fcff',
                                 '#fbf8fcff',
                                 '#fbf7fcff',
                                 '#fbf7fbff',
                                 '#faf6fbff',
                                 '#faf6fbff',
                                 '#faf5fbff',
                                 '#f9f4faff',
                                 '#f9f4faff',
                                 '#f9f3faff',
                                 '#f8f2faff',
                                 '#f8f2f9ff',
                                 '#f7f1f9ff',
                                 '#f7f1f9ff',
                                 '#f7f0f9ff',
                                 '#f6eff8ff',
                                 '#f6eff8ff',
                                 '#f6eef8ff',
                                 '#f5edf7ff',
                                 '#f5edf7ff',
                                 '#f5ecf7ff',
                                 '#f4ecf7ff',
                                 '#f4ebf6ff',
                                 '#f4eaf6ff',
                                 '#f3eaf6ff',
                                 '#f3e9f6ff',
                                 '#f3e8f5ff',
                                 '#f2e8f5ff',
                                 '#f2e7f5ff',
                                 '#f2e7f4ff',
                                 '#f1e6f4ff',
                                 '#f1e5f4ff',
                                 '#f1e5f4ff',
                                 '#f0e4f3ff',
                                 '#f0e3f3ff',
                                 '#f0e3f3ff',
                                 '#efe2f3ff',
                                 '#efe2f2ff',
                                 '#efe1f2ff',
                                 '#eee0f2ff',
                                 '#eee0f1ff',
                                 '#eedff1ff',
                                 '#eddef1ff',
                                 '#eddef1ff',
                                 '#edddf0ff',
                                 '#ecdcf0ff',
                                 '#ecdcf0ff',
                                 '#ecdbf0ff',
                                 '#ebdbefff',
                                 '#ebdaefff',
                                 '#ebd9efff',
                                 '#ead9eeff',
                                 '#ead8eeff',
                                 '#ead7eeff',
                                 '#e9d7eeff',
                                 '#e9d6edff',
                                 '#e8d6edff',
                                 '#e8d5edff',
                                 '#e8d4edff',
                                 '#e7d4ecff',
                                 '#e7d3ecff',
                                 '#e7d2ecff',
                                 '#e6d2ecff',
                                 '#e6d1ebff',
                                 '#e6d1ebff',
                                 '#e5d0ebff',
                                 '#e5cfeaff',
                                 '#e5cfeaff',
                                 '#e4ceeaff',
                                 '#e4cdeaff',
                                 '#e4cde9ff',
                                 '#e3cce9ff',
                                 '#e3cce9ff',
                                 '#e3cbe9ff',
                                 '#e2cae8ff',
                                 '#e2cae8ff',
                                 '#e2c9e8ff',
                                 '#e1c8e7ff',
                                 '#e1c8e7ff',
                                 '#e1c7e7ff',
                                 '#e0c7e7ff',
                                 '#e0c6e6ff',
                                 '#e0c5e6ff',
                                 '#dfc5e6ff',
                                 '#dfc4e6ff',
                                 '#dfc3e5ff',
                                 '#dec3e5ff',
                                 '#dec2e5ff',
                                 '#dec2e4ff',
                                 '#ddc1e4ff',
                                 '#ddc0e4ff',
                                 '#ddc0e4ff',
                                 '#dcbfe3ff',
                                 '#dcbee3ff',
                                 '#dcbee3ff',
                                 '#dbbde3ff',
                                 '#dbbce2ff',
                                 '#dabce2ff',
                                 '#dabbe2ff',
                                 '#dabbe2ff',
                                 '#d9bae1ff',
                                 '#d9b9e1ff',
                                 '#d9b9e1ff',
                                 '#d8b8e0ff',
                                 '#d8b7e0ff',
                                 '#d8b7e0ff',
                                 '#d7b6e0ff',
                                 '#d7b6dfff',
                                 '#d7b5dfff',
                                 '#d6b4dfff',
                                 '#d6b4dfff',
                                 '#d6b3deff',
                                 '#d5b2deff',
                                 '#d5b2deff',
                                 '#d5b1ddff',
                                 '#d4b1ddff',
                                 '#d4b0ddff',
                                 '#d4afddff',
                                 '#d3afdcff',
                                 '#d3aedcff',
                                 '#d3addcff',
                                 '#d2addcff',
                                 '#d2acdbff',
                                 '#d2acdbff',
                                 '#d1abdbff',
                                 '#d1aadaff',
                                 '#d1aadaff',
                                 '#d0a9daff',
                                 '#d0a8daff',
                                 '#d0a8d9ff',
                                 '#cfa7d9ff',
                                 '#cfa7d9ff',
                                 '#cfa6d9ff',
                                 '#cea5d8ff',
                                 '#cea5d8ff',
                                 '#cea4d8ff',
                                 '#cda3d7ff',
                                 '#cda3d7ff',
                                 '#cda2d7ff',
                                 '#cca2d7ff',
                                 '#cca1d6ff',
                                 '#cba0d6ff',
                                 '#cba0d6ff',
                                 '#cb9fd6ff',
                                 '#ca9ed5ff',
                                 '#ca9ed5ff',
                                 '#ca9dd5ff',
                                 '#c99cd5ff',
                                 '#c99cd4ff',
                                 '#c99bd4ff',
                                 '#c89bd4ff',
                                 '#c89ad3ff',
                                 '#c899d3ff',
                                 '#c799d3ff',
                                 '#c798d3ff',
                                 '#c797d2ff',
                                 '#c697d2ff',
                                 '#c696d2ff',
                                 '#c696d2ff',
                                 '#c595d1ff',
                                 '#c594d1ff',
                                 '#c594d1ff',
                                 '#c493d0ff',
                                 '#c492d0ff',
                                 '#c492d0ff',
                                 '#c391d0ff',
                                 '#c391cfff',
                                 '#c390cfff',
                                 '#c28fcfff',
                                 '#c28fcfff',
                                 '#c28eceff',
                                 '#c18dceff',
                                 '#c18dceff',
                                 '#c18ccdff',
                                 '#c08ccdff',
                                 '#c08bcdff',
                                 '#c08acdff',
                                 '#bf8accff',
                                 '#bf89ccff',
                                 '#bf88ccff',
                                 '#be88ccff',
                                 '#be87cbff',
                                 '#bd87cbff',
                                 '#bd86cbff',
                                 '#bd85cbff',
                                 '#bc85caff',
                                 '#bc84caff',
                                 '#bc83caff',
                                 '#bb83c9ff',
                                 '#bb82c9ff',
                                 '#bb82c9ff',
                                 '#ba81c9ff',
                                 '#ba80c8ff',
                                 '#ba80c8ff',
                                 '#b97fc8ff',
                                 '#b97ec8ff',
                                 '#b97ec7ff',
                                 '#b87dc7ff',
                                 '#b87cc7ff',
                                 '#b87cc6ff',
                                 '#b77bc6ff',
                                 '#b77bc6ff',
                                 '#b77ac6ff',
                                 '#b679c5ff',
                                 '#b679c5ff',
                                 '#b678c5ff',
                                 '#b577c5ff',
                                 '#b577c4ff',
                                 '#b576c4ff',
                                 '#b476c4ff',
                                 '#b475c3ff',
                                 '#b474c3ff',
                                 '#b374c3ff',
                                 '#b373c3ff',
                                 '#b372c2ff',
                                 '#b272c2ff',
                                 '#b271c2ff',
                                 '#b271c2ff',
                                 '#b170c1ff',
                                 '#b16fc1ff',
                                 '#b16fc1ff',
                                 '#b06ec0ff',
                                 '#b06dc0ff',
                                 '#b06dc0ff',
                                 '#af6cc0ff',
                                 '#af6cbfff',
                                 '#ae6bbfff',
                                 '#ae6abfff',
                                 '#ae6abfff',
                                 '#ad69beff',
                                 '#ad68beff',
                                 '#ad68beff',
                                 '#ac67beff',
                                 '#ac67bdff',
                                 '#ac66bdff',
                                 '#ab65bdff',
                                 '#ab65bcff',
                                 '#ab64bcff',
                                 '#aa63bcff',
                                 '#aa63bcff',
                                 '#aa62bbff',
                                 '#a961bbff',
                                 '#a961bbff',
                                 '#a960bbff',
                                 '#a860baff',
                                 '#a85fbaff'],
                     'bad': '#00000000'},
           'cmap3': {'colours': ['#ffffffff',
                                 '#fffeffff',
                                 '#fffefeff',
                                 '#fffdfeff',
                                 '#fffcfdff',
                                 '#fffcfdff',
                                 '#fffbfdff',
                                 '#fffbfcff',
                                 '#fffafcff',
                                 '#fef9fbff',
                                 '#fef9fbff',
                                 '#fef8fbff',
                                 '#fef7faff',
                                 '#fef7faff',
                                 '#fef6faff',
                                 '#fef5f9ff',
                                 '#fef5f9ff',
                                 '#fef4f8ff',
                                 '#fef3f8ff',
                                 '#fef3f8ff',
                                 '#fef2f7ff',
                                 '#fef2f7ff',
                                 '#fef1f6ff',
                                 '#fef0f6ff',
                                 '#fef0f6ff',
                                 '#feeff5ff',
                                 '#fdeef5ff',
                                 '#fdeef4ff',
                                 '#fdedf4ff',
                                 '#fdecf4ff',
                                 '#fdecf3ff',
                                 '#fdebf3ff',
                                 '#fdebf2ff',
                                 '#fdeaf2ff',
                                 '#fde9f2ff',
                                 '#fde9f1ff',
                                 '#fde8f1ff',
                                 '#fde7f0ff',
                                 '#fde7f0ff',
                                 '#fde6f0ff',
                                 '#fde5efff',
                                 '#fde5efff',
                                 '#fde4efff',
                                 '#fce4eeff',
                                 '#fce3eeff',
                                 '#fce2edff',
                                 '#fce2edff',
                                 '#fce1edff',
                                 '#fce0ecff',
                                 '#fce0ecff',
                                 '#fcdfebff',
                                 '#fcdeebff',
                                 '#fcdeebff',
                                 '#fcddeaff',
                                 '#fcdceaff',
                                 '#fcdce9ff',
                                 '#fcdbe9ff',
                                 '#fcdbe9ff',
                                 '#fcdae8ff',
                                 '#fcd9e8ff',
                                 '#fbd9e7ff',
                                 '#fbd8e7ff',
                                 '#fbd7e7ff',
                                 '#fbd7e6ff',
                                 '#fbd6e6ff',
                                 '#fbd5e6ff',
                                 '#fbd5e5ff',
                                 '#fbd4e5ff',
                                 '#fbd4e4ff',
                                 '#fbd3e4ff',
                                 '#fbd2e4ff',
                                 '#fbd2e3ff',
                                 '#fbd1e3ff',
                                 '#fbd0e2ff',
                                 '#fbd0e2ff',
                                 '#fbcfe2ff',
                                 '#fbcee1ff',
                                 '#facee1ff',
                                 '#facde0ff',
                                 '#facde0ff',
                                 '#facce0ff',
                                 '#facbdfff',
                                 '#facbdfff',
                                 '#facadeff',
                                 '#fac9deff',
                                 '#fac9deff',
                                 '#fac8ddff',
                                 '#fac7ddff',
                                 '#fac7dcff',
                                 '#fac6dcff',
                                 '#fac5dcff',
                                 '#fac5dbff',
                                 '#fac4dbff',
                                 '#fac4dbff',
                                 '#f9c3daff',
                                 '#f9c2daff',
                                 '#f9c2d9ff',
                                 '#f9c1d9ff',
                                 '#f9c0d9ff',
                                 '#f9c0d8ff',
                                 '#f9bfd8ff',
                                 '#f9bed7ff',
                                 '#f9bed7ff',
                                 '#f9bdd7ff',
                                 '#f9bdd6ff',
                                 '#f9bcd6ff',
                                 '#f9bbd5ff',
                                 '#f9bbd5ff',
                                 '#f9bad5ff',
                                 '#f9b9d4ff',
                                 '#f9b9d4ff',
                                 '#f8b8d3ff',
                                 '#f8b7d3ff',
                                 '#f8b7d3ff',
                                 '#f8b6d2ff',
                                 '#f8b5d2ff',
                                 '#f8b5d2ff',
                                 '#f8b4d1ff',
                                 '#f8b4d1ff',
                                 '#f8b3d0ff',
                                 '#f8b2d0ff',
                                 '#f8b2d0ff',
                                 '#f8b1cfff',
                                 '#f8b0cfff',
                                 '#f8b0ceff',
                                 '#f8afceff',
                                 '#f8aeceff',
                                 '#f8aecdff',
                                 '#f7adcdff',
                                 '#f7adccff',
                                 '#f7acccff',
                                 '#f7abccff',
                                 '#f7abcbff',
                                 '#f7aacbff',
                                 '#f7a9caff',
                                 '#f7a9caff',
                                 '#f7a8caff',
                                 '#f7a7c9ff',
                                 '#f7a7c9ff',
                                 '#f7a6c8ff',
                                 '#f7a6c8ff',
                                 '#f7a5c8ff',
                                 '#f7a4c7ff',
                                 '#f7a4c7ff',
                                 '#f7a3c7ff',
                                 '#f6a2c6ff',
                                 '#f6a2c6ff',
                                 '#f6a1c5ff',
                                 '#f6a0c5ff',
                                 '#f6a0c5ff',
                                 '#f69fc4ff',
                                 '#f69ec4ff',
                                 '#f69ec3ff',
                                 '#f69dc3ff',
                                 '#f69dc3ff',
                                 '#f69cc2ff',
                                 '#f69bc2ff',
                                 '#f69bc1ff',
                                 '#f69ac1ff',
                                 '#f699c1ff',
                                 '#f699c0ff',
                                 '#f698c0ff',
                                 '#f597bfff',
                                 '#f597bfff',
                                 '#f596bfff',
                                 '#f596beff',
                                 '#f595beff',
                                 '#f594beff',
                                 '#f594bdff',
                                 '#f593bdff',
                                 '#f592bcff',
                                 '#f592bcff',
                                 '#f591bcff',
                                 '#f590bbff',
                                 '#f590bbff',
                                 '#f58fbaff',
                                 '#f58fbaff',
                                 '#f58ebaff',
                                 '#f58db9ff',
                                 '#f48db9ff',
                                 '#f48cb8ff',
                                 '#f48bb8ff',
                                 '#f48bb8ff',
                                 '#f48ab7ff',
                                 '#f489b7ff',
                                 '#f489b6ff',
                                 '#f488b6ff',
                                 '#f487b6ff',
                                 '#f487b5ff',
                                 '#f486b5ff',
                                 '#f486b4ff',
                                 '#f485b4ff',
                                 '#f484b4ff',
                                 '#f484b3ff',
                                 '#f483b3ff',
                                 '#f482b3ff',
                                 '#f382b2ff',
                                 '#f381b2ff',
                                 '#f380b1ff',
                                 '#f380b1ff',
                                 '#f37fb1ff',
                                 '#f37fb0ff',
                                 '#f37eb0ff',
                                 '#f37dafff',
                                 '#f37dafff',
                                 '#f37cafff',
                                 '#f37baeff',
                                 '#f37baeff',
                                 '#f37aadff',
                                 '#f379adff',
                                 '#f379adff',
                                 '#f378acff',
                                 '#f377acff',
                                 '#f277abff',
                                 '#f276abff',
                                 '#f276abff',
                                 '#f275aaff',
                                 '#f274aaff',
                                 '#f274aaff',
                                 '#f273a9ff',
                                 '#f272a9ff',
                                 '#f272a8ff',
                                 '#f271a8ff',
                                 '#f270a8ff',
                                 '#f270a7ff',
                                 '#f26fa7ff',
                                 '#f26fa6ff',
                                 '#f26ea6ff',
                                 '#f26da6ff',
                                 '#f26da5ff',
                                 '#f16ca5ff',
                                 '#f16ba4ff',
                                 '#f16ba4ff',
                                 '#f16aa4ff',
                                 '#f169a3ff',
                                 '#f169a3ff',
                                 '#f168a2ff',
                                 '#f168a2ff',
                                 '#f167a2ff',
                                 '#f166a1ff',
                                 '#f166a1ff',
                                 '#f165a0ff',
                                 '#f164a0ff',
                                 '#f164a0ff',
                                 '#f1639fff',
                                 '#f1629fff',
                                 '#f1629fff',
                                 '#f0619eff',
                                 '#f0609eff',
                                 '#f0609dff',
                                 '#f05f9dff',
                                 '#f05f9dff',
                                 '#f05e9cff',
                                 '#f05d9cff',
                                 '#f05d9bff',
                                 '#f05c9bff'],
                     'bad': '#00000000'},
           'cmap4': {'colours': ['#ffffffff',
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
                                 '#fffaf9ff',
                                 '#fff9f8ff',
                                 '#fff9f8ff',
                                 '#fff8f7ff',
                                 '#fff8f7ff',
                                 '#fff7f6ff',
                                 '#fff7f6ff',
                                 '#fff7f5ff',
                                 '#fff6f5ff',
                                 '#fff6f4ff',
                                 '#fff5f4ff',
                                 '#fff5f3ff',
                                 '#fff4f3ff',
                                 '#fff4f2ff',
                                 '#fff3f2ff',
                                 '#fff3f1ff',
                                 '#fff2f1ff',
                                 '#fff2f0ff',
                                 '#fff2efff',
                                 '#fff1efff',
                                 '#fef1eeff',
                                 '#fef0eeff',
                                 '#fef0edff',
                                 '#feefedff',
                                 '#feefecff',
                                 '#feeeecff',
                                 '#feeeebff',
                                 '#feeeebff',
                                 '#feedeaff',
                                 '#feedeaff',
                                 '#feece9ff',
                                 '#feece9ff',
                                 '#feebe8ff',
                                 '#feebe8ff',
                                 '#feeae7ff',
                                 '#feeae7ff',
                                 '#feeae6ff',
                                 '#fee9e6ff',
                                 '#fee9e5ff',
                                 '#fee8e5ff',
                                 '#fee8e4ff',
                                 '#fee7e4ff',
                                 '#fee7e3ff',
                                 '#fee6e3ff',
                                 '#fee6e2ff',
                                 '#fee6e1ff',
                                 '#fee5e1ff',
                                 '#fee5e0ff',
                                 '#fee4e0ff',
                                 '#fee4dfff',
                                 '#fee3dfff',
                                 '#fee3deff',
                                 '#fee2deff',
                                 '#fee2ddff',
                                 '#fee1ddff',
                                 '#fee1dcff',
                                 '#fee1dcff',
                                 '#fee0dbff',
                                 '#fee0dbff',
                                 '#fedfdaff',
                                 '#fedfdaff',
                                 '#feded9ff',
                                 '#feded9ff',
                                 '#feddd8ff',
                                 '#feddd8ff',
                                 '#feddd7ff',
                                 '#fedcd7ff',
                                 '#fedcd6ff',
                                 '#fedbd6ff',
                                 '#fedbd5ff',
                                 '#fedad5ff',
                                 '#fedad4ff',
                                 '#fed9d4ff',
                                 '#fed9d3ff',
                                 '#fed9d2ff',
                                 '#fed8d2ff',
                                 '#fed8d1ff',
                                 '#fed7d1ff',
                                 '#fed7d0ff',
                                 '#fed6d0ff',
                                 '#fed6cfff',
                                 '#fed5cfff',
                                 '#fed5ceff',
                                 '#fed5ceff',
                                 '#fdd4cdff',
                                 '#fdd4cdff',
                                 '#fdd3ccff',
                                 '#fdd3ccff',
                                 '#fdd2cbff',
                                 '#fdd2cbff',
                                 '#fdd1caff',
                                 '#fdd1caff',
                                 '#fdd1c9ff',
                                 '#fdd0c9ff',
                                 '#fdd0c8ff',
                                 '#fdcfc8ff',
                                 '#fdcfc7ff',
                                 '#fdcec7ff',
                                 '#fdcec6ff',
                                 '#fdcdc6ff',
                                 '#fdcdc5ff',
                                 '#fdccc5ff',
                                 '#fdccc4ff',
                                 '#fdccc3ff',
                                 '#fdcbc3ff',
                                 '#fdcbc2ff',
                                 '#fdcac2ff',
                                 '#fdcac1ff',
                                 '#fdc9c1ff',
                                 '#fdc9c0ff',
                                 '#fdc8c0ff',
                                 '#fdc8bfff',
                                 '#fdc8bfff',
                                 '#fdc7beff',
                                 '#fdc7beff',
                                 '#fdc6bdff',
                                 '#fdc6bdff',
                                 '#fdc5bcff',
                                 '#fdc5bcff',
                                 '#fdc4bbff',
                                 '#fdc4bbff',
                                 '#fdc4baff',
                                 '#fdc3baff',
                                 '#fdc3b9ff',
                                 '#fdc2b9ff',
                                 '#fdc2b8ff',
                                 '#fdc1b8ff',
                                 '#fdc1b7ff',
                                 '#fdc0b7ff',
                                 '#fdc0b6ff',
                                 '#fdc0b6ff',
                                 '#fdbfb5ff',
                                 '#fdbfb4ff',
                                 '#fdbeb4ff',
                                 '#fdbeb3ff',
                                 '#fdbdb3ff',
                                 '#fdbdb2ff',
                                 '#fdbcb2ff',
                                 '#fdbcb1ff',
                                 '#fdbbb1ff',
                                 '#fdbbb0ff',
                                 '#fdbbb0ff',
                                 '#fdbaafff',
                                 '#fdbaafff',
                                 '#fdb9aeff',
                                 '#fdb9aeff',
                                 '#fdb8adff',
                                 '#fdb8adff',
                                 '#fcb7acff',
                                 '#fcb7acff',
                                 '#fcb7abff',
                                 '#fcb6abff',
                                 '#fcb6aaff',
                                 '#fcb5aaff',
                                 '#fcb5a9ff',
                                 '#fcb4a9ff',
                                 '#fcb4a8ff',
                                 '#fcb3a8ff',
                                 '#fcb3a7ff',
                                 '#fcb3a6ff',
                                 '#fcb2a6ff',
                                 '#fcb2a5ff',
                                 '#fcb1a5ff',
                                 '#fcb1a4ff',
                                 '#fcb0a4ff',
                                 '#fcb0a3ff',
                                 '#fcafa3ff',
                                 '#fcafa2ff',
                                 '#fcafa2ff',
                                 '#fcaea1ff',
                                 '#fcaea1ff',
                                 '#fcada0ff',
                                 '#fcada0ff',
                                 '#fcac9fff',
                                 '#fcac9fff',
                                 '#fcab9eff',
                                 '#fcab9eff',
                                 '#fcaa9dff',
                                 '#fcaa9dff',
                                 '#fcaa9cff',
                                 '#fca99cff',
                                 '#fca99bff',
                                 '#fca89bff',
                                 '#fca89aff',
                                 '#fca79aff',
                                 '#fca799ff',
                                 '#fca699ff',
                                 '#fca698ff',
                                 '#fca697ff',
                                 '#fca597ff',
                                 '#fca596ff',
                                 '#fca496ff',
                                 '#fca495ff',
                                 '#fca395ff',
                                 '#fca394ff',
                                 '#fca294ff',
                                 '#fca293ff',
                                 '#fca293ff',
                                 '#fca192ff',
                                 '#fca192ff',
                                 '#fca091ff',
                                 '#fca091ff',
                                 '#fc9f90ff',
                                 '#fc9f90ff',
                                 '#fc9e8fff',
                                 '#fc9e8fff',
                                 '#fc9e8eff',
                                 '#fc9d8eff',
                                 '#fc9d8dff',
                                 '#fc9c8dff',
                                 '#fc9c8cff',
                                 '#fb9b8cff',
                                 '#fb9b8bff',
                                 '#fb9a8bff',
                                 '#fb9a8aff',
                                 '#fb9a8aff',
                                 '#fb9989ff',
                                 '#fb9988ff',
                                 '#fb9888ff',
                                 '#fb9887ff',
                                 '#fb9787ff',
                                 '#fb9786ff',
                                 '#fb9686ff',
                                 '#fb9685ff',
                                 '#fb9585ff',
                                 '#fb9584ff',
                                 '#fb9584ff',
                                 '#fb9483ff',
                                 '#fb9483ff',
                                 '#fb9382ff',
                                 '#fb9382ff',
                                 '#fb9281ff',
                                 '#fb9281ff',
                                 '#fb9180ff',
                                 '#fb9180ff',
                                 '#fb917fff',
                                 '#fb907fff',
                                 '#fb907eff',
                                 '#fb8f7eff',
                                 '#fb8f7dff',
                                 '#fb8e7dff',
                                 '#fb8e7cff',
                                 '#fb8d7cff',
                                 '#fb8d7bff'],
                     'bad': '#00000000'},
           'cmap5': {'colours': ['#ffffffff',
                                 '#fffffeff',
                                 '#fffffeff',
                                 '#fffefdff',
                                 '#fffefcff',
                                 '#fffefcff',
                                 '#fffefbff',
                                 '#fffdfbff',
                                 '#fffdfaff',
                                 '#fffdf9ff',
                                 '#fffdf9ff',
                                 '#fffcf8ff',
                                 '#fffcf7ff',
                                 '#fffcf7ff',
                                 '#fffcf6ff',
                                 '#fffbf5ff',
                                 '#fffbf5ff',
                                 '#fffbf4ff',
                                 '#fffbf4ff',
                                 '#fffaf3ff',
                                 '#fffaf2ff',
                                 '#fffaf2ff',
                                 '#fffaf1ff',
                                 '#fff9f0ff',
                                 '#fff9f0ff',
                                 '#fff9efff',
                                 '#fff9eeff',
                                 '#fff8eeff',
                                 '#fff8edff',
                                 '#fff8edff',
                                 '#fff8ecff',
                                 '#fff7ebff',
                                 '#fff7ebff',
                                 '#fff7eaff',
                                 '#fff7e9ff',
                                 '#fff6e9ff',
                                 '#fff6e8ff',
                                 '#fff6e7ff',
                                 '#fff6e7ff',
                                 '#fff6e6ff',
                                 '#fff5e6ff',
                                 '#fff5e5ff',
                                 '#fff5e4ff',
                                 '#fff5e4ff',
                                 '#fff4e3ff',
                                 '#fff4e2ff',
                                 '#fff4e2ff',
                                 '#fff4e1ff',
                                 '#fff3e1ff',
                                 '#fff3e0ff',
                                 '#fff3dfff',
                                 '#fff3dfff',
                                 '#fff2deff',
                                 '#fff2ddff',
                                 '#fff2ddff',
                                 '#fff2dcff',
                                 '#fff1dbff',
                                 '#fff1dbff',
                                 '#fff1daff',
                                 '#fff1daff',
                                 '#fff0d9ff',
                                 '#fff0d8ff',
                                 '#fff0d8ff',
                                 '#fff0d7ff',
                                 '#ffefd6ff',
                                 '#ffefd6ff',
                                 '#ffefd5ff',
                                 '#ffefd4ff',
                                 '#ffeed4ff',
                                 '#ffeed3ff',
                                 '#ffeed3ff',
                                 '#ffeed2ff',
                                 '#ffedd1ff',
                                 '#ffedd1ff',
                                 '#ffedd0ff',
                                 '#ffedcfff',
                                 '#ffedcfff',
                                 '#ffecceff',
                                 '#ffeccdff',
                                 '#ffeccdff',
                                 '#ffecccff',
                                 '#ffebccff',
                                 '#ffebcbff',
                                 '#ffebcaff',
                                 '#ffebcaff',
                                 '#ffeac9ff',
                                 '#ffeac8ff',
                                 '#ffeac8ff',
                                 '#ffeac7ff',
                                 '#ffe9c6ff',
                                 '#ffe9c6ff',
                                 '#ffe9c5ff',
                                 '#ffe9c5ff',
                                 '#ffe8c4ff',
                                 '#ffe8c3ff',
                                 '#ffe8c3ff',
                                 '#ffe8c2ff',
                                 '#ffe7c1ff',
                                 '#ffe7c1ff',
                                 '#ffe7c0ff',
                                 '#ffe7bfff',
                                 '#ffe6bfff',
                                 '#ffe6beff',
                                 '#ffe6beff',
                                 '#ffe6bdff',
                                 '#ffe5bcff',
                                 '#ffe5bcff',
                                 '#ffe5bbff',
                                 '#ffe5baff',
                                 '#ffe5baff',
                                 '#ffe4b9ff',
                                 '#ffe4b8ff',
                                 '#ffe4b8ff',
                                 '#ffe4b7ff',
                                 '#ffe3b7ff',
                                 '#ffe3b6ff',
                                 '#ffe3b5ff',
                                 '#ffe3b5ff',
                                 '#ffe2b4ff',
                                 '#ffe2b3ff',
                                 '#ffe2b3ff',
                                 '#ffe2b2ff',
                                 '#ffe1b1ff',
                                 '#ffe1b1ff',
                                 '#ffe1b0ff',
                                 '#ffe1b0ff',
                                 '#ffe0afff',
                                 '#ffe0aeff',
                                 '#ffe0aeff',
                                 '#fee0adff',
                                 '#fedfacff',
                                 '#fedfacff',
                                 '#fedfabff',
                                 '#fedfabff',
                                 '#fedeaaff',
                                 '#fedea9ff',
                                 '#fedea9ff',
                                 '#fedea8ff',
                                 '#fedda7ff',
                                 '#fedda7ff',
                                 '#fedda6ff',
                                 '#fedda5ff',
                                 '#fedca5ff',
                                 '#fedca4ff',
                                 '#fedca4ff',
                                 '#fedca3ff',
                                 '#fedca2ff',
                                 '#fedba2ff',
                                 '#fedba1ff',
                                 '#fedba0ff',
                                 '#fedba0ff',
                                 '#feda9fff',
                                 '#feda9eff',
                                 '#feda9eff',
                                 '#feda9dff',
                                 '#fed99dff',
                                 '#fed99cff',
                                 '#fed99bff',
                                 '#fed99bff',
                                 '#fed89aff',
                                 '#fed899ff',
                                 '#fed899ff',
                                 '#fed898ff',
                                 '#fed797ff',
                                 '#fed797ff',
                                 '#fed796ff',
                                 '#fed796ff',
                                 '#fed695ff',
                                 '#fed694ff',
                                 '#fed694ff',
                                 '#fed693ff',
                                 '#fed592ff',
                                 '#fed592ff',
                                 '#fed591ff',
                                 '#fed590ff',
                                 '#fed490ff',
                                 '#fed48fff',
                                 '#fed48fff',
                                 '#fed48eff',
                                 '#fed38dff',
                                 '#fed38dff',
                                 '#fed38cff',
                                 '#fed38bff',
                                 '#fed38bff',
                                 '#fed28aff',
                                 '#fed289ff',
                                 '#fed289ff',
                                 '#fed288ff',
                                 '#fed188ff',
                                 '#fed187ff',
                                 '#fed186ff',
                                 '#fed186ff',
                                 '#fed085ff',
                                 '#fed084ff',
                                 '#fed084ff',
                                 '#fed083ff',
                                 '#fecf82ff',
                                 '#fecf82ff',
                                 '#fecf81ff',
                                 '#fecf81ff',
                                 '#fece80ff',
                                 '#fece7fff',
                                 '#fece7fff',
                                 '#fece7eff',
                                 '#fecd7dff',
                                 '#fecd7dff',
                                 '#fecd7cff',
                                 '#fecd7bff',
                                 '#fecc7bff',
                                 '#fecc7aff',
                                 '#fecc7aff',
                                 '#fecc79ff',
                                 '#fecb78ff',
                                 '#fecb78ff',
                                 '#fecb77ff',
                                 '#fecb76ff',
                                 '#feca76ff',
                                 '#feca75ff',
                                 '#feca75ff',
                                 '#feca74ff',
                                 '#feca73ff',
                                 '#fec973ff',
                                 '#fec972ff',
                                 '#fec971ff',
                                 '#fec971ff',
                                 '#fec870ff',
                                 '#fec86fff',
                                 '#fec86fff',
                                 '#fec86eff',
                                 '#fec76eff',
                                 '#fec76dff',
                                 '#fec76cff',
                                 '#fec76cff',
                                 '#fec66bff',
                                 '#fec66aff',
                                 '#fec66aff',
                                 '#fec669ff',
                                 '#fec568ff',
                                 '#fec568ff',
                                 '#fec567ff',
                                 '#fec567ff',
                                 '#fec466ff',
                                 '#fec465ff',
                                 '#fec465ff',
                                 '#fec464ff',
                                 '#fec363ff',
                                 '#fec363ff',
                                 '#fec362ff',
                                 '#fec361ff',
                                 '#fec261ff',
                                 '#fec260ff',
                                 '#fec260ff',
                                 '#fec25fff',
                                 '#fec15eff',
                                 '#fec15eff',
                                 '#fec15dff'],
                     'bad': '#00000000'}},
 'shapes': {'shape4': [[-197.2, -197.2],
                       [197.2, -197.2],
                       [197.2, 197.2],
                       [-197.2, 197.2],
                       [-197.2, -197.2]],
            'shape5': [[-340.0, -340.0], [-197.2, -197.2]],
            'shape6': [[340.0, -340.0], [197.2, -197.2]],
            'shape7': [[340.0, 340.0], [197.2, 197.2]],
            'shape8': [[-340.0, 340.0], [-197.2, 197.2]]}}
PANEL = {'title': ['Model output',
           'Climbing',
           'Active',
           'Alone',
           'Social active',
           'Social resting'],
 'headings': [],
 'partial': 'The dashed circle marking the bed, labelled "Bed" on the '
            'first map, is artwork pasted in Illustrator; not drawn by '
            'code: the data hold no bed position.',
 'subplots': [{'role': 'plot',
               'name': 'Model output',
               'text_style': [],
               'rect': [2.217, 2.5145, 0.739, 0.739],
               'pos': [0.26082352941176473,
                       0.7042272727272727,
                       0.08694117647058824,
                       0.06718181818181823],
               'xlim': [-340.0, 340.0],
               'ylim': [-340.0, 340.0],
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
               'ylabel': {'text': 'Top-down view',
                          'size': 7.0,
                          'colour': '#262626',
                          'rotation': 90.0,
                          'pad': 4.0,
                          'ha': 'center',
                          'va': 'baseline',
                          'coords': [-0.0717185385656296, 0.5]},
               'files': [{'file': 'model_output_image.png',
                          'kind': 'image',
                          'style': {'zorder': 0.0,
                                    'rank': 0,
                                    'cmap': 'cmap0',
                                    'clim': [0.46598598, 0.97052905]},
                          'styles': [{'zorder': 0.0,
                                      'rank': 0,
                                      'cmap': 'cmap0',
                                      'clim': [0.46598598,
                                               0.97052905]}]}],
               'decor': [{'kind': 'line',
                          'shape': 'shape4',
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
                          'shape': 'shape5',
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
                          'shape': 'shape6',
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
                          'shape': 'shape7',
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
                          'shape': 'shape8',
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
                           'clim': [0.46598598, 0.97052905],
                           'extent': [-340.0, 340.0, -340.0, 340.0],
                           'origin': 'upper',
                           'interpolation': 'nearest',
                           'zorder': 0.0,
                           'alpha': None}]},
              {'role': 'plot',
               'name': 'Climbing',
               'text_style': [],
               'rect': [3.22, 2.5145, 0.739, 0.739],
               'pos': [0.3788235294117647,
                       0.7042272727272727,
                       0.08694117647058824,
                       0.06718181818181823],
               'xlim': [-340.0, 340.0],
               'ylim': [-340.0, 340.0],
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
               'ylabel': {'text': 'Top-down view',
                          'size': 7.0,
                          'colour': '#262626',
                          'rotation': 90.0,
                          'pad': 4.0,
                          'ha': 'center',
                          'va': 'baseline',
                          'coords': [-0.07171853856563004, 0.5]},
               'files': [{'file': 'climbing_map.csv',
                          'kind': 'map',
                          'style': {'zorder': 0.0,
                                    'rank': 0,
                                    'cmap': 'cmap1',
                                    'clim': [0.0, 1.0]},
                          'styles': [{'zorder': 0.0,
                                      'rank': 0,
                                      'cmap': 'cmap1',
                                      'clim': [0.0, 1.0]}]}],
               'decor': [{'kind': 'line',
                          'shape': 'shape4',
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
                          'shape': 'shape5',
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
                          'shape': 'shape6',
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
                          'shape': 'shape7',
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
                          'shape': 'shape8',
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
                           'clim': [0.0, 1.0],
                           'extent': [-340.0, 340.0, -340.0, 340.0],
                           'origin': 'upper',
                           'interpolation': 'nearest',
                           'zorder': 0.0,
                           'alpha': None}]},
              {'role': 'plot',
               'name': 'Active',
               'text_style': [],
               'rect': [4.224, 2.5145, 0.739, 0.739],
               'pos': [0.4969411764705883,
                       0.7042272727272727,
                       0.08694117647058824,
                       0.06718181818181823],
               'xlim': [-340.0, 340.0],
               'ylim': [-340.0, 340.0],
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
               'ylabel': {'text': 'Top-down view',
                          'size': 7.0,
                          'colour': '#262626',
                          'rotation': 90.0,
                          'pad': 4.0,
                          'ha': 'center',
                          'va': 'baseline',
                          'coords': [-0.07171853856562915, 0.5]},
               'files': [{'file': 'active_map.csv',
                          'kind': 'map',
                          'style': {'zorder': 0.0,
                                    'rank': 0,
                                    'cmap': 'cmap2',
                                    'clim': [0.0, 1.0]},
                          'styles': [{'zorder': 0.0,
                                      'rank': 0,
                                      'cmap': 'cmap2',
                                      'clim': [0.0, 1.0]}]}],
               'decor': [{'kind': 'line',
                          'shape': 'shape4',
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
                          'shape': 'shape5',
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
                          'shape': 'shape6',
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
                          'shape': 'shape7',
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
                          'shape': 'shape8',
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
                           'clim': [0.0, 1.0],
                           'extent': [-340.0, 340.0, -340.0, 340.0],
                           'origin': 'upper',
                           'interpolation': 'nearest',
                           'zorder': 0.0,
                           'alpha': None}]},
              {'role': 'plot',
               'name': 'Alone',
               'text_style': [],
               'rect': [5.222, 2.5145, 0.739, 0.739],
               'pos': [0.6143529411764707,
                       0.7042272727272727,
                       0.08694117647058819,
                       0.06718181818181812],
               'xlim': [-340.0, 340.0],
               'ylim': [-340.0, 340.0],
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
               'ylabel': {'text': 'Top-down view',
                          'size': 7.0,
                          'colour': '#262626',
                          'rotation': 90.0,
                          'pad': 4.0,
                          'ha': 'center',
                          'va': 'baseline',
                          'coords': [-0.07171853856562915,
                                     0.4999999999999982]},
               'files': [{'file': 'alone_map.csv',
                          'kind': 'map',
                          'style': {'zorder': 0.0,
                                    'rank': 0,
                                    'cmap': 'cmap3',
                                    'clim': [0.0, 1.0]},
                          'styles': [{'zorder': 0.0,
                                      'rank': 0,
                                      'cmap': 'cmap3',
                                      'clim': [0.0, 1.0]}]}],
               'decor': [{'kind': 'line',
                          'shape': 'shape4',
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
                          'shape': 'shape5',
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
                          'shape': 'shape6',
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
                          'shape': 'shape7',
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
                          'shape': 'shape8',
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
                           'clim': [0.0, 1.0],
                           'extent': [-340.0, 340.0, -340.0, 340.0],
                           'origin': 'upper',
                           'interpolation': 'nearest',
                           'zorder': 0.0,
                           'alpha': None}]},
              {'role': 'plot',
               'name': 'Social active',
               'text_style': [],
               'rect': [6.225, 2.5145, 0.739, 0.739],
               'pos': [0.7323529411764705,
                       0.7042272727272727,
                       0.08694117647058819,
                       0.06718181818181812],
               'xlim': [-340.0, 340.0],
               'ylim': [-340.0, 340.0],
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
               'ylabel': {'text': 'Top-down view',
                          'size': 7.0,
                          'colour': '#262626',
                          'rotation': 90.0,
                          'pad': 4.0,
                          'ha': 'center',
                          'va': 'baseline',
                          'coords': [-0.07171853856562826,
                                     0.4999999999999982]},
               'files': [{'file': 'social_active_map.csv',
                          'kind': 'map',
                          'style': {'zorder': 0.0,
                                    'rank': 0,
                                    'cmap': 'cmap4',
                                    'clim': [0.0, 1.0]},
                          'styles': [{'zorder': 0.0,
                                      'rank': 0,
                                      'cmap': 'cmap4',
                                      'clim': [0.0, 1.0]}]}],
               'decor': [{'kind': 'line',
                          'shape': 'shape4',
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
                          'shape': 'shape5',
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
                          'shape': 'shape6',
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
                          'shape': 'shape7',
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
                          'shape': 'shape8',
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
                           'clim': [0.0, 1.0],
                           'extent': [-340.0, 340.0, -340.0, 340.0],
                           'origin': 'upper',
                           'interpolation': 'nearest',
                           'zorder': 0.0,
                           'alpha': None}]},
              {'role': 'plot',
               'name': 'Social resting',
               'text_style': [],
               'rect': [7.229, 2.5145, 0.739, 0.739],
               'pos': [0.8504705882352941,
                       0.7042272727272727,
                       0.08694117647058819,
                       0.06718181818181812],
               'xlim': [-340.0, 340.0],
               'ylim': [-340.0, 340.0],
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
               'ylabel': {'text': 'Top-down view',
                          'size': 7.0,
                          'colour': '#262626',
                          'rotation': 90.0,
                          'pad': 4.0,
                          'ha': 'center',
                          'va': 'baseline',
                          'coords': [-0.07171853856562826,
                                     0.4999999999999982]},
               'files': [{'file': 'social_resting_map.csv',
                          'kind': 'map',
                          'style': {'zorder': 0.0,
                                    'rank': 0,
                                    'cmap': 'cmap5',
                                    'clim': [0.0, 1.0]},
                          'styles': [{'zorder': 0.0,
                                      'rank': 0,
                                      'cmap': 'cmap5',
                                      'clim': [0.0, 1.0]}]}],
               'decor': [{'kind': 'line',
                          'shape': 'shape4',
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
                          'shape': 'shape5',
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
                          'shape': 'shape6',
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
                          'shape': 'shape7',
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
                          'shape': 'shape8',
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
               'images': [{'cmap': 'cmap5',
                           'clim': [0.0, 1.0],
                           'extent': [-340.0, 340.0, -340.0, 340.0],
                           'origin': 'upper',
                           'interpolation': 'nearest',
                           'zorder': 0.0,
                           'alpha': None}]}],
 'texts': [{'text': 'Model output',
            'x': 2.5865,
            'y': 2.4763,
            'size': 8.0,
            'weight': 'normal',
            'ha': 'center',
            'va': 'baseline',
            'rotation': 0.0,
            'colour': '#262626'},
           {'text': 'Climbing',
            'x': 3.5895,
            'y': 2.4763,
            'size': 8.0,
            'weight': 'normal',
            'ha': 'center',
            'va': 'baseline',
            'rotation': 0.0,
            'colour': '#6662d7'},
           {'text': 'Active',
            'x': 4.5935,
            'y': 2.4763,
            'size': 8.0,
            'weight': 'normal',
            'ha': 'center',
            'va': 'baseline',
            'rotation': 0.0,
            'colour': '#a85fba'},
           {'text': 'Alone',
            'x': 5.5915,
            'y': 2.4763,
            'size': 8.0,
            'weight': 'normal',
            'ha': 'center',
            'va': 'baseline',
            'rotation': 0.0,
            'colour': '#f05c9b'},
           {'text': 'Social active',
            'x': 6.5945,
            'y': 2.4763,
            'size': 8.0,
            'weight': 'normal',
            'ha': 'center',
            'va': 'baseline',
            'rotation': 0.0,
            'colour': '#fb8d7b'},
           {'text': 'Social resting',
            'x': 7.5985,
            'y': 2.4763,
            'size': 8.0,
            'weight': 'normal',
            'ha': 'center',
            'va': 'baseline',
            'rotation': 0.0,
            'colour': '#fec15d'}],
 'legends': [],
 'letter': {'ch': 'd', 'x': 1.8382, 'baseline': 2.3717, 'top': 2.2517}}


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
                         "figures/fig2)")
    a = ap.parse_args(argv)
    for path in render(a.data, a.out_dir):
        print(f"wrote {os.path.normpath(path)}")


if __name__ == "__main__":
    main()
