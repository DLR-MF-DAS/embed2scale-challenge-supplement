# %% Embed2Scale challenge demo notebook
# In this script we show two ways of loading the challenge task data; first through our custom challenge dataloader, and then with a dataloader from the updated SSL4EO-S12 V1.1 dataset.
#We then give an example of how to create a submission file by creating embeddings through random sampling.

import numpy as np
import pandas as pd

from torchvision import transforms
from torch.utils.data import DataLoader

from challenge_dataset import E2SChallengeDataset, collate_fn
from ssl4eos12_dataset import SSL4EOS12Dataset, S2L1C_MEAN, S2L1C_STD, S2L2A_MEAN, S2L2A_STD, S1GRD_MEAN, S1GRD_STD

# %% Configurations
modalities = ['s2l2a', 's2l1c', 's1']

# 
path_to_data = '/path/to/challenge/data/'
path_to_output_file = 'path/to/output/file.csv'

write_result_to_file = False  # Set to True to trigger saving of the csv at the end.

# Create data transformation
# Get mean and standard deviations for the modealities in the correct order
mean_data = S2L2A_MEAN + S2L1C_MEAN + S1GRD_MEAN
std_data = S2L2A_STD + S2L1C_STD + S1GRD_STD

data_transform = transforms.Compose([
    # Add additional transformation here
    transforms.Normalize(mean=mean_data, std=std_data)
])

# Note that both E2SChallengeDataset and SSL4EOS12Dataset outputs torch tensors, so there is no need to a ToTensor transform.

# %% Load data with custom dataloader

# Example 1.
# Do not concatenate modalities
# Dataloader output is {'data': {'s2l2a': s2l2a_data, 's2l1c': s2l1c_data, 's1': s1_data}, 'file_name': file_name}
# The data has shapes [n_samples, n_seasons, n_channels, height, width] (for s2l2a [1, 4, 12, 264, 264])

concatenate_modalities = False
dataset_e2s = E2SChallengeDataset(path_to_data, 
                               modalities = modalities, 
                               dataset_name='bands', 
                               transform=data_transform, 
                               concat=concatenate_modalities,
                               output_file_name=False
                              )

# Print dataset length
print(f"Length of train dataset: {len(dataset_e2s)}")

# Print shape of first sample
for m, d in dataset_e2s[0].items():
    print(f'Modality {m} shape:', d.shape)


# Example 2.
# Concatenate modalities
# dataloader output is {'data': concatenated_data, 'file_name': file_name}
# The data has shapes [n_samples, n_seasons, n_channels, height, width] (for concatenated_data [1, 4, 27, 264, 264])

concatenate_modalities = True
dataset_e2s = E2SChallengeDataset(path_to_data, 
                               modalities = modalities, 
                               dataset_name='bands', 
                               transform=data_transform, 
                               concat=concatenate_modalities,
                               output_file_name=True
                              )

# Print dataset length
print(f"Length of train dataset: {len(dataset_e2s)}")

# Print shape of first sample
print(dataset_e2s[0]['data'].shape)

# %% Load with SSL4EOS12 V1.1 dataloader
# Note that we have modified the code to allow for a different number of samples per zarr files. 
# The challenge task data consists of a single sample per file, while SSL4EO-S12 V1.1 has 64 samples per zarr file.
dataset_ssl4eo = SSL4EOS12Dataset(
    data_dir=path_to_data,
    modalities=modalities, # optional, list of modality folders.
    transform=data_transform,  # optional, torchvision transforms. Returns tensors if not provided.
    concat=True,  # Concatenate all modalities along the band dimension.
    single_timestamp=False,  # Load single timestamps rather than time series.
    num_batch_samples=1,  # optional, subsample samples in each zarr file.
    num_timestamps=4  # optional, number of seasons to include
)

# Print dataset length
print(f"Length of train dataset: {len(dataset_ssl4eo)}")

# Print shape of first sample
print(dataset_ssl4eo[0].shape)

# Compare the output from the datasets
print("The two datasets' first sample is the same:", np.all((dataset_e2s[0]['data'] == dataset_ssl4eo[0]).numpy()))

# %% Dataloader
train_loader  = DataLoader(
    dataset=dataset_e2s,
    batch_size=2,  # Note that each each challenge task zarr file contains a single sample.
    shuffle=True,
    collate_fn=collate_fn,  # Data needs to be concatenated along sample dimension instead of being stacked,
)

for ind, data_file_name in enumerate(train_loader):
    for find, fn in enumerate(data_file_name['file_name']):
        print(f'File name {find}:', fn[0:10] + '...')
    print(data_file_name['data'].shape)
    break

# %% Create submission file
# In this section, we create a submission by randomly generating embeddings of the correct size.
# Finally, we create a submission file.

# We use the E2SChallengeDataset since we can easily get the sample ID (file name) from the dataloader.
def str_format_np_array(arr):
    """Create string from numpy array formatted as: '[val1, val2, ...]'."""
    return '[' + ','.join([str(n) for n in arr]) + ']'

def create_submission_from_dict(emb_dict):
    """Assume dictionary has format {hash-id0: embedding0, hash-id1: embedding1, ...}
    """
    df_submission = pd.DataFrame(data=[[k, str_format_np_array(e)] for k, e in emb_dict.items()], 
                                 columns=['id', 'embedding'], dtype=str)
        
    return df_submission

# Randomly generate embeddings from normal distribution.

create_n_embeddings = 10

embedding_dim = 1024
embeddings = {}
rng = np.random.default_rng(seed=None)
for ind, data_file_name in enumerate(train_loader):
    # -------------------------
    # Do compression magic here
    # -------------------------

    # Randomly generate embedding from normal distribution
    for fn in data_file_name['file_name']:
        emb = rng.normal(0, 1, size=(embedding_dim,))
        embeddings[fn] = emb

    # Stop early in this example
    if ind >= create_n_embeddings-1:
        break

# Create submission file
submission_file = create_submission_from_dict(embeddings)

# Print submission
print(submission_file.head())

# Write submission
if False:
    submission_file.to_csv('./random_embeddings.csv', index=False)