# figS14_d_alone_time

Figure S14, panel d. Title: "Time spent alone".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS14/figS14_d_alone_time.py`](../../../code/figS14/figS14_d_alone_time.py).

## Files

### `juvenile_adult_lines.csv` (228 B)

From the subplot "Juvenile Adult" (row 1, column 1 of the panel's subplots, 4.81-5.95 in across and 3.30-4.54 in down the page), under the page text "***" / "-30" / "p < 10"; y axis "Time spent alone"; drawn over x -0.6 to 1.6, y -0.025507361 to 0.86725028 (values beyond these limits are exported but were not visible); its x axis prints "Juvenile" at 0, "Adult" at 1.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `Time spent alone` | y position on the axis labelled "Time spent alone" |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `category` | the category named by the nearest x tick label |

Line styles: 2 lines: colour #f05c9b, width 1.3 pt; 1 line: colour #737373, width 0.5 pt, dashed

### `juvenile_adult_points.csv` (180.4 KB)

From the subplot "Juvenile Adult" (row 1, column 1 of the panel's subplots, 4.81-5.95 in across and 3.30-4.54 in down the page), under the page text "***" / "-30" / "p < 10"; y axis "Time spent alone"; drawn over x -0.6 to 1.6, y -0.025507361 to 0.86725028 (values beyond these limits are exported but were not visible); its x axis prints "Juvenile" at 0, "Adult" at 1.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position; this axis carries no label; the plotted, jittered position |
| `Time spent alone` | y position on the axis labelled "Time spent alone" |
| `marker area (pt^2)` | the marker's area, points squared |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

### `juvenile_time_alone_vs_adult_time_alone_lines.csv` (94 B)

From the subplot "Juvenile time alone vs Adult time alone" (row 1, column 2 of the panel's subplots, 6.24-7.43 in across and 3.34-4.53 in down the page), under the page text "***" / "-34" / "p < 10"; x axis "Adult time alone"; y axis "Juvenile time alone"; drawn over x -0.017515055 to 0.87575273, y -0.017515055 to 0.87575273 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Adult time alone` | x position on the axis labelled "Adult time alone" |
| `Juvenile time alone` | y position on the axis labelled "Juvenile time alone" |

Line styles: 1 line: colour #9e9e9e, width 0.9 pt, dashed

### `juvenile_time_alone_vs_adult_time_alone_points.csv` (37.0 KB)

From the subplot "Juvenile time alone vs Adult time alone" (row 1, column 2 of the panel's subplots, 6.24-7.43 in across and 3.34-4.53 in down the page), under the page text "***" / "-34" / "p < 10"; x axis "Adult time alone"; y axis "Juvenile time alone"; drawn over x -0.017515055 to 0.87575273, y -0.017515055 to 0.87575273 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `Adult time alone` | x position on the axis labelled "Adult time alone" |
| `Juvenile time alone` | y position on the axis labelled "Juvenile time alone" |

Every marker has an area of 5 pt^2.
Every marker is filled #f05c9bbf.

### `juvenile_time_alone_vs_adult_time_alone_shapes.csv` (354 B)

From the subplot "Juvenile time alone vs Adult time alone" (row 1, column 2 of the panel's subplots, 6.24-7.43 in across and 3.34-4.53 in down the page), under the page text "***" / "-34" / "p < 10"; x axis "Adult time alone"; y axis "Juvenile time alone"; drawn over x -0.017515055 to 0.87575273, y -0.017515055 to 0.87575273 (values beyond these limits are exported but were not visible).

One row is one vertex of one shape's outline, curves sampled.

| Column | Meaning |
|---|---|
| `shape` | which shape, numbered from 1 in drawing order |
| `vertex` | the vertex's place along the outline |
| `Adult time alone` | x position on the axis labelled "Adult time alone" |
| `Juvenile time alone` | y position on the axis labelled "Juvenile time alone" |
| `fill colour` | the shape's fill colour, hex RGB |

Drawn as: Polygon.
Every shape's outline: none.

### `alone_wedges.csv` (148 B)

From the subplot "Alone" (row 2, column 1 of the panel's subplots, 7.49-7.95 in across and 3.66-4.12 in down the page), under the page text "Alone"; no axis labels; drawn over x -1.04 to 1.04, y -1.04 to 1.04 (values beyond these limits are exported but were not visible).

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

Every wedge's outline: #262626.

### `page_shapes.csv` (111 B)

Drawn on the page around the panel's subplots, not in one of them: 1 Line2D.

One row is one vertex of one shape drawn on the page.

| Column | Meaning |
|---|---|
| `shape` | which shape, numbered from 1 in drawing order |
| `vertex` | the vertex's place along the shape |
| `x (in)` | inches from the page's left edge |
| `y (in)` | inches down from the page's top edge |

Drawn as: Line2D.
Every shape's fill: none.
Every line's colour: #262626.
Every line's width (pt): 0.5.
Every line is: solid.
These are drawn on the page around the panel's subplots, not in one of them, so they are given in page inches, not in data coordinates. A shape that does not end where it starts is an open line.

### `annotations.csv` (624 B)

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
| Line2D | 4 | 4 |
| PathCollection | 5 | 5 |
| Polygon | 2 | 2 |
| Text | 6 | 4 |
| Wedge | 2 | 2 |
| Line2D (on the page) | 1 | 1 |
