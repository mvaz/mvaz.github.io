#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Miguel Vaz'
SITENAME = 'Brain log'
SITEURL = 'https://mvaz.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

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
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Specify name of a built-in theme
THEME = "medius"

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb']

# Medius theme specific stuff

STATIC_PATHS = ['images']
HEADER_IMAGE = "network_layout.jpg"

MEDIUS_CATEGORIES = {
    'Linux': {
        'description': 'Linux is an operating system',
        #'logo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/GalacticRotation2.svg/250px-GalacticRotation2.svg.png',
        'thumbnail': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/NewTux.svg/200px-NewTux.svg.png'
    },
    'Finance': {
        'description': 'Perambulations on Risk Management',
        #'logo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/GalacticRotation2.svg/250px-GalacticRotation2.svg.png',
        'thumbnail': 'https://pbs.twimg.com/profile_images/578083482024308736/7R7HCSon.png'    
    }
}



MEDIUS_AUTHORS = {
    'Miguel Vaz': {
        'description': """
            Jack of some trades.
        """,
        'cover': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Milky_Way_Arch.jpg/1920px-Milky_Way_Arch.jpg',
        'image': 'https://lh6.googleusercontent.com/-zEMaXmWAhdI/AAAAAAAAAAI/AAAAAAAAAAA/eVdgsm3TIDU/s128-c-k/photo.jpg',
        'links': (('github-square', 'https://github.com/mvaz'),
                  ('twitter-square', 'https://twitter.com/migueljvaz'),
                  ('envelope-square', '#')),
    }
}

