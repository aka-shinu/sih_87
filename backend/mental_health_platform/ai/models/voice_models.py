"""
Voice analysis models for mental health.
"""
from django.db import models


class VoiceAnalysis(models.Model):
    """Voice analysis results."""
    audio_file = models.FileField(upload_to='voice_analysis/')
    duration = models.FloatField()
    sample_rate = models.IntegerField()
    emotion_detected = models.CharField(max_length=20)
    stress_level = models.FloatField()
    speaking_rate = models.FloatField()
    pitch_variation = models.FloatField()
    confidence = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Voice Analysis - {self.emotion_detected}"


class VoiceFeature(models.Model):
    """Voice feature extraction."""
    analysis = models.ForeignKey(VoiceAnalysis, on_delete=models.CASCADE)
    feature_type = models.CharField(max_length=50)
    feature_value = models.FloatField()
    timestamp = models.FloatField()

    def __str__(self):
        return f"{self.feature_type} - {self.feature_value}"


class VoiceModel(models.Model):
    """Voice analysis model configuration."""
    name = models.CharField(max_length=100)
    model_type = models.CharField(max_length=50)
    version = models.CharField(max_length=20)
    accuracy = models.FloatField()
    supported_languages = models.JSONField(default=list)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} v{self.version}"
