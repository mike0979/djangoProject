from django.urls import path
from fastApp import views

urlpatterns = [
    path('login', views.login),
    path('users', views.user_operate),
]