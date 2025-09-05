"""
Resources app configuration.
"""
from django.apps import AppConfig


class ResourcesConfig(AppConfig):
    """Resources app configuration."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mental_health_platform.apps.resources'
    verbose_name = 'Resources'
