from django.urls import path, re_path
from location import views

urlpatterns = [
    re_path(r'^stations(?:/(?P<id>\d+))?$', views.station_operate),
    re_path(r'^lines(?:/(?P<id>\d+))?$', views.line_operate),
    path('locations', views.get_locations),
    path('location_types', views.get_location_types)
]