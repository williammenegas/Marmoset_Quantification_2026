# figS2_f_mesh_grid

Figure S2, panel f. Title: "Mesh grid".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS2/figS2_f_mesh_grid.py`](../../../code/figS2/figS2_f_mesh_grid.py).

The photograph beside the plot is artwork pasted in Illustrator; not drawn by code.

## Files

### `depth_a_u_vs_mesh_points_sorted_lines.csv` (7.0 KB)

From the subplot "Depth (a.u.) vs Mesh points (sorted)" (row 1, column 1 of the panel's subplots, 2.47-3.28 in across and 4.68-5.53 in down the page); x axis "Mesh points (sorted)"; y axis "Depth (a.u.)"; drawn over x 0 to 375, y 0 to 250 (values beyond these limits are exported but were not visible).

One row is one x value shared by the lines; one column per line.

| Column | Meaning |
|---|---|
| `Mesh points (sorted)` | x position on the axis labelled "Mesh points (sorted)" |
| `Other (769)` | the line "Other (769)": y position on the axis labelled "Depth (a.u.)" (unit: a.u.) |
| `Climbing (737)` | the line "Climbing (737)": y position on the axis labelled "Depth (a.u.)" (unit: a.u.) |

Lines: "Other (769)": colour #737373, width 1 pt; "Climbing (737)": colour #6662d7, width 1 pt

### `depth_a_u_vs_mesh_points_sorted_shapes.csv` (37.6 KB)

From the subplot "Depth (a.u.) vs Mesh points (sorted)" (row 1, column 1 of the panel's subplots, 2.47-3.28 in across and 4.68-5.53 in down the page); x axis "Mesh points (sorted)"; y axis "Depth (a.u.)"; drawn over x 0 to 375, y 0 to 250 (values beyond these limits are exported but were not visible).

One row is one vertex of one shape's outline, curves sampled.

| Column | Meaning |
|---|---|
| `shape` | which shape, numbered from 1 in drawing order |
| `vertex` | the vertex's place along the outline |
| `Mesh points (sorted)` | x position on the axis labelled "Mesh points (sorted)" |
| `Depth (a.u.)` | y position on the axis labelled "Depth (a.u.)" (unit: a.u.) |
| `fill colour` | the shape's fill colour, hex RGB |

Drawn as: FillBetweenPolyCollection.
Every shape's outline: none.

### `annotations.csv` (65 B)

Every text printed in the panel: inside a subplot (x and y in that subplot's data coordinates; for an annotation with a leader line, the point it marks in `target x` and `target y`) or on the page around the subplots (x and y in inches from the page's top-left: the text's anchor).

| Column | Meaning |
|---|---|
| `subplot` | the subplot the text is in; blank for page text |
| `text` | the text as printed, on one line |
| `x`, `y` | its position (see `coordinates`) |
| `coordinates` | "data" or "page inches" |

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- legend: 1 Legend

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| FillBetweenPolyCollection | 2 | 2 |
| Legend | 1 | 0 |
| Line2D | 2 | 2 |
