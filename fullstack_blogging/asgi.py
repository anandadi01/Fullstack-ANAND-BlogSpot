"""
ASGI config for fullstack_blogging project.

It exposes the ASGI callable as a module-level variable named ``app``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fullstack_blogging.settings')

app = get_asgi_application()
