# figS12_f_projection_vs_control

Figure S12, panel f. No title is printed on this panel.

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS12/figS12_f_projection_vs_control.py`](../../../code/figS12/figS12_f_projection_vs_control.py).

## Files

### `projection_on_the_lines.csv` (275 B)

From the subplot "Projection on the" (row 1, column 1 of the panel's subplots, 5.37-7.07 in across and 5.64-6.69 in down the page), marked "AUROC 0.993" inside; y axis "Projection on the group response"; drawn over x -0.5 to 1.5, y -0.0078480644 to 0.088247558 (values beyond these limits are exported but were not visible); its x axis prints "Held-out control" at 0, "Tablet" at 1.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `Projection on the group response` | y position on the axis labelled "Projection on the group response" |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `category` | the category named by the nearest x tick label |

Line styles: 1 line: colour #e0e0e0, width 0.5 pt; 2 lines: colour #000000, width 0.9 pt

### `projection_on_the_points.csv` (6.5 KB)

From the subplot "Projection on the" (row 1, column 1 of the panel's subplots, 5.37-7.07 in across and 5.64-6.69 in down the page), marked "AUROC 0.993" inside; y axis "Projection on the group response"; drawn over x -0.5 to 1.5, y -0.0078480644 to 0.088247558 (values beyond these limits are exported but were not visible); its x axis prints "Held-out control" at 0, "Tablet" at 1.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position; this axis carries no label; the plotted, jittered position |
| `Projection on the group response` | y position on the axis labelled "Projection on the group response" |
| `marker area (pt^2)` | the marker's area, points squared |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

### `annotations.csv` (130 B)

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
| Line2D | 3 | 3 |
| PathCollection | 4 | 4 |
| Text | 2 | 2 |
