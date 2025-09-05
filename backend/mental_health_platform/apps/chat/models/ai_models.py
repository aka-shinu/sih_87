"""
AI processing models.
"""
from django.db import models


class AIModel(models.Model):
    """AI model configuration."""
    name = models.CharField(max_length=100, unique=True)
    model_type = models.CharField(max_length=50)
    version = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    config = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} v{self.version}"


class AIAnalysis(models.Model):
    """AI analysis results."""
    message = models.ForeignKey('chat.Message', on_delete=models.CASCADE)
    model = models.ForeignKey(AIModel, on_delete=models.CASCADE)
    analysis_type = models.CharField(max_length=50)
    result = models.JSONField()
    confidence = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.analysis_type} - {self.confidence:.2f}"


class CrisisAlert(models.Model):
    """Crisis alert model."""
    ALERT_LEVELS = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]

    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    message = models.ForeignKey('chat.Message', on_delete=models.CASCADE)
    alert_level = models.CharField(max_length=10, choices=ALERT_LEVELS)
    risk_score = models.FloatField()
    is_resolved = models.BooleanField(default=False)
    resolved_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Crisis Alert: {self.alert_level} - {self.user.email}"
