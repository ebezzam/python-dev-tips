"""
We will create a dataset with images, audios, and text data
so that you can see how various data types can be pushed to
Hugging Face!

The default configuration is in `examples/configs/hf_dataset.yaml`:

```bash
# install
pip install datasets huggingface_hub soundfile

# make a WRITE token on HuggingFace: https://huggingface.co/settings/tokens

# run
python examples/create_huggingface_dataset.py \
hf_token=... \
```
"""

import hydra
from hydra.utils import to_absolute_path
import os
import time
import glob
import numpy as np
import soundfile as sf
from PIL import Image as PILImage
from datasets import Dataset, Image, Audio, ClassLabel
from omegaconf import open_dict
from huggingface_hub import upload_file
import re
import pandas as pd


# -- helper functions
def convert(text):
    return int(text) if text.isdigit() else text.lower()


def alphanum_key(key):
    return [convert(c) for c in re.split("([0-9]+)", key)]


def natural_sort(arr):
    return sorted(arr, key=alphanum_key)


@hydra.main(version_base=None, config_path="configs", config_name="hf_dataset")
def main(config):

    start_time = time.time()

    # extract and check parameters
    repo_id = config.repo_id
    hf_token = config.hf_token
    test_size = config.test_size

    assert repo_id is not None, "Please provide a Hugging Face repo_id."
    assert hf_token is not None, "Please provide a Hugging Face token."

    # to absolute path, as needed by Hugging Face upload
    for data in config.data_dir:
        if "dir" in config.data_dir[data]:
            config.data_dir[data]["dir"] = to_absolute_path(config.data_dir[data]["dir"])
        elif "file" in config.data_dir[data]:
            config.data_dir[data]["file"] = to_absolute_path(config.data_dir[data]["file"])

    # Step 1: Check data (create dummy data if not present)
    n_files = 100  # number of dummy files to create
    for data in config.data_dir:

        # for directory of data
        if "dir" in config.data_dir[data]:
            input_dir = config.data_dir[data]["dir"]
            data_type = config.data_dir[data]["type"]

            if not os.path.exists(input_dir):
                # create dummy data
                print(f"-- Creating {n_files} dummy {data_type} files in {input_dir}")
                os.makedirs(input_dir, exist_ok=True)
                for i in range(n_files):
                    if data_type == "png":
                        img = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
                        img_path = os.path.join(input_dir, f"{i}.png")
                        PILImage.fromarray(img).save(img_path)
                    elif data_type == "wav":
                        audio = np.random.randn(16000)
                        audio_path = os.path.join(input_dir, f"{i}.wav")
                        sf.write(audio_path, audio, samplerate=16000)
                    elif data_type == "txt":
                        text = f"Hello, this is file {i}"
                        text_path = os.path.join(input_dir, f"{i}.txt")
                        with open(text_path, "w") as f:
                            f.write(text)

            # check number of files
            files = glob.glob(os.path.join(input_dir, "*." + data_type))
            n_files = len(files)
            print(f"Found {n_files} {data_type} files in {input_dir}")

        # for CSV file where each line is a data point
        elif "file" in config.data_dir[data]:
            input_file = config.data_dir[data]["file"]

            if not os.path.exists(input_file):
                # create dummy labels
                labels = ["good", "ok", "bad"]
                file_labels = np.random.choice(labels, n_files)
                with open(input_file, "w") as f:
                    for i in range(n_files):
                        f.write(f"{i},{file_labels[i]}\n")
                print(f"-- Created dummy labels file at {input_file}")

            # check number of unique labels (open with Pandas)
            df = pd.read_csv(input_file, header=None)
            n_files = len(df)
            labels = df[1].unique()
            n_labels = len(df[1].unique())
            print(f"Found {n_files} lines with {n_labels} unique labels ({labels}) in {input_file}")

        else:
            raise ValueError("Please provide either `dir` or `file` in data_dir")

    # -- only keep common files across all datasets
    bn = [os.path.basename(f).split(".")[0] for f in files]
    for data in config.data_dir:
        if "dir" in config.data_dir[data]:
            input_dir = config.data_dir[data]["dir"]
            data_type = config.data_dir[data]["type"]
            files = glob.glob(os.path.join(input_dir, "*." + data_type))
            bn_data = [os.path.basename(f).split(".")[0] for f in files]
            common_files = list(set(bn).intersection(bn_data))
    common_files = natural_sort(common_files)
    print(f"Number of common files: {len(common_files)}")

    # -- add common files into dictionary
    for data in config.data_dir:
        if "dir" in config.data_dir[data]:
            with open_dict(config):
                config.data_dir[data]["data"] = common_files
        if "file" in config.data_dir[data]:
            # take row according to common_files
            df = pd.read_csv(config.data_dir[data]["file"], header=None)
            # -- make first column string
            df[0] = df[0].astype(str)
            df = df[df[0].isin(common_files)]
            with open_dict(config):
                config.data_dir[data]["data"] = df[1].tolist()

    # Step 2: Create train and test data
    dataset_dict = {}

    # -- create dictionary of content
    for data in config.data_dir:
        if "dir" in config.data_dir[data]:
            files = config.data_dir[data]["data"]
            data_type = config.data_dir[data]["type"]
            data_files = [
                os.path.join(config.data_dir[data]["dir"], f"{f}.{data_type}") for f in files
            ]

            if data_type in ["txt"]:
                # open file content for text files
                data_files = [open(f).read() for f in data_files]
            dataset_dict[data] = data_files
        elif "file" in config.data_dir[data]:
            dataset_dict[data] = config.data_dir[data]["data"]

    # -- create dataset
    dataset = Dataset.from_dict(dataset_dict)
    for data in config.data_dir:
        if "dir" in config.data_dir[data]:
            if config.data_dir[data]["type"] in ["png", "jpg", "jpeg", "tiff"]:
                dataset = dataset.cast_column(data, Image())
            elif config.data_dir[data]["type"] in ["wav", "mp3", "flac", "ogg"]:
                dataset = dataset.cast_column(data, Audio())
        elif "file" in config.data_dir[data]:
            if config.data_dir[data]["label"]:
                labels = list(set(config.data_dir[data]["data"]))
                dataset = dataset.cast_column(data, ClassLabel(names=labels))

    # -- split into train and test
    dataset = dataset.train_test_split(
        test_size=test_size,
        seed=config.seed,
        shuffle=True,
        stratify_by_column=config.stratify_by_column,  # shuffle must be True
    )
    print(dataset)

    """
    DatasetDict({
        train: Dataset({
            features: ['audio', 'images', 'text', 'labels'],
            num_rows: 85
        })
        test: Dataset({
            features: ['audio', 'images', 'text', 'labels'],
            num_rows: 15
        })
    })
    """

    # Step 3: Push to Hugging Face
    dataset.push_to_hub(repo_id, token=hf_token)

    # -- push individual files
    for data in config.data_dir:
        if "dir" in config.data_dir[data]:
            # push first file
            local_fp = os.path.join(
                config.data_dir[data]["dir"],
                config.data_dir[data]["data"][0] + "." + config.data_dir[data]["type"],
            )
            remote_fn = "example." + config.data_dir[data]["type"]
            upload_file(
                path_or_fileobj=local_fp,
                path_in_repo=remote_fn,
                repo_id=repo_id,
                repo_type="dataset",
                token=hf_token,
            )

    # total time in minutes
    print(f"Total time: {(time.time() - start_time) / 60} minutes")


if __name__ == "__main__":
    main()
