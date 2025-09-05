"""
Admin configuration for chat app.
"""
from django.contrib import admin
from .models.chat_models import ChatSession, Message
from .models.ai_models import AIAnalysis, CrisisAlert
from .models.session_models import ChatSessionState, ChatMetrics


@admin.register(ChatSession)
class ChatSessionAdmin(admin.ModelAdmin):
    """Chat session admin."""
    list_display = ('id', 'user', 'session_id', 'is_active', 'message_count', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('user__email', 'session_id')
    readonly_fields = ('created_at', 'updated_at')
    
    def message_count(self, obj):
        """Get message count for session."""
        return obj.messages.count()
    
    def get_queryset(self, request):
        """Optimize queryset."""
        return super().get_queryset(request).select_related('user')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Message admin."""
    list_display = ('id', 'session', 'message_type', 'content_preview', 'created_at')
    list_filter = ('message_type', 'created_at')
    search_fields = ('session__session_id', 'content')
    readonly_fields = ('created_at',)
    
    def content_preview(self, obj):
        """Show content preview."""
        if len(obj.content) > 50:
            return obj.content[:50] + '...'
        return obj.content
    
    def get_queryset(self, request):
        """Optimize queryset."""
        return super().get_queryset(request).select_related('session', 'session__user')


@admin.register(AIAnalysis)
class AIAnalysisAdmin(admin.ModelAdmin):
    """AI analysis admin."""
    list_display = ('id', 'message', 'analysis_type', 'confidence', 'created_at')
    list_filter = ('analysis_type', 'created_at', 'confidence')
    search_fields = ('message__content', 'analysis_type')
    readonly_fields = ('created_at',)
    
    def get_queryset(self, request):
        """Optimize queryset."""
        return super().get_queryset(request).select_related('message', 'model')


@admin.register(CrisisAlert)
class CrisisAlertAdmin(admin.ModelAdmin):
    """Crisis alert admin."""
    list_display = ('id', 'user', 'alert_level', 'risk_score', 'is_resolved', 'created_at')
    list_filter = ('alert_level', 'is_resolved', 'created_at')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('created_at',)
    
    def get_queryset(self, request):
        """Optimize queryset."""
        return super().get_queryset(request).select_related('user')


@admin.register(ChatSessionState)
class ChatSessionStateAdmin(admin.ModelAdmin):
    """Chat session state admin."""
    list_display = ('id', 'session', 'last_activity', 'created_at')
    list_filter = ('created_at', 'last_activity')
    search_fields = ('session__title', 'session__session_id')
    readonly_fields = ('created_at', 'last_activity')
    
    def get_queryset(self, request):
        """Optimize queryset."""
        return super().get_queryset(request).select_related('session', 'session__user')


@admin.register(ChatMetrics)
class ChatMetricsAdmin(admin.ModelAdmin):
    """Chat metrics admin."""
    list_display = ('id', 'session', 'total_messages', 'user_messages', 'ai_messages', 'avg_response_time', 'created_at')
    list_filter = ('created_at', 'total_messages')
    search_fields = ('session__title', 'session__session_id')
    readonly_fields = ('created_at', 'updated_at')
    
    def get_queryset(self, request):
        """Optimize queryset."""
        return super().get_queryset(request).select_related('session', 'session__user')
