from django.urls import path
from location import views

urlpatterns = [
    path('stations', views.station_operate),
    path('lines', views.line_operate),
    path('locations', views.get_locations),
    path('location_types', views.get_location_types)
]