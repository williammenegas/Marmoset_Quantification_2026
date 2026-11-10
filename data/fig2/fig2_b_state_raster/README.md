# fig2_b_state_raster

Figure 2, panel b. No title is printed on this panel.

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, and photographs and video frames as PNG.

- Redrawn from this folder alone by [`code/fig2/fig2_b_state_raster.py`](../../../code/fig2/fig2_b_state_raster.py).

## Files

### `behavioral_state_vs_time_min_points.csv` (199.4 KB)

From the subplot "Behavioral state vs Time (min)" (row 1, column 1 of the panel's subplots, 2.18-7.99 in across and 0.67-1.92 in down the page); x axis "Time (min)"; y axis "Behavioral state"; drawn over x 0 to 60, y 0.5 to 80.5 (values beyond these limits are exported but were not visible); its y axis prints "5" at 5.5, "28" at 28.5, "59" at 59.5, "80" at 80.5.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `Time (min)` | x position on the axis labelled "Time (min)" (unit: min) |
| `Behavioral state` | y position on the axis labelled "Behavioral state" |
| `colour` | the marker's fill colour, hex RGB |

Every marker has an area of 0.8 pt^2.

### `behavioral_state_vs_time_min_boxes.csv` (187 B)

From the subplot "Behavioral state vs Time (min)" (row 1, column 1 of the panel's subplots, 2.18-7.99 in across and 0.67-1.92 in down the page); x axis "Time (min)"; y axis "Behavioral state"; drawn over x 0 to 60, y 0.5 to 80.5 (values beyond these limits are exported but were not visible); its y axis prints "5" at 5.5, "28" at 28.5, "59" at 59.5, "80" at 80.5.

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (min) left` | x of the box's left edge on the axis labelled "Time (min)" (unit: min) |
| `Time (min) right` | x of the box's right edge on the axis labelled "Time (min)" (unit: min) |
| `Behavioral state bottom` | y of the box's lower edge on the axis labelled "Behavioral state" |
| `Behavioral state top` | y of the box's upper edge on the axis labelled "Behavioral state" |
| `fill colour` | the box's fill colour, hex RGB |

Filled: yes.
Every box's outline: none.

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- nothing else

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| PathCollection | 1 | 1 |
| Rectangle | 4 | 4 |
