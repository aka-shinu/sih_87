"""
Blockchain app configuration.
"""
from django.apps import AppConfig


class BlockchainConfig(AppConfig):
    """Blockchain app configuration."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mental_health_platform.apps.blockchain'
    verbose_name = 'Blockchain'
