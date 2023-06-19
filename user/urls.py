from django.urls import path
from user import views

urlpatterns = [
    path('login', views.login),
    path('users', views.user_operate),
    path('logout', views.logout),
]