# figS13_a_cage_occupancy

Figure S13, panel a. Title: "Cage space".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS13/figS13_a_cage_occupancy.py`](../../../code/figS13/figS13_a_cage_occupancy.py).

## Files

### `control_points.csv` (25 B)

From the subplot "Control" (row 1, column 5 of the panel's subplots, 0.53-1.27 in across and 1.16-1.90 in down the page), under the page text "Control"; no axis labels; drawn over x -500 to 500, y -500 to 500 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |

Every marker has an area of 8.490396 pt^2.
Every marker is filled #33b259.

### `control_map.csv` (45.0 KB)

From the subplot "Control" (row 1, column 5 of the panel's subplots, 0.53-1.27 in across and 1.16-1.90 in down the page), under the page text "Control"; no axis labels; drawn over x -500 to 500, y -500 to 500 (values beyond these limits are exported but were not visible).

A 64 x 64 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -500 to 500, y -500 to 500 (lower origin).
Colour map mb (Normalize), limits 0 to 1; no colour bar.

### `control_control_day_1_lines.csv` (8.2 KB)

From the subplot "Control Control (day 1)" (row 1, column 1 of the panel's subplots, 1.69-2.31 in across and 1.12-1.94 in down the page); y axis "Time near stimulus (min)"; drawn over x -0.5 to 1.5, y 0 to 28.517401 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Control (day 1)" at 1.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `Time near stimulus (min)` | y position on the axis labelled "Time near stimulus (min)" (unit: min) |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `category` | the category named by the nearest x tick label |

Line styles: 90 lines: colour #cccccc, width 0.5 pt; 3 lines: colour #262626, width 0.5 pt

### `control_control_day_1_points.csv` (7.9 KB)

From the subplot "Control Control (day 1)" (row 1, column 1 of the panel's subplots, 1.69-2.31 in across and 1.12-1.94 in down the page); y axis "Time near stimulus (min)"; drawn over x -0.5 to 1.5, y 0 to 28.517401 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Control (day 1)" at 1.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position; this axis carries no label; the plotted, jittered position |
| `Time near stimulus (min)` | y position on the axis labelled "Time near stimulus (min)" (unit: min) |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

Every marker has an area of 6 pt^2.

### `treat_points.csv` (25 B)

From the subplot "Treat" (row 1, column 6 of the panel's subplots, 2.44-3.18 in across and 1.16-1.90 in down the page), under the page text "Treat"; no axis labels; drawn over x -500 to 500, y -500 to 500 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |

Every marker has an area of 8.490396 pt^2.
Every marker is filled #33b259.

### `treat_map.csv` (43.8 KB)

From the subplot "Treat" (row 1, column 6 of the panel's subplots, 2.44-3.18 in across and 1.16-1.90 in down the page), under the page text "Treat"; no axis labels; drawn over x -500 to 500, y -500 to 500 (values beyond these limits are exported but were not visible).

A 64 x 64 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -500 to 500, y -500 to 500 (lower origin).
Colour map mb (Normalize), limits 0 to 1; no colour bar.

### `control_treat_lines.csv` (7.2 KB)

From the subplot "Control Treat" (row 1, column 2 of the panel's subplots, 3.60-4.22 in across and 1.12-1.94 in down the page); y axis "Time near stimulus (min)"; drawn over x -0.5 to 1.5, y 0 to 14.795722 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Treat" at 1.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `Time near stimulus (min)` | y position on the axis labelled "Time near stimulus (min)" (unit: min) |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `category` | the category named by the nearest x tick label |

Line styles: 89 lines: colour #cccccc, width 0.5 pt; 3 lines: colour #262626, width 0.5 pt

### `control_treat_points.csv` (6.9 KB)

From the subplot "Control Treat" (row 1, column 2 of the panel's subplots, 3.60-4.22 in across and 1.12-1.94 in down the page); y axis "Time near stimulus (min)"; drawn over x -0.5 to 1.5, y 0 to 14.795722 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Treat" at 1.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position; this axis carries no label; the plotted, jittered position |
| `Time near stimulus (min)` | y position on the axis labelled "Time near stimulus (min)" (unit: min) |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

Every marker has an area of 6 pt^2.

### `object_points.csv` (25 B)

From the subplot "Object" (row 1, column 7 of the panel's subplots, 4.35-5.09 in across and 1.16-1.90 in down the page), under the page text "Object"; no axis labels; drawn over x -500 to 500, y -500 to 500 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |

Every marker has an area of 8.490396 pt^2.
Every marker is filled #33b259.

### `object_map.csv` (43.9 KB)

From the subplot "Object" (row 1, column 7 of the panel's subplots, 4.35-5.09 in across and 1.16-1.90 in down the page), under the page text "Object"; no axis labels; drawn over x -500 to 500, y -500 to 500 (values beyond these limits are exported but were not visible).

A 64 x 64 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -500 to 500, y -500 to 500 (lower origin).
Colour map mb (Normalize), limits 0 to 1; no colour bar.

### `control_object_lines.csv` (7.3 KB)

From the subplot "Control Object" (row 1, column 3 of the panel's subplots, 5.51-6.13 in across and 1.12-1.94 in down the page); y axis "Time near stimulus (min)"; drawn over x -0.5 to 1.5, y 0 to 13.481635 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Object" at 1.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `Time near stimulus (min)` | y position on the axis labelled "Time near stimulus (min)" (unit: min) |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `category` | the category named by the nearest x tick label |

Line styles: 88 lines: colour #cccccc, width 0.5 pt; 3 lines: colour #262626, width 0.5 pt

### `control_object_points.csv` (6.9 KB)

From the subplot "Control Object" (row 1, column 3 of the panel's subplots, 5.51-6.13 in across and 1.12-1.94 in down the page); y axis "Time near stimulus (min)"; drawn over x -0.5 to 1.5, y 0 to 13.481635 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Object" at 1.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position; this axis carries no label; the plotted, jittered position |
| `Time near stimulus (min)` | y position on the axis labelled "Time near stimulus (min)" (unit: min) |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

Every marker has an area of 6 pt^2.

### `tablet_points.csv` (26 B)

From the subplot "Tablet" (row 1, column 8 of the panel's subplots, 6.25-6.99 in across and 1.16-1.90 in down the page), under the page text "Tablet"; no axis labels; drawn over x -500 to 500, y -500 to 500 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |

Every marker has an area of 8.490396 pt^2.
Every marker is filled #33b259.

### `tablet_map.csv` (43.1 KB)

From the subplot "Tablet" (row 1, column 8 of the panel's subplots, 6.25-6.99 in across and 1.16-1.90 in down the page), under the page text "Tablet"; no axis labels; drawn over x -500 to 500, y -500 to 500 (values beyond these limits are exported but were not visible).

A 64 x 64 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -500 to 500, y -500 to 500 (lower origin).
Colour map mb (Normalize), limits 0 to 1; no colour bar.

### `control_tablet_lines.csv` (5.6 KB)

From the subplot "Control Tablet" (row 1, column 4 of the panel's subplots, 7.41-8.03 in across and 1.12-1.94 in down the page); y axis "Time near stimulus (min)"; drawn over x -0.5 to 1.5, y 0 to 31.339776 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Tablet" at 1.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `Time near stimulus (min)` | y position on the axis labelled "Time near stimulus (min)" (unit: min) |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `category` | the category named by the nearest x tick label |

Line styles: 68 lines: colour #cccccc, width 0.5 pt; 3 lines: colour #262626, width 0.5 pt

### `control_tablet_points.csv` (5.3 KB)

From the subplot "Control Tablet" (row 1, column 4 of the panel's subplots, 7.41-8.03 in across and 1.12-1.94 in down the page); y axis "Time near stimulus (min)"; drawn over x -0.5 to 1.5, y 0 to 31.339776 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Tablet" at 1.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position; this axis carries no label; the plotted, jittered position |
| `Time near stimulus (min)` | y position on the axis labelled "Time near stimulus (min)" (unit: min) |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

Every marker has an area of 6 pt^2.

### `noise_points.csv` (25 B)

From the subplot "Noise" (row 2, column 5 of the panel's subplots, 0.53-1.27 in across and 2.49-3.23 in down the page), under the page text "Noise"; no axis labels; drawn over x -500 to 500, y -500 to 500 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |

Every marker has an area of 8.490396 pt^2.
Every marker is filled #33b259.

### `noise_map.csv` (43.9 KB)

From the subplot "Noise" (row 2, column 5 of the panel's subplots, 0.53-1.27 in across and 2.49-3.23 in down the page), under the page text "Noise"; no axis labels; drawn over x -500 to 500, y -500 to 500 (values beyond these limits are exported but were not visible).

A 64 x 64 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -500 to 500, y -500 to 500 (lower origin).
Colour map mb (Normalize), limits 0 to 1; no colour bar.

### `control_noise_lines.csv` (7.3 KB)

From the subplot "Control Noise" (row 2, column 1 of the panel's subplots, 1.69-2.31 in across and 2.45-3.27 in down the page); y axis "Time near stimulus (min)"; drawn over x -0.5 to 1.5, y 0 to 28.631062 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Noise" at 1.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `Time near stimulus (min)` | y position on the axis labelled "Time near stimulus (min)" (unit: min) |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `category` | the category named by the nearest x tick label |

Line styles: 90 lines: colour #cccccc, width 0.5 pt; 3 lines: colour #262626, width 0.5 pt

### `control_noise_points.csv` (7.0 KB)

From the subplot "Control Noise" (row 2, column 1 of the panel's subplots, 1.69-2.31 in across and 2.45-3.27 in down the page); y axis "Time near stimulus (min)"; drawn over x -0.5 to 1.5, y 0 to 28.631062 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Noise" at 1.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position; this axis carries no label; the plotted, jittered position |
| `Time near stimulus (min)` | y position on the axis labelled "Time near stimulus (min)" (unit: min) |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

Every marker has an area of 6 pt^2.

### `toys_points.csv` (25 B)

From the subplot "Toys" (row 2, column 6 of the panel's subplots, 2.44-3.18 in across and 2.49-3.23 in down the page), under the page text "Toys"; no axis labels; drawn over x -500 to 500, y -500 to 500 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |

Every marker has an area of 8.490396 pt^2.
Every marker is filled #33b259.

### `toys_map.csv` (44.8 KB)

From the subplot "Toys" (row 2, column 6 of the panel's subplots, 2.44-3.18 in across and 2.49-3.23 in down the page), under the page text "Toys"; no axis labels; drawn over x -500 to 500, y -500 to 500 (values beyond these limits are exported but were not visible).

A 64 x 64 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -500 to 500, y -500 to 500 (lower origin).
Colour map mb (Normalize), limits 0 to 1; no colour bar.

### `control_toys_lines.csv` (6.6 KB)

From the subplot "Control Toys" (row 2, column 2 of the panel's subplots, 3.60-4.22 in across and 2.45-3.27 in down the page); y axis "Time near stimulus (min)"; drawn over x -0.5 to 1.5, y 0 to 14.463264 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Toys" at 1.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `Time near stimulus (min)` | y position on the axis labelled "Time near stimulus (min)" (unit: min) |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `category` | the category named by the nearest x tick label |

Line styles: 82 lines: colour #cccccc, width 0.5 pt; 3 lines: colour #262626, width 0.5 pt

### `control_toys_points.csv` (6.3 KB)

From the subplot "Control Toys" (row 2, column 2 of the panel's subplots, 3.60-4.22 in across and 2.45-3.27 in down the page); y axis "Time near stimulus (min)"; drawn over x -0.5 to 1.5, y 0 to 14.463264 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Toys" at 1.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position; this axis carries no label; the plotted, jittered position |
| `Time near stimulus (min)` | y position on the axis labelled "Time near stimulus (min)" (unit: min) |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

Every marker has an area of 6 pt^2.

### `intruder_points.csv` (24 B)

From the subplot "Intruder" (row 2, column 7 of the panel's subplots, 4.35-5.09 in across and 2.49-3.23 in down the page), under the page text "Intruder"; no axis labels; drawn over x -500 to 500, y -500 to 500 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |

Every marker has an area of 8.490396 pt^2.
Every marker is filled #33b259.

### `intruder_map.csv` (43.3 KB)

From the subplot "Intruder" (row 2, column 7 of the panel's subplots, 4.35-5.09 in across and 2.49-3.23 in down the page), under the page text "Intruder"; no axis labels; drawn over x -500 to 500, y -500 to 500 (values beyond these limits are exported but were not visible).

A 64 x 64 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -500 to 500, y -500 to 500 (lower origin).
Colour map mb (Normalize), limits 0 to 1; no colour bar.

### `control_intruder_lines.csv` (7.6 KB)

From the subplot "Control Intruder" (row 2, column 3 of the panel's subplots, 5.51-6.13 in across and 2.45-3.27 in down the page); y axis "Time near stimulus (min)"; drawn over x -0.5 to 1.5, y 0 to 13.062912 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Intruder" at 1.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `Time near stimulus (min)` | y position on the axis labelled "Time near stimulus (min)" (unit: min) |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `category` | the category named by the nearest x tick label |

Line styles: 90 lines: colour #cccccc, width 0.5 pt; 3 lines: colour #262626, width 0.5 pt

### `control_intruder_points.csv` (7.2 KB)

From the subplot "Control Intruder" (row 2, column 3 of the panel's subplots, 5.51-6.13 in across and 2.45-3.27 in down the page); y axis "Time near stimulus (min)"; drawn over x -0.5 to 1.5, y 0 to 13.062912 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Intruder" at 1.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position; this axis carries no label; the plotted, jittered position |
| `Time near stimulus (min)` | y position on the axis labelled "Time near stimulus (min)" (unit: min) |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

Every marker has an area of 6 pt^2.

### `mask_points.csv` (26 B)

From the subplot "Mask" (row 2, column 8 of the panel's subplots, 6.25-6.99 in across and 2.49-3.23 in down the page), under the page text "Mask"; no axis labels; drawn over x -500 to 500, y -500 to 500 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |

Every marker has an area of 8.490396 pt^2.
Every marker is filled #33b259.

### `mask_map.csv` (45.3 KB)

From the subplot "Mask" (row 2, column 8 of the panel's subplots, 6.25-6.99 in across and 2.49-3.23 in down the page), under the page text "Mask"; no axis labels; drawn over x -500 to 500, y -500 to 500 (values beyond these limits are exported but were not visible).

A 64 x 64 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -500 to 500, y -500 to 500 (lower origin).
Colour map mb (Normalize), limits 0 to 1; no colour bar.

### `control_mask_lines.csv` (7.2 KB)

From the subplot "Control Mask" (row 2, column 4 of the panel's subplots, 7.41-8.03 in across and 2.45-3.27 in down the page); y axis "Time near stimulus (min)"; drawn over x -0.5 to 1.5, y 0 to 9.0698417 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Mask" at 1.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `Time near stimulus (min)` | y position on the axis labelled "Time near stimulus (min)" (unit: min) |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `category` | the category named by the nearest x tick label |

Line styles: 92 lines: colour #cccccc, width 0.5 pt; 3 lines: colour #262626, width 0.5 pt

### `control_mask_points.csv` (6.9 KB)

From the subplot "Control Mask" (row 2, column 4 of the panel's subplots, 7.41-8.03 in across and 2.45-3.27 in down the page); y axis "Time near stimulus (min)"; drawn over x -0.5 to 1.5, y 0 to 9.0698417 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Mask" at 1.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position; this axis carries no label; the plotted, jittered position |
| `Time near stimulus (min)` | y position on the axis labelled "Time near stimulus (min)" (unit: min) |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

Every marker has an area of 6 pt^2.

### `page_shapes.csv` (63 B)

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

### `annotations.csv` (692 B)

Every text printed in the panel: inside a subplot (x and y in that subplot's data coordinates; for an annotation with a leader line, the point it marks in `target x` and `target y`) or on the page around the subplots (x and y in inches from the page's top-left: the text's anchor).

| Column | Meaning |
|---|---|
| `subplot` | the subplot the text is in; blank for page text |
| `text` | the text as printed, on one line |
| `x`, `y` | its position (see `coordinates`) |
| `coordinates` | "data" or "page inches" |

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- decoration: the dashed cage wireframe: 40 Line2D

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| AxesImage | 8 | 8 |
| Line2D | 753 | 713 |
| PathCollection | 24 | 24 |
| Text | 8 | 8 |
| Line2D (on the page) | 1 | 1 |
