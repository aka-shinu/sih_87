"""
URL configuration for mental health platform.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('mental_health_platform.apps.authentication.urls')),
    path('api/chat/', include('mental_health_platform.apps.chat.urls')),
    path('api/analytics/', include('mental_health_platform.apps.analytics.urls')),
    path('api/resources/', include('mental_health_platform.apps.resources.urls')),
    path('api/blockchain/', include('mental_health_platform.apps.blockchain.urls')),
    path('api/admin/', include('mental_health_platform.apps.admin_dashboard.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
