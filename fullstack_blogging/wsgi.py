"""
WSGI config for fullstack_blogging project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fullstack_blogging.settings')

app = get_wsgi_application()
# app = app

def handler(event, context):
    response = app(event['body'], event['headers'])
    return{
        'statusCode': response.status_code,  
        'body': response.content,  
        'headers': dict(response.headers)
    }