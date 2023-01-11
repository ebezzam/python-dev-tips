import numpy as np
from abc import abstractmethod


class FFTConvolveBase(object):
    def __init__(self, filter) -> None:

        assert isinstance(filter, np.ndarray)
        self.filter = filter
        self.filter_frequency_response = self._compute_filter_frequency_response(filter)

    @abstractmethod
    def _compute_filter_frequency_response(self, filter) -> np.ndarray:
        raise NotImplementedError

    @abstractmethod
    def __call__(self, signal) -> np.ndarray:
        pass


class RFFTConvolve(FFTConvolveBase):
    def __init__(self, filter) -> None:

        # check real
        assert np.isreal(filter)
        super(RFFTConvolve, self).__init__(filter)

    def _compute_filter_frequency_response(self):
        return np.fft.rfft(self.filter)

    def __call__(self, signal) -> np.ndarray:
        signal_frequency_response = np.fft.rfft(signal)
        return np.fft.irfft(signal_frequency_response * self.filter_frequency_response)


class FFTConvolve(FFTConvolveBase):
    def __init__(self, filter) -> None:
        super(FFTConvolve, self).__init__(filter)

    def _compute_filter_frequency_response(self):
        return np.fft.fft(self.filter)

    def __call__(self, signal) -> np.ndarray:
        signal_frequency_response = np.fft.fft(signal)
        return np.fft.ifft(signal_frequency_response * self.filter_frequency_response)
