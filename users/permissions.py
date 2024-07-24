from rest_framework import permissions


class IsModers(permissions.BasePermission):
    """Проверяет, являестся ли пользователь модератором."""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moders").exists()


class IsOwner(permissions.BasePermission):
    """Проверяет, являестся ли пользователь владеьцем."""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
