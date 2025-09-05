"""
Trend analysis models.
"""
from django.db import models


class TrendAnalysis(models.Model):
    """Trend analysis model."""
    analysis_type = models.CharField(max_length=50)
    time_period = models.CharField(max_length=20)
    trend_direction = models.CharField(max_length=20)
    trend_strength = models.FloatField()
    data_points = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.analysis_type} - {self.trend_direction}"


class MentalHealthTrend(models.Model):
    """Mental health trend tracking."""
    metric_name = models.CharField(max_length=100)
    value = models.FloatField()
    period_start = models.DateTimeField()
    period_end = models.DateTimeField()
    trend_data = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.metric_name} - {self.value}"


class CrisisTrend(models.Model):
    """Crisis trend analysis."""
    date = models.DateField()
    crisis_count = models.IntegerField(default=0)
    severity_distribution = models.JSONField(default=dict)
    resolution_time_avg = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Crisis Trend - {self.date}: {self.crisis_count}"
