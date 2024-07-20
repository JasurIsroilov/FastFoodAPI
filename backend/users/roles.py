from enum import Enum


class RolesEnum(Enum):
    can_add_food = "add_food"
    can_update_food = "update_food"
    can_delete_food = "delete_food"
    can_view_order = "get_order"
    can_accept_order = "accept order"
    can_send_order = "send_order"
    can_get_menu = "get_menu"
    can_order = "order"
    all = "__all__"


USER_ROLE_GROUPS = {
    "user": [RolesEnum.can_get_menu.value, RolesEnum.can_order.value],
    "waiter": [RolesEnum.can_add_food.value, RolesEnum.can_update_food.value, RolesEnum.can_delete_food.value,
               RolesEnum.can_view_order.value, RolesEnum.can_accept_order.value, RolesEnum.can_send_order.value],
    "admin": [RolesEnum.all.value],
}
