# Embed2scale challenge submission demo

Here is an example, both as jupyter notebook and python script, how to 
- Load the challenge dataset data using the embed2scale custom dataset as well as the SSL4EO-S12 V1.1 dataset.
- Create embeddings for each challenge task sample.
- Create a submission file ready for submitting to eval.ai

The recommended pyhton packages for loading the challenge data are provided in requirements.txt. Note that only zarr<3.0 is a hard requirement, the remaining are recommendations which we have tested. The challenge task data is created with the versions of xarray and zarr stated in requirements.txt.