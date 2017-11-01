#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

TIMEZONE = "America/Chicago"
DEFAULT_DATE_FORMAT = '%a %d %B %Y'

# THEME
THEME = 'pelican-themes/graymill'
# basic, bootlex, cebong, graymill, monospace,
#SITETAGLINE = 'Join Us September 15, 2018'


AUTHOR = u'Kate'
SITENAME = u'Reeher-Palmer Wedding'
SITEURL = 'www.wedding.reeher-palmer.net'
# contact

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
        #'google_embed',
        'assets',
        'autopages',
        'filetime_from_git',
        #'pelican-page-order'
]

# PLUGIN CONFIG

## Google Embed
GMAPS_KEY = 'AIzaSyCUihKCI4VNe-FREn1hgfO9U98vGrhFLy0'

## Autopages
AUTHOR_PAGE_PATH = 'authors'
CATEGORY_PAGE_PATH = 'categories'
TAG_PAGE_PATH = 'tags'

## Filetime From Git


PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# theme
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (('Home', "/"), 
	('Wedding Ceremony','/pages/ceremony.html'),
	('Wedding Reception','/pages/reception.html'),
	('Registry','/pages/wedding-registry.html'))

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_SUMMARY = True
STATIC_PATHS = ['images']
DEFAULT_PAGINATION = 5

MAIL = 'wedding@reeher-palmer.net'
DIRECT_TEMPLATES = ['index']

COPYRIGHT = 'Copyright 2017 KLReeher'
SHOW_COPYRIGHT = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
