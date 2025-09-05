"""
Authentication utilities for mental health platform.
"""
import hashlib
import secrets
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta


class AuthUtils:
    """Authentication utility functions."""
    
    @staticmethod
    def generate_verification_token():
        """Generate email verification token."""
        return secrets.token_urlsafe(32)
    
    @staticmethod
    def generate_password_reset_token():
        """Generate password reset token."""
        return secrets.token_urlsafe(32)
    
    @staticmethod
    def hash_password(password):
        """Hash password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()
    
    @staticmethod
    def send_verification_email(user, token):
        """Send email verification."""
        subject = 'Verify your email - Mental Health Platform'
        message = f"""
        Hi {user.username},
        
        Please click the link below to verify your email:
        {settings.FRONTEND_URL}/verify-email/{token}
        
        This link will expire in 24 hours.
        
        Best regards,
        Mental Health Platform Team
        """
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
    
    @staticmethod
    def send_password_reset_email(user, token):
        """Send password reset email."""
        subject = 'Reset your password - Mental Health Platform'
        message = f"""
        Hi {user.username},
        
        You requested a password reset. Click the link below to reset your password:
        {settings.FRONTEND_URL}/reset-password/{token}
        
        This link will expire in 1 hour.
        
        If you didn't request this, please ignore this email.
        
        Best regards,
        Mental Health Platform Team
        """
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])


class SessionUtils:
    """Session utility functions."""
    
    @staticmethod
    def is_session_valid(session_key):
        """Check if session is valid."""
        try:
            from django.contrib.sessions.models import Session
            session = Session.objects.get(session_key=session_key)
            return session.expire_date > timezone.now()
        except:
            return False
    
    @staticmethod
    def get_user_from_session(session_key):
        """Get user from session key."""
        try:
            from django.contrib.sessions.models import Session
            session = Session.objects.get(session_key=session_key)
            user_id = session.get_decoded().get('_auth_user_id')
            if user_id:
                return User.objects.get(id=user_id)
        except:
            pass
        return None
    
    @staticmethod
    def extend_session(session, hours=24):
        """Extend session expiration."""
        session.set_expiry(timezone.now() + timedelta(hours=hours))
        session.save()
