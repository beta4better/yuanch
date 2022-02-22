#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Charles Yuan'
SITENAME = '好奇-求知'
SITEURL = ''

THEME ='pelican-themes/svbtle'

PATH = 'content'
TAG_CLOUD = True
TAG_CLOUD_STEPS = 5
TAG_CLOUD_MAX_ITEMS = 50
TAG_CLOUD_BADGE = True
TAG_CLOUD_SORTING = 'size'

# Plugins
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["tag_cloud", "neighbors"]

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh_CN'

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
        )

# Social widget
SOCIAL = (('GitHub', 'https://github.com/beta4better'),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
