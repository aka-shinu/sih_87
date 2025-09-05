"""
Model utilities for AI services.
"""
import numpy as np
import torch
from transformers import pipeline


class ModelUtils:
    """AI model utility functions."""
    
    @staticmethod
    def load_model(model_name, task="text-classification"):
        """Load pre-trained model."""
        try:
            return pipeline(task, model=model_name)
        except Exception as e:
            print(f"Error loading model {model_name}: {e}")
            return None
    
    @staticmethod
    def preprocess_text(text):
        """Preprocess text for model input."""
        # Basic text cleaning
        text = text.strip().lower()
        # Remove extra whitespace
        text = ' '.join(text.split())
        return text
    
    @staticmethod
    def calculate_confidence(scores):
        """Calculate confidence from model scores."""
        if isinstance(scores, list) and len(scores) > 0:
            return scores[0].get('score', 0.0)
        return 0.0
    
    @staticmethod
    def normalize_scores(scores):
        """Normalize model scores."""
        if not scores:
            return []
        
        # Convert to numpy array for processing
        score_values = [score.get('score', 0.0) for score in scores]
        normalized = np.array(score_values)
        
        # Normalize to 0-1 range
        if np.max(normalized) > 0:
            normalized = normalized / np.max(normalized)
        
        return normalized.tolist()
    
    @staticmethod
    def get_top_predictions(scores, top_k=3):
        """Get top K predictions from scores."""
        if not scores:
            return []
        
        # Sort by score
        sorted_scores = sorted(scores, key=lambda x: x.get('score', 0.0), reverse=True)
        return sorted_scores[:top_k]
    
    @staticmethod
    def validate_model_output(output):
        """Validate model output format."""
        if not isinstance(output, list):
            return False
        
        for item in output:
            if not isinstance(item, dict):
                return False
            if 'label' not in item or 'score' not in item:
                return False
        
        return True
