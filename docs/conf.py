import os
import sys

# Ajouter le chemin vers le package
sys.path.insert(0, os.path.abspath("../src"))

# -- Project information
project = "package_creation_tutorial"
copyright = "2025, Ryhem Mekni"
author = "Ryhem Mekni"
release = "0.1.0"

# -- General configuration
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.githubpages",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "en"

# -- Options for HTML output
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
