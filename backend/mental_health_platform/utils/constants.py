"""
Constants for mental health platform.
"""

# AI Model Constants
AI_MODELS = {
    'SENTIMENT': 'cardiffnlp/twitter-roberta-base-sentiment-latest',
    'EMOTION': 'j-hartmann/emotion-english-distilroberta-base',
    'CRISIS': 'distilbert-base-uncased'
}

# Crisis Detection Constants
CRISIS_KEYWORDS = [
    'suicide', 'kill myself', 'end it all', 'not worth living',
    'want to die', 'better off dead', 'give up', 'hopeless',
    'no point', 'can\'t go on', 'end my life', 'better dead'
]

# Sentiment Labels
SENTIMENT_LABELS = {
    'POSITIVE': 'positive',
    'NEGATIVE': 'negative',
    'NEUTRAL': 'neutral'
}

# Emotion Labels
EMOTION_LABELS = {
    'JOY': 'joy',
    'SADNESS': 'sadness',
    'ANGER': 'anger',
    'FEAR': 'fear',
    'SURPRISE': 'surprise',
    'DISGUST': 'disgust'
}

# Crisis Risk Levels
CRISIS_LEVELS = {
    'LOW': 0.0,
    'MEDIUM': 0.5,
    'HIGH': 0.8,
    'CRITICAL': 1.0
}

# Response Types
RESPONSE_TYPES = {
    'CRISIS': 'crisis',
    'COMFORT': 'comfort',
    'SUPPORT': 'support',
    'GENERAL': 'general'
}

# Priority Levels
PRIORITY_LEVELS = {
    'LOW': 'low',
    'MEDIUM': 'medium',
    'HIGH': 'high',
    'CRITICAL': 'critical'
}

# User Roles
USER_ROLES = {
    'STUDENT': 'student',
    'COUNSELOR': 'counselor',
    'ADMIN': 'admin'
}

# Chat Session Constants
CHAT_SESSION_TIMEOUT = 7200  # 2 hours
MAX_MESSAGES_PER_SESSION = 1000
AI_RESPONSE_TIMEOUT = 30  # seconds

# Analytics Constants
ANALYTICS_CACHE_TIMEOUT = 3600  # 1 hour
DAILY_STATS_CACHE_TIMEOUT = 86400  # 24 hours
USER_STATS_CACHE_TIMEOUT = 3600  # 1 hour

# Privacy Constants
ANONYMIZATION_THRESHOLD = 5  # Minimum users for analytics
DATA_RETENTION_DAYS = 365
PII_FIELDS = ['email', 'phone', 'name', 'address']

# API Constants
API_RATE_LIMIT = 100  # requests per minute
MAX_REQUEST_SIZE = 1024 * 1024  # 1MB
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100

# File Upload Constants
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_IMAGE_TYPES = ['jpg', 'jpeg', 'png', 'gif']
ALLOWED_AUDIO_TYPES = ['mp3', 'wav', 'm4a']
ALLOWED_VIDEO_TYPES = ['mp4', 'avi', 'mov']

# Security Constants
PASSWORD_MIN_LENGTH = 8
SESSION_TIMEOUT = 3600  # 1 hour
MAX_LOGIN_ATTEMPTS = 5
LOCKOUT_DURATION = 900  # 15 minutes

# Mental Health Constants
SUICIDE_PREVENTION_LIFELINE = "1-800-273-8255"
CRISIS_TEXT_LINE = "741741"
MENTAL_HEALTH_EMERGENCY = "911"

# Language Support
SUPPORTED_LANGUAGES = [
    'en', 'hi', 'ta', 'te', 'bn', 'gu', 'mr', 'kn', 'ml', 'pa',
    'or', 'as', 'ne', 'ur', 'ar'
]

# Time Zones
DEFAULT_TIMEZONE = 'UTC'
INDIAN_TIMEZONE = 'Asia/Kolkata'
