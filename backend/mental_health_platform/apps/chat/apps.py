"""
Chat app configuration.
"""
from django.apps import AppConfig


class ChatConfig(AppConfig):
    """Chat app configuration."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mental_health_platform.apps.chat'
    verbose_name = 'AI Chat'
