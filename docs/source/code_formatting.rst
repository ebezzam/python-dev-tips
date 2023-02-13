Code formatting
===============

Code formatting is important for readability. It allows you to write code that
is easy to follow (for your future self as much as others), and (least importantly) 
adheres to the `PEP8 <https://www.python.org/dev/peps/pep-0008/>`_ standard.

However, remembering all the rules and manually formatting your code is not
how we want to spend our time as developers. To this end, there are several
tools that can help us with this task. The ones we use are:

* `Black <https://github.com/psf/black>`_ which will reformat your code 
  in-place to conform to the PEP8 standard.
* `Flake8 <https://flake8.pycqa.org/en/latest/>`__ which is a *linter* that 
  will check your code for errors and style violations, but not reformat it. For
  example, for me it has identified code where I have unused variables or 
  scripts / functions that are too long.

While you can use these tools manually, it is much more convenient to use them
as pre-commit hooks. This means that before you commit your code, these tools
will be run automatically. If they find any errors, the commit will be aborted
and you will have to fix the errors before you can commit again. Pre-commit
helps you to automate this process and avoid commits that do not conform to
the PEP8 standard (and commits that are just for formatting).

A few files are needed to setup pre-commit hooks:

* `.pre-commit-config.yaml <https://github.com/ebezzam/python-dev-tips/blob/main/.pre-commit-config.yaml>`_: This file contains the configuration for the
  pre-commit hooks. It specifies which tools to use, and how to use them.
* `.flake8 <https://github.com/ebezzam/python-dev-tips/blob/main/.flake8>`_: This file contains the configuration for Flake8. It specifies 
  e.g. which errors to ignore, and which line length to use. 
* `pyproject.toml <https://github.com/ebezzam/python-dev-tips/blob/main/pyproject.toml>`_: This file contains the configuration for Black. It 
  specifies e.g. which line length to use.

You can then install the pre-commit hooks for your project by running the 
following commands:

.. code:: bash

    # inside virtual environment
    (project_env) pip install pre-commit
    (project_env) pip install black

    # Install git hooks
    (project_env) pre-commit install
    # pre-commit installed at .git/hooks/pre-commit
