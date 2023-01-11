# python-dev-tips

## Creating virtual environment

With `Anaconda <https://www.anaconda.com/>`__ (recommended). 
After installing Anaconda or `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`__ (light version), create a new environment:

.. code:: bash

    # create new environment, press enter to accept
    conda create -n project_env python=3.9

    # view available environments
    conda info --envs

    # activate environment
    conda activate project_env

    # deactivate environment
    conda deactivate


For machines really light on memory (e.g. Raspberry Pi) use 
`Virtualenv <https://virtualenv.pypa.io/en/latest/>`__:

.. code:: bash

    # install library if not already
    pip install virtualenv

    # create virtual environment (creates folder called project_env)
    python3 -m venv project_env

    # activate virtual environment
    source project_env/bin/activate

    # deactivate virtual environment
    deactivate
