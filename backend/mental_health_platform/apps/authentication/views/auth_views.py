"""
Authentication views for mental health platform.
"""
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .serializers.auth_serializers import LoginSerializer, RegisterSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """User login endpoint."""
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({
                'message': 'Login successful',
                'user_id': user.id,
                'username': user.username
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'error': 'Invalid credentials'
            }, status=status.HTTP_401_UNAUTHORIZED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    """User registration endpoint."""
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            'message': 'Registration successful',
            'user_id': user.id,
            'username': user.username
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout_view(request):
    """User logout endpoint."""
    logout(request)
    return Response({
        'message': 'Logout successful'
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def user_profile_view(request):
    """Get user profile."""
    if request.user.is_authenticated:
        return Response({
            'user_id': request.user.id,
            'username': request.user.username,
            'email': request.user.email,
            'is_active': request.user.is_active
        }, status=status.HTTP_200_OK)
    
    return Response({
        'error': 'User not authenticated'
    }, status=status.HTTP_401_UNAUTHORIZED)
