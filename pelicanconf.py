#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

TIMEZONE = "America/Chicago"
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
PATH = 'content'
DEFAULT_LANG = u'en'

PLUGIN_PATHS = ['pelican-plugins', '/pelican/pelican-plugins']
PLUGINS = [
        #'google_embed',
        'assets',
        'autopages',
        'filetime_from_git',
        'i18n_subsites',
        'tipue_search',
        #'pelican-page-order'
]

# THEME
THEME = 'pelican-bootstrap3'
# basic, bootlex, cebong, graymill, monospace,

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Site Info
AUTHOR = u'K.L.Reeher & C.E.Palmer'
SITENAME = u'Reeher-Palmer Wedding'
SITEURL = 'http://localhost:8000'
#SITEURL = 'www.wedding.reeher-palmer.net'
SITETAGLINE = 'Join Us September 15, 2018'


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
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [('ceremony', '/pages/ceremony.html' ),('reception', '/pages/reception.html'),('rsvp', '/pages/rsvp.html')]
DISPLAY_CATEGORIES_ON_MENU = False
FAVICON = ''
DISPLAY_ARTICLE_INFO_ON_INDEX = False
PADDED_SINGLE_COLUMN_STYLE = True
HIDE_SIDEBAR = True
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')
BOOTSTRAP_FLUID = True
PYGMENTS_STYLE = 'vim'
BOOTSTRAP_NAVBAR_INVERSE = True


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


COPYRIGHT = '<a href="mailto:wedding@reeher-palmer.net?Subject=Reeher-Palmer%20Wedding" target="_top">Reeher-Palmer</a> 2018'
SHOW_COPYRIGHT = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
