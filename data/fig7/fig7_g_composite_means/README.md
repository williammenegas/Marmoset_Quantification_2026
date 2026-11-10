# fig7_g_composite_means

Figure 7, panel g. Title: "Total score per animal".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig7/fig7_g_composite_means.py`](../../../code/fig7/fig7_g_composite_means.py).

## Files

### `total_score_per_animal_lines.csv` (272 B)

From the subplot "Total score per animal" (row 1, column 1 of the panel's subplots, 0.67-2.61 in across and 6.05-7.51 in down the page), under the page text "Total score per animal"; x axis "Group 1 composite"; y axis "Group 2 composite"; z axis "Group 3 composite"; drawn over x -3 to 3, y -3 to 3, z -3 to 3 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Group 1 composite` | x position on the axis labelled "Group 1 composite" |
| `Group 2 composite` | y position on the axis labelled "Group 2 composite" |
| `Group 3 composite` | z position on the axis labelled "Group 3 composite" |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `marker fill` | the fill colour of the line's markers, hex RGB; blank where it draws none |
| `marker edge` | the outline colour of the line's markers, hex RGB; blank where it draws none |

Line styles: 1 line: colour #1f77b4, width 1.5 pt, no line, marker 'D' 2.91548 pt, filled #3e6556, edged #1f77b4; 1 line: colour #ff7f0e, width 1.5 pt, no line, marker 'D' 2.91548 pt, filled #5f4a73, edged #ff7f0e; 1 line: colour #2ca02c, width 1.5 pt, no line, marker 'D' 2.91548 pt, filled #7e683b, edged #2ca02c

### `total_score_per_animal_points.csv` (2.9 KB)

From the subplot "Total score per animal" (row 1, column 1 of the panel's subplots, 0.67-2.61 in across and 6.05-7.51 in down the page), under the page text "Total score per animal"; x axis "Group 1 composite"; y axis "Group 2 composite"; z axis "Group 3 composite"; drawn over x -3 to 3, y -3 to 3, z -3 to 3 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `Group 1 composite` | x position on the axis labelled "Group 1 composite" |
| `Group 2 composite` | y position on the axis labelled "Group 2 composite" |
| `Group 3 composite` | z position on the axis labelled "Group 3 composite" |
| `colour` | the marker's fill colour, hex RGB |

Every marker has an area of 8 pt^2.

### `annotations.csv` (78 B)

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
| Line3D | 3 | 3 |
| Path3DCollection | 3 | 3 |
