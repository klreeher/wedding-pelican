#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from import_file import import_file

pelicanconf = import_file('pelicanconf.py')

from pelicanconf import *

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)


SITEURL = 'wedding.reeher-palmer.net'
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
