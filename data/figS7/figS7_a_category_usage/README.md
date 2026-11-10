# figS7_a_category_usage

Figure S7, panel a. Title: "State usage".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS7/figS7_a_category_usage.py`](../../../code/figS7/figS7_a_category_usage.py).

## Files

### `state_usage_lines.csv` (534 B)

From the subplot "State usage" (row 1, column 1 of the panel's subplots, 0.85-2.39 in across and 1.35-3.31 in down the page), under the page text "State usage"; x axis "State"; y axis "Fraction"; drawn over x -0.6 to 3.6, y 0 to 1 (values beyond these limits are exported but were not visible); its x axis prints "Climbing" at 0, "Active" at 1, "Social" at 2, "Alone" at 3.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `State` | x position on the axis labelled "State" |
| `Fraction` | y position on the axis labelled "Fraction" |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `category` | the category named by the nearest x tick label |

Line styles: 5 lines: colour #e0e0e0, width 0.6 pt, dashed; 1 line: colour #6662d7, width 0.9 pt; 1 line: colour #a85fba, width 0.9 pt; 1 line: colour #fb8d7b, width 0.9 pt; 1 line: colour #f05c9b, width 0.9 pt

### `state_usage_points.csv` (916.2 KB)

From the subplot "State usage" (row 1, column 1 of the panel's subplots, 0.85-2.39 in across and 1.35-3.31 in down the page), under the page text "State usage"; x axis "State"; y axis "Fraction"; drawn over x -0.6 to 3.6, y 0 to 1 (values beyond these limits are exported but were not visible); its x axis prints "Climbing" at 0, "Active" at 1, "Social" at 2, "Alone" at 3.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position on the axis labelled "State"; the plotted, jittered position |
| `Fraction` | y position on the axis labelled "Fraction" |
| `marker area (pt^2)` | the marker's area, points squared |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

### `annotations.csv` (119 B)

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
| Line2D | 9 | 9 |
| PathCollection | 8 | 8 |
| Text | 1 | 1 |
