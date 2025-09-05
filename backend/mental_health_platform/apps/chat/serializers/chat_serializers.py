"""
Chat serializers for mental health platform.
"""
from rest_framework import serializers
from ..models.chat_models import ChatSession, Message


class MessageSerializer(serializers.ModelSerializer):
    """Message serializer."""
    
    class Meta:
        model = Message
        fields = [
            'id', 'session', 'content', 'sender', 'message_type',
            'timestamp', 'is_encrypted', 'metadata'
        ]
        read_only_fields = ['id', 'timestamp']
    
    def create(self, validated_data):
        """Create message with automatic timestamp."""
        from django.utils import timezone
        validated_data['timestamp'] = timezone.now()
        return super().create(validated_data)


class ChatSessionSerializer(serializers.ModelSerializer):
    """Chat session serializer."""
    messages = MessageSerializer(many=True, read_only=True)
    message_count = serializers.SerializerMethodField()
    
    class Meta:
        model = ChatSession
        fields = [
            'id', 'user', 'title', 'is_active', 'created_at',
            'last_activity', 'ended_at', 'messages', 'message_count'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'last_activity']
    
    def get_message_count(self, obj):
        """Get message count for session."""
        return obj.messages.count()
    
    def create(self, validated_data):
        """Create session with current timestamp."""
        from django.utils import timezone
        validated_data['created_at'] = timezone.now()
        validated_data['last_activity'] = timezone.now()
        return super().create(validated_data)


class ChatSessionListSerializer(serializers.ModelSerializer):
    """Chat session list serializer (without messages)."""
    message_count = serializers.SerializerMethodField()
    last_message = serializers.SerializerMethodField()
    
    class Meta:
        model = ChatSession
        fields = [
            'id', 'title', 'is_active', 'created_at',
            'last_activity', 'ended_at', 'message_count', 'last_message'
        ]
    
    def get_message_count(self, obj):
        """Get message count for session."""
        return obj.messages.count()
    
    def get_last_message(self, obj):
        """Get last message preview."""
        last_message = obj.messages.last()
        if last_message:
            return {
                'content': last_message.content[:100] + '...' if len(last_message.content) > 100 else last_message.content,
                'sender': last_message.sender,
                'timestamp': last_message.timestamp
            }
        return None


class MessageCreateSerializer(serializers.ModelSerializer):
    """Message creation serializer."""
    
    class Meta:
        model = Message
        fields = ['content', 'message_type', 'metadata']
    
    def validate_content(self, value):
        """Validate message content."""
        if not value or not value.strip():
            raise serializers.ValidationError("Message content cannot be empty")
        
        if len(value) > 5000:
            raise serializers.ValidationError("Message content too long (max 5000 characters)")
        
        return value.strip()
    
    def validate_message_type(self, value):
        """Validate message type."""
        valid_types = ['text', 'voice', 'image', 'file']
        if value not in valid_types:
            raise serializers.ValidationError(f"Invalid message type. Must be one of: {valid_types}")
        return value
