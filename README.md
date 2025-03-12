# embed2scale-challenge-supplement
Supplementary information for the [embed2scale challenge](https://eval.ai/web/challenges/challenge-page/2465/overview). This repo contains the leaderboard for the challenge, documentation, demos for loading and creating submissions, and more.

The repository is structured as follows:
- The Embed2Scale Challenge leaderboard is presented below, ranked by aggregating the rankings on the individual downstream tasks. Please refer to [here](https://eval.ai/web/challenges/challenge-page/2465/evaluation) for details on the evaluation and ranking.
- `data_loading_submission_demo/`: Contains Jupyter notebooks detailing how the challenge data can be loaded and how the embeddings can be structured into a submission file to be ready for submission on [eval.ai](https://eval.ai/web/challenges/challenge-page/2465/evaluation).
- `figs/`: Images and supplementary files for the competition. Nothing useful that isn't written here or on [eval.ai](https://eval.ai/web/challenges/challenge-page/2465/overview).

# Leaderboard
Leaderboard updated: 2025-03-12 07:40:48

__Dev phase leaderboard__
| Rank | Team | Mean Q |
| :----: | :---- | :------: |
| 1 | AI4G Intern Squad | -0.083 |
| 2 | Host\_94421\_Team | -0.626 |
| 3 | Baseline random embeddings | -8.227 |



Note that 'Host_94421_Team' is the challenge organizers and serves as a non-competing baseline.

## FAQ

In case you have question, please open an issue here. Below a list of insights from questions you posed:

- [#1](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/issues/1): relevant datasets $D^{(\ast)}$ on HuggingFace :
    * *SSL4EO-S12-v1.1*: pre-training of your encoder $E(D)=X=(x_1,x_2,\dots,x_{1024})$: https://huggingface.co/datasets/embed2scale/SSL4EO-S12-v1.1
    * *SSL4EO-S12-downstream*: downstream evaluation $f(X)=f\left(E(D^\ast)\right)=\sum_ia_ix_i=\hat y$: https://huggingface.co/datasets/embed2scale/SSL4EO-S12-downstream
- [#2](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/issues/2):
  *The pretraining dataset SSL4EO-S12-v1.1 contains metadata on georeferencing. May my encoder $E$ utilize such information for compression?*
  No, the SSL4EO-S12-downstream dataset does not provide georeferencing information. The challenge intents to test lossy neural compression on multiple remote sensing modalities without geographic information.
- [#3](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/issues/3):
  *The SSL4EO-S12-v1.1 data $D$ contain RGB imagery (S2RGB). Can I expect this modality for SSL4EO-S12-downstream data $D^\ast$, too?* No, the data cube relevant for the challenge consists of spatially aligned:
  * gridded [ground-range-detected](https://sentiwiki.copernicus.eu/web/s1-processing#S1Processing-GroundRangeDetected(GRD)S1-Processing-Ground-Range-Detected) (GRD) [Synthetic Aperture Radar](https://en.wikipedia.org/wiki/Sentinel-1) (SAR) [Sentinel-1](https://en.wikipedia.org/wiki/Sentinel-1), and
  * multi-spectral [Sentinel-2](https://en.wikipedia.org/wiki/Sentinel-2) L1C and [atmospherically corrected](https://gis.stackexchange.com/questions/385975/should-i-always-choose-sentinel-2-atmospheric-corrected-imagery) (L2A)
imagery.
- [#4](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/issues/4): *I am confused regarding the directory structure of the pre-training $D$ and downstream $D^\ast$ datasets, pls assist.* The relevant mapping reads:
  | *SSL4EO-S12-v1.1* | *SSL4EO-S12-downstream* |
  |-------------------|-------------------------|
  | `S1GRD`           | `s1`                    |
  | `S2L1C`           | `s2l1c`                 |
  | `S2L2A`           | `s2l2a`                 |
  | `S2RGB`           | `-`                     |
- [#5](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/issues/5): *How should I interpret the `Stdout file` and `Stderr file` which I find under `My Submissions` on eval.ai?*
The `Stdout file` contains the final status of the submission from our evaluation in case there were no breaking errors during the evaluation. In addition to the `q_mean` value also shown on the leaderboard, there are the following three fields and their explanations:<br>
`status: Completed.` means the submission was processed and evaluated without issues.<br>
`"more_than_3_LP_failed_for_single_downstream_task": false` means that fewer than 3 linear probings failed during any downstream task evaluation. We allow for up to 3 (out of 10) to fail, i.e. produce a NaN value. More than 3 would immediately break the evaluation and return an error.<br>
`"zarr_zip_not_removed_from_id_column": false` is a simple check that ".zarr.zip" is removed from the challenge data file names by the participants. Forgetting to remove this is not a breaking error, we will remove it ourselves. The reason for this message in the `Stdout file` is to notify that this was forgotten and it is therefore a good idea to verify that no other instructions were missed.<br>
The `Stderr file` is empty if there was no breaking errors.<br>
In case there was a breaking error, the submission will be shown with the status `Failed` ounder `My Submissions`. In this case, the `Stdout file` will be empty while the `Stderr file` will provide the error message.
- [#6](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/issues/6): *Are there any differences in data distribution between the SSL4EO-S12-downstream and SSL4EO-S12 v1.1 data?*<br>
Yes, the two datasets are sampled at different locations and therefore have different distributions. In the [`challenge_dataset.py`](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/blob/main/data_loading_submission_demo/challenge_dataset.py) file, the means and standard deviations are now updated to show the means and standard deviations for the SSL4EO-S12-downstream data (initially, the means and stds for SSL4EO-S12 v1.1 were copied to this file. __If you cloned the repository before 20250311 16:30 and want to use the values calculated by us, please pull the latest changes from this repository__.)
