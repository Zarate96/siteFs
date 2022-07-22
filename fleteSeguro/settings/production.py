import os
import dj_database_url
from decouple import config
from fleteSeguro.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

SITE_URL = 'https://fleteseguro.com.mx'
PROTOCOL_HTTP = 'https'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

