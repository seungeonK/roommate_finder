"""
Django settings for RoommateFinder project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import sys
from pathlib import Path
import os

import dj_database_url
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bnsa+wj-r#obp6!bdnc$(@yr41$g3jsj%163g2w(dyfgtv%bep'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '0.0.0.0',
    '127.0.0.1',
    'localhost',
    'pure-reaches-12380.herokuapp.com'
]


# Application definition

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

PROJECT_APPS = [
    'social_app.apps.SocialAppConfig',
    'users.apps.UsersConfig',
]
# it is the thrid party api
THIRD_PARTY_APP = [
    #----Google Authentication API-----#
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'crispy_forms',
    # phone stuff
    'phone_field',
    # AWS stuff?
    'storages',
    # Postgre stuff?
    'django_extensions',
    # twilio stuff
    'chatapp',
]

INSTALLED_APPS = DEFAULT_APPS + PROJECT_APPS + THIRD_PARTY_APP

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 2
LOGIN_REDIRECT_URL = '/'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'RoommateFinder.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'RoommateFinder.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': '1234',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbcoatdhbj2hv',
        'USER': 'jfbrnjgulrztaz',
        'PASSWORD': 'df183ec3d56d1119d2f130e7c7217ee9d6ac65873b351f6c40067d4967105217',
        'HOST': 'ec2-52-23-190-126.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }


# (Seungeon) django/heroku database linking
# db_from_env = dj_database_url.config(conn_max_age=600)
# DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# set up where heroku static files are
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'


# AWS Stuff
# # AWS credentials to access bucket
AWS_ACCESS_KEY_ID = 'AKIAT5JXBWLMVCZZAE7U'
AWS_SECRET_ACCESS_KEY = 'sDW8OxAsG/5WhO6ijSnBgIxmJafvBdov3TV3Kq/V'
AWS_STORAGE_BUCKET_NAME = 'roomie-finder'

# # overwrite files of the same name (e.g. if 2 users uploaded image.jpg, just overwrite instead of changing everyone's stuff)
AWS_S3_FILE_OVERWRITE = False
# recommended to set it to none cuz current default causes problems
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


CRISPY_TEMPLATE_PACK = 'bootstrap4'

# (Seungeon) a full absolute path to a dir where we like Django to store uploaded files
# It is the place where the uploaded files are saved
# using os.path.join() means no matter what OS ur using, it will safely create a full absoulte path to the dir
# BASE_DIR specifies the project's base directory
#
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# (Seungeon) this is where we access the profile pics on the broswer side
# ex) pure-reaches-whatever.com/media/the_name_of_the_pic
MEDIA_URL = '/media/'

# Activate Django-Heroku.
try:
    # Configure Django App for Heroku.
    import django_heroku
    django_heroku.settings(locals())
except ImportError:
    found = False


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (os.path.join(os.path.dirname(__file__),'static'),)


TWILIO_ACCT_SID='AC73454785d6d7c885c047656d34a0b627'
TWILIO_CHAT_SID='IS37db0fd7ecfc4769abbc1833bd11bf57'
TWILIO_SYNC_SID='ISa2a449e1960064b38a302cd32698b6a3'
TWILIO_API_SID='SKf2453063677a1b10463927e42cba9b2d'
TWILIO_API_SECRET='7QlAPapGXtOQdAdwH3Zbu87bYJGt4Ocq'

# ACCOUNT_ADAPTER = "social_app.adapter.CustomAccountAdapter"

# ACCOUNT_ALLOW_SIGNUPS = False