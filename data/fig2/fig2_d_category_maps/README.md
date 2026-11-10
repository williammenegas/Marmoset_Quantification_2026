# fig2_d_category_maps

Figure 2, panel d. Title: "Model output", "Climbing", "Active", "Alone", "Social active", "Social resting".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig2/fig2_d_category_maps.py`](../../../code/fig2/fig2_d_category_maps.py).

The dashed circle marking the bed, labelled "Bed" on the first map, is artwork pasted in Illustrator; not drawn by code: the data hold no bed position.

## Files

### `model_output_image.png` (3.8 KB)

From the subplot "Model output" (row 1, column 1 of the panel's subplots, 2.22-2.96 in across and 2.51-3.25 in down the page), under the page text "Model output"; y axis "Top-down view"; drawn over x -340 to 340, y -340 to 340 (values beyond these limits are exported but were not visible).

A picture drawn into the subplot, saved as a PNG.

Image extent: x -340 to 340, y -340 to 340 (upper origin).
48 x 48 pixels, saved as drawn (top row first).

### `climbing_map.csv` (26.5 KB)

From the subplot "Climbing" (row 1, column 2 of the panel's subplots, 3.22-3.96 in across and 2.51-3.25 in down the page), under the page text "Climbing"; y axis "Top-down view"; drawn over x -340 to 340, y -340 to 340 (values beyond these limits are exported but were not visible).

A 48 x 48 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `Top-down view \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -340 to 340, y -340 to 340 (upper origin).
Colour map Climbing (Normalize), limits 0 to 1; no colour bar.

### `active_map.csv` (25.8 KB)

From the subplot "Active" (row 1, column 3 of the panel's subplots, 4.22-4.96 in across and 2.51-3.25 in down the page), under the page text "Active"; y axis "Top-down view"; drawn over x -340 to 340, y -340 to 340 (values beyond these limits are exported but were not visible).

A 48 x 48 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `Top-down view \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -340 to 340, y -340 to 340 (upper origin).
Colour map Active (Normalize), limits 0 to 1; no colour bar.

### `alone_map.csv` (26.6 KB)

From the subplot "Alone" (row 1, column 4 of the panel's subplots, 5.22-5.96 in across and 2.51-3.25 in down the page), under the page text "Alone"; y axis "Top-down view"; drawn over x -340 to 340, y -340 to 340 (values beyond these limits are exported but were not visible).

A 48 x 48 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `Top-down view \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -340 to 340, y -340 to 340 (upper origin).
Colour map Alone (Normalize), limits 0 to 1; no colour bar.

### `social_active_map.csv` (27.1 KB)

From the subplot "Social active" (row 1, column 5 of the panel's subplots, 6.22-6.96 in across and 2.51-3.25 in down the page), under the page text "Social active"; y axis "Top-down view"; drawn over x -340 to 340, y -340 to 340 (values beyond these limits are exported but were not visible).

A 48 x 48 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `Top-down view \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -340 to 340, y -340 to 340 (upper origin).
Colour map Social active (Normalize), limits 0 to 1; no colour bar.

### `social_resting_map.csv` (23.1 KB)

From the subplot "Social resting" (row 1, column 6 of the panel's subplots, 7.23-7.97 in across and 2.51-3.25 in down the page), under the page text "Social resting"; y axis "Top-down view"; drawn over x -340 to 340, y -340 to 340 (values beyond these limits are exported but were not visible).

A 48 x 48 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `Top-down view \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -340 to 340, y -340 to 340 (upper origin).
Colour map Social resting (Normalize), limits 0 to 1; no colour bar.

### `annotations.csv` (255 B)

Every text printed in the panel: inside a subplot (x and y in that subplot's data coordinates; for an annotation with a leader line, the point it marks in `target x` and `target y`) or on the page around the subplots (x and y in inches from the page's top-left: the text's anchor).

| Column | Meaning |
|---|---|
| `subplot` | the subplot the text is in; blank for page text |
| `text` | the text as printed, on one line |
| `x`, `y` | its position (see `coordinates`) |
| `coordinates` | "data" or "page inches" |

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- decoration: the dashed cage wireframe: 30 Line2D

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| AxesImage | 6 | 6 |
| Line2D | 30 | 0 |
