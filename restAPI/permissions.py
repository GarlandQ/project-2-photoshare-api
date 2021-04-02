from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    # Only allow owners of the account to edit
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only allow write permissions to the owner
        return obj.user == request.user