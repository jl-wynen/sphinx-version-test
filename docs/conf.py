import os
import sys

sys.path.insert(0, os.path.abspath("."))

project = "test"
source_suffix = ".rst"
html_sourcelink_suffix = ""
master_doc = "index"
warning_is_error = True
language = "en"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]
pygments_style = "sphinx"

html_theme = "pydata_sphinx_theme"
version = "3.0"  # TODO get from package
html_theme_options = {
    "left_sidebar_end": [],
    "show_nav_level": 1,
    "github_url": "https://github.com/SciCatProject/scitacean",

    # NEW
    "navbar_end": ["version-switcher", "navbar-icon-links"],
    "switcher": {
        "json_url": "https://jl-wynen.github.io/sphinx-version-test/_static/version-switcher.json", # TODO
        "version_match": version,
    }
}
html_context = {
    "github_user": "SciCatProject",
    "github_repo": "scitacean",
    "github_version": "main",
    "doc_path": "docs",
}

html_title = "Test"
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
htmlhelp_basename = "testdoc"
