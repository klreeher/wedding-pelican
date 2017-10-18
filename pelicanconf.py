#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import bulrush

TIMEZONE = "America/Chicago"
DEFAULT_DATE_FORMAT = '%a %d %B %Y'

# THEME
THEME = '../pelican-themes/bulrush/bulrush'
JINJA_ENVIRONMENT = bulrush.ENVIRONMENT
JINJA_FILTERS = bulrush.FILTERS

## Bulrush specific
SITESUBTITLE = 'Join Us September 15, 2018'
### Static files
#STATIC_PATHS = [
#    '../pelican-themes/bulrush/bulrush/static/bulma-gen'
#]
#EXTRA_PATH_METADATA = {
#    'static/custom.css': {'path': 'bulma.css'}
#}

AUTHOR = u'Kate'
SITENAME = u'Reeher-Palmer Wedding'
SITEURL = ''
# contact

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = [
        'google_embed',
        'assets',
        'autopages',
        'filetime_from_git',
        'pelican-page-order'
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

#THEME = "C:/Users/Kate Reeher/ownCloud/pelican-themes/html5-dopetrope"

# Blogroll
# LINKS = (('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

STATIC_PATHS = ['images']
DEFAULT_PAGINATION = 1

MAIL = 'wedding@reeher-palmer.net'

COPYRIGHT = 'Copyright 2017 KLReeher'
SHOW_COPYRIGHT = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
