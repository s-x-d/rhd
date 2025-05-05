from .base import *
import os

SET ENV VARS
eb setenv DJANGO_SECRET_KEY='++u08fgezk9(tv)vyliz3b!tgh*s@p@phs$3v8i80)%e@&b4254721' DJANGO_SETTINGS_MODULE=aws.settings DB_NAME=rhd_db DB_USER=_db_master DB_PASSWORD=QZgU5CUZm2MQKENld02B DB_HOST=rh-db.c98es86wumdc.eu-west-2.rds.amazonaws.com DB_PORT=5432 DEBUG=False

# ADDED FROM LOCAL to get py manage.py runserver --settings=aws.settings.prod to work -----------------------------------------------------------------
os.environ.setdefault('DB_NAME', 'rhd_db')
os.environ.setdefault('DB_USER', 'rh_user')
os.environ.setdefault('DB_PASSWORD', '123')
os.environ.setdefault('DB_HOST', 'localhost')
os.environ.setdefault('DB_PORT', '5432')

os.environ.setdefault('DJANGO_SECRET_KEY', '++u08#fgezk9(tv)vyliz3b!tgh*s@p@p#hs$3v8i80)%e@&b4')
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY') # Add this line to actually set the SECRET_KEY in Django settings
#----------------------------------------------------------------------------------------------------------------------------


# Security settings
DEBUG = False  # Changed from True since this is production
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# Admin settings (keep as is)
ADMINS = [
    ('Robin H', 'robinxhowland@gmail.com'),
]

# Host settings (keep as is)
ALLOWED_HOSTS = [
    'sc-app-env.eba-irvhxx4x.eu-west-2.elasticbeanstalk.com/',
    'skynetcoder.com',
    'www.skynetcoder.com',  # Added www subdomain
    '13.43.110.179',
    'localhost',
    '127.0.0.1',
] + os.environ.get('ALLOWED_HOSTS', '').split(',')

# Database settings (keep as is)
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
STATIC_ROOT = '/var/www/skynetcoder.com/static'  # Changed to match Nginx config
STATIC_URL = '/static/'
MEDIA_ROOT = '/var/www/skynetcoder.com/media'
MEDIA_URL = '/media/'

# Remove STATICFILES_DIRS from base.py in production
STATICFILES_DIRS = []

# Security settings
SECURE_SSL_REDIRECT = False  # Changed to False until we set up SSL
SESSION_COOKIE_SECURE = False  # Changed to False until we set up SSL
CSRF_COOKIE_SECURE = False  # Changed to False until we set up SSL
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Add this for proper proxy handling
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
