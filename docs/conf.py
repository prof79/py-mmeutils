# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'mmeutils'
copyright = '2024, Markus M. Egger'
author = 'Markus M. Egger'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Paths for modules -------------------------------------------------------
# https://stackoverflow.com/questions/53668052/sphinx-cannot-find-my-python-files-says-no-module-named
import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

# -- Extension options -------------------------------------------------------
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
myst_enable_extensions = [
    'colon_fence',
    'dollarmath',
    'fiedlist',
    'tasklist',
]
