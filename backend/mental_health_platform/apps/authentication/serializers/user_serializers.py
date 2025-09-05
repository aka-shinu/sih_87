"""
User serializers for mental health platform.
"""
from rest_framework import serializers
from django.contrib.auth.models import User
from ..models.user_models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """User profile serializer."""
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    
    class Meta:
        model = UserProfile
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'phone', 'date_of_birth', 'gender', 'university',
            'student_id', 'emergency_contact', 'preferred_language',
            'timezone', 'is_verified', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        user = instance.user
        
        for attr, value in user_data.items():
            setattr(user, attr, value)
        user.save()
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        return instance


class UserListSerializer(serializers.ModelSerializer):
    """User list serializer for admin."""
    profile = UserProfileSerializer(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'profile']


class UserCreateSerializer(serializers.ModelSerializer):
    """User creation serializer for admin."""
    password = serializers.CharField(write_only=True, min_length=8)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'is_active']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    """User update serializer for admin."""
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_active']
