from os import getenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = getenv('SECRET_KEY', 'unsafe')
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
    'django_filters',
    'rest_framework',
    'account',
    'article',
    'comment'
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

ROOT_URLCONF = 'fefu_wiki.urls'

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

WSGI_APPLICATION = 'fefu_wiki.wsgi.application'

# Database

DATABASES = {
    'default':
    {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': getenv('DATABASE_NAME'),
        'USER': getenv('POSTGRES_USER'),
        'PASSWORD': getenv('POSTGRES_PASSWORD'),
        'HOST': 'localhost',
        'PORT': getenv('DATABASE_PORT', '5432'),
    }
}

# Password validation

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
AUTH_USER_MODEL = 'account.User'

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'

# Media files

MEDIA_URL = 'media/'
MEDIA_ROOT = 'media'
# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DRF

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'account.pagination.DefaultPagination',
}


# Microsoft auth

MS_AZURE = {
    'CLIENT_ID': getenv('AZURE_CLIENT_ID'),
    'CLIENT_SECRET': getenv('AZURE_CLIENT_SECRET'),
    'AUTHORITY': rf'https://login.microsoftonline.com/{getenv("AZURE_TENANT")}',
    'SCOPE': ['email'],
    'SESSION_TYPE': 'filesystem',
    'REDIRECT_PATH': 'login/microsoft/getAToken',
    'FULL_REDIRECT_PATH': 'http://localhost:8000/login/microsoft/getAToken',
}

AUTHENTICATION_BACKENDS = ('account.backends.MSBackend',)
