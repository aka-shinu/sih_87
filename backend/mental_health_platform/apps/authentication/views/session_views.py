"""
Session management views for mental health platform.
"""
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.sessions.models import Session
from django.utils import timezone
from datetime import timedelta


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def active_sessions_view(request):
    """Get active user sessions."""
    user_sessions = Session.objects.filter(
        expire_date__gte=timezone.now(),
        session_key__in=request.user.session_set.values_list('session_key', flat=True)
    )
    
    sessions_data = []
    for session in user_sessions:
        sessions_data.append({
            'session_key': session.session_key,
            'expire_date': session.expire_date,
            'is_current': session.session_key == request.session.session_key
        })
    
    return Response({
        'sessions': sessions_data,
        'count': len(sessions_data)
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def terminate_session_view(request):
    """Terminate a specific session."""
    session_key = request.data.get('session_key')
    
    if not session_key:
        return Response({
            'error': 'Session key is required'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        session = Session.objects.get(session_key=session_key)
        if session.expire_date >= timezone.now():
            session.delete()
            return Response({
                'message': 'Session terminated successfully'
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'error': 'Session already expired'
            }, status=status.HTTP_400_BAD_REQUEST)
    except Session.DoesNotExist:
        return Response({
            'error': 'Session not found'
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def terminate_all_sessions_view(request):
    """Terminate all user sessions except current."""
    current_session_key = request.session.session_key
    
    user_sessions = Session.objects.filter(
        expire_date__gte=timezone.now(),
        session_key__in=request.user.session_set.values_list('session_key', flat=True)
    ).exclude(session_key=current_session_key)
    
    terminated_count = user_sessions.count()
    user_sessions.delete()
    
    return Response({
        'message': f'{terminated_count} sessions terminated successfully'
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def session_info_view(request):
    """Get current session information."""
    session = request.session
    return Response({
        'session_key': session.session_key,
        'created_at': session.get('created_at'),
        'last_activity': session.get('last_activity'),
        'is_authenticated': request.user.is_authenticated
    }, status=status.HTTP_200_OK)
