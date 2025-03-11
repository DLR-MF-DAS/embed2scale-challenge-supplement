# embed2scale-challenge-supplement
Supplementary information for the [embed2scale challenge](https://eval.ai/web/challenges/challenge-page/2465/overview). This repo contains the leaderboard for the challenge, documentation, demos for loading and creating submissions, and more.

The repository is structured as follows:
- The Embed2Scale Challenge leaderboard is presented below, ranked by aggregating the rankings on the individual downstream tasks. Please refer to [here](https://eval.ai/web/challenges/challenge-page/2465/evaluation) for details on the evaluation and ranking.
- `data_loading_submission_demo/`: Contains Jupyter notebooks detailing how the challenge data can be loaded and how the embeddings can be structured into a submission file to be ready for submission on [eval.ai](https://eval.ai/web/challenges/challenge-page/2465/evaluation).
- `figs/`: Images and supplementary files for the competition. Nothing useful that isn't written here or on [eval.ai](https://eval.ai/web/challenges/challenge-page/2465/overview).

# Leaderboard
<!-- INSERT LEADERBOARD HERE -->

## FAQ

In case you have question, pls open an issue here. Below a list of insights from questions you posed:

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
  
