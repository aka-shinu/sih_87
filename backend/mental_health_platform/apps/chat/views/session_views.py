"""
Session management views for mental health platform.
"""
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models.chat_models import ChatSession
from ..models.session_models import ChatSessionState, ChatMetrics
from ..serializers.chat_serializers import ChatSessionSerializer
from django.utils import timezone


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_session_view(request):
    """Create new chat session."""
    session_data = {
        'title': request.data.get('title', 'New Chat Session'),
        'is_active': True,
        'user': request.user.id
    }
    
    serializer = ChatSessionSerializer(data=session_data)
    if serializer.is_valid():
        session = serializer.save()
        
        # Create initial session state
        ChatSessionState.objects.create(
            session=session,
            current_context={'title': session.title},
            user_preferences={}
        )
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_session_view(request, session_id):
    """Update chat session."""
    try:
        session = ChatSession.objects.get(id=session_id, user=request.user)
    except ChatSession.DoesNotExist:
        return Response({'error': 'Session not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ChatSessionSerializer(session, data=request.data, partial=True)
    if serializer.is_valid():
        updated_session = serializer.save()
        
        # Update session state
        session_state, created = ChatSessionState.objects.get_or_create(
            session=updated_session,
            defaults={'current_context': {}, 'user_preferences': {}}
        )
        session_state.current_context.update({'last_update': request.data})
        session_state.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def end_session_view(request, session_id):
    """End chat session."""
    try:
        session = ChatSession.objects.get(id=session_id, user=request.user)
    except ChatSession.DoesNotExist:
        return Response({'error': 'Session not found'}, status=status.HTTP_404_NOT_FOUND)
    
    session.is_active = False
    session.ended_at = timezone.now()
    session.save()
    
    # Update session state
    try:
        session_state = ChatSessionState.objects.get(session=session)
        session_state.current_context['ended'] = True
        session_state.current_context['duration'] = str(session.ended_at - session.created_at)
        session_state.save()
    except ChatSessionState.DoesNotExist:
        pass
    
    return Response({'message': 'Session ended successfully'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def session_activity_view(request, session_id):
    """Get session state and metrics."""
    try:
        session = ChatSession.objects.get(id=session_id, user=request.user)
    except ChatSession.DoesNotExist:
        return Response({'error': 'Session not found'}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        session_state = ChatSessionState.objects.get(session=session)
        state_data = {
            'current_context': session_state.current_context,
            'user_preferences': session_state.user_preferences,
            'last_activity': session_state.last_activity,
            'created_at': session_state.created_at
        }
    except ChatSessionState.DoesNotExist:
        state_data = None
    
    try:
        metrics = ChatMetrics.objects.get(session=session)
        metrics_data = {
            'total_messages': metrics.total_messages,
            'user_messages': metrics.user_messages,
            'ai_messages': metrics.ai_messages,
            'avg_response_time': metrics.avg_response_time,
            'sentiment_trend': metrics.sentiment_trend
        }
    except ChatMetrics.DoesNotExist:
        metrics_data = None
    
    return Response({
        'session_id': session_id,
        'state': state_data,
        'metrics': metrics_data
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def session_stats_view(request, session_id):
    """Get session statistics."""
    try:
        session = ChatSession.objects.get(id=session_id, user=request.user)
    except ChatSession.DoesNotExist:
        return Response({'error': 'Session not found'}, status=status.HTTP_404_NOT_FOUND)
    
    from ..models.chat_models import Message
    
    message_count = Message.objects.filter(session=session).count()
    user_messages = Message.objects.filter(session=session, message_type='user').count()
    ai_messages = Message.objects.filter(session=session, message_type='ai').count()
    
    duration = None
    if hasattr(session, 'ended_at') and session.ended_at:
        duration = str(session.ended_at - session.created_at)
    else:
        duration = str(timezone.now() - session.created_at)
    
    return Response({
        'session_id': session_id,
        'total_messages': message_count,
        'user_messages': user_messages,
        'ai_messages': ai_messages,
        'duration': duration,
        'is_active': session.is_active,
        'created_at': session.created_at,
        'updated_at': session.updated_at
    }, status=status.HTTP_200_OK)
