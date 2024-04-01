#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

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
import os
import sys

from datetime import date
from typing import Dict, List, Union

from docutils import nodes
from docutils.nodes import Element, Node

from sphinx.writers.html import HTMLTranslator

# below required for local build
import sphinx_rtd_theme  # noqa: F401 'sphinx_rtd_theme' imported but unused

sys.path.insert(0, os.path.abspath("../.."))
import holidays  # noqa: E402 module level import not at top of file


# -- Project information -----------------------------------------------------

project = "holidays"
copyright = str(date.today().year)
author = "dr-prodigy"
version = holidays.__version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#
extensions = [
    # 'sphinx.ext.intersphinx',
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    # 'sphinx.ext.doctest',
    # 'sphinx.ext.mathjax',
    "sphinx.ext.todo",
    # 'sphinx.ext.viewcode',
    # 'sphinxcontrib.httpdomain',
    "sphinx_rtd_theme",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns: List[str] = []

# Add any paths that contain templates here, relative to this directory.
#
# templates_path = ['_templates']

# The name of the Pygments (syntax highlighting) style to use.
# If not set, either the theme’s default style or 'sphinx' is selected for HTML
# output.
#
pygments_style = "sphinx"

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = "4.3.2"

# -- Options for internationalization ----------------------------------------

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages. See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'  # default
html_theme = "sphinx_rtd_theme"

# Custom style (imports regular style and adding new ones)
#
# See https://docs.readthedocs.io/en/stable/guides/adding-custom-css.html
#     #overriding-or-replacing-a-theme-s-stylesheet
#
html_style = "css/custom.css"

# The “title” for HTML documentation generated with Sphinx’s own templates.
#
# html_title = '<project> v<revision> documentation'  # default


# Name of image file that is the logo of the docs, or URL that points to same.
# Width not to exceed 200 pixels.
#
# html_logo = None  # default


# Name of a Windows-style icon file (.ico) that is the favicon of the docs, or
# URL that points to same.
#
# html_favicon = None  # default

# A ‘Last updated on:’ timestamp is inserted at every page bottom, using the
#  given strftime() format. The empty # string is equivalent to '%b %d, %Y'
#  (or a locale-dependent equivalent).
#
html_last_updated_fmt = ""

# Include reST sources in the HTML build as _sources/name. The default is True
#
html_copy_source = False

# Theme options are theme-specific and customize the look and feel of a theme
# further. For a list of options available for each theme, see the
# documentation.
#
# See https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html
#
html_theme_options: Dict[str, Union[str, bool, int]] = {
    # 'canonical_url': '',
    # 'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    # 'analytics_anonymize_ip': False
    # 'logo_only': False,
    # 'display_version': True,
    # 'prev_next_buttons_location': 'bottom',
    # 'style_external_links': False,
    # 'vcs_pageview_mode': '',
    # 'style_nav_header_background': '#2980B9',
    # Toc options
    # 'collapse_navigation': True,
    # 'sticky_navigation': True,
    # 'navigation_depth': 4,
    # 'includehidden': True,
    # 'titles_only': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ["_static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself. Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for the Python domain -------------------------------------------

# Set to True to suppress the module name of the python reference if it can be
# resolved.
#
python_use_unqualified_type_names = True


# -- sphinx.ext.autodoc configuration ----------------------------------------

# See https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
#     #configuration

autoclass_content = "both"
autodoc_member_order = "groupwise"
# See https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
#     #directives
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",  # 'alphabetical' (def) 'groupwise', 'bysource'
    "undoc-members": True,
    # 'private-members': False,  # default
    # 'special-members': False,  # default
    "inherited-members": False,  # Disabled due to performance concerns.
    "show-inheritance": True,
    # 'ignore-module-all': False,  # default
    # 'imported-members': False, # default
    # 'exclude-members': '',  # default
    # 'class-doc-from': '',  # default
}
# autodoc_docstring_signature = True  # default
# autodoc_mock_imports = []  # default
autodoc_typehints = "description"
# autodoc_typehints_description_target = 'all'  # default
# autodoc_type_aliases = {}  # default
# autodoc_warningiserror = True  # default
# autodoc_inherit_docstrings = True  # default


# https://stackoverflow.com/questions/2701998
autosummary_generate = True


# -- sphinx.ext.to do configuration ------------------------------------------

# If true, `to do` and `todoList` produce output, else they produce nothing.
#
todo_include_todos = True


# -- Patch to open external links in new tab ---------------------------------

# see https://stackoverflow.com/a/61669375/3159288

# code below from version 4.0.0 at
# https://github.com/sphinx-doc/sphinx/blob/master/sphinx/writers/html5.py


class PatchedHTMLTranslator(HTMLTranslator):
    """Adds open-in-new-tab support.
    See https://stackoverflow.com/questions/25583581.
    """

    def unknown_visit(self, node: Node) -> None:
        pass

    def visit_reference(self, node: Element) -> None:
        atts = {"class": "reference"}
        if node.get("internal") or "refuri" not in node:
            atts["class"] += " internal"
        else:
            atts["class"] += " external"
            # ---------------------------------------------------------
            # Customize behavior (open in new tab, secure linking site)
            atts["target"] = "_blank"
            atts["rel"] = "noopener noreferrer"
            # ---------------------------------------------------------
        if "refuri" in node:
            atts["href"] = node["refuri"] or "#"
            if self.settings.cloak_email_addresses and atts["href"].startswith(
                "mailto:"
            ):
                atts["href"] = self.cloak_mailto(atts["href"])
                self.in_mailto = True
        else:
            assert (
                "refid" in node
            ), 'References must have "refuri" or "refid" attribute.'
            atts["href"] = "#" + node["refid"]
        if not isinstance(node.parent, nodes.TextElement):
            assert len(node) == 1 and isinstance(node[0], nodes.image)
            atts["class"] += " image-reference"
        if "reftitle" in node:
            atts["title"] = node["reftitle"]
        if "target" in node:
            atts["target"] = node["target"]
        self.body.append(self.starttag(node, "a", "", **atts))

        if node.get("secnumber"):
            self.body.append(
                ("%s" + self.secnumber_suffix)
                % ".".join(map(str, node["secnumber"]))
            )


def setup(app):
    app.set_translator("html", PatchedHTMLTranslator)
