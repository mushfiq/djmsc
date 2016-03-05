import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2#__8lllf474ug@#!4$z$iio_+*sn=72by*i$(2_0+&@9$gr99'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'api',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.csrf.CsrfViewMiddleware',
]

ROOT_URLCONF = 'djmsc.urls'

WSGI_APPLICATION = 'djmsc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'djmsc.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

REST_FRAMEWORK = {
    'PAGE_SIZE': 10
}
