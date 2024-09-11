import environ

import os
from pathlib import Path



env = environ.Env(
    DEBUG=(bool, False)
)



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['127.0.0.1']

LOGIN_URL = "users:login"


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # tashqi paket
    "crispy_forms",
    "crispy_bootstrap5",
    # 'ckeditor',
    # 'ckeditor-uploader',

    # men yaratgan applar
    'users',
    'courses',
    # 'rest_framework',
    # 'paycomuz',
    # "payment",
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'users.middleware.SimpleMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
          BASE_DIR / "templates",
          # BASE_DIR / "business",
          # BASE_DIR / "professions/templates/professions",
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    # #  SQLite3 uchun
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    # PostgreSQL uchun
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'), # ASUS DB name="tbi_site", db ni nomini kiritamiz
        'HOST': env('DB_HOST'),# ['localhost', '127.0.0.1', '0.0.0.0'],
        'PORT': '5432',
        'USER': env('DB_USER'), # psql dagi user nomini kiritamiz
        'PASSWORD': env('DB_PASS'), # parolni kiritamiz
      }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'


USE_I18N = True
USE_TZ = True
AUTH_USER_MODEL = "users.CustomUser"


# LOGIN_REDIRECT_URL = 'dashboard'
# LOGOUT_REDIRECT_URL = 'landing_page'


MEDIA_URL = "/media/"
MEDIA_ROOT = "media-files"

MEDIAFILES_DIRS = [
      BASE_DIR / 'media-files',
      ]




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# STATIC_ROOT = BASE_DIR / 'static-files'
STATIC_ROOT = 'static-files'

STATICFILES_DIRS = [
      BASE_DIR / 'static',
      # BASE_DIR / 'static/images',
]
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]




# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = env('EMAIL_HOST_USER')
# # EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
# EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False


# localhost = "Server url bo'lishi kerak"
# CELERY_BROKER_URL = 'ampq://guest:guest@localhost:5672//'


# PAYCOM_SETTINGS = {
#     "KASSA_ID": "",  # token
#     "SECRET_KEY": "",  # password
#     "ACCOUNTS": {
#         "KEY": "order_id"
#     },
#     "TOKEN": ""
# }