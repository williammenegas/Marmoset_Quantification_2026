# figS11_a_recording_schedule

Figure S11, panel a. Title: "Recording schedule".

What the panel draws, in the data coordinates of each of its subplots: its points, lines, bars, maps and shapes as CSV, photographs and video frames as PNG, and every text printed on it in `annotations.csv`.

- Redrawn from this folder alone by [`code/figS11/figS11_a_recording_schedule.py`](../../../code/figS11/figS11_a_recording_schedule.py).

## Files

### `recording_schedule_lines.csv` (771 B)

From the subplot "Recording schedule" (row 1, column 1 of the panel's subplots, 0.43-4.12 in across and 0.53-1.88 in down the page), under the page text "Recording schedule"; no axis labels; drawn over x 0.435 to 4.115, y 1.881 to 0.531 (values beyond these limits are exported but were not visible).

One row is one vertex of one line; lines are separated by their "line" number.

| Column | Meaning |
|---|---|
| `line` | which line the vertex belongs to, numbered from 1 |
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |

Line styles: 26 lines: colour #262626, width 0.6 pt

### `recording_schedule_shapes.csv` (97.7 KB)

From the subplot "Recording schedule" (row 1, column 1 of the panel's subplots, 0.43-4.12 in across and 0.53-1.88 in down the page), under the page text "Recording schedule"; no axis labels; drawn over x 0.435 to 4.115, y 1.881 to 0.531 (values beyond these limits are exported but were not visible).

One row is one vertex of one shape's outline, curves sampled.

| Column | Meaning |
|---|---|
| `shape` | which shape, numbered from 1 in drawing order |
| `vertex` | the vertex's place along the outline |
| `x` | x position; this axis carries no label |
| `y` | y position; this axis carries no label |
| `shape type` | the matplotlib artist that drew it |
| `fill colour` | the shape's fill colour, hex RGB |
| `edge colour` | the shape's outline colour, hex RGB |

### `annotations.csv` (1.6 KB)

Every text printed in the panel: inside a subplot (x and y in that subplot's data coordinates; for an annotation with a leader line, the point it marks in `target x` and `target y`) or on the page around the subplots (x and y in inches from the page's top-left: the text's anchor).

| Column | Meaning |
|---|---|
| `subplot` | the subplot the text is in; blank for page text |
| `text` | the text as printed, on one line |
| `x`, `y` | its position (see `coordinates`) |
| `coordinates` | "data" or "page inches" |

## Schematics

The subplot "Recording schedule" is the recording schedule, drawn as labelled boxes. Its shapes are exported as drawn, in the subplot's own coordinates, and its texts are in annotations.csv; they show a design, not measurements.

## Not in these files

Left out because they carry no data; the panel's script draws them from its own settings: the axes, their ticks and labels, and what is listed here (a colour bar's colour map and limits are given above, with the data it keys).

- nothing else

## Checks

Artists found in the panel's subplots, and how many of each were exported:

| Type | Found | Exported |
|---|---|---|
| FancyBboxPatch | 26 | 26 |
| Line2D | 26 | 26 |
| PathPatch | 1 | 1 |
| Text | 35 | 35 |
