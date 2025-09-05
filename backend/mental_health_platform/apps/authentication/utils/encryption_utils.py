"""
Encryption utilities for mental health platform.
"""
from cryptography.fernet import Fernet
from django.conf import settings
import base64
import hashlib


class EncryptionUtils:
    """Encryption utility functions."""
    
    @staticmethod
    def generate_key():
        """Generate encryption key."""
        return Fernet.generate_key()
    
    @staticmethod
    def get_encryption_key():
        """Get encryption key from settings."""
        key = getattr(settings, 'ENCRYPTION_KEY', None)
        if not key:
            raise ValueError("ENCRYPTION_KEY not set in settings")
        return key.encode() if isinstance(key, str) else key
    
    @staticmethod
    def encrypt_data(data):
        """Encrypt data."""
        if isinstance(data, str):
            data = data.encode()
        
        key = EncryptionUtils.get_encryption_key()
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)
        return base64.b64encode(encrypted_data).decode()
    
    @staticmethod
    def decrypt_data(encrypted_data):
        """Decrypt data."""
        try:
            encrypted_data = base64.b64decode(encrypted_data.encode())
            key = EncryptionUtils.get_encryption_key()
            fernet = Fernet(key)
            decrypted_data = fernet.decrypt(encrypted_data)
            return decrypted_data.decode()
        except Exception as e:
            raise ValueError(f"Failed to decrypt data: {e}")
    
    @staticmethod
    def hash_sensitive_data(data):
        """Hash sensitive data for storage."""
        if isinstance(data, str):
            data = data.encode()
        
        salt = getattr(settings, 'HASH_SALT', 'default_salt').encode()
        return hashlib.pbkdf2_hmac('sha256', data, salt, 100000).hex()
    
    @staticmethod
    def encrypt_pii(data):
        """Encrypt personally identifiable information."""
        return EncryptionUtils.encrypt_data(data)
    
    @staticmethod
    def decrypt_pii(encrypted_data):
        """Decrypt personally identifiable information."""
        return EncryptionUtils.decrypt_data(encrypted_data)


class DataAnonymization:
    """Data anonymization utilities."""
    
    @staticmethod
    def anonymize_email(email):
        """Anonymize email address."""
        if '@' not in email:
            return email
        
        local, domain = email.split('@', 1)
        if len(local) <= 2:
            return f"*@{domain}"
        
        return f"{local[0]}***{local[-1]}@{domain}"
    
    @staticmethod
    def anonymize_phone(phone):
        """Anonymize phone number."""
        if len(phone) <= 4:
            return "***"
        
        return f"{phone[:2]}***{phone[-2:]}"
    
    @staticmethod
    def anonymize_name(name):
        """Anonymize name."""
        if len(name) <= 2:
            return "***"
        
        return f"{name[0]}***{name[-1]}"
    
    @staticmethod
    def anonymize_user_data(user_data):
        """Anonymize user data for analytics."""
        anonymized = user_data.copy()
        
        if 'email' in anonymized:
            anonymized['email'] = DataAnonymization.anonymize_email(anonymized['email'])
        
        if 'phone' in anonymized:
            anonymized['phone'] = DataAnonymization.anonymize_phone(anonymized['phone'])
        
        if 'name' in anonymized:
            anonymized['name'] = DataAnonymization.anonymize_name(anonymized['name'])
        
        return anonymized
