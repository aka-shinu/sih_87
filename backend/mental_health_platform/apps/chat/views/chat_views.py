"""
Chat views for mental health platform.
"""
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models.chat_models import ChatSession, Message
from ..serializers.chat_serializers import ChatSessionSerializer, MessageSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def chat_sessions_view(request):
    """Get or create chat sessions."""
    if request.method == 'GET':
        sessions = ChatSession.objects.filter(user=request.user).order_by('-created_at')
        serializer = ChatSessionSerializer(sessions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = ChatSessionSerializer(data=request.data)
        if serializer.is_valid():
            session = serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def chat_session_detail_view(request, session_id):
    """Get, update, or delete specific chat session."""
    try:
        session = ChatSession.objects.get(id=session_id, user=request.user)
    except ChatSession.DoesNotExist:
        return Response({'error': 'Session not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ChatSessionSerializer(session)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = ChatSessionSerializer(session, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        session.delete()
        return Response({'message': 'Session deleted'}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def messages_view(request, session_id):
    """Get or create messages for a session."""
    try:
        session = ChatSession.objects.get(id=session_id, user=request.user)
    except ChatSession.DoesNotExist:
        return Response({'error': 'Session not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        messages = Message.objects.filter(session=session).order_by('created_at')
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            message = serializer.save(session=session, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def active_sessions_view(request):
    """Get active chat sessions."""
    active_sessions = ChatSession.objects.filter(
        user=request.user,
        is_active=True
    ).order_by('-last_activity')
    
    serializer = ChatSessionSerializer(active_sessions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
