from django.urls import path, re_path
from user import views

urlpatterns = [
    path('login', views.login),
    path('users', views.user_operate),
    path('logout', views.logout),
    path('roles', views.role_operate),
    path('pwd/<int:user_id>', views.change_password),
    re_path(r'^roles(?:/(?P<id>\d+))?$', views.role_operate),
    path('functions', views.get_functions),
]