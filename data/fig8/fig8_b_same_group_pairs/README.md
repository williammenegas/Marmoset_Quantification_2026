# fig8_b_same_group_pairs

Figure 8, panel b. Title: "Comparison to chance distribution".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig8/fig8_b_same_group_pairs.py`](../../../code/fig8/fig8_b_same_group_pairs.py).

## Files

### `same_group_pct_lines.csv` (413 B)

From the subplot "Same group (%)" (row 1, column 1 of the panel's subplots, 7.30-8.06 in across and 0.71-1.91 in down the page), in the row labelled "Spouses" / "Same-age siblings" / "Parent-offspring" / "Other household"; x axis "Same group (%)"; drawn over x 0 to 100, y 3.55 to -0.55 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `series` | the line's legend label, or the name its colour carries on the panel |
| `Same group (%)` | x position on the axis labelled "Same group (%)" (unit: %) |
| `y` | y position; this axis carries no label |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |

Line styles: 4 lines: colour #999999, width 0.8 pt; 4 lines: colour #262626, width 1.5 pt, no line, marker 'o' 4.2 pt, filled #262626, edged #262626

### `same_group_pct_boxes.csv` (168 B)

From the subplot "Same group (%)" (row 1, column 1 of the panel's subplots, 7.30-8.06 in across and 0.71-1.91 in down the page), in the row labelled "Spouses" / "Same-age siblings" / "Parent-offspring" / "Other household"; x axis "Same group (%)"; drawn over x 0 to 100, y 3.55 to -0.55 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Same group (%) left` | x of the box's left edge on the axis labelled "Same group (%)" (unit: %) |
| `Same group (%) right` | x of the box's right edge on the axis labelled "Same group (%)" (unit: %) |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |

Filled: yes.
Every box's fill: #e0e0e0.
Every box's outline: none.

### `page_shapes.csv` (63 B)

Drawn on the page around the panel's subplots, not in one of them: 1 Line2D.

One row is one vertex of one shape drawn on the page.

| Column | Meaning |
|---|---|
| `shape` | which shape, numbered from 1 in drawing order |
| `vertex` | the vertex's place along the shape |
| `x (in)` | inches from the page's left edge |
| `y (in)` | inches down from the page's top edge |

Drawn as: Line2D.
Every shape's fill: none.
Every line's colour: #231f20.
Every line's width (pt): 0.5.
Every line is: solid.
These are drawn on the page around the panel's subplots, not in one of them, so they are given in page inches, not in data coordinates. A shape that does not end where it starts is an open line.

### `annotations.csv` (265 B)

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
| Line2D | 8 | 8 |
| Rectangle | 4 | 4 |
| Line2D (on the page) | 1 | 1 |
