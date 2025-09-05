"""
Behavioral analysis models for mental health.
"""
from django.db import models


class BehavioralPattern(models.Model):
    """User behavioral pattern analysis."""
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE, null=True, blank=True)
    pattern_type = models.CharField(max_length=50)
    pattern_data = models.JSONField(default=dict)
    confidence = models.FloatField()
    is_anonymized = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Behavioral Pattern - {self.pattern_type}"


class EngagementMetrics(models.Model):
    """User engagement metrics."""
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE, null=True, blank=True)
    login_frequency = models.FloatField()
    session_duration = models.FloatField()
    message_frequency = models.FloatField()
    response_time = models.FloatField()
    feature_usage = models.JSONField(default=dict)
    is_anonymized = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Engagement Metrics - {self.login_frequency}"


class StressIndicator(models.Model):
    """Stress indicator analysis."""
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE, null=True, blank=True)
    stress_level = models.FloatField()
    indicators = models.JSONField(default=list)
    severity = models.CharField(max_length=20)
    is_anonymized = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Stress Indicator - {self.stress_level:.2f}"
