# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import datetime
import sys
from unittest import mock
import os

sys.path.insert(0, os.path.abspath(os.path.join("..", "..")))

MOCK_MODULES = ["matplotlib", "matplotlib.pyplot", "numpy", ""]
for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = mock.Mock()


# -- Project information -----------------------------------------------------

project = "pydevtips"
copyright = f"{datetime.date.today().year}, Eric Bezzam"
author = "Eric Bezzam"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

autodoc_default_options = {
    "members": True,
}
autodoc_typehints = "none"  # for cleaner sphinx output, don't show type hints

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "NumPy [latest]": ("https://docs.scipy.org/doc/numpy/", None),
    "matplotlib": ("http://matplotlib.sourceforge.net/", None),
}
intersphinx_disabled_domains = ["std"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
