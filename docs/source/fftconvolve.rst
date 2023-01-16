Class example
=============

.. GENERATE DOCUMENTATION FOR ALL CLASSES
.. .. automodule:: pydevtips.fftconvolve
..     :member-order: bysource
..     :show-inheritance:
..     :special-members: __init__, __call__


.. GENERATE INDIVIDUALLY WITH CUSTOM TEXT

There are two classes in this module for performing convolution in the frequency domain with a fixed filter.

.. autosummary::
    pydevtips.fftconvolve.RFFTConvolve
    pydevtips.fftconvolve.FFTConvolve

Both inherit from the base class :class:`pydevtips.fftconvolve.FFTConvolveBase`, 
overwriting the abstract methods: :func:`pydevtips.fftconvolve.FFTConvolveBase._compute_filter_frequency_response` and 
:func:`pydevtips.fftconvolve.FFTConvolveBase.__call__`.

RFFTConvolve
------------

.. autoclass:: pydevtips.fftconvolve.RFFTConvolve
    :member-order: bysource
    :show-inheritance:
    :special-members: __init__, __call__

FFTConvolve
-----------

.. autoclass:: pydevtips.fftconvolve.FFTConvolve
    :member-order: bysource
    :show-inheritance:
    :special-members: __init__, __call__


FFTConvolveBase
---------------

.. autoclass:: pydevtips.fftconvolve.FFTConvolveBase
    :member-order: bysource
    :show-inheritance:
    :members:
    :undoc-members:
    :special-members: __init__, __call__
    :private-members: _compute_filter_frequency_response
