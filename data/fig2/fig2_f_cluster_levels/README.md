# fig2_f_cluster_levels

Figure 2, panel f. Title: "4 clusters", "18 clusters", "80 clusters".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig2/fig2_f_cluster_levels.py`](../../../code/fig2/fig2_f_cluster_levels.py).

## Files

### `4_clusters_points.csv` (168 B)

From the subplot "4 clusters" (row 1, column 1 of the panel's subplots, 2.18-3.14 in across and 3.65-4.62 in down the page), under the page text "4 clusters"; x axis "t-SNE 1"; y axis "t-SNE 2"; drawn over x -40 to 40, y -40 to 40 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `t-SNE 1` | x position on the axis labelled "t-SNE 1" |
| `t-SNE 2` | y position on the axis labelled "t-SNE 2" |
| `marker area (pt^2)` | the marker's area, points squared |
| `colour` | the marker's fill colour, hex RGB |

### `18_clusters_points.csv` (604 B)

From the subplot "18 clusters" (row 1, column 2 of the panel's subplots, 3.44-4.41 in across and 3.65-4.62 in down the page), under the page text "18 clusters"; x axis "t-SNE 1"; drawn over x -80 to 80, y -80 to 80 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `t-SNE 1` | x position on the axis labelled "t-SNE 1" |
| `y` | y position; this axis carries no label |
| `marker area (pt^2)` | the marker's area, points squared |
| `colour` | the marker's fill colour, hex RGB |

### `80_clusters_points.csv` (2.6 KB)

From the subplot "80 clusters" (row 1, column 3 of the panel's subplots, 4.70-5.67 in across and 3.65-4.62 in down the page), under the page text "80 clusters"; x axis "t-SNE 1"; drawn over x -120 to 120, y -120 to 120 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `t-SNE 1` | x position on the axis labelled "t-SNE 1" |
| `y` | y position; this axis carries no label |
| `marker area (pt^2)` | the marker's area, points squared |
| `colour` | the marker's fill colour, hex RGB |

### `annotations.csv` (544 B)

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
| PathCollection | 3 | 3 |
| Text | 12 | 12 |
