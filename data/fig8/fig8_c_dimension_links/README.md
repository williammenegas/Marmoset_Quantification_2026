# fig8_c_dimension_links

Figure 8, panel c. Title: "Baseline dimensions", "Stimulus dimensions".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig8/fig8_c_dimension_links.py`](../../../code/fig8/fig8_c_dimension_links.py).

## Files

### `lines.csv` (564 B)

From the subplot "" (row 1, column 1 of the panel's subplots, 1.85-3.75 in across and 2.75-4.92 in down the page), in the row labelled "B1: Social vs climbing" / "B2: Activity / speed" / "B3: Time alone" / "B4: Alone behavioral states" / "B5: Climbing sequences" / "B6: Soc-act / active switches" / "B7: Active behavioral states" / "B8: Top speed"; no axis labels; drawn over x 1.85 to 3.75, y 4.924 to 2.754 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `marker fill` | the fill colour of the line's markers, hex RGB; blank where it draws none |
| `marker edge` | the outline colour of the line's markers, hex RGB; blank where it draws none |

Line styles: 8 lines: colour #231f20, width 1.5 pt, no line, marker 'o' 5 pt, filled #231f20, edged #231f20; 5 lines: colour #d1d3d4, width 1.5 pt, no line, marker 'o' 5 pt, filled #d1d3d4, edged #d1d3d4

### `shapes.csv` (44.2 KB)

From the subplot "" (row 1, column 1 of the panel's subplots, 1.85-3.75 in across and 2.75-4.92 in down the page), in the row labelled "B1: Social vs climbing" / "B2: Activity / speed" / "B3: Time alone" / "B4: Alone behavioral states" / "B5: Climbing sequences" / "B6: Soc-act / active switches" / "B7: Active behavioral states" / "B8: Top speed"; no axis labels; drawn over x 1.85 to 3.75, y 4.924 to 2.754 (values beyond these limits are exported but were not visible).

One row is one vertex of one shape's outline, curves sampled.

| Column | Meaning |
|---|---|
| `shape` | which shape, numbered from 1 in drawing order |
| `vertex` | the vertex's place along the outline |
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |
| `edge colour` | the shape's outline colour, hex RGB |

Drawn as: PathPatch.
Every shape's fill: none.

### `page_shapes.csv` (299 B)

Drawn on the page around the panel's subplots, not in one of them: 2 Rectangle.

One row is one vertex of one shape drawn on the page.

| Column | Meaning |
|---|---|
| `shape` | which shape, numbered from 1 in drawing order |
| `vertex` | the vertex's place along the shape |
| `x (in)` | inches from the page's left edge |
| `y (in)` | inches down from the page's top edge |
| `fill colour` | the shape's fill colour, hex RGB; none for a line |

Drawn as: Rectangle.
Every line's colour: none.
Every line's width (pt): 1.
Every line is: solid.
These are drawn on the page around the panel's subplots, not in one of them, so they are given in page inches, not in data coordinates. A shape that does not end where it starts is an open line.

### `annotations.csv` (828 B)

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
| Line2D | 13 | 13 |
| PathPatch | 6 | 6 |
| Rectangle (on the page) | 2 | 2 |
