# figS14_e_usage_difference

Figure S14, panel e. Title: "Hierarchical representation", "Difference in usage".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS14/figS14_e_usage_difference.py`](../../../code/figS14/figS14_e_usage_difference.py).

## Files

### `hierarchical_representation_shapes.csv` (50.2 KB)

From the subplot "Hierarchical representation" (row 1, column 1 of the panel's subplots, 0.93-2.17 in across and 5.02-6.26 in down the page), under the page text "Hierarchical representation"; no axis labels; drawn over x -1.32 to 1.32, y -1.32 to 1.32 (values beyond these limits are exported but were not visible).

One row is one vertex of one shape's outline, curves sampled.

| Column | Meaning |
|---|---|
| `shape` | which shape, numbered from 1 in drawing order |
| `vertex` | the vertex's place along the outline |
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |
| `shape type` | the matplotlib artist that drew it |
| `fill colour` | the shape's fill colour, hex RGB |
| `edge colour` | the shape's outline colour, hex RGB |

### `hierarchical_representation_wedges.csv` (6.3 KB)

From the subplot "Hierarchical representation" (row 1, column 1 of the panel's subplots, 0.93-2.17 in across and 5.02-6.26 in down the page), under the page text "Hierarchical representation"; no axis labels; drawn over x -1.32 to 1.32, y -1.32 to 1.32 (values beyond these limits are exported but were not visible).

One row is one wedge.

| Column | Meaning |
|---|---|
| `centre x` | the wedge's centre, in the axes' data units |
| `centre y` | the wedge's centre, in the axes' data units |
| `outer radius` | data units |
| `ring width` | outer minus inner radius; blank for a full wedge |
| `start angle (deg)` | degrees anticlockwise from the +x axis |
| `end angle (deg)` | degrees anticlockwise from the +x axis |
| `fill colour` | the wedge's fill colour, hex RGB |
| `edge colour` | the wedge's outline colour, hex RGB |

### `hierarchical_representation_colour_key.csv` (4.8 KB)

From the subplot "Hierarchical representation colour key" (row 1, column 1 of the panel's subplots, its colour key, 1.15-1.95 in across and 6.23-6.27 in down the page); x axis "Relative difference"; drawn over x -0.4 to 0.4, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one step of the key's colour ramp.

| Column | Meaning |
|---|---|
| `Relative difference` | where the step sits along the key: its x position on the key's own axis, labelled "Relative difference" |
| `colour` | the colour drawn there, hex RGB |

The key is an image drawn by hand, not a matplotlib colour bar; the page texts beside it name its ends (see annotations.csv).

### `difference_in_usage_points.csv` (4.1 KB)

From the subplot "Difference in usage" (row 2, column 1 of the panel's subplots, 2.52-3.68 in across and 5.09-6.25 in down the page), under the page text "Difference in usage"; x axis "t-SNE 1"; y axis "t-SNE 2"; drawn over x -110 to 110, y -110 to 110 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `series` | the name the points' label or colour carries on the panel |
| `t-SNE 1` | x position on the axis labelled "t-SNE 1" |
| `t-SNE 2` | y position on the axis labelled "t-SNE 2" |
| `marker area (pt^2)` | the marker's area, points squared |
| `colour` | the marker's fill colour, hex RGB |

### `annotations.csv` (372 B)

Every text printed in the panel: inside a subplot (x and y in that subplot's data coordinates; for an annotation with a leader line, the point it marks in `target x` and `target y`) or on the page around the subplots (x and y in inches from the page's top-left: the text's anchor).

| Column | Meaning |
|---|---|
| `subplot` | the subplot the text is in; blank for page text |
| `text` | the text as printed, on one line |
| `x`, `y` | its position (see `coordinates`) |
| `coordinates` | "data" or "page inches" |

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- decoration: the dashed category outlines: 6 Line2D

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| Arc | 16 | 16 |
| AxesImage | 1 | 1 |
| Circle | 1 | 1 |
| Line2D | 6 | 0 |
| PathCollection | 80 | 80 |
| Text | 4 | 4 |
| Wedge | 146 | 146 |
