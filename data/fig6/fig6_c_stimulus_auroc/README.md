# fig6_c_stimulus_auroc

Figure 6, panel c. No title is printed on this panel.

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, and photographs and video frames as PNG.

- Redrawn from this folder alone by [`code/fig6/fig6_c_stimulus_auroc.py`](../../../code/fig6/fig6_c_stimulus_auroc.py).

## Files

### `auroc_vs_held_out_control_lines.csv` (421 B)

From the subplot "AUROC vs held-out control" (row 1, column 1 of the panel's subplots, 0.98-2.81 in across and 5.32-6.78 in down the page); y axis "AUROC vs held-out control"; drawn over x -0.6 to 7.6, y 0.45 to 1.02 (values beyond these limits are exported but were not visible); its x axis prints "Box" at 0, "Face" at 1, "Intruder" at 2, "Mask" at 3, "Treat" at 4, "Toys" at 5, "Noise" at 6, "Object" at 7.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `AUROC vs held-out control` | y position on the axis labelled "AUROC vs held-out control" |
| `category` | the category named by the nearest x tick label |

Line styles: 8 lines: colour #262626, width 0.5 pt; 1 line: colour #262626, width 0.5 pt, dashed

### `auroc_vs_held_out_control_bars.csv` (336 B)

From the subplot "AUROC vs held-out control" (row 1, column 1 of the panel's subplots, 0.98-2.81 in across and 5.32-6.78 in down the page); y axis "AUROC vs held-out control"; drawn over x -0.6 to 7.6, y 0.45 to 1.02 (values beyond these limits are exported but were not visible); its x axis prints "Box" at 0, "Face" at 1, "Intruder" at 2, "Mask" at 3, "Treat" at 4, "Toys" at 5, "Noise" at 6, "Object" at 7.

One row is one vertical bar.

| Column | Meaning |
|---|---|
| `x` | x of the bar's centre; this axis carries no label |
| `bar width` | the bar's width, in x units |
| `bar bottom` | where the bar starts, in y units |
| `AUROC vs held-out control` | the bar's height: y extent on the axis labelled "AUROC vs held-out control" |
| `colour` | the bar's fill colour, hex RGB |
| `category` | the category named by the nearest tick label |

### `auroc_vs_held_out_control_boxes.csv` (109 B)

From the subplot "AUROC vs held-out control" (row 1, column 1 of the panel's subplots, 0.98-2.81 in across and 5.32-6.78 in down the page); y axis "AUROC vs held-out control"; drawn over x -0.6 to 7.6, y 0.45 to 1.02 (values beyond these limits are exported but were not visible); its x axis prints "Box" at 0, "Face" at 1, "Intruder" at 2, "Mask" at 3, "Treat" at 4, "Toys" at 5, "Noise" at 6, "Object" at 7.

One row is one rectangle.

| Column | Meaning |
|---|---|
| `x left` | x of the box's left edge; this axis carries no label |
| `x right` | x of the box's right edge; this axis carries no label |
| `AUROC vs held-out control bottom` | y of the box's lower edge on the axis labelled "AUROC vs held-out control" |
| `AUROC vs held-out control top` | y of the box's upper edge on the axis labelled "AUROC vs held-out control" |

Filled: yes.
Every box's fill: #73737338.
Every box's outline: none.

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- nothing else

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| Line2D | 9 | 9 |
| Rectangle | 9 | 9 |
