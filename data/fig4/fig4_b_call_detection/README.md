# fig4_b_call_detection

Figure 4, panel b. No title is printed on this panel.

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig4/fig4_b_call_detection.py`](../../../code/fig4/fig4_b_call_detection.py).

## Files

### `frequency_khz_vs_time_minutes_1_lines.csv` (62 B)

From the subplot "Frequency (kHz) vs Time (minutes) 1" (row 1, column 1 of the panel's subplots, 3.96-7.79 in across and 0.58-1.14 in down the page); x axis "Time (minutes)"; y axis "Frequency (kHz)"; drawn over x 0 to 15, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (minutes)` | x position on the axis labelled "Time (minutes)" (unit: minutes) |
| `Frequency (kHz)` | y position on the axis labelled "Frequency (kHz)" (unit: kHz) |

Line styles: 2 lines: colour #cccccc, width 0.5 pt, dashed

### `frequency_khz_vs_time_minutes_1_map.csv` (12.9 MB)

From the subplot "Frequency (kHz) vs Time (minutes) 1" (row 1, column 1 of the panel's subplots, 3.96-7.79 in across and 0.58-1.14 in down the page); x axis "Time (minutes)"; y axis "Frequency (kHz)"; drawn over x 0 to 15, y 3 to 12 (values beyond these limits are exported but were not visible).

A 376 x 2465 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `Frequency (kHz) \ Time (minutes)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 14.978299, y 3 to 12 (lower origin).
Colour map from_list (Normalize), limits 0 to 1e-06; no colour bar.

### `frequency_khz_vs_time_minutes_1_colour_key.csv` (4.8 KB)

From the subplot "Frequency (kHz) vs Time (minutes) 1 colour key" (row 1, column 1 of the panel's subplots, its colour key, 8.01-8.06 in across and 0.65-1.07 in down the page); no axis labels; drawn over x 0 to 1, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one step of the key's colour ramp.

| Column | Meaning |
|---|---|
| `ramp value` | the value the key's image holds there |
| `colour` | the colour drawn there, hex RGB |

The key is an image drawn by hand, not a matplotlib colour bar; the page texts beside it name its ends (see annotations.csv).

### `frequency_khz_vs_time_minutes_2_lines.csv` (62 B)

From the subplot "Frequency (kHz) vs Time (minutes) 2" (row 2, column 1 of the panel's subplots, 3.96-7.79 in across and 1.39-1.95 in down the page); x axis "Time (minutes)"; y axis "Frequency (kHz)"; drawn over x 0 to 15, y 3 to 12 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time (minutes)` | x position on the axis labelled "Time (minutes)" (unit: minutes) |
| `Frequency (kHz)` | y position on the axis labelled "Frequency (kHz)" (unit: kHz) |

Line styles: 2 lines: colour #cccccc, width 0.5 pt, dashed

### `frequency_khz_vs_time_minutes_2_map.csv` (12.9 MB)

From the subplot "Frequency (kHz) vs Time (minutes) 2" (row 2, column 1 of the panel's subplots, 3.96-7.79 in across and 1.39-1.95 in down the page); x axis "Time (minutes)"; y axis "Frequency (kHz)"; drawn over x 0 to 15, y 3 to 12 (values beyond these limits are exported but were not visible).

A 376 x 2465 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `Frequency (kHz) \ Time (minutes)` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0 to 14.978299, y 3 to 12 (lower origin).
Colour map from_list (Normalize), limits 0 to 1e-06; no colour bar.

### `frequency_khz_vs_time_minutes_2_colour_key.csv` (4.8 KB)

From the subplot "Frequency (kHz) vs Time (minutes) 2 colour key" (row 2, column 1 of the panel's subplots, its colour key, 8.01-8.06 in across and 1.46-1.88 in down the page); no axis labels; drawn over x 0 to 1, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one step of the key's colour ramp.

| Column | Meaning |
|---|---|
| `ramp value` | the value the key's image holds there |
| `colour` | the colour drawn there, hex RGB |

The key is an image drawn by hand, not a matplotlib colour bar; the page texts beside it name its ends (see annotations.csv).

### `annotations.csv` (339 B)

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
| AxesImage | 4 | 4 |
| Line2D | 4 | 4 |
| Text | 2 | 2 |
