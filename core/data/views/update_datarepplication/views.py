from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from core.data.models import DataReplication
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from django.db import transaction


class UpdateDataRepplicationView(EmergencyModeMixin, LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, TemplateView):
    template_name = 'update_view_datarep.html'
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    # sobrescritura del método post para el guardado de los datos
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            status_replication = True if request.POST['status'] == 'True' else False
            with transaction.atomic():
                data_replication = DataReplication.objects.get(id = 1)
                data_replication.autoreplication = status_replication
                data_replication.save()
                data_replication.save(using='mirror_database')
        except Exception as e:
            data['error'] = str(e)
        # regreso de la respuesta del servidor
        return JsonResponse(data, safe=False)
    
    # método que retorna el estado actual de la replicación de la base de datos
    def get_actual_replication_state(self):
        status = DataReplication.objects.filter(id = 1)
        if status.exists():
            return status[0].autoreplication
        status = DataReplication.objects.using('mirror_database').filter(id = 1)
        if status.exists():
            return status[0].autoreplication

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Autoreplicación datos aplicación"
        context['list'] = reverse_lazy('app_views:dashboard_admin')
        context['action'] = 'update' 
        context['datareplication'] = self.get_actual_replication_state()
        context['color'] = self.get_number_color()
        return context