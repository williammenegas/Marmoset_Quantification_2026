# fig2_e_state_usage

Figure 2, panel e. Title: "Behavioral state usage".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig2/fig2_e_state_usage.py`](../../../code/fig2/fig2_e_state_usage.py).

## Files

### `behavioral_state_usage_bars.csv` (2.1 KB)

From the subplot "Behavioral state usage" (row 1, column 1 of the panel's subplots, 0.77-1.84 in across and 3.77-4.58 in down the page), under the page text "Behavioral state usage"; x axis "Behavioral state (ID)"; y axis "State usage (%)"; drawn over x 0 to 80, y 0 to 7.5 (values beyond these limits are exported but were not visible).

One row is one vertical bar.

| Column | Meaning |
|---|---|
| `Behavioral state (ID)` | x of the bar's centre on the axis labelled "Behavioral state (ID)" |
| `bar width` | the bar's width, in x units |
| `bar bottom` | where the bar starts, in y units |
| `State usage (%)` | the bar's height: y extent on the axis labelled "State usage (%)" (unit: %) |
| `colour` | the bar's fill colour, hex RGB |

### `annotations.csv` (79 B)

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
| Rectangle | 80 | 80 |
