import numpy as np
import matplotlib.pyplot as plt
from pydevtips.fftconvolve import RFFTConvolve
import hydra
import os


@hydra.main(version_base=None, config_path="configs", config_name="defaults")
def main(config):

    output_dir = os.getcwd()
    np.random.seed(config.seed)

    # Create a signal
    signal = np.random.randn(config.signal_len)

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
