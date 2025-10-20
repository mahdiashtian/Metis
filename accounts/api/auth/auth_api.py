from rest_framework.permissions import AllowAny
from rest_framework_simplejwt import views as jwt_views


class TokenObtainPairView(jwt_views.TokenObtainPairView):
    permission_classes = [AllowAny]
