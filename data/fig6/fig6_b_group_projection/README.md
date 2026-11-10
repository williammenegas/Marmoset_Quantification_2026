# fig6_b_group_projection

Figure 6, panel b. No title is printed on this panel.

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, and photographs and video frames as PNG.

- Redrawn from this folder alone by [`code/fig6/fig6_b_group_projection.py`](../../../code/fig6/fig6_b_group_projection.py).

## Files

### `projection_on_the_group_response_lines.csv` (78 B)

From the subplot "Projection on the group response" (row 1, column 1 of the panel's subplots, 0.89-8.07 in across and 3.33-4.84 in down the page); y axis "Projection on the group response"; drawn over x -0.6 to 8.6, y -0.031075608 to 0.089353632 (values beyond these limits are exported but were not visible); its x axis prints "Box" at 0, "Face" at 1, "Intruder" at 2, "Mask" at 3, "Treat" at 4, "Toys" at 5, "Noise" at 6, "Object" at 7, "Control" at 8.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `Projection on the group response` | y position on the axis labelled "Projection on the group response" |
| `category` | the category named by the nearest x tick label |

Line styles: 1 line: colour #e0e0e0, width 0.5 pt

### `projection_on_the_group_response_points.csv` (33.9 KB)

From the subplot "Projection on the group response" (row 1, column 1 of the panel's subplots, 0.89-8.07 in across and 3.33-4.84 in down the page); y axis "Projection on the group response"; drawn over x -0.6 to 8.6, y -0.031075608 to 0.089353632 (values beyond these limits are exported but were not visible); its x axis prints "Box" at 0, "Face" at 1, "Intruder" at 2, "Mask" at 3, "Treat" at 4, "Toys" at 5, "Noise" at 6, "Object" at 7, "Control" at 8.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position; this axis carries no label; the plotted, jittered position |
| `Projection on the group response` | y position on the axis labelled "Projection on the group response" |
| `marker area (pt^2)` | the marker's area, points squared |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- nothing else

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| Line2D | 1 | 1 |
| PathCollection | 18 | 18 |
