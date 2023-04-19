"""
Example of vectorizing operations with `numpy`

Blog: https://towardsdatascience.com/the-art-of-speeding-up-python-loop-4970715717c
Blog: https://shihchinw.github.io/2019/03/performance-tips-of-numpy-ndarray.html

"""

import numpy as np
import time
from scipy.fft import rfft2  # depending on version of `numpy` float32 may not output complex64


n_trials = 100

""" Adding two vectors, compare nonvectorized and vectorized operations """
print("\n-- Adding two vectors")
n = 1000
a = np.random.randn(n)
b = np.random.randn(n)

# Nonvectorized
start = time.perf_counter()
for _ in range(n_trials):
    c = []
    for i in range(len(a)):
        c.append(a[i] + b[i])
    c = np.array(c)
nonvectorized_time = (time.perf_counter() - start) / n_trials
print(f"Nonvectorized time: {nonvectorized_time} seconds")

# Vectorized
start = time.perf_counter()
for _ in range(n_trials):
    c_vec = a + b
vectorized_time = (time.perf_counter() - start) / n_trials
print(f"Vectorized time: {vectorized_time} seconds")

assert np.allclose(c, c_vec)
print(f"Speed-up: {nonvectorized_time / vectorized_time}")


""" Broadcasting """
print("\n-- Broadcasting")
n = 100
a = np.random.randn(n, n)
b = np.random.randn(n)  # add a row vector to each row of a

# Nonvectorized
start = time.perf_counter()
for _ in range(n_trials):
    c = []
    for i in range(len(a)):
        c.append(a[i] + b)
    c = np.array(c)
nonvectorized_time = (time.perf_counter() - start) / n_trials
print(f"Nonvectorized time: {nonvectorized_time} seconds")

# Vectorized
start = time.perf_counter()
for _ in range(n_trials):
    c_vec = a + b[np.newaxis, :]
vectorized_time = (time.perf_counter() - start) / n_trials
print(f"Vectorized time: {vectorized_time} seconds")

assert np.allclose(c, c_vec)
print(f"Speed-up: {nonvectorized_time / vectorized_time}")


""" Apply function along axis (if memory allows) """
print("\n-- Apply function (e.g. fft) along axis")
n = 512
n_signals = 500
a = np.random.randn(n, n_signals)

# Nonvectorized
start = time.perf_counter()
for _ in range(n_trials):
    c = []
    for i in range(n_signals):
        c.append(np.fft.fft(a[:, i]))
    c = np.array(c)
nonvectorized_time = (time.perf_counter() - start) / n_trials
print(f"Nonvectorized time: {nonvectorized_time} seconds")

# Vectorized
start = time.perf_counter()
for _ in range(n_trials):
    c_vec = np.fft.fft(a, axis=0)
vectorized_time = (time.perf_counter() - start) / n_trials
print(f"Vectorized time: {vectorized_time} seconds")

assert np.allclose(c.T, c_vec)
print(f"Speed-up: {nonvectorized_time / vectorized_time}")


""" Using smaller data types if possible """
print("\n-- Using smaller data types if possible")

# float64
a = np.random.randn(512, 512)
start = time.perf_counter()
for _ in range(n_trials):
    # b = np.fft.rfft2(a)
    b = rfft2(a)
float64_time = (time.perf_counter() - start) / n_trials
print(f"float64 time: {float64_time} seconds")

# float32
a32 = a.astype(np.float32)
start = time.perf_counter()
for _ in range(n_trials):
    # b32 = np.fft.rfft2(a32)
    b32 = rfft2(a32)
float32_time = (time.perf_counter() - start) / n_trials
print(f"float32 time: {float32_time} seconds")

assert b32.dtype == np.complex64

print(f"Speed-up: {float64_time / float32_time}")
