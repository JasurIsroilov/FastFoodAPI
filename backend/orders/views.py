from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.response import Response

from users.permissions import HasJWTAccessToken
from .serializers import (
    OrderCreateSerializer,
    OrderAcceptSerializer,
    OrderSendSerializer,
    OrderRetrieveSerializer,
)
from .permissions import (
    CanOrder,
    CanAcceptOrder,
    CanSendOrder,
    CanViewOrder,
)
from .services import (
    save_ordered_food,
    update_order_status,
)
from .models import OrdersModel


class OrderCreateAPIView(GenericAPIView):

    serializer_class = OrderCreateSerializer
    permission_classes = [HasJWTAccessToken, CanOrder]

    def post(self, request):
        _serializer = self.serializer_class(data=request.data)
        _serializer.is_valid(raise_exception=True)
        save_ordered_food(request)
        return Response({"message": "OK"}, status=201)


class OrderAcceptAPIView(GenericAPIView):

    permission_classes = [HasJWTAccessToken, CanAcceptOrder]
    serializer_class = OrderAcceptSerializer

    def post(self, request):
        _serializer = self.serializer_class(data=request.data)
        _serializer.is_valid(raise_exception=True)
        update_order_status(request)
        return Response(data={"message": "OK"}, status=204)


class OrderSendAPIView(GenericAPIView):

    permission_classes = [HasJWTAccessToken, CanSendOrder]
    serializer_class = OrderSendSerializer

    def post(self, request):
        _serializer = self.serializer_class(data=request.data)
        _serializer.is_valid(raise_exception=True)
        update_order_status(request)
        return Response(data={"message": "OK"}, status=204)


class OrdersListAPIView(ListAPIView):
    queryset = OrdersModel.objects.all()
    permission_classes = [HasJWTAccessToken, CanViewOrder]
    serializer_class = OrderRetrieveSerializer


class OrderRetrieveAPIView(RetrieveAPIView):
    queryset = OrdersModel.objects.all()
    permission_classes = [HasJWTAccessToken, CanViewOrder]
    serializer_class = OrderRetrieveSerializer
