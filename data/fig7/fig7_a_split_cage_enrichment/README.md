# fig7_a_split_cage_enrichment

Figure 7, panel a. Title: "Alternating", "Early vs late", "Cage locations enriched in each cluster-based group", "Box", "Intruder", "Mask".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig7/fig7_a_split_cage_enrichment.py`](../../../code/fig7/fig7_a_split_cage_enrichment.py).

## Files

### `alternating_lines.csv` (176 B)

From the subplot "Alternating" (row 1, column 1 of the panel's subplots, 0.52-1.34 in across and 0.53-0.80 in down the page), under the page text "Alternating"; x axis "Time (months)"; drawn over x -1.5 to 13.5, y -0.45090909 to 0.54909091 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (months)` | x position on the axis labelled "Time (months)" |
| `y` | y position; this axis carries no label |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `marker fill` | the fill colour of the line's markers, hex RGB; blank where it draws none; "none" where they are drawn unfilled |

Line styles: 1 line: colour #b8b8b8, width 0.5 pt; 1 line: colour #1f77b4, width 1.5 pt, no line, marker 'o' 5 pt, filled #404040, edged #404040; 1 line: colour #ff7f0e, width 1.5 pt, no line, marker 'o' 5 pt, unfilled, edged #404040; 1 line: colour #2ca02c, width 1.5 pt, no line, marker 'o' 5 pt, filled #404040, edged #404040; 1 line: colour #d62728, width 1.5 pt, no line, marker 'o' 5 pt, unfilled, edged #404040; 1 line: colour #9467bd, width 1.5 pt, no line, marker 'o' 5 pt, filled #404040, edged #404040

### `early_vs_late_lines.csv` (176 B)

From the subplot "Early vs late" (row 1, column 2 of the panel's subplots, 1.89-2.71 in across and 0.53-0.80 in down the page), under the page text "Early vs late"; x axis "Time (months)"; drawn over x -1.5 to 13.5, y -0.5 to 0.5 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (months)` | x position on the axis labelled "Time (months)" |
| `y` | y position; this axis carries no label |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `marker fill` | the fill colour of the line's markers, hex RGB; blank where it draws none; "none" where they are drawn unfilled |

Line styles: 1 line: colour #b8b8b8, width 0.5 pt; 1 line: colour #1f77b4, width 1.5 pt, no line, marker 'o' 5 pt, filled #404040, edged #404040; 1 line: colour #ff7f0e, width 1.5 pt, no line, marker 'o' 5 pt, filled #404040, edged #404040; 1 line: colour #2ca02c, width 1.5 pt, no line, marker 'o' 5 pt, filled #404040, edged #404040; 1 line: colour #d62728, width 1.5 pt, no line, marker 'o' 5 pt, unfilled, edged #404040; 1 line: colour #9467bd, width 1.5 pt, no line, marker 'o' 5 pt, unfilled, edged #404040

### `box_group_1_map.csv` (20.0 KB)

From the subplot "Box Group 1" (row 2, column 1 of the panel's subplots, 0.52-1.24 in across and 1.60-2.32 in down the page), under the page text "Box"; y axis "Group 1"; drawn over x -500 to 500, y -500 to 500 (values beyond these limits are exported but were not visible).

A 41 x 41 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `Group 1 \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -500 to 500, y -500 to 500 (lower origin).
Colour map mb (Normalize), limits 0 to 1.5; a colour bar with no label.

### `intruder_1_map.csv` (20.5 KB)

From the subplot "Intruder 1" (row 2, column 2 of the panel's subplots, 1.30-2.02 in across and 1.60-2.32 in down the page), under the page text "Cage locations enriched in each cluster-based group" / "Intruder"; no axis labels; drawn over x -500 to 500, y -500 to 500 (values beyond these limits are exported but were not visible).

A 41 x 41 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -500 to 500, y -500 to 500 (lower origin).
Colour map mb (Normalize), limits 0 to 1.5; a colour bar with no label.

### `mask_1_map.csv` (20.0 KB)

From the subplot "Mask 1" (row 2, column 3 of the panel's subplots, 2.07-2.79 in across and 1.60-2.32 in down the page), under the page text "Mask"; no axis labels; drawn over x -500 to 500, y -500 to 500 (values beyond these limits are exported but were not visible).

A 41 x 41 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -500 to 500, y -500 to 500 (lower origin).
Colour map mb (Normalize), limits 0 to 1.5; a colour bar with no label.

### `box_group_2_map.csv` (21.0 KB)

From the subplot "Box Group 2" (row 3, column 1 of the panel's subplots, 0.52-1.24 in across and 2.43-3.15 in down the page); y axis "Group 2"; drawn over x -500 to 500, y -500 to 500 (values beyond these limits are exported but were not visible).

A 41 x 41 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `Group 2 \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -500 to 500, y -500 to 500 (lower origin).
Colour map mb (Normalize), limits 0 to 1.5; a colour bar with no label.

### `intruder_2_map.csv` (20.5 KB)

From the subplot "Intruder 2" (row 3, column 2 of the panel's subplots, 1.30-2.02 in across and 2.43-3.15 in down the page); no axis labels; drawn over x -500 to 500, y -500 to 500 (values beyond these limits are exported but were not visible).

A 41 x 41 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -500 to 500, y -500 to 500 (lower origin).
Colour map mb (Normalize), limits 0 to 1.5; a colour bar with no label.

### `mask_2_map.csv` (20.2 KB)

From the subplot "Mask 2" (row 3, column 3 of the panel's subplots, 2.07-2.79 in across and 2.43-3.15 in down the page); no axis labels; drawn over x -500 to 500, y -500 to 500 (values beyond these limits are exported but were not visible).

A 41 x 41 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -500 to 500, y -500 to 500 (lower origin).
Colour map mb (Normalize), limits 0 to 1.5; a colour bar with no label.

### `box_group_3_map.csv` (20.8 KB)

From the subplot "Box Group 3" (row 4, column 1 of the panel's subplots, 0.52-1.24 in across and 3.26-3.98 in down the page); y axis "Group 3"; drawn over x -500 to 500, y -500 to 500 (values beyond these limits are exported but were not visible).

A 41 x 41 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `Group 3 \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -500 to 500, y -500 to 500 (lower origin).
Colour map mb (Normalize), limits 0 to 1.5; a colour bar with no label.

### `intruder_3_map.csv` (20.8 KB)

From the subplot "Intruder 3" (row 4, column 2 of the panel's subplots, 1.30-2.02 in across and 3.26-3.98 in down the page); no axis labels; drawn over x -500 to 500, y -500 to 500 (values beyond these limits are exported but were not visible).

A 41 x 41 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -500 to 500, y -500 to 500 (lower origin).
Colour map mb (Normalize), limits 0 to 1.5; a colour bar with no label.

### `mask_3_map.csv` (20.2 KB)

From the subplot "Mask 3" (row 4, column 3 of the panel's subplots, 2.07-2.79 in across and 3.26-3.98 in down the page); no axis labels; drawn over x -500 to 500, y -500 to 500 (values beyond these limits are exported but were not visible).

A 41 x 41 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -500 to 500, y -500 to 500 (lower origin).
Colour map mb (Normalize), limits 0 to 1.5; a colour bar with no label.

### `annotations.csv` (425 B)

Every text printed in the panel: inside a subplot (x and y in that subplot's data coordinates; for an annotation with a leader line, the point it marks in `target x` and `target y`) or on the page around the subplots (x and y in inches from the page's top-left: the text's anchor).

| Column | Meaning |
|---|---|
| `subplot` | the subplot the text is in; blank for page text |
| `text` | the text as printed, on one line |
| `x`, `y` | its position (see `coordinates`) |
| `coordinates` | "data" or "page inches" |

## Schematics

The subplot "Alternating" is the alternating split: one year of recording periods dealt into two halves, drawn as dots on a time line. Its shapes are exported as drawn, in the subplot's own coordinates, and its texts are in annotations.csv; they show a design, not measurements.
The subplot "Early vs late" is the early-vs-late split, drawn the same way. Its shapes are exported as drawn, in the subplot's own coordinates, and its texts are in annotations.csv; they show a design, not measurements.

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- colour bar (its label and limits are given with the data it keys): 3 LineCollection, 3 QuadMesh
- decoration: the dashed cage wireframe: 45 Line2D
- decoration: the grey box marking where the stimulus stands: 9 FancyBboxPatch

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| AxesImage | 9 | 9 |
| FancyBboxPatch | 9 | 0 |
| Line2D | 57 | 12 |
| LineCollection | 3 | 0 |
| QuadMesh | 3 | 0 |
