from rest_framework.permissions import BasePermission
from users.roles import USER_ROLE_GROUPS, RolesEnum


class CanOrder(BasePermission):
    def has_permission(self, request, view):
        if RolesEnum.can_order.value in USER_ROLE_GROUPS.get(request.user.role):
            return True
        if RolesEnum.all.value in USER_ROLE_GROUPS.get(request.user.role):
            return True
        return False


class CanAcceptOrder(BasePermission):
    def has_permission(self, request, view):
        if RolesEnum.can_accept_order.value in USER_ROLE_GROUPS.get(request.user.role):
            return True
        if RolesEnum.all.value in USER_ROLE_GROUPS.get(request.user.role):
            return True
        return False


class CanSendOrder(BasePermission):
    def has_permission(self, request, view):
        if RolesEnum.can_send_order.value in USER_ROLE_GROUPS.get(request.user.role):
            return True
        if RolesEnum.all.value in USER_ROLE_GROUPS.get(request.user.role):
            return True
        return False


class CanViewOrder(BasePermission):
    def has_permission(self, request, view):
        if RolesEnum.can_view_order.value in USER_ROLE_GROUPS.get(request.user.role):
            return True
        if RolesEnum.all.value in USER_ROLE_GROUPS.get(request.user.role):
            return True
        return False
