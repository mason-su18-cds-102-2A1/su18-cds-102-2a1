# -*- coding: utf-8 -*-
"""Pelican setings for CDS-102 (Summer 2018) labs."""

from __future__ import unicode_literals

# GENERAL
AUTHOR = "Dr. Glasbrenner"
SITENAME = "CDS-102: Introduction to Computational and Data Sciences Lab"
SITEURL = ""
SLACK_URL = "http://masoncds101.slack.com"
GITHUB_URL = "https://github.com/mason-su18-cds-102-2a1/su18-cds-102-2a1"
UNIVERSITYURL = "https://gmu.edu"
TIMEZONE = "America/New_York"
DEFAULT_LANG = "en"

# PROCESSING
CACHE_CONTENT = False
READERS = {
    "html": None,
    "yaml": None,
}

# THEME
THEME = "theme"
THEME_STATIC_PATHS = ["static"]
FRONT_PAGE_STYLE = "schedule"
TYPOGRIFY = True
HIGHLIGHT_JS_STYLE = "default"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Define paths and urls
PATH = "content"
IMAGES_PATH = "img"
STATIC_PATHS = [
    "doc",
    "files",
    IMAGES_PATH,
]
PAGE_PATHS = ["pages"]
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
ARTICLE_URL = ""
ARTICLE_SAVE_AS = ""
AUTHOR_URL = ""
AUTHOR_SAVE_AS = ""
DRAFT_URL = ""
DRAFT_SAVE_AS = ""
CATEGORY_URL = ""
CATEGORY_SAVE_AS = ""
TAG_URL = ""
TAG_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAGS_SAVE_AS = ""
INDEX_SAVE_AS = "index.html"
DIRECT_TEMPLATES = [
    "index",
]
PAGINATED_DIRECT_TEMPLATES = []
TEMPLATE_PAGES = {
    "syllabus.html": "syllabus.html",
    "datasets.html": "datasets.html",
}
SUMMARY_MAX_LENGTH = 50

# Menu items
MENUITEMS = []

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "custom_article_urls",
    "pandoc_reader",
    "rmd_reader",
    "pelican-plugin-tidy-html",
]

# Plugin: Custom Article URLs
CUSTOM_ARTICLE_URLS = {
    'Labs': {
        'URL': 'labs/{slug}/',
        'SAVE_AS': ('labs/{slug}/index.html'),
    },
}

# Plugin: RMD Reader
RMD_READER_CLEANUP = True
RMD_READER_RENAME_PLOT = "directory"
RMD_READER_KNITR_QUIET = True
RMD_READER_KNITR_ENCODING = "UTF-8"
RMD_READER_KNITR_OPTS_CHUNK = {
    "fig.path": IMAGES_PATH,
}
RMD_READER_KNITR_OPTS_KNIT = None

# Plugin: Pandoc Reader
PANDOC_ARGS = [
    "--no-highlight",
    "--filter",
    "pandoc-citeproc",
    "--mathjax",
    "--variable",
    "\"mathjax-url:#\"",
]
PANDOC_EXTENSIONS = [
    "+autolink_bare_uris",
    "+ascii_identifiers",
    "-tex_math_single_backslash",
    "-implicit_figures",
    "+multiline_tables",
    "+tex_math_double_backslash",
    "+smart",
]
