"""
NLP processing service for mental health.
"""
import numpy as np
from transformers import pipeline
from .ai_service import MentalHealthAI


class NLPService:
    """NLP processing service."""
    
    def __init__(self):
        self.ai_service = MentalHealthAI()
        self.sentiment_pipeline = pipeline("sentiment-analysis")
        self.emotion_pipeline = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base"
        )
    
    def analyze_text(self, text, language='en'):
        """Analyze text for sentiment and emotion."""
        sentiment = self.sentiment_pipeline(text)
        emotion = self.emotion_pipeline(text)
        
        return {
            'sentiment': sentiment[0]['label'],
            'sentiment_score': sentiment[0]['score'],
            'emotion': emotion[0]['label'],
            'emotion_score': emotion[0]['score'],
            'language': language
        }
    
    def extract_keywords(self, text):
        """Extract keywords from text."""
        words = text.lower().split()
        keywords = [word for word in words if len(word) > 3]
        return list(set(keywords))
    
    def detect_language(self, text):
        """Detect text language."""
        # Simple language detection based on character patterns
        if any(ord(char) > 127 for char in text):
            return 'hi'  # Hindi or other Indian language
        return 'en'  # English
    
    def preprocess_text(self, text):
        """Preprocess text for analysis."""
        import re
        # Remove special characters but keep spaces
        cleaned = re.sub(r'[^\w\s]', '', text)
        # Convert to lowercase
        cleaned = cleaned.lower()
        # Remove extra spaces
        cleaned = ' '.join(cleaned.split())
        return cleaned
