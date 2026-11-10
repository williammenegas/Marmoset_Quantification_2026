# figS5_b_entropy_memory

Figure S5, panel b. Title: "Entropy rate", "Structure", "Memory".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS5/figS5_b_entropy_memory.py`](../../../code/figS5/figS5_b_entropy_memory.py).

## Files

### `entropy_rate_shuffled_observed_lines.csv` (7.5 KB)

From the subplot "Entropy rate Shuffled Observed" (row 1, column 1 of the panel's subplots, 5.04-5.73 in across and 1.15-2.65 in down the page), under the page text "Entropy rate"; y axis "Entropy rate (bits/bout)"; drawn over x 0.5 to 2.5, y 1.8589044 to 5.6538216 (values beyond these limits are exported but were not visible); its x axis prints "Shuffled" at 1, "Observed" at 2.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `Entropy rate (bits/bout)` | y position on the axis labelled "Entropy rate (bits/bout)" (unit: bits/bout) |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `category` | the category named by the nearest x tick label |

Line styles: 92 lines: colour #cccccc, width 0.5 pt; 1 line: colour #262626, width 0.5 pt

### `entropy_rate_shuffled_observed_points.csv` (7.2 KB)

From the subplot "Entropy rate Shuffled Observed" (row 1, column 1 of the panel's subplots, 5.04-5.73 in across and 1.15-2.65 in down the page), under the page text "Entropy rate"; y axis "Entropy rate (bits/bout)"; drawn over x 0.5 to 2.5, y 1.8589044 to 5.6538216 (values beyond these limits are exported but were not visible); its x axis prints "Shuffled" at 1, "Observed" at 2.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position; this axis carries no label; the plotted, jittered position |
| `Entropy rate (bits/bout)` | y position on the axis labelled "Entropy rate (bits/bout)" (unit: bits/bout) |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

Every marker has an area of 6 pt^2.

### `structure_lines.csv` (129 B)

From the subplot "Structure" (row 1, column 2 of the panel's subplots, 6.23-6.67 in across and 1.15-2.65 in down the page), under the page text "Structure"; x axis "All animals"; y axis "Entropy removed by order (%)"; drawn over x 0.5 to 1.5, y 0 to 59.360323 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `All animals` | x position on the axis labelled "All animals" |
| `Entropy removed by order (%)` | y position on the axis labelled "Entropy removed by order (%)" (unit: %) |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |

Line styles: 1 line: colour #000000, width 0.9 pt; 1 line: colour #737373, width 0.5 pt, dashed

### `structure_points.csv` (3.1 KB)

From the subplot "Structure" (row 1, column 2 of the panel's subplots, 6.23-6.67 in across and 1.15-2.65 in down the page), under the page text "Structure"; x axis "All animals"; y axis "Entropy removed by order (%)"; drawn over x 0.5 to 1.5, y 0 to 59.360323 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `All animals` | x position on the axis labelled "All animals" |
| `Entropy removed by order (%)` | y position on the axis labelled "Entropy removed by order (%)" (unit: %) |
| `marker area (pt^2)` | the marker's area, points squared |
| `colour` | the marker's fill colour, hex RGB |

### `memory_lines.csv` (378 B)

From the subplot "Memory" (row 1, column 3 of the panel's subplots, 7.19-7.93 in across and 1.15-2.65 in down the page), under the page text "Memory"; x axis "Lag (bouts)"; y axis "MI above shuffled (bits)"; drawn over x 0.76143389 to 306.00161, y -0.0336825 to 2.2034729 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Lag (bouts)` | x position on the axis labelled "Lag (bouts)" (unit: bouts) |
| `MI above shuffled (bits)` | y position on the axis labelled "MI above shuffled (bits)" (unit: bits) |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |

Line styles: 1 line: colour #212121, width 0.8 pt; 1 line: colour #737373, width 0.5 pt, dashed

### `memory_shapes.csv` (539 B)

From the subplot "Memory" (row 1, column 3 of the panel's subplots, 7.19-7.93 in across and 1.15-2.65 in down the page), under the page text "Memory"; x axis "Lag (bouts)"; y axis "MI above shuffled (bits)"; drawn over x 0.76143389 to 306.00161, y -0.0336825 to 2.2034729 (values beyond these limits are exported but were not visible).

One row is one vertex of one shape's outline, curves sampled.

| Column | Meaning |
|---|---|
| `shape` | which shape, numbered from 1 in drawing order |
| `vertex` | the vertex's place along the outline |
| `Lag (bouts)` | x position on the axis labelled "Lag (bouts)" (unit: bouts) |
| `MI above shuffled (bits)` | y position on the axis labelled "MI above shuffled (bits)" (unit: bits) |

Drawn as: FillBetweenPolyCollection.
Every shape's fill: #2121212e.
Every shape's outline: #2121212e.

### `annotations.csv` (268 B)

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
| FillBetweenPolyCollection | 1 | 1 |
| Line2D | 97 | 97 |
| PathCollection | 4 | 4 |
| Text | 2 | 2 |
