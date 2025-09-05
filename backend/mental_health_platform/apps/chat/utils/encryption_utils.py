"""
Encryption utilities for chat messages.
"""
from cryptography.fernet import Fernet
from django.conf import settings
import base64
import hashlib


class MessageEncryption:
    """Message encryption utilities."""
    
    @staticmethod
    def get_encryption_key():
        """Get encryption key from settings."""
        key = getattr(settings, 'MESSAGE_ENCRYPTION_KEY', None)
        if not key:
            raise ValueError("MESSAGE_ENCRYPTION_KEY not set in settings")
        return key.encode() if isinstance(key, str) else key
    
    @staticmethod
    def encrypt_message(message_content):
        """Encrypt message content."""
        if not message_content:
            return message_content
        
        try:
            key = MessageEncryption.get_encryption_key()
            fernet = Fernet(key)
            encrypted_content = fernet.encrypt(message_content.encode())
            return base64.b64encode(encrypted_content).decode()
        except Exception as e:
            raise ValueError(f"Failed to encrypt message: {e}")
    
    @staticmethod
    def decrypt_message(encrypted_content):
        """Decrypt message content."""
        if not encrypted_content:
            return encrypted_content
        
        try:
            encrypted_data = base64.b64decode(encrypted_content.encode())
            key = MessageEncryption.get_encryption_key()
            fernet = Fernet(key)
            decrypted_content = fernet.decrypt(encrypted_data)
            return decrypted_content.decode()
        except Exception as e:
            raise ValueError(f"Failed to decrypt message: {e}")
    
    @staticmethod
    def generate_message_hash(content):
        """Generate hash for message integrity."""
        if not content:
            return None
        
        return hashlib.sha256(content.encode()).hexdigest()
    
    @staticmethod
    def verify_message_integrity(content, expected_hash):
        """Verify message integrity."""
        if not content or not expected_hash:
            return False
        
        actual_hash = MessageEncryption.generate_message_hash(content)
        return actual_hash == expected_hash
