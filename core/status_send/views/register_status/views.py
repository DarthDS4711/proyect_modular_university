from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from core.app_functions.rollback_data import rollback_data
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.status_send.forms.form_register_status import StatusSendForm
from core.status_send.models import StatusSend
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction



class RegisterStatusView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, CreateView):
    model = StatusSend
    template_name = 'registerStatusSend.html'
    success_url = reverse_lazy('status_send:list')
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_form(self):
        return super().get_form(StatusSendForm)
    
    # sobrescritura del método post para el guardado de los datos
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
        context["title"] = "Registrar Estados de envio"
        context["image"] = "img/send.png"
        context['list'] = reverse_lazy('status_send:list')
        context['action'] = 'register'
        context['btn'] = 'Registrar'
        context['color'] = self.get_number_color()
        return context