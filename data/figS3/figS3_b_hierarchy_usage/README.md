# figS3_b_hierarchy_usage

Figure S3, panel b. No title is printed on this panel.

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS3/figS3_b_hierarchy_usage.py`](../../../code/figS3/figS3_b_hierarchy_usage.py).

## Files

### `level_5_behavioral_state_boxes.csv` (4.1 KB)

From the subplot "Level-5 behavioral state" (row 1, column 1 of the panel's subplots, 4.69-8.11 in across and 1.12-2.01 in down the page); x axis "Level-5 behavioral state"; drawn over x 0 to 1, y 0 to 3 (values beyond these limits are exported but were not visible).

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Level-5 behavioral state left` | x of the box's left edge on the axis labelled "Level-5 behavioral state" |
| `Level-5 behavioral state right` | x of the box's right edge on the axis labelled "Level-5 behavioral state" |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |
| `fill colour` | the box's fill colour, hex RGB |

Filled: yes.
Every box's outline: #ffffff.

### `usage_vs_level_5_behavioral_state_bars.csv` (3.4 KB)

From the subplot "Usage vs Level-5 behavioral state" (row 2, column 1 of the panel's subplots, 4.69-8.11 in across and 2.09-2.39 in down the page); x axis "Level-5 behavioral state"; y axis "Usage"; drawn over x 0 to 1.0000002, y 0 to 0.069588855 (values beyond these limits are exported but were not visible); its x axis prints "0" at 0, "20" at 0.3868815, "40" at 0.61719595, "60" at 0.80783994, "80" at 1.0000002.

One row is one vertical bar.

| Column | Meaning |
|---|---|
| `Level-5 behavioral state` | x of the bar's centre on the axis labelled "Level-5 behavioral state" |
| `bar width` | the bar's width, in x units |
| `bar bottom` | where the bar starts, in y units |
| `Usage` | the bar's height: y extent on the axis labelled "Usage" |
| `colour` | the bar's fill colour, hex RGB |

### `annotations.csv` (176 B)

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
| Rectangle | 182 | 182 |
| Text | 3 | 3 |
