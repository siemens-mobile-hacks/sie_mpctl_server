from django.urls import re_path
from core.consumers import DataConsumer

urlpatterns: list = [
    re_path(r'ws/data/$', DataConsumer.as_asgi()),
]
