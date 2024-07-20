from django.shortcuts import get_object_or_404

from .models import FoodsModel


def get_food_by_id(food_id: str):
    food = get_object_or_404(FoodsModel, pk=food_id)
    return food
