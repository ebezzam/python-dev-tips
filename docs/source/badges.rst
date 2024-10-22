Badges
======

Adding badges to your GitHub repository and documentation amounts to simply adding an image.

For example, in a `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__ file:

.. code:: rst

    .. image:: https://readthedocs.org/projects/pydevtips/badge/?version=latest
        :target: http://pydevtips.readthedocs.io/en/latest/
        :alt: Documentation Status

which when rendered will make the following badge:

.. image:: https://readthedocs.org/projects/pydevtips/badge/?version=latest
    :target: http://pydevtips.readthedocs.io/en/latest/
    :alt: Documentation Status

You can also create `badges from GitHub Actions <https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge>`__.

.. code:: rst

    .. image:: https://github.com/ebezzam/python-dev-tips/actions/workflows/poetry.yml/badge.svg
        :target: https://github.com/ebezzam/python-dev-tips/blob/main/.github/workflows/poetry.yml
        :alt: Unit tests and formatting

.. image:: https://github.com/ebezzam/python-dev-tips/actions/workflows/poetry.yml/badge.svg
    :target: https://github.com/ebezzam/python-dev-tips/blob/main/.github/workflows/poetry.yml
    :alt: Unit tests and formatting

Finally, you can use `Badgen <https://badgen.net/>`__ or `Shields.io <https://shields.io/badges>`__ to create custom badges.

