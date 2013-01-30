# Production Enviroment Variables
__author__ = 'aramael'

import os

SETTINGS_DIR, filename = os.path.split(os.path.abspath(__file__))

SITE_ROOT = os.path.dirname( SETTINGS_DIR )

# Make this unique, and don't share it with anybody.
SECRET_KEY = '^27$&amp;*b*2_v_427$755&amp;-lhg=1^r+nlv54@+7cwv-gyj)jnasu'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Django Databases
DATABASES = {}

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(SITE_ROOT, 'static'),
    )

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(SITE_ROOT, 'templates'),
    )

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    )

INTERNAL_IPS = ('127.0.0.1',
    )