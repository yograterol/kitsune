from settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SESSION_COOKIE_SECURE = False

# Allows you to run Kitsune without running Celery---all tasks
# will be done synchronously.
CELERY_ALWAYS_EAGER = True

# Allows you to specify waffle settings in the querystring.
WAFFLE_OVERRIDE = True

# Change this to True if you're going to be doing search-related
# work.
ES_LIVE_INDEXING = False

# Basic cache configuration for development.
CACHES = {
    'default': {
        'BACKEND': 'caching.backends.memcached.CacheClass',
        'LOCATION': 'localhost:11211',
        'PREFIX': 'sumo:',
        }
    }

# Basic database configuration for development.
DATABASES = {
    'default': {
        'NAME': 'kitsune',
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'USER': 'kitsune',
        'PASSWORD': '',
        'OPTIONS': {'init_command': 'SET storage_engine=InnoDB'},
        'TEST_CHARSET': 'utf8',
        'TEST_COLLATION': 'utf8_unicode_ci',
        },
    }

LESS_PREPROCESS = True
LESS_BIN = '/usr/bin/lessc'
