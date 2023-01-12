******************************************************************************************************************************************
python-dev-tips, `Slides <https://docs.google.com/presentation/d/1BnezhwUy22DiF72wss8GU_YIMfhjortz-uILdIFGuoM/edit?usp=sharing>`__
******************************************************************************************************************************************

Creating virtual environment and install
========================================

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


Releasing package to PyPi
=========================

This is done through `twine <https://pypi.org/project/twine/>`__:

.. code:: bash

    # inside virtual environment
    (project_env) pip install twine

    # build package
    (project_env) python setup.py sdist bdist_wheel
    # -- create in dist folder

    # upload to test pypi
    (project_env) python -m twine upload  dist/pydevtips-X.X.X.tar.gz
    # -- X.X.X is the version number in setup.py
    # -- enter username and password
    # -- check https://pypi.org/project/pydevtips/X.X.X/


TODO
====

- matplotlib in dev install
- profiling to compare RFFT and FFT
- unit test to check that they are equal when signal is real
- example file with hydra
- pypi 
- manifest file to not include file in package
- GitHub actions
- documentation if time
