# figS12_e_projection_schematic

Figure S12, panel e. Title: "Projection: response × template".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS12/figS12_e_projection_schematic.py`](../../../code/figS12/figS12_e_projection_schematic.py).

## Files

### `response_c_map.csv` (24.5 KB)

From the subplot "Response (c)" (row 1, column 1 of the panel's subplots, 2.67-3.07 in across and 5.74-6.14 in down the page), under the page text "Response (c)"; no axis labels; drawn over x -410 to 410, y -410 to 410 (values beyond these limits are exported but were not visible).

A 41 x 41 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -410 to 410, y -410 to 410 (lower origin).
Colour map mb (Normalize), limits -0.016620077 to 0.016620077; no colour bar.

### `template_d_1_map.csv` (23.6 KB)

From the subplot "Template (d) 1" (row 1, column 2 of the panel's subplots, 3.57-3.97 in across and 5.74-6.14 in down the page), under the page text "Template (d)"; no axis labels; drawn over x -410 to 410, y -410 to 410 (values beyond these limits are exported but were not visible).

A 41 x 41 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -410 to 410, y -410 to 410 (lower origin).
Colour map mb (Normalize), limits -0.58034195 to 0.58034195; no colour bar.

### `held_out_control_baseline_map.csv` (24.7 KB)

From the subplot "Held-out control - baseline" (row 2, column 1 of the panel's subplots, 2.67-3.07 in across and 6.38-6.78 in down the page), under the page text "Held-out control - baseline"; no axis labels; drawn over x -410 to 410, y -410 to 410 (values beyond these limits are exported but were not visible).

A 41 x 41 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -410 to 410, y -410 to 410 (lower origin).
Colour map mb (Normalize), limits -0.0029194331 to 0.0029194331; no colour bar.

### `template_d_2_map.csv` (23.6 KB)

From the subplot "Template (d) 2" (row 2, column 2 of the panel's subplots, 3.57-3.97 in across and 6.38-6.78 in down the page), under the page text "Template (d)"; no axis labels; drawn over x -410 to 410, y -410 to 410 (values beyond these limits are exported but were not visible).

A 41 x 41 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -410 to 410, y -410 to 410 (lower origin).
Colour map mb (Normalize), limits -0.58034195 to 0.58034195; no colour bar.

### `annotations.csv` (400 B)

Every text printed in the panel: inside a subplot (x and y in that subplot's data coordinates; for an annotation with a leader line, the point it marks in `target x` and `target y`) or on the page around the subplots (x and y in inches from the page's top-left: the text's anchor).

| Column | Meaning |
|---|---|
| `subplot` | the subplot the text is in; blank for page text |
| `text` | the text as printed, on one line |
| `x`, `y` | its position (see `coordinates`) |
| `coordinates` | "data" or "page inches" |

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- decoration: the dashed cage wireframe: 20 Line2D

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| AxesImage | 4 | 4 |
| Line2D | 20 | 0 |
