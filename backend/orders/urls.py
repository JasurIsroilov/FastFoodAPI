from django.urls import path

from .views import (
    OrderCreateAPIView,
    OrderAcceptAPIView,
    OrderSendAPIView,
    OrdersListAPIView,
    OrderRetrieveAPIView,
)


urlpatterns = [
    path("create", OrderCreateAPIView.as_view(), name="create_order"),
    path("accept", OrderAcceptAPIView.as_view(), name="accept_order"),
    path("send", OrderSendAPIView.as_view(), name="send_order"),
    path("list", OrdersListAPIView.as_view(), name="list_order"),
    path("<str:pk>", OrderRetrieveAPIView.as_view(), name="get_order"),
]
