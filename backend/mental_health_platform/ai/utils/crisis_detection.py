import numpy as np
from typing import Dict, List, Tuple


class CrisisDetection:
    def __init__(self):
        self.crisis_keywords = np.array([
            'suicide', 'kill myself', 'end it all', 'not worth living',
            'want to die', 'better off dead', 'give up', 'hopeless',
            'no point', 'can\'t go on', 'end my life', 'better dead',
            'not worth it', 'end everything', 'stop living', 'no reason to live'
        ])
        
        self.severity_weights = {
            'suicide': 1.0,
            'kill myself': 0.9,
            'end it all': 0.8,
            'not worth living': 0.7,
            'want to die': 0.8,
            'better off dead': 0.7,
            'give up': 0.6,
            'hopeless': 0.6
        }
    
    def detect_crisis_advanced(self, text: str) -> Dict[str, any]:
        """Advanced crisis detection with severity scoring"""
        text_lower = text.lower()
        text_words = np.array(text_lower.split())
        
        keyword_matches = np.isin(self.crisis_keywords, text_words)
        matched_keywords = self.crisis_keywords[keyword_matches]
        
        if len(matched_keywords) == 0:
            return {
                'is_crisis': False,
                'severity': 0.0,
                'risk_level': 'low',
                'keywords_found': [],
                'action_required': False
            }
        
        severity_scores = np.array([self.severity_weights.get(keyword, 0.5) for keyword in matched_keywords])
        max_severity = np.max(severity_scores)
        avg_severity = np.mean(severity_scores)
        
        crisis_score = (max_severity * 0.7 + avg_severity * 0.3)
        
        if crisis_score >= 0.8:
            risk_level = 'critical'
            action_required = True
        elif crisis_score >= 0.6:
            risk_level = 'high'
            action_required = True
        elif crisis_score >= 0.4:
            risk_level = 'medium'
            action_required = False
        else:
            risk_level = 'low'
            action_required = False
        
        return {
            'is_crisis': True,
            'severity': float(crisis_score),
            'risk_level': risk_level,
            'keywords_found': matched_keywords.tolist(),
            'action_required': action_required,
            'max_severity': float(max_severity),
            'avg_severity': float(avg_severity)
        }
    
    def detect_escalation_pattern(self, messages: List[str]) -> Dict[str, any]:
        """Detect escalation pattern in conversation"""
        if len(messages) < 3:
            return {'escalation_detected': False, 'pattern': 'insufficient_data'}
        
        crisis_scores = []
        for message in messages[-10:]:
            detection = self.detect_crisis_advanced(message)
            crisis_scores.append(detection['severity'])
        
        crisis_array = np.array(crisis_scores)
        
        if len(crisis_array) >= 3:
            trend_slope = np.polyfit(range(len(crisis_array)), crisis_array, 1)[0]
            if trend_slope > 0.1 and crisis_array[-1] > 0.6:
                return {
                    'escalation_detected': True,
                    'pattern': 'increasing_crisis',
                    'trend_slope': float(trend_slope),
                    'current_risk': float(crisis_array[-1]),
                    'escalation_rate': float(trend_slope * len(crisis_array))
                }
        
        return {'escalation_detected': False, 'pattern': 'stable'}
    
    def generate_crisis_response(self, detection_result: Dict[str, any]) -> Dict[str, str]:
        """Generate appropriate crisis response based on detection"""
        if detection_result['risk_level'] == 'critical':
            return {
                'message': "I'm very concerned about what you're sharing. Please reach out to a mental health professional immediately. You can call the National Suicide Prevention Lifeline at 1-800-273-8255.",
                'action': 'immediate_intervention',
                'priority': 'critical',
                'helpline': '1-800-273-8255'
            }
        elif detection_result['risk_level'] == 'high':
            return {
                'message': "I'm worried about you. It sounds like you're going through a very difficult time. Would you like to talk to a counselor or mental health professional?",
                'action': 'professional_referral',
                'priority': 'high',
                'helpline': '1-800-273-8255'
            }
        elif detection_result['risk_level'] == 'medium':
            return {
                'message': "I understand you're going through a tough time. How can I help you feel better today?",
                'action': 'support',
                'priority': 'medium',
                'helpline': None
            }
        else:
            return {
                'message': "Thank you for sharing with me. How are you feeling today?",
                'action': 'general_support',
                'priority': 'low',
                'helpline': None
            }
    
    def calculate_risk_trend(self, historical_scores: List[float]) -> Dict[str, float]:
        """Calculate risk trend over time using NumPy"""
        if len(historical_scores) < 2:
            return {'trend': 0, 'volatility': 0, 'recent_change': 0}
        
        scores_array = np.array(historical_scores)
        time_index = np.arange(len(scores_array))
        
        trend = np.polyfit(time_index, scores_array, 1)[0]
        volatility = np.std(scores_array)
        
        recent_change = scores_array[-1] - scores_array[0] if len(scores_array) > 1 else 0
        
        return {
            'trend': float(trend),
            'volatility': float(volatility),
            'recent_change': float(recent_change)
        }
    
    def assess_intervention_urgency(self, detection_result: Dict[str, any], 
                                  historical_data: List[Dict[str, any]]) -> Dict[str, any]:
        """Assess urgency of intervention needed"""
        current_severity = detection_result['severity']
        
        if len(historical_data) > 0:
            historical_scores = [data['severity'] for data in historical_data[-7:]]
            risk_trend = self.calculate_risk_trend(historical_scores)
        else:
            risk_trend = {'trend': 0, 'volatility': 0, 'recent_change': 0}
        
        urgency_score = current_severity * 0.6 + abs(risk_trend['trend']) * 0.4
        
        if urgency_score >= 0.8:
            urgency_level = 'immediate'
        elif urgency_score >= 0.6:
            urgency_level = 'urgent'
        elif urgency_score >= 0.4:
            urgency_level = 'moderate'
        else:
            urgency_level = 'low'
        
        return {
            'urgency_score': float(urgency_score),
            'urgency_level': urgency_level,
            'current_severity': current_severity,
            'trend_contribution': float(abs(risk_trend['trend'])),
            'recommended_action': self.get_recommended_action(urgency_level)
        }
    
    def get_recommended_action(self, urgency_level: str) -> str:
        """Get recommended action based on urgency level"""
        actions = {
            'immediate': 'Contact emergency services and crisis helpline immediately',
            'urgent': 'Schedule immediate appointment with mental health professional',
            'moderate': 'Provide support resources and encourage professional consultation',
            'low': 'Continue monitoring and provide general support'
        }
        return actions.get(urgency_level, 'Continue monitoring')
