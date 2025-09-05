"""
Analytics app configuration.
"""
from django.apps import AppConfig


class AnalyticsConfig(AppConfig):
    """Analytics app configuration."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mental_health_platform.apps.analytics'
    verbose_name = 'Analytics'
