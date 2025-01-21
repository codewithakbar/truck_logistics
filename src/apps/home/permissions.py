from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrDispatcherOrReadOnly(BasePermission):
    """
    Custom permission to allow access only to:
    - Admin users (is_staff=True),
    - Users with 'dispatcher' user type for all actions (POST, PUT, DELETE).
    All other users are restricted to read-only methods (GET, HEAD, OPTIONS).
    """
    
    def has_permission(self, request, view):
        # Allow read-only methods for any authenticated user
        if request.method in SAFE_METHODS:
            return True
        
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Allow admin users or users with 'dispatcher' user type to perform write actions
        return request.user.is_staff or getattr(request.user, 'user_type', None) == 'dispatcher'
