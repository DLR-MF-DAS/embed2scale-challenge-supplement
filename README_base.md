# Leaderboard
<!-- INSERT LEADERBOARD HERE -->

# NEWS

## Development Phase ended, Final Submission for Ranking ahead!

The development phase closed. Now get ready to compress approx. 90GB from https://huggingface.co/datasets/embed2scale/SSL4EO-S12-downstream/tree/5c5539acd6f42e2e3547ec816fcf577e3f6800fa/data_eval (available for download starting Apr 1, 2025) for submission starting Apr 3 through Apr 5.
Your scores will determine the final ranking to find our winners (cf. below). We are excited about your solution, all the best luck!

## About CVPR EARTHVISION winners

In addition to the winner according to https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement?tab=readme-ov-file#leaderboard we decided to also invite the solution with the highest `q_mean` score to present their solution at the CVPR EARTHVISION workshop. Each of the winning teams will receive a cash prize of 1k EUR as support to come to Nashville, TN, USA for the presentation. On April 7, 2025 we'll get in touch with the two winning teams through the email ID they provided to Eval.AI. **Teams that participated in the development phase are the only ones eligible to count as valid winners of the final test phase.**

### Attention regarding the submission that counts

Just to clarify: The winning solution on the leaderboard will be determined by the **last public** one that you will have submitted in the period Apr 3-5, 2025. This is due to the nature how our global ranking works.

For the independent ranking based on the `q_mean` score, the best of your (up to) three **public** submissions counts according to the [Eval.AI leaderboard](https://eval.ai/web/challenges/challenge-page/2465/leaderboard/6117).

In summary, after the evaluation phase ended on Apr 5, 2025 we will contact the two winning teams on Apr 7, 2025 through their email specified on the Eval.AI platform according to:
- 1k EUR for the 1st ranked in https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement?tab=readme-ov-file#leaderboard (_Test phase_ leaderboard, not _Dev phase_)
- 1k EUR for the 1st ranked in https://eval.ai/web/challenges/challenge-page/2465/leaderboard/6117

Moreover, for a winning team it is mandatory to have participated in the development phase that happened Mar 10 through Mar 31, 2025. _Participation_ is defined as having registered with a valid email for https://eval.ai/web/challenges/challenge-page/2465 before April 1, 2025 and having submitted at least one successfully evaluated (marked as _Finished_), private or **public** submission.

Also, we require the winning teams to open-source their (neural) compressor code under https://www.apache.org/licenses/LICENSE-2.0 . We demand that the embeddings corresponding to the submitted, winning solution can be transparently reproduced.

---

**public** as selected on submission time through the Eval.AI platform:

<img src="figs/public_submission_screenshot.png" width="500">

Note that you have a total of 3 submission in Apr 3-5, 2025 - whether private or **public**. We recommend you exclusively submit with option **public**.

### And even should you not win the thing ...

... we are so grateful you participated! We are also very happy to link the code to your solution here. If you'd like so, pls open a corresponding issue here.

# Embed2Scale Challenge - supplementary material
Supplementary information for the [Embed2Scale (E2S) challenge](https://eval.ai/web/challenges/challenge-page/2465) as part of the [2025 CVPR EARTHVISION workshop](https://www.grss-ieee.org/events/earthvision-2025) co-organized by the Horizon Europe [Embed2Scale_ consortium](https://embed2scale.eu). This repo contains the (customized) leaderboard for the challenge, documentation, demos for loading and creating submissions, frequently asked questions based on GitHub issues you can open, and more.

The repository is structured as follows:
- The Embed2Scale Challenge leaderboard is presented below, ranked by aggregating the rankings on the individual downstream tasks. Please refer to [here](https://eval.ai/web/challenges/challenge-page/2465/evaluation) for details on the evaluation and ranking.
- `data_loading_submission_demo/`: Contains Jupyter notebooks detailing how the challenge data can be loaded and how the embeddings can be structured into a submission file to be ready for submission on [eval.ai](https://eval.ai/web/challenges/challenge-page/2465/evaluation).
- `figs/`: Images and supplementary files for the competition. Nothing useful that isn't written here or on [eval.ai](https://eval.ai/web/challenges/challenge-page/2465/overview).

## FAQ

In case you have question, please open an issue here. Below a list of insights from questions you posed:

- [GH issue #1](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/issues/1) and [GH issue #13](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/issues/13): relevant datasets $D^{(\ast)}$ on HuggingFace:<br>
    * *SSL4EO-S12-v1.1*: pre-training of your encoder $E(D)=X=(x_1,x_2,\dots,x_{1024})$: https://huggingface.co/datasets/embed2scale/SSL4EO-S12-v1.1
      + timestamp metadata info in ZARR files, seasons in linear order in range of years 2020 to 2021
    * *SSL4EO-S12-downstream*: downstream evaluation $f(X)=f\left(E(D^\ast)\right)=a_0+\sum_ia_ix_i=\hat y$: https://huggingface.co/datasets/embed2scale/SSL4EO-S12-downstream/tree/5c5539acd6f42e2e3547ec816fcf577e3f6800fa , timestamp ordering in buckets of months of the year:
      1. *spring* (northern hemisphere): Mar - May
      2. *summer*: Jun - Aug
      3. *fall*: Sep - Nov
      4. *winter*: Dec - Feb
- [GH issue #12](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/issues/12) and [GH issue #7](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/issues/7):
  *The [E2S Eval.AI webpage](https://eval.ai/web/challenges/challenge-page/2465) states linear probing as in* $f(X)=\sum_ia_ix_i$. *Do I need to include a constant feature* $x_1=1$ *in my embedding* $X$ *to account for a bias term?*<br>
  No, our linear probing automatically accounts for a bias term. BTW, we normalize your embeddings $X$ by a global, overall mean shift and division by the corresponding standard deviation over all embedding values submitted.
- [GH issue #2](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/issues/2):
  *The pretraining dataset SSL4EO-S12-v1.1 contains metadata on georeferencing. May my encoder* $E$ *utilize such information for compression?*<br>
  No, the SSL4EO-S12-downstream dataset does not provide georeferencing information. The challenge intents to test lossy neural compression on multiple remote sensing modalities without geographic information.
- [GH issue #3](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/issues/3):
  *The SSL4EO-S12-v1.1 data* $D$ *contain RGB imagery (S2RGB). Can I expect this modality for SSL4EO-S12-downstream data* $D^\ast$, *too?* <br>
  No, the data cube relevant for the challenge consists of spatially aligned:
  * gridded [ground-range-detected](https://sentiwiki.copernicus.eu/web/s1-processing#S1Processing-GroundRangeDetected(GRD)S1-Processing-Ground-Range-Detected) (GRD) [Synthetic Aperture Radar](https://en.wikipedia.org/wiki/Sentinel-1) (SAR) [Sentinel-1](https://en.wikipedia.org/wiki/Sentinel-1), and
  * multi-spectral [Sentinel-2](https://en.wikipedia.org/wiki/Sentinel-2) L1C and [atmospherically corrected](https://gis.stackexchange.com/questions/385975/should-i-always-choose-sentinel-2-atmospheric-corrected-imagery) (L2A)
imagery.
- [GH issue #4](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/issues/4): *I am confused regarding the directory structure of the pre-training* $D$ *and downstream* $D^\ast$ *datasets, pls assist.*<br>
  The relevant mapping reads:
  | *SSL4EO-S12-v1.1* | *SSL4EO-S12-downstream* |
  |-------------------|-------------------------|
  | `S1GRD`           | `s1`                    |
  | `S2L1C`           | `s2l1c`                 |
  | `S2L2A`           | `s2l2a`                 |
  | `S2RGB`           | `-`                     |
- [GH issue #5](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/issues/5): *How should I interpret the `Stdout file` and `Stderr file` which I find under `My Submissions` on eval.ai?*<br>
    * The `Stdout file` contains the final status of the submission from our evaluation in case there were no breaking errors during the evaluation. In addition to the `q_mean` value also shown on the leaderboard, there are the following three fields and their explanations:<br>
        + `status: Completed.` means the submission was processed and evaluated without issues.
        + `"more_than_3_LP_failed_for_single_downstream_task": false` means that fewer than 3 linear probings failed during any downstream task evaluation. We allow for up to 3 (out of 10) to fail, i.e. produce a NaN value. More than 3 would immediately break the evaluation and return an error.
        + `"zarr_zip_not_removed_from_id_column": false` is a simple check that ".zarr.zip" is removed from the challenge data file names by the participants. Forgetting to remove this is not a breaking error, we will remove it ourselves. The reason for this message in the `Stdout file` is to notify that this was forgotten and it is therefore a good idea to verify that no other instructions were missed.
    * The `Stderr file` is empty if there was no breaking errors.
    * In case there was a breaking error, the submission will be shown with the status `Failed` under `My Submissions`. In this case, the `Stdout file` will be empty while the `Stderr file` will provide the error message.
- [GH issue #6](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/issues/6) and [GH issue #10](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/issues/10): *Are there any differences in data distribution between the SSL4EO-S12-downstream and SSL4EO-S12 v1.1 data?*<br>
Yes, there is one main difference in that the SSL4EO-S12 v1.1 shifts the S2 channels up by 1000 in order to be compliant with the latest ESA processing. The Challenge data does not have this shift in the zarr files, but the [`challenge_dataset.py`](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/blob/main/data_loading_submission_demo/challenge_dataset.py) there is the flag `shift_s2_channels` which sets configures the dataset to apply the shift. This is by default True in order to align with SSL4EO-S12 v1.1. We also provide the mean and standard deviations for both the raw challenge data, and the means and standard deviations from SSL4EO-S12 v1.1.
- *Why does only one of my submissions show up on the [custom leaderboard](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement#leaderboard)?*<br>
The custom leaderboard shows the latest submission from each participating team. __To ensure that you rank as high as possible, resubmit your best submission as your very last submission before the end of each challenge phase__.
- *Will my private submissions show up on the custom leaderboard?*<br>
No, only public submissions are shown on the custom leaderboard.
- *Does the E2S challenge put any restrictions on team size?* <br>
No, you are free to collaborate as you prefer. However, keep in mind that you probably do not wanna inflate a potential paper associated with your (winning) solution. For the presentation of the winning solution at CVPR we expect one or two of your team mates to represent.
- [GH issue #8](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/issues/8): *Help me understand the quality score* $Q_t$?<br>
$Q_t=A_t/\Delta A_t$ one may interpret as a signal-to-noise ratio where $A_t$ is the mean accuracy of a given (secret) downstream task $t$ and $\Delta A_t$ specifies the fluctuation of $A_t$ when the linear probing function $f(X)=\hat y$ is trained multiple times through k-fold cross-validation. Technically, $Q_t\propto A_t/(\Delta A_t+\epsilon)$ with $\epsilon>0$ such that the maximum value of $Q_t$ is `100`. However, since we utilize $R^2$ for regression tasks, $Q_t$ may turn negative indicating that linear probing performs even worse than simply predicting the mean value of all labels for that downstream task.
- *How are the non-competing baselines created?*<br>
The `Baseline mean embeddings` is created with [baseline_compression_mean.ipynb](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/blob/main/data_loading_submission_demo/baseline_compression_mean.ipynb) and `Baseline random embeddings` is created with [demo_load_create_submission.ipynb](https://github.com/DLR-MF-DAS/embed2scale-challenge-supplement/blob/main/data_loading_submission_demo/demo_load_create_submission.ipynb). The `Host_94421_Team` submissions can be both our own development as well as test submissions.
- *The seasonal order of data cubes in the `SSL4EO-S12-*` datasets is: spring, summer, fall, winter*?<br> Yes.
