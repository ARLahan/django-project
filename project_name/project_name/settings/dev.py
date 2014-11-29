"""Development settings and globals."""

import os
from .base import *

########## OVERRIDE BASE DEBUG CONFIGURATION ###############################
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

import warnings
warnings.filterwarnings(
    'error', r"DateTimeField .* received a naive datetime",
    RuntimeWarning, r'django\.db\.models\.fields')


# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG

#TEST_RUNNER = 'django.test.runner.DiscoverRunner'

print("\n\tServer in LOCAL/DEVELOPMENT mode")

########## END DEBUG CONFIGURATION ##########################################

########## OVERRIDE PRODUCTION EMAIL CONFIGURATION ##########################
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION ##########################################

######## OVERRIDE BASE DATABASE CONFIGURATION ###############################
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases 
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(DATABASE_ROOT, ''.join(SITE_NAME, 'db')),
     }
 }
######## END DATABASE CONFIGURATION ##########################################

########## CACHE CONFIGURATION ###############################################
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION ###########################################

########## DEBUG TOOLBAR CONFIGURATION #######################################
# See: http://django-debug-toolbar.readthedocs.org/en/latest/installation.html#explicit-setup
INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PATCH_SETTINGS = False

# http://django-debug-toolbar.readthedocs.org/en/latest/installation.html
INTERNAL_IPS = ('127.0.0.1',)
########## END debug TOOLBAR CONFIGURATION ###################################