import numpy as np
from tqdm import tqdm
import time
from pydevtips.fftconvolve import RFFTConvolve, FFTConvolve


seed = 0
np.random.seed(seed)


# create random signal
n = 1000
signal = np.random.randn(n)

# create filter
filter = np.random.randn(n)

# create FFT objects
rfft_convolver = RFFTConvolve(filt=filter, length=len(signal))
fft_convolver = FFTConvolve(filter=filter, length=len(signal))

# profile
n_trials = 100

# rfft
print("rfft")
rfft_convolved_signal = np.zeros_like(signal)
start_time = time.time()
for _ in tqdm(range(n_trials)):
    rfft_out = rfft_convolver(signal)
proc_time_rfft = (time.time() - start_time) / n_trials

# fft
print("fft")
fft_convolved_signal = np.zeros_like(signal)
start_time = time.time()
for _ in tqdm(range(n_trials)):
    fft_out = fft_convolver(signal)
proc_time_fft = (time.time() - start_time) / n_trials

# fft without initializing
print("fft naive (without initializing)")
for _ in tqdm(range(n_trials)):
    fft_naive_out = np.convolve(signal, filter, mode="full")
proc_time_fft_naive = (time.time() - start_time) / n_trials

# check results
assert np.allclose(rfft_out, fft_out)
assert np.allclose(rfft_out, fft_naive_out)
print(f"rfft: {proc_time_rfft} s")
print(f"fft: {proc_time_fft} s")
print(f"fft naive: {proc_time_fft_naive} s")
print(f"rfft is {proc_time_fft / proc_time_rfft:.2f} times faster than fft")
print(f"fft is {proc_time_fft_naive / proc_time_fft:.2f} times faster than fft naive")
print(f"rfft is {proc_time_fft_naive / proc_time_rfft:.2f} times faster than fft naive")
