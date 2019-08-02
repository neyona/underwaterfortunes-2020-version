import django_heroku
"""
Django settings for fortune_project project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=y=_+-@tn_qyq6mcus3*#6yn)#bz8bxj#w2m2@=w)a+v7x2!gj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['https://ancient-brook-69837.herokuapp.com',
                 'https://underwaterfortunes.com',
                 '127.0.0.1',
                 '127.0.0.1:8000',
                 ]

SECURE_SSL_REDIRECT = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # 3rd
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_auth',
    'rest_auth.registration',
    # local
    'fortunes.apps.FortunesConfig',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fortune_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'build')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fortune_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'build', 'static',)]

STATICFILES_STORAGE = (
    'whitenoise.storage.CompressedManifestStaticFilesStorage'
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

WHITENOISE_ROOT = os.path.join(BASE_DIR, 'build', 'root')

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication'
    ],
}

# Is authenticated or read only because otherwise no fortune shows up in
# mobile browsers. It is odd that mobile chrome and computer chrome render
# so differently.

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_ID = 1

django_heroku.settings(locals())


def get_cache():
    try:
        servers = os.environ['*********']
        username = os.environ['*********']
        password = os.environ['***********************************']
        return {
            'default': {
                'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
                'TIMEOUT': None,
                'LOCATION': servers,
                'OPTIONS': {
                    'binary': True,
                    'username': username,
                    'password': password,
                    'behaviors': {
                        # Enable faster IO
                        'no_block': True,
                        'tcp_nodelay': True,
                        # Keep connection alive
                        'tcp_keepalive': True,
                        # Timeout settings
                        'connect_timeout': 2000,  # ms
                        'send_timeout': 750 * 1000,  # us
                        'receive_timeout': 750 * 1000,  # us
                        '_poll_timeout': 2000,  # ms
                        # Better failover
                        'ketama': True,
                        'remove_failed': 1,
                        'retry_timeout': 2,
                        'dead_timeout': 30,
                    }
                }
            }
        }
    except:
        return {
            'default': {
                'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
            }
        }


CACHES = get_cache()
