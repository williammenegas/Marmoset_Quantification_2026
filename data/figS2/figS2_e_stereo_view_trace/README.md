# figS2_e_stereo_view_trace

Figure S2, panel e. No title is printed on this panel.

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, and photographs and video frames as PNG.

- Redrawn from this folder alone by [`code/figS2/figS2_e_stereo_view_trace.py`](../../../code/figS2/figS2_e_stereo_view_trace.py).

## Files

### `head_depth_a_u_vs_time_min_lines.csv` (63 B)

From the subplot "Head depth (a.u.) vs Time (min)" (row 2, column 1 of the panel's subplots, 3.94-7.35 in across and 3.40-4.14 in down the page); x axis "Time (min)"; y axis "Head depth (a.u.)"; drawn over x 0 to 30, y 0 to 250 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (min)` | x position on the axis labelled "Time (min)" (unit: min) |
| `Head depth (a.u.)` | y position on the axis labelled "Head depth (a.u.)" (unit: a.u.) |

Line styles: 1 line: colour #999999, width 0.5 pt, dashed

### `head_depth_a_u_vs_time_min_boxes.csv` (431 B)

From the subplot "Head depth (a.u.) vs Time (min)" (row 2, column 1 of the panel's subplots, 3.94-7.35 in across and 3.40-4.14 in down the page); x axis "Time (min)"; y axis "Head depth (a.u.)"; drawn over x 0 to 30, y 0 to 250 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (min) left` | x of the box's left edge on the axis labelled "Time (min)" (unit: min) |
| `Time (min) right` | x of the box's right edge on the axis labelled "Time (min)" (unit: min) |
| `Head depth (a.u.) bottom` | y of the box's lower edge on the axis labelled "Head depth (a.u.)" (unit: a.u.) |
| `Head depth (a.u.) top` | y of the box's upper edge on the axis labelled "Head depth (a.u.)" (unit: a.u.) |

Filled: yes.
Every box's fill: #e3e3e3.
Every box's outline: none.

### `head_depth_a_u_vs_time_min_segments.csv` (81.6 KB)

From the subplot "Head depth (a.u.) vs Time (min)" (row 2, column 1 of the panel's subplots, 3.94-7.35 in across and 3.40-4.14 in down the page); x axis "Time (min)"; y axis "Head depth (a.u.)"; drawn over x 0 to 30, y 0 to 250 (values beyond these limits are exported but were not visible).

One row is one straight segment.

| Column | Meaning |
|---|---|
| `Time (min) from` | x of the segment's start on the axis labelled "Time (min)" (unit: min) |
| `Head depth (a.u.) from` | y of the segment's start on the axis labelled "Head depth (a.u.)" (unit: a.u.) |
| `Time (min) to` | x of the segment's end on the axis labelled "Time (min)" (unit: min) |
| `Head depth (a.u.) to` | y of the segment's end on the axis labelled "Head depth (a.u.)" (unit: a.u.) |
| `Depth (a.u.)` | the value the segment's colour maps |

Colour map inferno from 25 to 175.

### `time_min_boxes.csv` (371 B)

From the subplot "Time (min)" (row 1, column 1 of the panel's subplots, 3.94-7.35 in across and 3.34-3.37 in down the page); x axis "Time (min)"; drawn over x 0 to 30, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (min) left` | x of the box's left edge on the axis labelled "Time (min)" (unit: min) |
| `Time (min) right` | x of the box's right edge on the axis labelled "Time (min)" (unit: min) |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |

Filled: yes.
Every box's fill: #262626.
Every box's outline: none.

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- colour bar (its label and limits are given with the data it keys): 1 LineCollection, 1 QuadMesh

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| Line2D | 1 | 1 |
| LineCollection | 2 | 1 |
| QuadMesh | 1 | 0 |
| Rectangle | 28 | 28 |
