import numpy as np
from tqdm import tqdm
import time
from pydevtips.fftconvolve import RFFTConvolve, FFTConvolve

# create random signal
signal = np.random.randn(10000)

# create filter
n = 10000
filter = np.ones(n) / n

# create FFT objects
rfft_convolver = RFFTConvolve(filter=filter, length=len(signal))
fft_convolver = FFTConvolve(filter=filter, length=len(signal))

# profile
n_trials = 1000

# rfft
print("rfft")
rfft_convolved_signal = np.zeros_like(signal)
start_time = time.time()
for _ in tqdm(range(n_trials)):
    _ = rfft_convolver(signal)
proc_time_rfft = (time.time() - start_time) / n_trials

# fft
print("fft")
fft_convolved_signal = np.zeros_like(signal)
start_time = time.time()
for _ in tqdm(range(n_trials)):
    _ = fft_convolver(signal)
proc_time_fft = (time.time() - start_time) / n_trials

# compare times
print(f"rfft: {proc_time_rfft:.3f} s")
print(f"fft: {proc_time_fft:.3f} s")
print(f"rfft is {proc_time_fft / proc_time_rfft:.2f} times faster than fft")
