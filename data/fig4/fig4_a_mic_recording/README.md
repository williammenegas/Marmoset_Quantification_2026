# fig4_a_mic_recording

Figure 4, panel a. Title: "Recording", "Amplitude", "Spectrogram".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig4/fig4_a_mic_recording.py`](../../../code/fig4/fig4_a_mic_recording.py).

The recording layout -- grey boxes, cages and microphone marks -- is a schematic drawn by code; its shapes are exported as drawn, not as measurements.

## Files

### `recording_lines.csv` (950 B)

From the subplot "Recording" (row 1, column 1 of the panel's subplots, 0.54-1.46 in across and 0.62-2.18 in down the page), under the page text "Recording"; no axis labels; drawn over x 0.5444 to 1.4644, y 2.18 to 0.62 (values beyond these limits are exported but were not visible).

One row is one x value shared by the lines; one column per line.

| Column | Meaning |
|---|---|
| `x` | x position; this axis carries no label |
| `#262626` | the line "#262626": y position; this axis carries no label |
| `#262626 (2)` | the line "#262626 (2)": y position; this axis carries no label |

Lines: "#262626": colour #262626, width 0.4 pt; "#262626 (2)": colour #262626, width 0.4 pt

### `recording_lines_2.csv` (928 B)

From the subplot "Recording" (row 1, column 1 of the panel's subplots, 0.54-1.46 in across and 0.62-2.18 in down the page), under the page text "Recording"; no axis labels; drawn over x 0.5444 to 1.4644, y 2.18 to 0.62 (values beyond these limits are exported but were not visible).

One row is one x value shared by the lines; one column per line.

| Column | Meaning |
|---|---|
| `x` | x position; this axis carries no label |
| `#262626` | the line "#262626": y position; this axis carries no label |
| `#262626 (2)` | the line "#262626 (2)": y position; this axis carries no label |

Lines: "#262626": colour #262626, width 0.4 pt; "#262626 (2)": colour #262626, width 0.4 pt

### `recording_other_lines.csv` (1.5 KB)

From the subplot "Recording" (row 1, column 1 of the panel's subplots, 0.54-1.46 in across and 0.62-2.18 in down the page), under the page text "Recording"; no axis labels; drawn over x 0.5444 to 1.4644, y 2.18 to 0.62 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |

Line styles: 7 lines: colour #919494, width 0.5 pt, dashed; 16 lines: colour #000000, width 0.5 pt; 8 lines: colour #262626, width 0.4 pt

### `recording_boxes.csv` (238 B)

From the subplot "Recording" (row 1, column 1 of the panel's subplots, 0.54-1.46 in across and 0.62-2.18 in down the page), under the page text "Recording"; no axis labels; drawn over x 0.5444 to 1.4644, y 2.18 to 0.62 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `x left` | x of the box's left edge; this axis carries no label |
| `x right` | x of the box's right edge; this axis carries no label |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |

Filled: yes.
Every box's fill: none.
Every box's outline: #000000.

### `recording_shapes.csv` (21.2 KB)

From the subplot "Recording" (row 1, column 1 of the panel's subplots, 0.54-1.46 in across and 0.62-2.18 in down the page), under the page text "Recording"; no axis labels; drawn over x 0.5444 to 1.4644, y 2.18 to 0.62 (values beyond these limits are exported but were not visible).

One row is one vertex of one shape's outline, curves sampled.

| Column | Meaning |
|---|---|
| `shape` | which shape, numbered from 1 in drawing order |
| `vertex` | the vertex's place along the outline |
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |
| `fill colour` | the shape's fill colour, hex RGB |
| `edge colour` | the shape's outline colour, hex RGB |

Drawn as: FancyBboxPatch.

### `amplitude_1_lines.csv` (132 B)

From the subplot "Amplitude 1" (row 1, column 2 of the panel's subplots, 1.68-2.28 in across and 0.67-0.91 in down the page), under the page text "Amplitude"; x axis "Time (seconds)"; drawn over x 0 to 6, y -1 to 1 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `y` | y position; this axis carries no label |

Line styles: 4 lines: colour #bdbdbf, width 0.33 pt, dashed

### `amplitude_1_shapes.csv` (151.8 KB)

From the subplot "Amplitude 1" (row 1, column 2 of the panel's subplots, 1.68-2.28 in across and 0.67-0.91 in down the page), under the page text "Amplitude"; x axis "Time (seconds)"; drawn over x 0 to 6, y -1 to 1 (values beyond these limits are exported but were not visible).

One row is one vertex of one shape's outline, curves sampled.

| Column | Meaning |
|---|---|
| `shape` | which shape, numbered from 1 in drawing order |
| `vertex` | the vertex's place along the outline |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `y` | y position; this axis carries no label |

Drawn as: FillBetweenPolyCollection.
Every shape's fill: #212121.
Every shape's outline: #212121.

### `spectrogram_1_lines.csv` (134 B)

From the subplot "Spectrogram 1" (row 1, column 3 of the panel's subplots, 2.60-3.20 in across and 0.67-0.91 in down the page), under the page text "Spectrogram"; x axis "Time (seconds)"; y axis "kHz"; drawn over x 0 to 6, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `kHz` | y position on the axis labelled "kHz" |

Line styles: 4 lines: colour #bdbdbf, width 0.33 pt, dashed

### `spectrogram_1_map.csv` (362.7 KB)

From the subplot "Spectrogram 1" (row 1, column 3 of the panel's subplots, 2.60-3.20 in across and 0.67-0.91 in down the page), under the page text "Spectrogram"; x axis "Time (seconds)"; y axis "kHz"; drawn over x 0 to 6, y 3 to 12 (values beyond these limits are exported but were not visible).

A 94 x 275 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `kHz \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 6, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 1646 cells (rows x columns) print over 0.24 x 0.60 in, 94 x 240 pixels at 400 dpi, so every 4 rows and every 6 columns are averaged (blank cells left out) into the 94 x 275 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits 0 to 5e-07; no colour bar.

### `amplitude_2_lines.csv` (132 B)

From the subplot "Amplitude 2" (row 2, column 1 of the panel's subplots, 1.68-2.28 in across and 1.00-1.24 in down the page); x axis "Time (seconds)"; drawn over x 0 to 6, y -1 to 1 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `y` | y position; this axis carries no label |

Line styles: 4 lines: colour #bdbdbf, width 0.33 pt, dashed

### `amplitude_2_shapes.csv` (152.1 KB)

From the subplot "Amplitude 2" (row 2, column 1 of the panel's subplots, 1.68-2.28 in across and 1.00-1.24 in down the page); x axis "Time (seconds)"; drawn over x 0 to 6, y -1 to 1 (values beyond these limits are exported but were not visible).

One row is one vertex of one shape's outline, curves sampled.

| Column | Meaning |
|---|---|
| `shape` | which shape, numbered from 1 in drawing order |
| `vertex` | the vertex's place along the outline |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `y` | y position; this axis carries no label |

Drawn as: FillBetweenPolyCollection.
Every shape's fill: #212121.
Every shape's outline: #212121.

### `spectrogram_2_lines.csv` (134 B)

From the subplot "Spectrogram 2" (row 2, column 2 of the panel's subplots, 2.60-3.20 in across and 1.00-1.24 in down the page); x axis "Time (seconds)"; y axis "kHz"; drawn over x 0 to 6, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `kHz` | y position on the axis labelled "kHz" |

Line styles: 4 lines: colour #bdbdbf, width 0.33 pt, dashed

### `spectrogram_2_map.csv` (362.7 KB)

From the subplot "Spectrogram 2" (row 2, column 2 of the panel's subplots, 2.60-3.20 in across and 1.00-1.24 in down the page); x axis "Time (seconds)"; y axis "kHz"; drawn over x 0 to 6, y 3 to 12 (values beyond these limits are exported but were not visible).

A 94 x 275 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `kHz \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 6, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 1646 cells (rows x columns) print over 0.24 x 0.60 in, 94 x 240 pixels at 400 dpi, so every 4 rows and every 6 columns are averaged (blank cells left out) into the 94 x 275 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits 0 to 5e-07; no colour bar.

### `amplitude_3_lines.csv` (132 B)

From the subplot "Amplitude 3" (row 3, column 1 of the panel's subplots, 1.68-2.28 in across and 1.32-1.56 in down the page); x axis "Time (seconds)"; drawn over x 0 to 6, y -1 to 1 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `y` | y position; this axis carries no label |

Line styles: 4 lines: colour #bdbdbf, width 0.33 pt, dashed

### `amplitude_3_shapes.csv` (153.5 KB)

From the subplot "Amplitude 3" (row 3, column 1 of the panel's subplots, 1.68-2.28 in across and 1.32-1.56 in down the page); x axis "Time (seconds)"; drawn over x 0 to 6, y -1 to 1 (values beyond these limits are exported but were not visible).

One row is one vertex of one shape's outline, curves sampled.

| Column | Meaning |
|---|---|
| `shape` | which shape, numbered from 1 in drawing order |
| `vertex` | the vertex's place along the outline |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `y` | y position; this axis carries no label |

Drawn as: FillBetweenPolyCollection.
Every shape's fill: #212121.
Every shape's outline: #212121.

### `spectrogram_3_lines.csv` (134 B)

From the subplot "Spectrogram 3" (row 3, column 2 of the panel's subplots, 2.60-3.20 in across and 1.32-1.56 in down the page); x axis "Time (seconds)"; y axis "kHz"; drawn over x 0 to 6, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `kHz` | y position on the axis labelled "kHz" |

Line styles: 4 lines: colour #bdbdbf, width 0.33 pt, dashed

### `spectrogram_3_map.csv` (362.7 KB)

From the subplot "Spectrogram 3" (row 3, column 2 of the panel's subplots, 2.60-3.20 in across and 1.32-1.56 in down the page); x axis "Time (seconds)"; y axis "kHz"; drawn over x 0 to 6, y 3 to 12 (values beyond these limits are exported but were not visible).

A 94 x 275 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `kHz \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 6, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 1646 cells (rows x columns) print over 0.24 x 0.60 in, 94 x 240 pixels at 400 dpi, so every 4 rows and every 6 columns are averaged (blank cells left out) into the 94 x 275 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits 0 to 5e-07; no colour bar.

### `amplitude_4_lines.csv` (132 B)

From the subplot "Amplitude 4" (row 4, column 1 of the panel's subplots, 1.68-2.28 in across and 1.66-1.90 in down the page); x axis "Time (seconds)"; drawn over x 0 to 6, y -1 to 1 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `y` | y position; this axis carries no label |

Line styles: 4 lines: colour #bdbdbf, width 0.33 pt, dashed

### `amplitude_4_shapes.csv` (153.5 KB)

From the subplot "Amplitude 4" (row 4, column 1 of the panel's subplots, 1.68-2.28 in across and 1.66-1.90 in down the page); x axis "Time (seconds)"; drawn over x 0 to 6, y -1 to 1 (values beyond these limits are exported but were not visible).

One row is one vertex of one shape's outline, curves sampled.

| Column | Meaning |
|---|---|
| `shape` | which shape, numbered from 1 in drawing order |
| `vertex` | the vertex's place along the outline |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `y` | y position; this axis carries no label |

Drawn as: FillBetweenPolyCollection.
Every shape's fill: #212121.
Every shape's outline: #212121.

### `spectrogram_4_lines.csv` (134 B)

From the subplot "Spectrogram 4" (row 4, column 2 of the panel's subplots, 2.60-3.20 in across and 1.66-1.90 in down the page); x axis "Time (seconds)"; y axis "kHz"; drawn over x 0 to 6, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (seconds)` | x position on the axis labelled "Time (seconds)" (unit: seconds) |
| `kHz` | y position on the axis labelled "kHz" |

Line styles: 4 lines: colour #bdbdbf, width 0.33 pt, dashed

### `spectrogram_4_map.csv` (362.7 KB)

From the subplot "Spectrogram 4" (row 4, column 2 of the panel's subplots, 2.60-3.20 in across and 1.66-1.90 in down the page); x axis "Time (seconds)"; y axis "kHz"; drawn over x 0 to 6, y 3 to 12 (values beyond these limits are exported but were not visible).

A 94 x 275 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `kHz \ Time (seconds)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 6, y 3 to 12 (lower origin).
Averaged to print resolution: the image's 376 x 1646 cells (rows x columns) print over 0.24 x 0.60 in, 94 x 240 pixels at 400 dpi, so every 4 rows and every 6 columns are averaged (blank cells left out) into the 94 x 275 cells here, still at least one per printed pixel, each cell's x and y the means of the centres it covers. The extent and the colour limits are those drawn.
Colour map from_list (Normalize), limits 0 to 5e-07; no colour bar.

### `annotations.csv` (611 B)

Every text printed in the panel: inside a subplot (x and y in that subplot's data coordinates; for an annotation with a leader line, the point it marks in `target x` and `target y`) or on the page around the subplots (x and y in inches from the page's top-left: the text's anchor).

| Column | Meaning |
|---|---|
| `subplot` | the subplot the text is in; blank for page text |
| `text` | the text as printed, on one line |
| `x`, `y` | its position (see `coordinates`) |
| `coordinates` | "data" or "page inches" |

## Schematics

The subplot "Recording" is the recording layout, drawn as boxes, cages and microphone marks. Its shapes are exported as drawn, in the subplot's own coordinates, and its texts are in annotations.csv; they show a design, not measurements.

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- decoration: the light frame round each row of microphone traces: 8 Rectangle

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| AxesImage | 4 | 4 |
| FancyBboxPatch | 8 | 8 |
| FillBetweenPolyCollection | 4 | 4 |
| Line2D | 67 | 67 |
| Rectangle | 16 | 8 |
| Text | 12 | 12 |
