#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kate'
SITENAME = u'Reeher-Palmer Wedding'
SITEURL = ''
# contact
PLUGINS = [
        'google_embed'
]

GMAPS_KEY = 'AIzaSyCUihKCI4VNe-FREn1hgfO9U98vGrhFLy0'

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

THEME = "C:/Users/Kate Reeher/ownCloud/pelican-themes/html5-dopetrope"

# Blogroll
# LINKS = (('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

STATIC_PATHS = ['images']
DEFAULT_PAGINATION = 0

MAIL = 'wedding@reeher-palmer.net'

COPYRIGHT = 'Copyright 2017 KLReeher'
SHOW_COPYRIGHT = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
