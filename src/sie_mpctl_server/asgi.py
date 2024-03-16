import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sie_mpctl_server.settings')
asgi_application: any = get_asgi_application()

import core.routing # noqa

application: ProtocolTypeRouter = ProtocolTypeRouter({
    'http': asgi_application,
    'websocket': AuthMiddlewareStack(
        URLRouter(
            core.routing.urlpatterns
        )
    )
})
