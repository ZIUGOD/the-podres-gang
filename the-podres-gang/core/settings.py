# First, you start. Then, you grow and improve."

from pathlib import Path
from os import path
from django.core.management.utils import get_random_secret_key
import environ

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

SECRET_KEY = env("SECRET_KEY", default=get_random_secret_key())

DEBUG = env("DEBUG", default=False)

ALLOWED_HOSTS = env("ALLOWED_HOSTS", default="127.0.0.1, localhost").split(" ")

DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",  # Enables the Django admin site, allowing for administrative tasks and data management.
    "django.contrib.auth",  # Provides authentication support, including user accounts, permissions, and groups.
    "django.contrib.contenttypes",  # Manages content types, allowing for generic relationships between models.
    "django.contrib.sessions",  # Implements session management, enabling the storage of user-specific data across requests.
    "django.contrib.messages",  # Facilitates messaging framework, allowing for the display of one-time notifications to users.
    "django.contrib.staticfiles",  # Handles the management and serving of static files (CSS, JavaScript, images).
    # Custom applications bellow
    "features.gallery",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

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
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
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

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

MEDIA_URL = '/media/'
MEDIA_ROOT = path.join(BASE_DIR, 'media')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# Static files
STATIC_URL = "/static/"
STATICFILES_DIRS = [path.join(BASE_DIR, "static")]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = BASE_DIR / "static_django"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



# .########.####.##.....##..######....#######..########.
# ......##...##..##.....##.##....##..##.....##.##.....##
# .....##....##..##.....##.##........##.....##.##.....##
# ....##.....##..##.....##.##...####.##.....##.##.....##
# ...##......##..##.....##.##....##..##.....##.##.....##
# ..##.......##..##.....##.##....##..##.....##.##.....##
# .########.####..#######...######....#######..########.