Documentation
=============

We will be using a `Sphinx <https://www.sphinx-doc.org/en/master/>`__ to generate documentation from 
docstrings that are written within code. Docstrings are long-form
comments beneath class and functions declaration that typically describe:

- What the function or class does.
- Its inputs and their data types.
- Its outputs and their data types.

For example:

.. code:: Python

    def add(a, b):
        """
        Add two integers.
        
        Parameters
        ----------
        a : int
            First integer.
        b : int
            Second integer.

        Returns
        -------
        result : int
            Sum of inputs.

        """

        assert isinstance(a, int)
        assert isinstance(b, int)
        return a + b

Which will be rendered as :func:`pydevtips.utils.add`.

Initial setup
-------------

So you've diligently written your docstrings (or used GitHub Copilot!), and you 
want to generate your documentation.

Here are some recommended steps to get started with Sphinx:

#. Create a lightweight virtual environment for building the documentation. This can save a lot of time when building and publishing documentation remotely, as we'll show with `ReadTheDocs <https://readthedocs.org/>`__.

    .. code:: bash
        
        # create new environment, press enter to accept
        conda create -n docs_env python=3.9

        # activate environment
        conda activate docs_env

        # install requirements stored in `docs` 
        # (may differ from our file depending on your needs)
        (docs_env) cd docs
        (docs_env) pip install -r requirements.txt

#. Inside your virtual environment, run ``sphinx-quickstart`` to creates a lot of the boilerplate configurations. This will guide you through a set of questions, such as your project details. We recommend creating separate ``source`` and ``build`` directories.
#. Build the documentation, e.g. with ``make html``.
#. Open ``docs/build/html/index.html`` in a browser to see your initial documentation!

Editing your documentation
--------------------------

The ``index.rst`` file will serve as the "homepage" for your documentation (built into ``index.html``).
Typically, people have the same content as their README. Before you copy-and-paste
the contents (!), you can directly insert the contents with the following line.

.. code:: rst

    .. include:: ../../README.rst

.. note::

    `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__
    is the default plaintext markup language used by Sphinx. At this point, you may be thinking:
    *"But my README is a Markdown file (.md)..."*. While there are `tools <https://www.sphinx-doc.org/en/master/usage/markdown.html>`__
    to make Sphinx compatible with Markdown, I think you will save yourself more headaches to simply
    switch to reStructuredText. There are also `online tools <https://cloudconvert.com/md-to-rst>`__
    to help you with that.


Adding new pages to your documentation amount to:

#. Creating new RST files.
#. Including them in your ``index.rst`` file.
#. Rebuilding the documentation, e.g. with ``make html``.

You may also need to edit the ``conf.py`` file to use different features.
Check out our `index.rst <https://raw.githubusercontent.com/ebezzam/python-dev-tips/feat/docs/docs/source/index.rst>`__
and `conf.py <https://github.com/ebezzam/python-dev-tips/blob/feat/docs/docs/source/conf.py>`__
files for example configurations.


You can do a clean build of your documentation with the following commands:

.. code:: bash

    make clean
    make html


Pro-tips
--------

* Changing to the ReadTheDocs theme inside `conf.py <https://github.com/ebezzam/python-dev-tips/blob/ec6b15c6718b96e2c1a00496d2cf7005755d006c/docs/source/conf.py#L75>`__.
* `Intersphinx <https://docs.readthedocs.io/en/stable/guides/intersphinx.html>`__ for linking to other documentations.
  In the ``conf.py`` file: `add <https://github.com/ebezzam/python-dev-tips/blob/ec6b15c6718b96e2c1a00496d2cf7005755d006c/docs/source/conf.py#L43>`__
  the Sphinx extension, and `link <https://github.com/ebezzam/python-dev-tips/blob/ec6b15c6718b96e2c1a00496d2cf7005755d006c/docs/source/conf.py#L54>`__
  to the other documentation. Inside your documentation you can link to the other library, e.g.
  for data types:

  .. code:: Python

    ...

    """
    Parameters
    ----------
    filter : :py:class:`~numpy.ndarray`
    """

    ...

  which renders as in :func:`pydevtips.fftconvolve.RFFTConvolve.__init__` 
  with a clickable link to NumPy's documentation.
* `Mock modules <https://github.com/ebezzam/python-dev-tips/blob/ec6b15c6718b96e2c1a00496d2cf7005755d006c/docs/source/conf.py#L24>`__ to keep your documentation virtual environment light.
* `Add the path <https://github.com/ebezzam/python-dev-tips/blob/feat/docs/docs/source/conf.py#L22>`__ 
  to your package, so that it doesn't have to be installed (again keeping your documentation environment light!).
* `Automate year <https://github.com/ebezzam/python-dev-tips/blob/ec6b15c6718b96e2c1a00496d2cf7005755d006c/docs/source/conf.py#L32>`__.


Publishing
----------

With a set of HTML files, there are many ways to publish your documentation online.
We present one approach through `ReadTheDocs <https://readthedocs.org/>`__ (RTD), which is
free and very popular among Python developers. Another popular free options is through
`GitHub Pages <https://pages.github.com/>`__. I prefer RTD to not have the GitHub username or
organization in the documentation URL.

To publish on RTD:

#. Make an account: https://readthedocs.org/accounts/signup/
#. Import a project from the `dashboard <https://readthedocs.org/dashboard/>`__. There are two ways to do this: (1) linking your GitHub account and selecting one of your **public** repositories, or (2) importing the project manually. When linking to GitHub, the documentation is re-built whenever there are changes to the selected branch.

You can (optionally) define a `.readthedocs.yaml <>`__ 
file to ensure a build environment as close as possible to your local machine.
