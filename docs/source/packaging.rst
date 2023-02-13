Packaging
=========

Packaging your code is the process of organizing your project files
so that it can be built and installed by other users. As well as
your source code, there are a few files that are needed by
`setuptools <https://setuptools.pypa.io/en/latest/>`__ -- the 
commonly-used Python library for packaging code that can be 
installed with `pip <https://pypi.org/project/pip>`_ and uploaded
to `PyPI <http://pypi.org/>`_.


Project structure
-----------------

A typical (minimal) file structure for a Python project to be 
"pip-installable" looks like so:

.. code::

    project/
    |-- __init__.py
    |-- code.py
    |-- # other files
    README.rst     # or .md, .txt, etc
    setup.py

where:

* The folder ``project`` contains your source code files and
  an ``__init__.py``, which could be empty.
* ``README.rst`` which is not necessary for building the Python, but 
  is often the first file that new users will look into to learn
  about the project, how to install it, and how to use it. On GitHub
  and PyPI, it will be rendered as the "homepage" for your project. 
* ``setup.py`` is a configuration file for installing the project. More
  on that :ref:`below <setup.py>`.

The project can then be built (locally) with the command below:

.. code:: bash

    (project_env) pip install -e .

The project can be imported in your Python script as:

.. code:: Python

    import project


setup.py
--------

The ``setup.py`` is used to configure the project packaging by ``setuptools``.
Below is the ``setup.py`` file for this "dummy" project.

.. literalinclude:: ../../setup.py
    :caption: setup.py
    :linenos:

* Lines 3-4: use the contents of ``README.rst`` to be rendered for the homepage
  on PyPI. *Be sure to set the correct file extension and set Line 13
  accordingly*.
* Line 7: specifies the name of the package / in which folder the source code
  is located, such that the package can be installed with ``pip install pydevtips``
  if on PyPI and imported as ``import pydevtips``.
* Line 8: sets the package version, *which should be (typically) modified before
  uploading a new version to PyPI (below)*.
* Line 9-10: for your name and contact info.
* Line 20-26: specifies the Python version and package dependencies.

Releasing new version and deploying to PyPI
-------------------------------------------

Uploading your project to PyPI is done via the `twine <https://pypi.org/project/twine/>`__
library.

.. code:: bash

    # inside virtual environment
    (project_env) pip install twine

In the steps below, replace "X.X.X" with the appropriate version number, *matching the one
in your* ``setup.py`` *file*. See `Semantic Versioning <https://semver.org/>`__ for
recommendations on picking version numbers.

.. code:: bash

    # edit version in `setup.py`
    # build package
    (project_env) python setup.py sdist bdist_wheel
    # -- creates zip in dist folder

    # upload to pypi
    (project_env) python -m twine upload  dist/pydevtips-X.X.X.tar.gz
    # -- X.X.X is the version number in setup.py
    # -- enter username and password
    # -- check https://pypi.org/project/pydevtips/X.X.X/

    # new tag on GitHub
    git tag -a X.X.X -m "version X.X.X"
    git push origin X.X.X

If you project is hosted on GitHub, you can create a new release by:

#. Clicking (the rightmost) "..." dropdown menu (from the `tags page <https://github.com/ebezzam/python-dev-tips/tags>`_).
#. Selecting "Create release". 
#. At the bottom pressing "Publish release".
