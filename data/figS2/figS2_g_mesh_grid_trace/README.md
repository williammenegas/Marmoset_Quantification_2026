# figS2_g_mesh_grid_trace

Figure S2, panel g. No title is printed on this panel.

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, and photographs and video frames as PNG.

- Redrawn from this folder alone by [`code/figS2/figS2_g_mesh_grid_trace.py`](../../../code/figS2/figS2_g_mesh_grid_trace.py).

## Files

### `mesh_points_sorted_vs_time_min_lines.csv` (889 B)

From the subplot "Mesh points (sorted) vs Time (min)" (row 2, column 1 of the panel's subplots, 3.94-7.35 in across and 4.79-5.55 in down the page); x axis "Time (min)"; y axis "Mesh points (sorted)"; drawn over x 0 to 30, y 0 to 375 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (min)` | x position on the axis labelled "Time (min)" (unit: min) |
| `Mesh points (sorted)` | y position on the axis labelled "Mesh points (sorted)" |

Line styles: 28 lines: colour #ffffff, width 0.5 pt, dashed

### `mesh_points_sorted_vs_time_min_map.csv` (6.7 MB)

From the subplot "Mesh points (sorted) vs Time (min)" (row 2, column 1 of the panel's subplots, 3.94-7.35 in across and 4.79-5.55 in down the page); x axis "Time (min)"; y axis "Mesh points (sorted)"; drawn over x 0 to 30, y 0 to 375 (values beyond these limits are exported but were not visible).

A 375 x 1800 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `Mesh points (sorted) \ Time (min)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `Depth (a.u.)` | every other cell: the image cell's value |

Image extent: x 0 to 30, y 0 to 375 (lower origin).
Colour map inferno (Normalize), limits 25 to 175, colour bar "Depth (a.u.)".

### `time_min_boxes.csv` (371 B)

From the subplot "Time (min)" (row 1, column 1 of the panel's subplots, 3.94-7.35 in across and 4.73-4.76 in down the page); x axis "Time (min)"; drawn over x 0 to 30, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (min) left` | x of the box's left edge on the axis labelled "Time (min)" (unit: min) |
| `Time (min) right` | x of the box's right edge on the axis labelled "Time (min)" (unit: min) |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |

Filled: yes.
Every box's fill: #262626.
Every box's outline: none.

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- colour bar (its label and limits are given with the data it keys): 1 LineCollection, 1 QuadMesh

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| AxesImage | 1 | 1 |
| Line2D | 28 | 28 |
| LineCollection | 1 | 0 |
| QuadMesh | 1 | 0 |
| Rectangle | 14 | 14 |
