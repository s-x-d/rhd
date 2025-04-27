from .base import *
import os
from pathlib import Path

# Security settings
DEBUG = True
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# Admin settings
ADMINS = [
    ('Robin H', 'robinxhowland@gmail.com'),
]

# Host settings
ALLOWED_HOSTS = [
    'ec2-13-43-110-179.eu-west-2.compute.amazonaws.com',
    'skynetcoder.com',
    '13.43.110.179',
    'localhost',
    '127.0.0.1',
] + os.environ.get('ALLOWED_HOSTS', '').split(',')

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Static files settings
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
