"""
Admin configuration for authentication app.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models.user_models import UserProfile
from .models.role_models import UserRole
from .models.session_models import UserSession


class UserProfileInline(admin.StackedInline):
    """Inline admin for user profile."""
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'


class UserAdmin(BaseUserAdmin):
    """Custom user admin."""
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """User profile admin."""
    list_display = ('user', 'preferred_language', 'created_at')
    list_filter = ('preferred_language', 'created_at')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('User Information', {
            'fields': ('user',)
        }),
        ('Profile Details', {
            'fields': ('bio', 'avatar')
        }),
        ('Preferences', {
            'fields': ('preferred_language', 'privacy_settings')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    """User role admin."""
    list_display = ('user', 'role', 'assigned_at')
    list_filter = ('assigned_at', 'role')
    search_fields = ('user__email', 'role__name')
    readonly_fields = ('assigned_at',)
    
    def get_queryset(self, request):
        """Optimize queryset."""
        return super().get_queryset(request).select_related('user', 'role')


@admin.register(UserSession)
class UserSessionAdmin(admin.ModelAdmin):
    """User session admin."""
    list_display = ('user', 'ip_address', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at', 'last_activity')
    search_fields = ('user__email', 'ip_address')
    readonly_fields = ('created_at', 'last_activity')
    
    def get_queryset(self, request):
        """Filter sessions for admin."""
        return super().get_queryset(request).select_related('user')


# Register custom User admin
admin.site.register(User, UserAdmin)