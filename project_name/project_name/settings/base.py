"""
Django settings for {{ project_name }} project.

Using Jinja2 templating system

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
from django_extensions.management.commands.generate_secret_key import Command
########## BASE CONFIGURATION ################################################
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

########## SECRET CONFIGURATION ###############################################
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: a new secret key is automatically re-generated  
SECRET_KEY = Command().handle_noargs()
########## END SECRET CONFIGURATION ###########################################

DEBUG = False

TEMPLATE_DEBUG = False

# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts

ALLOWED_HOSTS = []
########## END BASE CONFIGURATION ############################################


########## PATHS CONFIGURATION ###############################################

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Site name:
SITE_NAME = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
APP_ROOT = os.path.dirname(os.path.dirname(__file__))

# SQLite3 database file location:
DATABASE_ROOT = os.path.join(BASE_DIR, 'data/')

# Add our project to our pythonpath, this way we don't need to
# type our project name in our dotted import paths:
sys.path.append(APP_ROOT)
sys.path.append(DATABASE_ROOT)

########## END PATHS CONFIGURATION ###########################################

########## APPs CONFIGURATION ################################################
# Application definition
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps

DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    'django.contrib.humanize',

    # Admin panel and documentation:
    'django.contrib.admin',
    # 'django.contrib.admindocs',
)

# Third party apps for this project
THIRDPARTY_APPS = (
    'django_jinja',
    'django_jinja.contrib._humanize',
    'django_extensions',
    'ckeditor',
)

# Apps specific for this project go here.
LOCAL_APPS = (

)

INSTALLED_APPS = DJANGO_APPS + THIRDPARTY_APPS + LOCAL_APPS
#
########## END APPs CONFIGURATION ############################################

# MIDDLEWARE CONFIGURATION ##################################################
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
########## END MIDDLEWARE CONFIGURATION #####################################

########## URL CONFIGURATION and APPLICATION CONFIGURATION ##################
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '{}.urls'.format(SITE_NAME)

WSGI_APPLICATION = '{}.wsgi.application'.format(SITE_NAME)
########## END CONFIGURATION and APPLICATION CONFIGURATION ##################

# ######### DATABASE CONFIGURATION ###########################################
#
# DATABASE CONFIGURATION in:
# dev = dev.py >> using sqlite3
# pro = pro.py >> using postgresql+psycopg2
#
########## END DATABASE CONFIGURATIONN #######################################

########## GENERAL CONFIGURATION #############################################
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'UTC'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
########## END GENERAL CONFIGURATION

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
########## END GENERAL CONFIGURATION #########################################

########## MEDIA CONFIGURATION ##############################################
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

# Temporary directory for file uploads
FILE_UPLOAD_TEMP_DIR = os.path.join(os.path.dirname(BASE_DIR), 'tmp')
########## END MEDIA CONFIGURATION ###########################################

########## STATIC FILE CONFIGURATION #########################################
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)
########## END STATIC FILE CONFIGURATION #####################################

########## MANAGER CONFIGURATION #############################################
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Al-Ramah Lahan', 'bytewin@bytewin.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION ########################################

########## FIXTURE CONFIGURATION ############################################
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
)
########## END FIXTURE CONFIGURATION ########################################

########## TEMPLATE CONFIGURATION ###########################################
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django_jinja.loaders.AppLoader',
    'django_jinja.loaders.FileSystemLoader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

DEFAULT_JINJA2_TEMPLATE_EXTENSION = '.jinja'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)
########## END TEMPLATE CONFIGURATION ######################################

########## LOGGING CONFIGURATION ###########################################
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django_jinja': {
            'handlers': ['console', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
########## END LOGGING CONFIGURATION #########################################

# TEST RUNNER:
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
#
##############################################################################
# CKEDITOR CONFIG #############################################
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = os.path.join(STATIC_URL, 'js', 'jquery.min.js')
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_DATE_FOLDERS = False
CKEDITOR_CONTENT_FOLDER = 'content/'
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
CKEDITOR_RESTRICT_BY_USER = False
CKEDITOR_MEDIA_PREFIX = MEDIA_ROOT
CKEDITOR_CONFIGS = {
    'default': {
        "removePlugins": "stylesheetparser",
        # 'uiColor': '#ACC5E0',
        'language': LANGUAGE_CODE,
        'toolbar': 'Extra',
        'height': 400,
        'width': '100%',
        'resize_minWidth': 600,
        'resize_minHeight': 200,
        'resize_dir': 'both',
        'fullPage': False,
        'allowedContent': True,
    },
}
