# fig6_e_pairwise_auroc

Figure 6, panel e. No title is printed on this panel.

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig6/fig6_e_pairwise_auroc.py`](../../../code/fig6/fig6_e_pairwise_auroc.py).

## Files

### `map.csv` (581 B)

From the subplot "" (row 1, column 1 of the panel's subplots, 6.61-8.11 in across and 5.32-6.82 in down the page); no axis labels; drawn over x -0.5 to 8.5, y 8.5 to -0.5 (values beyond these limits are exported but were not visible); its x axis prints "Control" at 0, "Object" at 1, "Noise" at 2, "Toys" at 3, "Mask" at 4, "Treat" at 5, "Box" at 6, "Face" at 7, "Intruder" at 8; its y axis prints "Control" at 0, "Object" at 1, "Noise" at 2, "Toys" at 3, "Mask" at 4, "Treat" at 5, "Box" at 6, "Face" at 7, "Intruder" at 8.

A 9 x 9 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `y \ x` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -0.5 to 8.5, y 8.5 to -0.5 (upper origin).
Colour map from_list (Normalize), limits 50 to 100; no colour bar.

### `annotations.csv` (626 B)

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
| AxesImage | 1 | 1 |
| Text | 45 | 45 |
