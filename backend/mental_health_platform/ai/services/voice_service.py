"""
Voice analysis service for mental health.
"""
try:
    import librosa
    import soundfile as sf
    import speech_recognition as sr
    import sounddevice as sd
    VOICE_AVAILABLE = True
except ImportError:
    try:
        # Fallback to basic audio processing
        import wave
        import numpy as np
        VOICE_AVAILABLE = True
        VOICE_BASIC = True
    except ImportError:
        VOICE_AVAILABLE = False
        VOICE_BASIC = False

import numpy as np
from .ai_service import MentalHealthAI


class VoiceService:
    """Voice analysis service."""
    
    def __init__(self):
        self.ai_service = MentalHealthAI()
        if not VOICE_AVAILABLE:
            print("Warning: Voice analysis libraries not available. Install librosa, soundfile, and speech_recognition for voice features.")
    
    def analyze_voice(self, audio_file_path):
        """Analyze voice for emotion and stress."""
        if not VOICE_AVAILABLE:
            return {
                'error': 'Voice analysis not available. Please install required libraries.',
                'emotion': 'unknown',
                'stress_level': 0.0,
                'speaking_rate': 0.0
            }
        
        try:
            # Load audio file
            y, sr = librosa.load(audio_file_path)
            
            # Extract features
            features = self.extract_voice_features(y, sr)
            
            # Analyze emotion
            emotion = self.detect_emotion(features)
            
            # Detect stress
            stress_level = self.detect_stress(features)
            
            return {
                'emotion': emotion,
                'stress_level': stress_level,
                'features': features,
                'duration': len(y) / sr,
                'sample_rate': sr
            }
        except Exception as e:
            return {'error': str(e)}
    
    def extract_voice_features(self, y, sr):
        """Extract voice features."""
        # Pitch
        pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
        pitch_mean = np.mean(pitches[pitches > 0])
        
        # Energy
        energy = np.sum(y**2)
        
        # Zero crossing rate
        zcr = np.mean(librosa.feature.zero_crossing_rate(y))
        
        # MFCC features
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        mfcc_mean = np.mean(mfccs, axis=1)
        
        return {
            'pitch_mean': float(pitch_mean),
            'energy': float(energy),
            'zcr': float(zcr),
            'mfcc_mean': mfcc_mean.tolist()
        }
    
    def detect_emotion(self, features):
        """Detect emotion from voice features."""
        # Simple emotion detection based on pitch and energy
        pitch = features['pitch_mean']
        energy = features['energy']
        
        if pitch > 200 and energy > 0.1:
            return 'excited'
        elif pitch < 100 and energy < 0.05:
            return 'sad'
        elif energy > 0.15:
            return 'angry'
        else:
            return 'neutral'
    
    def detect_stress(self, features):
        """Detect stress level from voice features."""
        # Stress detection based on pitch variation and energy
        pitch = features['pitch_mean']
        energy = features['energy']
        zcr = features['zcr']
        
        # Higher pitch variation and energy indicates stress
        stress_score = (pitch / 300) + (energy * 10) + (zcr * 100)
        return min(stress_score, 1.0)
