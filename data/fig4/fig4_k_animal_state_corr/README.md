# fig4_k_animal_state_corr

Figure 4, panel k. No title is printed on this panel.

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig4/fig4_k_animal_state_corr.py`](../../../code/fig4/fig4_k_animal_state_corr.py).

## Files

### `animal_vs_level_5_behavioral_state_map.csv` (63.6 KB)

From the subplot "Animal vs Level-5 behavioral state" (row 1, column 1 of the panel's subplots, 6.09-7.89 in across and 5.55-6.65 in down the page); x axis "Level-5 behavioral state"; y axis "Animal"; drawn over x 0.5 to 80.5, y 0 to 68 (values beyond these limits are exported but were not visible).

A 68 x 80 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `Animal \ Level-5 behavioral state` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x 0.5 to 80.5, y 0 to 68 (lower origin).
Colour map mb (Normalize), limits -0.55313375 to 0.55313375; no colour bar.

### `annotations.csv` (311 B)

Every text printed in the panel: inside a subplot (x and y in that subplot's data coordinates; for an annotation with a leader line, the point it marks in `target x` and `target y`) or on the page around the subplots (x and y in inches from the page's top-left: the text's anchor).

| Column | Meaning |
|---|---|
| `subplot` | the subplot the text is in; blank for page text |
| `text` | the text as printed, on one line |
| `x`, `y` | its position (see `coordinates`) |
| `coordinates` | "data" or "page inches" |
| `target x`, `target y` | the point an annotation's leader line marks, in data coordinates |

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- decoration: the dotted category boundaries: 3 Line2D

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| Annotation | 4 | 4 |
| AxesImage | 1 | 1 |
| Line2D | 3 | 0 |
