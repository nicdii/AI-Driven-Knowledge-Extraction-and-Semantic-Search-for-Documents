"""
Django settings for search_system project.
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# --------------------------------------------------

# Base Directory

# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
# --------------------------------------------------

# Environment Variables

# --------------------------------------------------

load_dotenv(BASE_DIR / ".env")

# --------------------------------------------------

# Security

# --------------------------------------------------

SECRET_KEY = os.getenv(
"DJANGO_SECRET_KEY",
"django-insecure-development-key"
)

DEBUG = os.getenv(
"DJANGO_DEBUG",
"True"
).lower() == "true"

ALLOWED_HOSTS = [
host.strip()
for host in os.getenv(
"DJANGO_ALLOWED_HOSTS",
"127.0.0.1,localhost"
).split(",")
]

# --------------------------------------------------

# Installed Apps

# --------------------------------------------------

INSTALLED_APPS = [


# Django Apps
"django.contrib.admin",
"django.contrib.auth",
"django.contrib.contenttypes",
"django.contrib.sessions",
"django.contrib.messages",
"django.contrib.staticfiles",

# Third Party Apps
"rest_framework",

# Local Apps
"accounts",
"documents",
"ocr",
"metadata_extraction",
"embeddings",
"retrieval",
"api",
"chatbot",
]

# --------------------------------------------------

# Middleware

# --------------------------------------------------

MIDDLEWARE = [
"django.middleware.security.SecurityMiddleware",
"django.contrib.sessions.middleware.SessionMiddleware",
"django.middleware.common.CommonMiddleware",
"django.middleware.csrf.CsrfViewMiddleware",
"django.contrib.auth.middleware.AuthenticationMiddleware",
"django.contrib.messages.middleware.MessageMiddleware",
"django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# --------------------------------------------------

# URLs

# --------------------------------------------------

ROOT_URLCONF = "search_system.urls"

# --------------------------------------------------

# Templates

# --------------------------------------------------

TEMPLATES = [
{
"BACKEND": "django.template.backends.django.DjangoTemplates",

    "DIRS": [
        BASE_DIR / "templates",
    ],

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

# --------------------------------------------------

# WSGI

# --------------------------------------------------

WSGI_APPLICATION = "search_system.wsgi.application"

# --------------------------------------------------

# Database

# --------------------------------------------------

USE_SQLITE_FALLBACK = (
os.getenv(
"USE_SQLITE_FALLBACK",
"False"
).lower() == "true"
)

if USE_SQLITE_FALLBACK:


    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


else:

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",

            "NAME": os.getenv(
                "POSTGRES_DB",
                "search_system"
            ),

            "USER": os.getenv(
                "POSTGRES_USER",
                "postgres"
            ),

            "PASSWORD": os.getenv(
                "POSTGRES_PASSWORD",
                ""
            ),

            "HOST": os.getenv(
                "POSTGRES_HOST",
                "localhost"
            ),

            "PORT": os.getenv(
                "POSTGRES_PORT",
                "5432"
            ),
        }
}


# --------------------------------------------------

# Password Validation

# --------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
{
"NAME":
"django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
},
{
"NAME":
"django.contrib.auth.password_validation.MinimumLengthValidator"
},
{
"NAME":
"django.contrib.auth.password_validation.CommonPasswordValidator"
},
{
"NAME":
"django.contrib.auth.password_validation.NumericPasswordValidator"
},
]

# --------------------------------------------------

# Internationalization

# --------------------------------------------------

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True

# --------------------------------------------------

# Static Files

# --------------------------------------------------

STATIC_URL = "/static/"

STATICFILES_DIRS = [
BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

# --------------------------------------------------

# Media Files

# --------------------------------------------------

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"

# --------------------------------------------------

# Authentication

# --------------------------------------------------

LOGIN_URL = "accounts:login"

LOGIN_REDIRECT_URL = "/"

LOGOUT_REDIRECT_URL = "/"

# --------------------------------------------------

# REST Framework

# --------------------------------------------------

REST_FRAMEWORK = {


"DEFAULT_PERMISSION_CLASSES": [
    "rest_framework.permissions.IsAuthenticated",
],

"DEFAULT_AUTHENTICATION_CLASSES": [
    "rest_framework.authentication.SessionAuthentication",
],


}

# --------------------------------------------------

# OCR Settings

# --------------------------------------------------

TESSERACT_PATH = os.getenv(
"TESSERACT_PATH",
""
)

POPPLER_PATH = os.getenv(
"POPPLER_PATH",
""
)

OCR_LANGUAGE = os.getenv(
"OCR_LANGUAGE",
"eng+pan"
)

# --------------------------------------------------

# Logging

# --------------------------------------------------

LOGGING = {
"version": 1,


"disable_existing_loggers": False,

"formatters": {
    "standard": {
        "format":
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    },
},

"handlers": {

    "file": {
        "class": "logging.FileHandler",
        "filename": BASE_DIR / "logs/app.log",
        "formatter": "standard",
        "level": "INFO",
    },

    "console": {
        "class": "logging.StreamHandler",
        "formatter": "standard",
        "level": "INFO",
    },
},

"root": {
    "handlers": ["file", "console"],
    "level": "INFO",
},


}

# --------------------------------------------------

# Default Primary Key

# --------------------------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# git remote add origin https://github.com/nicdii/AI-Driven-Knowledge-Extraction-and-Semantic-Search-for-Documents.git