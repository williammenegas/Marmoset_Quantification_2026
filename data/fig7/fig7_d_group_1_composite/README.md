# fig7_d_group_1_composite

Figure 7, panel d. Title: "Group 1 composite".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig7/fig7_d_group_1_composite.py`](../../../code/fig7/fig7_d_group_1_composite.py).

## Files

### `group_1_composite_lines.csv` (51 B)

From the subplot "Group 1 composite" (row 1, column 1 of the panel's subplots, 0.72-1.72 in across and 4.41-5.41 in down the page), under the page text "Group 1 composite"; x axis "Half 1 (mean z)"; y axis "Half 2 (mean z)"; drawn over x -2 to 3, y -2 to 3 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Half 1 (mean z)` | x position on the axis labelled "Half 1 (mean z)" |
| `Half 2 (mean z)` | y position on the axis labelled "Half 2 (mean z)" |

Line styles: 1 line: colour #999999, width 0.5 pt, dashed

### `group_1_composite_points.csv` (2.1 KB)

From the subplot "Group 1 composite" (row 1, column 1 of the panel's subplots, 0.72-1.72 in across and 4.41-5.41 in down the page), under the page text "Group 1 composite"; x axis "Half 1 (mean z)"; y axis "Half 2 (mean z)"; drawn over x -2 to 3, y -2 to 3 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `Half 1 (mean z)` | x position on the axis labelled "Half 1 (mean z)" |
| `Half 2 (mean z)` | y position on the axis labelled "Half 2 (mean z)" |
| `colour` | the marker's fill colour, hex RGB |

Every marker has an area of 8 pt^2.

### `correlation_with_others_vs_features_bars.csv` (176 B)

From the subplot "Correlation with others vs Features" (row 1, column 2 of the panel's subplots, 2.23-2.58 in across and 4.44-5.27 in down the page); x axis "Features"; y axis "Correlation with others"; drawn over x 0.4444 to 3.5556, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one vertical bar.

| Column | Meaning |
|---|---|
| `Features` | x of the bar's centre on the axis labelled "Features" |
| `bar width` | the bar's width, in x units |
| `bar bottom` | where the bar starts, in y units |
| `Correlation with others` | the bar's height: y extent on the axis labelled "Correlation with others" |
| `name` | what the bar stands for, as the drawing code names it |

Every bar is filled: #90c2af.

### `annotations.csv` (115 B)

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
| Line2D | 1 | 1 |
| PathCollection | 3 | 3 |
| Rectangle | 3 | 3 |
| Text | 1 | 1 |
