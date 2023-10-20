from django.urls import path, re_path
from opm import views

urlpatterns = [
    re_path(r'^operational_messages(?:/(?P<id>\d+))?$', views.opm_operate),
    path('operational_messages/<int:opm_id>/action', views.opm_publish),
    path('opm_level', views.get_opm_level),
    path('opm_template', views.opm_template_operate),
    path('opm_template/<int:id>', views.get_opm_template),
]