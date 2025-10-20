from rest_framework.permissions import AllowAny
from rest_framework_simplejwt import views as jwt_views


class TokenRefreshApi(jwt_views.TokenRefreshView):
    permission_classes = [AllowAny]
