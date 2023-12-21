import os
import chat.routing

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hello_world.settings")

django_asgi_application = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(chat.routing.websocket_urlpatterns))
        ),
    }
)
