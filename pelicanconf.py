#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
# GENERAL
AUTHOR = 'ccenzura'
SITENAME = 'Around Python'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'Europe/Warsaw'
DEFAULT_LANG = 'pl'
SUMMARY_MAX_LENGTH = 50

#THEME
THEME = 'themes/pelican-twitchy'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_RECENT_POSTS_ON_MENU = True
DISPLAY_TAGS_ON_MENU = False
PYGMENTS_STYLE = "default"
BOOTSTRAP_THEME = "slate"

# PLUGINS
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb2pelican']
IGNORE_FILES = ['.ipynb_checkpoints']
IPYNB_IGNORE = True # ignorowanie cells z tagiem #ignore

# CONTENTc
USE_FOLDER_AS_CATEGORY = True
STATIC_PATHS = ['images', 'articles']
ARTICLE_PATHS = ['articles']
ARTICLE_URL = 'articles/{category}/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{category}/{slug}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Bitbucket', 'https://bitbucket.org/ccenzura/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
