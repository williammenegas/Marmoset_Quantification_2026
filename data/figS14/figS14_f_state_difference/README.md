# figS14_f_state_difference

Figure S14, panel f. No title is printed on this panel.

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS14/figS14_f_state_difference.py`](../../../code/figS14/figS14_f_state_difference.py).

## Files

### `relative_difference_vs_behavioral_state_lines.csv` (80 B)

From the subplot "Relative difference vs Behavioral state #" (row 1, column 1 of the panel's subplots, 4.87-8.05 in across and 5.14-6.21 in down the page); x axis "Behavioral state #"; y axis "Relative difference"; drawn over x 0.5 to 80.5, y -0.55 to 0.55 (values beyond these limits are exported but were not visible); its x axis prints "1-5" at 3, "6-28" at 17, "29-59" at 44, "60-80" at 70.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Behavioral state #` | x position on the axis labelled "Behavioral state #" |
| `Relative difference` | y position on the axis labelled "Relative difference" |
| `category` | the category named by the nearest x tick label |

Line styles: 1 line: colour #262626, width 0.5 pt

### `relative_difference_vs_behavioral_state_bars.csv` (2.9 KB)

From the subplot "Relative difference vs Behavioral state #" (row 1, column 1 of the panel's subplots, 4.87-8.05 in across and 5.14-6.21 in down the page); x axis "Behavioral state #"; y axis "Relative difference"; drawn over x 0.5 to 80.5, y -0.55 to 0.55 (values beyond these limits are exported but were not visible); its x axis prints "1-5" at 3, "6-28" at 17, "29-59" at 44, "60-80" at 70.

One row is one vertical bar.

| Column | Meaning |
|---|---|
| `Behavioral state #` | x of the bar's centre on the axis labelled "Behavioral state #" |
| `bar width` | the bar's width, in x units |
| `bar bottom` | where the bar starts, in y units |
| `Relative difference` | the bar's height: y extent on the axis labelled "Relative difference" |
| `colour` | the bar's fill colour, hex RGB |
| `category` | the category named by the nearest tick label |

### `annotations.csv` (351 B)

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
