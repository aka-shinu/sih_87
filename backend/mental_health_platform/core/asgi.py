"""
ASGI config for mental health platform.
"""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mental_health_platform.core.settings.development')
application = get_asgi_application()
