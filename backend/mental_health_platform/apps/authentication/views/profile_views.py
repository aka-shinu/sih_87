"""
Profile management views for mental health platform.
"""
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers.user_serializers import UserProfileSerializer


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def profile_detail_view(request):
    """Get or update user profile."""
    if request.method == 'GET':
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = UserProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password_view(request):
    """Change user password."""
    old_password = request.data.get('old_password')
    new_password = request.data.get('new_password')
    
    if not old_password or not new_password:
        return Response({
            'error': 'Old password and new password are required'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    if not request.user.check_password(old_password):
        return Response({
            'error': 'Invalid old password'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    if len(new_password) < 8:
        return Response({
            'error': 'New password must be at least 8 characters long'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    request.user.set_password(new_password)
    request.user.save()
    
    return Response({
        'message': 'Password changed successfully'
    }, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_account_view(request):
    """Delete user account."""
    password = request.data.get('password')
    
    if not password:
        return Response({
            'error': 'Password is required to delete account'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    if not request.user.check_password(password):
        return Response({
            'error': 'Invalid password'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    request.user.delete()
    
    return Response({
        'message': 'Account deleted successfully'
    }, status=status.HTTP_200_OK)
