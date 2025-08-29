from rest_framework import permissions


class CanEditOrNot(permissions.BasePermission):
    message = "You Can not Edit or Delete a Completed Task"

    def has_object_permission(self, request, view, obj):
        if request.method in  permissions.SAFE_METHODS:
            return True
        return not obj.is_completed
