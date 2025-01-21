from rest_framework.permissions import BasePermission
from rest_framework import permissions

class IsAdminOrDispatcher(BasePermission):
    """
    Custom permission to allow access only to admin users or users with 'dispatcher' user type
    for all actions (POST, PUT, DELETE).
    Non-admin, non-dispatcher users are restricted to read-only methods (GET, HEAD, OPTIONS).
    """
    
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # If the request method is one of the safe methods (GET, HEAD, OPTIONS), allow it
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Check if the user is an admin or has the 'dispatcher' user type for write operations
        if request.user.is_staff or request.user.user_type == 'dispatcher':
            return True
        
        # If the user is neither an admin nor a dispatcher, deny all write actions
        return False
