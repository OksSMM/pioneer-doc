# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Pioneer'
copyright = '2021, Geoscan LTD'
author = 'Geoscan LTD'

# The short X.Y version
version = '2.4'
# The full version, including alpha/beta/rc tags
release = 'September update 2021'

# Здесь перечисляются множественные подстановки, которые при билде будут объявлятся в конце страницы (версии,ссылки и.т.д) ----

rst_epilog = """

.. |fw_ap_mini| replace:: `Pioneer Mini 1.6.7747 <https://disk.yandex.ru/d/xdrsPzICMUQgPw>`__
.. |fw_ap_base| replace:: `Pioneer Base 1.6.7178 <https://disk.yandex.ru/d/WqHQAxirCzi7iw>`__
.. |fw_ap_max| replace:: `Pioneer Max 1.6.7287 <https://disk.yandex.ru/d/ffN2OSTgEO8cqg>`__

.. |fw_opt_board| replace:: `Option Bord 4.0 <https://disk.yandex.ru/d/8M2tgzu0DCV0jw>`__
.. |fw_USNav| replace:: `Модуль USNav <https://disk.yandex.ru/d/1YYCDEVqNCpBvA>`__

.. |dnld_ps| replace:: `Установщик Pioneer Station <https://dl.geoscan.aero/pioneer/upload/GCS/GEOSCAN_Pioneer_Station.exe>`__
.. |dnld_ps32| replace:: `Установщик Pioneer Station 32bit <https://dl.geoscan.aero/pioneer/upload/GCS/PioneerStationWin32.zip>`__

"""

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.githubpages',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'ru'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
import os
import sys

sys.path.append(os.path.abspath("./_ext"))

extensions = ['tile']

from tile import TileDirective
from tile import tilenode
from tile import visit_tile
from tile import depart_tile

html_theme = 'sphinx_rtd_theme_upgraded'
html_theme_path = ['_themes', ]

def setup(app):
    app.add_css_file('style.css')

    app.add_node(tilenode, html=(visit_tile, depart_tile))
    app.add_directive('tile', TileDirective)


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
#html_theme_options = {'logo_only': True,}
html_theme_options = {'logo_only': True,
                      'includehidden': True}

html_logo = "_static/images/logo.png"
html_favicon = "_static/images/favicon.ico"
html_show_sphinx = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'css/index.css',
    'css/tiles.css',
    'css/cont_grid_layout.css',
    'css/gallery_layout.css'
]

html_js_files = [
    'js/tiles.js',
    'js/index.js'
]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'pioneerdoc'

latex_logo = "_static/images/logo_latex.png"
# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
     'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
     'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
     'preamble': '',

    # Latex figure (float) alignment
    #
     'figure_align': 'H',

	    'fontpkg': r'''

''',
    # Additional stuff for the LaTeX preamble.
	'preamble': r"""
	\usepackage{setspace}
	\usepackage{fontspec}
	\setmainfont[Ligatures=TeX]{Georgia}
	\setsansfont[Ligatures=TeX]{Arial}
	""",

}


# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'pioneer.tex', '',
     '', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'Pioneer', 'Pioneer Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'pioneer', 'Pioneer Documentation',
     author, 'pioneer', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


