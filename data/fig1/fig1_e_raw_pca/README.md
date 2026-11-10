# fig1_e_raw_pca

Figure 1, panel e. Title: "Raw data", "PCA".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig1/fig1_e_raw_pca.py`](../../../code/fig1/fig1_e_raw_pca.py).

## Files

### `x_coordinates_map.csv` (87.0 KB)

From the subplot "X coordinates" (row 1, column 1 of the panel's subplots, 0.73-2.49 in across and 4.48-4.75 in down the page), under the page text "Raw data" / "X coordinates"; x axis "Time (min)"; y axis "Label #"; drawn over x 0 to 6, y 21 to 0 (values beyond these limits are exported but were not visible).

A 21 x 360 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `Label # \ Time (min)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `z-score` | every other cell: the image cell's value |

Image extent: x 0 to 6, y 21 to 0 (upper origin).
Colour map mb (Normalize), limits -2 to 2, colour bar "z-score".

### `y_coordinates_map.csv` (86.8 KB)

From the subplot "Y coordinates" (row 2, column 1 of the panel's subplots, 0.73-2.49 in across and 4.91-5.18 in down the page), under the page text "Y coordinates"; x axis "Time (min)"; y axis "Label #"; drawn over x 0 to 6, y 21 to 0 (values beyond these limits are exported but were not visible).

A 21 x 360 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `Label # \ Time (min)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `z-score` | every other cell: the image cell's value |

Image extent: x 0 to 6, y 21 to 0 (upper origin).
Colour map mb (Normalize), limits -2 to 2, colour bar "z-score".

### `pca_lines.csv` (105 B)

From the subplot "PCA" (row 1, column 2 of the panel's subplots, 3.17-4.01 in across and 4.52-5.20 in down the page), under the page text "PCA", in the row labelled "Y coordinates"; x axis "Component"; y axis "Explained (%)"; drawn over x 0.2 to 40.8, y 0 to 80 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Component` | x position on the axis labelled "Component" |
| `Explained (%)` | y position on the axis labelled "Explained (%)" (unit: %) |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |

Line styles: 1 line: colour #262626, width 0.84 pt; 1 line: colour #999999, width 0.84 pt

### `pca_bars.csv` (925 B)

From the subplot "PCA" (row 1, column 2 of the panel's subplots, 3.17-4.01 in across and 4.52-5.20 in down the page), under the page text "PCA", in the row labelled "Y coordinates"; x axis "Component"; y axis "Explained (%)"; drawn over x 0.2 to 40.8, y 0 to 80 (values beyond these limits are exported but were not visible).

One row is one vertical bar.

| Column | Meaning |
|---|---|
| `Component` | x of the bar's centre on the axis labelled "Component" |
| `bar width` | the bar's width, in x units |
| `bar bottom` | where the bar starts, in y units |
| `Explained (%)` | the bar's height: y extent on the axis labelled "Explained (%)" (unit: %) |

Every bar is filled: #262626.

### `annotations.csv` (251 B)

Every text printed in the panel: inside a subplot (x and y in that subplot's data coordinates; for an annotation with a leader line, the point it marks in `target x` and `target y`) or on the page around the subplots (x and y in inches from the page's top-left: the text's anchor).

| Column | Meaning |
|---|---|
| `subplot` | the subplot the text is in; blank for page text |
| `text` | the text as printed, on one line |
| `x`, `y` | its position (see `coordinates`) |
| `coordinates` | "data" or "page inches" |

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- colour bar (its label and limits are given with the data it keys): 1 LineCollection, 1 QuadMesh

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| AxesImage | 2 | 2 |
| Line2D | 2 | 2 |
| LineCollection | 1 | 0 |
| QuadMesh | 1 | 0 |
| Rectangle | 40 | 40 |
| Text | 2 | 2 |
