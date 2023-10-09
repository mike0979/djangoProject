from django.urls import path, re_path
from device import views

urlpatterns = [
    re_path(r'^devices(?:/(?P<id>\d+))?$', views.device_operate),
    path('device_types', views.get_device_types),
]