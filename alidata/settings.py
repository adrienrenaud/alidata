"""
Django settings for alidata project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'alidata.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'alidata/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                # 'django.core.context_processors.request',
                # "django.contrib.auth.context_processors.auth",
                # "django.core.context_processors.debug",
                # "django.core.context_processors.i18n",
                # "django.core.context_processors.media",
                # "django.core.context_processors.static",
                # "django.core.context_processors.tz",
                # "django.contrib.messages.context_processors.messages",
                # "django.core.context_processors.media",
            ],
        },
    },
]



WSGI_APPLICATION = 'alidata.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
# }

# Update database configuration with $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'











STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'alidata/static'),
)



AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY_ID')



DEFAULT_FILE_STORAGE = 'alidata.s3utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'alidata.s3utils.StaticRootS3BotoStorage'     

if os.environ.get('ALIDATA_ENV_TYPE')=='STAGING':
    AWS_STORAGE_BUCKET_NAME = 'alidata-staging'
elif os.environ.get('ALIDATA_ENV_TYPE')=='PRODUCTION':
    AWS_STORAGE_BUCKET_NAME = 'alidata'
else:
    AWS_STORAGE_BUCKET_NAME = 'foo'
S3_URL = 'https://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'

MEDIA_URL = S3_URL + 'media/'
STATIC_URL = S3_URL + 'static/'

AWS_REDUCED_REDUNDANCY = False # We enable this server-wide on our staging server's S3 buckets
AWS_PRELOAD_METADATA = True # You want this to be on!






##########
#### FOR TESTING
if os.environ.get('ALIDATA_ENV_TYPE')=='DEVELOPMENT':
    DEBUG = True
    TEMPLATES[0]['OPTIONS']['debug'] = True

    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'    

    MEDIA_URL = '/media/'
    STATIC_URL = '/static/'

    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb2',
        'USER': 'postgres',
        'PASSWORD': os.environ.get('POSTGRES_PWD'),
        'HOST':'localhost',
        }
    }
    
    















