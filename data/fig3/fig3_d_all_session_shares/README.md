# fig3_d_all_session_shares

Figure 3, panel d. Title: "Distribution - all animals".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig3/fig3_d_all_session_shares.py`](../../../code/fig3/fig3_d_all_session_shares.py).

## Files

### `climbing_bars.csv` (1.4 KB)

From the subplot "Climbing" (row 1, column 1 of the panel's subplots, 0.91-2.54 in across and 3.44-3.73 in down the page), marked "Climbing" inside; x axis "Session # (sorted by PC1)"; y axis "Fraction of time"; drawn over x 0 to 5358, y 0 to 0.9 (values beyond these limits are exported but were not visible).

One row is one vertical bar.

| Column | Meaning |
|---|---|
| `Session # (sorted by PC1)` | x of the bar's centre on the axis labelled "Session # (sorted by PC1)" |
| `bar width` | the bar's width, in x units |
| `bar bottom` | where the bar starts, in y units |
| `Fraction of time` | the bar's height: y extent on the axis labelled "Fraction of time" |

Every bar is filled: #262626.

### `active_bars.csv` (1.4 KB)

From the subplot "Active" (row 1, column 2 of the panel's subplots, 2.76-4.38 in across and 3.44-3.73 in down the page), marked "Active" inside; x axis "Session # (sorted by PC1)"; y axis "Fraction of time"; drawn over x 0 to 5358, y 0 to 0.9 (values beyond these limits are exported but were not visible).

One row is one vertical bar.

| Column | Meaning |
|---|---|
| `Session # (sorted by PC1)` | x of the bar's centre on the axis labelled "Session # (sorted by PC1)" |
| `bar width` | the bar's width, in x units |
| `bar bottom` | where the bar starts, in y units |
| `Fraction of time` | the bar's height: y extent on the axis labelled "Fraction of time" |

Every bar is filled: #262626.

### `alone_bars.csv` (1.4 KB)

From the subplot "Alone" (row 1, column 3 of the panel's subplots, 4.60-6.23 in across and 3.44-3.73 in down the page), marked "Alone" inside; x axis "Session # (sorted by PC1)"; y axis "Fraction of time"; drawn over x 0 to 5358, y 0 to 0.9 (values beyond these limits are exported but were not visible).

One row is one vertical bar.

| Column | Meaning |
|---|---|
| `Session # (sorted by PC1)` | x of the bar's centre on the axis labelled "Session # (sorted by PC1)" |
| `bar width` | the bar's width, in x units |
| `bar bottom` | where the bar starts, in y units |
| `Fraction of time` | the bar's height: y extent on the axis labelled "Fraction of time" |

Every bar is filled: #262626.

### `social_bars.csv` (1.4 KB)

From the subplot "Social" (row 1, column 4 of the panel's subplots, 6.45-8.08 in across and 3.44-3.73 in down the page), marked "Social" inside; x axis "Session # (sorted by PC1)"; y axis "Fraction of time"; drawn over x 0 to 5358, y 0 to 0.9 (values beyond these limits are exported but were not visible).

One row is one vertical bar.

| Column | Meaning |
|---|---|
| `Session # (sorted by PC1)` | x of the bar's centre on the axis labelled "Session # (sorted by PC1)" |
| `bar width` | the bar's width, in x units |
| `bar bottom` | where the bar starts, in y units |
| `Fraction of time` | the bar's height: y extent on the axis labelled "Fraction of time" |

Every bar is filled: #262626.

### `page_shapes.csv` (61 B)

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
Every line's colour: #808285.
Every line's width (pt): 0.6.
Every line is: solid.
These are drawn on the page around the panel's subplots, not in one of them, so they are given in page inches, not in data coordinates. A shape that does not end where it starts is an open line.

### `annotations.csv` (208 B)

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
| Rectangle | 216 | 216 |
| Text | 4 | 4 |
| Line2D (on the page) | 1 | 1 |
