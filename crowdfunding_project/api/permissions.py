from rest_framework import permissions
from campaigns.models import (
    Campaign,
    Bonus,
)


class ModifyIfOwnerOrRead(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'create':
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'partial_update', 'destroy']:
            if type(obj) == Campaign:
                return obj.owner == request.user or request.user.is_staff
            elif type(obj) == Bonus:
                return obj.campaign.owner == request.user or request.user.is_staff
            else:
                return False  # пересмотреть
        else:
            return True
