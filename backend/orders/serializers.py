from rest_framework.serializers import (
    ModelSerializer,
    ChoiceField,
    UUIDField,
)

from .models import OrdersModel
from .order_statuses import OrderStatusesEnum


class OrderCreateSerializer(ModelSerializer):

    status = ChoiceField(choices=[OrderStatusesEnum.ordered.value])

    class Meta:
        model = OrdersModel
        fields = ["status", "distance", "food"]


class OrderAcceptSerializer(ModelSerializer):

    id = UUIDField()
    status = ChoiceField(choices=[OrderStatusesEnum.accepted.value])

    class Meta:
        model = OrdersModel
        fields = ["id", "status"]


class OrderSendSerializer(ModelSerializer):

    id = UUIDField()
    status = ChoiceField(choices=[OrderStatusesEnum.sent.value])

    class Meta:
        model = OrdersModel
        fields = ["id", "status"]


class OrderRetrieveSerializer(ModelSerializer):

    class Meta:
        model = OrdersModel
        fields = "__all__"
