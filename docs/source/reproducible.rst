Reproducible examples
=====================

Examples and tutorials are a great way to showcase your software. However,
for them to be useful, they need to be reproducible. There are a few ways
you can ensure this is the case:

* Providing clear instructions to install the software and its dependencies, 
  as described :ref:`here<Virtual environments>`.
* Providing clear instructions to run the example and download any necessary data, 
  e.g. in the README or in the home page of the documentation.
* Using notebooks and scripts to showcase your software. See :ref:`below<Using 
  notebooks and scripts>` for more details.
* Using configuration management tools, such as `Hydra <https://hydra.cc/>`_, 
  for separating the configuration of an experiment from the code. See
  :ref:`below<Separating configuration from code>` for more details.

Using notebooks and scripts
---------------------------

Jupyter notebooks are a great way to showcase your software. They allow you to
combine code, text, and images in a single document. However, they can be
prone to errors when not running cells in order. Moreover, they are a pain
when it comes to version control, as they are not plain text files and lend
to many lines of code being changed when only a few lines are actually
changed.

Scripts on the other hand are plain text files and are easy to version
control. Moreover, they are less prone to errors as everything is run in
order, and you are less prone to have missing or incorrectly defined
variables.

Both notebooks and scripts have their place. My recommendation is to:

#. (Optionally) Use notebooks for interactive development.
#. Convert the notebook into a script / scripts + files with utility functions, and continue development.
#. Commit the script(s) to your repository.
#. Create a polished notebook to showcase your software with code, text, and images.
#. Commit the notebook to your repository.

In this manner, you can avoid the annoyances of notebooks with version control,
while still being able to showcase your software in a polished notebook.

Separating configuration from code
----------------------------------

Relying on scripts can still lead to pesky little commits and code duplication,
e.g. when you want to change a parameter or showcase different results from the
same functionality. This is where configuration management tools, such as
`Hydra <https://hydra.cc/>`_, can come in handy.

Hydra allow you to separate the configuration of an experiment from the code, 
through a separate configuration YAML file. This allows you to change the 
parameters inside the configuration file(s) without having to change the code.
This is particularly useful when you want to demonstrate different scenarios, e.g. 
when you have have a script that trains a model and a configuration file that 
specifies the parameters of the model / training. Moreover, having a single 
configuration file that exposes all the relevant parameters can be much more
convenient than having to dig through the code to find them.

The script `examples/real_convolve.py <https://github.com/ebezzam/python-dev-tips/blob/main/examples/real_convolve.py>`_
shows how to use Hydra, namely adding a decorate to the function:

.. code-block:: python

    @hydra.main(version_base=None, config_path="configs", config_name="defaults")
    def main(config):
        # `config` is a dictionary with the parameters specified in the YAML file.
        # e.g. `config.seed`

Running ``python examples/real_convolve.py`` will run the script with the default parameters
from the file ``configs/defaults.yaml``. You can also specify a different configuration
file, e.g. ``python examples/real_convolve.py -cn exp1`` will run the script with the
file ``configs/exp1.yaml``. Instead of creating a new configuration file, you can also
specify the parameters directly through the command line, e.g. 
``python examples/real_convolve.py filter_len=15``.

One handy thing about Hydra is that it creates a folder ``outputs`` with the
timestamp of the run, and saves the configuration file used in that run. You
can also save the results of the run in that folder:

.. code-block:: python

    @hydra.main(version_base=None, config_path="configs", config_name="defaults")
    def main(config):
        # ...
        # Save the results
        np.save(os.path.join(os.getcwd(), "results.npy"), results)

This makes hydra a great tool for keeping tracking of experiment runs and their 
parameters, while limiting changes to the code (and having new code commits).

Setting the seed
----------------

Setting the seed is important for reproducibility. You can set the seed in the
configuration file and use it the script like so:

.. code-block:: python

    @hydra.main(version_base=None, config_path="configs", config_name="defaults")
    def main(config):

        # Set the seed for numpy
        np.random.seed(config.seed)
        # application-specific seed setting

Instantiating objects
---------------------

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