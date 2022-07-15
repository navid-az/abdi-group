from django.utils.translation import gettext_lazy as _
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

with open(os.path.join(BASE_DIR, 'secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()

DEBUG = False

ALLOWED_HOSTS = ['abdi-group.com','www.abdi-group.com','www.abdi-group.ir','abdi-group.ir']
# ,'127.0.0.1'

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
    'capabilities.apps.CapabilitiesConfig',
    'product_and_services.apps.ProductAndServicesConfig',
    'company.apps.CompanyConfig',
    'mr_dr.apps.MrDrConfig',
    'news.apps.NewsConfig',
    #3rd party apps
    'ckeditor',
    'ckeditor_uploader',
    'jalali_date',
    'storages',
    'modeltranslation',
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

# postgres database (development)

# DATABASES = {
#     'default': {
#         'HOST':'127.0.0.1',
#         'ENGINE':'django.db.backends.postgresql',
#         'NAME':'abdigrou_database',
#         'USER':'abdigrou_navid',
#         'PASSWORD':'SQLelephantPoSt25',
#         'HOST':'127.0.0.1',
#     }
# }

# mySQL database

# development db
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'abdi_test',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#         'USER': 'root',
#         'PASSWORD': 'ds@51>_3iB#24',
#     }
# }

# main db
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'abdigrou_database',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'abdigrou_root',
        'PASSWORD': ']DI1+Qv{dxkB',
    }
}

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
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

# Media files 
# MEDIA_URL = 'media/'
# MEDIA_ROOT = BASE_DIR / 'media'

# ckeditor settings 
CKEDITOR_UPLOAD_PATH = "news-images/"

# https settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

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
EMAIL_HOST_PASSWORD = 'VM?FV#E(gBD&'
# EMAIL_HOST_PASSWORD = 'cjAFwV3pL9SmAqa'

# Jalali date settings
JALALI_DATE_DEFAULTS = {
   'Strftime': {
        'date': '%y/%m/%d',
        'datetime': '%H:%M:%S _ %y/%m/%d',
    },
    'Static': {
        'js': [
            'admin/js/django_jalali.min.js',
        ],
        'css': {
            'all': [
                'admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css',
            ]
        }
    },
}

#ARVAN CLOUD storages(MEDIA FILES)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = 'c9523f91-170f-4ceb-a60d-26fe2808b6eb'
AWS_SECRET_ACCESS_KEY = '50b6d4c78585b15bb6f1824fcd846b20abd19887c6964f5821402a0195089c09'
AWS_S3_ENDPOINT_URL = 'https://s3.ir-thr-at1.arvanstorage.com'
AWS_STORAGE_BUCKET_NAME = 'abdimedia'
AWS_SERVICE_NAME = 's3'
AWS_S3_FILE_OVERWRITE = False