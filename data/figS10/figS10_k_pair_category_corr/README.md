# figS10_k_pair_category_corr

Figure S10, panel k. No title is printed on this panel.

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS10/figS10_k_pair_category_corr.py`](../../../code/figS10/figS10_k_pair_category_corr.py).

## Files

### `spearman_rho_vs_call_rate_lines.csv` (418 B)

From the subplot "Spearman rho vs call rate" (row 1, column 1 of the panel's subplots, 3.72-5.36 in across and 6.43-7.63 in down the page); y axis "Spearman rho vs call rate"; drawn over x -0.40428571 to 4.3414286, y -0.53836877 to 0.63065 (values beyond these limits are exported but were not visible); its x axis prints "Climb" at 0, "Active" at 1, "Alone" at 2, "Soc-act" at 3, "Soc-rest" at 4.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `Spearman rho vs call rate` | y position on the axis labelled "Spearman rho vs call rate" |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `category` | the category named by the nearest x tick label |

Line styles: 1 line: colour #6662d7, width 0.9 pt; 1 line: colour #a85fba, width 0.9 pt; 1 line: colour #f05c9b, width 0.9 pt; 1 line: colour #fb8d7b, width 0.9 pt; 1 line: colour #fec15d, width 0.9 pt; 1 line: colour #e0e0e0, width 0.5 pt

### `spearman_rho_vs_call_rate_points.csv` (13.7 KB)

From the subplot "Spearman rho vs call rate" (row 1, column 1 of the panel's subplots, 3.72-5.36 in across and 6.43-7.63 in down the page); y axis "Spearman rho vs call rate"; drawn over x -0.40428571 to 4.3414286, y -0.53836877 to 0.63065 (values beyond these limits are exported but were not visible); its x axis prints "Climb" at 0, "Active" at 1, "Alone" at 2, "Soc-act" at 3, "Soc-rest" at 4.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position; this axis carries no label; the plotted, jittered position |
| `Spearman rho vs call rate` | y position on the axis labelled "Spearman rho vs call rate" |
| `marker area (pt^2)` | the marker's area, points squared |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

### `annotations.csv` (99 B)

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
| Line2D | 6 | 6 |
| PathCollection | 10 | 10 |
| Text | 1 | 1 |
