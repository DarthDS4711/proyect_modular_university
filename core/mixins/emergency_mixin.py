from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from core.admin_site.models import EmergencyModeApp


class EmergencyModeMixin:
    def dispatch(self, request, *args, **kwargs):
        emergency_app = EmergencyModeApp.objects.using('status_application').filter(id = 1)
        if emergency_app.exists() and emergency_app[0].is_emergency_actived == False:
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(reverse_lazy('app_views:error_page'))
