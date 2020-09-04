"""
Django settings for HonLecturer project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import urllib.parse as up
import psycopg2
import os
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '03m64d61xpfh=jp9sdonalpx@*8@g-)z4)ajl3z*(s^_)s_euu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


MESSAGE_TAGS = {
    messages.DEBUG:'alert-info',
    messages.INFO:'alert-info',
    messages.SUCCESS:'alert-success',
    messages.WARNING:'alert-warning',
    messages.ERROR:'alert-danger',
    
}



# Application definition


INSTALLED_APPS = [
    'GradeManager.apps.GrademanagerConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'HonLecturer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'HonLecturer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': "HonLecturerDB",
         'USER': 'postgres',
         #'PASSWORD': 'Ranti',
         'PASSWORD': 'Kenny1',
         'HOST': '127.0.0.1',
         'PORT': '5432',
 
    }
}


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


STATIC_URL = '/static/'
MEDIA_URL = '/mediauploaddir/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploaddir')

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

AUTHENTICATION_BACKENDS = ['GradeManager.EmailBackend.EmailBackend']
LOGIN_REDIRECT_URL = '/'
LOGIN_URL='login_view'
#BASE_URL = 'http://192.168.0.111/onlinecoursereg'  'http://192.168.0.111/WebResult.WebApi/api/Student/PythonScore'
#BASE_URL = 'http://192.168.0.111/WebResult.WebApi'
BASE_URL = 'http://192.168.8.102/WebResult.WebApi'
CIPHER_PASS='Deji1@Poly'
WORKSHEET_PASS ='Deji1@Poly'
WORKBOOKHASHED_PASSWORD="Akoms1@Poly"