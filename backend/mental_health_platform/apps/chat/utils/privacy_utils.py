"""
Privacy utilities for mental health platform.
"""
import hashlib
import secrets
from django.conf import settings
from cryptography.fernet import Fernet
import base64


class PrivacyUtils:
    """Privacy protection utilities."""
    
    @staticmethod
    def encrypt_message_content(content):
        """Encrypt message content."""
        if not content:
            return content
        
        try:
            key = settings.ENCRYPTION_KEY.encode() if isinstance(settings.ENCRYPTION_KEY, str) else settings.ENCRYPTION_KEY
            fernet = Fernet(key)
            encrypted_content = fernet.encrypt(content.encode())
            return base64.b64encode(encrypted_content).decode()
        except Exception:
            return content  # Return original if encryption fails
    
    @staticmethod
    def decrypt_message_content(encrypted_content):
        """Decrypt message content."""
        if not encrypted_content:
            return encrypted_content
        
        try:
            encrypted_data = base64.b64decode(encrypted_content.encode())
            key = settings.ENCRYPTION_KEY.encode() if isinstance(settings.ENCRYPTION_KEY, str) else settings.ENCRYPTION_KEY
            fernet = Fernet(key)
            decrypted_content = fernet.decrypt(encrypted_data)
            return decrypted_content.decode()
        except Exception:
            return encrypted_content  # Return original if decryption fails
    
    @staticmethod
    def anonymize_message_for_analytics(message_content):
        """Anonymize message content for analytics."""
        if not message_content:
            return message_content
        
        # Remove personal identifiers
        import re
        
        # Remove email addresses
        message_content = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[EMAIL]', message_content)
        
        # Remove phone numbers
        message_content = re.sub(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', '[PHONE]', message_content)
        
        # Remove names (simple heuristic)
        message_content = re.sub(r'\b[A-Z][a-z]+ [A-Z][a-z]+\b', '[NAME]', message_content)
        
        # Remove specific numbers (SSN, etc.)
        message_content = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', '[SSN]', message_content)
        
        return message_content
    
    @staticmethod
    def generate_message_hash(content):
        """Generate hash for message content."""
        if not content:
            return None
        
        # Use SHA-256 for content hashing
        return hashlib.sha256(content.encode()).hexdigest()
    
    @staticmethod
    def is_sensitive_content(content):
        """Check if content contains sensitive information."""
        if not content:
            return False
        
        sensitive_patterns = [
            r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',  # Phone numbers
            r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # Email
            r'\b\d{3}-\d{2}-\d{4}\b',  # SSN
            r'\b[A-Z][a-z]+ [A-Z][a-z]+\b',  # Names
        ]
        
        import re
        for pattern in sensitive_patterns:
            if re.search(pattern, content):
                return True
        
        return False
    
    @staticmethod
    def sanitize_content_for_storage(content):
        """Sanitize content before storage."""
        if not content:
            return content
        
        # Remove null bytes and control characters
        content = content.replace('\x00', '')
        content = ''.join(char for char in content if ord(char) >= 32 or char in '\n\r\t')
        
        # Limit length
        max_length = getattr(settings, 'MAX_MESSAGE_LENGTH', 5000)
        if len(content) > max_length:
            content = content[:max_length] + '...'
        
        return content


class DataRetentionUtils:
    """Data retention utilities."""
    
    @staticmethod
    def should_retain_message(message, retention_days=365):
        """Check if message should be retained based on policy."""
        from django.utils import timezone
        from datetime import timedelta
        
        if not message.created_at:
            return True
        
        cutoff_date = timezone.now() - timedelta(days=retention_days)
        return message.created_at > cutoff_date
    
    @staticmethod
    def anonymize_old_messages():
        """Anonymize old messages for long-term storage."""
        from ..models.chat_models import Message
        from django.utils import timezone
        from datetime import timedelta
        
        # Find messages older than 1 year
        cutoff_date = timezone.now() - timedelta(days=365)
        old_messages = Message.objects.filter(created_at__lt=cutoff_date, is_anonymized=False)
        
        anonymized_count = 0
        for message in old_messages:
            # Anonymize content
            message.content = PrivacyUtils.anonymize_message_for_analytics(message.content)
            message.is_anonymized = True
            message.save()
            anonymized_count += 1
        
        return anonymized_count
