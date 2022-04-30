from tkinter.tix import Tree
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open(os.path.join(BASE_DIR, 'secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['abdi-group.com','www.abdi-group.com','www.abdi-group.ir','abdi-group.ir']
# ,'127.0.0.1'

# Application definition

INSTALLED_APPS = [
    # whitenoise enable in development 
    "whitenoise.runserver_nostatic",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # apps
    'home.apps.HomeConfig',
    'capabilities.apps.CapabilitiesConfig',
    'product_and_services.apps.ProductAndServicesConfig',
    'company.apps.CompanyConfig',
    'mr_dr.apps.MrDrConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # white noise 
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # translation
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'abdiGroup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR/'templates' ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'abdiGroup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'HOST': '127.0.0.1'
        'ENGINE':'django.db.backends.postgresql',
        'NAME':'abdigrou_database',
        'USER':'abdigrou_navid',
        'PASSWORD':'SQLelephantPoSt25',
        'HOST':'127.0.0.1',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE':'django.db.backends.postgresql',
#         'NAME':'abdi-group-database',
#         'USER':'postgres',
#         'PASSWORD':'SQLelephantPoSt25',
#         'HOST':'localhost',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('fa', _('Persian')),
    ('en', _('English')),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

# https settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# email 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.abdi-group.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'mr.dr@abdi-group.com'
EMAIL_HOST_PASSWORD = 'cjAFwV3pL9SmAqa'
