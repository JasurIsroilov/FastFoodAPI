from rest_framework.generics import CreateAPIView

from .serializers import RegisterUserSerializer
from .models import CustomUserModel


class RegisterAPIView(CreateAPIView):
    queryset = CustomUserModel.objects.all()
    serializer_class = RegisterUserSerializer
