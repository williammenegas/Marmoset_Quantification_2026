# figS14_a_climbing_time

Figure S14, panel a. Title: "Time spent climbing".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS14/figS14_a_climbing_time.py`](../../../code/figS14/figS14_a_climbing_time.py).

## Files

### `juvenile_adult_lines.csv` (232 B)

From the subplot "Juvenile Adult" (row 1, column 1 of the panel's subplots, 1.13-2.27 in across and 1.32-2.56 in down the page), under the page text "***" / "-3" / "p < 10"; y axis "Time spent climbing"; drawn over x -0.6 to 1.6, y -0.020000972 to 0.68003306 (values beyond these limits are exported but were not visible); its x axis prints "Juvenile" at 0, "Adult" at 1.

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `Time spent climbing` | y position on the axis labelled "Time spent climbing" |
| `colour` | the line's colour, hex RGB (a line drawn as markers only shows the marker colours instead) |
| `category` | the category named by the nearest x tick label |

Line styles: 2 lines: colour #6662d7, width 1.3 pt; 1 line: colour #737373, width 0.5 pt, dashed

### `juvenile_adult_points.csv` (181.5 KB)

From the subplot "Juvenile Adult" (row 1, column 1 of the panel's subplots, 1.13-2.27 in across and 1.32-2.56 in down the page), under the page text "***" / "-3" / "p < 10"; y axis "Time spent climbing"; drawn over x -0.6 to 1.6, y -0.020000972 to 0.68003306 (values beyond these limits are exported but were not visible); its x axis prints "Juvenile" at 0, "Adult" at 1.

One row is one scatter point.

| Column | Meaning |
|---|---|
| `group` | which scatter call drew the point, numbered from 1 in drawing order |
| `x_plot` | x position; this axis carries no label; the plotted, jittered position |
| `Time spent climbing` | y position on the axis labelled "Time spent climbing" |
| `marker area (pt^2)` | the marker's area, points squared |
| `colour` | the marker's fill colour, hex RGB |
| `category` | the category named by the nearest x tick label |

### `juvenile_time_climbing_vs_adult_time_climbing_lines.csv` (100 B)

From the subplot "Juvenile time climbing vs Adult time climbing" (row 1, column 2 of the panel's subplots, 2.56-3.75 in across and 1.36-2.55 in down the page), under the page text "n/s" / "p = 0.085"; x axis "Adult time climbing"; y axis "Juvenile time climbing"; drawn over x -0.013555086 to 0.67775431, y -0.013555086 to 0.67775431 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Adult time climbing` | x position on the axis labelled "Adult time climbing" |
| `Juvenile time climbing` | y position on the axis labelled "Juvenile time climbing" |

Line styles: 1 line: colour #9e9e9e, width 0.9 pt, dashed

### `juvenile_time_climbing_vs_adult_time_climbing_points.csv` (38.2 KB)

From the subplot "Juvenile time climbing vs Adult time climbing" (row 1, column 2 of the panel's subplots, 2.56-3.75 in across and 1.36-2.55 in down the page), under the page text "n/s" / "p = 0.085"; x axis "Adult time climbing"; y axis "Juvenile time climbing"; drawn over x -0.013555086 to 0.67775431, y -0.013555086 to 0.67775431 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `Adult time climbing` | x position on the axis labelled "Adult time climbing" |
| `Juvenile time climbing` | y position on the axis labelled "Juvenile time climbing" |

Every marker has an area of 5 pt^2.
Every marker is filled #6662d7bf.

### `juvenile_time_climbing_vs_adult_time_climbing_shapes.csv` (360 B)

From the subplot "Juvenile time climbing vs Adult time climbing" (row 1, column 2 of the panel's subplots, 2.56-3.75 in across and 1.36-2.55 in down the page), under the page text "n/s" / "p = 0.085"; x axis "Adult time climbing"; y axis "Juvenile time climbing"; drawn over x -0.013555086 to 0.67775431, y -0.013555086 to 0.67775431 (values beyond these limits are exported but were not visible).

One row is one vertex of one shape's outline, curves sampled.

| Column | Meaning |
|---|---|
| `shape` | which shape, numbered from 1 in drawing order |
| `vertex` | the vertex's place along the outline |
| `Adult time climbing` | x position on the axis labelled "Adult time climbing" |
| `Juvenile time climbing` | y position on the axis labelled "Juvenile time climbing" |
| `fill colour` | the shape's fill colour, hex RGB |

Drawn as: Polygon.
Every shape's outline: none.

### `climb_wedges.csv` (148 B)

From the subplot "Climb" (row 2, column 1 of the panel's subplots, 3.81-4.27 in across and 1.68-2.14 in down the page), under the page text "Climb"; no axis labels; drawn over x -1.04 to 1.04, y -1.04 to 1.04 (values beyond these limits are exported but were not visible).

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

### `annotations.csv` (618 B)

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
