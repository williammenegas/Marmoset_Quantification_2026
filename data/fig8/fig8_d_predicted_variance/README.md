# fig8_d_predicted_variance

Figure 8, panel d. Title: "Variance (%) predicted using baseline dimensions".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig8/fig8_d_predicted_variance.py`](../../../code/fig8/fig8_d_predicted_variance.py).

## Files

### `share_predicted_pct_bars.csv` (166 B)

From the subplot "Share predicted (%)" (row 1, column 1 of the panel's subplots, 6.37-7.61 in across and 2.92-4.30 in down the page), under the page text "Variance (%) predicted using baseline dimensions", in the row labelled "Broad reaction" / "Treat approach" / "Mask reaction" / "Intruder activity" / "Approach to tablet"; x axis "Share predicted (%)"; drawn over x 0 to 1, y 4.305 to 2.924 (values beyond these limits are exported but were not visible); its x axis prints "0" at 0, "50" at 0.5, "100" at 1.

One row is one horizontal bar.

| Column | Meaning |
|---|---|
| `y` | y of the bar's centre; this axis carries no label |
| `bar height` | the bar's thickness, in y units |
| `bar left` | where the bar starts, in x units |
| `Share predicted (%)` | the bar's length: x extent on the axis labelled "Share predicted (%)" (unit: %) |

Every bar is filled: #bcbec0.

### `annotations.csv` (321 B)

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
| Rectangle | 5 | 5 |
