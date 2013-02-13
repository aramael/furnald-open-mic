# Production Enviroment Variables
__author__ = 'aramael'

import os
from common import INSTALLED_APPS

SETTINGS_DIR, filename = os.path.split(os.path.abspath(__file__))

SITE_ROOT = os.path.dirname( SETTINGS_DIR )

# Make this unique, and don't share it with anybody.
# Set it by issuing following command
# <code>
# heroku config:add SECRET_KEY=''
# </code>
SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Django Databases
DATABASES = {}

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

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

# Static Files #
################
INSTALLED_APPS += ('storages',)

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(SITE_ROOT, 'prod_static')

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

# This setting sets the path to the S3 storage class
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Your Amazon Web Services storage bucket name, as a string.
AWS_STORAGE_BUCKET_NAME = 'furnaldopenmikenight'

# Your Amazon Web Services access key, as a string.
# Set it by issuing following command
# <code>
# heroku config:add AWS_ACCESS_KEY_ID='your_access_key_id'
# </code>
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']

# Your Amazon Web Services secret access key, as a string.
# Set it by issuing following command
# <code>
# heroku config:add AWS_SECRET_ACCESS_KEY='your_secret_access_key'
# </code>
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Set Static URL
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL
