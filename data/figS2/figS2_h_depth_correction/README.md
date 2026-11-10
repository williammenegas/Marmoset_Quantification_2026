# figS2_h_depth_correction

Figure S2, panel h. Title: "Raw data", "Depth correction applied", "Top view (raw)", "Side view (raw)", "Top view (corrected)", "Side view (corrected)".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS2/figS2_h_depth_correction.py`](../../../code/figS2/figS2_h_depth_correction.py).

## Files

### `top_view_raw_points.csv` (1.2 MB)

From the subplot "Top view (raw)" (row 2, column 1 of the panel's subplots, 1.32-2.25 in across and 6.43-7.36 in down the page), under the page text "Top view (raw)"; x axis "X (px)"; y axis "Y (px)"; drawn over x -400 to 400, y -400 to 400 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `X (px)` | x position on the axis labelled "X (px)" (unit: px) |
| `Y (px)` | y position on the axis labelled "Y (px)" (unit: px) |
| `Depth (a.u.)` | the value the point's colour maps, on the colour bar labelled "Depth (a.u.)" |

Colour map from_list (Normalize) from 50 to 175.
Every marker has an area of 0.8 pt^2.

### `side_view_raw_points.csv` (1.1 MB)

From the subplot "Side view (raw)" (row 1, column 1 of the panel's subplots, 2.79-3.70 in across and 6.38-7.42 in down the page), under the page text "Side view (raw)"; x axis "X (px)"; y axis "Depth (a.u.)"; drawn over x -400 to 400, y 50 to 175 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `X (px)` | x position on the axis labelled "X (px)" (unit: px) |
| `Depth (a.u.)` | y position on the axis labelled "Depth (a.u.)" (unit: a.u.) |
| `Depth (a.u.)` | the value the point's colour maps, on the colour bar labelled "Depth (a.u.)" |

Colour map from_list (Normalize) from 50 to 175.
Every marker has an area of 0.8 pt^2.

### `top_view_corrected_points.csv` (1.2 MB)

From the subplot "Top view (corrected)" (row 2, column 2 of the panel's subplots, 5.04-5.97 in across and 6.45-7.38 in down the page), under the page text "Top view (corrected)"; x axis "X (a.u.)"; y axis "Y (a.u.)"; drawn over x -80 to 80, y -80 to 80 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `X (a.u.)` | x position on the axis labelled "X (a.u.)" (unit: a.u.) |
| `Y (a.u.)` | y position on the axis labelled "Y (a.u.)" (unit: a.u.) |
| `Depth (a.u.)` | the value the point's colour maps, on the colour bar labelled "Depth (a.u.)" |

Colour map from_list (Normalize) from 50 to 175.
Every marker has an area of 0.8 pt^2.

### `side_view_corrected_points.csv` (1.1 MB)

From the subplot "Side view (corrected)" (row 1, column 2 of the panel's subplots, 6.56-7.35 in across and 6.38-7.42 in down the page), under the page text "Side view (corrected)"; x axis "X (a.u.)"; y axis "Depth (a.u.)"; drawn over x -80 to 80, y 50 to 175 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `X (a.u.)` | x position on the axis labelled "X (a.u.)" (unit: a.u.) |
| `Depth (a.u.)` | y position on the axis labelled "Depth (a.u.)" (unit: a.u.) |
| `Depth (a.u.)` | the value the point's colour maps, on the colour bar labelled "Depth (a.u.)" |

Colour map from_list (Normalize) from 50 to 175.
Every marker has an area of 0.8 pt^2.

### `page_shapes.csv` (91 B)

Drawn on the page around the panel's subplots, not in one of them: 2 Line2D.

One row is one vertex of one shape drawn on the page.

| Column | Meaning |
|---|---|
| `shape` | which shape, numbered from 1 in drawing order |
| `vertex` | the vertex's place along the shape |
| `x (in)` | inches from the page's left edge |
| `y (in)` | inches down from the page's top edge |

Drawn as: Line2D.
Every shape's fill: none.
Every line's colour: #262626.
Every line's width (pt): 0.5.
Every line is: solid.
These are drawn on the page around the panel's subplots, not in one of them, so they are given in page inches, not in data coordinates. A shape that does not end where it starts is an open line.

### `annotations.csv` (308 B)

Every text printed in the panel: inside a subplot (x and y in that subplot's data coordinates; for an annotation with a leader line, the point it marks in `target x` and `target y`) or on the page around the subplots (x and y in inches from the page's top-left: the text's anchor).

| Column | Meaning |
|---|---|
| `subplot` | the subplot the text is in; blank for page text |
| `text` | the text as printed, on one line |
| `x`, `y` | its position (see `coordinates`) |
| `coordinates` | "data" or "page inches" |

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- colour bar (its label and limits are given with the data it keys): 2 LineCollection, 2 QuadMesh
- decoration: the dashed cage wireframe: 10 Line2D

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| Line2D | 10 | 0 |
| LineCollection | 2 | 0 |
| PathCollection | 4 | 4 |
| QuadMesh | 2 | 0 |
| Line2D (on the page) | 2 | 2 |
