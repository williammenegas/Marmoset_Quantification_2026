# fig7_h_composite_halves

Figure 7, panel h. Title: "Split per animal".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig7/fig7_h_composite_halves.py`](../../../code/fig7/fig7_h_composite_halves.py).

## Files

### `split_per_animal_lines.csv` (5.8 KB)

From the subplot "Split per animal" (row 1, column 1 of the panel's subplots, 3.30-5.24 in across and 6.05-7.51 in down the page), under the page text "Split per animal"; x axis "Group 1 composite"; y axis "Group 2 composite"; z axis "Group 3 composite"; drawn over x -3 to 3, y -3 to 3, z -3 to 3 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Group 1 composite` | x position on the axis labelled "Group 1 composite" |
| `Group 2 composite` | y position on the axis labelled "Group 2 composite" |
| `Group 3 composite` | z position on the axis labelled "Group 3 composite" |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |

Line styles: 19 lines: colour #81baa4, width 0.6 pt; 22 lines: colour #b193cf, width 0.6 pt; 23 lines: colour #debe7d, width 0.6 pt

### `split_per_animal_points.csv` (5.3 KB)

From the subplot "Split per animal" (row 1, column 1 of the panel's subplots, 3.30-5.24 in across and 6.05-7.51 in down the page), under the page text "Split per animal"; x axis "Group 1 composite"; y axis "Group 2 composite"; z axis "Group 3 composite"; drawn over x -3 to 3, y -3 to 3, z -3 to 3 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `Group 1 composite` | x position on the axis labelled "Group 1 composite" |
| `Group 2 composite` | y position on the axis labelled "Group 2 composite" |
| `Group 3 composite` | z position on the axis labelled "Group 3 composite" |
| `colour` | the marker's fill colour, hex RGB |

Every marker has an area of 4.5 pt^2.

### `annotations.csv` (70 B)

Every text printed in the panel: inside a subplot (x and y in that subplot's data coordinates; for an annotation with a leader line, the point it marks in `target x` and `target y`) or on the page around the subplots (x and y in inches from the page's top-left: the text's anchor).

| Column | Meaning |
|---|---|
| `subplot` | the subplot the text is in; blank for page text |
| `text` | the text as printed, on one line |
| `x`, `y` | its position (see `coordinates`) |
| `coordinates` | "data" or "page inches" |

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- nothing else

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| Line3D | 64 | 64 |
| Path3DCollection | 6 | 6 |
