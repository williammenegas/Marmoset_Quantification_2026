# fig6_d_heldout_projection

Figure 6, panel d. No title is printed on this panel.

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, and photographs and video frames as PNG.

- Redrawn from this folder alone by [`code/fig6/fig6_d_heldout_projection.py`](../../../code/fig6/fig6_d_heldout_projection.py).

## Files

### `projection_lines.csv` (1.2 KB)

From the subplot "Projection" (row 1, column 1 of the panel's subplots, 3.54-6.01 in across and 5.32-6.78 in down the page); y axis "Projection (grey = held-out control)"; drawn over x -0.6 to 7.6, y -1.6788667 to 1.1275651 (values beyond these limits are exported but were not visible); its x axis prints "Box" at 0, "Face" at 1, "Intruder" at 2, "Mask" at 3, "Treat" at 4, "Toys" at 5, "Noise" at 6, "Object" at 7.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `Projection (grey = held-out control)` | y position on the axis labelled "Projection (grey = held-out control)" |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `category` | the category named by the nearest x tick label |

Line styles: 16 lines: colour #000000, width 0.9 pt; 1 line: colour #262626, width 0.5 pt, dashed

### `projection_points.csv` (54.0 KB)

From the subplot "Projection" (row 1, column 1 of the panel's subplots, 3.54-6.01 in across and 5.32-6.78 in down the page); y axis "Projection (grey = held-out control)"; drawn over x -0.6 to 7.6, y -1.6788667 to 1.1275651 (values beyond these limits are exported but were not visible); its x axis prints "Box" at 0, "Face" at 1, "Intruder" at 2, "Mask" at 3, "Treat" at 4, "Toys" at 5, "Noise" at 6, "Object" at 7.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position; this axis carries no label; the plotted, jittered position |
| `Projection (grey = held-out control)` | y position on the axis labelled "Projection (grey = held-out control)" |
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
| Line2D | 17 | 17 |
| PathCollection | 32 | 32 |
