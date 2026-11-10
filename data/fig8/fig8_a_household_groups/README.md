# fig8_a_household_groups

Figure 8, panel a. Title: "Parents", "Juveniles".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig8/fig8_a_household_groups.py`](../../../code/fig8/fig8_a_household_groups.py).

## Files

### `boxes.csv` (2.7 KB)

From the subplot "" (row 1, column 1 of the panel's subplots, 0.44-6.41 in across and 0.44-2.71 in down the page); no axis labels; drawn over x -0.3 to 28, y -9.8 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `x left` | x of the box's left edge; this axis carries no label |
| `x right` | x of the box's right edge; this axis carries no label |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |
| `fill colour` | the box's fill colour, hex RGB |
| `edge colour` | the box's outline colour, hex RGB |

Filled: yes.

### `page_shapes.csv` (1.6 KB)

Drawn on the page around the panel's subplots, not in one of them: 2 Line2D, 5 Rectangle.

One row is one vertex of one shape drawn on the page.

| Column | Meaning |
|---|---|
| `shape` | which shape, numbered from 1 in drawing order |
| `vertex` | the vertex's place along the shape |
| `x (in)` | inches from the page's left edge |
| `y (in)` | inches down from the page's top edge |
| `shape type` | the matplotlib artist that drew it |
| `fill colour` | the shape's fill colour, hex RGB; none for a line |
| `edge colour` | the line's or outline's colour, hex RGB |
| `line width (pt)` | the line's width, points |
| `line style` | solid, dashed, dotted or dash-dot |

These are drawn on the page around the panel's subplots, not in one of them, so they are given in page inches, not in data coordinates. A shape that does not end where it starts is an open line.

### `annotations.csv` (2.5 KB)

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
| Rectangle | 72 | 72 |
| Text | 98 | 98 |
| Line2D (on the page) | 2 | 2 |
| Rectangle (on the page) | 5 | 5 |
