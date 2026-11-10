# figS2_c_single_view_trace

Figure S2, panel c. Title: "Example animal".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS2/figS2_c_single_view_trace.py`](../../../code/figS2/figS2_c_single_view_trace.py).

## Files

### `example_animal_head_radius_px_lines.csv` (51.9 KB)

From the subplot "Example animal Head radius (px)" (row 2, column 1 of the panel's subplots, 3.88-7.35 in across and 2.01-2.75 in down the page); x axis "Time (min)"; y axis "Head radius (px)"; drawn over x 0 to 30, y 0 to 60 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (min)` | x position on the axis labelled "Time (min)" (unit: min) |
| `Head radius (px)` | y position on the axis labelled "Head radius (px)" (unit: px) |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |

Line styles: 1 line: colour #262626, width 0.6 pt; 1 line: colour #999999, width 0.5 pt, dashed

### `example_animal_head_radius_px_boxes.csv` (415 B)

From the subplot "Example animal Head radius (px)" (row 2, column 1 of the panel's subplots, 3.88-7.35 in across and 2.01-2.75 in down the page); x axis "Time (min)"; y axis "Head radius (px)"; drawn over x 0 to 30, y 0 to 60 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (min) left` | x of the box's left edge on the axis labelled "Time (min)" (unit: min) |
| `Time (min) right` | x of the box's right edge on the axis labelled "Time (min)" (unit: min) |
| `Head radius (px) bottom` | y of the box's lower edge on the axis labelled "Head radius (px)" (unit: px) |
| `Head radius (px) top` | y of the box's upper edge on the axis labelled "Head radius (px)" (unit: px) |

Filled: yes.
Every box's fill: #e3e3e3.
Every box's outline: none.

### `example_animal_boxes.csv` (371 B)

From the subplot "Example animal" (row 1, column 1 of the panel's subplots, 3.88-7.35 in across and 1.95-1.98 in down the page), under the page text "Example animal"; x axis "Time (min)"; drawn over x 0 to 30, y 0 to 1 (values beyond these limits are exported but were not visible).

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

### `annotations.csv` (123 B)

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
| Line2D | 2 | 2 |
| Rectangle | 28 | 28 |
