# -*- coding: utf-8 -*- #

import os
import pylast

#dev
DEBUG = True
TEMPLATE_DEBUG = DEBUG

#contact/admin
ADMINS = (
  ('nerdfiles', 'nerdfiles@gmail.com'),
)
MANAGERS = ADMINS

#db
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
    'NAME': 'dev.db',                      # Or path to database file if using sqlite3.
    'USER': '',                      # Not used with sqlite3.
    'PASSWORD': '',                  # Not used with sqlite3.
    'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
    'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
  }
}

#essentials
PROJECT_ROOT = os.path.dirname(__file__)
DIRNAME = os.path.dirname(os.path.abspath(__file__))
_ = lambda s: s

#additional settings
TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
ROOT_URLCONF = 'django_lastfm.urls'

#security
SECRET_KEY = '3c8cv6n1lc!l(0kvl4^$$9_z*wx9i6oe_l#+8hqas+kpf7o$$m'

#assets
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "lastfm", "assets")
MEDIA_URL = '/assets/'

#static
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
  'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

#templating
TEMPLATE_LOADERS = (
  'django.template.loaders.filesystem.Loader',
  'django.template.loaders.app_directories.Loader',
)
TEMPLATE_DIRS = (
  os.path.join(PROJECT_ROOT, "lastfm", "templates"),
)

#middleware
MIDDLEWARE_CLASSES = (
  'django.middleware.common.CommonMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
)


#apps
INSTALLED_APPS = (
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.sites',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django.contrib.admin',
  'django.contrib.admindocs',

  # third-party
  'django_extensions',

  # custom
  'utils',
  'lastfm',
)

#logging
LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'handlers': {
    'mail_admins': {
      'level': 'ERROR',
      'class': 'django.utils.log.AdminEmailHandler'
    }
  },
  'loggers': {
    'django.request': {
      'handlers': ['mail_admins'],
      'level': 'ERROR',
      'propagate': True,
    },
  }
}

#pylast
username = "wittysense"
password_hash = pylast.md5("f0xf0x0!6")
API_KEY = "4c84847605bf2fd159d3aa5277ef2f32" 
API_SECRET = "15097744590f54e0f9df2c8c5bee4cd0"

