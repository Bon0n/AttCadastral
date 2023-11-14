"""
Django settings for cadastro project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

import export

from .get_config import config
import ldap
from django_auth_ldap.config import LDAPSearch, LDAPGroupQuery, GroupOfNamesType, PosixGroupType

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fy&y9sdxd03xsrr492m+8qj72uv4b$jpy5$s=4!#kgpvw+kizp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_att_cadastro',
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

ROOT_URLCONF = 'cadastro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'app_att_cadastro/templates')],
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

WSGI_APPLICATION = 'cadastro.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

params = config(section='postgresql')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': params['database'],
        'USER': params['user'],
        'PASSWORD': params['password'],
        'HOST': params['host'],
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

AUTH_LDAP_SERVER_URI = 'ldap://networksecuritybr.local:389'
AUTH_LDAP_BIND_DN = 'CN=Andrei Bonon de Oliveira,OU=INFRAESTRUTURA SUPORTE TI,OU=USUARIOS,OU=FITCARD,OU=CORP,DC=networksecuritybr,DC=local'
AUTH_LDAP_BIND_PASSWORD = 'Mudar@123'
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    'OU=INFRAESTRUTURA SUPORTE TI,OU=USUARIOS,OU=FITCARD,OU=CORP,DC=networksecuritybr,DC=local', ldap.SCOPE_SUBTREE,
    '(sAMAccountName=%(user)s)')
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    'CN=FITCARD-INFRAESTRUTURA-SUPORTE,OU=ACESSO,OU=GRUPOS,OU=FITCARD,OU=CORP,DC=networksecuritybr,DC=local',
    ldap.SCOPE_SUBTREE, '(objectClass=groupOfNames)')
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()
AUTH_LDAP_MIRROR_GROUPS = True

# Populate the Django user from the LDAP directory.
AUTH_LDAP_REQUIRE_GROUP = 'CN=G_ACESSO_WIFI,OU=GRUPOS,OU=GERAL,OU=CORP,DC=networksecuritybr,DC=local'

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
    "username": "uid",
    "password": "userPassword",
}
AUTH_LDAP_PROFILE_ATTR_MAP = {
    "home_directory": "homeDirectory"
}
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "CN=G_ACESSO_WIFI,OU=GRUPOS,OU=GERAL,OU=CORP,DC=networksecuritybr,DC=local",
    "is_staff": "CN=FITCARD-INFRAESTRUTURA-SUPORTE,OU=ACESSO,OU=GRUPOS,OU=FITCARD,OU=CORP,DC=networksecuritybr,DC=local",
    "is_superuser": "CN=FITCARD-INFRAESTRUTURA-SUPORTE,OU=ACESSO,OU=GRUPOS,OU=FITCARD,OU=CORP,DC=networksecuritybr,DC=local"
}

AUTH_LDAP_ALWAYS_UPDATE_USER = True
AUTH_LDAP_FIND_GROUP_PERMS = True
AUTH_LDAP_CACHE_TIMEOUT = 3600

# Keep ModelBackend around for per-user permissions and maybe a local
# superuser.
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
