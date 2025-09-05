"""
Crisis detection service for mental health.
"""
import numpy as np
from .ai_service import MentalHealthAI


class CrisisService:
    """Crisis detection service."""
    
    def __init__(self):
        self.ai_service = MentalHealthAI()
        self.crisis_keywords = np.array([
            'suicide', 'kill myself', 'end it all', 'not worth living',
            'want to die', 'better off dead', 'give up', 'hopeless'
        ])
    
    def detect_crisis(self, text, user_data=None):
        """Detect crisis situation from text and user data."""
        # Text-based crisis detection
        text_risk = self.analyze_text_crisis(text)
        
        # Behavioral crisis detection
        behavioral_risk = 0
        if user_data:
            behavioral_risk = self.analyze_behavioral_crisis(user_data)
        
        # Combine risks
        total_risk = max(text_risk, behavioral_risk)
        
        # Determine risk level
        risk_level = self.get_risk_level(total_risk)
        
        return {
            'risk_score': total_risk,
            'risk_level': risk_level,
            'text_risk': text_risk,
            'behavioral_risk': behavioral_risk,
            'keywords_found': self.find_crisis_keywords(text),
            'requires_intervention': total_risk > 0.8
        }
    
    def analyze_text_crisis(self, text):
        """Analyze text for crisis indicators."""
        text_lower = text.lower()
        text_words = np.array(text_lower.split())
        
        # Check for crisis keywords
        keyword_matches = np.isin(self.crisis_keywords, text_words)
        keyword_score = np.sum(keyword_matches) / len(self.crisis_keywords)
        
        # Check for negative sentiment
        sentiment_analysis = self.ai_service.analyze_text(text)
        sentiment_score = sentiment_analysis['sentiment_score']
        
        # Combine scores
        crisis_score = (keyword_score * 0.7) + ((1 - sentiment_score) * 0.3)
        
        return min(crisis_score, 1.0)
    
    def analyze_behavioral_crisis(self, user_data):
        """Analyze user behavior for crisis indicators."""
        patterns = user_data.get('patterns', {})
        engagement = user_data.get('engagement', {})
        
        # Behavioral crisis indicators
        indicators = []
        
        # Sudden drop in activity
        if patterns.get('login_frequency', 0) < 1:
            indicators.append(0.3)
        
        # Very short sessions
        if patterns.get('avg_session_duration', 0) < 60:  # Less than 1 minute
            indicators.append(0.2)
        
        # Night activity (stress indicator)
        if patterns.get('night_activity', False):
            indicators.append(0.2)
        
        # Low engagement
        if engagement.get('score', 0) < 5:
            indicators.append(0.3)
        
        return sum(indicators) if indicators else 0
    
    def find_crisis_keywords(self, text):
        """Find crisis keywords in text."""
        text_lower = text.lower()
        found_keywords = []
        
        for keyword in self.crisis_keywords:
            if keyword in text_lower:
                found_keywords.append(keyword)
        
        return found_keywords
    
    def get_risk_level(self, risk_score):
        """Get risk level from score."""
        if risk_score >= 0.8:
            return 'critical'
        elif risk_score >= 0.6:
            return 'high'
        elif risk_score >= 0.4:
            return 'medium'
        else:
            return 'low'
    
    def generate_crisis_response(self, risk_level, keywords_found):
        """Generate appropriate crisis response."""
        if risk_level == 'critical':
            return {
                'message': "I'm very concerned about what you're sharing. Please reach out to a mental health professional immediately. You can call the National Suicide Prevention Lifeline at 1-800-273-8255.",
                'action': 'immediate_intervention',
                'priority': 'critical'
            }
        elif risk_level == 'high':
            return {
                'message': "I'm worried about you. It sounds like you're going through a very difficult time. Would you like to talk to a counselor or mental health professional?",
                'action': 'professional_referral',
                'priority': 'high'
            }
        else:
            return {
                'message': "I understand you're going through a tough time. How can I help you feel better today?",
                'action': 'support',
                'priority': 'medium'
            }
