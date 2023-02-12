Virtual environments
====================

Virtual environments are a way to isolate your project from the rest of your
system. This is important because it allows you to install packages that are
specific to your project, without affecting the rest of your system. 

Creating an environment
-----------------------

There are several ways to create virtual environments. The most popular 
(and recommended) is with `Anaconda <https://www.anaconda.com/>`__.
After installing Anaconda or `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`__ (light version), 
you create a new environment like so:

.. code:: bash

    # create new environment, press enter to accept
    conda create -n project_env python=3.9

    # view available environments
    conda info --envs

    # activate environment
    conda activate project_env

    # deactivate environment
    (project_env) conda deactivate


For machines really light on memory (e.g. Raspberry Pi), you can use 
`Virtualenv <https://virtualenv.pypa.io/en/latest/>`__:

.. code:: bash

    # install library if not already
    pip install virtualenv

    # create virtual environment (creates folder called project_env)
    python3 -m venv project_env

    # activate virtual environment
    source project_env/bin/activate

    # deactivate virtual environment
    (project_env) deactivate

Note that when the virtual environment is activated, it will
typically appear in parenthesis in the command line.

Sharing your environment
------------------------

Inside your virtual environment, you can install packages specific to 
your project. It is highly recommended to keep track of the packages
you install, so that others (including yourself) can easily recreate 
the same virtual environment. There are three common approaches to 
storing and keeping track of packages:

* ``requirements.txt``: This is a simple text file that lists all the
  packages you have installed. You can create this file by running:

  .. code:: bash

      (project_env) pip freeze > requirements.txt

  You can then install all the packages in this file by running:

  .. code:: bash

      (project_env) pip install -r requirements.txt


* ``environment.yml``: This is a YAML file that lists all the packages you have installed. You can create this file by running:
    
    .. code:: bash
    
        (project_env) conda env export > environment.yml
    
    You can simulatenously create the environment and install all the packages in this file by running:
    
    .. code:: bash
    
        conda env create -f environment.yml

    You can check that the environment was created by running:

    .. code:: bash
    
        conda env list

    The the name of the environment is specified at the top of ``environment.yml``.
    
    Note that this approach is specific to Anaconda / Miniconda. More 
    information can be found 
    `here <https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html>`_.


* A more involved approach to package your project, such that it can be installed via ``pip`` with the necessary dependencies:

    .. code:: bash
    
        # local install
        (project_env) pip install -e .

        # if on PyPi
        (project_env) pip install <PACKAGE_NAME>

    This approach is discussed in PACKAGING.
