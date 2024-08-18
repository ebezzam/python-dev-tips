***************************************
pydevtips: Python Development Tips
***************************************

.. image:: https://readthedocs.org/projects/pydevtips/badge/?version=latest
    :target: http://pydevtips.readthedocs.io/en/latest/
    :alt: Documentation Status


.. image:: https://github.com/ebezzam/python-dev-tips/actions/workflows/python.yml/badge.svg
    :target: https://github.com/ebezzam/python-dev-tips/blob/main/.github/workflows/python.yml
    :alt: Unit tests and formatting

.. image:: https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white
    :target: https://youtu.be/okxaTuBdDuY?si=5AQ5pOpmsCH8BLt2&t=3803
    :alt: Recording

.. image:: https://img.shields.io/badge/Google_Slides-yellow
    :target: https://docs.google.com/presentation/d/1D1_JywMl2rjaeuVzpykPBOJsDIuwQKGOJB4EFZjej2s/edit#slide=id.g2eaa4b61f15_0_1346
    :alt: Slides


.. |ss| raw:: html

   <strike>

.. |se| raw:: html

   </strike>


Reproducibility is important for software: *if it's not reproducible, 
it's not useful*. Even if you don't plan on sharing your code, imagine 
coming back to a project after a few weeks, or having
to install it on a new machine. You'll be all the more thankful to your
past self if you have a clear way to install and run your code.

This repository is a collection of tips and tricks for developing stable 
and reproducible Python code. There is a slight focus on scientific 
computing, but the general principles can apply to most Python projects.
If you're reading this from `GitHub <https://github.com/ebezzam/python-dev-tips>`_, please check out the 
`documentation <https://pydevtips.readthedocs.io/en/latest/>`_ for a
more in-depth explanation of the topics covered.

The intended audience is myself (as I often find myself going to past
projects to find how I did something!), but also for students and 
anyone who is interested in learning some new tricks or even 
sharing their own! I try to follow the principles laid out here on
development and reproducibility, so feel free to point out any lapses
or suggest improvements, either by opening an issue or pull request.

As is typical in open source, there are many ways to do the same thing.
But hopefully this gives you a starting point. Feel free to pick and 
choose the features that you like. This flexibility is one of the best
(and worst parts) of open source. Some of the things we cover:

* Virtual environments.
* Version control.
* Reproducible examples.
* Documentation.
* Code formatting.
* Unit tests and continuous integration.
* Packaging and distribution.
* Remove development.
* Creating and sharing datasets with Hugging Face.

The accompanying 
`slides <https://docs.google.com/presentation/d/1D1_JywMl2rjaeuVzpykPBOJsDIuwQKGOJB4EFZjej2s/edit#slide=id.g2eaa4b61f15_0_1346>`__ 
and `video <https://youtu.be/okxaTuBdDuY?si=5AQ5pOpmsCH8BLt2&t=3803>`__
are from a tutorial given at LauzHack's `Deep Learning Bootcamp <https://github.com/LauzHack/deep-learning-bootcamp>`__. 
Feel free to modify and use it for your own purposes.

.. note::

    A good amount of this documentation and code is written with `GitHub 
    Copilot <https://github.com/features/copilot>`_, which I highly recommend for development. If you don't like
    writing documentation, it is a great way to get started as it is able to 
    understand the functionality of your code and produce meaningful text to describe it. 
    It should be used be used with caution, |ss| *but it can be a great tool for getting started* |se|
    and you often you need to make a few tweaks (*like the previous repetition*).
    But it's a huge time-saver!

Installation
============

This "dummy" package can be installed with pip:

.. code:: bash

    pip install pydevtips

Or from source, e.g. with Anaconda / Miniconda:

.. code:: bash

    # create new environment, press enter to accept
    conda create -n project_env python=3.11

    # view available environments
    conda info --envs

    # activate environment
    conda activate project_env

    # install package locally
    (project_env) pip install -e .

    # run tests
    # - one time: pip install pytest
    (project_env) pytest

    # deactivate environment
    (project_env) conda deactivate

Examples
========

Examples can be found in the ``examples`` and ``notebooks`` folders.
Scripts from the ``examples`` folder should be run from the root of the
repository, e.g.:

.. code:: bash

    python examples/real_convolve.py

Parameter setting is done with `hydra <https://hydra.cc/>`_. More on that
in the :ref:`Reproducible examples<Reproducible examples>` section of the 
documentation.


TODO
====

- numba: https://numba.pydata.org/
- picking a license
- change documentation links to main branch
- github page
- point out features in scripts: object-oriented, asserts, tqdm, type hints
- matplotlib, pytest, black in dev install
- manifest file to not include file in package
- GitHub actions for releasing to PyPi when changes to version
- pytorch compatible
- Cython / C++
