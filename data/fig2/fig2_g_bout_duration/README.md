# fig2_g_bout_duration

Figure 2, panel g. Title: "Mean bout duration".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig2/fig2_g_bout_duration.py`](../../../code/fig2/fig2_g_bout_duration.py).

## Files

### `mean_bout_duration_lines.csv` (365 B)

From the subplot "Mean bout duration" (row 1, column 1 of the panel's subplots, 6.19-7.90 in across and 3.65-4.62 in down the page), under the page text "Mean bout duration"; x axis "# clusters"; y axis "Mean bout duration (s)"; drawn over x -0.5 to 4.5, y 0.28105 to 10.090587 (values beyond these limits are exported but were not visible); its x axis prints "4" at 0, "10" at 1, "18" at 2, "30" at 3, "80" at 4.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `# clusters` | x position on the axis labelled "# clusters" |
| `Mean bout duration (s)` | y position on the axis labelled "Mean bout duration (s)" (unit: s) |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |

Line styles: 5 lines: colour #262626, width 1.2 pt; 1 line: colour #1f77b4, width 1.5 pt, no line, marker 'o' 3 pt, filled #262626, edged #262626; 1 line: colour #ff7f0e, width 1.5 pt, no line, marker 'o' 3 pt, filled #262626, edged #262626; 1 line: colour #2ca02c, width 1.5 pt, no line, marker 'o' 3 pt, filled #262626, edged #262626; 1 line: colour #d62728, width 1.5 pt, no line, marker 'o' 3 pt, filled #262626, edged #262626; 1 line: colour #9467bd, width 1.5 pt, no line, marker 'o' 3 pt, filled #262626, edged #262626

### `mean_bout_duration_points.csv` (8.9 KB)

From the subplot "Mean bout duration" (row 1, column 1 of the panel's subplots, 6.19-7.90 in across and 3.65-4.62 in down the page), under the page text "Mean bout duration"; x axis "# clusters"; y axis "Mean bout duration (s)"; drawn over x -0.5 to 4.5, y 0.28105 to 10.090587 (values beyond these limits are exported but were not visible); its x axis prints "4" at 0, "10" at 1, "18" at 2, "30" at 3, "80" at 4.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `# clusters` | x position on the axis labelled "# clusters" |
| `Mean bout duration (s)` | y position on the axis labelled "Mean bout duration (s)" (unit: s) |

Every marker has an area of 5 pt^2.
Every marker is filled #c2c7cfcc.

### `annotations.csv` (75 B)

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
| Line2D | 10 | 10 |
| PathCollection | 5 | 5 |
