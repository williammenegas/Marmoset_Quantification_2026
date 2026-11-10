# figS8_d_call_examples

Figure S8, panel d. Title: "Individual call examples".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS8/figS8_d_call_examples.py`](../../../code/figS8/figS8_d_call_examples.py).

## Files

### `example_1_2_lines.csv` (78 B)

From the subplot "Example 1 2" (row 2, column 1 of the panel's subplots, 4.65-5.25 in across and 3.44-3.69 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `y` | y position; this axis carries no label |

Line styles: 2 lines: colour #6d6e71, width 0.6 pt, dashed

### `example_1_2_map.csv` (450.6 KB)

From the subplot "Example 1 2" (row 2, column 1 of the panel's subplots, 4.65-5.25 in across and 3.44-3.69 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

A 126 x 250 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 1.8229167, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 500 cells (rows x columns) print over 0.25 x 0.59 in, 100 x 237 pixels at 400 dpi, so every 3 rows and every 2 columns are averaged (blank cells left out) into the 126 x 250 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits -5e-09 to 5e-09; no colour bar.

### `example_1_1_boxes.csv` (79 B)

From the subplot "Example 1 1" (row 1, column 1 of the panel's subplots, 4.65-5.25 in across and 3.39-3.41 in down the page), under the page text "Example 1"; x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (seconds) left` | x of the box's left edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Time (seconds) right` | x of the box's right edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |

Filled: yes.
Every box's fill: #ed2f24.
Every box's outline: none.

### `example_1_4_lines.csv` (92 B)

From the subplot "Example 1 4" (row 4, column 1 of the panel's subplots, 4.65-5.25 in across and 3.80-4.05 in down the page); x axis "Time (seconds)"; y axis "Frequency (kHz)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `Frequency (kHz)` | y position on the axis labelled "Frequency (kHz)" (unit: kHz) |

Line styles: 2 lines: colour #6d6e71, width 0.6 pt, dashed

### `example_1_4_map.csv` (467.6 KB)

From the subplot "Example 1 4" (row 4, column 1 of the panel's subplots, 4.65-5.25 in across and 3.80-4.05 in down the page); x axis "Time (seconds)"; y axis "Frequency (kHz)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

A 126 x 250 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `Frequency (kHz) \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 1.8229167, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 500 cells (rows x columns) print over 0.25 x 0.59 in, 100 x 237 pixels at 400 dpi, so every 3 rows and every 2 columns are averaged (blank cells left out) into the 126 x 250 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits -5e-09 to 5e-09; no colour bar.

### `example_1_3_boxes.csv` (107 B)

From the subplot "Example 1 3" (row 3, column 1 of the panel's subplots, 4.65-5.25 in across and 3.75-3.77 in down the page); x axis "Time (seconds)"; y axis "Frequency (kHz)"; drawn over x 0 to 1.8229167, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (seconds) left` | x of the box's left edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Time (seconds) right` | x of the box's right edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Frequency (kHz) bottom` | y of the box's lower edge on the axis labelled "Frequency (kHz)" (unit: kHz) |
| `Frequency (kHz) top` | y of the box's upper edge on the axis labelled "Frequency (kHz)" (unit: kHz) |

Filled: yes.
Every box's fill: #bcbdbf.
Every box's outline: none.

### `example_1_6_lines.csv` (92 B)

From the subplot "Example 1 6" (row 6, column 1 of the panel's subplots, 4.65-5.25 in across and 4.16-4.41 in down the page); x axis "Time (seconds)"; y axis "Frequency (kHz)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `Frequency (kHz)` | y position on the axis labelled "Frequency (kHz)" (unit: kHz) |

Line styles: 2 lines: colour #6d6e71, width 0.6 pt, dashed

### `example_1_6_map.csv` (466.5 KB)

From the subplot "Example 1 6" (row 6, column 1 of the panel's subplots, 4.65-5.25 in across and 4.16-4.41 in down the page); x axis "Time (seconds)"; y axis "Frequency (kHz)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

A 126 x 250 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `Frequency (kHz) \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 1.8229167, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 500 cells (rows x columns) print over 0.25 x 0.59 in, 100 x 237 pixels at 400 dpi, so every 3 rows and every 2 columns are averaged (blank cells left out) into the 126 x 250 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits -5e-09 to 5e-09; no colour bar.

### `example_1_5_boxes.csv` (107 B)

From the subplot "Example 1 5" (row 5, column 1 of the panel's subplots, 4.65-5.25 in across and 4.11-4.14 in down the page); x axis "Time (seconds)"; y axis "Frequency (kHz)"; drawn over x 0 to 1.8229167, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (seconds) left` | x of the box's left edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Time (seconds) right` | x of the box's right edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Frequency (kHz) bottom` | y of the box's lower edge on the axis labelled "Frequency (kHz)" (unit: kHz) |
| `Frequency (kHz) top` | y of the box's upper edge on the axis labelled "Frequency (kHz)" (unit: kHz) |

Filled: yes.
Every box's fill: #bcbdbf.
Every box's outline: none.

### `example_1_8_lines.csv` (78 B)

From the subplot "Example 1 8" (row 8, column 1 of the panel's subplots, 4.65-5.25 in across and 4.52-4.77 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `y` | y position; this axis carries no label |

Line styles: 2 lines: colour #6d6e71, width 0.6 pt, dashed

### `example_1_8_map.csv` (462.8 KB)

From the subplot "Example 1 8" (row 8, column 1 of the panel's subplots, 4.65-5.25 in across and 4.52-4.77 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

A 126 x 250 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 1.8229167, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 500 cells (rows x columns) print over 0.25 x 0.59 in, 100 x 237 pixels at 400 dpi, so every 3 rows and every 2 columns are averaged (blank cells left out) into the 126 x 250 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits -5e-09 to 5e-09; no colour bar.

### `example_1_7_boxes.csv` (79 B)

From the subplot "Example 1 7" (row 7, column 1 of the panel's subplots, 4.65-5.25 in across and 4.47-4.50 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (seconds) left` | x of the box's left edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Time (seconds) right` | x of the box's right edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |

Filled: yes.
Every box's fill: #bcbdbf.
Every box's outline: none.

### `example_2_2_lines.csv` (82 B)

From the subplot "Example 2 2" (row 2, column 2 of the panel's subplots, 5.52-6.11 in across and 3.44-3.69 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `y` | y position; this axis carries no label |

Line styles: 2 lines: colour #6d6e71, width 0.6 pt, dashed

### `example_2_2_map.csv` (458.1 KB)

From the subplot "Example 2 2" (row 2, column 2 of the panel's subplots, 5.52-6.11 in across and 3.44-3.69 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

A 126 x 250 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 1.8229167, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 500 cells (rows x columns) print over 0.25 x 0.59 in, 100 x 238 pixels at 400 dpi, so every 3 rows and every 2 columns are averaged (blank cells left out) into the 126 x 250 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits -5e-09 to 5e-09; no colour bar.

### `example_2_1_boxes.csv` (81 B)

From the subplot "Example 2 1" (row 1, column 2 of the panel's subplots, 5.52-6.11 in across and 3.39-3.41 in down the page), under the page text "Example 2"; x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (seconds) left` | x of the box's left edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Time (seconds) right` | x of the box's right edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |

Filled: yes.
Every box's fill: #bcbdbf.
Every box's outline: none.

### `example_2_4_lines.csv` (82 B)

From the subplot "Example 2 4" (row 4, column 2 of the panel's subplots, 5.52-6.11 in across and 3.80-4.05 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `y` | y position; this axis carries no label |

Line styles: 2 lines: colour #6d6e71, width 0.6 pt, dashed

### `example_2_4_map.csv` (457.5 KB)

From the subplot "Example 2 4" (row 4, column 2 of the panel's subplots, 5.52-6.11 in across and 3.80-4.05 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

A 126 x 250 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 1.8229167, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 500 cells (rows x columns) print over 0.25 x 0.59 in, 100 x 238 pixels at 400 dpi, so every 3 rows and every 2 columns are averaged (blank cells left out) into the 126 x 250 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits -5e-09 to 5e-09; no colour bar.

### `example_2_3_boxes.csv` (81 B)

From the subplot "Example 2 3" (row 3, column 2 of the panel's subplots, 5.52-6.11 in across and 3.75-3.77 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (seconds) left` | x of the box's left edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Time (seconds) right` | x of the box's right edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |

Filled: yes.
Every box's fill: #f6b219.
Every box's outline: none.

### `example_2_6_lines.csv` (82 B)

From the subplot "Example 2 6" (row 6, column 2 of the panel's subplots, 5.52-6.11 in across and 4.16-4.41 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `y` | y position; this axis carries no label |

Line styles: 2 lines: colour #6d6e71, width 0.6 pt, dashed

### `example_2_6_map.csv` (464.0 KB)

From the subplot "Example 2 6" (row 6, column 2 of the panel's subplots, 5.52-6.11 in across and 4.16-4.41 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

A 126 x 250 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 1.8229167, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 500 cells (rows x columns) print over 0.25 x 0.59 in, 100 x 238 pixels at 400 dpi, so every 3 rows and every 2 columns are averaged (blank cells left out) into the 126 x 250 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits -5e-09 to 5e-09; no colour bar.

### `example_2_5_boxes.csv` (81 B)

From the subplot "Example 2 5" (row 5, column 2 of the panel's subplots, 5.52-6.11 in across and 4.11-4.14 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (seconds) left` | x of the box's left edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Time (seconds) right` | x of the box's right edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |

Filled: yes.
Every box's fill: #bcbdbf.
Every box's outline: none.

### `example_2_8_lines.csv` (82 B)

From the subplot "Example 2 8" (row 8, column 2 of the panel's subplots, 5.52-6.11 in across and 4.52-4.77 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `y` | y position; this axis carries no label |

Line styles: 2 lines: colour #6d6e71, width 0.6 pt, dashed

### `example_2_8_map.csv` (462.7 KB)

From the subplot "Example 2 8" (row 8, column 2 of the panel's subplots, 5.52-6.11 in across and 4.52-4.77 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

A 126 x 250 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 1.8229167, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 500 cells (rows x columns) print over 0.25 x 0.59 in, 100 x 238 pixels at 400 dpi, so every 3 rows and every 2 columns are averaged (blank cells left out) into the 126 x 250 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits -5e-09 to 5e-09; no colour bar.

### `example_2_7_boxes.csv` (81 B)

From the subplot "Example 2 7" (row 7, column 2 of the panel's subplots, 5.52-6.11 in across and 4.47-4.50 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (seconds) left` | x of the box's left edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Time (seconds) right` | x of the box's right edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |

Filled: yes.
Every box's fill: #bcbdbf.
Every box's outline: none.

### `example_3_2_lines.csv` (78 B)

From the subplot "Example 3 2" (row 2, column 3 of the panel's subplots, 6.39-6.98 in across and 3.44-3.69 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `y` | y position; this axis carries no label |

Line styles: 2 lines: colour #6d6e71, width 0.6 pt, dashed

### `example_3_2_map.csv` (460.6 KB)

From the subplot "Example 3 2" (row 2, column 3 of the panel's subplots, 6.39-6.98 in across and 3.44-3.69 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

A 126 x 250 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 1.8229167, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 500 cells (rows x columns) print over 0.25 x 0.59 in, 100 x 237 pixels at 400 dpi, so every 3 rows and every 2 columns are averaged (blank cells left out) into the 126 x 250 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits -5e-09 to 5e-09; no colour bar.

### `example_3_1_boxes.csv` (79 B)

From the subplot "Example 3 1" (row 1, column 3 of the panel's subplots, 6.39-6.98 in across and 3.39-3.41 in down the page), under the page text "Example 3"; x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (seconds) left` | x of the box's left edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Time (seconds) right` | x of the box's right edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |

Filled: yes.
Every box's fill: #bcbdbf.
Every box's outline: none.

### `example_3_4_lines.csv` (78 B)

From the subplot "Example 3 4" (row 4, column 3 of the panel's subplots, 6.39-6.98 in across and 3.80-4.05 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `y` | y position; this axis carries no label |

Line styles: 2 lines: colour #6d6e71, width 0.6 pt, dashed

### `example_3_4_map.csv` (461.3 KB)

From the subplot "Example 3 4" (row 4, column 3 of the panel's subplots, 6.39-6.98 in across and 3.80-4.05 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

A 126 x 250 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 1.8229167, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 500 cells (rows x columns) print over 0.25 x 0.59 in, 100 x 237 pixels at 400 dpi, so every 3 rows and every 2 columns are averaged (blank cells left out) into the 126 x 250 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits -5e-09 to 5e-09; no colour bar.

### `example_3_3_boxes.csv` (79 B)

From the subplot "Example 3 3" (row 3, column 3 of the panel's subplots, 6.39-6.98 in across and 3.75-3.77 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (seconds) left` | x of the box's left edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Time (seconds) right` | x of the box's right edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |

Filled: yes.
Every box's fill: #bcbdbf.
Every box's outline: none.

### `example_3_6_lines.csv` (78 B)

From the subplot "Example 3 6" (row 6, column 3 of the panel's subplots, 6.39-6.98 in across and 4.16-4.41 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `y` | y position; this axis carries no label |

Line styles: 2 lines: colour #6d6e71, width 0.6 pt, dashed

### `example_3_6_map.csv` (457.9 KB)

From the subplot "Example 3 6" (row 6, column 3 of the panel's subplots, 6.39-6.98 in across and 4.16-4.41 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

A 126 x 250 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 1.8229167, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 500 cells (rows x columns) print over 0.25 x 0.59 in, 100 x 237 pixels at 400 dpi, so every 3 rows and every 2 columns are averaged (blank cells left out) into the 126 x 250 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits -5e-09 to 5e-09; no colour bar.

### `example_3_5_boxes.csv` (79 B)

From the subplot "Example 3 5" (row 5, column 3 of the panel's subplots, 6.39-6.98 in across and 4.11-4.14 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (seconds) left` | x of the box's left edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Time (seconds) right` | x of the box's right edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |

Filled: yes.
Every box's fill: #4ba647.
Every box's outline: none.

### `example_3_8_lines.csv` (78 B)

From the subplot "Example 3 8" (row 8, column 3 of the panel's subplots, 6.39-6.98 in across and 4.52-4.77 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `y` | y position; this axis carries no label |

Line styles: 2 lines: colour #6d6e71, width 0.6 pt, dashed

### `example_3_8_map.csv` (461.9 KB)

From the subplot "Example 3 8" (row 8, column 3 of the panel's subplots, 6.39-6.98 in across and 4.52-4.77 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

A 126 x 250 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 1.8229167, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 500 cells (rows x columns) print over 0.25 x 0.59 in, 100 x 237 pixels at 400 dpi, so every 3 rows and every 2 columns are averaged (blank cells left out) into the 126 x 250 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits -5e-09 to 5e-09; no colour bar.

### `example_3_7_boxes.csv` (79 B)

From the subplot "Example 3 7" (row 7, column 3 of the panel's subplots, 6.39-6.98 in across and 4.47-4.50 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (seconds) left` | x of the box's left edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Time (seconds) right` | x of the box's right edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |

Filled: yes.
Every box's fill: #bcbdbf.
Every box's outline: none.

### `example_4_2_lines.csv` (82 B)

From the subplot "Example 4 2" (row 2, column 4 of the panel's subplots, 7.26-7.85 in across and 3.44-3.69 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `y` | y position; this axis carries no label |

Line styles: 2 lines: colour #6d6e71, width 0.6 pt, dashed

### `example_4_2_map.csv` (461.7 KB)

From the subplot "Example 4 2" (row 2, column 4 of the panel's subplots, 7.26-7.85 in across and 3.44-3.69 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

A 126 x 250 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 1.8229167, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 500 cells (rows x columns) print over 0.25 x 0.59 in, 100 x 238 pixels at 400 dpi, so every 3 rows and every 2 columns are averaged (blank cells left out) into the 126 x 250 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits -5e-09 to 5e-09; no colour bar.

### `example_4_1_boxes.csv` (81 B)

From the subplot "Example 4 1" (row 1, column 4 of the panel's subplots, 7.26-7.85 in across and 3.39-3.41 in down the page), under the page text "Example 4"; x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (seconds) left` | x of the box's left edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Time (seconds) right` | x of the box's right edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |

Filled: yes.
Every box's fill: #bcbdbf.
Every box's outline: none.

### `example_4_4_lines.csv` (82 B)

From the subplot "Example 4 4" (row 4, column 4 of the panel's subplots, 7.26-7.85 in across and 3.80-4.05 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `y` | y position; this axis carries no label |

Line styles: 2 lines: colour #6d6e71, width 0.6 pt, dashed

### `example_4_4_map.csv` (468.9 KB)

From the subplot "Example 4 4" (row 4, column 4 of the panel's subplots, 7.26-7.85 in across and 3.80-4.05 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

A 126 x 250 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 1.8229167, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 500 cells (rows x columns) print over 0.25 x 0.59 in, 100 x 238 pixels at 400 dpi, so every 3 rows and every 2 columns are averaged (blank cells left out) into the 126 x 250 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits -5e-09 to 5e-09; no colour bar.

### `example_4_3_boxes.csv` (81 B)

From the subplot "Example 4 3" (row 3, column 4 of the panel's subplots, 7.26-7.85 in across and 3.75-3.77 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (seconds) left` | x of the box's left edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Time (seconds) right` | x of the box's right edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |

Filled: yes.
Every box's fill: #bcbdbf.
Every box's outline: none.

### `example_4_6_lines.csv` (82 B)

From the subplot "Example 4 6" (row 6, column 4 of the panel's subplots, 7.26-7.85 in across and 4.16-4.41 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `y` | y position; this axis carries no label |

Line styles: 2 lines: colour #6d6e71, width 0.6 pt, dashed

### `example_4_6_map.csv` (468.2 KB)

From the subplot "Example 4 6" (row 6, column 4 of the panel's subplots, 7.26-7.85 in across and 4.16-4.41 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

A 126 x 250 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 1.8229167, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 500 cells (rows x columns) print over 0.25 x 0.59 in, 100 x 238 pixels at 400 dpi, so every 3 rows and every 2 columns are averaged (blank cells left out) into the 126 x 250 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits -5e-09 to 5e-09; no colour bar.

### `example_4_5_boxes.csv` (81 B)

From the subplot "Example 4 5" (row 5, column 4 of the panel's subplots, 7.26-7.85 in across and 4.11-4.14 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (seconds) left` | x of the box's left edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Time (seconds) right` | x of the box's right edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |

Filled: yes.
Every box's fill: #bcbdbf.
Every box's outline: none.

### `example_4_8_lines.csv` (82 B)

From the subplot "Example 4 8" (row 8, column 4 of the panel's subplots, 7.26-7.85 in across and 4.52-4.77 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `y` | y position; this axis carries no label |

Line styles: 2 lines: colour #6d6e71, width 0.6 pt, dashed

### `example_4_8_map.csv` (447.6 KB)

From the subplot "Example 4 8" (row 8, column 4 of the panel's subplots, 7.26-7.85 in across and 4.52-4.77 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 3 to 12 (values beyond these limits are exported but were not visible).

A 126 x 250 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 1.8229167, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 500 cells (rows x columns) print over 0.25 x 0.59 in, 100 x 238 pixels at 400 dpi, so every 3 rows and every 2 columns are averaged (blank cells left out) into the 126 x 250 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits -5e-09 to 5e-09; no colour bar.

### `example_4_7_boxes.csv` (81 B)

From the subplot "Example 4 7" (row 7, column 4 of the panel's subplots, 7.26-7.85 in across and 4.47-4.50 in down the page); x axis "Time (seconds)"; drawn over x 0 to 1.8229167, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (seconds) left` | x of the box's left edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Time (seconds) right` | x of the box's right edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |

Filled: yes.
Every box's fill: #3e5eaa.
Every box's outline: none.

### `annotations.csv` (269 B)

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
| AxesImage | 16 | 16 |
| Line2D | 32 | 32 |
| Rectangle | 16 | 16 |
