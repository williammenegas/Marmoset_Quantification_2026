# fig1_b_label_timeseries

Figure 1, panel b. Title: "Label timeseries".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig1/fig1_b_label_timeseries.py`](../../../code/fig1/fig1_b_label_timeseries.py).

## Files

### `label_timeseries_lines.csv` (582.1 KB)

From the subplot "Label timeseries" (row 1, column 1 of the panel's subplots, 4.29-7.78 in across and 0.60-2.32 in down the page), under the page text "Label timeseries"; x axis "Time (seconds)"; y axis "Position (X)"; z axis "Position (Y)"; drawn over x 0 to 60, y -481.26832 to 481.26832, z -481.26832 to 481.26832 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `Position (X)` | y position on the axis labelled "Position (X)" |
| `Position (Y)` | z position on the axis labelled "Position (Y)" |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |

Line styles: 13 lines: colour #d1d4d4, width 0.5 pt; 1 line: colour #211f1f, width 0.75 pt; 13 lines: colour #fcc2d4, width 0.5 pt; 1 line: colour #f86990, width 0.75 pt; 13 lines: colour #debfe3, width 0.5 pt; 1 line: colour #ac5fb8, width 0.75 pt; 13 lines: colour #c2bff0, width 0.5 pt; 1 line: colour #6361d7, width 0.75 pt

### `annotations.csv` (71 B)

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
| Line3D | 56 | 56 |
