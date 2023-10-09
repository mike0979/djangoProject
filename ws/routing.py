from django.urls import path
from ws import consumers

websocket_urlpatterns = [
    path('api/v1/message/<str:code>', consumers.ChatConsumer.as_asgi()),
]