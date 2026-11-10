# figS3_a_hierarchy_flow

Figure S3, panel a. No title is printed on this panel.

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS3/figS3_a_hierarchy_flow.py`](../../../code/figS3/figS3_a_hierarchy_flow.py).

## Files

### `level_5_behavioral_state_boxes.csv` (6.1 KB)

From the subplot "Level-5 behavioral state" (row 1, column 1 of the panel's subplots, 1.33-4.16 in across and 1.14-2.39 in down the page); x axis "Level-5 behavioral state"; drawn over x -0.02 to 1.02, y -0.045 to 1.045 (values beyond these limits are exported but were not visible); its x axis prints "0" at 0, "20" at 0.36058389, "40" at 0.59147652, "60" at 0.79708004, "80" at 1.

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Level-5 behavioral state left` | x of the box's left edge on the axis labelled "Level-5 behavioral state" |
| `Level-5 behavioral state right` | x of the box's right edge on the axis labelled "Level-5 behavioral state" |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |
| `fill colour` | the box's fill colour, hex RGB |

Filled: yes.
Every box's outline: none.

### `level_5_behavioral_state_shapes.csv` (646.5 KB)

From the subplot "Level-5 behavioral state" (row 1, column 1 of the panel's subplots, 1.33-4.16 in across and 1.14-2.39 in down the page); x axis "Level-5 behavioral state"; drawn over x -0.02 to 1.02, y -0.045 to 1.045 (values beyond these limits are exported but were not visible); its x axis prints "0" at 0, "20" at 0.36058389, "40" at 0.59147652, "60" at 0.79708004, "80" at 1.

One row is one vertex of one shape's outline, curves sampled.

| Column | Meaning |
|---|---|
| `shape` | which shape, numbered from 1 in drawing order |
| `vertex` | the vertex's place along the outline |
| `Level-5 behavioral state` | x position on the axis labelled "Level-5 behavioral state" |
| `y` | y position; this axis carries no label |
| `fill colour` | the shape's fill colour, hex RGB |

Drawn as: FillBetweenPolyCollection.
Every shape's outline: none.

### `annotations.csv` (384 B)

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
| FillBetweenPolyCollection | 138 | 138 |
| Rectangle | 142 | 142 |
| Text | 5 | 5 |
