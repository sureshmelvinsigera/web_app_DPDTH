"""
Django settings for airline project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import django_heroku
import dj_database_url
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7!@8iekdn*_6e&x8m!mofryeaw775c&%-nc_)z)+p9w5@bw+(n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'flights.apps.FlightsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',  # new

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'airline.urls'

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

WSGI_APPLICATION = 'airline.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': os.environ['DATABASE_PORT'],
    }
}

print('DATABASE_NAME', os.environ['DATABASE_NAME'])
print('DATABASE_USER', os.environ['DATABASE_USER'])
print('DATABASE_PASSWORD', os.environ['DATABASE_PASSWORD'])
print('DATABASE_HOST', os.environ['DATABASE_HOST'])
print('DATABASE_PORT', os.environ['DATABASE_PORT'])

# Sample Database String from Heroku
# 'postgres://wvvgxgeoriumxg:c4e8612ae286a211a8c94976df0811e9b6fcdacb3ef3e468401e0619b38a1004@ec2-107-22-168-211.compute-1.amazonaws.com:5432/d5siauekbh9qlu'
# $dbconn = pg_connect("host=ec2-107-22-168-211.compute-1.amazonaws.com port=5432 dbname=d5siauekbh9qlu user=wvvgxgeoriumxg password=c4e8612ae286a211a8c94976df0811e9b6fcdacb3ef3e468401e0619b38a1004");

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
#        'HOST': '127.0.0.1', # localhost, local copy of postgres
        'HOST': 'db', # Docker copy of postgres
        'PORT': 5432,
        #'PORT': 5433,
    }
}

"""
if os.environ.get('TRAVIS_TEST_RESULT') == 0;
#if not 'TRAVIS' in os.environ:
    DATABASES = {}
    DATABASES['default'] = dj_database_url.config(conn_max_age=600)

    #DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

    #DATABASE_URL = os.environ.get('DATABASE_URL')
    # postgres://USER:PASSWORD@HOST:PORT/NAME
    #db_from_env = dj_database_url.config(default=DATABASE_URL, conn_max_age=500, ssl_require=True)
    #DATABASES['default'].update(db_from_env)
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'USER': 'postgres',
            'NAME': 'postgres',
            'HOST': 'db',
            'PORT': 5432,
            #'PORT': 5433,
        }
    }
"""

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = "/static/"


"""
if os.environ.get('TRAVIS_TEST_RESULT') == 0;
#if not 'TRAVIS' in os.environ:
    # Activate Django-Heroku.
    django_heroku.settings(locals())
"""
django_heroku.settings(locals())
