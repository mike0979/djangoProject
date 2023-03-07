from django.urls import path
from fastApp import views

urlpatterns = [
    path('get_method_params/', views.get_method_params),
    path('login/', views.login),
]