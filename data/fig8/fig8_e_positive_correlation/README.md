# fig8_e_positive_correlation

Figure 8, panel e. Title: "Example: positive correlation".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig8/fig8_e_positive_correlation.py`](../../../code/fig8/fig8_e_positive_correlation.py).

## Files

### `example_positive_correlation_lines.csv` (145 B)

From the subplot "Example: positive correlation" (row 1, column 1 of the panel's subplots, 1.00-2.31 in across and 5.21-6.52 in down the page), under the page text "Example: positive correlation"; x axis "B1: Social vs climbing (z)"; y axis "S2: Treat approach (z)"; drawn over x -3.5 to 3.5, y -3.5 to 3.5 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `B1: Social vs climbing (z)` | x position on the axis labelled "B1: Social vs climbing (z)" |
| `S2: Treat approach (z)` | y position on the axis labelled "S2: Treat approach (z)" |

Line styles: 2 lines: colour #231f20, width 0.5 pt; 1 line: colour #231f20, width 0.5 pt, dashed

### `example_positive_correlation_points.csv` (4.2 KB)

From the subplot "Example: positive correlation" (row 1, column 1 of the panel's subplots, 1.00-2.31 in across and 5.21-6.52 in down the page), under the page text "Example: positive correlation"; x axis "B1: Social vs climbing (z)"; y axis "S2: Treat approach (z)"; drawn over x -3.5 to 3.5, y -3.5 to 3.5 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `B1: Social vs climbing (z)` | x position on the axis labelled "B1: Social vs climbing (z)" |
| `S2: Treat approach (z)` | y position on the axis labelled "S2: Treat approach (z)" |
| `colour` | the marker's fill colour, hex RGB |

Every marker has an area of 11.943936 pt^2.

### `annotations.csv` (164 B)

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
| PathCollection | 2 | 2 |
