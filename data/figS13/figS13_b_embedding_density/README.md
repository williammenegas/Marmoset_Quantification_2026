# figS13_b_embedding_density

Figure S13, panel b. Title: "Behavioral embedding space".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS13/figS13_b_embedding_density.py`](../../../code/figS13/figS13_b_embedding_density.py).

## Files

### `control_map.csv` (85.4 KB)

From the subplot "Control" (row 2, column 1 of the panel's subplots, 0.53-1.27 in across and 4.20-4.94 in down the page), under the page text "Control"; no axis labels; drawn over x -120 to 120, y -120 to 120 (values beyond these limits are exported but were not visible).

A 96 x 96 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -120 to 120, y -120 to 120 (lower origin).
Colour map mb (Normalize), limits 0 to 1; no colour bar.

### `control_control_day_1_lines.csv` (8.3 KB)

From the subplot "Control Control (day 1)" (row 1, column 1 of the panel's subplots, 1.68-2.30 in across and 4.14-4.96 in down the page); y axis "Social resting time (min)"; drawn over x -0.5 to 1.5, y 0 to 11.318377 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Control (day 1)" at 1.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `Social resting time (min)` | y position on the axis labelled "Social resting time (min)" (unit: min) |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `category` | the category named by the nearest x tick label |

Line styles: 91 lines: colour #cccccc, width 0.5 pt; 3 lines: colour #262626, width 0.5 pt

### `control_control_day_1_points.csv` (8.0 KB)

From the subplot "Control Control (day 1)" (row 1, column 1 of the panel's subplots, 1.68-2.30 in across and 4.14-4.96 in down the page); y axis "Social resting time (min)"; drawn over x -0.5 to 1.5, y 0 to 11.318377 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Control (day 1)" at 1.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position; this axis carries no label; the plotted, jittered position |
| `Social resting time (min)` | y position on the axis labelled "Social resting time (min)" (unit: min) |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

Every marker has an area of 6 pt^2.

### `treat_map.csv` (84.9 KB)

From the subplot "Treat" (row 2, column 2 of the panel's subplots, 2.44-3.18 in across and 4.20-4.94 in down the page), under the page text "Treat"; no axis labels; drawn over x -120 to 120, y -120 to 120 (values beyond these limits are exported but were not visible).

A 96 x 96 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -120 to 120, y -120 to 120 (lower origin).
Colour map mb (Normalize), limits 0 to 1; no colour bar.

### `control_treat_lines.csv` (7.3 KB)

From the subplot "Control Treat" (row 1, column 2 of the panel's subplots, 3.59-4.21 in across and 4.14-4.96 in down the page); y axis "Social resting time (min)"; drawn over x -0.5 to 1.5, y 0 to 8.7717839 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Treat" at 1.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `Social resting time (min)` | y position on the axis labelled "Social resting time (min)" (unit: min) |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `category` | the category named by the nearest x tick label |

Line styles: 91 lines: colour #cccccc, width 0.5 pt; 3 lines: colour #262626, width 0.5 pt

### `control_treat_points.csv` (7.0 KB)

From the subplot "Control Treat" (row 1, column 2 of the panel's subplots, 3.59-4.21 in across and 4.14-4.96 in down the page); y axis "Social resting time (min)"; drawn over x -0.5 to 1.5, y 0 to 8.7717839 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Treat" at 1.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position; this axis carries no label; the plotted, jittered position |
| `Social resting time (min)` | y position on the axis labelled "Social resting time (min)" (unit: min) |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

Every marker has an area of 6 pt^2.

### `object_map.csv` (85.0 KB)

From the subplot "Object" (row 2, column 3 of the panel's subplots, 4.35-5.09 in across and 4.20-4.94 in down the page), under the page text "Object"; no axis labels; drawn over x -120 to 120, y -120 to 120 (values beyond these limits are exported but were not visible).

A 96 x 96 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -120 to 120, y -120 to 120 (lower origin).
Colour map mb (Normalize), limits 0 to 1; no colour bar.

### `control_object_lines.csv` (7.3 KB)

From the subplot "Control Object" (row 1, column 3 of the panel's subplots, 5.50-6.12 in across and 4.14-4.96 in down the page); y axis "Social resting time (min)"; drawn over x -0.5 to 1.5, y 0 to 13.396733 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Object" at 1.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `Social resting time (min)` | y position on the axis labelled "Social resting time (min)" (unit: min) |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `category` | the category named by the nearest x tick label |

Line styles: 89 lines: colour #cccccc, width 0.5 pt; 3 lines: colour #262626, width 0.5 pt

### `control_object_points.csv` (7.0 KB)

From the subplot "Control Object" (row 1, column 3 of the panel's subplots, 5.50-6.12 in across and 4.14-4.96 in down the page); y axis "Social resting time (min)"; drawn over x -0.5 to 1.5, y 0 to 13.396733 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Object" at 1.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position; this axis carries no label; the plotted, jittered position |
| `Social resting time (min)` | y position on the axis labelled "Social resting time (min)" (unit: min) |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

Every marker has an area of 6 pt^2.

### `tablet_map.csv` (84.8 KB)

From the subplot "Tablet" (row 2, column 4 of the panel's subplots, 6.25-6.99 in across and 4.20-4.94 in down the page), under the page text "Tablet"; no axis labels; drawn over x -120 to 120, y -120 to 120 (values beyond these limits are exported but were not visible).

A 96 x 96 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -120 to 120, y -120 to 120 (lower origin).
Colour map mb (Normalize), limits 0 to 1; no colour bar.

### `control_tablet_lines.csv` (5.8 KB)

From the subplot "Control Tablet" (row 1, column 4 of the panel's subplots, 7.41-8.03 in across and 4.14-4.96 in down the page); y axis "Social resting time (min)"; drawn over x -0.5 to 1.5, y 0 to 9.1762333 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Tablet" at 1.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `Social resting time (min)` | y position on the axis labelled "Social resting time (min)" (unit: min) |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `category` | the category named by the nearest x tick label |

Line styles: 70 lines: colour #cccccc, width 0.5 pt; 3 lines: colour #262626, width 0.5 pt

### `control_tablet_points.csv` (5.5 KB)

From the subplot "Control Tablet" (row 1, column 4 of the panel's subplots, 7.41-8.03 in across and 4.14-4.96 in down the page); y axis "Social resting time (min)"; drawn over x -0.5 to 1.5, y 0 to 9.1762333 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Tablet" at 1.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position; this axis carries no label; the plotted, jittered position |
| `Social resting time (min)` | y position on the axis labelled "Social resting time (min)" (unit: min) |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

Every marker has an area of 6 pt^2.

### `noise_map.csv` (84.6 KB)

From the subplot "Noise" (row 4, column 1 of the panel's subplots, 0.53-1.27 in across and 5.53-6.27 in down the page), under the page text "Noise"; no axis labels; drawn over x -120 to 120, y -120 to 120 (values beyond these limits are exported but were not visible).

A 96 x 96 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -120 to 120, y -120 to 120 (lower origin).
Colour map mb (Normalize), limits 0 to 1; no colour bar.

### `control_noise_lines.csv` (7.4 KB)

From the subplot "Control Noise" (row 3, column 1 of the panel's subplots, 1.68-2.30 in across and 5.47-6.29 in down the page); y axis "Social resting time (min)"; drawn over x -0.5 to 1.5, y 0 to 13.274067 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Noise" at 1.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `Social resting time (min)` | y position on the axis labelled "Social resting time (min)" (unit: min) |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `category` | the category named by the nearest x tick label |

Line styles: 92 lines: colour #cccccc, width 0.5 pt; 3 lines: colour #262626, width 0.5 pt

### `control_noise_points.csv` (7.1 KB)

From the subplot "Control Noise" (row 3, column 1 of the panel's subplots, 1.68-2.30 in across and 5.47-6.29 in down the page); y axis "Social resting time (min)"; drawn over x -0.5 to 1.5, y 0 to 13.274067 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Noise" at 1.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position; this axis carries no label; the plotted, jittered position |
| `Social resting time (min)` | y position on the axis labelled "Social resting time (min)" (unit: min) |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

Every marker has an area of 6 pt^2.

### `toys_map.csv` (85.0 KB)

From the subplot "Toys" (row 4, column 2 of the panel's subplots, 2.44-3.18 in across and 5.53-6.27 in down the page), under the page text "Toys"; no axis labels; drawn over x -120 to 120, y -120 to 120 (values beyond these limits are exported but were not visible).

A 96 x 96 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -120 to 120, y -120 to 120 (lower origin).
Colour map mb (Normalize), limits 0 to 1; no colour bar.

### `control_toys_lines.csv` (6.6 KB)

From the subplot "Control Toys" (row 3, column 2 of the panel's subplots, 3.59-4.21 in across and 5.47-6.29 in down the page); y axis "Social resting time (min)"; drawn over x -0.5 to 1.5, y 0 to 16.151494 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Toys" at 1.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `Social resting time (min)` | y position on the axis labelled "Social resting time (min)" (unit: min) |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `category` | the category named by the nearest x tick label |

Line styles: 82 lines: colour #cccccc, width 0.5 pt; 3 lines: colour #262626, width 0.5 pt

### `control_toys_points.csv` (6.3 KB)

From the subplot "Control Toys" (row 3, column 2 of the panel's subplots, 3.59-4.21 in across and 5.47-6.29 in down the page); y axis "Social resting time (min)"; drawn over x -0.5 to 1.5, y 0 to 16.151494 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Toys" at 1.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position; this axis carries no label; the plotted, jittered position |
| `Social resting time (min)` | y position on the axis labelled "Social resting time (min)" (unit: min) |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

Every marker has an area of 6 pt^2.

### `intruder_map.csv` (84.9 KB)

From the subplot "Intruder" (row 4, column 3 of the panel's subplots, 4.35-5.09 in across and 5.53-6.27 in down the page), under the page text "Intruder"; no axis labels; drawn over x -120 to 120, y -120 to 120 (values beyond these limits are exported but were not visible).

A 96 x 96 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -120 to 120, y -120 to 120 (lower origin).
Colour map mb (Normalize), limits 0 to 1; no colour bar.

### `control_intruder_lines.csv` (7.6 KB)

From the subplot "Control Intruder" (row 3, column 3 of the panel's subplots, 5.50-6.12 in across and 5.47-6.29 in down the page); y axis "Social resting time (min)"; drawn over x -0.5 to 1.5, y 0 to 8.9562 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Intruder" at 1.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `Social resting time (min)` | y position on the axis labelled "Social resting time (min)" (unit: min) |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `category` | the category named by the nearest x tick label |

Line styles: 91 lines: colour #cccccc, width 0.5 pt; 3 lines: colour #262626, width 0.5 pt

### `control_intruder_points.csv` (7.3 KB)

From the subplot "Control Intruder" (row 3, column 3 of the panel's subplots, 5.50-6.12 in across and 5.47-6.29 in down the page); y axis "Social resting time (min)"; drawn over x -0.5 to 1.5, y 0 to 8.9562 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Intruder" at 1.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position; this axis carries no label; the plotted, jittered position |
| `Social resting time (min)` | y position on the axis labelled "Social resting time (min)" (unit: min) |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

Every marker has an area of 6 pt^2.

### `mask_map.csv` (84.3 KB)

From the subplot "Mask" (row 4, column 4 of the panel's subplots, 6.25-6.99 in across and 5.53-6.27 in down the page), under the page text "Mask"; no axis labels; drawn over x -120 to 120, y -120 to 120 (values beyond these limits are exported but were not visible).

A 96 x 96 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -120 to 120, y -120 to 120 (lower origin).
Colour map mb (Normalize), limits 0 to 1; no colour bar.

### `control_mask_lines.csv` (7.4 KB)

From the subplot "Control Mask" (row 3, column 4 of the panel's subplots, 7.41-8.03 in across and 5.47-6.29 in down the page); y axis "Social resting time (min)"; drawn over x -0.5 to 1.5, y 0 to 8.7717839 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Mask" at 1.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `Social resting time (min)` | y position on the axis labelled "Social resting time (min)" (unit: min) |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `category` | the category named by the nearest x tick label |

Line styles: 92 lines: colour #cccccc, width 0.5 pt; 3 lines: colour #262626, width 0.5 pt

### `control_mask_points.csv` (7.0 KB)

From the subplot "Control Mask" (row 3, column 4 of the panel's subplots, 7.41-8.03 in across and 5.47-6.29 in down the page); y axis "Social resting time (min)"; drawn over x -0.5 to 1.5, y 0 to 8.7717839 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Mask" at 1.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position; this axis carries no label; the plotted, jittered position |
| `Social resting time (min)` | y position on the axis labelled "Social resting time (min)" (unit: min) |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

Every marker has an area of 6 pt^2.

### `page_shapes.csv` (69 B)

Drawn on the page around the panel's subplots, not in one of them: 1 Line2D.

One row is one vertex of one shape drawn on the page.

| Column | Meaning |
|---|---|
| `shape` | which shape, numbered from 1 in drawing order |
| `vertex` | the vertex's place along the shape |
| `x (in)` | inches from the page's left edge |
| `y (in)` | inches down from the page's top edge |

Drawn as: Line2D.
Every shape's fill: none.
Every line's colour: #737373.
Every line's width (pt): 0.5.
Every line is: solid.
These are drawn on the page around the panel's subplots, not in one of them, so they are given in page inches, not in data coordinates. A shape that does not end where it starts is an open line.

### `annotations.csv` (720 B)

Every text printed in the panel: inside a subplot (x and y in that subplot's data coordinates; for an annotation with a leader line, the point it marks in `target x` and `target y`) or on the page around the subplots (x and y in inches from the page's top-left: the text's anchor).

| Column | Meaning |
|---|---|
| `subplot` | the subplot the text is in; blank for page text |
| `text` | the text as printed, on one line |
| `x`, `y` | its position (see `coordinates`) |
| `coordinates` | "data" or "page inches" |

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- decoration: the dashed category outlines: 48 Line2D

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| AxesImage | 8 | 8 |
| Line2D | 770 | 722 |
| PathCollection | 16 | 16 |
| Text | 8 | 8 |
| Line2D (on the page) | 1 | 1 |
