from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent # Build paths inside the project like this: BASE_DIR / 'subdir'.

SECRET_KEY = 'django-insecure-b%4=6j-#r&&4hbj_is(aunv^q2cma-pu9(i=q8^!z)0ynd1%id'# SECURITY WARNING: keep the secret key used in production secret!

DEBUG = True# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',
    'webpack_loader',
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

ROOT_URLCONF = 'aws.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
		,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'aws.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'rhd_db',
		'USER': 'rh_user',
		'PASSWORD': '123',
		'HOST': 'localhost',  # Host (can remain as localhost for now)
		'PORT': '5432',  # Default PostgreSQL port
	}
}



# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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

# https://docs.djangoproject.com/en/5.2/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images) # https://docs.djangoproject.com/en/5.2/howto/static-files/
STATIC_URL = 'static/'
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'static'), # serve static files in dev
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' # Default primary key field type # https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

WEBPACK_LOADER = {
	'DEFAULT': {
		'BUNDLE_DIR_NAME': 'bundles/',  # Directory where Webpack outputs files
		'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),  # Used by webpack-bundle-tracker
	}
}

