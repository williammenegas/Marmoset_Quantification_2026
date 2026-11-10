# figS7_b_pca_variance

Figure S7, panel b. Title: "PCA across sessions".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS7/figS7_b_pca_variance.py`](../../../code/figS7/figS7_b_pca_variance.py).

## Files

### `pca_across_sessions_lines.csv` (73 B)

From the subplot "PCA across sessions" (row 1, column 1 of the panel's subplots, 3.20-4.67 in across and 1.35-3.31 in down the page), under the page text "PCA across sessions", marked "PC 1" inside; x axis "Component #"; y axis "Variance explained (%)"; drawn over x 0.2 to 30.8, y 0 to 30 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Component #` | x position on the axis labelled "Component #" |
| `Variance explained (%)` | y position on the axis labelled "Variance explained (%)" (unit: %) |

Line styles: 1 line: colour #262626, width 0.6 pt

### `pca_across_sessions_bars.csv` (655 B)

From the subplot "PCA across sessions" (row 1, column 1 of the panel's subplots, 3.20-4.67 in across and 1.35-3.31 in down the page), under the page text "PCA across sessions", marked "PC 1" inside; x axis "Component #"; y axis "Variance explained (%)"; drawn over x 0.2 to 30.8, y 0 to 30 (values beyond these limits are exported but were not visible).

One row is one vertical bar.

| Column | Meaning |
|---|---|
| `Component #` | x of the bar's centre on the axis labelled "Component #" |
| `bar width` | the bar's width, in x units |
| `bar bottom` | where the bar starts, in y units |
| `Variance explained (%)` | the bar's height: y extent on the axis labelled "Variance explained (%)" (unit: %) |

Every bar is filled: #737373.

### `annotations.csv` (123 B)

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
| Rectangle | 30 | 30 |
| Text | 1 | 1 |
