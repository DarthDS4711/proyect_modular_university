from django.http import JsonResponse
from django.urls import reverse_lazy
from core.app_functions.rollback_data import rollback_data
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.status_send.forms.form_register_status import StatusSendForm
from core.status_send.models import StatusSend
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction


class UpdateStatusSendView(EmergencyModeMixin, LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, UpdateView):
    from_class = StatusSendForm
    template_name = 'editStatusSend.html'
    model = StatusSend
    success_url = reverse_lazy('status_send:list')
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def get_form(self):
        return super().get_form(StatusSendForm)
    
    def post(self, request, *args, **kwargs):
        data = {}
        with transaction.atomic():
            form = self.get_form()
            data = form.save()
            if 'error' in data:
                rollback_data(3)
        # regreso de la respuesta del servidor
        return JsonResponse(data)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar Estado"
        context["image"] = "img/send.png"
        context['list'] = reverse_lazy('status_send:list')
        context['action'] = 'update'
        context['btn'] = 'Actualizar'
        context['color'] = self.get_number_color()
        return context

