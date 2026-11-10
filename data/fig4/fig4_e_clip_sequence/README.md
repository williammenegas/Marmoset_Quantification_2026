# fig4_e_clip_sequence

Figure 4, panel e. No title is printed on this panel.

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig4/fig4_e_clip_sequence.py`](../../../code/fig4/fig4_e_clip_sequence.py).

## Files

### `time_near_other_vs_segment_boxes.csv` (1.5 KB)

From the subplot "Time near other vs Segment #" (row 1, column 1 of the panel's subplots, 4.02-7.81 in across and 2.43-2.88 in down the page); x axis "Segment #"; y axis "Time near other"; drawn over x 0 to 258, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Segment # left` | x of the box's left edge on the axis labelled "Segment #" |
| `Segment # right` | x of the box's right edge on the axis labelled "Segment #" |
| `Time near other bottom` | y of the box's lower edge on the axis labelled "Time near other" |
| `Time near other top` | y of the box's upper edge on the axis labelled "Time near other" |

Filled: yes.
Every box's fill: #d8d8d8.
Every box's outline: none.

### `time_near_other_vs_segment_steps.csv` (4.0 KB)

From the subplot "Time near other vs Segment #" (row 1, column 1 of the panel's subplots, 4.02-7.81 in across and 2.43-2.88 in down the page); x axis "Segment #"; y axis "Time near other"; drawn over x 0 to 258, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one step: the value held between two edges.

| Column | Meaning |
|---|---|
| `Segment # from` | x of the step's start on the axis labelled "Segment #" |
| `Segment # to` | x of the step's end on the axis labelled "Segment #" |
| `Time near other` | the value held over the step: y position on the axis labelled "Time near other" |

Every step's line: #3c3c3c.
Every step's fill: none.
Drawn as an open line through the steps, with no baseline: each step is joined to the next by a vertical line at the edge they share.

### `call_rate_vs_segment_boxes.csv` (1.6 KB)

From the subplot "Call rate vs Segment #" (row 2, column 1 of the panel's subplots, 4.02-7.81 in across and 2.96-3.41 in down the page); x axis "Segment #"; y axis "Call rate"; drawn over x 0 to 258, y 0 to 30 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Segment # left` | x of the box's left edge on the axis labelled "Segment #" |
| `Segment # right` | x of the box's right edge on the axis labelled "Segment #" |
| `Call rate bottom` | y of the box's lower edge on the axis labelled "Call rate" |
| `Call rate top` | y of the box's upper edge on the axis labelled "Call rate" |

Filled: yes.
Every box's fill: #d4ccee.
Every box's outline: none.

### `call_rate_vs_segment_steps.csv` (3.0 KB)

From the subplot "Call rate vs Segment #" (row 2, column 1 of the panel's subplots, 4.02-7.81 in across and 2.96-3.41 in down the page); x axis "Segment #"; y axis "Call rate"; drawn over x 0 to 258, y 0 to 30 (values beyond these limits are exported but were not visible).

One row is one step: the value held between two edges.

| Column | Meaning |
|---|---|
| `Segment # from` | x of the step's start on the axis labelled "Segment #" |
| `Segment # to` | x of the step's end on the axis labelled "Segment #" |
| `Call rate` | the value held over the step: y position on the axis labelled "Call rate" |

Every step's line: #8067ce.
Every step's fill: none.
Drawn as an open line through the steps, with no baseline: each step is joined to the next by a vertical line at the edge they share.

### `page_shapes.csv` (499 B)

Drawn on the page around the panel's subplots, not in one of them: 4 Rectangle.

One row is one vertex of one shape drawn on the page.

| Column | Meaning |
|---|---|
| `shape` | which shape, numbered from 1 in drawing order |
| `vertex` | the vertex's place along the shape |
| `x (in)` | inches from the page's left edge |
| `y (in)` | inches down from the page's top edge |
| `fill colour` | the shape's fill colour, hex RGB; none for a line |

Drawn as: Rectangle.
Every line's colour: #221f1f.
Every line's width (pt): 0.5.
Every line is: solid.
These are drawn on the page around the panel's subplots, not in one of them, so they are given in page inches, not in data coordinates. A shape that does not end where it starts is an open line.

### `annotations.csv` (143 B)

Every text printed in the panel: inside a subplot (x and y in that subplot's data coordinates; for an annotation with a leader line, the point it marks in `target x` and `target y`) or on the page around the subplots (x and y in inches from the page's top-left: the text's anchor).

| Column | Meaning |
|---|---|
| `subplot` | the subplot the text is in; blank for page text |
| `text` | the text as printed, on one line |
| `x`, `y` | its position (see `coordinates`) |
| `coordinates` | "data" or "page inches" |

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- decoration: the dashed lines at the call-rate and time-near-other ticks: 7 Line2D

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| Line2D | 7 | 0 |
| Rectangle | 257 | 257 |
| StepPatch | 2 | 2 |
| Rectangle (on the page) | 4 | 4 |
