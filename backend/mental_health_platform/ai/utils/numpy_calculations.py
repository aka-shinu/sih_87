import numpy as np
import pandas as pd
from typing import List, Dict, Any


class NumPyCalculations:
    def __init__(self):
        self.crisis_keywords = np.array([
            'suicide', 'kill myself', 'end it all', 'not worth living',
            'want to die', 'better off dead', 'give up', 'hopeless',
            'no point', 'can\'t go on', 'end my life', 'better dead'
        ])
    
    def detect_crisis_numpy(self, text: str) -> float:
        """Efficient crisis detection using NumPy vectorized operations"""
        text_lower = text.lower()
        text_words = np.array(text_lower.split())
        keyword_matches = np.isin(self.crisis_keywords, text_words)
        crisis_score = np.sum(keyword_matches) / len(self.crisis_keywords)
        severity_multiplier = np.sum(keyword_matches) * 0.2
        final_score = min(crisis_score + severity_multiplier, 1.0)
        return float(final_score)
    
    def aggregate_sentiment_scores(self, sentiment_data: List[Dict]) -> Dict[str, float]:
        """Aggregate sentiment scores using NumPy statistical functions"""
        scores = np.array([data['score'] for data in sentiment_data])
        labels = np.array([data['label'] for data in sentiment_data])
        
        mean_score = np.mean(scores)
        std_score = np.std(scores)
        
        positive_count = np.sum(labels == 'POSITIVE')
        negative_count = np.sum(labels == 'NEGATIVE')
        neutral_count = np.sum(labels == 'NEUTRAL')
        
        sentiment_trend = np.polyfit(range(len(scores)), scores, 1)[0] if len(scores) > 1 else 0
        
        return {
            'mean_sentiment': float(mean_score),
            'std_sentiment': float(std_score),
            'positive_ratio': float(positive_count / len(scores)),
            'negative_ratio': float(negative_count / len(scores)),
            'neutral_ratio': float(neutral_count / len(scores)),
            'trend': float(sentiment_trend)
        }
    
    def analyze_emotion_patterns(self, emotion_data: List[Dict]) -> Dict[str, Any]:
        """Analyze emotion patterns using NumPy array operations"""
        emotions = np.array([data['emotion'] for data in emotion_data])
        scores = np.array([data['score'] for data in emotion_data])
        
        unique_emotions, counts = np.unique(emotions, return_counts=True)
        emotion_distribution = dict(zip(unique_emotions, counts / len(emotions)))
        
        dominant_emotion_idx = np.argmax(counts)
        dominant_emotion = unique_emotions[dominant_emotion_idx]
        emotion_volatility = np.std(scores)
        
        return {
            'emotion_distribution': emotion_distribution,
            'dominant_emotion': dominant_emotion,
            'emotion_volatility': float(emotion_volatility),
            'total_emotions': len(unique_emotions)
        }
    
    def calculate_stress_level(self, behavioral_data: Dict[str, List]) -> Dict[str, float]:
        """Calculate stress level using multiple NumPy factors"""
        login_frequency = np.array(behavioral_data.get('login_frequency', []))
        message_length = np.array(behavioral_data.get('message_length', []))
        response_time = np.array(behavioral_data.get('response_time', []))
        activity_hours = np.array(behavioral_data.get('activity_hours', []))
        
        if len(login_frequency) == 0:
            return {'stress_level': 0, 'irregular_login': 0, 'short_sessions': 0, 'night_activity': 0}
        
        login_norm = self.normalize_array(login_frequency)
        message_norm = self.normalize_array(message_length) if len(message_length) > 0 else np.array([0])
        response_norm = self.normalize_array(response_time) if len(response_time) > 0 else np.array([0])
        
        irregular_login = 1 - login_norm[0] if len(login_norm) > 0 else 0
        short_messages = 1 - message_norm[0] if len(message_norm) > 0 else 0
        slow_response = response_norm[0] if len(response_norm) > 0 else 0
        
        night_activity = np.sum((activity_hours >= 22) | (activity_hours <= 6)) / len(activity_hours) if len(activity_hours) > 0 else 0
        
        stress_score = (0.3 * irregular_login + 0.2 * short_messages + 0.2 * slow_response + 0.3 * night_activity)
        
        return {
            'stress_level': float(stress_score),
            'irregular_login': float(irregular_login),
            'short_sessions': float(short_messages),
            'night_activity': float(night_activity)
        }
    
    def generate_analytics_report(self, analytics_data: Dict[str, List]) -> Dict[str, Any]:
        """Generate comprehensive analytics using NumPy statistical functions"""
        sentiment_scores = np.array(analytics_data.get('sentiment_scores', []))
        emotion_scores = np.array(analytics_data.get('emotion_scores', []))
        crisis_alerts = np.array(analytics_data.get('crisis_alerts', []))
        user_engagement = np.array(analytics_data.get('user_engagement', []))
        
        if len(sentiment_scores) == 0:
            return {'trends': {}, 'correlations': {}, 'risk_assessment': {}, 'averages': {}}
        
        time_periods = len(sentiment_scores)
        time_index = np.arange(time_periods)
        
        sentiment_trend = np.polyfit(time_index, sentiment_scores, 1)[0]
        emotion_trend = np.polyfit(time_index, emotion_scores, 1)[0] if len(emotion_scores) > 0 else 0
        engagement_trend = np.polyfit(time_index, user_engagement, 1)[0] if len(user_engagement) > 0 else 0
        
        sentiment_emotion_corr = np.corrcoef(sentiment_scores, emotion_scores)[0, 1] if len(emotion_scores) > 0 else 0
        sentiment_engagement_corr = np.corrcoef(sentiment_scores, user_engagement)[0, 1] if len(user_engagement) > 0 else 0
        
        high_risk_periods = np.sum(crisis_alerts > 0.8) if len(crisis_alerts) > 0 else 0
        risk_percentage = (high_risk_periods / len(crisis_alerts)) * 100 if len(crisis_alerts) > 0 else 0
        
        return {
            'trends': {
                'sentiment_trend': float(sentiment_trend),
                'emotion_trend': float(emotion_trend),
                'engagement_trend': float(engagement_trend)
            },
            'correlations': {
                'sentiment_emotion': float(sentiment_emotion_corr),
                'sentiment_engagement': float(sentiment_engagement_corr)
            },
            'risk_assessment': {
                'high_risk_periods': int(high_risk_periods),
                'risk_percentage': float(risk_percentage)
            },
            'averages': {
                'sentiment': float(np.mean(sentiment_scores)),
                'emotion': float(np.mean(emotion_scores)) if len(emotion_scores) > 0 else 0,
                'engagement': float(np.mean(user_engagement)) if len(user_engagement) > 0 else 0
            }
        }
    
    def create_anonymized_statistics(self, raw_data: Dict[str, List]) -> Dict[str, Any]:
        """Create anonymized statistics using NumPy without revealing individual data"""
        sentiment_data = np.array(raw_data.get('sentiment_scores', []))
        emotion_data = np.array(raw_data.get('emotion_scores', []))
        crisis_data = np.array(raw_data.get('crisis_scores', []))
        
        if len(sentiment_data) == 0:
            return {'total_users': 0, 'sentiment_stats': {}, 'emotion_stats': {}, 'crisis_stats': {}}
        
        return {
            'total_users': len(sentiment_data),
            'sentiment_stats': {
                'mean': float(np.mean(sentiment_data)),
                'std': float(np.std(sentiment_data)),
                'min': float(np.min(sentiment_data)),
                'max': float(np.max(sentiment_data))
            },
            'emotion_stats': {
                'mean': float(np.mean(emotion_data)) if len(emotion_data) > 0 else 0,
                'std': float(np.std(emotion_data)) if len(emotion_data) > 0 else 0
            },
            'crisis_stats': {
                'total_alerts': int(np.sum(crisis_data > 0.8)) if len(crisis_data) > 0 else 0,
                'alert_rate': float(np.mean(crisis_data > 0.8) * 100) if len(crisis_data) > 0 else 0
            }
        }
    
    def track_student_progress(self, student_data: List[Dict]) -> Dict[str, float]:
        """Track individual student progress over time using NumPy"""
        if len(student_data) < 2:
            return {'trend': 0, 'recent_trend': 0, 'overall_improvement': 0, 'data_points': 0}
        
        timestamps = np.array([data['timestamp'] for data in student_data])
        sentiment_scores = np.array([data['sentiment'] for data in student_data])
        
        trend = np.polyfit(range(len(sentiment_scores)), sentiment_scores, 1)[0]
        
        recent_scores = sentiment_scores[-7:] if len(sentiment_scores) >= 7 else sentiment_scores
        recent_trend = np.polyfit(range(len(recent_scores)), recent_scores, 1)[0]
        
        overall_improvement = sentiment_scores[-1] - sentiment_scores[0]
        
        return {
            'trend': float(trend),
            'recent_trend': float(recent_trend),
            'overall_improvement': float(overall_improvement),
            'data_points': len(sentiment_scores)
        }
    
    def normalize_array(self, arr: np.ndarray) -> np.ndarray:
        """Normalize array to 0-1 scale using NumPy"""
        if len(arr) == 0:
            return np.array([])
        
        min_val = np.min(arr)
        max_val = np.max(arr)
        
        if max_val == min_val:
            return np.zeros_like(arr)
        
        return (arr - min_val) / (max_val - min_val)
    
    def calculate_confidence_scores(self, results: List[Dict]) -> Dict[str, float]:
        """Calculate confidence scores using NumPy statistical functions"""
        scores = np.array([result.get('score', 0) for result in results])
        
        if len(scores) == 0:
            return {'mean': 0, 'std': 0, 'max': 0, 'min': 0}
        
        return {
            'mean': float(np.mean(scores)),
            'std': float(np.std(scores)),
            'max': float(np.max(scores)),
            'min': float(np.min(scores))
        }
