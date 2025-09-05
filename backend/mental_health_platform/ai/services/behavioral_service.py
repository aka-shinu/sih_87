"""
Behavioral analysis service for mental health.
"""
import numpy as np
from datetime import datetime, timedelta


class BehavioralService:
    """Behavioral analysis service."""
    
    def __init__(self):
        pass
    
    def analyze_behavior(self, user_data):
        """Analyze user behavioral patterns."""
        patterns = self.extract_patterns(user_data)
        engagement = self.calculate_engagement(user_data)
        stress_indicators = self.detect_stress_indicators(user_data)
        
        return {
            'patterns': patterns,
            'engagement': engagement,
            'stress_indicators': stress_indicators
        }
    
    def extract_patterns(self, user_data):
        """Extract behavioral patterns."""
        login_times = user_data.get('login_times', [])
        message_times = user_data.get('message_times', [])
        session_durations = user_data.get('session_durations', [])
        
        patterns = {
            'login_frequency': len(login_times),
            'avg_session_duration': np.mean(session_durations) if session_durations else 0,
            'message_frequency': len(message_times),
            'activity_hours': self.get_activity_hours(login_times + message_times)
        }
        
        return patterns
    
    def calculate_engagement(self, user_data):
        """Calculate user engagement metrics."""
        total_sessions = user_data.get('total_sessions', 0)
        total_messages = user_data.get('total_messages', 0)
        last_activity = user_data.get('last_activity')
        
        # Calculate engagement score
        engagement_score = (total_sessions * 0.3) + (total_messages * 0.7)
        
        # Check if user is active (logged in within last 7 days)
        is_active = False
        if last_activity:
            days_since_activity = (datetime.now() - last_activity).days
            is_active = days_since_activity <= 7
        
        return {
            'score': engagement_score,
            'is_active': is_active,
            'total_sessions': total_sessions,
            'total_messages': total_messages
        }
    
    def detect_stress_indicators(self, user_data):
        """Detect stress indicators from behavior."""
        patterns = self.extract_patterns(user_data)
        
        # Stress indicators
        irregular_login = patterns['login_frequency'] < 3  # Less than 3 logins
        short_sessions = patterns['avg_session_duration'] < 300  # Less than 5 minutes
        night_activity = self.has_night_activity(patterns['activity_hours'])
        
        stress_score = 0
        if irregular_login:
            stress_score += 0.3
        if short_sessions:
            stress_score += 0.3
        if night_activity:
            stress_score += 0.4
        
        return {
            'stress_score': stress_score,
            'irregular_login': irregular_login,
            'short_sessions': short_sessions,
            'night_activity': night_activity
        }
    
    def get_activity_hours(self, timestamps):
        """Get activity hours from timestamps."""
        hours = []
        for timestamp in timestamps:
            if isinstance(timestamp, datetime):
                hours.append(timestamp.hour)
        return hours
    
    def has_night_activity(self, activity_hours):
        """Check if user is active during night hours."""
        night_hours = [22, 23, 0, 1, 2, 3, 4, 5, 6]  # 10 PM to 6 AM
        return any(hour in night_hours for hour in activity_hours)
