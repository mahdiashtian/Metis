from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

websocket_urlpatterns = [
]

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(websocket_urlpatterns),
    }
)
