"""
Django settings for staking project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-^+xa-i63v4%v4*i#el^nbff4l^6wajjggeh3d6mva9a+maddl4"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Users",
    "Investment",
    "django_celery_beat",
    "compressor",
    'livereload',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'livereload.middleware.LiveReloadScript',
]

ROOT_URLCONF = "staking.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "staking.context_processors.fetch_and_save_data",
            ],
        },
    },
]

WSGI_APPLICATION = "staking.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

from urllib.parse import urlparse

# Obtener la URL de la base de datos desde las variables de entorno
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgres://tu_usuario:tu_contraseña@db:5432/tu_proyecto_db"
)

# Parsear la URL de la base de datos
db_info = urlparse(DATABASE_URL)

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': db_info.path[1:],  # Nombre de la base de datos
#         'USER': db_info.username,   # Usuario
#         'PASSWORD': db_info.password,  # Contraseña
#         'HOST': db_info.hostname,   # Host (en este caso, el servicio `db` en Docker)
#         'PORT': db_info.port or 5432,  # Puerto
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "OPTIONS": {},
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = "/media/"  # URL base para servir archivos multimedia
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Configuración de Celery
CELERY_BROKER_URL = "redis://localhost:6379/0"  # URL de Redis
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"  # Almacenamiento de resultados
CELERY_TIMEZONE = "UTC"  # Zona horaria


CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers.DatabaseScheduler"
CELERY_TASK_ALWAYS_EAGER = False

# from celery.schedules import crontab

# CELERY_BEAT_SCHEDULE = {
#     'increment-account-balance': {
#         'task': 'Investment.tasks.process_pending_deposits',
#         'schedule': crontab(minute=0, hour=0),  # Ejecuta la tarea diariamente a las 00:00
#     },
# }

COMPRESS_ROOT = BASE_DIR / "static"

COMPRESS_ENABLED = True

STATICFILES_FINDERS = ("compressor.finders.CompressorFinder",)
