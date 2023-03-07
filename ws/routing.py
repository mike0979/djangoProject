from django.urls import path
from ws import consumers

websocket_urlpatterns = [
    path('room/', consumers.ChatConsumer.as_asgi()),
]