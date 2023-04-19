"""
Example of using `joblib` to parallelize a loop.

pip install joblib

"""


import numpy as np
import time

try:
    from joblib import Parallel, delayed
except ImportError:
    print("Install joblib to run this example")
    exit()


def f(seed, n, proc_time):
    np.random.seed(seed)
    x = np.random.randn(n)
    time.sleep(proc_time)  # simulate some long running process
    return np.fft.fft(x)


if __name__ == "__main__":

    # Create a list of inputs
    n = 2048
    n_exp = 100
    proc_time = 0.2
    n_cpu = 6

    # Compare processing time for serial and parallel processing

    # Serial processing
    start = time.perf_counter()
    outputs_ser = []
    for seed in range(n_exp):
        outputs_ser.append(f(seed, n, proc_time))
    serial_time = time.perf_counter() - start
    print(f"Serial processing took {serial_time} seconds")

    # Parallel processing
    start = time.perf_counter()
    outputs_par = Parallel(n_jobs=n_cpu)(delayed(f)(seed, n, proc_time) for seed in range(n_exp))
    parallel_time = time.perf_counter() - start
    print(f"Parallel processing took {parallel_time} seconds")

    # Speed-up
    print(f"Speed-up: {serial_time / parallel_time}")
