# fig1_d_paths_by_id

Figure 1, panel d. Title: "Sorted by ID".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig1/fig1_d_paths_by_id.py`](../../../code/fig1/fig1_d_paths_by_id.py).

The marmoset-head icons beside the animals' names are artwork pasted in Illustrator; not drawn by code.

## Files

### `animal_1_lines.csv` (221.7 KB)

From the subplot "Animal 1" (row 1, column 1 of the panel's subplots, 4.44-5.25 in across and 2.89-3.69 in down the page), under the page text "Animal 1"; x axis "Position (X)"; y axis "Position (Y)"; drawn over x -490.52348 to 490.52348, y -490.52348 to 490.52348 (values beyond these limits are exported but were not visible); its x axis prints "0" at -400, "400" at 0, "800" at 400; its y axis prints "0" at -400, "400" at 0, "800" at 400.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Position (X)` | x position on the axis labelled "Position (X)" |
| `Position (Y)` | y position on the axis labelled "Position (Y)" |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |

Line styles: 13 lines: colour #d1d4d4, width 0.5 pt; 1 line: colour #211f1f, width 0.75 pt

### `animal_2_lines.csv` (225.6 KB)

From the subplot "Animal 2" (row 1, column 2 of the panel's subplots, 5.36-6.16 in across and 2.89-3.69 in down the page), under the page text "Animal 2"; x axis "Position (X)"; y axis "Position (Y)"; drawn over x -490.52348 to 490.52348, y -490.52348 to 490.52348 (values beyond these limits are exported but were not visible); its x axis prints "0" at -400, "400" at 0, "800" at 400.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Position (X)` | x position on the axis labelled "Position (X)" |
| `Position (Y)` | y position on the axis labelled "Position (Y)" |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |

Line styles: 13 lines: colour #fcc2d4, width 0.5 pt; 1 line: colour #f86990, width 0.75 pt

### `animal_3_lines.csv` (225.5 KB)

From the subplot "Animal 3" (row 1, column 3 of the panel's subplots, 6.27-7.07 in across and 2.89-3.69 in down the page), under the page text "Animal 3"; x axis "Position (X)"; y axis "Position (Y)"; drawn over x -490.52348 to 490.52348, y -490.52348 to 490.52348 (values beyond these limits are exported but were not visible); its x axis prints "0" at -400, "400" at 0, "800" at 400.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Position (X)` | x position on the axis labelled "Position (X)" |
| `Position (Y)` | y position on the axis labelled "Position (Y)" |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |

Line styles: 13 lines: colour #debfe3, width 0.5 pt; 1 line: colour #ac5fb8, width 0.75 pt

### `animal_4_lines.csv` (229.3 KB)

From the subplot "Animal 4" (row 1, column 4 of the panel's subplots, 7.18-7.98 in across and 2.89-3.69 in down the page), under the page text "Animal 4"; x axis "Position (X)"; y axis "Position (Y)"; drawn over x -490.52348 to 490.52348, y -490.52348 to 490.52348 (values beyond these limits are exported but were not visible); its x axis prints "0" at -400, "400" at 0, "800" at 400.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Position (X)` | x position on the axis labelled "Position (X)" |
| `Position (Y)` | y position on the axis labelled "Position (Y)" |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |

Line styles: 13 lines: colour #c2bff0, width 0.5 pt; 1 line: colour #6361d7, width 0.75 pt

### `annotations.csv` (200 B)

Every text printed in the panel: inside a subplot (x and y in that subplot's data coordinates; for an annotation with a leader line, the point it marks in `target x` and `target y`) or on the page around the subplots (x and y in inches from the page's top-left: the text's anchor).

| Column | Meaning |
|---|---|
| `subplot` | the subplot the text is in; blank for page text |
| `text` | the text as printed, on one line |
| `x`, `y` | its position (see `coordinates`) |
| `coordinates` | "data" or "page inches" |

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- decoration: the cage schematic: solid far wall, dashed corners: 20 Line2D

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| Line2D | 76 | 56 |
