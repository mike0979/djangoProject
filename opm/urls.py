from django.urls import path
from opm import views

urlpatterns = [
    path('operational_messages/', views.opm_operate),
    path('operational_messages/<int:opm_id>/', views.get_opm_detail),
    path('operational_messages/<int:opm_id>/action', views.opm_publish),
    # path('operational_messages/<int:opm_id>/reply', ),
]