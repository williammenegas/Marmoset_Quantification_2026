# fig5_c_state_usage

Figure 5, panel c. Title: "State usage (Control)", "State usage (Tablet)".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig5/fig5_c_state_usage.py`](../../../code/fig5/fig5_c_state_usage.py).

## Files

### `frequency_pct_vs_behavioral_state_1_bars.csv` (1.7 KB)

From the subplot "Frequency (%) vs Behavioral state # 1" (row 1, column 1 of the panel's subplots, 0.78-2.28 in across and 4.41-5.53 in down the page); x axis "Behavioral state #"; y axis "Frequency (%)"; drawn over x -0.5 to 81.5, y 0 to 10 (values beyond these limits are exported but were not visible).

One row is one vertical bar.

| Column | Meaning |
|---|---|
| `Behavioral state #` | x of the bar's centre on the axis labelled "Behavioral state #" |
| `bar width` | the bar's width, in x units |
| `bar bottom` | where the bar starts, in y units |
| `Frequency (%)` | the bar's height: y extent on the axis labelled "Frequency (%)" (unit: %) |

Every bar is filled: #76b5a0.

### `frequency_pct_vs_behavioral_state_2_bars.csv` (1.7 KB)

From the subplot "Frequency (%) vs Behavioral state # 2" (row 1, column 2 of the panel's subplots, 2.58-4.08 in across and 4.41-5.53 in down the page); x axis "Behavioral state #"; y axis "Frequency (%)"; drawn over x -0.5 to 81.5, y 0 to 10 (values beyond these limits are exported but were not visible).

One row is one vertical bar.

| Column | Meaning |
|---|---|
| `Behavioral state #` | x of the bar's centre on the axis labelled "Behavioral state #" |
| `bar width` | the bar's width, in x units |
| `bar bottom` | where the bar starts, in y units |
| `Frequency (%)` | the bar's height: y extent on the axis labelled "Frequency (%)" (unit: %) |

Every bar is filled: #c98ecf.

### `annotations.csv` (188 B)

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
| Line2D | 10 | 0 |
| Rectangle | 160 | 160 |
