import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, List, Any


class BehavioralAnalysis:
    def __init__(self):
        self.stress_indicators = {
            'irregular_login': 0.3,
            'short_messages': 0.2,
            'slow_response': 0.2,
            'night_activity': 0.3
        }
    
    def analyze_behavior_patterns(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze user behavioral patterns using NumPy"""
        login_times = np.array(user_data.get('login_times', []))
        message_times = np.array(user_data.get('message_times', []))
        session_durations = np.array(user_data.get('session_durations', []))
        message_lengths = np.array(user_data.get('message_lengths', []))
        
        patterns = self.extract_patterns(login_times, message_times, session_durations, message_lengths)
        engagement = self.calculate_engagement(user_data)
        stress_indicators = self.detect_stress_indicators(patterns, user_data)
        
        return {
            'patterns': patterns,
            'engagement': engagement,
            'stress_indicators': stress_indicators
        }
    
    def extract_patterns(self, login_times: np.ndarray, message_times: np.ndarray, 
                        session_durations: np.ndarray, message_lengths: np.ndarray) -> Dict[str, float]:
        """Extract behavioral patterns using NumPy operations"""
        patterns = {
            'login_frequency': len(login_times),
            'avg_session_duration': float(np.mean(session_durations)) if len(session_durations) > 0 else 0,
            'message_frequency': len(message_times),
            'avg_message_length': float(np.mean(message_lengths)) if len(message_lengths) > 0 else 0
        }
        
        if len(login_times) > 0:
            login_hours = np.array([dt.hour for dt in login_times])
            patterns['activity_hours'] = login_hours.tolist()
            patterns['night_activity'] = self.has_night_activity(login_hours)
        else:
            patterns['activity_hours'] = []
            patterns['night_activity'] = False
        
        return patterns
    
    def calculate_engagement(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate user engagement metrics"""
        total_sessions = user_data.get('total_sessions', 0)
        total_messages = user_data.get('total_messages', 0)
        last_activity = user_data.get('last_activity')
        
        engagement_score = (total_sessions * 0.3) + (total_messages * 0.7)
        
        is_active = False
        if last_activity:
            if isinstance(last_activity, str):
                last_activity = datetime.fromisoformat(last_activity.replace('Z', '+00:00'))
            days_since_activity = (datetime.now() - last_activity).days
            is_active = days_since_activity <= 7
        
        return {
            'score': float(engagement_score),
            'is_active': is_active,
            'total_sessions': total_sessions,
            'total_messages': total_messages
        }
    
    def detect_stress_indicators(self, patterns: Dict[str, Any], user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Detect stress indicators from behavior patterns"""
        irregular_login = patterns['login_frequency'] < 3
        short_sessions = patterns['avg_session_duration'] < 300
        night_activity = patterns.get('night_activity', False)
        
        stress_score = 0
        if irregular_login:
            stress_score += 0.3
        if short_sessions:
            stress_score += 0.3
        if night_activity:
            stress_score += 0.4
        
        return {
            'stress_score': float(stress_score),
            'irregular_login': irregular_login,
            'short_sessions': short_sessions,
            'night_activity': night_activity,
            'stress_level': self.get_stress_level(stress_score)
        }
    
    def get_stress_level(self, stress_score: float) -> str:
        """Get stress level description"""
        if stress_score >= 0.8:
            return 'very_high'
        elif stress_score >= 0.6:
            return 'high'
        elif stress_score >= 0.4:
            return 'medium'
        elif stress_score >= 0.2:
            return 'low'
        else:
            return 'very_low'
    
    def has_night_activity(self, activity_hours: np.ndarray) -> bool:
        """Check if user is active during night hours"""
        night_hours = [22, 23, 0, 1, 2, 3, 4, 5, 6]
        return any(hour in night_hours for hour in activity_hours)
    
    def analyze_conversation_trend(self, messages: List[Dict[str, Any]]) -> Dict[str, float]:
        """Analyze conversation trend over time"""
        if not messages:
            return {'trend': 0, 'sentiment_change': 0, 'volatility': 0}
        
        sentiments = []
        for message in messages:
            if 'sentiment_score' in message:
                sentiments.append(message['sentiment_score'])
        
        if len(sentiments) < 2:
            return {'trend': 0, 'sentiment_change': 0, 'volatility': 0}
        
        sentiments_array = np.array(sentiments)
        trend_slope = np.polyfit(range(len(sentiments_array)), sentiments_array, 1)[0]
        volatility = np.std(sentiments_array)
        
        if trend_slope > 0.1:
            trend = 'improving'
        elif trend_slope < -0.1:
            trend = 'declining'
        else:
            trend = 'stable'
        
        return {
            'trend': trend,
            'sentiment_change': float(trend_slope),
            'volatility': float(volatility),
            'average_sentiment': float(np.mean(sentiments_array))
        }
    
    def detect_help_seeking_patterns(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Detect help-seeking patterns in user behavior"""
        message_content = user_data.get('message_content', [])
        help_keywords = np.array([
            'help', 'support', 'counselor', 'therapist', 'advice',
            'guidance', 'assistance', 'struggling', 'difficult',
            'overwhelmed', 'stressed', 'anxious', 'depressed'
        ])
        
        help_mentions = 0
        for message in message_content:
            if isinstance(message, str):
                message_words = np.array(message.lower().split())
                keyword_matches = np.isin(help_keywords, message_words)
                help_mentions += np.sum(keyword_matches)
        
        total_messages = len(message_content)
        help_seeking_ratio = help_mentions / total_messages if total_messages > 0 else 0
        
        return {
            'help_mentions': int(help_mentions),
            'help_seeking_ratio': float(help_seeking_ratio),
            'is_seeking_help': help_seeking_ratio > 0.1,
            'help_intensity': self.get_help_intensity(help_seeking_ratio)
        }
    
    def get_help_intensity(self, help_ratio: float) -> str:
        """Get help-seeking intensity level"""
        if help_ratio >= 0.3:
            return 'very_high'
        elif help_ratio >= 0.2:
            return 'high'
        elif help_ratio >= 0.1:
            return 'medium'
        elif help_ratio >= 0.05:
            return 'low'
        else:
            return 'very_low'
    
    def calculate_wellness_score(self, behavioral_data: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate overall wellness score based on multiple factors"""
        engagement = behavioral_data.get('engagement', {})
        stress_indicators = behavioral_data.get('stress_indicators', {})
        help_seeking = behavioral_data.get('help_seeking_patterns', {})
        
        engagement_score = engagement.get('score', 0)
        stress_score = stress_indicators.get('stress_score', 0)
        help_score = help_seeking.get('help_seeking_ratio', 0)
        
        wellness_score = (engagement_score * 0.4 + (1 - stress_score) * 0.4 + help_score * 0.2)
        
        return {
            'wellness_score': float(wellness_score),
            'engagement_contribution': float(engagement_score * 0.4),
            'stress_contribution': float((1 - stress_score) * 0.4),
            'help_contribution': float(help_score * 0.2),
            'wellness_level': self.get_wellness_level(wellness_score)
        }
    
    def get_wellness_level(self, wellness_score: float) -> str:
        """Get wellness level description"""
        if wellness_score >= 0.8:
            return 'excellent'
        elif wellness_score >= 0.6:
            return 'good'
        elif wellness_score >= 0.4:
            return 'fair'
        elif wellness_score >= 0.2:
            return 'poor'
        else:
            return 'critical'
