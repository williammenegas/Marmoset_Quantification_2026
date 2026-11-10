# figS10_c_homecage_loud_tsne

Figure S10, panel c. Title: "Behavioral space".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS10/figS10_c_homecage_loud_tsne.py`](../../../code/figS10/figS10_c_homecage_loud_tsne.py).

## Files

### `behavioral_space_map.csv` (15.1 KB)

From the subplot "Behavioral space" (row 1, column 1 of the panel's subplots, 6.29-7.49 in across and 0.76-1.96 in down the page), under the page text "Behavioral space"; x axis "t-SNE 1"; y axis "t-SNE 2"; drawn over x -120 to 120, y -120 to 120 (values beyond these limits are exported but were not visible).

A 40 x 40 matrix. 
One row is one image row (its y centre first); one column per image column (its x centre in the header).

| Column | Meaning |
|---|---|
| `t-SNE 2 \ t-SNE 1` | header: each column's x centre (or category); first column: each row's y centre (or category) |
| `value` | every other cell: the image cell's value |

Image extent: x -100 to 100, y -100 to 100 (lower origin).
Colour map mb (Normalize), limits -0.00055092296 to 0.00055092296; no colour bar.

### `annotations.csv` (73 B)

Every text printed in the panel: inside a subplot (x and y in that subplot's data coordinates; for an annotation with a leader line, the point it marks in `target x` and `target y`) or on the page around the subplots (x and y in inches from the page's top-left: the text's anchor).

| Column | Meaning |
|---|---|
| `subplot` | the subplot the text is in; blank for page text |
| `text` | the text as printed, on one line |
| `x`, `y` | its position (see `coordinates`) |
| `coordinates` | "data" or "page inches" |

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- decoration: the dashed category outlines: 6 Line2D

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| AxesImage | 1 | 1 |
| Line2D | 6 | 0 |
