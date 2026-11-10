# figS9_a_classifier_design

Figure S9, panel a. Title: "Microphone data", "Spectrogram", "RNN", "Dense", "Softmax".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS9/figS9_a_classifier_design.py`](../../../code/figS9/figS9_a_classifier_design.py).

## Files

### `microphone_data_1_lines.csv` (146 B)

From the subplot "Microphone data 1" (row 2, column 1 of the panel's subplots, 1.05-1.59 in across and 1.12-1.33 in down the page), under the page text "Microphone data"; x axis "Time (seconds)"; y axis "Frequency (kHz)"; drawn over x 0 to 6, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `Frequency (kHz)` | y position on the axis labelled "Frequency (kHz)" (unit: kHz) |

Line styles: 4 lines: colour #6d6e71, width 0.5 pt, dashed

### `microphone_data_1_map.csv` (244.8 KB)

From the subplot "Microphone data 1" (row 2, column 1 of the panel's subplots, 1.05-1.59 in across and 1.12-1.33 in down the page), under the page text "Microphone data"; x axis "Time (seconds)"; y axis "Frequency (kHz)"; drawn over x 0 to 6, y 3 to 12 (values beyond these limits are exported but were not visible).

A 94 x 236 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `Frequency (kHz) \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 6, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 1646 cells (rows x columns) print over 0.21 x 0.54 in, 83 x 216 pixels at 400 dpi, so every 4 rows and every 7 columns are averaged (blank cells left out) into the 94 x 236 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits -18 to -10; no colour bar.

### `microphone_data_2_lines.csv` (146 B)

From the subplot "Microphone data 2" (row 3, column 1 of the panel's subplots, 1.05-1.59 in across and 1.42-1.63 in down the page); x axis "Time (seconds)"; y axis "Frequency (kHz)"; drawn over x 0 to 6, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `Frequency (kHz)` | y position on the axis labelled "Frequency (kHz)" (unit: kHz) |

Line styles: 4 lines: colour #6d6e71, width 0.5 pt, dashed

### `microphone_data_2_map.csv` (244.9 KB)

From the subplot "Microphone data 2" (row 3, column 1 of the panel's subplots, 1.05-1.59 in across and 1.42-1.63 in down the page); x axis "Time (seconds)"; y axis "Frequency (kHz)"; drawn over x 0 to 6, y 3 to 12 (values beyond these limits are exported but were not visible).

A 94 x 236 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `Frequency (kHz) \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 6, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 1646 cells (rows x columns) print over 0.21 x 0.54 in, 84 x 216 pixels at 400 dpi, so every 4 rows and every 7 columns are averaged (blank cells left out) into the 94 x 236 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits -18 to -10; no colour bar.

### `microphone_data_3_lines.csv` (146 B)

From the subplot "Microphone data 3" (row 4, column 1 of the panel's subplots, 1.05-1.59 in across and 1.71-1.92 in down the page); x axis "Time (seconds)"; y axis "Frequency (kHz)"; drawn over x 0 to 6, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `Frequency (kHz)` | y position on the axis labelled "Frequency (kHz)" (unit: kHz) |

Line styles: 4 lines: colour #6d6e71, width 0.5 pt, dashed

### `microphone_data_3_map.csv` (244.9 KB)

From the subplot "Microphone data 3" (row 4, column 1 of the panel's subplots, 1.05-1.59 in across and 1.71-1.92 in down the page); x axis "Time (seconds)"; y axis "Frequency (kHz)"; drawn over x 0 to 6, y 3 to 12 (values beyond these limits are exported but were not visible).

A 94 x 236 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `Frequency (kHz) \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 6, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 1646 cells (rows x columns) print over 0.21 x 0.54 in, 84 x 216 pixels at 400 dpi, so every 4 rows and every 7 columns are averaged (blank cells left out) into the 94 x 236 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits -18 to -10; no colour bar.

### `microphone_data_4_lines.csv` (146 B)

From the subplot "Microphone data 4" (row 5, column 1 of the panel's subplots, 1.05-1.59 in across and 2.01-2.22 in down the page); x axis "Time (seconds)"; y axis "Frequency (kHz)"; drawn over x 0 to 6, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `Frequency (kHz)` | y position on the axis labelled "Frequency (kHz)" (unit: kHz) |

Line styles: 4 lines: colour #6d6e71, width 0.5 pt, dashed

### `microphone_data_4_map.csv` (244.9 KB)

From the subplot "Microphone data 4" (row 5, column 1 of the panel's subplots, 1.05-1.59 in across and 2.01-2.22 in down the page); x axis "Time (seconds)"; y axis "Frequency (kHz)"; drawn over x 0 to 6, y 3 to 12 (values beyond these limits are exported but were not visible).

A 94 x 236 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `Frequency (kHz) \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 6, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 1646 cells (rows x columns) print over 0.21 x 0.54 in, 84 x 216 pixels at 400 dpi, so every 4 rows and every 7 columns are averaged (blank cells left out) into the 94 x 236 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits -18 to -10; no colour bar.

### `microphone_data_2_colour_key.csv` (4.8 KB)

From the subplot "Microphone data 2 colour key" (row 3, column 1 of the panel's subplots, its colour key, 1.70-1.76 in across and 1.39-2.01 in down the page); no axis labels; drawn over x -0.5 to 0.5, y 255.5 to -0.5 (values beyond these limits are exported but were not visible).

One row is one step of the key's colour ramp.

| Column | Meaning |
|---|---|
| `ramp value` | the value the key's image holds there |
| `colour` | the colour drawn there, hex RGB |

The key is an image drawn by hand, not a matplotlib colour bar; the page texts beside it name its ends (see annotations.csv).

### `schematic_lines.csv` (1.3 KB)

From the subplot "schematic" (row 1, column 1 of the panel's subplots, 0.02-8.52 in across and -0.01-10.99 in down the page); no axis labels; drawn over x 0 to 8.5, y 11 to 0 (values beyond these limits are exported but were not visible); it covers the page, so its x and y are inches across and down the page from its top-left corner.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |

Line styles: 1 line: colour #262626, width 1 pt

### `schematic_boxes.csv` (50 B)

From the subplot "schematic" (row 1, column 1 of the panel's subplots, 0.02-8.52 in across and -0.01-10.99 in down the page); no axis labels; drawn over x 0 to 8.5, y 11 to 0 (values beyond these limits are exported but were not visible); it covers the page, so its x and y are inches across and down the page from its top-left corner.

One row is one rectangle.

| Column | Meaning |
|---|---|
| `x left` | x of the box's left edge; this axis carries no label |
| `x right` | x of the box's right edge; this axis carries no label |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |

Filled: no.
Every box's fill: none.
Every box's outline: #6d6e71.

### `schematic_shapes.csv` (49.9 KB)

From the subplot "schematic" (row 1, column 1 of the panel's subplots, 0.02-8.52 in across and -0.01-10.99 in down the page); no axis labels; drawn over x 0 to 8.5, y 11 to 0 (values beyond these limits are exported but were not visible); it covers the page, so its x and y are inches across and down the page from its top-left corner.

One row is one vertex of one shape's outline, curves sampled.

| Column | Meaning |
|---|---|
| `shape` | which shape, numbered from 1 in drawing order |
| `vertex` | the vertex's place along the outline |
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |
| `shape type` | the matplotlib artist that drew it |
| `fill colour` | the shape's fill colour, hex RGB |
| `edge colour` | the shape's outline colour, hex RGB |

### `annotations.csv` (851 B)

Every text printed in the panel: inside a subplot (x and y in that subplot's data coordinates; for an annotation with a leader line, the point it marks in `target x` and `target y`) or on the page around the subplots (x and y in inches from the page's top-left: the text's anchor).

| Column | Meaning |
|---|---|
| `subplot` | the subplot the text is in; blank for page text |
| `text` | the text as printed, on one line |
| `x`, `y` | its position (see `coordinates`) |
| `coordinates` | "data" or "page inches" |

## Schematics

The subplot "schematic" is the network, drawn as labelled boxes and arrows. Its shapes are exported as drawn, in the subplot's own coordinates, and its texts are in annotations.csv; they show a design, not measurements.

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- nothing else

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| AxesImage | 5 | 5 |
| FancyBboxPatch | 13 | 13 |
| Line2D | 17 | 17 |
| Polygon | 5 | 5 |
| Rectangle | 1 | 1 |
| Text | 4 | 4 |
