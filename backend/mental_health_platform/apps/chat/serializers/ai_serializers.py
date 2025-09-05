"""
AI serializers for mental health platform.
"""
from rest_framework import serializers
from ..models.ai_models import AIAnalysis, CrisisAlert


class AIAnalysisSerializer(serializers.ModelSerializer):
    """AI analysis serializer."""
    
    class Meta:
        model = AIAnalysis
        fields = [
            'id', 'user', 'message_text', 'sentiment_score', 'emotion_score',
            'confidence', 'analysis_data', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']
    
    def to_representation(self, instance):
        """Custom representation for API response."""
        data = super().to_representation(instance)
        
        # Add computed fields
        data['sentiment_label'] = self.get_sentiment_label(instance.sentiment_score)
        data['emotion_label'] = self.get_emotion_label(instance.emotion_score)
        data['risk_level'] = self.get_risk_level(instance.sentiment_score, instance.emotion_score)
        
        return data
    
    def get_sentiment_label(self, score):
        """Get sentiment label from score."""
        if score >= 0.6:
            return 'positive'
        elif score <= 0.4:
            return 'negative'
        else:
            return 'neutral'
    
    def get_emotion_label(self, score):
        """Get emotion label from score."""
        if score >= 0.8:
            return 'very_emotional'
        elif score >= 0.6:
            return 'emotional'
        elif score >= 0.4:
            return 'moderate'
        else:
            return 'calm'
    
    def get_risk_level(self, sentiment_score, emotion_score):
        """Get risk level from scores."""
        combined_score = (sentiment_score + emotion_score) / 2
        
        if combined_score <= 0.3:
            return 'high_risk'
        elif combined_score <= 0.5:
            return 'medium_risk'
        else:
            return 'low_risk'


class CrisisAlertSerializer(serializers.ModelSerializer):
    """Crisis alert serializer."""
    
    class Meta:
        model = CrisisAlert
        fields = [
            'id', 'user', 'message_content', 'risk_level', 'risk_score',
            'keywords_found', 'confidence', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']
    
    def to_representation(self, instance):
        """Custom representation for API response."""
        data = super().to_representation(instance)
        
        # Add computed fields
        data['requires_immediate_attention'] = instance.risk_score >= 0.8
        data['intervention_recommended'] = instance.risk_score >= 0.6
        data['safety_score'] = 1.0 - instance.risk_score
        
        return data


class AIResponseSerializer(serializers.Serializer):
    """AI response serializer."""
    response = serializers.CharField(max_length=2000)
    sentiment = serializers.CharField(max_length=20)
    confidence = serializers.FloatField(min_value=0.0, max_value=1.0)
    suggestions = serializers.ListField(
        child=serializers.CharField(max_length=200),
        required=False
    )
    crisis_detected = serializers.BooleanField(default=False)
    intervention_needed = serializers.BooleanField(default=False)


class VoiceAnalysisSerializer(serializers.Serializer):
    """Voice analysis serializer."""
    audio_file = serializers.FileField()
    emotion_detected = serializers.CharField(max_length=20)
    stress_level = serializers.FloatField(min_value=0.0, max_value=1.0)
    speaking_rate = serializers.FloatField()
    pitch_variation = serializers.FloatField()
    confidence = serializers.FloatField(min_value=0.0, max_value=1.0)
