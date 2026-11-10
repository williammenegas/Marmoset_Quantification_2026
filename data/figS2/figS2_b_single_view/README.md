# figS2_b_single_view

Figure S2, panel b. Title: "Single view".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS2/figS2_b_single_view.py`](../../../code/figS2/figS2_b_single_view.py).

The photograph beside the plot is artwork pasted in Illustrator; not drawn by code.

## Files

### `head_radius_px_vs_state_category_frames_lines.csv` (385 B)

From the subplot "Head radius (px) vs State category (frames)" (row 1, column 1 of the panel's subplots, 2.42-3.36 in across and 1.90-2.62 in down the page), under the page text "AUC = 0.82"; x axis "State category (frames)"; y axis "Head radius (px)"; drawn over x -0.6 to 1.6, y 0 to 60 (values beyond these limits are exported but were not visible); its x axis prints "Other (751)" at 0, "Climbing (733)" at 1.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `State category (frames)` | x position on the axis labelled "State category (frames)" (unit: frames) |
| `Head radius (px)` | y position on the axis labelled "Head radius (px)" (unit: px) |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `marker fill` | the fill colour of the line's markers, hex RGB; blank where it draws none |
| `category` | the category named by the nearest x tick label |

Line styles: 1 line: colour #737373, width 1.4 pt; 1 line: colour #1f77b4, width 1.5 pt, no line, marker 'o' 3.6 pt, filled #737373, edged #ffffff; 1 line: colour #6662d7, width 1.4 pt; 1 line: colour #ff7f0e, width 1.5 pt, no line, marker 'o' 3.6 pt, filled #6662d7, edged #ffffff; 1 line: colour #999999, width 0.5 pt, dashed

### `head_radius_px_vs_state_category_frames_points.csv` (66.2 KB)

From the subplot "Head radius (px) vs State category (frames)" (row 1, column 1 of the panel's subplots, 2.42-3.36 in across and 1.90-2.62 in down the page), under the page text "AUC = 0.82"; x axis "State category (frames)"; y axis "Head radius (px)"; drawn over x -0.6 to 1.6, y 0 to 60 (values beyond these limits are exported but were not visible); its x axis prints "Other (751)" at 0, "Climbing (733)" at 1.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position on the axis labelled "State category (frames)" (unit: frames); the plotted, jittered position |
| `Head radius (px)` | y position on the axis labelled "Head radius (px)" (unit: px) |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

Every marker has an area of 3 pt^2.

### `annotations.csv` (240 B)

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
| Line2D | 5 | 5 |
| PathCollection | 2 | 2 |
| Text | 2 | 2 |
