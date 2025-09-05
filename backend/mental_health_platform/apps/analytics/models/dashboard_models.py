"""
Dashboard models for admin interface.
"""
from django.db import models


class DashboardWidget(models.Model):
    """Dashboard widget configuration."""
    WIDGET_TYPES = [
        ('chart', 'Chart'),
        ('metric', 'Metric'),
        ('table', 'Table'),
        ('alert', 'Alert'),
    ]

    name = models.CharField(max_length=100)
    widget_type = models.CharField(max_length=20, choices=WIDGET_TYPES)
    config = models.JSONField(default=dict)
    is_active = models.BooleanField(default=True)
    position = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.widget_type}"


class DashboardLayout(models.Model):
    """Dashboard layout configuration."""
    name = models.CharField(max_length=100)
    layout_config = models.JSONField(default=dict)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AlertRule(models.Model):
    """Alert rule configuration."""
    name = models.CharField(max_length=100)
    condition = models.JSONField()
    threshold = models.FloatField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert: {self.name}"
