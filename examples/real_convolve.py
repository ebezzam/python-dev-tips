import numpy as np
import matplotlib.pyplot as plt
from pydevtips.fftconvolve import RFFTConvolve


# Create a signal
signal = np.random.randn(1000)

# Create a moving average filter (low pass)
n = 10
filter = np.ones(n) / n

# initialize the convolver
convolver = RFFTConvolve(filter=filter, length=len(signal))

# convolve
convolved_signal = convolver(signal)

# plot with three subplots
fig, ax = plt.subplots(3, 1, figsize=(10, 10))
ax[0].plot(signal)
ax[0].set_title("Signal")
ax[1].plot(filter)
ax[1].set_title("Filter")
ax[2].plot(convolved_signal)
ax[2].set_title("Convolved Signal")

plt.show()
