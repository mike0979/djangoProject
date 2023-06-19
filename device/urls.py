from django.urls import path
from device import views

urlpatterns = [
    path('devices', views.device_operate),
    path('devices/', views.get_devices),
    path('device/<int:device_id>/', views.get_device_detail),
    path('device_types/', views.get_device_types),
]