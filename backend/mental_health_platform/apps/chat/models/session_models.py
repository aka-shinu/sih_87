"""
Chat session management models.
"""
from django.db import models


class ChatSessionState(models.Model):
    """Chat session state model."""
    session = models.OneToOneField('chat.ChatSession', on_delete=models.CASCADE)
    current_context = models.JSONField(default=dict)
    user_preferences = models.JSONField(default=dict)
    conversation_history = models.JSONField(default=list)
    last_activity = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"State for {self.session.session_id}"


class ChatMetrics(models.Model):
    """Chat metrics model."""
    session = models.ForeignKey('chat.ChatSession', on_delete=models.CASCADE)
    total_messages = models.IntegerField(default=0)
    user_messages = models.IntegerField(default=0)
    ai_messages = models.IntegerField(default=0)
    avg_response_time = models.FloatField(default=0.0)
    sentiment_trend = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Metrics for {self.session.session_id}"
