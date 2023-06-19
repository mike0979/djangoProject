from django.urls import path
from fileHandler import views

urlpatterns = [
    path('upload', views.upload),
    path('download/<str:file_name>', views.download),
    path('resource', views.upload_resource)# temporary function,it will be delete later
]