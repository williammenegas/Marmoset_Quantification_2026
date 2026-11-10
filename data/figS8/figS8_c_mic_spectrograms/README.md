# figS8_c_mic_spectrograms

Figure S8, panel c. Title: "Example spectrograms".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS8/figS8_c_mic_spectrograms.py`](../../../code/figS8/figS8_c_mic_spectrograms.py).

## Files

### `example_spectrograms_time_seconds_boxes.csv` (116 B)

From the subplot "Example spectrograms Time (seconds)" (row 2, column 1 of the panel's subplots, 0.78-3.99 in across and 3.37-3.43 in down the page), under the page text "3" / "2" / "1"; x axis "Time (seconds)"; drawn over x 0 to 35, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (seconds) left` | x of the box's left edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Time (seconds) right` | x of the box's right edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |
| `fill colour` | the box's fill colour, hex RGB |

Filled: yes.
Every box's outline: none.

### `mic_1_boxes.csv` (86 B)

From the subplot "Mic. 1" (row 3, column 1 of the panel's subplots, 0.78-3.99 in across and 3.46-3.68 in down the page), marked "Mic. 1" inside; x axis "Time (seconds)"; drawn over x 0 to 35, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (seconds) left` | x of the box's left edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Time (seconds) right` | x of the box's right edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |

Filled: no.
Every box's fill: none.
Every box's outline: #6d6e71.

### `mic_1_map.csv` (3.3 MB)

From the subplot "Mic. 1" (row 3, column 1 of the panel's subplots, 0.78-3.99 in across and 3.46-3.68 in down the page), marked "Mic. 1" inside; x axis "Time (seconds)"; drawn over x 0 to 35, y 3 to 12 (values beyond these limits are exported but were not visible).

A 94 x 2400 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 35, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 2400 cells (rows x columns) print over 0.23 x 3.21 in, 90 x 1282 pixels at 400 dpi, so every 4 rows are averaged (blank cells left out) into the 94 x 2400 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits -5e-09 to 5e-09; no colour bar.

### `mic_1_colour_key.csv` (4.5 KB)

From the subplot "Mic. 1 colour key" (row 3, column 1 of the panel's subplots, its colour key, 4.02-4.07 in across and 3.46-3.68 in down the page); no axis labels; drawn over x -0.5 to 0.5, y 256.5 to -0.5 (values beyond these limits are exported but were not visible).

One row is one step of the key's colour ramp.

| Column | Meaning |
|---|---|
| `ramp value` | the value the key's image holds there |
| `colour` | the colour drawn there, hex RGB |

The key is an image drawn by hand, not a matplotlib colour bar; the page texts beside it name its ends (see annotations.csv).

### `frequency_khz_vs_time_seconds_1_boxes.csv` (269 B)

From the subplot "Frequency (kHz) vs Time (seconds) 1" (row 4, column 1 of the panel's subplots, 0.78-3.99 in across and 3.74-3.80 in down the page); x axis "Time (seconds)"; y axis "Frequency (kHz)"; drawn over x 0 to 35, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (seconds) left` | x of the box's left edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Time (seconds) right` | x of the box's right edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Frequency (kHz) bottom` | y of the box's lower edge on the axis labelled "Frequency (kHz)" (unit: kHz) |
| `Frequency (kHz) top` | y of the box's upper edge on the axis labelled "Frequency (kHz)" (unit: kHz) |
| `fill colour` | the box's fill colour, hex RGB |

Filled: yes.
Every box's outline: none.

### `mic_2_boxes.csv` (235 B)

From the subplot "Mic. 2" (row 5, column 1 of the panel's subplots, 0.78-3.99 in across and 3.83-4.05 in down the page), marked "Mic. 2" inside; x axis "Time (seconds)"; y axis "Frequency (kHz)"; drawn over x 0 to 35, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (seconds) left` | x of the box's left edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Time (seconds) right` | x of the box's right edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Frequency (kHz) bottom` | y of the box's lower edge on the axis labelled "Frequency (kHz)" (unit: kHz) |
| `Frequency (kHz) top` | y of the box's upper edge on the axis labelled "Frequency (kHz)" (unit: kHz) |

Filled: no.
Every box's fill: none.
Every box's outline: #6d6e71.

### `mic_2_map.csv` (3.3 MB)

From the subplot "Mic. 2" (row 5, column 1 of the panel's subplots, 0.78-3.99 in across and 3.83-4.05 in down the page), marked "Mic. 2" inside; x axis "Time (seconds)"; y axis "Frequency (kHz)"; drawn over x 0 to 35, y 3 to 12 (values beyond these limits are exported but were not visible).

A 94 x 2400 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `Frequency (kHz) \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 35, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 2400 cells (rows x columns) print over 0.23 x 3.21 in, 90 x 1282 pixels at 400 dpi, so every 4 rows are averaged (blank cells left out) into the 94 x 2400 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits -5e-09 to 5e-09; no colour bar.

### `mic_2_colour_key.csv` (4.5 KB)

From the subplot "Mic. 2 colour key" (row 5, column 1 of the panel's subplots, its colour key, 4.02-4.07 in across and 3.83-4.05 in down the page); no axis labels; drawn over x -0.5 to 0.5, y 256.5 to -0.5 (values beyond these limits are exported but were not visible).

One row is one step of the key's colour ramp.

| Column | Meaning |
|---|---|
| `ramp value` | the value the key's image holds there |
| `colour` | the colour drawn there, hex RGB |

The key is an image drawn by hand, not a matplotlib colour bar; the page texts beside it name its ends (see annotations.csv).

### `frequency_khz_vs_time_seconds_2_boxes.csv` (396 B)

From the subplot "Frequency (kHz) vs Time (seconds) 2" (row 6, column 1 of the panel's subplots, 0.78-3.99 in across and 4.11-4.17 in down the page); x axis "Time (seconds)"; y axis "Frequency (kHz)"; drawn over x 0 to 35, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (seconds) left` | x of the box's left edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Time (seconds) right` | x of the box's right edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Frequency (kHz) bottom` | y of the box's lower edge on the axis labelled "Frequency (kHz)" (unit: kHz) |
| `Frequency (kHz) top` | y of the box's upper edge on the axis labelled "Frequency (kHz)" (unit: kHz) |
| `fill colour` | the box's fill colour, hex RGB |

Filled: yes.
Every box's outline: none.

### `mic_3_boxes.csv` (358 B)

From the subplot "Mic. 3" (row 7, column 1 of the panel's subplots, 0.78-3.99 in across and 4.19-4.42 in down the page), marked "Mic. 3" inside; x axis "Time (seconds)"; y axis "Frequency (kHz)"; drawn over x 0 to 35, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (seconds) left` | x of the box's left edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Time (seconds) right` | x of the box's right edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Frequency (kHz) bottom` | y of the box's lower edge on the axis labelled "Frequency (kHz)" (unit: kHz) |
| `Frequency (kHz) top` | y of the box's upper edge on the axis labelled "Frequency (kHz)" (unit: kHz) |

Filled: no.
Every box's fill: none.
Every box's outline: #6d6e71.

### `mic_3_map.csv` (3.3 MB)

From the subplot "Mic. 3" (row 7, column 1 of the panel's subplots, 0.78-3.99 in across and 4.19-4.42 in down the page), marked "Mic. 3" inside; x axis "Time (seconds)"; y axis "Frequency (kHz)"; drawn over x 0 to 35, y 3 to 12 (values beyond these limits are exported but were not visible).

A 94 x 2400 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `Frequency (kHz) \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 35, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 2400 cells (rows x columns) print over 0.23 x 3.21 in, 90 x 1282 pixels at 400 dpi, so every 4 rows are averaged (blank cells left out) into the 94 x 2400 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits -5e-09 to 5e-09; no colour bar.

### `mic_3_colour_key.csv` (4.5 KB)

From the subplot "Mic. 3 colour key" (row 7, column 1 of the panel's subplots, its colour key, 4.02-4.07 in across and 4.19-4.42 in down the page); no axis labels; drawn over x -0.5 to 0.5, y 256.5 to -0.5 (values beyond these limits are exported but were not visible).

One row is one step of the key's colour ramp.

| Column | Meaning |
|---|---|
| `ramp value` | the value the key's image holds there |
| `colour` | the colour drawn there, hex RGB |

The key is an image drawn by hand, not a matplotlib colour bar; the page texts beside it name its ends (see annotations.csv).

### `frequency_khz_vs_time_seconds_3_boxes.csv` (145 B)

From the subplot "Frequency (kHz) vs Time (seconds) 3" (row 8, column 1 of the panel's subplots, 0.78-3.99 in across and 4.47-4.53 in down the page); x axis "Time (seconds)"; y axis "Frequency (kHz)"; drawn over x 0 to 35, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (seconds) left` | x of the box's left edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Time (seconds) right` | x of the box's right edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Frequency (kHz) bottom` | y of the box's lower edge on the axis labelled "Frequency (kHz)" (unit: kHz) |
| `Frequency (kHz) top` | y of the box's upper edge on the axis labelled "Frequency (kHz)" (unit: kHz) |
| `fill colour` | the box's fill colour, hex RGB |

Filled: yes.
Every box's outline: none.

### `mic_4_boxes.csv` (87 B)

From the subplot "Mic. 4" (row 9, column 1 of the panel's subplots, 0.78-3.99 in across and 4.56-4.78 in down the page), marked "Mic. 4" inside; x axis "Time (seconds)"; drawn over x 0 to 35, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (seconds) left` | x of the box's left edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Time (seconds) right` | x of the box's right edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |

Filled: no.
Every box's fill: none.
Every box's outline: #6d6e71.

### `mic_4_map.csv` (3.3 MB)

From the subplot "Mic. 4" (row 9, column 1 of the panel's subplots, 0.78-3.99 in across and 4.56-4.78 in down the page), marked "Mic. 4" inside; x axis "Time (seconds)"; drawn over x 0 to 35, y 3 to 12 (values beyond these limits are exported but were not visible).

A 94 x 2400 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 35, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 2400 cells (rows x columns) print over 0.23 x 3.21 in, 90 x 1282 pixels at 400 dpi, so every 4 rows are averaged (blank cells left out) into the 94 x 2400 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits -5e-09 to 5e-09; no colour bar.

### `mic_4_colour_key.csv` (4.5 KB)

From the subplot "Mic. 4 colour key" (row 9, column 1 of the panel's subplots, its colour key, 4.02-4.07 in across and 4.56-4.78 in down the page); no axis labels; drawn over x -0.5 to 0.5, y 256.5 to -0.5 (values beyond these limits are exported but were not visible).

One row is one step of the key's colour ramp.

| Column | Meaning |
|---|---|
| `ramp value` | the value the key's image holds there |
| `colour` | the colour drawn there, hex RGB |

The key is an image drawn by hand, not a matplotlib colour bar; the page texts beside it name its ends (see annotations.csv).

### `time_seconds_boxes.csv` (281 B)

From the subplot "Time (seconds)" (row 1, column 1 of the panel's subplots, 0.00-8.50 in across and 0.00-11.00 in down the page); x axis "Time (seconds)"; drawn over x 0 to 35, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Time (seconds) left` | x of the box's left edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `Time (seconds) right` | x of the box's right edge on the axis labelled "Time (seconds)" (unit: seconds) |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |

Filled: no.
Every box's fill: none.
Every box's outline: #262626.
These shapes are drawn over the page, not in a subplot: the boxes over the four call windows that d shows, and the small boxes round their numbers; x is on the Mic. 1 spectrogram's time axis, y on its frequency axis carried on past its own row.

### `annotations.csv` (390 B)

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
| AxesImage | 8 | 8 |
| Rectangle | 44 | 44 |
| Text | 4 | 4 |
