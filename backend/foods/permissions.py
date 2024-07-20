from rest_framework.permissions import BasePermission
from users.roles import USER_ROLE_GROUPS, RolesEnum


class CanAddFood(BasePermission):
    def has_permission(self, request, view):
        if RolesEnum.can_add_food.value in USER_ROLE_GROUPS.get(request.user.role):
            return True
        if RolesEnum.all.value in USER_ROLE_GROUPS.get(request.user.role):
            return True
        return False


class CanUpdateFood(BasePermission):
    def has_permission(self, request, view):
        if RolesEnum.can_update_food.value in USER_ROLE_GROUPS.get(request.user.role):
            return True
        if RolesEnum.all.value in USER_ROLE_GROUPS.get(request.user.role):
            return True
        return False


class CanDeleteFood(BasePermission):
    def has_permission(self, request, view):
        if RolesEnum.can_delete_food.value in USER_ROLE_GROUPS.get(request.user.role):
            return True
        if RolesEnum.all.value in USER_ROLE_GROUPS.get(request.user.role):
            return True
        return False


class CanGetMenu(BasePermission):
    def has_permission(self, request, view):
        if RolesEnum.can_get_menu.value in USER_ROLE_GROUPS.get(request.user.role):
            return True
        if RolesEnum.all.value in USER_ROLE_GROUPS.get(request.user.role):
            return True
        return False
