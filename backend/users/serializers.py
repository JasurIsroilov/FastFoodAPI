from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    ChoiceField,
)
from .models import CustomUserModel


class RegisterUserSerializer(ModelSerializer):
    password = CharField(write_only=True, required=True)
    role = ChoiceField(choices=["user"])

    extra_kwargs = {
        'role': {'required': True},
        'first_name': {'required': True},
        'last_name': {'required': True}
    }

    class Meta:
        model = CustomUserModel
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'role']

    def create(self, validated_data):
        user = super(RegisterUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
