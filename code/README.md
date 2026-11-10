# Code for the paper's figures

Standalone scripts that redraw the paper's figure panels from the source data in [`data/`](../data/README.md), with numpy and matplotlib alone.

## Usage

```bash
pip install -r code/requirements.txt
python code/render_all.py                 # every figure
python code/render_all.py fig1 figS3      # or a subset
python code/render_all.py --list          # list panels without rendering
```

Each panel script writes the panel, cut from its page, to `figures/<fig>/<panel id>.pdf` and `.png` for a main figure and to `supplemental_figures/<fig>/<panel id>.pdf` and `.png` for a supplementary one; each page script writes the whole page to `figures/<fig>.pdf` and `.png` (`supplemental_figures/<fig>.pdf` and `.png`). Paths are from the repository's root; PNGs are at 400 dpi, and a PDF keeps its text as TrueType text. Scripts can also be run one at a time:

```bash
python code/fig1/fig1_b_label_timeseries.py        # one panel
python code/fig1/fig1_page.py                       # one page
```

Both take `--data DIR` to read the data from somewhere else and `--out-dir DIR` to write somewhere else. `render_all.py` runs the scripts in one process and imports nothing but the standard library, numpy and matplotlib.

## Layout

```
code/
  README.md               this file
  LICENSE                 MIT
  requirements.txt        numpy, matplotlib (tested versions)
  render_all.py           everything, a subset (fig1 figS3), --list
  fig1/ ... fig8/         the main figures
  figS1/ ... figS14/      the supplementary figures
    <panel id>.py         standalone redraw of one panel
    <fig>_page.py         the whole page, from its panel scripts
data/                     the source data, one folder per panel (CC BY 4.0)
figures/                  what the main figures' scripts write
  <fig>/<panel id>.pdf, .png
  <fig>.pdf, .png
supplemental_figures/     the same, for the supplementary figures
```

A panel id is `<fig>_<letter>_<slug>`: the figure folder, the panel's letter as printed, and a short name for what the panel shows, e.g. `fig1_b_label_timeseries`. The figure folders are `fig1`, `fig2`, `fig3`, `fig4`, `fig5`, `fig6`, `fig7`, `fig8` for Figures 1-8 and `figS1`, `figS2`, `figS3`, `figS4`, `figS5`, `figS6`, `figS7`, `figS8`, `figS9`, `figS10`, `figS11`, `figS12`, `figS13`, `figS14` for Figures S1-S14.

## Data

Every panel script names the folder it reads from explicitly, as a `DATA` constant near the top of the script:

```python
DATA = os.path.join(HERE, "..", "..", "data", "fig1", "fig1_b_label_timeseries")
```

Nothing is resolved by name or searched for at run time: the path in the script is the path that is opened, and a script reads nothing outside its own data folder. A file missing from that folder stops the script with an error (`render_all.py` reports it as `FAIL`). What each file holds, its columns and units are in [`data/README.md`](../data/README.md) and in the README of each panel's data folder.

The data folders hold what a panel draws, not how the page is laid out, so each script carries its own layout as literals: the axes' rectangles in page inches, limits, scales, ticks, labels, titles, legends, colour maps and their limits, the drawing styles, the house type (Arial; letters 12 pt bold, titles 8, labels and ticks 7, legends 6), and the decoration the data leave out by design -- cage wireframes, category outlines, category boundaries.

## Panels

112 panels on 22 pages: 107 redrawn by a script here, 5 pasted in as artwork. A panel drawn by code with some artwork pasted beside it says so in its script's docstring. A page with artwork draws it over its panels, from one transparent image of the whole page in `data/<fig>/<fig>_artwork/`, so the rendered page is complete.

### Figure 1 (`fig1/`)

| Panel | Description | Script |
|---|---|---|
| a | the cage and camera, and the tracker's label accuracy | `fig1_a_homecage_video`: artwork pasted in Illustrator; not drawn by code |
| b | every keypoint against time, in 3-D | [`fig1_b_label_timeseries.py`](fig1/fig1_b_label_timeseries.py) |
| c | a labelled frame of all four animals | [`fig1_c_labeled_image.py`](fig1/fig1_c_labeled_image.py) |
| d | each animal's path, sorted by identity | [`fig1_d_paths_by_id.py`](fig1/fig1_d_paths_by_id.py) |
| e | six calm minutes of one animal's raw keypoints, and their PCA | [`fig1_e_raw_pca.py`](fig1/fig1_e_raw_pca.py) |
| f | the same after the egocentric transform, and its PCA | [`fig1_f_egocentric_pca.py`](fig1/fig1_f_egocentric_pca.py) |

Page: [`fig1_page.py`](fig1/fig1_page.py).

### Figure 2 (`fig2/`)

| Panel | Description | Script |
|---|---|---|
| a | the 80 clusters on t-SNE, area by usage | [`fig2_a_state_usage_tsne.py`](fig2/fig2_a_state_usage_tsne.py) |
| b | an hour of one animal, each sample at its state | [`fig2_b_state_raster.py`](fig2/fig2_b_state_raster.py) |
| c | the model schematic (hand-drawn) | `fig2_c_model_schematic`: artwork pasted in Illustrator; not drawn by code |
| d | where each category happens, and all of them on one map | [`fig2_d_category_maps.py`](fig2/fig2_d_category_maps.py) |
| e | usage of each of the 80 states | [`fig2_e_state_usage.py`](fig2/fig2_e_state_usage.py) |
| f | the embedding at three levels | [`fig2_f_cluster_levels.py`](fig2/fig2_f_cluster_levels.py) |
| g | how long a bout lasts at each level | [`fig2_g_bout_duration.py`](fig2/fig2_g_bout_duration.py) |

Page: [`fig2_page.py`](fig2/fig2_page.py).

### Figure 3 (`fig3/`)

| Panel | Description | Script |
|---|---|---|
| a | two cagemates' categories over one session | [`fig3_a_category_rasters.py`](fig3/fig3_a_category_rasters.py) |
| b | two cagemates on four days, in t-SNE | [`fig3_b_tsne_by_day.py`](fig3/fig3_b_tsne_by_day.py) |
| c | one animal's category shares by session, sorted by PC1 | [`fig3_c_animal_session_shares.py`](fig3/fig3_c_animal_session_shares.py) |
| d | every session's category shares, sorted by PC1 | [`fig3_d_all_session_shares.py`](fig3/fig3_d_all_session_shares.py) |
| e | cagemates move together: three views per category, and every endpoint at once | [`fig3_e_cagemate_correlation.py`](fig3/fig3_e_cagemate_correlation.py) |

Page: [`fig3_page.py`](fig3/fig3_page.py).

### Figure 4 (`fig4/`)

| Panel | Description | Script |
|---|---|---|
| a | four microphones: recording layout, amplitude and spectrograms | [`fig4_a_mic_recording.py`](fig4/fig4_a_mic_recording.py) |
| b | spectrogram frames the call detector scored without and with calls | [`fig4_b_call_detection.py`](fig4/fig4_b_call_detection.py) |
| c | time near the other animal per clip | [`fig4_c_time_near_other.py`](fig4/fig4_c_time_near_other.py) |
| d | calls per minute per clip, on c's count axis | [`fig4_d_calls_per_minute.py`](fig4/fig4_d_calls_per_minute.py) |
| e | one animal's clips in the order recorded, each measure on its own axes, its high clips shaded | [`fig4_e_clip_sequence.py`](fig4/fig4_e_clip_sequence.py) |
| f | one animal's call rate against each category's share of a clip | [`fig4_f_call_rate_vs_category.py`](fig4/fig4_f_call_rate_vs_category.py) |
| g | every animal's correlation per category | [`fig4_g_category_corr.py`](fig4/fig4_g_category_corr.py) |
| h | where the animals sit when the room is loud, in the cage | [`fig4_h_loud_cage_map.py`](fig4/fig4_h_loud_cage_map.py) |
| i | the same in behavioral space | [`fig4_i_loud_tsne_map.py`](fig4/fig4_i_loud_tsne_map.py) |
| j | the animals' mean correlation per state | [`fig4_j_mean_state_corr.py`](fig4/fig4_j_mean_state_corr.py) |
| k | each animal's correlation per state | [`fig4_k_animal_state_corr.py`](fig4/fig4_k_animal_state_corr.py) |

Page: [`fig4_page.py`](fig4/fig4_page.py).

### Figure 5 (`fig5/`)

| Panel | Description | Script |
|---|---|---|
| a | one animal's state usage in each session, on the t-SNE plane | [`fig5_a_session_tsne.py`](fig5/fig5_a_session_tsne.py) |
| b | the same sessions as rasters, by category and the box zone | [`fig5_b_category_rasters.py`](fig5/fig5_b_category_rasters.py) |
| c | every state's mean usage, control and tablet | [`fig5_c_state_usage.py`](fig5/fig5_c_state_usage.py) |
| d | one state's usage per animal, every state's mean, and the discriminability score | [`fig5_d_usage_discriminability.py`](fig5/fig5_d_usage_discriminability.py) |
| e | every state's correlation with time near the tablet | [`fig5_e_state_corr.py`](fig5/fig5_e_state_corr.py) |
| f | d's three views, for the correlations | [`fig5_f_corr_discriminability.py`](fig5/fig5_f_corr_discriminability.py) |

Page: [`fig5_page.py`](fig5/fig5_page.py).

### Figure 6 (`fig6/`)

| Panel | Description | Script |
|---|---|---|
| a | per stimulus, where occupancy moves from control, in the cage and in behavioral space | [`fig6_a_response_maps.py`](fig6/fig6_a_response_maps.py) |
| b | every animal's projection on the group response, per stimulus | [`fig6_b_group_projection.py`](fig6/fig6_b_group_projection.py) |
| c | AUROC against a held-out control per stimulus, with the null | [`fig6_c_stimulus_auroc.py`](fig6/fig6_c_stimulus_auroc.py) |
| d | every animal's projection, held-out control against stimulus | [`fig6_d_heldout_projection.py`](fig6/fig6_d_heldout_projection.py) |
| e | every session type against every other | [`fig6_e_pairwise_auroc.py`](fig6/fig6_e_pairwise_auroc.py) |

Page: [`fig6_page.py`](fig6/fig6_page.py).

### Figure 7 (`fig7/`)

| Panel | Description | Script |
|---|---|---|
| a | the recording split (alternating, early vs late) and the cage locations enriched in each group, each map marking where its stimulus stands | [`fig7_a_split_cage_enrichment.py`](fig7/fig7_a_split_cage_enrichment.py) |
| b | each animal's first half against every animal's second (alternating split), and where its halves are grouped | [`fig7_b_alternating_halves.py`](fig7/fig7_b_alternating_halves.py) |
| c | the same for the early-vs-late split | [`fig7_c_early_late_halves.py`](fig7/fig7_c_early_late_halves.py) |
| d | group 1's composite, half 1 against half 2, and its features, by their correlation with the others | [`fig7_d_group_1_composite.py`](fig7/fig7_d_group_1_composite.py) |
| e | the same for group 2 | [`fig7_e_group_2_composite.py`](fig7/fig7_e_group_2_composite.py) |
| f | the same for group 3 | [`fig7_f_group_3_composite.py`](fig7/fig7_f_group_3_composite.py) |
| g | the three composites as one space, each animal's mean of halves | [`fig7_g_composite_means.py`](fig7/fig7_g_composite_means.py) |
| h | the same space, each animal's half 1 joined to its half 2 | [`fig7_h_composite_halves.py`](fig7/fig7_h_composite_halves.py) |
| i | adults and juveniles in each group | [`fig7_i_age_by_group.py`](fig7/fig7_i_age_by_group.py) |

Page: [`fig7_page.py`](fig7/fig7_page.py).

### Figure 8 (`fig8/`)

| Panel | Description | Script |
|---|---|---|
| a | every household's cagemates in their groups: one block per cage's parents and one per cage's juveniles | [`fig8_a_household_groups.py`](fig8/fig8_a_household_groups.py) |
| b | by pair type, the share of pairs in the same group, against chance and its shuffle band | [`fig8_b_same_group_pairs.py`](fig8/fig8_b_same_group_pairs.py) |
| c | which baseline dimensions are linked to which stimulus dimensions (true-score r of at least .4 in size) | [`fig8_c_dimension_links.py`](fig8/fig8_c_dimension_links.py) |
| d | the share of each response's reliable variance that all baseline features predict, in an unseen household | [`fig8_d_predicted_variance.py`](fig8/fig8_d_predicted_variance.py) |
| e | a positive correlation: one half's B1 score against the other half's treat approach | [`fig8_e_positive_correlation.py`](fig8/fig8_e_positive_correlation.py) |
| f | a negative correlation: one half's B1 score against the other half's mask reaction | [`fig8_f_negative_correlation.py`](fig8/fig8_f_negative_correlation.py) |
| g | no correlation: the prediction from all baseline features, in an unseen household, against the other half's approach to the tablets | [`fig8_g_no_correlation.py`](fig8/fig8_g_no_correlation.py) |

Page: [`fig8_page.py`](fig8/fig8_page.py).

### Figure S1 (`figS1/`)

| Panel | Description | Script |
|---|---|---|
| a | the first four components of the raw data, over an hour | [`figS1_a_raw_components.py`](figS1/figS1_a_raw_components.py) |
| b | the first four components of the egocentric data, over an hour | [`figS1_b_egocentric_components.py`](figS1/figS1_b_egocentric_components.py) |

Page: [`figS1_page.py`](figS1/figS1_page.py).

### Figure S2 (`figS2/`)

| Panel | Description | Script |
|---|---|---|
| a | the camera array and the three methods (hand-drawn) | `figS2_a_depth_methods`: artwork pasted in Illustrator; not drawn by code |
| b | single view: head radius, climbing-state frames against the rest | [`figS2_b_single_view.py`](figS2/figS2_b_single_view.py) |
| c | the single view over a 30-minute window of one animal | [`figS2_c_single_view_trace.py`](figS2/figS2_c_single_view_trace.py) |
| d | stereo vision: head depth for the same frames | [`figS2_d_stereo_view.py`](figS2/figS2_d_stereo_view.py) |
| e | the stereo view over the same window | [`figS2_e_stereo_view_trace.py`](figS2/figS2_e_stereo_view_trace.py) |
| f | mesh grid: sorted depths per class | [`figS2_f_mesh_grid.py`](figS2/figS2_f_mesh_grid.py) |
| g | the mesh grid over the same window | [`figS2_g_mesh_grid_trace.py`](figS2/figS2_g_mesh_grid_trace.py) |
| h | one session's head positions, as recorded and depth-corrected | [`figS2_h_depth_correction.py`](figS2/figS2_h_depth_correction.py) |

Page: [`figS2_page.py`](figS2/figS2_page.py).

### Figure S3 (`figS3/`)

| Panel | Description | Script |
|---|---|---|
| a | usage flowing down the hierarchy's levels | [`figS3_a_hierarchy_flow.py`](figS3/figS3_a_hierarchy_flow.py) |
| b | the same hierarchy at three levels, over each state's usage | [`figS3_b_hierarchy_usage.py`](figS3/figS3_b_hierarchy_usage.py) |

Page: [`figS3_page.py`](figS3/figS3_page.py).

### Figure S4 (`figS4/`)

| Panel | Description | Script |
|---|---|---|
| a | fifteen descriptions' share of each cluster's frames, at five levels | [`figS4_a_description_levels.py`](figS4/figS4_a_description_levels.py) |
| b | the same at level 5, 1, 10 and 60 s before the labelled frame | [`figS4_b_description_lags.py`](figS4/figS4_b_description_lags.py) |

Page: [`figS4_page.py`](figS4/figS4_page.py).

### Figure S5 (`figS5/`)

| Panel | Description | Script |
|---|---|---|
| a | one session's transition probabilities, shuffled and observed | [`figS5_a_transition_matrices.py`](figS5/figS5_a_transition_matrices.py) |
| b | entropy rate, the share the order removes, and memory by lag | [`figS5_b_entropy_memory.py`](figS5/figS5_b_entropy_memory.py) |

Page: [`figS5_page.py`](figS5/figS5_page.py).

### Figure S6 (`figS6/`)

| Panel | Description | Script |
|---|---|---|
| a | the 80 states over every recording of one animal, as a flow | [`figS6_a_state_flow.py`](figS6/figS6_a_state_flow.py) |

Page: [`figS6_page.py`](figS6/figS6_page.py).

### Figure S7 (`figS7/`)

| Panel | Description | Script |
|---|---|---|
| a | every session's share of each category | [`figS7_a_category_usage.py`](figS7/figS7_a_category_usage.py) |
| b | the variance each component of the PCA across sessions explains | [`figS7_b_pca_variance.py`](figS7/figS7_b_pca_variance.py) |
| c | every session on PC1 and PC2, coloured by each category's share | [`figS7_c_pca_by_category.py`](figS7/figS7_c_pca_by_category.py) |

Page: [`figS7_page.py`](figS7/figS7_page.py).

### Figure S8 (`figS8/`)

| Panel | Description | Script |
|---|---|---|
| a | 35 s of each microphone's waveform, calls boxed | [`figS8_a_raw_waveforms.py`](figS8/figS8_a_raw_waveforms.py) |
| b | each microphone's amplitude over the same 35 s | [`figS8_b_mic_amplitudes.py`](figS8/figS8_b_mic_amplitudes.py) |
| c | the same 35 s as spectrograms against the four-microphone mean | [`figS8_c_mic_spectrograms.py`](figS8/figS8_c_mic_spectrograms.py) |
| d | four call windows on all four microphones | [`figS8_d_call_examples.py`](figS8/figS8_d_call_examples.py) |

Page: [`figS8_page.py`](figS8/figS8_page.py).

### Figure S9 (`figS9/`)

| Panel | Description | Script |
|---|---|---|
| a | the microphones' spectrograms and the classifier's strategy | [`figS9_a_classifier_design.py`](figS9/figS9_a_classifier_design.py) |
| b | each call class's spectral profile | `figS9_b_spectral_profiles`: artwork pasted in Illustrator; not drawn by code |
| c | 10 s of each call class's calls | `figS9_c_call_type_examples`: artwork pasted in Illustrator; not drawn by code |

Page: [`figS9_page.py`](figS9/figS9_page.py).

### Figure S10 (`figS10/`)

| Panel | Description | Script |
|---|---|---|
| a | home cage: the 5-minute segments' call rates | [`figS10_a_homecage_call_rate.py`](figS10/figS10_a_homecage_call_rate.py) |
| b | home cage: where animals sit when the room is loud, in the cage | [`figS10_b_homecage_loud_cage.py`](figS10/figS10_b_homecage_loud_cage.py) |
| c | home cage: the same in behavioral space | [`figS10_c_homecage_loud_tsne.py`](figS10/figS10_c_homecage_loud_tsne.py) |
| d | home cage: the animals' mean correlation per state | [`figS10_d_homecage_mean_corr.py`](figS10/figS10_d_homecage_mean_corr.py) |
| e | home cage: every animal's correlation per category | [`figS10_e_homecage_category_corr.py`](figS10/figS10_e_homecage_category_corr.py) |
| f | home cage: each animal's correlation per state | [`figS10_f_homecage_animal_corr.py`](figS10/figS10_f_homecage_animal_corr.py) |
| g | pair trials: the 5-minute segments' call rates | [`figS10_g_pair_call_rate.py`](figS10/figS10_g_pair_call_rate.py) |
| h | pair trials: where animals sit when the room is loud, in the cage | [`figS10_h_pair_loud_cage.py`](figS10/figS10_h_pair_loud_cage.py) |
| i | pair trials: the same in behavioral space | [`figS10_i_pair_loud_tsne.py`](figS10/figS10_i_pair_loud_tsne.py) |
| j | pair trials: the animals' mean correlation per state | [`figS10_j_pair_mean_corr.py`](figS10/figS10_j_pair_mean_corr.py) |
| k | pair trials: every animal's correlation per category | [`figS10_k_pair_category_corr.py`](figS10/figS10_k_pair_category_corr.py) |
| l | pair trials: each animal's correlation per state | [`figS10_l_pair_animal_corr.py`](figS10/figS10_l_pair_animal_corr.py) |

Page: [`figS10_page.py`](figS10/figS10_page.py).

### Figure S11 (`figS11/`)

| Panel | Description | Script |
|---|---|---|
| a | the recording schedule | [`figS11_a_recording_schedule.py`](figS11/figS11_a_recording_schedule.py) |
| b | one animal's state usage against time near the tablet, per minute | [`figS11_b_state_vs_tablet.py`](figS11/figS11_b_state_vs_tablet.py) |
| c | each stimulus's response map in every behavioural category | [`figS11_c_category_response_maps.py`](figS11/figS11_c_category_response_maps.py) |

Page: [`figS11_page.py`](figS11/figS11_page.py).

### Figure S12 (`figS12/`)

| Panel | Description | Script |
|---|---|---|
| a | one animal's cell maps under the tablet | [`figS12_a_example_tablet.py`](figS12/figS12_a_example_tablet.py) |
| b | the same animal's control baseline | [`figS12_b_example_control.py`](figS12/figS12_b_example_control.py) |
| c | its response, tablet minus control | [`figS12_c_example_response.py`](figS12/figS12_c_example_response.py) |
| d | the other animals' mean response | [`figS12_d_colony_response.py`](figS12/figS12_d_colony_response.py) |
| e | the projection, as a schematic | [`figS12_e_projection_schematic.py`](figS12/figS12_e_projection_schematic.py) |
| f | every animal's projection against its held-out control | [`figS12_f_projection_vs_control.py`](figS12/figS12_f_projection_vs_control.py) |

Page: [`figS12_page.py`](figS12/figS12_page.py).

### Figure S13 (`figS13/`)

| Panel | Description | Script |
|---|---|---|
| a | per condition: occupancy map, and each animal's time near the stimulus | [`figS13_a_cage_occupancy.py`](figS13/figS13_a_cage_occupancy.py) |
| b | per condition: embedding density, and each animal's time in social rest | [`figS13_b_embedding_density.py`](figS13/figS13_b_embedding_density.py) |

Page: [`figS13_page.py`](figS13/figS13_page.py).

### Figure S14 (`figS14/`)

| Panel | Description | Script |
|---|---|---|
| a | time spent climbing, juvenile against adult | [`figS14_a_climbing_time.py`](figS14/figS14_a_climbing_time.py) |
| b | time spent active, juvenile against adult | [`figS14_b_active_time.py`](figS14/figS14_b_active_time.py) |
| c | time spent social, juvenile against adult | [`figS14_c_social_time.py`](figS14/figS14_c_social_time.py) |
| d | time spent alone, juvenile against adult | [`figS14_d_alone_time.py`](figS14/figS14_d_alone_time.py) |
| e | the relative difference in usage, over the hierarchy and on the t-SNE plane | [`figS14_e_usage_difference.py`](figS14/figS14_e_usage_difference.py) |
| f | the same per level-5 state | [`figS14_f_state_difference.py`](figS14/figS14_f_state_difference.py) |

Page: [`figS14_page.py`](figS14/figS14_page.py).

## Requirements

Python 3.11 or later. Tested with Python 3.13.9, numpy 2.3.5 and matplotlib 3.10.6 ([`requirements.txt`](requirements.txt)). The figures are set in Arial. Where Arial is not installed, matplotlib warns ("findfont: Font family 'Arial' not found") and falls back to its bundled DejaVu Sans, which sets text wider, so the renders then differ from the published pages.

## License

The code in this folder is released under the MIT License; see [`LICENSE`](LICENSE). The data in [`data/`](../data/README.md) are released under CC BY 4.0; see its own LICENSE.
