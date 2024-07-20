from rest_framework.permissions import BasePermission
from rest_framework.exceptions import ValidationError


class HasJWTAccessToken(BasePermission):
    def has_permission(self, request, view):
        authorization = request.headers.get("Authorization")
        if not authorization:
            raise ValidationError(detail="No token", code=401)

        auth: list = authorization.split(" ")
        if len(auth) != 2:
            raise ValidationError(detail="Incorrect token", code=401)
        if auth[0] != "Bearer":
            raise ValidationError(detail="Token must be Bearer", code=401)
        if not request.user:
            return False
        return True
