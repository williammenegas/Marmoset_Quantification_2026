# fig4_d_calls_per_minute

Figure 4, panel d. No title is printed on this panel.

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig4/fig4_d_calls_per_minute.py`](../../../code/fig4/fig4_d_calls_per_minute.py).

## Files

### `number_of_clips_vs_calls_per_minute_bars.csv` (704 B)

From the subplot "Number of clips vs Calls per minute" (row 1, column 1 of the panel's subplots, 2.24-3.57 in across and 2.41-3.34 in down the page); x axis "Calls per minute"; y axis "Number of clips"; drawn over x -3.96 to 83.16, y 0 to 1964.55 (values beyond these limits are exported but were not visible).

One row is one vertical bar.

| Column | Meaning |
|---|---|
| `Calls per minute` | x of the bar's centre on the axis labelled "Calls per minute" |
| `bar width` | the bar's width, in x units |
| `bar bottom` | where the bar starts, in y units |
| `Number of clips` | the bar's height: y extent on the axis labelled "Number of clips" |

Every bar is filled: #8067ce.

### `annotations.csv` (112 B)

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
| Rectangle | 40 | 40 |
