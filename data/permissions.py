from djoser import permissions
from rest_framework.permissions import BasePermission

class DynamicClearancePermission(BasePermission):
    def has_permission(self, request, view):
        required_level = getattr(view, 'required_level', 1)
        return request.user.is_authenticated and request.user.clearance_level >= required_level

