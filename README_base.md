# embed2scale-challenge-supplement
Supplementary information for the [embed2scale challenge](https://eval.ai/web/challenges/challenge-page/2465/overview). This repo contains the leaderboard for the challenge, documentation, demos for loading and creating submissions, and more.

The repository is structured as follows:
- The Embed2Scale Challenge leaderboard is presented below, ranked by aggregating the rankings on the individual downstream tasks. Please refer to [here](https://eval.ai/web/challenges/challenge-page/2465/evaluation) for details on the evaluation and ranking.
- `data_loading_submission_demo/`: Contains Jupyter notebooks detailing how the challenge data can be loaded and how the embeddings can be structured into a submission file to be ready for submission on [eval.ai](https://eval.ai/web/challenges/challenge-page/2465/evaluation).
- `figs/`: Images and supplementary files for the competition. Nothing useful that isn't written here or on [eval.ai](https://eval.ai/web/challenges/challenge-page/2465/overview).

# Leaderboard
<!-- INSERT LEADERBOARD HERE -->

## FAQ

In case you have question, please open an issue here. Below a list of insights from questions you posed:

- [GH issue #1](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/issues/1): relevant datasets $D^{(\ast)}$ on HuggingFace:<br>
    * *SSL4EO-S12-v1.1*: pre-training of your encoder $E(D)=X=(x_1,x_2,\dots,x_{1024})$: https://huggingface.co/datasets/embed2scale/SSL4EO-S12-v1.1
    * *SSL4EO-S12-downstream*: downstream evaluation $f(X)=f\left(E(D^\ast)\right)=\sum_ia_ix_i=\hat y$: https://huggingface.co/datasets/embed2scale/SSL4EO-S12-downstream
- [GH issue #2](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/issues/2):
  *The pretraining dataset SSL4EO-S12-v1.1 contains metadata on georeferencing. May my encoder* $E$ *utilize such information for compression?*<br>
  No, the SSL4EO-S12-downstream dataset does not provide georeferencing information. The challenge intents to test lossy neural compression on multiple remote sensing modalities without geographic information.
- [GH issue #3](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/issues/3):
  *The SSL4EO-S12-v1.1 data* $D$ *contain RGB imagery (S2RGB). Can I expect this modality for SSL4EO-S12-downstream data* $D^\ast$, *too?* <br>
  No, the data cube relevant for the challenge consists of spatially aligned:
  * gridded [ground-range-detected](https://sentiwiki.copernicus.eu/web/s1-processing#S1Processing-GroundRangeDetected(GRD)S1-Processing-Ground-Range-Detected) (GRD) [Synthetic Aperture Radar](https://en.wikipedia.org/wiki/Sentinel-1) (SAR) [Sentinel-1](https://en.wikipedia.org/wiki/Sentinel-1), and
  * multi-spectral [Sentinel-2](https://en.wikipedia.org/wiki/Sentinel-2) L1C and [atmospherically corrected](https://gis.stackexchange.com/questions/385975/should-i-always-choose-sentinel-2-atmospheric-corrected-imagery) (L2A)
imagery.
- [GH issue #4](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/issues/4): *I am confused regarding the directory structure of the pre-training $D$ and downstream $D^\ast$ datasets, pls assist.* The relevant mapping reads:
  | *SSL4EO-S12-v1.1* | *SSL4EO-S12-downstream* |
  |-------------------|-------------------------|
  | `S1GRD`           | `s1`                    |
  | `S2L1C`           | `s2l1c`                 |
  | `S2L2A`           | `s2l2a`                 |
  | `S2RGB`           | `-`                     |
- [GH issue #5](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/issues/5): *How should I interpret the `Stdout file` and `Stderr file` which I find under `My Submissions` on eval.ai?*
The `Stdout file` contains the final status of the submission from our evaluation in case there were no breaking errors during the evaluation. In addition to the `q_mean` value also shown on the leaderboard, there are the following three fields and their explanations:<br>
`status: Completed.` means the submission was processed and evaluated without issues.<br>
`"more_than_3_LP_failed_for_single_downstream_task": false` means that fewer than 3 linear probings failed during any downstream task evaluation. We allow for up to 3 (out of 10) to fail, i.e. produce a NaN value. More than 3 would immediately break the evaluation and return an error.<br>
`"zarr_zip_not_removed_from_id_column": false` is a simple check that ".zarr.zip" is removed from the challenge data file names by the participants. Forgetting to remove this is not a breaking error, we will remove it ourselves. The reason for this message in the `Stdout file` is to notify that this was forgotten and it is therefore a good idea to verify that no other instructions were missed.<br>
The `Stderr file` is empty if there was no breaking errors.<br>
In case there was a breaking error, the submission will be shown with the status `Failed` under `My Submissions`. In this case, the `Stdout file` will be empty while the `Stderr file` will provide the error message.
- [GH issue #6](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/issues/6): *Are there any differences in data distribution between the SSL4EO-S12-downstream and SSL4EO-S12 v1.1 data?*<br>
Yes, the locations in the two datasets are sampled differently and therefore have different distributions. In the [`challenge_dataset.py`](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/blob/main/data_loading_submission_demo/challenge_dataset.py) file now shows the means and standard deviations for the SSL4EO-S12-downstream data (after 2025-03-11 16:30, before this, the SSL4EO-S12 v1.1 stats were given). You are free to use any normalization/transformation, e.g. the SSL4EO-S12 v1.1 found [here](https://github.com/DLR-MF-DAS/SSL4EO-S12-v1.1).
- *Why do only one of my submissions show up on the [custom leaderboard](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement)?*<br>
The custom leaderboard shows the latest submission from each participating team. It also does not take into account the `Public` or `Private` settings during submission and will show the latest one regardless of this setting. __To ensure that you rank as high as possible, resubmit your best submission as your very last submission before the end of each challenge phase__.
- *Why is my `Private` submission showing up on the [custom leaderboard](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement)?*<br>
Please see the previous answer.
- *Does the E2S challenge put any restrictions on team size?* <br>
No, you are free to collaborate as you prefer. However, keep in mind that you probably do not wanna inflate a potential paper associated with your (winning) solution. For the presentation of the winning solution at CVPR we expect one or two of your team mates to represent.
- [GH issue #8](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/issues/8): *Help me understand the quality score $Q_t$?*<br>
$Q_t=A_t/\Delta A_t$ one may interpret as a signal-to-noise ratio where $A_t$ is the mean accuracy of a given (secret) downstream task $t$ and $\Delta A_t$ specifies the fluctuation of $A_t$ when the linear probing function $f(X)=\hat y$ is trained multiple times through k-fold cross-validation. Technically, $Q_t\propto A_t/(\Delta A_t+\epsilon)$ with $\epsilon>0$ such that the maximum value of $Q_t$ is `100`. However, since we utilize $R^2$ for regression tasks, $Q_t$ may turn negative indicating that linear probing performs even worse than simply predicting the mean value of all labels for that downstream task.
