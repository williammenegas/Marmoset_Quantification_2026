# fig5_a_session_tsne

Figure 5, panel a. Title: "Control 1", "Control 2", "Control 3", "Control 4", "Box", "Example animal".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig5/fig5_a_session_tsne.py`](../../../code/fig5/fig5_a_session_tsne.py).

## Files

### `control_1_points.csv` (3.4 KB)

From the subplot "Control 1" (row 1, column 1 of the panel's subplots, 1.05-2.00 in across and 0.46-1.41 in down the page), under the page text "Control 1"; x axis "t-SNE 1"; y axis "t-SNE 2"; drawn over x -120 to 120, y -120 to 120 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `t-SNE 1` | x position on the axis labelled "t-SNE 1" |
| `t-SNE 2` | y position on the axis labelled "t-SNE 2" |
| `marker area (pt^2)` | the marker's area, points squared |
| `colour` | the marker's fill colour, hex RGB |

### `control_2_points.csv` (3.4 KB)

From the subplot "Control 2" (row 1, column 2 of the panel's subplots, 2.55-3.50 in across and 0.46-1.41 in down the page), under the page text "Control 2"; x axis "t-SNE 1"; y axis "t-SNE 2"; drawn over x -120 to 120, y -120 to 120 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `t-SNE 1` | x position on the axis labelled "t-SNE 1" |
| `t-SNE 2` | y position on the axis labelled "t-SNE 2" |
| `marker area (pt^2)` | the marker's area, points squared |
| `colour` | the marker's fill colour, hex RGB |

### `control_3_points.csv` (3.4 KB)

From the subplot "Control 3" (row 1, column 3 of the panel's subplots, 4.05-5.00 in across and 0.46-1.41 in down the page), under the page text "Control 3"; x axis "t-SNE 1"; y axis "t-SNE 2"; drawn over x -120 to 120, y -120 to 120 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `t-SNE 1` | x position on the axis labelled "t-SNE 1" |
| `t-SNE 2` | y position on the axis labelled "t-SNE 2" |
| `marker area (pt^2)` | the marker's area, points squared |
| `colour` | the marker's fill colour, hex RGB |

### `control_4_points.csv` (3.4 KB)

From the subplot "Control 4" (row 1, column 4 of the panel's subplots, 5.55-6.50 in across and 0.46-1.41 in down the page), under the page text "Control 4"; x axis "t-SNE 1"; y axis "t-SNE 2"; drawn over x -120 to 120, y -120 to 120 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `t-SNE 1` | x position on the axis labelled "t-SNE 1" |
| `t-SNE 2` | y position on the axis labelled "t-SNE 2" |
| `marker area (pt^2)` | the marker's area, points squared |
| `colour` | the marker's fill colour, hex RGB |

### `box_points.csv` (3.4 KB)

From the subplot "Box" (row 1, column 5 of the panel's subplots, 7.05-8.00 in across and 0.46-1.41 in down the page), under the page text "Box"; x axis "t-SNE 1"; y axis "t-SNE 2"; drawn over x -120 to 120, y -120 to 120 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `t-SNE 1` | x position on the axis labelled "t-SNE 1" |
| `t-SNE 2` | y position on the axis labelled "t-SNE 2" |
| `marker area (pt^2)` | the marker's area, points squared |
| `colour` | the marker's fill colour, hex RGB |

### `annotations.csv` (238 B)

Every text printed in the panel: inside a subplot (x and y in that subplot's data coordinates; for an annotation with a leader line, the point it marks in `target x` and `target y`) or on the page around the subplots (x and y in inches from the page's top-left: the text's anchor).

| Column | Meaning |
|---|---|
| `subplot` | the subplot the text is in; blank for page text |
| `text` | the text as printed, on one line |
| `x`, `y` | its position (see `coordinates`) |
| `coordinates` | "data" or "page inches" |

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- decoration: the dashed category outlines: 30 Line2D

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| Line2D | 30 | 0 |
| PathCollection | 400 | 400 |
