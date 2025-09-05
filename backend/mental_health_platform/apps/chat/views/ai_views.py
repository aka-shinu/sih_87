"""
AI processing views for mental health platform.
"""
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from mental_health_platform.ai.services.ai_service import MentalHealthAI
from ..models.ai_models import AIAnalysis, CrisisAlert
from ..serializers.ai_serializers import AIAnalysisSerializer, CrisisAlertSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def analyze_message_view(request):
    """Analyze message for sentiment and emotion."""
    message_text = request.data.get('message')
    
    if not message_text:
        return Response({'error': 'Message is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        ai_service = MentalHealthAI()
        analysis = ai_service.analyze_text(message_text)
        
        # Save analysis to database
        ai_analysis = AIAnalysis.objects.create(
            user=request.user,
            message_text=message_text,
            sentiment_score=analysis['sentiment_score'],
            emotion_score=analysis['emotion_score'],
            confidence=analysis['confidence'],
            analysis_data=analysis
        )
        
        serializer = AIAnalysisSerializer(ai_analysis)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def detect_crisis_view(request):
    """Detect crisis situation from message."""
    message_text = request.data.get('message')
    
    if not message_text:
        return Response({'error': 'Message is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        ai_service = MentalHealthAI()
        crisis_analysis = ai_service.detect_crisis(message_text)
        
        # Save crisis detection to database
        crisis_detection = CrisisDetection.objects.create(
            user=request.user,
            message_content=message_text,
            risk_level=crisis_analysis['risk_level'],
            risk_score=crisis_analysis['risk_score'],
            keywords_found=crisis_analysis['keywords_found'],
            confidence=crisis_analysis['confidence']
        )
        
        serializer = CrisisDetectionSerializer(crisis_detection)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ai_analysis_history_view(request):
    """Get AI analysis history for user."""
    analyses = AIAnalysis.objects.filter(user=request.user).order_by('-created_at')[:50]
    serializer = AIAnalysisSerializer(analyses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def crisis_detection_history_view(request):
    """Get crisis detection history for user."""
    detections = CrisisDetection.objects.filter(user=request.user).order_by('-created_at')[:20]
    serializer = CrisisDetectionSerializer(detections, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def generate_response_view(request):
    """Generate AI response to user message."""
    message_text = request.data.get('message')
    context = request.data.get('context', {})
    
    if not message_text:
        return Response({'error': 'Message is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        ai_service = MentalHealthAI()
        response = ai_service.generate_response(message_text, context)
        
        return Response({
            'response': response['response'],
            'sentiment': response['sentiment'],
            'confidence': response['confidence'],
            'suggestions': response.get('suggestions', [])
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
