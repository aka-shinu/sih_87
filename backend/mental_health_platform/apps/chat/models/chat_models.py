"""
Chat models for AI conversation.
"""
from django.db import models


class ChatSession(models.Model):
    """Chat session model."""
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    session_id = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Session {self.session_id} - {self.user.email}"


class Message(models.Model):
    """Message model for chat."""
    MESSAGE_TYPES = [
        ('user', 'User'),
        ('ai', 'AI'),
        ('system', 'System'),
    ]

    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name='messages')
    message_type = models.CharField(max_length=10, choices=MESSAGE_TYPES)
    content = models.TextField()
    metadata = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message_type}: {self.content[:50]}..."


class AIResponse(models.Model):
    """AI response model."""
    message = models.OneToOneField(Message, on_delete=models.CASCADE, related_name='ai_response')
    sentiment = models.CharField(max_length=20)
    emotion = models.CharField(max_length=20)
    confidence = models.FloatField()
    crisis_risk = models.FloatField(default=0.0)
    response_type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AI Response: {self.sentiment} - {self.emotion}"
