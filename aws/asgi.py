"""
ASGI config for aws project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Use production settings by default for AWS deployment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aws.settings.prod')

application = get_asgi_application()
