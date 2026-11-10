# fig1_c_labeled_image

Figure 1, panel c. Title: "Labeled image".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig1/fig1_c_labeled_image.py`](../../../code/fig1/fig1_c_labeled_image.py).

Only the left part, "Labeled image", is drawn by code. The right part, "ID accuracy", is artwork pasted in Illustrator; not drawn by code.

## Files

### `labeled_image_lines.csv` (13.6 KB)

From the subplot "Labeled image" (row 1, column 1 of the panel's subplots, 0.57-1.72 in across and 2.70-3.86 in down the page), under the page text "Labeled image"; no axis labels; drawn over x 565 to 946, y 580 to 199 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `marker fill` | the fill colour of the line's markers, hex RGB; blank where it draws none |

Line styles: 176 lines: colour #ffffff, width 0.35 pt; 1 line: colour #1f77b4, width 1.5 pt, no line, marker 'o' 2.3 pt, filled #211f1f, edged #ffffff; 1 line: colour #ff7f0e, width 1.5 pt, no line, marker 'o' 2.3 pt, filled #6361d7, edged #ffffff; 1 line: colour #2ca02c, width 1.5 pt, no line, marker 'o' 2.3 pt, filled #ac5fb8, edged #ffffff; 1 line: colour #d62728, width 1.5 pt, no line, marker 'o' 2.3 pt, filled #f86990, edged #ffffff

### `labeled_image.png` (187.3 KB)

From the subplot "Labeled image" (row 1, column 1 of the panel's subplots, 0.57-1.72 in across and 2.70-3.86 in down the page), under the page text "Labeled image"; no axis labels; drawn over x 565 to 946, y 580 to 199 (values beyond these limits are exported but were not visible).

A picture drawn into the subplot, saved as a PNG.

Image extent: x 565 to 946, y 580 to 199 (upper origin).
381 x 381 pixels, saved as drawn (top row first).

### `annotations.csv` (68 B)

Every text printed in the panel: inside a subplot (x and y in that subplot's data coordinates; for an annotation with a leader line, the point it marks in `target x` and `target y`) or on the page around the subplots (x and y in inches from the page's top-left: the text's anchor).

| Column | Meaning |
|---|---|
| `subplot` | the subplot the text is in; blank for page text |
| `text` | the text as printed, on one line |
| `x`, `y` | its position (see `coordinates`) |
| `coordinates` | "data" or "page inches" |

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- legend: 1 Legend

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| AxesImage | 1 | 1 |
| Legend | 1 | 0 |
| Line2D | 180 | 180 |
