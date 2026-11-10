# fig4_j_mean_state_corr

Figure 4, panel j. No title is printed on this panel.

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig4/fig4_j_mean_state_corr.py`](../../../code/fig4/fig4_j_mean_state_corr.py).

## Files

### `mean_rho_across_animals_vs_level_5_behavioral_state_lines.csv` (78 B)

From the subplot "Mean rho across animals vs Level-5 behavioral state" (row 1, column 1 of the panel's subplots, 4.18-5.53 in across and 5.55-6.65 in down the page); x axis "Level-5 behavioral state"; y axis "Mean rho across animals"; drawn over x -3.4175 to 84.4175, y -0.2281598 to 0.29660029 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Level-5 behavioral state` | x position on the axis labelled "Level-5 behavioral state" |
| `Mean rho across animals` | y position on the axis labelled "Mean rho across animals" |

Line styles: 1 line: colour #262626, width 0.6 pt

### `mean_rho_across_animals_vs_level_5_behavioral_state_bars.csv` (2.4 KB)

From the subplot "Mean rho across animals vs Level-5 behavioral state" (row 1, column 1 of the panel's subplots, 4.18-5.53 in across and 5.55-6.65 in down the page); x axis "Level-5 behavioral state"; y axis "Mean rho across animals"; drawn over x -3.4175 to 84.4175, y -0.2281598 to 0.29660029 (values beyond these limits are exported but were not visible).

One row is one vertical bar.

| Column | Meaning |
|---|---|
| `Level-5 behavioral state` | x of the bar's centre on the axis labelled "Level-5 behavioral state" |
| `bar width` | the bar's width, in x units |
| `bar bottom` | where the bar starts, in y units |
| `Mean rho across animals` | the bar's height: y extent on the axis labelled "Mean rho across animals" |
| `colour` | the bar's fill colour, hex RGB |

### `annotations.csv` (415 B)

Every text printed in the panel: inside a subplot (x and y in that subplot's data coordinates; for an annotation with a leader line, the point it marks in `target x` and `target y`) or on the page around the subplots (x and y in inches from the page's top-left: the text's anchor).

| Column | Meaning |
|---|---|
| `subplot` | the subplot the text is in; blank for page text |
| `text` | the text as printed, on one line |
| `x`, `y` | its position (see `coordinates`) |
| `coordinates` | "data" or "page inches" |
| `target x`, `target y` | the point an annotation's leader line marks, in data coordinates |

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- decoration: the dotted category boundaries: 3 Line2D

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| Annotation | 4 | 4 |
| Line2D | 4 | 1 |
| Rectangle | 80 | 80 |
