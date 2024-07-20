from rest_framework.serializers import (
    ModelSerializer,
    UUIDField,
)

from .models import FoodsModel


class FoodsSerializer(ModelSerializer):

    class Meta:
        model = FoodsModel
        fields = ["name", "description"]


class FoodsReadSerializer(ModelSerializer):

    class Meta:
        model = FoodsModel
        fields = ["name", "description", "author"]
