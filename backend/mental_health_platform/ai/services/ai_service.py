import numpy as np
import pandas as pd
from transformers import pipeline
from datetime import datetime


class MentalHealthAI:
    _instance = None
    _models = None
    
    def __new__(cls):
        """Singleton pattern to load models only once"""
        if cls._instance is None:
            cls._instance = super(MentalHealthAI, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self._models is None:
            self._models = self.load_models()
        self.models = self._models
        self.crisis_keywords = np.array([
            'suicide', 'kill myself', 'end it all', 'not worth living',
            'want to die', 'better off dead', 'give up', 'hopeless',
            'no point', 'can\'t go on', 'end my life', 'better dead'
        ])
    
    def load_models(self):
        """Load pre-trained models from Hugging Face"""
        return {
            'sentiment': pipeline("sentiment-analysis", 
                                model="cardiffnlp/twitter-roberta-base-sentiment-latest"),
            'emotion': pipeline("text-classification", 
                              model="j-hartmann/emotion-english-distilroberta-base"),
            'crisis': pipeline("sentiment-analysis", 
                             model="distilbert-base-uncased")
        }
    
    def analyze_text(self, text):
        """Analyze text using pre-trained models with NumPy calculations"""
        sentiment = self.models['sentiment'](text)
        emotion = self.models['emotion'](text)
        crisis_risk = self.detect_crisis_numpy(text)
        confidence_stats = self.calculate_confidence_numpy([sentiment, emotion])
        
        return {
            'sentiment': sentiment[0]['label'],
            'sentiment_score': sentiment[0]['score'],
            'emotion': emotion[0]['label'],
            'emotion_score': emotion[0]['score'],
            'crisis_risk': crisis_risk,
            'confidence': confidence_stats['mean_confidence'],
            'timestamp': datetime.now().isoformat()
        }
    
    def detect_crisis_numpy(self, text):
        """Use NumPy for efficient crisis detection"""
        text_lower = text.lower()
        text_words = np.array(text_lower.split())
        keyword_matches = np.isin(self.crisis_keywords, text_words)
        crisis_score = np.sum(keyword_matches) / len(self.crisis_keywords)
        severity_multiplier = np.sum(keyword_matches) * 0.2
        final_score = min(crisis_score + severity_multiplier, 1.0)
        return float(final_score)
    
    def calculate_confidence_numpy(self, results):
        """Use NumPy for confidence calculations"""
        scores = np.array([result[0]['score'] for result in results])
        return {
            'mean_confidence': float(np.mean(scores)),
            'std_confidence': float(np.std(scores)),
            'max_confidence': float(np.max(scores)),
            'min_confidence': float(np.min(scores))
        }
    
    def detect_crisis(self, text):
        """Detect crisis situation with detailed analysis"""
        crisis_score = self.detect_crisis_numpy(text)
        keywords_found = [keyword for keyword in self.crisis_keywords if keyword in text.lower()]
        
        if crisis_score >= 0.8:
            risk_level = 'critical'
        elif crisis_score >= 0.6:
            risk_level = 'high'
        elif crisis_score >= 0.4:
            risk_level = 'medium'
        else:
            risk_level = 'low'
        
        return {
            'risk_score': crisis_score,
            'risk_level': risk_level,
            'keywords_found': keywords_found,
            'confidence': crisis_score,
            'requires_intervention': crisis_score > 0.6
        }
    
    def generate_response(self, text, context=None):
        """Generate AI response based on analysis"""
        analysis = self.analyze_text(text)
        crisis = self.detect_crisis(text)
        
        if crisis['risk_score'] > 0.8:
            return {
                'response': "I'm very concerned about what you're sharing. Please reach out to a mental health professional immediately. You can call the National Suicide Prevention Lifeline at 1-800-273-8255.",
                'sentiment': analysis['sentiment'],
                'confidence': analysis['confidence'],
                'suggestions': ['Contact crisis helpline', 'Speak to a counselor', 'Emergency services'],
                'crisis_detected': True,
                'intervention_needed': True
            }
        elif analysis['emotion'] == 'sadness' or analysis['emotion'] == 'fear':
            return {
                'response': "I understand you're going through a difficult time. Let's work together to help you feel better.",
                'sentiment': analysis['sentiment'],
                'confidence': analysis['confidence'],
                'suggestions': ['Deep breathing exercises', 'Mindfulness meditation', 'Talk to someone you trust'],
                'crisis_detected': False,
                'intervention_needed': False
            }
        elif analysis['sentiment'] == 'NEGATIVE':
            return {
                'response': "I hear that you're feeling down. Would you like to talk about what's bothering you?",
                'sentiment': analysis['sentiment'],
                'confidence': analysis['confidence'],
                'suggestions': ['Share your feelings', 'Try relaxation techniques', 'Consider professional help'],
                'crisis_detected': False,
                'intervention_needed': False
            }
        else:
            return {
                'response': "Thank you for sharing with me. How can I help you today?",
                'sentiment': analysis['sentiment'],
                'confidence': analysis['confidence'],
                'suggestions': ['Continue the conversation', 'Explore coping strategies', 'Set personal goals'],
                'crisis_detected': False,
                'intervention_needed': False
            }
    
    def analyze_behavioral_patterns(self, user_data):
        """Analyze behavioral patterns using NumPy"""
        login_frequency = np.array(user_data.get('login_frequency', []))
        message_lengths = np.array(user_data.get('message_lengths', []))
        response_times = np.array(user_data.get('response_times', []))
        activity_hours = np.array(user_data.get('activity_hours', []))
        
        if len(login_frequency) == 0:
            return {'patterns': {}, 'stress_indicators': {}, 'engagement': {}}
        
        patterns = {
            'avg_login_frequency': float(np.mean(login_frequency)),
            'login_consistency': float(1 - np.std(login_frequency) / np.mean(login_frequency)) if np.mean(login_frequency) > 0 else 0,
            'avg_message_length': float(np.mean(message_lengths)) if len(message_lengths) > 0 else 0,
            'avg_response_time': float(np.mean(response_times)) if len(response_times) > 0 else 0
        }
        
        stress_indicators = self.calculate_stress_indicators(patterns, activity_hours)
        engagement = self.calculate_engagement_score(patterns)
        
        return {
            'patterns': patterns,
            'stress_indicators': stress_indicators,
            'engagement': engagement
        }
    
    def calculate_stress_indicators(self, patterns, activity_hours):
        """Calculate stress indicators using NumPy"""
        if len(activity_hours) == 0:
            return {'stress_level': 0, 'night_activity': 0, 'irregular_patterns': 0}
        
        night_activity = np.sum((activity_hours >= 22) | (activity_hours <= 6)) / len(activity_hours)
        irregular_patterns = 1 - patterns.get('login_consistency', 0)
        
        stress_level = (night_activity * 0.4 + irregular_patterns * 0.6)
        
        return {
            'stress_level': float(stress_level),
            'night_activity': float(night_activity),
            'irregular_patterns': float(irregular_patterns)
        }
    
    def calculate_engagement_score(self, patterns):
        """Calculate user engagement score"""
        login_score = min(patterns.get('avg_login_frequency', 0) / 7, 1.0)
        message_score = min(patterns.get('avg_message_length', 0) / 100, 1.0)
        
        engagement_score = (login_score * 0.6 + message_score * 0.4)
        
        return {
            'score': float(engagement_score),
            'is_active': engagement_score > 0.3,
            'login_score': float(login_score),
            'message_score': float(message_score)
        }