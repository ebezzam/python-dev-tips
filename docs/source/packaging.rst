Packaging
=========

Project structure
-----------------

Folder with package subfolder and ``setup.py``

``setup.py``
------------

Specifying metadata and packages.

Releasing new version and deploying to PyPi
-------------------------------------------

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

    # new tag on GitHub
    git tag -a X.X.X -m "version X.X.X"
    git push origin X.X.X

On `GitHub <https://github.com/ebezzam/python-dev-tips/tags>`__ create a new release by:

#. Clicking (the rightmost) "..." dropdown menu.
#. Selecting "Create release". 
#. At the bottom pressing "Publish release".