import os

import hydra
import matplotlib.pyplot as plt
import numpy as np
from hydra.utils import instantiate

from pydevtips.fftconvolve import RFFTConvolve


class PowerTransform:
    def __init__(self, pow):
        self.pow = pow

    def __call__(self, x):
        return np.power(x, self.pow)


class ExampleZeros:
    """
    Wrapper over np.zeros
    """

    def __init__(self, signal_len) -> None:
        self.data = np.zeros(signal_len)

    def max(self):
        return self.data.max()

    def __array__(self):
        return self.data

    def __len__(self):
        return len(self.data)


class ExampleCustom:
    """
    Wrapper over custom np.ndarray creation method with an optional transform
    """

    def __init__(self, signal_len, numpy_method, transform=None) -> None:
        self.data = getattr(np, numpy_method)(signal_len)
        if transform is not None:
            self.data = transform(self.data)

    def max(self):
        return self.data.max()

    def __array__(self):
        return self.data

    def __len__(self):
        return len(self.data)


@hydra.main(version_base=None, config_path="configs", config_name="defaults")
def main(config):

    output_dir = os.getcwd()
    np.random.seed(config.seed)

    # Create a signal
    signal = instantiate(config.signal, config.signal_len)
    # Note that we added extra argument signal_len which was not defined in signal config
    print(f"Signal class, len and max: {type(signal), len(signal), signal.max()}")
    signal = np.array(signal)  # for the following computations np.ndarray is required

    # Create a moving average filter (low pass)
    n = config.filter_len
    filter = np.ones(n) / n

    # initialize the convolver
    convolver = RFFTConvolve(filt=filter, length=len(signal))

    # convolve
    convolved_signal = convolver(signal)

    # plot with three subplots
    _, ax = plt.subplots(3, 1, figsize=(10, 10))
    ax[0].plot(signal)
    ax[0].set_title("Signal")
    ax[1].plot(filter)
    ax[1].set_title("Filter")
    ax[2].plot(convolved_signal)
    ax[2].set_title("Convolved Signal")

    plt.savefig(os.path.join(output_dir, "convolved_signal.png"))
    output_fp = os.path.join(output_dir, "convolved_signal.png")
    print(f"Saved convolved signal to {output_fp}")

    plt.show()


if __name__ == "__main__":
    main()
