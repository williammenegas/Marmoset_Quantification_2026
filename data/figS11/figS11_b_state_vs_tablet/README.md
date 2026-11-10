# figS11_b_state_vs_tablet

Figure S11, panel b. Title: "Correlations (example animal)".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS11/figS11_b_state_vs_tablet.py`](../../../code/figS11/figS11_b_state_vs_tablet.py).

## Files

### `state_8_x_tablet_lines.csv` (75 B)

From the subplot "State 8 × Tablet" (row 1, column 1 of the panel's subplots, 4.58-5.92 in across and 0.71-1.64 in down the page), under the page text "State 8 × Tablet"; x axis "Time near tablet (%)"; y axis "State 8 usage (%)"; drawn over x -4 to 104, y 0 to 23.313889 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time near tablet (%)` | x position on the axis labelled "Time near tablet (%)" (unit: %) |
| `State 8 usage (%)` | y position on the axis labelled "State 8 usage (%)" (unit: %) |

Line styles: 1 line: colour #c98ecf, width 1 pt

### `state_8_x_tablet_points.csv` (1.6 KB)

From the subplot "State 8 × Tablet" (row 1, column 1 of the panel's subplots, 4.58-5.92 in across and 0.71-1.64 in down the page), under the page text "State 8 × Tablet"; x axis "Time near tablet (%)"; y axis "State 8 usage (%)"; drawn over x -4 to 104, y 0 to 23.313889 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `Time near tablet (%)` | x position on the axis labelled "Time near tablet (%)" (unit: %) |
| `State 8 usage (%)` | y position on the axis labelled "State 8 usage (%)" (unit: %) |

Every marker has an area of 9 pt^2.
Every marker is filled #e7cce9.

### `state_36_x_tablet_lines.csv` (77 B)

From the subplot "State 36 × Tablet" (row 1, column 2 of the panel's subplots, 6.68-8.01 in across and 0.71-1.64 in down the page), under the page text "State 36 × Tablet"; x axis "Time near tablet (%)"; y axis "State 36 usage (%)"; drawn over x -4 to 104, y 0 to 51.761111 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Time near tablet (%)` | x position on the axis labelled "Time near tablet (%)" (unit: %) |
| `State 36 usage (%)` | y position on the axis labelled "State 36 usage (%)" (unit: %) |

Line styles: 1 line: colour #c98ecf, width 1 pt

### `state_36_x_tablet_points.csv` (1.5 KB)

From the subplot "State 36 × Tablet" (row 1, column 2 of the panel's subplots, 6.68-8.01 in across and 0.71-1.64 in down the page), under the page text "State 36 × Tablet"; x axis "Time near tablet (%)"; y axis "State 36 usage (%)"; drawn over x -4 to 104, y 0 to 51.761111 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `Time near tablet (%)` | x position on the axis labelled "Time near tablet (%)" (unit: %) |
| `State 36 usage (%)` | y position on the axis labelled "State 36 usage (%)" (unit: %) |

Every marker has an area of 9 pt^2.
Every marker is filled #e7cce9.

### `annotations.csv` (267 B)

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
| Line2D | 2 | 2 |
| PathCollection | 2 | 2 |
| Text | 2 | 2 |
