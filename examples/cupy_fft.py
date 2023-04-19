"""

CuPy Example

Installing:
- check Cuda version, e.g. from Terminal run: `nvcc --version` or `nvidia-smi`
- install corresponding version of cupy, e.g. `pip install cupy-cuda11x`

Installation page: https://docs.cupy.dev/en/stable/install.html

"""

from importlib import util
import os
import numpy as np
import scipy
import time

try:
    import cupy as cp
    import cupyx

    CUPY_AVAILABLE = True
except ImportError:
    CUPY_AVAILABLE = False


def get_array_module(x):
    """
    Returns correct numerical module based on input.

    Parameters
    ----------
    x : :obj:`numpy.ndarray` or :obj:`cupy.ndarray`
        Array
    Returns
    -------
    mod : :obj:`func`
        Module to be used to process array (:mod:`numpy` or :mod:`cupy`)
    """
    if CUPY_AVAILABLE:
        return cp.get_array_module(x)
    else:
        return np


def fft2(x):
    """
    Applies correct fft method based on input.

    Parameters
    ----------
    x : :obj:`numpy.ndarray` or :obj:`cupy.ndarray`
        Array

    Returns
    -------
    mod : :obj:`func`
        Module to be used to process array (:mod:`numpy` or :mod:`cupy`)
    """
    if get_array_module(x) == np:
        func = scipy.fft.fft2
    else:
        func = cupyx.scipy.fft.fft2
    return func(x)


# compare FFT computation
n = 1024
n_trials = 100
x = np.random.rand(n, n)

if CUPY_AVAILABLE:
    x_gpu = cp.asarray(x)
    print(x_gpu.device)
else:
    x_gpu = x
    print("Cupy not available. Using numpy instead.")

# numpy
start = time.perf_counter()
for _ in range(n_trials):
    fft2(x)
time_cpu = time.perf_counter() - start
print(f"CPU processing took {time_cpu} seconds")

# cupy
start = time.perf_counter()
for _ in range(n_trials):
    fft2(x_gpu)
time_gpu = time.perf_counter() - start
print(f"GPU processing took {time_gpu} seconds")

# speed-up
print(f"Speed-up: {time_cpu / time_gpu}")
