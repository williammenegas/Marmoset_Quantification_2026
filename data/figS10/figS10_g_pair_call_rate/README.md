# figS10_g_pair_call_rate

Figure S10, panel g. Title: "Paired animals (2 per cage)".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS10/figS10_g_pair_call_rate.py`](../../../code/figS10/figS10_g_pair_call_rate.py).

## Files

### `paired_animals_2_per_cage_lines.csv` (63 B)

From the subplot "Paired animals (2 per cage)" (row 1, column 1 of the panel's subplots, 1.26-3.15 in across and 4.64-5.84 in down the page), under the page text "Paired animals (2 per cage)", marked "median 10.2/min" inside; x axis "Call rate (per min)"; y axis "5-min segments"; drawn over x 0 to 80, y 0 to 975.45 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `Call rate (per min)` | x position on the axis labelled "Call rate (per min)" (unit: per min) |
| `5-min segments` | y position on the axis labelled "5-min segments" |

Line styles: 1 line: colour #262626, width 0.6 pt, dashed

### `paired_animals_2_per_cage_bars.csv` (696 B)

From the subplot "Paired animals (2 per cage)" (row 1, column 1 of the panel's subplots, 1.26-3.15 in across and 4.64-5.84 in down the page), under the page text "Paired animals (2 per cage)", marked "median 10.2/min" inside; x axis "Call rate (per min)"; y axis "5-min segments"; drawn over x 0 to 80, y 0 to 975.45 (values beyond these limits are exported but were not visible).

One row is one vertical bar.

| Column | Meaning |
|---|---|
| `Call rate (per min)` | x of the bar's centre on the axis labelled "Call rate (per min)" (unit: per min) |
| `bar width` | the bar's width, in x units |
| `bar bottom` | where the bar starts, in y units |
| `5-min segments` | the bar's height: y extent on the axis labelled "5-min segments" |

Every bar is filled: #737373.

### `annotations.csv` (147 B)

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
| Line2D | 1 | 1 |
| Rectangle | 40 | 40 |
| Text | 1 | 1 |
