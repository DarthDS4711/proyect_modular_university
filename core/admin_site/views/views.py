from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.admin_site.models import EmergencyModeApp
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from django.db import transaction


class UpdateEmergencyAppView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, TemplateView):
    template_name = 'modify_emergency.html'
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    # sobrescritura del método post para el guardado de los datos
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            status_emergency = True if request.POST['status'] == 'activated' else False
            with transaction.atomic():
                emergency_mode = EmergencyModeApp.objects.using('status_application').get(id = 1)
                emergency_mode.is_emergency_actived = status_emergency
                emergency_mode.save(using='status_application')
        except Exception as e:
            data['error'] = str(e)
        # regreso de la respuesta del servidor
        return JsonResponse(data, safe=False)
    
    # método que retorna el estado actual de la replicación de la base de datos
    def get_actual_emergency_mode(self):
        status = EmergencyModeApp.objects.using('status_application').filter(id = 1)
        if status.exists():
            return status[0].is_emergency_actived

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Modo de emergencia de la aplicación"
        context['list'] = reverse_lazy('app_views:dashboard_admin')
        context['action'] = 'update' 
        context['emergency_mode'] = self.get_actual_emergency_mode()
        context['color'] = self.get_number_color()
        return context