# fig2_d_category_maps

Figure 2, panel d. Title: "Model output", "Climbing", "Active", "Alone", "Social active", "Social resting".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig2/fig2_d_category_maps.py`](../../../code/fig2/fig2_d_category_maps.py).

## Files

### `model_output_points.csv` (17.2 MB)

From the subplot "Model output" (row 1, column 1 of the panel's subplots, 2.21-2.95 in across and 2.51-3.25 in down the page), under the page text "Model output"; y axis "Top-down view"; drawn over x -340 to 340, y -340 to 340 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `series` | the name the points' label or colour carries on the panel |
| `x` | x position; this axis carries no label |
| `Top-down view` | y position on the axis labelled "Top-down view" |
| `colour` | the marker's fill colour, hex RGB |

Every marker has an area of 0.06 pt^2.

### `climbing_points.csv` (4.0 MB)

From the subplot "Climbing" (row 1, column 2 of the panel's subplots, 3.21-3.95 in across and 2.51-3.25 in down the page), under the page text "Climbing"; y axis "Top-down view"; drawn over x -340 to 340, y -340 to 340 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `series` | the name the points' label or colour carries on the panel |
| `x` | x position; this axis carries no label |
| `Top-down view` | y position on the axis labelled "Top-down view" |

Every marker has an area of 0.06 pt^2.
Every marker is filled #6662d773.

### `active_points.csv` (3.5 MB)

From the subplot "Active" (row 1, column 3 of the panel's subplots, 4.21-4.95 in across and 2.51-3.25 in down the page), under the page text "Active"; y axis "Top-down view"; drawn over x -340 to 340, y -340 to 340 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `series` | the name the points' label or colour carries on the panel |
| `x` | x position; this axis carries no label |
| `Top-down view` | y position on the axis labelled "Top-down view" |

Every marker has an area of 0.06 pt^2.
Every marker is filled #a85fba73.

### `alone_points.csv` (2.0 MB)

From the subplot "Alone" (row 1, column 4 of the panel's subplots, 5.21-5.95 in across and 2.51-3.25 in down the page), under the page text "Alone"; y axis "Top-down view"; drawn over x -340 to 340, y -340 to 340 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `series` | the name the points' label or colour carries on the panel |
| `x` | x position; this axis carries no label |
| `Top-down view` | y position on the axis labelled "Top-down view" |

Every marker has an area of 0.06 pt^2.
Every marker is filled #f05c9b73.

### `social_active_points.csv` (1.6 MB)

From the subplot "Social active" (row 1, column 5 of the panel's subplots, 6.22-6.95 in across and 2.51-3.25 in down the page), under the page text "Social active"; y axis "Top-down view"; drawn over x -340 to 340, y -340 to 340 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `series` | the name the points' label or colour carries on the panel |
| `x` | x position; this axis carries no label |
| `Top-down view` | y position on the axis labelled "Top-down view" |

Every marker has an area of 0.06 pt^2.
Every marker is filled #fb8d7b73.

### `social_resting_points.csv` (1.3 MB)

From the subplot "Social resting" (row 1, column 6 of the panel's subplots, 7.22-7.96 in across and 2.51-3.25 in down the page), under the page text "Social resting"; y axis "Top-down view"; drawn over x -340 to 340, y -340 to 340 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `series` | the name the points' label or colour carries on the panel |
| `x` | x position; this axis carries no label |
| `Top-down view` | y position on the axis labelled "Top-down view" |

Every marker has an area of 0.06 pt^2.
Every marker is filled #fec15d73.

### `annotations.csv` (261 B)

Every text printed in the panel: inside a subplot (x and y in that subplot's data coordinates; for an annotation with a leader line, the point it marks in `target x` and `target y`) or on the page around the subplots (x and y in inches from the page's top-left: the text's anchor).

| Column | Meaning |
|---|---|
| `subplot` | the subplot the text is in; blank for page text |
| `text` | the text as printed, on one line |
| `x`, `y` | its position (see `coordinates`) |
| `coordinates` | "data" or "page inches" |

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- decoration: the dashed cage wireframe: 30 Line2D

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| Line2D | 30 | 0 |
| PathCollection | 10 | 10 |
