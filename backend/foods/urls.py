from django.urls import path
from foods.views import (
    CreateFoodAPIView,
    ListFoodsAPIView,
    DeleteFoodAPIView,
    UpdateFoodAPIView,
)


urlpatterns = [
    path("create", CreateFoodAPIView.as_view(), name="create_food"),
    path("menu", ListFoodsAPIView.as_view(), name="list_foods"),
    path("delete/<str:pk>", DeleteFoodAPIView.as_view(), name="delete_food"),
    path("update/<str:pk>", UpdateFoodAPIView.as_view(), name="update_food"),
]
