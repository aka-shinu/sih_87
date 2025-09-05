"""
Crisis detection models for mental health.
"""
from django.db import models


class CrisisDetection(models.Model):
    """Crisis detection analysis."""
    RISK_LEVELS = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]

    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE, null=True, blank=True)
    message_content = models.TextField()
    risk_level = models.CharField(max_length=10, choices=RISK_LEVELS)
    risk_score = models.FloatField()
    keywords_found = models.JSONField(default=list)
    confidence = models.FloatField()
    is_anonymized = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Crisis Detection - {self.risk_level}"


class CrisisIntervention(models.Model):
    """Crisis intervention tracking."""
    detection = models.ForeignKey(CrisisDetection, on_delete=models.CASCADE)
    intervention_type = models.CharField(max_length=50)
    response_time = models.FloatField()
    resolution_status = models.CharField(max_length=20)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Intervention - {self.intervention_type}"


class CrisisAlert(models.Model):
    """Crisis alert system."""
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE, null=True, blank=True)
    alert_type = models.CharField(max_length=50)
    severity = models.CharField(max_length=20)
    message = models.TextField()
    is_resolved = models.BooleanField(default=False)
    resolved_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Crisis Alert - {self.alert_type}"
