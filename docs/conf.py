project = "PLACER"
extensions = ["sphinx.ext.autodoc"]
html_theme = "sphinx_rtd_theme"
exclude_patterns = ["_build"]

import os
import sys
sys.path.insert(0, os.path.abspath("../src"))
