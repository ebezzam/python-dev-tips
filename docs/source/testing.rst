Testing
=======

*"If debugging is the process of removing bugs, then programming must 
be the process of putting them in."*

*-- Edsger Dijkstra*

But there are ways to make it easier to find bugs and prevent the introduction
of new ones. This is where testing comes in. There are two types that I often use
(discussed below):

* `Assertion tests <https://en.wikipedia.org/wiki/Assertion_(software_development)>`__.
* `Unit tests <https://en.wikipedia.org/wiki/Unit_testing>`__.

We also the discuss the use of `GitHub Actions <https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python>`__.
for continuous integration (CI), namely the software practice of committing code
to a shared repository where the project is built and tested. 


Assertion tests
---------------

Assertion tests are lightweight Boolean checks that you can include in your code
to check that certain conditions are met. For example, you can check that the
input/output is what you expect. If the condition is not met, the
test will fail and code execution will stop.

For example, for :class:`pydevtips.fftconvolve.RFFTConvolve` we check that the
input is indeed real:

.. code:: python

    def __init__(self, filt, length) -> None:
        assert np.isreal(filt).all(), "Filter must be real."
        ...

Unit tests
----------

Unit testing is a method to test small pieces of code, usually functions. With 
a large code base, having unit tests can ensure you don't break core functionality
when you make changes.

In Python, there is the `pytest <https://docs.pytest.org>`__ package
that can be used to write and run unit tests. A common practice is to create a
`tests` folder in the root of your project and write your tests there. The test
functions should begin with `test_` so that ``pytest`` can find them.

For example, for our FFT convolvers -- :class:`pydevtips.fftconvolve.RFFTConvolve`
and :class:`pydevtips.fftconvolve.FFTConvolve` -- we can write unit tests to
check that they are consistent with :py:func:`numpy.convolve`, as done in 
`this script <https://github.com/ebezzam/python-dev-tips/blob/main/tests/test_fftconvolve.py>`__.

To run the unit tests:

.. code:: bash

    # install in virtual environment (if not done already)
    # -- pytest in the dev group
    (project_env) poetry install --with dev

    # run tests
    (project_env) poetry run pytest

    # -- if not using Poetry
    # (project_env) pip install pytest
    # (project_env) pytest

To run a specific test:

.. code:: bash

    # inside virtual environment
    (project_env) poetry run pytest tests/test_fftconvolve.py::test_fft

    # -- if not using Poetry
    # (project_env) pytest tests/test_fftconvolve.py::test_fft


Continuous integration with GitHub Actions
------------------------------------------

Continuous integration (CI) is the practice of automatically building and testing
code whenever a change is made to the codebase. This is useful to ensure that
the codebase is always in a working state.

With GitHub Actions, you can set up a workflow that will run, e.g. on every push to
the repository. This workflow can build the package, run the unit tests, build the
documentions, etc for different versions of Python and operating systems.

Workflows are defined in YAML files in the ``.github/workflows`` folder. For example,
the workflow for this project is defined in `this file <https://github.com/ebezzam/python-dev-tips/blob/main/.github/workflows/poetry.yml>`__,
whose code is shown below:

.. literalinclude:: ../../.github/workflows/poetry.yml
    :caption: poetry.yml
    :linenos:

The workflow performs the following:

* (Lines 5-12) Triggers on pushes and pull requests to the ``main`` branch.
* (Lines 21-24) Performs the test on all combinations of Python versions (3.10 and 3.11) and operating systems
  Ubuntu, Windows, and macOS.
* (Lines 33-43) Installs Python, Poetry, and the package with its dependencies.
* (Lines 44-56) Checks for code formatting and style and errors if it doesn't conform. 
  *Make sure it matches the code formatting you've setup in your project, e.g. via* :ref:`pre-commit hooks <Code formatting>`.
* (Lines 57-58) Runs the unit tests.

An older version of the workflow (not using Poetry but rather ``setup.py`` with 
``setuptools``) can be found below:

.. literalinclude:: ../../.github/workflows/setuptools.yml
    :caption: setuptools.yml (OLD WAY)
    :linenos:

More information on configuring GitHub Actions can be found in `their documentation <https://docs.github.com/en/actions>`__.
