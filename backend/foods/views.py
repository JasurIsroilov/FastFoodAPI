from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from rest_framework.response import Response

from .serializers import (
    FoodsSerializer,
    FoodsReadSerializer,
)
from .models import FoodsModel
from .permissions import (
    CanAddFood,
    CanUpdateFood,
    CanDeleteFood,
    CanGetMenu,
)
from users.permissions import HasJWTAccessToken


class CreateFoodAPIView(GenericAPIView):

    permission_classes = [HasJWTAccessToken, CanAddFood]
    serializer_class = FoodsSerializer

    def post(self, request):

        """
            View for creating a new food
        """

        _serializer = self.serializer_class(data=request.data)
        if _serializer.is_valid(raise_exception=True):
            _serializer.save(author=request.user)
            return Response({"message": "OK"}, status=201)
        return Response({"message": "Error"}, status=400)


class ListFoodsAPIView(ListAPIView):

    """
        View for getting a list of foods
    """

    queryset = FoodsModel.objects.all()
    serializer_class = FoodsReadSerializer
    permission_classes = [HasJWTAccessToken, CanGetMenu,]


class DeleteFoodAPIView(DestroyAPIView):

    """
        View for deleting a food
    """

    queryset = FoodsModel.objects.all()
    permission_classes = [HasJWTAccessToken, CanDeleteFood, ]


class UpdateFoodAPIView(UpdateAPIView):

    """
       View for updating the food
   """
    allowed_methods = ["patch"]
    queryset = FoodsModel.objects.all()
    serializer_class = FoodsSerializer
    permission_classes = [HasJWTAccessToken, CanUpdateFood, ]
