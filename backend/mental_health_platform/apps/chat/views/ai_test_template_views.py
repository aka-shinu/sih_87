from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@permission_classes([AllowAny])
def ai_test_dashboard_view(request):
    return render(request, 'ai-test/index.html')


@api_view(['GET'])
@permission_classes([AllowAny])
def ai_test_api_status(request):
    return JsonResponse({
        'status': 'active',
        'endpoints': {
            'dashboard': '/ai-test/',
            'sentiment': '/api/chat/ai/test/sentiment/',
            'emotion': '/api/chat/ai/test/emotion/',
            'crisis': '/api/chat/ai/test/crisis/',
            'voice': '/api/chat/ai/test/voice/',
            'behavioral': '/api/chat/ai/test/behavioral/',
            'full': '/api/chat/ai/test/full/',
            'models': '/api/chat/ai/test/models/'
        }
    })
