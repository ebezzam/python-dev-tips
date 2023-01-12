******************************************************************************************************************************************
python-dev-tips, `Slides <https://docs.google.com/presentation/d/1BnezhwUy22DiF72wss8GU_YIMfhjortz-uILdIFGuoM/edit?usp=sharing>`__
******************************************************************************************************************************************

Tutorial first given at ENS Ulm (January 2023) on how to develop a Python package (scientific computing perspective).

.. contents:: **Table of Contents**

Creating virtual environment and local install
==============================================

With `Anaconda <https://www.anaconda.com/>`__ (recommended). 
After installing Anaconda or `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`__ (light version), create a new environment:

.. code:: bash

    # create new environment, press enter to accept
    conda create -n project_env python=3.9

    # view available environments
    conda info --envs

    # activate environment
    conda activate project_env

    # instal package locally
    (project_env) pip install -e .

    # deactivate environment
    (project_env) conda deactivate


For machines really light on memory (e.g. Raspberry Pi) use 
`Virtualenv <https://virtualenv.pypa.io/en/latest/>`__:

.. code:: bash

    # install library if not already
    pip install virtualenv

    # create virtual environment (creates folder called project_env)
    python3 -m venv project_env

    # activate virtual environment
    source project_env/bin/activate

    # instal package locally
    (project_env) pip install -e .

    # deactivate virtual environment
    (project_env) deactivate


Code formatting
===============

Through pre-commit hooks:

.. code:: bash

    # inside virtual environment
    (project_env) pip install pre-commit
    (project_env) pip install black

    # Install git hooks
    (project_env) pre-commit install
    # pre-commit installed at .git/hooks/pre-commit


Testing
=======

Write tests in the `tests` folder as function that begin with `test_`.

To run tests (install `pytest <https://docs.pytest.org/en/stable/>`__ first if not already done):

.. code:: bash

    # inside virtual environment
    (project_env) pip install pytest

    # run tests
    (project_env) pytest

To run a specific test:

.. code:: bash

    # inside virtual environment
    (project_env) pytest tests/test_fftconvolve.py::test_fft


Releasing new version and deploying to PyPi
===========================================

Uploading to PyPi is done via `twine <https://pypi.org/project/twine/>`__.

In the steps below and **after merging to** ``main``, replace "X.X.X" with the appropriate version number.

See `Semantic Versioning <https://semver.org/>`__ for recommendations on picking version numbers.

.. code:: bash

    # inside virtual environment
    (project_env) pip install twine

    # edit version in setup
    # build package
    (project_env) python setup.py sdist bdist_wheel
    # -- creates zip in dist folder

    # upload to pypi
    (project_env) python -m twine upload  dist/pydevtips-X.X.X.tar.gz
    # -- X.X.X is the version number in setup.py
    # -- enter username and password
    # -- check https://pypi.org/project/pydevtips/X.X.X/

    # new release on GitHub
    git tag -a X.X.X -m "version X.X.X"
    git push origin X.X.X

On `GitHub <https://github.com/ebezzam/python-dev-tips/tags>`__ set the new tag 
by (1) clicking  (the rightmost) "..." and selecting "Create release" and (2) at the bottom 
pressing "Publish release".


TODO
====

- joblib example in profile
- github page
- point out features in scripts: object-oriented, asserts, tqdm, type hints
- matplotlib, pytest, black in dev install
- example file with hydra
- manifest file to not include file in package
- GitHub actions for releasing to PyPi when changes to version
- documentation (autodoc)
- adding badges to README
