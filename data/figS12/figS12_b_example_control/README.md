# figS12_b_example_control

Figure S12, panel b. Title: "Example animal: control (n = 9 sessions)".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS12/figS12_b_example_control.py`](../../../code/figS12/figS12_b_example_control.py).

## Files

### `climb_map.csv` (23.7 KB)

From the subplot "Climb" (row 1, column 1 of the panel's subplots, 2.67-3.47 in across and 2.19-2.99 in down the page), in the row labelled "Example animal: control (n = 9 sessions)"; no axis labels; drawn over x -410 to 410, y -410 to 410 (values beyond these limits are exported but were not visible).

A 41 x 41 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -410 to 410, y -410 to 410 (lower origin).
Colour map mb (Normalize), limits 0 to 0.001461733; no colour bar.

### `active_map.csv` (23.5 KB)

From the subplot "Active" (row 1, column 2 of the panel's subplots, 3.57-4.37 in across and 2.19-2.99 in down the page), in the row labelled "Example animal: control (n = 9 sessions)"; no axis labels; drawn over x -410 to 410, y -410 to 410 (values beyond these limits are exported but were not visible).

A 41 x 41 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -410 to 410, y -410 to 410 (lower origin).
Colour map mb (Normalize), limits 0 to 0.001461733; no colour bar.

### `alone_map.csv` (20.9 KB)

From the subplot "Alone" (row 1, column 3 of the panel's subplots, 4.47-5.27 in across and 2.19-2.99 in down the page), in the row labelled "Example animal: control (n = 9 sessions)"; no axis labels; drawn over x -410 to 410, y -410 to 410 (values beyond these limits are exported but were not visible).

A 41 x 41 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -410 to 410, y -410 to 410 (lower origin).
Colour map mb (Normalize), limits 0 to 0.001461733; no colour bar.

### `soc_act_map.csv` (19.4 KB)

From the subplot "Soc-act" (row 1, column 4 of the panel's subplots, 5.37-6.17 in across and 2.19-2.99 in down the page), in the row labelled "Example animal: control (n = 9 sessions)"; no axis labels; drawn over x -410 to 410, y -410 to 410 (values beyond these limits are exported but were not visible).

A 41 x 41 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -410 to 410, y -410 to 410 (lower origin).
Colour map mb (Normalize), limits 0 to 0.001461733; no colour bar.

### `soc_rest_map.csv` (17.4 KB)

From the subplot "Soc-rest" (row 1, column 5 of the panel's subplots, 6.27-7.07 in across and 2.19-2.99 in down the page), in the row labelled "Example animal: control (n = 9 sessions)"; no axis labels; drawn over x -410 to 410, y -410 to 410 (values beyond these limits are exported but were not visible).

A 41 x 41 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -410 to 410, y -410 to 410 (lower origin).
Colour map mb (Normalize), limits 0 to 0.001461733; no colour bar.

### `annotations.csv` (97 B)

Every text printed in the panel: inside a subplot (x and y in that subplot's data coordinates; for an annotation with a leader line, the point it marks in `target x` and `target y`) or on the page around the subplots (x and y in inches from the page's top-left: the text's anchor).

| Column | Meaning |
|---|---|
| `subplot` | the subplot the text is in; blank for page text |
| `text` | the text as printed, on one line |
| `x`, `y` | its position (see `coordinates`) |
| `coordinates` | "data" or "page inches" |

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- decoration: the dashed cage wireframe: 25 Line2D

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| AxesImage | 5 | 5 |
| Line2D | 25 | 0 |
