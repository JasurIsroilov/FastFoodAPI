from datetime import datetime, timedelta, timezone

from django.shortcuts import get_object_or_404

from .models import OrdersModel

from foods.services import get_food_by_id


def count_delivery_time(data: dict):
    # 1km = 180 sec
    # 1order = 75 sec
    seconds = int(data.get("distance")) * 180 + 75
    delivery = (timedelta(seconds=seconds) + datetime.now()).timestamp()
    return datetime.fromtimestamp(delivery, tz=timezone(timedelta(hours=3)))


def save_ordered_food(request):
    order = OrdersModel()
    order.status = request.data.get("status")
    order.distance = request.data.get("distance")
    order.delivery_at = count_delivery_time(request.data)
    order.author = request.user
    order.food = get_food_by_id(request.data.get("food"))
    order.save()


def update_order_status(request):
    order = get_object_or_404(OrdersModel, pk=request.data.get("id", None))
    order.status = request.data.get("status")
    order.waiter = request.user
    order.save()
    return
