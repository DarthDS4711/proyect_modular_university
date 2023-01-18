
from django.urls import path

from core.admin_site.views.views import UpdateEmergencyAppView


app_name='admin_site'
urlpatterns = [
    path('update/emergency_state/', UpdateEmergencyAppView.as_view(), name='update_emergency_app')
]