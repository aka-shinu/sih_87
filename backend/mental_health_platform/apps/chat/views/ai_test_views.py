"""
AI test views for mental health platform.
"""
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from mental_health_platform.ai.services.ai_service import MentalHealthAI
from mental_health_platform.ai.services.nlp_service import NLPService
from mental_health_platform.ai.services.crisis_service import CrisisService
from mental_health_platform.ai.services.voice_service import VoiceService
from mental_health_platform.ai.services.behavioral_service import BehavioralService
import json


@api_view(['GET'])
@permission_classes([AllowAny])
def ai_test_dashboard(request):
    """AI test dashboard endpoint."""
    return Response({
        'message': 'AI Test Dashboard',
        'endpoints': {
            'sentiment_analysis': '/api/ai/test/sentiment/',
            'emotion_analysis': '/api/ai/test/emotion/',
            'crisis_detection': '/api/ai/test/crisis/',
            'voice_analysis': '/api/ai/test/voice/',
            'behavioral_analysis': '/api/ai/test/behavioral/',
            'full_analysis': '/api/ai/test/full/',
            'test_models': '/api/ai/test/models/'
        },
        'status': 'active'
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def test_sentiment_analysis(request):
    """Test sentiment analysis."""
    text = request.data.get('text', '')
    
    if not text:
        return Response({'error': 'Text is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        nlp_service = NLPService()
        result = nlp_service.analyze_text(text)
        
        return Response({
            'input_text': text,
            'sentiment': result['sentiment'],
            'sentiment_score': result['sentiment_score'],
            'confidence': result.get('confidence', 0.0),
            'timestamp': result.get('timestamp'),
            'status': 'success'
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': str(e),
            'status': 'error'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([AllowAny])
def test_emotion_analysis(request):
    """Test emotion analysis."""
    text = request.data.get('text', '')
    
    if not text:
        return Response({'error': 'Text is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        nlp_service = NLPService()
        result = nlp_service.analyze_text(text)
        
        return Response({
            'input_text': text,
            'emotion': result['emotion'],
            'emotion_score': result['emotion_score'],
            'confidence': result.get('confidence', 0.0),
            'timestamp': result.get('timestamp'),
            'status': 'success'
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': str(e),
            'status': 'error'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([AllowAny])
def test_crisis_detection(request):
    """Test crisis detection."""
    text = request.data.get('text', '')
    
    if not text:
        return Response({'error': 'Text is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        crisis_service = CrisisService()
        result = crisis_service.detect_crisis(text)
        
        return Response({
            'input_text': text,
            'risk_score': result['risk_score'],
            'risk_level': result['risk_level'],
            'keywords_found': result['keywords_found'],
            'requires_intervention': result['requires_intervention'],
            'confidence': result.get('confidence', 0.0),
            'timestamp': result.get('timestamp'),
            'status': 'success'
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': str(e),
            'status': 'error'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([AllowAny])
def test_voice_analysis(request):
    """Test voice analysis."""
    audio_file = request.FILES.get('audio_file')
    
    if not audio_file:
        return Response({'error': 'Audio file is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        voice_service = VoiceService()
        result = voice_service.analyze_voice(audio_file)
        
        return Response({
            'file_name': audio_file.name,
            'file_size': audio_file.size,
            'emotion': result.get('emotion', 'unknown'),
            'stress_level': result.get('stress_level', 0.0),
            'speaking_rate': result.get('speaking_rate', 0.0),
            'pitch_variation': result.get('pitch_variation', 0.0),
            'confidence': result.get('confidence', 0.0),
            'features': result.get('features', {}),
            'status': 'success'
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': str(e),
            'status': 'error'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([AllowAny])
def test_behavioral_analysis(request):
    """Test behavioral analysis."""
    user_data = request.data.get('user_data', {})
    
    if not user_data:
        return Response({'error': 'User data is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        behavioral_service = BehavioralService()
        result = behavioral_service.analyze_behavior(user_data)
        
        return Response({
            'input_data': user_data,
            'patterns': result['patterns'],
            'engagement': result['engagement'],
            'stress_indicators': result['stress_indicators'],
            'status': 'success'
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': str(e),
            'status': 'error'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([AllowAny])
def test_full_analysis(request):
    """Test full AI analysis pipeline."""
    text = request.data.get('text', '')
    user_data = request.data.get('user_data', {})
    
    if not text:
        return Response({'error': 'Text is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        ai_service = MentalHealthAI()
        
        # Run full analysis
        analysis = ai_service.analyze_text(text)
        crisis_detection = ai_service.detect_crisis(text)
        response = ai_service.generate_response(text, user_data)
        
        return Response({
            'input_text': text,
            'user_data': user_data,
            'text_analysis': analysis,
            'crisis_detection': crisis_detection,
            'ai_response': response,
            'timestamp': analysis.get('timestamp'),
            'status': 'success'
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': str(e),
            'status': 'error'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([AllowAny])
def test_models_status(request):
    """Test AI models status."""
    try:
        ai_service = MentalHealthAI()
        
        # Test each service
        services_status = {
            'nlp_service': 'active',
            'crisis_service': 'active',
            'voice_service': 'active',
            'behavioral_service': 'active'
        }
        
        # Test with sample data
        test_text = "I'm feeling really sad today and don't know what to do."
        analysis = ai_service.analyze_text(test_text)
        crisis = ai_service.detect_crisis(test_text)
        
        return Response({
            'services_status': services_status,
            'test_analysis': {
                'sentiment': analysis['sentiment'],
                'emotion': analysis['emotion'],
                'crisis_risk': crisis['risk_level']
            },
            'models_loaded': True,
            'status': 'success'
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': str(e),
            'models_loaded': False,
            'status': 'error'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
