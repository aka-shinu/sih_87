"""
Permission utilities for mental health platform.
"""
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework.permissions import BasePermission


class IsStudent(BasePermission):
    """Permission class for students."""
    
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            hasattr(request.user, 'profile') and
            request.user.profile.role == 'student'
        )


class IsCounselor(BasePermission):
    """Permission class for counselors."""
    
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            hasattr(request.user, 'profile') and
            request.user.profile.role == 'counselor'
        )


class IsAdmin(BasePermission):
    """Permission class for admins."""
    
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            hasattr(request.user, 'profile') and
            request.user.profile.role == 'admin'
        )


class PermissionUtils:
    """Permission utility functions."""
    
    @staticmethod
    def create_permissions():
        """Create custom permissions."""
        from ..models.user_models import UserProfile
        
        content_type = ContentType.objects.get_for_model(UserProfile)
        
        permissions = [
            ('can_view_analytics', 'Can view analytics'),
            ('can_manage_resources', 'Can manage resources'),
            ('can_access_admin', 'Can access admin dashboard'),
            ('can_view_reports', 'Can view reports'),
            ('can_manage_users', 'Can manage users'),
        ]
        
        for codename, name in permissions:
            Permission.objects.get_or_create(
                codename=codename,
                name=name,
                content_type=content_type
            )
    
    @staticmethod
    def assign_role_permissions(user, role):
        """Assign permissions based on role."""
        permissions = PermissionUtils.get_role_permissions(role)
        user.user_permissions.set(permissions)
    
    @staticmethod
    def get_role_permissions(role):
        """Get permissions for a specific role."""
        permission_codenames = {
            'student': ['can_view_analytics'],
            'counselor': ['can_view_analytics', 'can_view_reports'],
            'admin': [
                'can_view_analytics', 'can_manage_resources', 
                'can_access_admin', 'can_view_reports', 'can_manage_users'
            ]
        }
        
        codenames = permission_codenames.get(role, [])
        return Permission.objects.filter(codename__in=codenames)
    
    @staticmethod
    def has_permission(user, permission_codename):
        """Check if user has specific permission."""
        return user.has_perm(f'authentication.{permission_codename}')
    
    @staticmethod
    def get_user_permissions(user):
        """Get all user permissions."""
        return user.get_all_permissions()
