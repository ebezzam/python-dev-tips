import numpy as np
from abc import abstractmethod


class FFTConvolveBase:
    """Abstract class for FFT convolve."""

    def __init__(self, filter, length) -> None:
        """
        Base class for creating a convolver that uses the same filter.

        Parameters
        ----------
        filter : :py:class:`~numpy.ndarray`
            Filter to convolve with. Must be real.
        length : int
            Length of the signal to convolve with.
        """

        assert isinstance(filter, np.ndarray)
        self.filter = filter
        self.signal_length = length
        self.pad_length = len(filter) + length - 1
        self.filter_frequency_response = self._compute_filter_frequency_response()

    @abstractmethod
    def _compute_filter_frequency_response(self) -> np.ndarray:
        """
        Compute the filter frequency response.

        Parameters
        ----------
        filter : :py:class:`~numpy.ndarray`
            Filter to compute the frequency response for.

        Returns
        -------
        filter_frequency_response : :py:class:`~numpy.ndarray`
            Filter frequency response.
        """
        raise NotImplementedError

    @abstractmethod
    def __call__(self, signal) -> np.ndarray:
        """Apply the filter to the signal, in the frequency domain."""
        pass


class RFFTConvolve(FFTConvolveBase):
    """Real FFT convolve."""

    def __init__(self, filter, length) -> None:
        """
        Create convolver that uses a real-valued filter.

        Parameters
        ----------
        filter : :py:class:`~numpy.ndarray`
            Filter to convolve with. Must be real.
        length : int
            Length of the signal to convolve with.
        """

        # check real
        assert np.isreal(filter).all()
        super(RFFTConvolve, self).__init__(filter, length)

    def _compute_filter_frequency_response(self):
        """Compute the filter frequency response."""
        return np.fft.rfft(self.filter, n=self.pad_length)

    def __call__(self, signal) -> np.ndarray:
        """
        Apply the real-valued filter to the signal, in the frequency domain.

        Parameters
        ----------
        signal : :py:class:`~numpy.ndarray`
            Signal to convolve with. Must be real.

        Returns
        -------
        result : :py:class:`~numpy.ndarray`
            Convolved signal.
        """
        signal_frequency_response = np.fft.rfft(signal, n=self.pad_length)
        return np.fft.irfft(
            signal_frequency_response * self.filter_frequency_response, n=self.pad_length
        )


class FFTConvolve(FFTConvolveBase):
    """General FFT convolve."""

    def __init__(self, filter, length) -> None:
        """
        Create convolver that uses a fixed filter.

        Parameters
        ----------
        filter : :py:class:`~numpy.ndarray`
            Filter to convolve with. Must be real.
        length : int
            Length of the signal to convolve with.
        """
        super(FFTConvolve, self).__init__(filter, length)

    def _compute_filter_frequency_response(self):
        """Compute the filter frequency response."""
        return np.fft.fft(self.filter, n=self.pad_length)

    def __call__(self, signal) -> np.ndarray:
        """
        Apply the filter to the signal, in the frequency domain.

        Parameters
        ----------
        signal : :py:class:`~numpy.ndarray`
            Signal to convolve with.

        Returns
        -------
        result : :py:class:`~numpy.ndarray`
            Convolved signal.
        """
        signal_frequency_response = np.fft.fft(signal, n=self.pad_length)
        return np.fft.ifft(
            signal_frequency_response * self.filter_frequency_response, n=self.pad_length
        )
