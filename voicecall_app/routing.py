

# call_app/routing.py

from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/call/(?P<pin_code>\w+)/$', consumers.ChatConsumer.as_asgi()),
]



