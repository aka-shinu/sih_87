"""
NLP models for mental health analysis.
"""
from django.db import models


class NLPAnalysis(models.Model):
    """NLP analysis results."""
    text_content = models.TextField()
    language = models.CharField(max_length=10, default='en')
    sentiment_score = models.FloatField()
    emotion_score = models.FloatField()
    confidence = models.FloatField()
    keywords = models.JSONField(default=list)
    entities = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"NLP Analysis - {self.sentiment_score:.2f}"


class TextPreprocessing(models.Model):
    """Text preprocessing configuration."""
    language = models.CharField(max_length=10)
    preprocessing_rules = models.JSONField(default=dict)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Preprocessing - {self.language}"


class LanguageModel(models.Model):
    """Language model configuration."""
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=10)
    model_type = models.CharField(max_length=50)
    version = models.CharField(max_length=20)
    accuracy = models.FloatField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.language}"
