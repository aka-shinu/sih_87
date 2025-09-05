"""
Statistics models for analytics.
"""
from django.db import models


class DailyStatistics(models.Model):
    """Daily aggregated statistics."""
    date = models.DateField(unique=True)
    total_users = models.IntegerField(default=0)
    active_users = models.IntegerField(default=0)
    total_messages = models.IntegerField(default=0)
    positive_sentiment_ratio = models.FloatField(default=0.0)
    negative_sentiment_ratio = models.FloatField(default=0.0)
    crisis_alerts = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Daily Stats - {self.date}"


class UserStatistics(models.Model):
    """User-specific statistics."""
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    total_sessions = models.IntegerField(default=0)
    total_messages = models.IntegerField(default=0)
    avg_sentiment = models.FloatField(default=0.0)
    crisis_incidents = models.IntegerField(default=0)
    last_activity = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Stats for {self.user.email}"


class SentimentAnalysis(models.Model):
    """Sentiment analysis data."""
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE, null=True, blank=True)
    message_content = models.TextField()
    sentiment = models.CharField(max_length=20)
    confidence = models.FloatField()
    emotion = models.CharField(max_length=20)
    is_anonymized = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sentiment: {self.sentiment} - {self.confidence:.2f}"
