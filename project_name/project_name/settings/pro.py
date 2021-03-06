"""Production settings and globals."""

from __future__ import absolute_import
import os
from django.core.exceptions import ImproperlyConfigured
from django_extensions.management.commands.generate_secret_key import Command
from .base import *
# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
# from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return os.environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)


########## SECRET CONFIGURATION ###############################################
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: a new secret key is automatically re-generated  
SECRET_KEY = Command().handle_noargs()
########## END SECRET CONFIGURATION ###########################################

########## PRODUCTION HOST CONFIGURATION #####################################
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['*']

print("\n\tServer in PRODUCTION mode\n")
########## END HOST CONFIGURATION ###########################################

# ######### DATABASE CONFIGURATION ###########################################
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'CONN_MAX_AGE': 60,
        'NAME': SITE_NAME,
        'HOST': 'localhost',
        'USER': 'user',
        'PASSWORD': '********',
        'TIME_ZONE': 'UTC'
    }
}
########## END DATABASE CONFIGURATION ########################################

########## PRODUCTION DEBUG CONFIGURATION ###################################
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION ##########################################


########## PRODUCTION EMAIL CONFIGURATION ###################################
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
# EMAIL_HOST = os.environ.get('EMAIL_HOST', 'mail.example.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', *******')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'mailbox@example.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
# EMAIL_PORT = os.environ.get('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
# EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
# EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
# SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION ###########################################

########## CACHE CONFIGURATION ###############################################
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
#CACHES = {}
########## END CACHE CONFIGURATION ###########################################

########## ANOTHER FORM OF SECRET KEY CONFIGURATION ##########################
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
#SECRET_KEY = get_env_setting('SECRET_KEY')
########## END SECRET CONFIGURATION ##########################################
