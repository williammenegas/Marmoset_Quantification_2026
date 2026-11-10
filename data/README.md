# Source data for the figures

The values behind every panel of the paper's figures and supplementary
figures, one folder per panel (and, for a figure with artwork no code
draws, one more for that artwork): what each panel draws, in the data
coordinates of its own axes, as CSV files (photographs and video frames as
PNG), with a README.md in every folder saying what each file holds.

The scripts in `code/` redraw each panel from its folder alone; see
`code/README.md`.

## Layout

```
data/
  README.md              this index
  LICENSE                CC BY 4.0
  fig1/ ... fig8/        the main figures
  figS1/ ... figS14/     the supplementary figures
    <figure>_artwork/    the figure's artwork, which no code draws: one
                         transparent image of the whole page (artwork.png)
                         and its README.md (only for a figure with artwork)
    <panel id>/          one panel, e.g. fig1/fig1_b_label_timeseries/
      README.md          its title, its files, their columns, what one row is
      *.csv, *.png       what it draws, subplot by subplot
      annotations.csv    every text printed on it (only where it prints any)
      page_shapes.csv    lines, arrows and swatches drawn on the page beside
                         it (only where it has them)
```

A panel id is `<figure>_<letter>_<name>`: the figure's folder, the panel's
letter as printed, and a short name for what it shows. The panel's script is
`code/<figure>/<panel id>.py`. A panel that is artwork pasted in
Illustrator, which no code draws, has no folder; the index lists it. A
figure with such artwork -- whole panels or parts of panels -- has it in
one more folder, `<figure>_artwork/`: one transparent image of the whole
page, which the page script draws over the panels.

## What a panel folder holds

- One file per subplot and kind of mark, named after the subplot and the
  kind: `points` (scatter points), `lines`, `bars` (bars and histograms,
  one row a bar), `boxes` (other rectangles, by their edges), `shapes`
  (filled areas and outlines, one row a vertex), `wedges`, `segments`,
  `contours`, `steps` (step plots, one row a step), `ribbons` (bands
  between stacked bars or boxes, by their ends), `flows` (a Sankey's
  counts, left boxes by right boxes), `map` (a matrix drawn as an image),
  `strip` (a one-row image), `colour_key` (a hand-made colour key) and
  `image` (a PNG).
- `annotations.csv`: every text printed in the panel, in its subplot's data
  coordinates, or in page inches for text on the page around the subplots
  (a panel that prints no such text has none).
- `README.md`: the panel's figure, letter and title; for every file, the
  subplot it comes from (its titles, axis labels, limits and place on the
  page), its columns, what one row is, and its colours, markers and colour
  limits; what is left out because it carries no data (axes, legends,
  colour bars, decoration such as cage wireframes and category outlines);
  and counts of what was found and exported.

## Units and conventions

- Values are in the units of the axis they are plotted on. A column is
  named after its axis label, and the README gives the unit where the label
  names one in brackets, e.g. `Time (min)`.
- A matrix (`map`, `flows`) has each column's x (or category) in its header
  row and each row's y (or category) in its first column. A map holding at
  least two cells for every pixel its image prints (at 400 dpi) is averaged
  in blocks down to print resolution, never below it, and its README says
  so.
- Along an axis of categories, a `category` column names the nearest tick
  label; swarm points keep their jittered x as `x_plot`.
- Positions on the page -- page texts, subplot boxes, page shapes -- are in
  inches from the page's top-left corner, x across and y down; the page is
  8.5 x 11 in.
- Colours are hex RGB, `#rrggbb`, with a fourth byte for opacity where a
  colour is see-through (`#rrggbbaa`); `none` is no colour. Line widths and
  marker sizes are in points, marker areas in points squared, angles in
  degrees anticlockwise from +x.
- Numbers carry eight significant figures; an empty cell is a missing value.

## Licence

The data in this folder is licensed under the Creative Commons Attribution
4.0 International License (CC BY 4.0); see `LICENSE`. You may share and
adapt it for any purpose, provided you give appropriate credit, link to the
license and indicate if changes were made.

## Index

107 panels drawn by code, 184.5 MB in all; a panel marked "artwork pasted in Illustrator; not drawn by code" has no folder.

### Figure 1 (`fig1/`, 2.3 MB)

| Panel | Folder | Title | Files | Size |
|---|---|---|---|---|
| a | `fig1_a_homecage_video` | "Homecage video", "Label accuracy" | artwork pasted in Illustrator; not drawn by code | |
| b | [`fig1_b_label_timeseries`](fig1/fig1_b_label_timeseries/README.md) | "Label timeseries" | `annotations.csv` (71 B); `label_timeseries_lines.csv` (582.1 KB) | 582.2 KB |
| c | [`fig1_c_labeled_image`](fig1/fig1_c_labeled_image/README.md) | "Labeled image" | `annotations.csv` (68 B); `labeled_image.png` (187.3 KB); `labeled_image_lines.csv` (13.6 KB) | 201.0 KB |
| d | [`fig1_d_paths_by_id`](fig1/fig1_d_paths_by_id/README.md) | "Sorted by ID" | `animal_1_lines.csv` (221.7 KB); `animal_2_lines.csv` (225.6 KB); `animal_3_lines.csv` (225.5 KB); `animal_4_lines.csv` (229.3 KB); `annotations.csv` (200 B) | 902.3 KB |
| e | [`fig1_e_raw_pca`](fig1/fig1_e_raw_pca/README.md) | "Raw data", "PCA" | `annotations.csv` (251 B); `pca_bars.csv` (925 B); `pca_lines.csv` (105 B); `x_coordinates_map.csv` (87.0 KB); `y_coordinates_map.csv` (86.8 KB) | 175.1 KB |
| f | [`fig1_f_egocentric_pca`](fig1/fig1_f_egocentric_pca/README.md) | "Egocentric data", "PCA" | `annotations.csv` (260 B); `pca_bars.csv` (861 B); `pca_lines.csv` (107 B); `x_coordinates_map.csv` (85.6 KB); `y_coordinates_map.csv` (85.3 KB) | 172.1 KB |
| artwork | [`fig1_artwork`](fig1/fig1_artwork/README.md) | the page's artwork, drawn over its panels | `artwork.png` (251.9 KB) | 251.9 KB |

### Figure 2 (`fig2/`, 443.7 KB)

| Panel | Folder | Title | Files | Size |
|---|---|---|---|---|
| a | [`fig2_a_state_usage_tsne`](fig2/fig2_a_state_usage_tsne/README.md) | "Behavioral state usage" | `annotations.csv` (78 B); `behavioral_state_usage_points.csv` (2.6 KB) | 2.7 KB |
| b | [`fig2_b_state_raster`](fig2/fig2_b_state_raster/README.md) | (no title printed) | `behavioral_state_vs_time_min_boxes.csv` (187 B); `behavioral_state_vs_time_min_points.csv` (199.4 KB) | 199.5 KB |
| c | `fig2_c_model_schematic` | (no title printed) | artwork pasted in Illustrator; not drawn by code | |
| d | [`fig2_d_category_maps`](fig2/fig2_d_category_maps/README.md) | "Model output", "Climbing", "Active", "Alone", "Social active", "Social resting" | `active_map.csv` (25.8 KB); `alone_map.csv` (26.6 KB); `annotations.csv` (255 B); `climbing_map.csv` (26.5 KB); `model_output_image.png` (3.8 KB); `social_active_map.csv` (27.1 KB); `social_resting_map.csv` (23.1 KB) | 133.2 KB |
| e | [`fig2_e_state_usage`](fig2/fig2_e_state_usage/README.md) | "Behavioral state usage" | `annotations.csv` (79 B); `behavioral_state_usage_bars.csv` (2.1 KB) | 2.2 KB |
| f | [`fig2_f_cluster_levels`](fig2/fig2_f_cluster_levels/README.md) | "4 clusters", "18 clusters", "80 clusters" | `18_clusters_points.csv` (604 B); `4_clusters_points.csv` (168 B); `80_clusters_points.csv` (2.6 KB); `annotations.csv` (544 B) | 3.9 KB |
| g | [`fig2_g_bout_duration`](fig2/fig2_g_bout_duration/README.md) | "Mean bout duration" | `annotations.csv` (75 B); `mean_bout_duration_lines.csv` (365 B); `mean_bout_duration_points.csv` (8.9 KB) | 9.3 KB |
| artwork | [`fig2_artwork`](fig2/fig2_artwork/README.md) | the page's artwork, drawn over its panels | `artwork.png` (92.9 KB) | 92.9 KB |

### Figure 3 (`fig3/`, 811.1 KB)

| Panel | Folder | Title | Files | Size |
|---|---|---|---|---|
| a | [`fig3_a_category_rasters`](fig3/fig3_a_category_rasters/README.md) | "Animal 1", "Animal 2" | `active_1_image.png` (273 B); `active_2_image.png` (296 B); `alone_1_image.png` (307 B); `alone_2_image.png` (299 B); `annotations.csv` (528 B); `climbing_1_image.png` (171 B); `climbing_2_image.png` (194 B); `near_bed_1_image.png` (256 B); `near_bed_2_image.png` (282 B); `social_active_1_image.png` (281 B); `social_active_2_image.png` (283 B); `social_rest_1_image.png` (294 B); `social_rest_2_image.png` (260 B) | 3.7 KB |
| b | [`fig3_b_tsne_by_day`](fig3/fig3_b_tsne_by_day/README.md) | "Day 1", "Day 2", "Day 3", "Day 4" | `annotations.csv` (263 B); `day_1_animal_1_points.csv` (2.6 KB); `day_1_animal_2_points.csv` (2.6 KB); `day_2_1_points.csv` (2.6 KB); `day_2_2_points.csv` (2.6 KB); `day_3_1_points.csv` (2.6 KB); `day_3_2_points.csv` (2.6 KB); `day_4_1_points.csv` (2.6 KB); `day_4_2_points.csv` (2.6 KB) | 21.2 KB |
| c | [`fig3_c_animal_session_shares`](fig3/fig3_c_animal_session_shares/README.md) | "Distribution - single animal" | `active_bars.csv` (3.6 KB); `alone_bars.csv` (3.6 KB); `annotations.csv` (203 B); `climbing_bars.csv` (3.6 KB); `page_shapes.csv` (63 B); `social_bars.csv` (3.6 KB) | 14.6 KB |
| d | [`fig3_d_all_session_shares`](fig3/fig3_d_all_session_shares/README.md) | "Distribution - all animals" | `active_bars.csv` (1.4 KB); `alone_bars.csv` (1.4 KB); `annotations.csv` (208 B); `climbing_bars.csv` (1.4 KB); `page_shapes.csv` (61 B); `social_bars.csv` (1.4 KB) | 5.9 KB |
| e | [`fig3_e_cagemate_correlation`](fig3/fig3_e_cagemate_correlation/README.md) | "Single cage", "All cages", "Cagemates vs shuffle", "Shuffle vs Paired" | `all_cages_1_lines.csv` (193 B); `all_cages_1_points.csv` (90.5 KB); `all_cages_2_lines.csv` (193 B); `all_cages_2_points.csv` (89.7 KB); `all_cages_3_lines.csv` (193 B); `all_cages_3_points.csv` (90.1 KB); `all_cages_4_lines.csv` (192 B); `all_cages_4_points.csv` (93.0 KB); `all_cages_5_lines.csv` (193 B); `all_cages_5_points.csv` (91.4 KB); `annotations.csv` (423 B); `cagemates_vs_shuffle_1_bars.csv` (2.7 KB); `cagemates_vs_shuffle_1_lines.csv` (49 B); `cagemates_vs_shuffle_2_bars.csv` (2.6 KB); `cagemates_vs_shuffle_2_lines.csv` (49 B); `cagemates_vs_shuffle_3_bars.csv` (2.7 KB); `cagemates_vs_shuffle_3_lines.csv` (49 B); `cagemates_vs_shuffle_4_bars.csv` (2.6 KB); `cagemates_vs_shuffle_4_lines.csv` (49 B); `cagemates_vs_shuffle_5_bars.csv` (2.7 KB); `cagemates_vs_shuffle_5_lines.csv` (49 B); `shuffle_vs_paired_lines.csv` (897 B); `shuffle_vs_paired_points.csv` (176.2 KB); `single_cage_each_animal_fraction_active_lines.csv` (1.6 KB); `single_cage_each_animal_fraction_alone_lines.csv` (1.6 KB); `single_cage_each_animal_fraction_climbing_lines.csv` (1.6 KB); `single_cage_each_animal_fraction_soc_act_lines.csv` (1.6 KB); `single_cage_each_animal_fraction_soc_rest_lines.csv` (1.6 KB) | 654.6 KB |
| artwork | [`fig3_artwork`](fig3/fig3_artwork/README.md) | the page's artwork, drawn over its panels | `artwork.png` (111.1 KB) | 111.1 KB |

### Figure 4 (`fig4/`, 28.0 MB)

| Panel | Folder | Title | Files | Size |
|---|---|---|---|---|
| a | [`fig4_a_mic_recording`](fig4/fig4_a_mic_recording/README.md) | "Recording", "Amplitude", "Spectrogram" | `amplitude_1_lines.csv` (132 B); `amplitude_1_shapes.csv` (151.8 KB); `amplitude_2_lines.csv` (132 B); `amplitude_2_shapes.csv` (152.1 KB); `amplitude_3_lines.csv` (132 B); `amplitude_3_shapes.csv` (153.5 KB); `amplitude_4_lines.csv` (132 B); `amplitude_4_shapes.csv` (153.5 KB); `annotations.csv` (611 B); `recording_boxes.csv` (238 B); `recording_lines.csv` (950 B); `recording_lines_2.csv` (928 B); `recording_other_lines.csv` (1.5 KB); `recording_shapes.csv` (21.2 KB); `spectrogram_1_lines.csv` (134 B); `spectrogram_1_map.csv` (362.7 KB); `spectrogram_2_lines.csv` (134 B); `spectrogram_2_map.csv` (362.7 KB); `spectrogram_3_lines.csv` (134 B); `spectrogram_3_map.csv` (362.7 KB); `spectrogram_4_lines.csv` (134 B); `spectrogram_4_map.csv` (362.7 KB) | 2.1 MB |
| b | [`fig4_b_call_detection`](fig4/fig4_b_call_detection/README.md) | (no title printed) | `annotations.csv` (339 B); `frequency_khz_vs_time_minutes_1_colour_key.csv` (4.8 KB); `frequency_khz_vs_time_minutes_1_lines.csv` (62 B); `frequency_khz_vs_time_minutes_1_map.csv` (12.9 MB); `frequency_khz_vs_time_minutes_2_colour_key.csv` (4.8 KB); `frequency_khz_vs_time_minutes_2_lines.csv` (62 B); `frequency_khz_vs_time_minutes_2_map.csv` (12.9 MB) | 25.8 MB |
| c | [`fig4_c_time_near_other`](fig4/fig4_c_time_near_other/README.md) | (no title printed) | `number_of_clips_vs_time_near_other_bars.csv` (800 B) | 800 B |
| d | [`fig4_d_calls_per_minute`](fig4/fig4_d_calls_per_minute/README.md) | (no title printed) | `annotations.csv` (112 B); `number_of_clips_vs_calls_per_minute_bars.csv` (704 B) | 816 B |
| e | [`fig4_e_clip_sequence`](fig4/fig4_e_clip_sequence/README.md) | (no title printed) | `annotations.csv` (143 B); `call_rate_vs_segment_boxes.csv` (1.6 KB); `call_rate_vs_segment_steps.csv` (3.0 KB); `page_shapes.csv` (499 B); `time_near_other_vs_segment_boxes.csv` (1.5 KB); `time_near_other_vs_segment_steps.csv` (4.0 KB) | 10.7 KB |
| f | [`fig4_f_call_rate_vs_category`](fig4/fig4_f_call_rate_vs_category/README.md) | "Climb", "Active", "Alone", "Soc-act", "Soc-rest" | `active_lines.csv` (78 B); `active_points.csv` (3.2 KB); `alone_lines.csv` (72 B); `alone_points.csv` (3.1 KB); `annotations.csv` (362 B); `climb_lines.csv` (72 B); `climb_points.csv` (2.7 KB); `soc_act_lines.csv` (79 B); `soc_act_points.csv` (3.4 KB); `soc_rest_lines.csv` (79 B); `soc_rest_points.csv` (3.3 KB) | 16.4 KB |
| g | [`fig4_g_category_corr`](fig4/fig4_g_category_corr/README.md) | (no title printed) | `annotations.csv` (65 B); `spearman_rho_lines.csv` (418 B); `spearman_rho_points.csv` (13.7 KB) | 14.2 KB |
| h | [`fig4_h_loud_cage_map`](fig4/fig4_h_loud_cage_map/README.md) | "Cage space" | `annotations.csv` (65 B); `cage_space_map.csv` (13.9 KB) | 14.0 KB |
| i | [`fig4_i_loud_tsne_map`](fig4/fig4_i_loud_tsne_map/README.md) | "Behavioral space" | `annotations.csv` (71 B); `behavioral_space_map.csv` (12.8 KB) | 12.9 KB |
| j | [`fig4_j_mean_state_corr`](fig4/fig4_j_mean_state_corr/README.md) | (no title printed) | `annotations.csv` (415 B); `mean_rho_across_animals_vs_level_5_behavioral_state_bars.csv` (2.4 KB); `mean_rho_across_animals_vs_level_5_behavioral_state_lines.csv` (78 B) | 2.9 KB |
| k | [`fig4_k_animal_state_corr`](fig4/fig4_k_animal_state_corr/README.md) | (no title printed) | `animal_vs_level_5_behavioral_state_map.csv` (63.6 KB); `annotations.csv` (311 B) | 63.9 KB |

### Figure 5 (`fig5/`, 88.5 KB)

| Panel | Folder | Title | Files | Size |
|---|---|---|---|---|
| a | [`fig5_a_session_tsne`](fig5/fig5_a_session_tsne/README.md) | "Control 1", "Control 2", "Control 3", "Control 4", "Box", "Example animal" | `annotations.csv` (238 B); `box_points.csv` (3.4 KB); `control_1_points.csv` (3.4 KB); `control_2_points.csv` (3.4 KB); `control_3_points.csv` (3.4 KB); `control_4_points.csv` (3.4 KB) | 17.1 KB |
| b | [`fig5_b_category_rasters`](fig5/fig5_b_category_rasters/README.md) | (no title printed) | `active_1_image.png` (286 B); `active_2_image.png` (275 B); `active_3_image.png` (286 B); `active_4_image.png` (254 B); `active_6_image.png` (274 B); `alone_1_image.png` (271 B); `alone_2_image.png` (276 B); `alone_3_image.png` (262 B); `alone_4_image.png` (286 B); `alone_6_image.png` (310 B); `annotations.csv` (685 B); `climbing_box_image.png` (248 B); `climbing_control_1_image.png` (248 B); `climbing_control_2_image.png` (180 B); `climbing_control_3_image.png` (254 B); `climbing_control_4_image.png` (234 B); `near_box_1_image.png` (180 B); `near_box_2_image.png` (122 B); `near_box_3_image.png` (164 B); `near_box_4_image.png` (179 B); `near_box_6_image.png` (263 B); `social_active_box_image.png` (290 B); `social_active_control_1_image.png` (220 B); `social_active_control_2_image.png` (288 B); `social_active_control_3_image.png` (188 B); `social_active_control_4_image.png` (266 B); `social_rest_1_image.png` (193 B); `social_rest_2_image.png` (277 B); `social_rest_3_image.png` (187 B); `social_rest_4_image.png` (277 B); `social_rest_6_image.png` (291 B) | 8.0 KB |
| c | [`fig5_c_state_usage`](fig5/fig5_c_state_usage/README.md) | "State usage (Control)", "State usage (Tablet)" | `annotations.csv` (188 B); `frequency_pct_vs_behavioral_state_1_bars.csv` (1.7 KB); `frequency_pct_vs_behavioral_state_2_bars.csv` (1.7 KB) | 3.5 KB |
| d | [`fig5_d_usage_discriminability`](fig5/fig5_d_usage_discriminability/README.md) | "Example state", "All states", "Discriminability" | `all_states_lines.csv` (82 B); `all_states_points.csv` (1.7 KB); `all_states_segments.csv` (7.1 KB); `annotations.csv` (501 B); `discriminability_control_tablet_lines.csv` (425 B); `discriminability_control_tablet_points.csv` (6.0 KB); `example_state_control_tablet_lines.csv` (5.7 KB); `example_state_control_tablet_points.csv` (5.5 KB) | 27.0 KB |
| e | [`fig5_e_state_corr`](fig5/fig5_e_state_corr/README.md) | "State correlation (Control)", "State correlation (Tablet)" | `annotations.csv` (198 B); `correlation_vs_behavioral_state_1_bars.csv` (1.8 KB); `correlation_vs_behavioral_state_1_lines.csv` (54 B); `correlation_vs_behavioral_state_2_bars.csv` (1.8 KB); `correlation_vs_behavioral_state_2_lines.csv` (54 B) | 3.9 KB |
| f | [`fig5_f_corr_discriminability`](fig5/fig5_f_corr_discriminability/README.md) | "Example state", "All states", "Discriminability" | `all_states_lines.csv` (100 B); `all_states_points.csv` (2.0 KB); `all_states_segments.csv` (8.2 KB); `annotations.csv` (505 B); `discriminability_control_tablet_lines.csv` (426 B); `discriminability_control_tablet_points.csv` (6.0 KB); `example_state_control_tablet_lines.csv` (6.0 KB); `example_state_control_tablet_points.csv` (5.7 KB) | 28.9 KB |

### Figure 6 (`fig6/`, 323.7 KB)

| Panel | Folder | Title | Files | Size |
|---|---|---|---|---|
| a | [`fig6_a_response_maps`](fig6/fig6_a_response_maps/README.md) | "Tablet (neutral)", "Tablet (social)", "Intruder", "Mask", "Treat", "Toys", "Noise", "Object", "Cage space", "Behavioral space" | `annotations.csv` (703 B); `intruder_t_sne_2_map.csv` (14.9 KB); `intruder_y_px_map.csv` (14.4 KB); `mask_t_sne_2_map.csv` (14.5 KB); `mask_y_px_map.csv` (15.2 KB); `noise_t_sne_2_map.csv` (14.8 KB); `noise_y_px_map.csv` (14.2 KB); `object_t_sne_2_map.csv` (14.9 KB); `object_y_px_map.csv` (14.2 KB); `tablet_neutral_t_sne_2_map.csv` (15.0 KB); `tablet_neutral_y_px_map.csv` (13.1 KB); `tablet_social_t_sne_2_map.csv` (15.1 KB); `tablet_social_y_px_map.csv` (13.1 KB); `toys_t_sne_2_map.csv` (14.8 KB); `toys_y_px_map.csv` (14.0 KB); `treat_t_sne_2_map.csv` (14.9 KB); `treat_y_px_map.csv` (14.4 KB) | 232.5 KB |
| b | [`fig6_b_group_projection`](fig6/fig6_b_group_projection/README.md) | (no title printed) | `projection_on_the_group_response_lines.csv` (78 B); `projection_on_the_group_response_points.csv` (33.9 KB) | 34.0 KB |
| c | [`fig6_c_stimulus_auroc`](fig6/fig6_c_stimulus_auroc/README.md) | (no title printed) | `auroc_vs_held_out_control_bars.csv` (336 B); `auroc_vs_held_out_control_boxes.csv` (109 B); `auroc_vs_held_out_control_lines.csv` (421 B) | 866 B |
| d | [`fig6_d_heldout_projection`](fig6/fig6_d_heldout_projection/README.md) | (no title printed) | `projection_lines.csv` (1.2 KB); `projection_points.csv` (54.0 KB) | 55.2 KB |
| e | [`fig6_e_pairwise_auroc`](fig6/fig6_e_pairwise_auroc/README.md) | (no title printed) | `annotations.csv` (626 B); `map.csv` (581 B) | 1.2 KB |

### Figure 7 (`fig7/`, 305.7 KB)

| Panel | Folder | Title | Files | Size |
|---|---|---|---|---|
| a | [`fig7_a_split_cage_enrichment`](fig7/fig7_a_split_cage_enrichment/README.md) | "Alternating", "Early vs late", "Cage locations enriched in each cluster-based group", "Box", "Intruder", "Mask" | `alternating_lines.csv` (176 B); `annotations.csv` (425 B); `box_group_1_map.csv` (20.0 KB); `box_group_2_map.csv` (21.0 KB); `box_group_3_map.csv` (20.8 KB); `early_vs_late_lines.csv` (176 B); `intruder_1_map.csv` (20.5 KB); `intruder_2_map.csv` (20.5 KB); `intruder_3_map.csv` (20.8 KB); `mask_1_map.csv` (20.0 KB); `mask_2_map.csv` (20.2 KB); `mask_3_map.csv` (20.2 KB) | 184.8 KB |
| b | [`fig7_b_alternating_halves`](fig7/fig7_b_alternating_halves/README.md) | "Alternating" | `alternating_animal_half_1_boxes.csv` (126 B); `alternating_animal_half_1_lines.csv` (143 B); `alternating_animal_half_1_map.csv` (47.8 KB); `alternating_boxes.csv` (166 B); `alternating_flows.csv` (90 B); `alternating_ribbons.csv` (476 B); `annotations.csv` (531 B) | 49.3 KB |
| c | [`fig7_c_early_late_halves`](fig7/fig7_c_early_late_halves/README.md) | "Early vs late" | `annotations.csv` (551 B); `early_vs_late_animal_half_1_boxes.csv` (126 B); `early_vs_late_animal_half_1_lines.csv` (143 B); `early_vs_late_animal_half_1_map.csv` (47.8 KB); `early_vs_late_boxes.csv` (166 B); `early_vs_late_flows.csv` (90 B); `early_vs_late_ribbons.csv` (572 B) | 49.4 KB |
| d | [`fig7_d_group_1_composite`](fig7/fig7_d_group_1_composite/README.md) | "Group 1 composite" | `annotations.csv` (115 B); `correlation_with_others_vs_features_bars.csv` (176 B); `group_1_composite_lines.csv` (51 B); `group_1_composite_points.csv` (2.1 KB) | 2.5 KB |
| e | [`fig7_e_group_2_composite`](fig7/fig7_e_group_2_composite/README.md) | "Group 2 composite" | `annotations.csv` (115 B); `correlation_with_others_vs_features_bars.csv` (227 B); `group_2_composite_lines.csv` (51 B); `group_2_composite_points.csv` (2.1 KB) | 2.5 KB |
| f | [`fig7_f_group_3_composite`](fig7/fig7_f_group_3_composite/README.md) | "Group 3 composite" | `annotations.csv` (115 B); `correlation_with_others_vs_features_bars.csv` (187 B); `group_3_composite_lines.csv` (51 B); `group_3_composite_points.csv` (2.1 KB) | 2.5 KB |
| g | [`fig7_g_composite_means`](fig7/fig7_g_composite_means/README.md) | "Total score per animal" | `annotations.csv` (78 B); `total_score_per_animal_lines.csv` (272 B); `total_score_per_animal_points.csv` (2.9 KB) | 3.2 KB |
| h | [`fig7_h_composite_halves`](fig7/fig7_h_composite_halves/README.md) | "Split per animal" | `annotations.csv` (70 B); `split_per_animal_lines.csv` (5.8 KB); `split_per_animal_points.csv` (5.3 KB) | 11.1 KB |
| i | [`fig7_i_age_by_group`](fig7/fig7_i_age_by_group/README.md) | (no title printed) | `adult_boxes.csv` (38 B); `animals_vs_group_bars.csv` (179 B); `annotations.csv` (94 B); `juvenile_boxes.csv` (38 B) | 349 B |

### Figure 8 (`fig8/`, 67.6 KB)

| Panel | Folder | Title | Files | Size |
|---|---|---|---|---|
| a | [`fig8_a_household_groups`](fig8/fig8_a_household_groups/README.md) | "Parents", "Juveniles" | `annotations.csv` (2.5 KB); `boxes.csv` (2.7 KB); `page_shapes.csv` (1.6 KB) | 6.8 KB |
| b | [`fig8_b_same_group_pairs`](fig8/fig8_b_same_group_pairs/README.md) | "Comparison to chance distribution" | `annotations.csv` (265 B); `page_shapes.csv` (63 B); `same_group_pct_boxes.csv` (168 B); `same_group_pct_lines.csv` (413 B) | 909 B |
| c | [`fig8_c_dimension_links`](fig8/fig8_c_dimension_links/README.md) | "Baseline dimensions", "Stimulus dimensions" | `annotations.csv` (828 B); `lines.csv` (564 B); `page_shapes.csv` (299 B); `shapes.csv` (44.2 KB) | 45.9 KB |
| d | [`fig8_d_predicted_variance`](fig8/fig8_d_predicted_variance/README.md) | "Variance (%) predicted using baseline dimensions" | `annotations.csv` (321 B); `share_predicted_pct_bars.csv` (166 B) | 487 B |
| e | [`fig8_e_positive_correlation`](fig8/fig8_e_positive_correlation/README.md) | "Example: positive correlation" | `annotations.csv` (164 B); `example_positive_correlation_lines.csv` (145 B); `example_positive_correlation_points.csv` (4.2 KB) | 4.5 KB |
| f | [`fig8_f_negative_correlation`](fig8/fig8_f_negative_correlation/README.md) | "Example: negative correlation" | `annotations.csv` (164 B); `example_negative_correlation_lines.csv` (144 B); `example_negative_correlation_points.csv` (4.2 KB) | 4.5 KB |
| g | [`fig8_g_no_correlation`](fig8/fig8_g_no_correlation/README.md) | "Example: no correlation" | `annotations.csv` (162 B); `example_no_correlation_lines.csv` (153 B); `example_no_correlation_points.csv` (4.2 KB) | 4.5 KB |

### Figure S1 (`figS1/`, 101.1 MB)

| Panel | Folder | Title | Files | Size |
|---|---|---|---|---|
| a | [`figS1_a_raw_components`](figS1/figS1_a_raw_components/README.md) | "Components of raw data" | `annotations.csv` (1.2 KB); `page_shapes.csv` (26.0 KB); `pc1_colour_key.csv` (4.8 KB); `pc1_plus_0_sd_lines.csv` (1.9 KB); `pc1_plus_1_sd_lines.csv` (1.9 KB); `pc1_plus_2_sd_lines.csv` (1.9 KB); `pc1_points.csv` (6.9 MB); `pc1_y_coordinate_points.csv` (4.6 MB); `pc2_colour_key.csv` (4.8 KB); `pc2_plus_0_sd_lines.csv` (1.9 KB); `pc2_plus_1_sd_lines.csv` (1.9 KB); `pc2_plus_2_sd_lines.csv` (1.9 KB); `pc2_points.csv` (6.9 MB); `pc2_x_coordinate_points.csv` (4.7 MB); `pc3_body_angle_points.csv` (4.7 MB); `pc3_colour_key.csv` (4.8 KB); `pc3_plus_0_sd_lines.csv` (1.9 KB); `pc3_plus_1_sd_lines.csv` (1.9 KB); `pc3_plus_2_sd_lines.csv` (1.9 KB); `pc3_points.csv` (6.9 MB); `pc4_body_angle_points.csv` (4.7 MB); `pc4_colour_key.csv` (4.8 KB); `pc4_plus_0_sd_lines.csv` (1.9 KB); `pc4_plus_1_sd_lines.csv` (1.9 KB); `pc4_plus_2_sd_lines.csv` (1.9 KB); `pc4_points.csv` (6.9 MB) | 46.4 MB |
| b | [`figS1_b_egocentric_components`](figS1/figS1_b_egocentric_components/README.md) | "Components of egocentric data" | `annotations.csv` (1.3 KB); `page_shapes.csv` (26.0 KB); `pc1_body_part_icon_lines.csv` (2.3 KB); `pc1_colour_key.csv` (4.8 KB); `pc1_front_hair_tuft_position_lines.csv` (81 B); `pc1_front_hair_tuft_position_points.csv` (6.9 MB); `pc1_plus_0_sd_lines.csv` (1.9 KB); `pc1_plus_1_sd_lines.csv` (1.9 KB); `pc1_plus_2_sd_lines.csv` (1.9 KB); `pc1_points.csv` (6.9 MB); `pc2_body_part_icon_lines.csv` (2.3 KB); `pc2_colour_key.csv` (4.8 KB); `pc2_front_hair_tuft_position_lines.csv` (81 B); `pc2_front_hair_tuft_position_points.csv` (6.9 MB); `pc2_plus_0_sd_lines.csv` (1.9 KB); `pc2_plus_1_sd_lines.csv` (1.9 KB); `pc2_plus_2_sd_lines.csv` (1.9 KB); `pc2_points.csv` (6.9 MB); `pc3_body_part_icon_lines.csv` (2.3 KB); `pc3_colour_key.csv` (4.8 KB); `pc3_front_right_hand_position_lines.csv` (79 B); `pc3_front_right_hand_position_points.csv` (6.6 MB); `pc3_plus_0_sd_lines.csv` (1.9 KB); `pc3_plus_1_sd_lines.csv` (1.9 KB); `pc3_plus_2_sd_lines.csv` (1.9 KB); `pc3_points.csv` (6.9 MB); `pc4_body_part_icon_lines.csv` (2.3 KB); `pc4_colour_key.csv` (4.8 KB); `pc4_front_left_hand_position_lines.csv` (80 B); `pc4_front_left_hand_position_points.csv` (6.8 MB); `pc4_plus_0_sd_lines.csv` (1.9 KB); `pc4_plus_1_sd_lines.csv` (1.9 KB); `pc4_plus_2_sd_lines.csv` (1.9 KB); `pc4_points.csv` (6.9 MB) | 54.7 MB |

### Figure S2 (`figS2/`, 13.1 MB)

| Panel | Folder | Title | Files | Size |
|---|---|---|---|---|
| a | `figS2_a_depth_methods` | "Multi-camera array", "Single view", "Stereo vision", "Mesh grid extraction" | artwork pasted in Illustrator; not drawn by code | |
| b | [`figS2_b_single_view`](figS2/figS2_b_single_view/README.md) | "Single view" | `annotations.csv` (240 B); `head_radius_px_vs_state_category_frames_lines.csv` (385 B); `head_radius_px_vs_state_category_frames_points.csv` (66.2 KB) | 66.9 KB |
| c | [`figS2_c_single_view_trace`](figS2/figS2_c_single_view_trace/README.md) | "Example animal" | `annotations.csv` (123 B); `example_animal_boxes.csv` (371 B); `example_animal_head_radius_px_boxes.csv` (415 B); `example_animal_head_radius_px_lines.csv` (51.9 KB) | 52.8 KB |
| d | [`figS2_d_stereo_view`](figS2/figS2_d_stereo_view/README.md) | "Stereo vision" | `annotations.csv` (240 B); `head_depth_a_u_vs_state_category_frames_lines.csv` (379 B); `head_depth_a_u_vs_state_category_frames_points.csv` (65.5 KB) | 66.2 KB |
| e | [`figS2_e_stereo_view_trace`](figS2/figS2_e_stereo_view_trace/README.md) | (no title printed) | `head_depth_a_u_vs_time_min_boxes.csv` (431 B); `head_depth_a_u_vs_time_min_lines.csv` (63 B); `head_depth_a_u_vs_time_min_segments.csv` (81.6 KB); `time_min_boxes.csv` (371 B) | 82.5 KB |
| f | [`figS2_f_mesh_grid`](figS2/figS2_f_mesh_grid/README.md) | "Mesh grid" | `annotations.csv` (65 B); `depth_a_u_vs_mesh_points_sorted_lines.csv` (7.0 KB); `depth_a_u_vs_mesh_points_sorted_shapes.csv` (37.6 KB) | 44.7 KB |
| g | [`figS2_g_mesh_grid_trace`](figS2/figS2_g_mesh_grid_trace/README.md) | (no title printed) | `mesh_points_sorted_vs_time_min_lines.csv` (889 B); `mesh_points_sorted_vs_time_min_map.csv` (6.7 MB); `time_min_boxes.csv` (371 B) | 6.7 MB |
| h | [`figS2_h_depth_correction`](figS2/figS2_h_depth_correction/README.md) | "Raw data", "Depth correction applied", "Top view (raw)", "Side view (raw)", "Top view (corrected)", "Side view (corrected)" | `annotations.csv` (308 B); `page_shapes.csv` (91 B); `side_view_corrected_points.csv` (1.1 MB); `side_view_raw_points.csv` (1.1 MB); `top_view_corrected_points.csv` (1.2 MB); `top_view_raw_points.csv` (1.2 MB) | 4.6 MB |
| artwork | [`figS2_artwork`](figS2/figS2_artwork/README.md) | the page's artwork, drawn over its panels | `artwork.png` (1.5 MB) | 1.5 MB |

### Figure S3 (`figS3/`, 660.6 KB)

| Panel | Folder | Title | Files | Size |
|---|---|---|---|---|
| a | [`figS3_a_hierarchy_flow`](figS3/figS3_a_hierarchy_flow/README.md) | (no title printed) | `annotations.csv` (384 B); `level_5_behavioral_state_boxes.csv` (6.1 KB); `level_5_behavioral_state_shapes.csv` (646.5 KB) | 653.0 KB |
| b | [`figS3_b_hierarchy_usage`](figS3/figS3_b_hierarchy_usage/README.md) | (no title printed) | `annotations.csv` (176 B); `level_5_behavioral_state_boxes.csv` (4.1 KB); `usage_vs_level_5_behavioral_state_bars.csv` (3.4 KB) | 7.7 KB |

### Figure S4 (`figS4/`, 2.6 MB)

| Panel | Folder | Title | Files | Size |
|---|---|---|---|---|
| a | [`figS4_a_description_levels`](figS4/figS4_a_description_levels/README.md) | (no title printed) | `all_level_1_1_shapes.csv` (1.7 KB); `all_level_1_2_shapes.csv` (1.7 KB); `all_level_1_3_shapes.csv` (1.7 KB); `all_level_2_1_shapes.csv` (3.8 KB); `all_level_2_2_shapes.csv` (3.8 KB); `all_level_2_3_shapes.csv` (3.8 KB); `all_level_3_1_shapes.csv` (8.8 KB); `all_level_3_2_shapes.csv` (8.8 KB); `all_level_3_3_shapes.csv` (8.8 KB); `all_level_4_1_shapes.csv` (13.2 KB); `all_level_4_2_shapes.csv` (13.2 KB); `all_level_4_3_shapes.csv` (13.2 KB); `all_level_5_1_shapes.csv` (37.0 KB); `all_level_5_2_shapes.csv` (37.0 KB); `all_level_5_3_shapes.csv` (37.0 KB); `annotations.csv` (1.3 KB); `body_moving_undirected_level_1_shapes.csv` (1.7 KB); `body_moving_undirected_level_2_shapes.csv` (3.8 KB); `body_moving_undirected_level_3_shapes.csv` (8.8 KB); `body_moving_undirected_level_4_shapes.csv` (13.2 KB); `body_moving_undirected_level_5_shapes.csv` (37.0 KB); `from_other_level_1_shapes.csv` (1.7 KB); `from_other_level_2_shapes.csv` (3.8 KB); `from_other_level_3_shapes.csv` (8.8 KB); `from_other_level_4_shapes.csv` (13.2 KB); `from_other_level_5_shapes.csv` (37.0 KB); `get_level_1_shapes.csv` (1.7 KB); `get_level_2_shapes.csv` (3.8 KB); `get_level_3_shapes.csv` (8.8 KB); `get_level_4_shapes.csv` (13.2 KB); `get_level_5_shapes.csv` (37.0 KB); `give_level_1_shapes.csv` (1.7 KB); `give_level_2_shapes.csv` (3.8 KB); `give_level_3_shapes.csv` (8.8 KB); `give_level_4_shapes.csv` (13.2 KB); `give_level_5_shapes.csv` (37.0 KB); `head_moving_undirected_level_1_shapes.csv` (1.7 KB); `head_moving_undirected_level_2_shapes.csv` (3.8 KB); `head_moving_undirected_level_3_shapes.csv` (8.8 KB); `head_moving_undirected_level_4_shapes.csv` (13.2 KB); `head_moving_undirected_level_5_shapes.csv` (37.0 KB); `interacting_level_1_shapes.csv` (1.7 KB); `interacting_level_2_shapes.csv` (3.8 KB); `interacting_level_3_shapes.csv` (8.8 KB); `interacting_level_4_shapes.csv` (13.2 KB); `interacting_level_5_shapes.csv` (37.0 KB); `limb_level_1_shapes.csv` (1.7 KB); `limb_level_2_shapes.csv` (3.8 KB); `limb_level_3_shapes.csv` (8.8 KB); `limb_level_4_shapes.csv` (13.2 KB); `limb_level_5_shapes.csv` (37.0 KB); `look_at_level_1_shapes.csv` (1.7 KB); `look_at_level_2_shapes.csv` (3.8 KB); `look_at_level_3_shapes.csv` (8.8 KB); `look_at_level_4_shapes.csv` (13.2 KB); `look_at_level_5_shapes.csv` (37.0 KB); `near_other_level_1_shapes.csv` (1.7 KB); `near_other_level_2_shapes.csv` (3.8 KB); `near_other_level_3_shapes.csv` (8.8 KB); `near_other_level_4_shapes.csv` (13.2 KB); `near_other_level_5_shapes.csv` (37.0 KB); `page_shapes.csv` (135 B); `side_by_level_1_shapes.csv` (1.7 KB); `side_by_level_2_shapes.csv` (3.8 KB); `side_by_level_3_shapes.csv` (8.8 KB); `side_by_level_4_shapes.csv` (13.2 KB); `side_by_level_5_shapes.csv` (37.0 KB); `to_other_level_1_shapes.csv` (1.7 KB); `to_other_level_2_shapes.csv` (3.8 KB); `to_other_level_3_shapes.csv` (8.8 KB); `to_other_level_4_shapes.csv` (13.2 KB); `to_other_level_5_shapes.csv` (37.0 KB); `upright_level_1_shapes.csv` (1.7 KB); `upright_level_2_shapes.csv` (3.8 KB); `upright_level_3_shapes.csv` (8.8 KB); `upright_level_4_shapes.csv` (13.2 KB); `upright_level_5_shapes.csv` (37.0 KB) | 969.5 KB |
| b | [`figS4_b_description_lags`](figS4/figS4_b_description_lags/README.md) | (no title printed) | `all_10_sec_prior_1_shapes.csv` (37.0 KB); `all_10_sec_prior_2_shapes.csv` (37.0 KB); `all_10_sec_prior_3_shapes.csv` (37.0 KB); `all_1_sec_prior_1_shapes.csv` (37.0 KB); `all_1_sec_prior_2_shapes.csv` (37.0 KB); `all_1_sec_prior_3_shapes.csv` (37.0 KB); `all_60_sec_prior_1_shapes.csv` (37.0 KB); `all_60_sec_prior_2_shapes.csv` (37.0 KB); `all_60_sec_prior_3_shapes.csv` (37.0 KB); `annotations.csv` (1.1 KB); `body_moving_undirected_10_sec_prior_shapes.csv` (37.0 KB); `body_moving_undirected_1_sec_prior_shapes.csv` (37.0 KB); `body_moving_undirected_60_sec_prior_shapes.csv` (37.0 KB); `from_other_10_sec_prior_shapes.csv` (37.0 KB); `from_other_1_sec_prior_shapes.csv` (37.0 KB); `from_other_60_sec_prior_shapes.csv` (37.0 KB); `get_10_sec_prior_shapes.csv` (37.0 KB); `get_1_sec_prior_shapes.csv` (37.0 KB); `get_60_sec_prior_shapes.csv` (37.0 KB); `give_10_sec_prior_shapes.csv` (37.0 KB); `give_1_sec_prior_shapes.csv` (37.0 KB); `give_60_sec_prior_shapes.csv` (37.0 KB); `head_moving_undirected_10_sec_prior_shapes.csv` (37.0 KB); `head_moving_undirected_1_sec_prior_shapes.csv` (37.0 KB); `head_moving_undirected_60_sec_prior_shapes.csv` (37.0 KB); `interacting_10_sec_prior_shapes.csv` (37.0 KB); `interacting_1_sec_prior_shapes.csv` (37.0 KB); `interacting_60_sec_prior_shapes.csv` (37.0 KB); `limb_10_sec_prior_shapes.csv` (37.0 KB); `limb_1_sec_prior_shapes.csv` (37.0 KB); `limb_60_sec_prior_shapes.csv` (37.0 KB); `look_at_10_sec_prior_shapes.csv` (37.0 KB); `look_at_1_sec_prior_shapes.csv` (37.0 KB); `look_at_60_sec_prior_shapes.csv` (37.0 KB); `near_other_10_sec_prior_shapes.csv` (37.0 KB); `near_other_1_sec_prior_shapes.csv` (37.0 KB); `near_other_60_sec_prior_shapes.csv` (37.0 KB); `page_shapes.csv` (135 B); `side_by_10_sec_prior_shapes.csv` (37.0 KB); `side_by_1_sec_prior_shapes.csv` (37.0 KB); `side_by_60_sec_prior_shapes.csv` (37.0 KB); `to_other_10_sec_prior_shapes.csv` (37.0 KB); `to_other_1_sec_prior_shapes.csv` (37.0 KB); `to_other_60_sec_prior_shapes.csv` (37.0 KB); `upright_10_sec_prior_shapes.csv` (37.0 KB); `upright_1_sec_prior_shapes.csv` (37.0 KB); `upright_60_sec_prior_shapes.csv` (37.0 KB) | 1.7 MB |

### Figure S5 (`figS5/`, 61.2 KB)

| Panel | Folder | Title | Files | Size |
|---|---|---|---|---|
| a | [`figS5_a_transition_matrices`](figS5/figS5_a_transition_matrices/README.md) | "Shuffled", "Observed" | `annotations.csv` (101 B); `observed_lines.csv` (164 B); `observed_map.csv` (14.7 KB); `shuffled_lines.csv` (164 B); `shuffled_map.csv` (27.0 KB) | 42.1 KB |
| b | [`figS5_b_entropy_memory`](figS5/figS5_b_entropy_memory/README.md) | "Entropy rate", "Structure", "Memory" | `annotations.csv` (268 B); `entropy_rate_shuffled_observed_lines.csv` (7.5 KB); `entropy_rate_shuffled_observed_points.csv` (7.2 KB); `memory_lines.csv` (378 B); `memory_shapes.csv` (539 B); `structure_lines.csv` (129 B); `structure_points.csv` (3.1 KB) | 19.1 KB |

### Figure S6 (`figS6/`, 450.3 KB)

| Panel | Folder | Title | Files | Size |
|---|---|---|---|---|
| a | [`figS6_a_state_flow`](figS6/figS6_a_state_flow/README.md) | "Example animal" | `annotations.csv` (209 B); `example_animal_boxes.csv` (180.8 KB); `example_animal_ribbons.csv` (269.3 KB) | 450.3 KB |

### Figure S7 (`figS7/`, 1.7 MB)

| Panel | Folder | Title | Files | Size |
|---|---|---|---|---|
| a | [`figS7_a_category_usage`](figS7/figS7_a_category_usage/README.md) | "State usage" | `annotations.csv` (119 B); `state_usage_lines.csv` (534 B); `state_usage_points.csv` (916.2 KB) | 916.9 KB |
| b | [`figS7_b_pca_variance`](figS7/figS7_b_pca_variance/README.md) | "PCA across sessions" | `annotations.csv` (123 B); `pca_across_sessions_bars.csv` (655 B); `pca_across_sessions_lines.csv` (73 B) | 851 B |
| c | [`figS7_c_pca_by_category`](figS7/figS7_c_pca_by_category/README.md) | "Behavioral distribution" | `active_lines.csv` (316 B); `active_points.csv` (191.1 KB); `alone_lines.csv` (316 B); `alone_points.csv` (191.6 KB); `annotations.csv` (249 B); `climbing_lines.csv` (316 B); `climbing_points.csv` (193.1 KB); `social_lines.csv` (316 B); `social_points.csv` (191.2 KB) | 768.5 KB |

### Figure S8 (`figS8/`, 24.1 MB)

| Panel | Folder | Title | Files | Size |
|---|---|---|---|---|
| a | [`figS8_a_raw_waveforms`](figS8/figS8_a_raw_waveforms/README.md) | "Raw microphone data" | `annotations.csv` (233 B); `mic_1_boxes.csv` (86 B); `mic_1_shapes.csv` (180.3 KB); `mic_2_boxes.csv` (237 B); `mic_2_shapes.csv` (182.2 KB); `mic_3_boxes.csv` (360 B); `mic_3_shapes.csv` (179.1 KB); `mic_4_boxes.csv` (87 B); `mic_4_shapes.csv` (179.9 KB); `raw_microphone_data_1_boxes.csv` (116 B); `raw_microphone_data_2_boxes.csv` (271 B); `raw_microphone_data_3_boxes.csv` (398 B); `raw_microphone_data_4_boxes.csv` (147 B) | 723.3 KB |
| b | [`figS8_b_mic_amplitudes`](figS8/figS8_b_mic_amplitudes/README.md) | "Example amplitudes" | `annotations.csv` (241 B); `example_amplitudes_1_boxes.csv` (116 B); `example_amplitudes_2_boxes.csv` (271 B); `example_amplitudes_3_boxes.csv` (398 B); `example_amplitudes_4_boxes.csv` (147 B); `mic_1_boxes.csv` (82 B); `mic_1_lines.csv` (227.5 KB); `mic_1_shapes.csv` (464.3 KB); `mic_2_boxes.csv` (217 B); `mic_2_lines.csv` (229.9 KB); `mic_2_shapes.csv` (466.6 KB); `mic_3_boxes.csv` (324 B); `mic_3_lines.csv` (224.8 KB); `mic_3_shapes.csv` (461.6 KB); `mic_4_boxes.csv` (83 B); `mic_4_lines.csv` (225.9 KB); `mic_4_shapes.csv` (462.7 KB) | 2.8 MB |
| c | [`figS8_c_mic_spectrograms`](figS8/figS8_c_mic_spectrograms/README.md) | "Example spectrograms" | `annotations.csv` (390 B); `example_spectrograms_time_seconds_boxes.csv` (116 B); `frequency_khz_vs_time_seconds_1_boxes.csv` (269 B); `frequency_khz_vs_time_seconds_2_boxes.csv` (396 B); `frequency_khz_vs_time_seconds_3_boxes.csv` (145 B); `mic_1_boxes.csv` (86 B); `mic_1_colour_key.csv` (4.5 KB); `mic_1_map.csv` (3.3 MB); `mic_2_boxes.csv` (235 B); `mic_2_colour_key.csv` (4.5 KB); `mic_2_map.csv` (3.3 MB); `mic_3_boxes.csv` (358 B); `mic_3_colour_key.csv` (4.5 KB); `mic_3_map.csv` (3.3 MB); `mic_4_boxes.csv` (87 B); `mic_4_colour_key.csv` (4.5 KB); `mic_4_map.csv` (3.3 MB); `time_seconds_boxes.csv` (281 B) | 13.2 MB |
| d | [`figS8_d_call_examples`](figS8/figS8_d_call_examples/README.md) | "Individual call examples" | `annotations.csv` (269 B); `example_1_1_boxes.csv` (79 B); `example_1_2_lines.csv` (78 B); `example_1_2_map.csv` (450.6 KB); `example_1_3_boxes.csv` (107 B); `example_1_4_lines.csv` (92 B); `example_1_4_map.csv` (467.6 KB); `example_1_5_boxes.csv` (107 B); `example_1_6_lines.csv` (92 B); `example_1_6_map.csv` (466.5 KB); `example_1_7_boxes.csv` (79 B); `example_1_8_lines.csv` (78 B); `example_1_8_map.csv` (462.8 KB); `example_2_1_boxes.csv` (81 B); `example_2_2_lines.csv` (82 B); `example_2_2_map.csv` (458.1 KB); `example_2_3_boxes.csv` (81 B); `example_2_4_lines.csv` (82 B); `example_2_4_map.csv` (457.5 KB); `example_2_5_boxes.csv` (81 B); `example_2_6_lines.csv` (82 B); `example_2_6_map.csv` (464.0 KB); `example_2_7_boxes.csv` (81 B); `example_2_8_lines.csv` (82 B); `example_2_8_map.csv` (462.7 KB); `example_3_1_boxes.csv` (79 B); `example_3_2_lines.csv` (78 B); `example_3_2_map.csv` (460.6 KB); `example_3_3_boxes.csv` (79 B); `example_3_4_lines.csv` (78 B); `example_3_4_map.csv` (461.3 KB); `example_3_5_boxes.csv` (79 B); `example_3_6_lines.csv` (78 B); `example_3_6_map.csv` (457.9 KB); `example_3_7_boxes.csv` (79 B); `example_3_8_lines.csv` (78 B); `example_3_8_map.csv` (461.9 KB); `example_4_1_boxes.csv` (81 B); `example_4_2_lines.csv` (82 B); `example_4_2_map.csv` (461.7 KB); `example_4_3_boxes.csv` (81 B); `example_4_4_lines.csv` (82 B); `example_4_4_map.csv` (468.9 KB); `example_4_5_boxes.csv` (81 B); `example_4_6_lines.csv` (82 B); `example_4_6_map.csv` (468.2 KB); `example_4_7_boxes.csv` (81 B); `example_4_8_lines.csv` (82 B); `example_4_8_map.csv` (447.6 KB) | 7.4 MB |

### Figure S9 (`figS9/`, 4.3 MB)

| Panel | Folder | Title | Files | Size |
|---|---|---|---|---|
| a | [`figS9_a_classifier_design`](figS9/figS9_a_classifier_design/README.md) | "Microphone data", "Spectrogram", "RNN", "Dense", "Softmax" | `annotations.csv` (851 B); `microphone_data_1_lines.csv` (146 B); `microphone_data_1_map.csv` (244.8 KB); `microphone_data_2_colour_key.csv` (4.8 KB); `microphone_data_2_lines.csv` (146 B); `microphone_data_2_map.csv` (244.9 KB); `microphone_data_3_lines.csv` (146 B); `microphone_data_3_map.csv` (244.9 KB); `microphone_data_4_lines.csv` (146 B); `microphone_data_4_map.csv` (244.9 KB); `schematic_boxes.csv` (50 B); `schematic_lines.csv` (1.3 KB); `schematic_shapes.csv` (49.9 KB) | 1.0 MB |
| b | `figS9_b_spectral_profiles` | "Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6", "Class 7", "Class 8" | artwork pasted in Illustrator; not drawn by code | |
| c | `figS9_c_call_type_examples` | "Class 1", "Class 5", "Class 2", "Class 6", "Class 3", "Class 7", "Class 4", "Class 8" | artwork pasted in Illustrator; not drawn by code | |
| artwork | [`figS9_artwork`](figS9/figS9_artwork/README.md) | the page's artwork, drawn over its panels | `artwork.png` (3.3 MB) | 3.3 MB |

### Figure S10 (`figS10/`, 227.6 KB)

| Panel | Folder | Title | Files | Size |
|---|---|---|---|---|
| a | [`figS10_a_homecage_call_rate`](figS10/figS10_a_homecage_call_rate/README.md) | "Family-housed animals" | `annotations.csv` (134 B); `family_housed_animals_bars.csv` (791 B); `family_housed_animals_lines.csv` (62 B) | 987 B |
| b | [`figS10_b_homecage_loud_cage`](figS10/figS10_b_homecage_loud_cage/README.md) | "Cage space" | `annotations.csv` (67 B); `cage_space_map.csv` (13.0 KB) | 13.0 KB |
| c | [`figS10_c_homecage_loud_tsne`](figS10/figS10_c_homecage_loud_tsne/README.md) | "Behavioral space" | `annotations.csv` (73 B); `behavioral_space_map.csv` (15.1 KB) | 15.1 KB |
| d | [`figS10_d_homecage_mean_corr`](figS10/figS10_d_homecage_mean_corr/README.md) | (no title printed) | `mean_rho_across_animals_vs_level_5_behavioral_state_bars.csv` (2.4 KB); `mean_rho_across_animals_vs_level_5_behavioral_state_lines.csv` (78 B) | 2.5 KB |
| e | [`figS10_e_homecage_category_corr`](figS10/figS10_e_homecage_category_corr/README.md) | (no title printed) | `annotations.csv` (99 B); `spearman_rho_vs_call_rate_lines.csv` (421 B); `spearman_rho_vs_call_rate_points.csv` (15.6 KB) | 16.1 KB |
| f | [`figS10_f_homecage_animal_corr`](figS10/figS10_f_homecage_animal_corr/README.md) | (no title printed) | `animal_vs_level_5_behavioral_state_map.csv` (71.7 KB) | 71.7 KB |
| g | [`figS10_g_pair_call_rate`](figS10/figS10_g_pair_call_rate/README.md) | "Paired animals (2 per cage)" | `annotations.csv` (147 B); `paired_animals_2_per_cage_bars.csv` (696 B); `paired_animals_2_per_cage_lines.csv` (63 B) | 906 B |
| h | [`figS10_h_pair_loud_cage`](figS10/figS10_h_pair_loud_cage/README.md) | "Cage space" | `annotations.csv` (67 B); `cage_space_map.csv` (13.9 KB) | 14.0 KB |
| i | [`figS10_i_pair_loud_tsne`](figS10/figS10_i_pair_loud_tsne/README.md) | "Behavioral space" | `annotations.csv` (73 B); `behavioral_space_map.csv` (12.8 KB) | 12.9 KB |
| j | [`figS10_j_pair_mean_corr`](figS10/figS10_j_pair_mean_corr/README.md) | (no title printed) | `mean_rho_across_animals_vs_level_5_behavioral_state_bars.csv` (2.4 KB); `mean_rho_across_animals_vs_level_5_behavioral_state_lines.csv` (78 B) | 2.5 KB |
| k | [`figS10_k_pair_category_corr`](figS10/figS10_k_pair_category_corr/README.md) | (no title printed) | `annotations.csv` (99 B); `spearman_rho_vs_call_rate_lines.csv` (418 B); `spearman_rho_vs_call_rate_points.csv` (13.7 KB) | 14.2 KB |
| l | [`figS10_l_pair_animal_corr`](figS10/figS10_l_pair_animal_corr/README.md) | (no title printed) | `animal_vs_level_5_behavioral_state_map.csv` (63.6 KB) | 63.6 KB |

### Figure S11 (`figS11/`, 1.1 MB)

| Panel | Folder | Title | Files | Size |
|---|---|---|---|---|
| a | [`figS11_a_recording_schedule`](figS11/figS11_a_recording_schedule/README.md) | "Recording schedule" | `annotations.csv` (1.6 KB); `recording_schedule_lines.csv` (771 B); `recording_schedule_shapes.csv` (97.7 KB) | 100.0 KB |
| b | [`figS11_b_state_vs_tablet`](figS11/figS11_b_state_vs_tablet/README.md) | "Correlations (example animal)" | `annotations.csv` (267 B); `state_36_x_tablet_lines.csv` (77 B); `state_36_x_tablet_points.csv` (1.5 KB); `state_8_x_tablet_lines.csv` (75 B); `state_8_x_tablet_points.csv` (1.6 KB) | 3.5 KB |
| c | [`figS11_c_category_response_maps`](figS11/figS11_c_category_response_maps/README.md) | "Box", "Face", "Intruder", "Mask", "Treat", "Toys", "Noise", "Object" | `annotations.csv` (900 B); `box_active_map.csv` (24.9 KB); `box_alone_map.csv` (25.1 KB); `box_climbing_map.csv` (24.8 KB); `box_soc_act_map.csv` (24.9 KB); `box_soc_rest_map.csv` (25.0 KB); `face_active_map.csv` (25.0 KB); `face_alone_map.csv` (24.6 KB); `face_climbing_map.csv` (24.8 KB); `face_soc_act_map.csv` (24.8 KB); `face_soc_rest_map.csv` (24.7 KB); `intruder_active_map.csv` (24.7 KB); `intruder_alone_map.csv` (24.9 KB); `intruder_climbing_map.csv` (24.8 KB); `intruder_soc_act_map.csv` (24.8 KB); `intruder_soc_rest_map.csv` (24.9 KB); `mask_active_map.csv` (24.4 KB); `mask_alone_map.csv` (24.7 KB); `mask_climbing_map.csv` (24.7 KB); `mask_soc_act_map.csv` (24.5 KB); `mask_soc_rest_map.csv` (24.5 KB); `noise_active_map.csv` (24.5 KB); `noise_alone_map.csv` (24.5 KB); `noise_climbing_map.csv` (24.1 KB); `noise_soc_act_map.csv` (24.6 KB); `noise_soc_rest_map.csv` (24.5 KB); `object_active_map.csv` (24.4 KB); `object_alone_map.csv` (24.5 KB); `object_climbing_map.csv` (24.4 KB); `object_soc_act_map.csv` (24.6 KB); `object_soc_rest_map.csv` (24.5 KB); `toys_active_map.csv` (24.3 KB); `toys_alone_map.csv` (24.6 KB); `toys_climbing_map.csv` (24.0 KB); `toys_soc_act_map.csv` (24.8 KB); `toys_soc_rest_map.csv` (24.8 KB); `treat_active_map.csv` (24.7 KB); `treat_alone_map.csv` (24.7 KB); `treat_climbing_map.csv` (24.4 KB); `treat_soc_act_map.csv` (24.9 KB); `treat_soc_rest_map.csv` (24.8 KB) | 987.1 KB |

### Figure S12 (`figS12/`, 531.2 KB)

| Panel | Folder | Title | Files | Size |
|---|---|---|---|---|
| a | [`figS12_a_example_tablet`](figS12/figS12_a_example_tablet/README.md) | "Example animal: tablet (n = 2 sessions)" | `active_map.csv` (22.0 KB); `alone_map.csv` (16.9 KB); `annotations.csv` (267 B); `climb_map.csv` (22.0 KB); `soc_act_map.csv` (14.0 KB); `soc_rest_map.csv` (12.3 KB) | 87.6 KB |
| b | [`figS12_b_example_control`](figS12/figS12_b_example_control/README.md) | "Example animal: control (n = 9 sessions)" | `active_map.csv` (23.5 KB); `alone_map.csv` (20.9 KB); `annotations.csv` (97 B); `climb_map.csv` (23.7 KB); `soc_act_map.csv` (19.4 KB); `soc_rest_map.csv` (17.4 KB) | 105.0 KB |
| c | [`figS12_c_example_response`](figS12/figS12_c_example_response/README.md) | "Example animal: tablet - control" | `active_map.csv` (24.7 KB); `alone_map.csv` (22.0 KB); `annotations.csv` (89 B); `climb_map.csv` (24.6 KB); `soc_act_map.csv` (20.6 KB); `soc_rest_map.csv` (18.3 KB) | 110.2 KB |
| d | [`figS12_d_colony_response`](figS12/figS12_d_colony_response/README.md) | "Colony average: tablet - control" | `active_map.csv` (24.9 KB); `alone_map.csv` (25.1 KB); `annotations.csv` (89 B); `climb_map.csv` (24.9 KB); `soc_act_map.csv` (24.9 KB); `soc_rest_map.csv` (25.0 KB) | 124.8 KB |
| e | [`figS12_e_projection_schematic`](figS12/figS12_e_projection_schematic/README.md) | "Projection: response × template" | `annotations.csv` (400 B); `held_out_control_baseline_map.csv` (24.7 KB); `response_c_map.csv` (24.5 KB); `template_d_1_map.csv` (23.6 KB); `template_d_2_map.csv` (23.6 KB) | 96.7 KB |
| f | [`figS12_f_projection_vs_control`](figS12/figS12_f_projection_vs_control/README.md) | (no title printed) | `annotations.csv` (130 B); `projection_on_the_lines.csv` (275 B); `projection_on_the_points.csv` (6.5 KB) | 6.9 KB |

### Figure S13 (`figS13/`, 1.3 MB)

| Panel | Folder | Title | Files | Size |
|---|---|---|---|---|
| a | [`figS13_a_cage_occupancy`](figS13/figS13_a_cage_occupancy/README.md) | "Cage space" | `annotations.csv` (692 B); `control_control_day_1_lines.csv` (8.2 KB); `control_control_day_1_points.csv` (7.9 KB); `control_intruder_lines.csv` (7.6 KB); `control_intruder_points.csv` (7.2 KB); `control_map.csv` (45.0 KB); `control_mask_lines.csv` (7.2 KB); `control_mask_points.csv` (6.9 KB); `control_noise_lines.csv` (7.3 KB); `control_noise_points.csv` (7.0 KB); `control_object_lines.csv` (7.3 KB); `control_object_points.csv` (6.9 KB); `control_points.csv` (25 B); `control_tablet_lines.csv` (5.6 KB); `control_tablet_points.csv` (5.3 KB); `control_toys_lines.csv` (6.6 KB); `control_toys_points.csv` (6.3 KB); `control_treat_lines.csv` (7.2 KB); `control_treat_points.csv` (6.9 KB); `intruder_map.csv` (43.3 KB); `intruder_points.csv` (24 B); `mask_map.csv` (45.3 KB); `mask_points.csv` (26 B); `noise_map.csv` (43.9 KB); `noise_points.csv` (25 B); `object_map.csv` (43.9 KB); `object_points.csv` (25 B); `page_shapes.csv` (63 B); `tablet_map.csv` (43.1 KB); `tablet_points.csv` (26 B); `toys_map.csv` (44.8 KB); `toys_points.csv` (25 B); `treat_map.csv` (43.8 KB); `treat_points.csv` (25 B) | 465.6 KB |
| b | [`figS13_b_embedding_density`](figS13/figS13_b_embedding_density/README.md) | "Behavioral embedding space" | `annotations.csv` (720 B); `control_control_day_1_lines.csv` (8.3 KB); `control_control_day_1_points.csv` (8.0 KB); `control_intruder_lines.csv` (7.6 KB); `control_intruder_points.csv` (7.3 KB); `control_map.csv` (85.4 KB); `control_mask_lines.csv` (7.4 KB); `control_mask_points.csv` (7.0 KB); `control_noise_lines.csv` (7.4 KB); `control_noise_points.csv` (7.1 KB); `control_object_lines.csv` (7.3 KB); `control_object_points.csv` (7.0 KB); `control_tablet_lines.csv` (5.8 KB); `control_tablet_points.csv` (5.5 KB); `control_toys_lines.csv` (6.6 KB); `control_toys_points.csv` (6.3 KB); `control_treat_lines.csv` (7.3 KB); `control_treat_points.csv` (7.0 KB); `intruder_map.csv` (84.9 KB); `mask_map.csv` (84.3 KB); `noise_map.csv` (84.6 KB); `object_map.csv` (85.0 KB); `page_shapes.csv` (69 B); `tablet_map.csv` (84.8 KB); `toys_map.csv` (85.0 KB); `treat_map.csv` (84.9 KB) | 792.6 KB |

### Figure S14 (`figS14/`, 945.9 KB)

| Panel | Folder | Title | Files | Size |
|---|---|---|---|---|
| a | [`figS14_a_climbing_time`](figS14/figS14_a_climbing_time/README.md) | "Time spent climbing" | `annotations.csv` (618 B); `climb_wedges.csv` (148 B); `juvenile_adult_lines.csv` (232 B); `juvenile_adult_points.csv` (181.5 KB); `juvenile_time_climbing_vs_adult_time_climbing_lines.csv` (100 B); `juvenile_time_climbing_vs_adult_time_climbing_points.csv` (38.2 KB); `juvenile_time_climbing_vs_adult_time_climbing_shapes.csv` (360 B); `page_shapes.csv` (111 B) | 221.3 KB |
| b | [`figS14_b_active_time`](figS14/figS14_b_active_time/README.md) | "Time spent active" | `active_wedges.csv` (148 B); `annotations.csv` (636 B); `juvenile_adult_lines.csv` (229 B); `juvenile_adult_points.csv` (179.9 KB); `juvenile_time_active_vs_adult_time_active_lines.csv` (96 B); `juvenile_time_active_vs_adult_time_active_points.csv` (36.8 KB); `juvenile_time_active_vs_adult_time_active_shapes.csv` (356 B); `page_shapes.csv` (111 B) | 218.2 KB |
| c | [`figS14_c_social_time`](figS14/figS14_c_social_time/README.md) | "Time spent social" | `annotations.csv` (575 B); `juvenile_adult_lines.csv` (229 B); `juvenile_adult_points.csv` (180.1 KB); `juvenile_time_social_vs_adult_time_social_lines.csv` (94 B); `juvenile_time_social_vs_adult_time_social_points.csv` (36.8 KB); `juvenile_time_social_vs_adult_time_social_shapes.csv` (350 B); `page_shapes.csv` (111 B); `social_wedges.csv` (148 B) | 218.4 KB |
| d | [`figS14_d_alone_time`](figS14/figS14_d_alone_time/README.md) | "Time spent alone" | `alone_wedges.csv` (148 B); `annotations.csv` (624 B); `juvenile_adult_lines.csv` (228 B); `juvenile_adult_points.csv` (180.4 KB); `juvenile_time_alone_vs_adult_time_alone_lines.csv` (94 B); `juvenile_time_alone_vs_adult_time_alone_points.csv` (37.0 KB); `juvenile_time_alone_vs_adult_time_alone_shapes.csv` (354 B); `page_shapes.csv` (111 B) | 219.0 KB |
| e | [`figS14_e_usage_difference`](figS14/figS14_e_usage_difference/README.md) | "Hierarchical representation", "Difference in usage" | `annotations.csv` (372 B); `difference_in_usage_points.csv` (4.1 KB); `hierarchical_representation_colour_key.csv` (4.8 KB); `hierarchical_representation_shapes.csv` (50.2 KB); `hierarchical_representation_wedges.csv` (6.3 KB) | 65.8 KB |
| f | [`figS14_f_state_difference`](figS14/figS14_f_state_difference/README.md) | (no title printed) | `annotations.csv` (351 B); `relative_difference_vs_behavioral_state_bars.csv` (2.9 KB); `relative_difference_vs_behavioral_state_lines.csv` (80 B) | 3.3 KB |
