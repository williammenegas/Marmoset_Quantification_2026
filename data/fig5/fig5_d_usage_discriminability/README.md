# fig5_d_usage_discriminability

Figure 5, panel d. Title: "Example state", "All states", "Discriminability".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig5/fig5_d_usage_discriminability.py`](../../../code/fig5/fig5_d_usage_discriminability.py).

## Files

### `example_state_control_tablet_lines.csv` (5.7 KB)

From the subplot "Example state Control Tablet" (row 1, column 1 of the panel's subplots, 4.68-5.34 in across and 4.41-5.53 in down the page), under the page text "Example state"; y axis "Usage (%): State 43"; drawn over x 0.4 to 2.6, y -0.94684074 to 8.705297 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 1, "Tablet" at 2.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `Usage (%): State 43` | y position on the axis labelled "Usage (%): State 43" |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `category` | the category named by the nearest x tick label |

Line styles: 72 lines: colour #cccccc, width 0.5 pt; 1 line: colour #262626, width 0.5 pt

### `example_state_control_tablet_points.csv` (5.5 KB)

From the subplot "Example state Control Tablet" (row 1, column 1 of the panel's subplots, 4.68-5.34 in across and 4.41-5.53 in down the page), under the page text "Example state"; y axis "Usage (%): State 43"; drawn over x 0.4 to 2.6, y -0.94684074 to 8.705297 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 1, "Tablet" at 2.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position; this axis carries no label; the plotted, jittered position |
| `Usage (%): State 43` | y position on the axis labelled "Usage (%): State 43" |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

Every marker has an area of 4.2 pt^2.

### `all_states_lines.csv` (82 B)

From the subplot "All states" (row 1, column 2 of the panel's subplots, 5.82-6.94 in across and 4.41-5.53 in down the page), under the page text "All states"; x axis "Frequency (%), tablet"; y axis "Frequency (%), control"; drawn over x 0 to 6.6554334, y 0 to 6.6554334 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Frequency (%), tablet` | x position on the axis labelled "Frequency (%), tablet" |
| `Frequency (%), control` | y position on the axis labelled "Frequency (%), control" |

Line styles: 1 line: colour #262626, width 0.5 pt, dashed

### `all_states_points.csv` (1.7 KB)

From the subplot "All states" (row 1, column 2 of the panel's subplots, 5.82-6.94 in across and 4.41-5.53 in down the page), under the page text "All states"; x axis "Frequency (%), tablet"; y axis "Frequency (%), control"; drawn over x 0 to 6.6554334, y 0 to 6.6554334 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `Frequency (%), tablet` | x position on the axis labelled "Frequency (%), tablet" |
| `Frequency (%), control` | y position on the axis labelled "Frequency (%), control" |

Every marker has an area of 8 pt^2.
Every marker is filled #262626.

### `all_states_segments.csv` (7.1 KB)

From the subplot "All states" (row 1, column 2 of the panel's subplots, 5.82-6.94 in across and 4.41-5.53 in down the page), under the page text "All states"; x axis "Frequency (%), tablet"; y axis "Frequency (%), control"; drawn over x 0 to 6.6554334, y 0 to 6.6554334 (values beyond these limits are exported but were not visible).

One row is one straight segment.

| Column | Meaning |
|---|---|
| `collection` | which line collection, numbered from 1 |
| `Frequency (%), tablet from` | x of the segment's start on the axis labelled "Frequency (%), tablet" |
| `Frequency (%), control from` | y of the segment's start on the axis labelled "Frequency (%), control" |
| `Frequency (%), tablet to` | x of the segment's end on the axis labelled "Frequency (%), tablet" |
| `Frequency (%), control to` | y of the segment's end on the axis labelled "Frequency (%), control" |

Every segment's colour: #cccccc.

### `discriminability_control_tablet_lines.csv` (425 B)

From the subplot "Discriminability Control Tablet" (row 1, column 3 of the panel's subplots, 7.34-8.01 in across and 4.41-5.53 in down the page), under the page text "Discriminability"; y axis "Average score (all states)"; drawn over x 0.4 to 2.6, y 0 to 8.6384489 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 1, "Tablet" at 2.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `Average score (all states)` | y position on the axis labelled "Average score (all states)" |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `category` | the category named by the nearest x tick label |

Line styles: 1 line: colour #76b5a0, width 0.9 pt; 1 line: colour #c98ecf, width 0.9 pt; 3 lines: colour #737373, width 0.5 pt, dashed; 1 line: colour #262626, width 0.5 pt

### `discriminability_control_tablet_points.csv` (6.0 KB)

From the subplot "Discriminability Control Tablet" (row 1, column 3 of the panel's subplots, 7.34-8.01 in across and 4.41-5.53 in down the page), under the page text "Discriminability"; y axis "Average score (all states)"; drawn over x 0.4 to 2.6, y 0 to 8.6384489 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 1, "Tablet" at 2.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position; this axis carries no label; the plotted, jittered position |
| `Average score (all states)` | y position on the axis labelled "Average score (all states)" |
| `marker area (pt^2)` | the marker's area, points squared |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

### `annotations.csv` (501 B)

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
| AnchoredOffsetbox | 2 | 2 |
| Line2D | 80 | 80 |
| LineCollection | 2 | 2 |
| PathCollection | 7 | 7 |
| Text | 4 | 4 |
