from uuid import uuid4
from datetime import datetime

from django.db import models
from django.conf import settings

from foods.models import FoodsModel


class OrdersModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    status = models.CharField(max_length=20, null=False)
    distance = models.FloatField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_at = models.DateTimeField()

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="author")
    waiter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="waiter", null=True)
    food = models.ForeignKey(FoodsModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "orders"
