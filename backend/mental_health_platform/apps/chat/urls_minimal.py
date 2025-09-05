"""
Minimal Chat URLs for testing.
"""
from django.urls import path
from .views import ai_test_views, ai_test_template_views

app_name = 'chat'

urlpatterns = [
    # AI Test URLs only
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
