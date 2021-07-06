from rest_framework import permissions


class IsAutenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            if request.user.username == 'divinoluiz':
                return True
            return False
        return False
