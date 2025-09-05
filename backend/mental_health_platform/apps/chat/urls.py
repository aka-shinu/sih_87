"""
Chat URLs.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import chat_views, ai_views, session_views, ai_test_views, ai_test_template_views

app_name = 'chat'

urlpatterns = [
    # Chat URLs
    path('sessions/', chat_views.chat_sessions_view, name='chat_sessions'),
    path('sessions/<int:session_id>/', chat_views.chat_session_detail_view, name='chat_session_detail'),
    path('sessions/<int:session_id>/messages/', chat_views.messages_view, name='messages'),
    path('sessions/active/', chat_views.active_sessions_view, name='active_sessions'),
    
    # AI URLs
    path('ai/analyze/', ai_views.analyze_message_view, name='analyze_message'),
    path('ai/crisis/', ai_views.detect_crisis_view, name='detect_crisis'),
    path('ai/response/', ai_views.generate_response_view, name='generate_response'),
    path('ai/history/', ai_views.ai_analysis_history_view, name='ai_history'),
    path('ai/crisis/history/', ai_views.crisis_detection_history_view, name='crisis_history'),
    
    # AI Test URLs
    path('ai/test/', ai_test_views.ai_test_dashboard, name='ai_test_dashboard'),
    path('ai/test/sentiment/', ai_test_views.test_sentiment_analysis, name='test_sentiment'),
    path('ai/test/emotion/', ai_test_views.test_emotion_analysis, name='test_emotion'),
    path('ai/test/crisis/', ai_test_views.test_crisis_detection, name='test_crisis'),
    path('ai/test/voice/', ai_test_views.test_voice_analysis, name='test_voice'),
    path('ai/test/behavioral/', ai_test_views.test_behavioral_analysis, name='test_behavioral'),
    path('ai/test/full/', ai_test_views.test_full_analysis, name='test_full_analysis'),
    path('ai/test/models/', ai_test_views.test_models_status, name='test_models_status'),
    
    # AI Test Template URLs
    path('ai-test/', ai_test_template_views.ai_test_dashboard_view, name='ai_test_dashboard_view'),
    path('ai-test/api/status/', ai_test_template_views.ai_test_api_status, name='ai_test_api_status'),
]
