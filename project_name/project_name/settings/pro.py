"""Production settings and globals."""

import os

from .base import *

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
# from django.core.exceptions import ImproperlyConfigured


# def get_env_setting(setting):
#     """ Get the environment setting or return exception """
#     try:
#         return os.environ[setting]
#     except KeyError:
#         error_msg = "Set the %s env variable" % setting
#         raise ImproperlyConfigured(error_msg)


########## PRODUCTION HOST CONFIGURATION #####################################
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['*']

print("\n\tServer in PRODUCTION mode\n")
########## END HOST CONFIGURATION ###########################################


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
# EMAIL_HOST = os.environ.get('EMAIL_HOST', 'mail.chezcarlos.ch')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', *******')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'chezcarlos@chezcarlos.ch')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
# EMAIL_PORT = os.environ.get('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
# EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
# EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
# SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION ###########################################

########## DATABASE CONFIGURATION ############################################
#DATABASES = {}
########## END DATABASE CONFIGURATION ########################################


########## CACHE CONFIGURATION ###############################################
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
#CACHES = {}
########## END CACHE CONFIGURATION ###########################################


########## SECRET CONFIGURATION ##############################################
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
#SECRET_KEY = get_env_setting('SECRET_KEY')
########## END SECRET CONFIGURATION ##########################################