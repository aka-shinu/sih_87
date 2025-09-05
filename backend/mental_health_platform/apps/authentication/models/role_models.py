"""
Role and permission models.
"""
from django.db import models


class Role(models.Model):
    """Role model for user permissions."""
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    permissions = models.JSONField(default=list)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserRole(models.Model):
    """User role assignment model."""
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)
    assigned_by = models.ForeignKey('authentication.User', on_delete=models.SET_NULL, null=True, related_name='assigned_roles')

    class Meta:
        unique_together = ['user', 'role']

    def __str__(self):
        return f"{self.user.email} - {self.role.name}"


class Permission(models.Model):
    """Permission model."""
    name = models.CharField(max_length=100, unique=True)
    codename = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    module = models.CharField(max_length=50)

    def __str__(self):
        return self.name
