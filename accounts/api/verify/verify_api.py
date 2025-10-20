from rest_framework.permissions import AllowAny
from rest_framework_simplejwt import views as jwt_views


class TokenVerifyApi(jwt_views.TokenVerifyView):
    permission_classes = [AllowAny]
