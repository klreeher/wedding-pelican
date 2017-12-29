#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

TIMEZONE = "America/Chicago"
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
PATH = 'content'
DEFAULT_LANG = u'en'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
        #'google_embed',
        'assets',
        'autopages',
        'filetime_from_git',
        #'pelican-page-order'
]

# THEME
THEME = 'pelican-themes/graymill'
# basic, bootlex, cebong, graymill, monospace,

# Site Info
AUTHOR = u'Kate'
SITENAME = u'Reeher-Palmer Wedding'
SITEURL = 'http://localhost:8000'
#SITEURL = 'www.wedding.reeher-palmer.net'
#SITETAGLINE = 'Join Us September 15, 2018'


# PLUGIN CONFIG

## Autopages
AUTHOR_PAGE_PATH = 'authors'
CATEGORY_PAGE_PATH = 'categories'
TAG_PAGE_PATH = 'tags'

WITH_FUTURE_DATES = False

DRAFT_SAVE_AS = 'drafts/{slug}.html'
DRAFT_URL = 'drafts/{slug}.html'

## Filetime From Git

GIT_FILETIME_FROM_GIT = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# theme
# To display static pages like About, Contact etc.
DISPLAY_PAGES_ON_NAV = True

#MENUITEMS = (('Home', SITEURL), ('Wedding Ceremony', SITEURL+'/pages/ceremony.html'), ('Wedding Reception', SITEURL+'/pages/reception.html'), ('Wedding Registry', SITEURL+'/pages/registry.html'))

#, ('About Us', 'pages/about-us.html')

DISPLAY_SUMMARY = True
# To include custom static files like htaccess, robots, PDF files etc. (path relative to './content/')
STATIC_PATHS = ['images', 'extras']
EXTRA_PATH_METADATA = {
    'extras/.htaccess': {'path': '.htaccess'},
    'extras/robots.txt': {'path': 'robots.txt'},
}
DEFAULT_PAGINATION = 5

MAIL = 'wedding@reeher-palmer.net'
DIRECT_TEMPLATES = ['index']

COPYRIGHT = 'Copyright 2017 Reeher-Palmer'
SHOW_COPYRIGHT = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
