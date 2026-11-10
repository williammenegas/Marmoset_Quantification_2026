# fig7_c_early_late_halves

Figure 7, panel c. Title: "Early vs late".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig7/fig7_c_early_late_halves.py`](../../../code/fig7/fig7_c_early_late_halves.py).

## Files

### `early_vs_late_animal_half_1_lines.csv` (143 B)

From the subplot "Early vs late Animal, half 1 (#)" (row 1, column 1 of the panel's subplots, 6.32-7.72 in across and 0.71-2.11 in down the page), under the page text "Group 3" / "Group 2" / "Group 1"; x axis "Animal, half 2 (#)"; y axis "Animal, half 1 (#)"; drawn over x -0.5 to 63.5, y 63.5 to -0.5 (values beyond these limits are exported but were not visible); its x axis prints "0" at -0.5, "64" at 63.5; its y axis prints "0" at -0.5, "64" at 63.5.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Animal, half 2 (#)` | x position on the axis labelled "Animal, half 2 (#)" |
| `Animal, half 1 (#)` | y position on the axis labelled "Animal, half 1 (#)" |

Line styles: 4 lines: colour #262626, width 0.5 pt

### `early_vs_late_animal_half_1_boxes.csv` (126 B)

From the subplot "Early vs late Animal, half 1 (#)" (row 1, column 1 of the panel's subplots, 6.32-7.72 in across and 0.71-2.11 in down the page), under the page text "Group 3" / "Group 2" / "Group 1"; x axis "Animal, half 2 (#)"; y axis "Animal, half 1 (#)"; drawn over x -0.5 to 63.5, y 63.5 to -0.5 (values beyond these limits are exported but were not visible); its x axis prints "0" at -0.5, "64" at 63.5; its y axis prints "0" at -0.5, "64" at 63.5.

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Animal, half 2 (#) left` | x of the box's left edge on the axis labelled "Animal, half 2 (#)" |
| `Animal, half 2 (#) right` | x of the box's right edge on the axis labelled "Animal, half 2 (#)" |
| `Animal, half 1 (#) bottom` | y of the box's lower edge on the axis labelled "Animal, half 1 (#)" |
| `Animal, half 1 (#) top` | y of the box's upper edge on the axis labelled "Animal, half 1 (#)" |

Filled: no.
Every box's fill: none.
Every box's outline: #262626.

### `early_vs_late_animal_half_1_map.csv` (47.8 KB)

From the subplot "Early vs late Animal, half 1 (#)" (row 1, column 1 of the panel's subplots, 6.32-7.72 in across and 0.71-2.11 in down the page), under the page text "Group 3" / "Group 2" / "Group 1"; x axis "Animal, half 2 (#)"; y axis "Animal, half 1 (#)"; drawn over x -0.5 to 63.5, y 63.5 to -0.5 (values beyond these limits are exported but were not visible); its x axis prints "0" at -0.5, "64" at 63.5; its y axis prints "0" at -0.5, "64" at 63.5.

A 64 x 64 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `Animal, half 1 (#) \ Animal, half 2 (#)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `Correlation` | every other cell: the image cell's value |

Image extent: x -0.5 to 63.5, y 63.5 to -0.5 (upper origin).
Colour map soft_diverging (Normalize), limits -0.8 to 0.8, colour bar "Correlation".

### `early_vs_late_boxes.csv` (166 B)

From the subplot "Early vs late" (row 2, column 1 of the panel's subplots, 6.32-7.72 in across and 2.67-3.92 in down the page), under the page text "Early vs late"; no axis labels; drawn over x 0 to 1, y 70 to 0 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `x left` | x of the box's left edge; this axis carries no label |
| `x right` | x of the box's right edge; this axis carries no label |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |
| `fill colour` | the box's fill colour, hex RGB |

Filled: yes.
Every box's outline: none.

### `early_vs_late_ribbons.csv` (572 B)

From the subplot "Early vs late" (row 2, column 1 of the panel's subplots, 6.32-7.72 in across and 2.67-3.92 in down the page), under the page text "Early vs late"; no axis labels; drawn over x 0 to 1, y 70 to 0 (values beyond these limits are exported but were not visible).

One row is one band, from a box on the left to a box on the right.

| Column | Meaning |
|---|---|
| `left box` | the name printed beside the box the band leaves |
| `right box` | the name printed beside the box it reaches |
| `band height` | the band's height, in the axes' y units: how much flows from the left box to the right one |
| `colour` | the band's colour, hex RGB |
| `x at left end` | where the band leaves its left box, in the axes' x units |
| `x at right end` | where it reaches its right box, in the axes' x units |
| `bottom at left end` | the band's lower y value at its left end |
| `top at left end` | the band's upper y value at its left end |
| `bottom at right end` | the band's lower y value at its right end |
| `top at right end` | the band's upper y value at its right end |

Each band is drawn as a closed cubic Bezier path: from its left end to its right end, both of its edges leave and arrive level, with the two control points of each edge at the x midway between the ends (at the left end's y, then at the right end's). The curve is drawing; the ends are the data.
Every band end lies on the edge of a box, inside its y range (see the boxes table for the boxes).
Drawn at 40% opacity.
The boxes on the left are the groups each animal falls in from half 1 of its recordings ("Half 1" above them), those on the right its group from half 2 ("Half 2"), for the early-vs-late split; the y axis counts animals, so a band's height is the number of animals that move from its left box to its right one.

### `early_vs_late_flows.csv` (90 B)

From the subplot "Early vs late" (row 2, column 1 of the panel's subplots, 6.32-7.72 in across and 2.67-3.92 in down the page), under the page text "Early vs late"; no axis labels; drawn over x 0 to 1, y 70 to 0 (values beyond these limits are exported but were not visible).

A 3 x 3 matrix. 
One row is one box on the left (its name first); one column per box on the right (its name in the header).

| Column | Meaning |
|---|---|
| `left box \ right box` | header: each right box's name; first column: each left box's name |
| `every other cell` | the summed height of the bands from that left box to that right box |

The band heights summed for each pair of boxes; 0 where no band joins them. A row's sum is its left box's height, a column's its right box's.
The boxes on the left are the groups each animal falls in from half 1 of its recordings ("Half 1" above them), those on the right its group from half 2 ("Half 2"), for the early-vs-late split; the y axis counts animals, so a band's height is the number of animals that move from its left box to its right one.

### `annotations.csv` (551 B)

Every text printed in the panel: inside a subplot (x and y in that subplot's data coordinates; for an annotation with a leader line, the point it marks in `target x` and `target y`) or on the page around the subplots (x and y in inches from the page's top-left: the text's anchor).

| Column | Meaning |
|---|---|
| `subplot` | the subplot the text is in; blank for page text |
| `text` | the text as printed, on one line |
| `x`, `y` | its position (see `coordinates`) |
| `coordinates` | "data" or "page inches" |

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- colour bar (its label and limits are given with the data it keys): 1 LineCollection, 1 QuadMesh

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| AxesImage | 1 | 1 |
| Line2D | 4 | 4 |
| LineCollection | 1 | 0 |
| PathPatch | 9 | 9 |
| QuadMesh | 1 | 0 |
| Rectangle | 7 | 7 |
| Text | 6 | 6 |
