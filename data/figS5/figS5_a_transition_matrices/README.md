# figS5_a_transition_matrices

Figure S5, panel a. Title: "Shuffled", "Observed".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS5/figS5_a_transition_matrices.py`](../../../code/figS5/figS5_a_transition_matrices.py).

## Files

### `shuffled_lines.csv` (164 B)

From the subplot "Shuffled" (row 1, column 1 of the panel's subplots, 0.75-2.25 in across and 1.15-2.65 in down the page), under the page text "Shuffled"; x axis "Next state"; y axis "Current state"; drawn over x 0.5 to 80.5, y 80.5 to 0.5 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Next state` | x position on the axis labelled "Next state" |
| `Current state` | y position on the axis labelled "Current state" |

Line styles: 6 lines: colour #737373, width 0.4 pt, dashed

### `shuffled_map.csv` (27.0 KB)

From the subplot "Shuffled" (row 1, column 1 of the panel's subplots, 0.75-2.25 in across and 1.15-2.65 in down the page), under the page text "Shuffled"; x axis "Next state"; y axis "Current state"; drawn over x 0.5 to 80.5, y 80.5 to 0.5 (values beyond these limits are exported but were not visible).

A 80 x 80 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `Current state \ Next state` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0.5 to 80.5, y 80.5 to 0.5 (upper origin).
Colour map from_list (Normalize), limits -3 to 0; no colour bar.

### `observed_lines.csv` (164 B)

From the subplot "Observed" (row 1, column 2 of the panel's subplots, 2.51-4.01 in across and 1.15-2.65 in down the page), under the page text "Observed"; x axis "Next state"; y axis "Current state"; drawn over x 0.5 to 80.5, y 80.5 to 0.5 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Next state` | x position on the axis labelled "Next state" |
| `Current state` | y position on the axis labelled "Current state" |

Line styles: 6 lines: colour #737373, width 0.4 pt, dashed

### `observed_map.csv` (14.7 KB)

From the subplot "Observed" (row 1, column 2 of the panel's subplots, 2.51-4.01 in across and 1.15-2.65 in down the page), under the page text "Observed"; x axis "Next state"; y axis "Current state"; drawn over x 0.5 to 80.5, y 80.5 to 0.5 (values beyond these limits are exported but were not visible).

A 80 x 80 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `Current state \ Next state` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0.5 to 80.5, y 80.5 to 0.5 (upper origin).
Colour map from_list (Normalize), limits -3 to 0; no colour bar.

### `annotations.csv` (101 B)

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
| AxesImage | 2 | 2 |
| Line2D | 12 | 12 |
| LineCollection | 1 | 0 |
| QuadMesh | 1 | 0 |
