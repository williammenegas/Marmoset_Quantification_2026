# figS6_a_state_flow

Figure S6, panel a. Title: "Example animal".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS6/figS6_a_state_flow.py`](../../../code/figS6/figS6_a_state_flow.py).

## Files

### `example_animal_boxes.csv` (180.8 KB)

From the subplot "Example animal" (row 1, column 1 of the panel's subplots, 0.36-7.89 in across and 1.01-3.24 in down the page), under the page text "Example animal" / "Climbing"; x axis "Recording #"; drawn over x -0.02 to 1.02, y -0.045 to 1.7856006 (values beyond these limits are exported but were not visible); its x axis prints "1" at 0, "5" at 0.090909091, "10" at 0.20454545, "15" at 0.31818182, "20" at 0.43181818, "25" at 0.54545455, "30" at 0.65909091, "35" at 0.77272727, "40" at 0.88636364, "45" at 1.

One row is one rectangle.

| Column | Meaning |
|---|---|
| `Recording # left` | x of the box's left edge on the axis labelled "Recording #" |
| `Recording # right` | x of the box's right edge on the axis labelled "Recording #" |
| `y bottom` | y of the box's lower edge; this axis carries no label |
| `y top` | y of the box's upper edge; this axis carries no label |
| `fill colour` | the box's fill colour, hex RGB |

Filled: yes.
Every box's outline: none.

### `example_animal_ribbons.csv` (269.3 KB)

From the subplot "Example animal" (row 1, column 1 of the panel's subplots, 0.36-7.89 in across and 1.01-3.24 in down the page), under the page text "Example animal" / "Climbing"; x axis "Recording #"; drawn over x -0.02 to 1.02, y -0.045 to 1.7856006 (values beyond these limits are exported but were not visible); its x axis prints "1" at 0, "5" at 0.090909091, "10" at 0.20454545, "15" at 0.31818182, "20" at 0.43181818, "25" at 0.54545455, "30" at 0.65909091, "35" at 0.77272727, "40" at 0.88636364, "45" at 1.

One row is one ribbon, joining a band of one bar to the same band of the next.

| Column | Meaning |
|---|---|
| `colour` | the ribbon's colour, hex RGB -- its state's colour, as on that state's bars in the boxes table |
| `x at left end` | where the ribbon leaves the right edge of its left bar, in the axes' x units |
| `x at right end` | where it reaches the left edge of its right bar, in the axes' x units |
| `Recording # at left end` | the Recording # the x axis numbers at the left end: its tick labels read as a straight line, rounded to the nearest whole number |
| `Recording # at right end` | the Recording # the x axis numbers at the right end: its tick labels read as a straight line, rounded to the nearest whole number |
| `bottom at left end` | the band's lower edge at the left end, in the axes' y units |
| `top at left end` | the band's upper edge at the left end, in the axes' y units |
| `bottom at right end` | the band's lower edge at the right end, in the axes' y units |
| `top at right end` | the band's upper edge at the right end, in the axes' y units |

The curve a ribbon follows between its two ends is the script's drawn smoothing, not data; only the ends are exported.
Every ribbon end meets the bar of its colour exactly: the smoothing starts and ends on the band heights the script computed.
Drawn at 38% opacity.

### `annotations.csv` (209 B)

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
| FillBetweenPolyCollection | 3520 | 3520 |
| Rectangle | 3600 | 3600 |
