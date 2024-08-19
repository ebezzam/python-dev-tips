"""
In this script, we use the Hugging Face dataset made
from the script examples/create_huggingface_dataset.py

The dataset is available at:
https://huggingface.co/bezzam/dummy-dataset

```bash
# install
pip install datasets librosa soundfile

# run
python examples/use_huggingface_dataset.py
```

During the first run, the dataset will be downloaded and cached.
Subsequent runs will use the cached dataset.

"""

from datasets import load_dataset
import numpy as np


# load train and test splits
ds_train = load_dataset("bezzam/dummy-dataset", split="train")
ds_test = load_dataset("bezzam/dummy-dataset", split="test")
print(f"Number of training samples: {len(ds_train)}")
print(f"Number of test samples: {len(ds_test)}")

# load first example
print("\n---- First example:")
example = ds_train[0]

# -- audio duration
duration = len(example["audio"]["array"]) / example["audio"]["sampling_rate"]
print(f"Duration of audio: {duration:.2f} seconds")

# -- image size
image = np.array(example["image"])
print(f"Size of image: {image.shape}")

# -- text
text = example["text"]
print(f"Text: {text}")

# -- label
label = example["label"]
label_str = ds_train.features["label"].int2str(label)
print(f"Label: {label_str}")
