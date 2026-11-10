# fig2_a_state_usage_tsne

Figure 2, panel a. Title: "Behavioral state usage".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/fig2/fig2_a_state_usage_tsne.py`](../../../code/fig2/fig2_a_state_usage_tsne.py).

## Files

### `behavioral_state_usage_points.csv` (2.6 KB)

From the subplot "Behavioral state usage" (row 1, column 1 of the panel's subplots, 0.73-1.58 in across and 0.73-1.58 in down the page), under the page text "Behavioral state usage"; x axis "tSNE 1"; y axis "tSNE 2"; drawn over x -120 to 120, y -120 to 120 (values beyond these limits are exported but were not visible).

One row is one scatter point.

| Column | Meaning |
|---|---|
| `tSNE 1` | x position on the axis labelled "tSNE 1" |
| `tSNE 2` | y position on the axis labelled "tSNE 2" |
| `marker area (pt^2)` | the marker's area, points squared |
| `colour` | the marker's fill colour, hex RGB |

### `annotations.csv` (78 B)

Every text printed in the panel: inside a subplot (x and y in that subplot's data coordinates; for an annotation with a leader line, the point it marks in `target x` and `target y`) or on the page around the subplots (x and y in inches from the page's top-left: the text's anchor).

| Column | Meaning |
|---|---|
| `subplot` | the subplot the text is in; blank for page text |
| `text` | the text as printed, on one line |
| `x`, `y` | its position (see `coordinates`) |
| `coordinates` | "data" or "page inches" |

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- decoration: the dashed category outlines: 4 QuadContourSet

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| PathCollection | 1 | 1 |
| QuadContourSet | 4 | 0 |
