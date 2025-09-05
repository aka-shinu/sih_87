"""
Session management models.
"""
from django.db import models
from django.contrib.sessions.models import Session


class UserSession(models.Model):
    """Extended user session model."""
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    session = models.OneToOneField(Session, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} - {self.session.session_key}"


class LoginAttempt(models.Model):
    """Login attempt tracking model."""
    email = models.EmailField()
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    success = models.BooleanField(default=False)
    failure_reason = models.CharField(max_length=100, blank=True)
    attempted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {'Success' if self.success else 'Failed'}"
