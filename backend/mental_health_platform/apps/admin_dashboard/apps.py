"""
Admin Dashboard app configuration.
"""
from django.apps import AppConfig


class AdminDashboardConfig(AppConfig):
    """Admin Dashboard app configuration."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mental_health_platform.apps.admin_dashboard'
    verbose_name = 'Admin Dashboard'
