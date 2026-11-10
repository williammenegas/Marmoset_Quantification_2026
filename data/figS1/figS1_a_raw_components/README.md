# figS1_a_raw_components

Figure S1, panel a. Title: "Components of raw data".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS1/figS1_a_raw_components.py`](../../../code/figS1/figS1_a_raw_components.py).

## Files

### `pc1_points.csv` (6.9 MB)

From the subplot "PC1" (row 1, column 1 of the panel's subplots, 0.62-1.38 in across and 1.33-2.09 in down the page), under the page text "PC1" / "+2 SD" / "-2"; no axis labels; drawn over x -420 to 420, y -420 to 420 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |
| `colour value` | the value the point's colour maps (no colour bar) |

Colour map mb (Normalize) from -2 to 2.
Every marker has an area of 0.9 pt^2.

### `pc1_colour_key.csv` (4.8 KB)

From the subplot "PC1 colour key" (row 1, column 1 of the panel's subplots, its colour key, 0.87-1.38 in across and 1.16-1.21 in down the page); no axis labels; drawn over x -2 to 2, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one step of the key's colour ramp.

| Column | Meaning |
|---|---|
| `ramp value` | the value the key's image holds there |
| `colour` | the colour drawn there, hex RGB |

The key is an image drawn by hand, not a matplotlib colour bar; the page texts beside it name its ends (see annotations.csv).

### `pc1_y_coordinate_points.csv` (4.6 MB)

From the subplot "PC1 Y coordinate" (row 1, column 2 of the panel's subplots, 1.90-2.56 in across and 1.33-1.89 in down the page), under the page text "Y coordinate"; x axis "PC1 score (SD)"; y axis "Y (px)"; drawn over x -3 to 3, y -500 to 500 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `PC1 score (SD)` | x position on the axis labelled "PC1 score (SD)" (unit: SD) |
| `Y (px)` | y position on the axis labelled "Y (px)" (unit: px) |

Every marker has an area of 2 pt^2.
Every marker is filled #2626260d.

### `pc1_plus_0_sd_lines.csv` (1.9 KB)

From the subplot "PC1 +0 SD" (row 1, column 3 of the panel's subplots, 2.74-3.12 in across and 1.33-1.95 in down the page); no axis labels; drawn over x -2.7488518 to 2.7488518, y -2.679554 to 6.2903836 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |

Line styles: 20 lines: colour #262626, width 0.5 pt; 1 line: colour #1f77b4, width 1.5 pt, no line, marker 'o' 2.6 pt, filled #7879b9, edged none

### `pc1_plus_1_sd_lines.csv` (1.9 KB)

From the subplot "PC1 +1 SD" (row 1, column 4 of the panel's subplots, 3.16-3.54 in across and 1.33-1.95 in down the page), under the page text "PC1"; no axis labels; drawn over x -2.7488518 to 2.7488518, y -2.679554 to 6.2903836 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |

Line styles: 20 lines: colour #262626, width 0.5 pt; 1 line: colour #1f77b4, width 1.5 pt, no line, marker 'o' 2.6 pt, filled #9d68ac, edged none

### `pc1_plus_2_sd_lines.csv` (1.9 KB)

From the subplot "PC1 +2 SD" (row 1, column 5 of the panel's subplots, 3.58-3.96 in across and 1.33-1.95 in down the page); no axis labels; drawn over x -2.7488518 to 2.7488518, y -2.679554 to 6.2903836 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |

Line styles: 20 lines: colour #262626, width 0.5 pt; 1 line: colour #1f77b4, width 1.5 pt, no line, marker 'o' 2.6 pt, filled #b9529f, edged none

### `pc2_points.csv` (6.9 MB)

From the subplot "PC2" (row 2, column 1 of the panel's subplots, 0.62-1.38 in across and 2.55-3.31 in down the page), under the page text "PC2" / "+2 SD" / "-2"; no axis labels; drawn over x -420 to 420, y -420 to 420 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |
| `colour value` | the value the point's colour maps (no colour bar) |

Colour map mb (Normalize) from -2 to 2.
Every marker has an area of 0.9 pt^2.

### `pc2_colour_key.csv` (4.8 KB)

From the subplot "PC2 colour key" (row 2, column 1 of the panel's subplots, its colour key, 0.87-1.38 in across and 2.38-2.43 in down the page); no axis labels; drawn over x -2 to 2, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one step of the key's colour ramp.

| Column | Meaning |
|---|---|
| `ramp value` | the value the key's image holds there |
| `colour` | the colour drawn there, hex RGB |

The key is an image drawn by hand, not a matplotlib colour bar; the page texts beside it name its ends (see annotations.csv).

### `pc2_x_coordinate_points.csv` (4.7 MB)

From the subplot "PC2 X coordinate" (row 2, column 2 of the panel's subplots, 1.90-2.56 in across and 2.55-3.11 in down the page), under the page text "X coordinate"; x axis "PC2 score (SD)"; y axis "X (px)"; drawn over x -3 to 3, y -500 to 500 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `PC2 score (SD)` | x position on the axis labelled "PC2 score (SD)" (unit: SD) |
| `X (px)` | y position on the axis labelled "X (px)" (unit: px) |

Every marker has an area of 2 pt^2.
Every marker is filled #2626260d.

### `pc2_plus_0_sd_lines.csv` (1.9 KB)

From the subplot "PC2 +0 SD" (row 2, column 3 of the panel's subplots, 2.74-3.12 in across and 2.55-3.17 in down the page), under the page text "+0 SD"; no axis labels; drawn over x -2.7488518 to 2.7488518, y -2.679554 to 6.2903836 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |

Line styles: 20 lines: colour #262626, width 0.5 pt; 1 line: colour #1f77b4, width 1.5 pt, no line, marker 'o' 2.6 pt, filled #7879b9, edged none

### `pc2_plus_1_sd_lines.csv` (1.9 KB)

From the subplot "PC2 +1 SD" (row 2, column 4 of the panel's subplots, 3.16-3.54 in across and 2.55-3.17 in down the page), under the page text "PC2"; no axis labels; drawn over x -2.7488518 to 2.7488518, y -2.679554 to 6.2903836 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |

Line styles: 20 lines: colour #262626, width 0.5 pt; 1 line: colour #1f77b4, width 1.5 pt, no line, marker 'o' 2.6 pt, filled #9d68ac, edged none

### `pc2_plus_2_sd_lines.csv` (1.9 KB)

From the subplot "PC2 +2 SD" (row 2, column 5 of the panel's subplots, 3.58-3.96 in across and 2.55-3.17 in down the page), under the page text "+2 SD"; no axis labels; drawn over x -2.7488518 to 2.7488518, y -2.679554 to 6.2903836 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |

Line styles: 20 lines: colour #262626, width 0.5 pt; 1 line: colour #1f77b4, width 1.5 pt, no line, marker 'o' 2.6 pt, filled #b9529f, edged none

### `pc3_points.csv` (6.9 MB)

From the subplot "PC3" (row 3, column 1 of the panel's subplots, 0.62-1.38 in across and 3.77-4.53 in down the page), under the page text "PC3" / "+2 SD" / "-2"; no axis labels; drawn over x -420 to 420, y -420 to 420 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |
| `colour value` | the value the point's colour maps (no colour bar) |

Colour map mb (Normalize) from -2 to 2.
Every marker has an area of 0.9 pt^2.

### `pc3_colour_key.csv` (4.8 KB)

From the subplot "PC3 colour key" (row 3, column 1 of the panel's subplots, its colour key, 0.87-1.38 in across and 3.60-3.65 in down the page); no axis labels; drawn over x -2 to 2, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one step of the key's colour ramp.

| Column | Meaning |
|---|---|
| `ramp value` | the value the key's image holds there |
| `colour` | the colour drawn there, hex RGB |

The key is an image drawn by hand, not a matplotlib colour bar; the page texts beside it name its ends (see annotations.csv).

### `pc3_body_angle_points.csv` (4.7 MB)

From the subplot "PC3 Body angle" (row 3, column 2 of the panel's subplots, 1.90-2.56 in across and 3.77-4.33 in down the page), under the page text "Body angle"; x axis "PC3 score (SD)"; y axis "Angle (rad)"; drawn over x -3 to 3, y -3.1415927 to 3.1415927 (values beyond these limits are exported but were not visible); its y axis prints "-π" at -3.1415927, "0" at 0, "π" at 3.1415927.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `PC3 score (SD)` | x position on the axis labelled "PC3 score (SD)" (unit: SD) |
| `Angle (rad)` | y position on the axis labelled "Angle (rad)" (unit: rad) |

Every marker has an area of 2 pt^2.
Every marker is filled #2626260d.

### `pc3_plus_0_sd_lines.csv` (1.9 KB)

From the subplot "PC3 +0 SD" (row 3, column 3 of the panel's subplots, 2.74-3.12 in across and 3.77-4.39 in down the page), under the page text "+0 SD"; no axis labels; drawn over x -2.7488518 to 2.7488518, y -2.679554 to 6.2903836 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |

Line styles: 20 lines: colour #262626, width 0.5 pt; 1 line: colour #1f77b4, width 1.5 pt, no line, marker 'o' 2.6 pt, filled #7879b9, edged none

### `pc3_plus_1_sd_lines.csv` (1.9 KB)

From the subplot "PC3 +1 SD" (row 3, column 4 of the panel's subplots, 3.16-3.54 in across and 3.77-4.39 in down the page), under the page text "PC3"; no axis labels; drawn over x -2.7488518 to 2.7488518, y -2.679554 to 6.2903836 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |

Line styles: 20 lines: colour #262626, width 0.5 pt; 1 line: colour #1f77b4, width 1.5 pt, no line, marker 'o' 2.6 pt, filled #9d68ac, edged none

### `pc3_plus_2_sd_lines.csv` (1.9 KB)

From the subplot "PC3 +2 SD" (row 3, column 5 of the panel's subplots, 3.58-3.96 in across and 3.77-4.39 in down the page), under the page text "+2 SD"; no axis labels; drawn over x -2.7488518 to 2.7488518, y -2.679554 to 6.2903836 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |

Line styles: 20 lines: colour #262626, width 0.5 pt; 1 line: colour #1f77b4, width 1.5 pt, no line, marker 'o' 2.6 pt, filled #b9529f, edged none

### `pc4_points.csv` (6.9 MB)

From the subplot "PC4" (row 4, column 1 of the panel's subplots, 0.62-1.38 in across and 4.99-5.75 in down the page), under the page text "PC4" / "+2 SD" / "-2"; no axis labels; drawn over x -420 to 420, y -420 to 420 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |
| `colour value` | the value the point's colour maps (no colour bar) |

Colour map mb (Normalize) from -2 to 2.
Every marker has an area of 0.9 pt^2.

### `pc4_colour_key.csv` (4.8 KB)

From the subplot "PC4 colour key" (row 4, column 1 of the panel's subplots, its colour key, 0.87-1.38 in across and 4.82-4.87 in down the page); no axis labels; drawn over x -2 to 2, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one step of the key's colour ramp.

| Column | Meaning |
|---|---|
| `ramp value` | the value the key's image holds there |
| `colour` | the colour drawn there, hex RGB |

The key is an image drawn by hand, not a matplotlib colour bar; the page texts beside it name its ends (see annotations.csv).

### `pc4_body_angle_points.csv` (4.7 MB)

From the subplot "PC4 Body angle" (row 4, column 2 of the panel's subplots, 1.90-2.56 in across and 4.99-5.55 in down the page), under the page text "Body angle"; x axis "PC4 score (SD)"; y axis "Angle (rad)"; drawn over x -3 to 3, y -3.1415927 to 3.1415927 (values beyond these limits are exported but were not visible); its y axis prints "-π" at -3.1415927, "0" at 0, "π" at 3.1415927.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `PC4 score (SD)` | x position on the axis labelled "PC4 score (SD)" (unit: SD) |
| `Angle (rad)` | y position on the axis labelled "Angle (rad)" (unit: rad) |

Every marker has an area of 2 pt^2.
Every marker is filled #2626260d.

### `pc4_plus_0_sd_lines.csv` (1.9 KB)

From the subplot "PC4 +0 SD" (row 4, column 3 of the panel's subplots, 2.74-3.12 in across and 4.99-5.61 in down the page), under the page text "+0 SD"; no axis labels; drawn over x -2.7488518 to 2.7488518, y -2.679554 to 6.2903836 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |

Line styles: 20 lines: colour #262626, width 0.5 pt; 1 line: colour #1f77b4, width 1.5 pt, no line, marker 'o' 2.6 pt, filled #7879b9, edged none

### `pc4_plus_1_sd_lines.csv` (1.9 KB)

From the subplot "PC4 +1 SD" (row 4, column 4 of the panel's subplots, 3.16-3.54 in across and 4.99-5.61 in down the page), under the page text "PC4"; no axis labels; drawn over x -2.7488518 to 2.7488518, y -2.679554 to 6.2903836 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |

Line styles: 20 lines: colour #262626, width 0.5 pt; 1 line: colour #1f77b4, width 1.5 pt, no line, marker 'o' 2.6 pt, filled #9d68ac, edged none

### `pc4_plus_2_sd_lines.csv` (1.9 KB)

From the subplot "PC4 +2 SD" (row 4, column 5 of the panel's subplots, 3.58-3.96 in across and 4.99-5.61 in down the page), under the page text "+2 SD"; no axis labels; drawn over x -2.7488518 to 2.7488518, y -2.679554 to 6.2903836 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |

Line styles: 20 lines: colour #262626, width 0.5 pt; 1 line: colour #1f77b4, width 1.5 pt, no line, marker 'o' 2.6 pt, filled #b9529f, edged none

### `page_shapes.csv` (26.0 KB)

Drawn on the page around the panel's subplots, not in one of them: 4 FancyArrowPatch, 1 Line2D.

One row is one vertex of one shape drawn on the page.

| Column | Meaning |
|---|---|
| `shape` | which shape, numbered from 1 in drawing order |
| `part` | which piece of the shape (an arrow's shaft and head) |
| `vertex` | the vertex's place along the shape |
| `x (in)` | inches from the page's left edge |
| `y (in)` | inches down from the page's top edge |
| `shape type` | the matplotlib artist that drew it |
| `fill colour` | the shape's fill colour, hex RGB; none for a line |

Every line's colour: #262626.
Every line's width (pt): 0.6.
Every line is: solid.
These are drawn on the page around the panel's subplots, not in one of them, so they are given in page inches, not in data coordinates. A shape that does not end where it starts is an open line.

### `annotations.csv` (1.2 KB)

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
| Line2D | 272 | 252 |
| PathCollection | 8 | 8 |
| FancyArrowPatch (on the page) | 4 | 4 |
| Line2D (on the page) | 1 | 1 |
