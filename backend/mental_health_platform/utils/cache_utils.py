"""
Redis caching utilities for mental health platform.
"""
import redis
from django.conf import settings
import json
import logging

logger = logging.getLogger(__name__)


class CacheManager:
    """Redis cache management."""
    
    def __init__(self):
        self.redis_client = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            decode_responses=True
        )
    
    def get(self, key):
        """Get value from cache."""
        try:
            value = self.redis_client.get(key)
            return json.loads(value) if value else None
        except Exception as e:
            logger.error(f"Cache get error: {e}")
            return None
    
    def set(self, key, value, timeout=3600):
        """Set value in cache with timeout."""
        try:
            serialized_value = json.dumps(value)
            return self.redis_client.setex(key, timeout, serialized_value)
        except Exception as e:
            logger.error(f"Cache set error: {e}")
            return False
    
    def delete(self, key):
        """Delete key from cache."""
        try:
            return self.redis_client.delete(key)
        except Exception as e:
            logger.error(f"Cache delete error: {e}")
            return False
    
    def exists(self, key):
        """Check if key exists in cache."""
        try:
            return self.redis_client.exists(key)
        except Exception as e:
            logger.error(f"Cache exists error: {e}")
            return False


class AnalyticsCache:
    """Analytics-specific caching."""
    
    def __init__(self):
        self.cache = CacheManager()
        self.analytics_prefix = "analytics:"
    
    def get_daily_stats(self, date):
        """Get daily statistics from cache."""
        key = f"{self.analytics_prefix}daily:{date}"
        return self.cache.get(key)
    
    def set_daily_stats(self, date, stats):
        """Cache daily statistics."""
        key = f"{self.analytics_prefix}daily:{date}"
        return self.cache.set(key, stats, timeout=86400)
    
    def get_user_stats(self, user_id):
        """Get user statistics from cache."""
        key = f"{self.analytics_prefix}user:{user_id}"
        return self.cache.get(key)
    
    def set_user_stats(self, user_id, stats):
        """Cache user statistics."""
        key = f"{self.analytics_prefix}user:{user_id}"
        return self.cache.set(key, stats, timeout=3600)


class SessionCache:
    """Session-specific caching."""
    
    def __init__(self):
        self.cache = CacheManager()
        self.session_prefix = "session:"
    
    def get_chat_session(self, session_id):
        """Get chat session from cache."""
        key = f"{self.session_prefix}chat:{session_id}"
        return self.cache.get(key)
    
    def set_chat_session(self, session_id, session_data):
        """Cache chat session."""
        key = f"{self.session_prefix}chat:{session_id}"
        return self.cache.set(key, session_data, timeout=7200)
    
    def get_ai_analysis(self, message_hash):
        """Get AI analysis from cache."""
        key = f"{self.session_prefix}ai:{message_hash}"
        return self.cache.get(key)
    
    def set_ai_analysis(self, message_hash, analysis):
        """Cache AI analysis."""
        key = f"{self.session_prefix}ai:{message_hash}"
        return self.cache.set(key, analysis, timeout=3600)
