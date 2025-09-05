"""
AI processing utilities for mental health platform.
"""
import numpy as np
from ...ai.services.ai_service import MentalHealthAI
from ..models.ai_models import AIAnalysis, CrisisDetection


class AIProcessingUtils:
    """AI processing utility functions."""
    
    def __init__(self):
        self.ai_service = MentalHealthAI()
    
    def process_message(self, message_text, user=None):
        """Process message through AI pipeline."""
        try:
            # Analyze text
            analysis = self.ai_service.analyze_text(message_text)
            
            # Detect crisis
            crisis_detection = self.ai_service.detect_crisis(message_text)
            
            # Save analysis to database
            if user:
                ai_analysis = AIAnalysis.objects.create(
                    user=user,
                    message_text=message_text,
                    sentiment_score=analysis['sentiment_score'],
                    emotion_score=analysis['emotion_score'],
                    confidence=analysis['confidence'],
                    analysis_data=analysis
                )
                
                if crisis_detection['risk_score'] > 0.5:
                    CrisisDetection.objects.create(
                        user=user,
                        message_content=message_text,
                        risk_level=crisis_detection['risk_level'],
                        risk_score=crisis_detection['risk_score'],
                        keywords_found=crisis_detection['keywords_found'],
                        confidence=crisis_detection['confidence']
                    )
            
            return {
                'analysis': analysis,
                'crisis_detection': crisis_detection,
                'processed': True
            }
            
        except Exception as e:
            return {
                'error': str(e),
                'processed': False
            }
    
    def generate_response(self, message_text, context=None):
        """Generate AI response to message."""
        try:
            response = self.ai_service.generate_response(message_text, context or {})
            return response
        except Exception as e:
            return {
                'response': "I'm sorry, I'm having trouble processing your message right now. Please try again.",
                'error': str(e)
            }
    
    def analyze_conversation_trend(self, messages):
        """Analyze conversation trend over time."""
        if not messages:
            return {'trend': 'neutral', 'sentiment_change': 0}
        
        sentiments = []
        for message in messages:
            if hasattr(message, 'ai_analysis') and message.ai_analysis:
                sentiments.append(message.ai_analysis.sentiment_score)
        
        if not sentiments:
            return {'trend': 'neutral', 'sentiment_change': 0}
        
        # Calculate trend using NumPy
        sentiments_array = np.array(sentiments)
        trend_slope = np.polyfit(range(len(sentiments_array)), sentiments_array, 1)[0]
        
        if trend_slope > 0.1:
            trend = 'improving'
        elif trend_slope < -0.1:
            trend = 'declining'
        else:
            trend = 'stable'
        
        return {
            'trend': trend,
            'sentiment_change': float(trend_slope),
            'average_sentiment': float(np.mean(sentiments_array))
        }
    
    def detect_escalation_pattern(self, messages):
        """Detect escalation pattern in conversation."""
        if len(messages) < 3:
            return {'escalation_detected': False, 'pattern': 'insufficient_data'}
        
        crisis_scores = []
        for message in messages[-10:]:  # Check last 10 messages
            if hasattr(message, 'crisis_detection') and message.crisis_detection:
                crisis_scores.append(message.crisis_detection.risk_score)
        
        if not crisis_scores:
            return {'escalation_detected': False, 'pattern': 'no_crisis_data'}
        
        # Check for increasing trend in crisis scores
        crisis_array = np.array(crisis_scores)
        if len(crisis_array) >= 3:
            trend_slope = np.polyfit(range(len(crisis_array)), crisis_array, 1)[0]
            if trend_slope > 0.1 and crisis_array[-1] > 0.6:
                return {
                    'escalation_detected': True,
                    'pattern': 'increasing_crisis',
                    'trend_slope': float(trend_slope),
                    'current_risk': float(crisis_array[-1])
                }
        
        return {'escalation_detected': False, 'pattern': 'stable'}
