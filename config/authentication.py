import jwt
from django.conf import settings
from users import models as user_models
from rest_framework import authentication


class JwtAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.META.get("HTTP_AUTHORIZATION")
            if token is None:
                return None
            _, jwt_token = token.split(" ")
            decoded = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=["HS256"])
            pk = decoded.get("pk")
            user = user_models.User.objects.get(pk=pk)
            return (user, None)
        except (ValueError, jwt.exceptions.DecodeError, user_models.User.DoesNotExist):
            return None
