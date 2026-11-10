# fig5_e_state_corr

Figure 5, panel e. Title: "State correlation (Control)", "State correlation (Tablet)".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig5/fig5_e_state_corr.py`](../../../code/fig5/fig5_e_state_corr.py).

## Files

### `correlation_vs_behavioral_state_1_lines.csv` (54 B)

From the subplot "Correlation vs Behavioral state # 1" (row 1, column 1 of the panel's subplots, 0.78-2.28 in across and 6.12-7.24 in down the page); x axis "Behavioral state #"; y axis "Correlation"; drawn over x -0.5 to 81.5, y -0.36868393 to 0.36868393 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Behavioral state #` | x position on the axis labelled "Behavioral state #" |
| `Correlation` | y position on the axis labelled "Correlation" |

Line styles: 1 line: colour #262626, width 0.5 pt

### `correlation_vs_behavioral_state_1_bars.csv` (1.8 KB)

From the subplot "Correlation vs Behavioral state # 1" (row 1, column 1 of the panel's subplots, 0.78-2.28 in across and 6.12-7.24 in down the page); x axis "Behavioral state #"; y axis "Correlation"; drawn over x -0.5 to 81.5, y -0.36868393 to 0.36868393 (values beyond these limits are exported but were not visible).

One row is one vertical bar.

| Column | Meaning |
|---|---|
| `Behavioral state #` | x of the bar's centre on the axis labelled "Behavioral state #" |
| `bar width` | the bar's width, in x units |
| `bar bottom` | where the bar starts, in y units |
| `Correlation` | the bar's height: y extent on the axis labelled "Correlation" |

Every bar is filled: #76b5a0.

### `correlation_vs_behavioral_state_2_lines.csv` (54 B)

From the subplot "Correlation vs Behavioral state # 2" (row 1, column 2 of the panel's subplots, 2.58-4.08 in across and 6.12-7.24 in down the page); x axis "Behavioral state #"; y axis "Correlation"; drawn over x -0.5 to 81.5, y -0.36868393 to 0.36868393 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Behavioral state #` | x position on the axis labelled "Behavioral state #" |
| `Correlation` | y position on the axis labelled "Correlation" |

Line styles: 1 line: colour #262626, width 0.5 pt

### `correlation_vs_behavioral_state_2_bars.csv` (1.8 KB)

From the subplot "Correlation vs Behavioral state # 2" (row 1, column 2 of the panel's subplots, 2.58-4.08 in across and 6.12-7.24 in down the page); x axis "Behavioral state #"; y axis "Correlation"; drawn over x -0.5 to 81.5, y -0.36868393 to 0.36868393 (values beyond these limits are exported but were not visible).

One row is one vertical bar.

| Column | Meaning |
|---|---|
| `Behavioral state #` | x of the bar's centre on the axis labelled "Behavioral state #" |
| `bar width` | the bar's width, in x units |
| `bar bottom` | where the bar starts, in y units |
| `Correlation` | the bar's height: y extent on the axis labelled "Correlation" |

Every bar is filled: #c98ecf.

### `annotations.csv` (198 B)

Every text printed in the panel: inside a subplot (x and y in that subplot's data coordinates; for an annotation with a leader line, the point it marks in `target x` and `target y`) or on the page around the subplots (x and y in inches from the page's top-left: the text's anchor).

| Column | Meaning |
|---|---|
| `subplot` | the subplot the text is in; blank for page text |
| `text` | the text as printed, on one line |
| `x`, `y` | its position (see `coordinates`) |
| `coordinates` | "data" or "page inches" |

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- decoration: the dashed category boundaries: 10 Line2D

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| AnchoredOffsetbox | 2 | 2 |
| Line2D | 12 | 2 |
| Rectangle | 160 | 160 |
