# fig7_i_age_by_group

Figure 7, panel i. No title is printed on this panel.

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig7/fig7_i_age_by_group.py`](../../../code/fig7/fig7_i_age_by_group.py).

## Files

### `animals_vs_group_bars.csv` (179 B)

From the subplot "Animals vs Group" (row 1, column 1 of the panel's subplots, 6.16-7.06 in across and 5.94-7.14 in down the page); x axis "Group"; y axis "Animals"; drawn over x -0.5 to 2.5, y 0 to 20 (values beyond these limits are exported but were not visible); its x axis prints "1" at 0, "2" at 1, "3" at 2.

One row is one vertical bar.

| Column | Meaning |
|---|---|
| `Group` | x of the bar's centre on the axis labelled "Group" |
| `bar width` | the bar's width, in x units |
| `bar bottom` | where the bar starts, in y units |
| `Animals` | the bar's height: y extent on the axis labelled "Animals" |
| `colour` | the bar's fill colour, hex RGB |

### `adult_boxes.csv` (38 B)

From the subplot "Adult" (row 2, column 1 of the panel's subplots, 7.32-7.39 in across and 6.41-6.48 in down the page); no axis labels; drawn over x 0 to 1, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `x left` | x of the box's left edge; this axis carries no label |
| `x right` | x of the box's right edge; this axis carries no label |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |

Filled: yes.
Every box's fill: #000000.
Every box's outline: none.

### `juvenile_boxes.csv` (38 B)

From the subplot "Juvenile" (row 3, column 1 of the panel's subplots, 7.32-7.39 in across and 6.57-6.64 in down the page); no axis labels; drawn over x 0 to 1, y 0 to 1 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `x left` | x of the box's left edge; this axis carries no label |
| `x right` | x of the box's right edge; this axis carries no label |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |

Filled: yes.
Every box's fill: #a9a9a9.
Every box's outline: none.

### `annotations.csv` (94 B)

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
| Rectangle | 8 | 8 |
