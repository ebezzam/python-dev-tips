Clean(er) code
==============

Below are a few tips for writing clean(er) code.

Code formatting
---------------

Code formatting is important for readability. It allows you to write code that
is easy to follow (for your future self as much as others), and (least importantly) 
adheres to the `PEP8 <https://www.python.org/dev/peps/pep-0008/>`_ standard.

However, remembering all the rules and manually formatting your code is not
how we want to spend our time as developers. To this end, there are several
tools that can help us with this task. The ones we use are:

* `Black <https://github.com/psf/black>`_ which will reformat your code 
  in-place to conform to the PEP8 standard.
* `Flake8 <https://flake8.pycqa.org/en/latest/>`_ which is a *linter* that 
  will check your code for errors and style violations, but not reformat it. For
  example, for me it has identified code where I have unused variables or 
  scripts / functions that are too long.
* `isort <https://pycqa.github.io/isort/>`_ which will sort your imports 
  alphabetically and group them by type.

There are many alternatives for there tools. An increasingly popular alternative
is `ruff <https://docs.astral.sh/ruff//>`_, which is written in Rust and is meant
to replace Flake8, Black, and isort.

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
* `pyproject.toml <https://github.com/ebezzam/python-dev-tips/blob/main/pyproject.toml>`_: This file contains the configuration for Black and isort. It 
  specifies e.g. which line length to use.

You can then install the pre-commit hooks for your project by running the 
following commands:

.. code:: bash

    # inside virtual environment
    # -- black, flake8, isort are in the dev group
    (project_env) poetry install --with dev

    # -- if not using Poetry
    # (project_env) pip install pre-commit black flake8 isort

    # Install git hooks
    (project_env) pre-commit install
    # pre-commit installed at .git/hooks/pre-commit

More pre-commit hooks are available provided by `Poetry <https://python-poetry.org/docs/pre-commit-hooks/>`_.


Avoiding long ``if-else`` statements with object instantiation
--------------------------------------------------------------

In :ref:`Reproducible examples<Reproducible examples>` we presented Hydra for separating configuration from code.
Another cool feature of Hydra is `object instantiating <https://hydra.cc/docs/advanced/instantiate_objects/overview/>`_.
Imagine you want to try different optimizers for your Deep Neural Network (DNN) or you want to try different DNNs in the same pipeline.
Instead of doing ``if-else`` statements, you write one line of code and let Hydra choose the
appropriate object class based on your configuration. See the script
`examples/real_convolve.py <https://github.com/ebezzam/python-dev-tips/blob/main/examples/real_convolve.py>`_
for the example.

.. code-block:: python

    @hydra.main(version_base=None, config_path="configs", config_name="defaults")
    def main(config):
        # instantiate object from config
        signal = instantiate(config.signal)
        # application specific choice of object class

``instantiate`` function from ``hydra.utils`` allows you to define an object in a YAML file 
without being tied to a particular class. To do this, you need to define ``_target_`` in 
your config (see configs in ``configs/signal``) and object initialization arguments. Object class 
can be either defined in your project (``configs/signal/ExampleZeros``, ``configs/signal/ExampleCustom``)
or taken from a package (``configs/signal/ExampleNumpy``).

Note that here we use another Hydra feature: config grouping and splitting. Instead of writing 
configurations for all objects in the main config and copying configuration files, we create a sub-directory ``signal``,
where all ``signal`` configs are defined. Now we can run the main config with the ``signal`` of
our choice simply by specifying it in the command line. For example, ``python examples/real_convolve.py signal=ExampleNumpy``
or ``python examples/real_convolve.py signal=ExampleZeros``.

If we need to define some of the arguments inside the code before creating an object, we can pass them directly to the ``instantiate`` function.
For example, we did not define ``signal_len`` in the ``signal`` configuration file and passed it by hand:
``signal = instantiate(config.signal, config.signal_len)``. This is especially useful when you have positional-only arguments
like ``numpy.random.randn`` in our example. Note that we can both define arguments in the configuration file and pass new ones to ``instantiate`` like we did for
``ExampleCustom``.

Object instantiating is recursive, i.e. some of the arguments of the class can also be
defined using ``_target_`` and they will be created automatically. For example,
``python examples/real_convolve.py signal=ExampleCustom +signal/transform=power`` defines the ``transform`` argument of
the ``ExampleCustom`` class as the ``PowerTransform`` class. The ``+signal/transform=power`` in the command line 
means adding the ``transform`` argument to the current ``signal`` configuration from the ``power.yaml`` config defined
in ``configs/signal/transform``. That is, you can have sub-sub-directories. The default values from sub-sub-directories
can also be changed in the command-line: ``python examples/real_convolve.py signal=ExampleCustom +signal/transform=power signal.transform.pow=3``
