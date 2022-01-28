from dataclasses import fields
from pyexpat import model
from django.views.generic.edit import CreateView
from core.status_send.forms.form_register_status import StatusSendForm
from core.status_send.models import StatusSend


class RegisterStatusView(CreateView):
    model = StatusSend
    template_name = 'registerStatusSend.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_form(self):
        return super().get_form(StatusSendForm)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registrar Estados de envio"
        context["image"] = "img/send.png"
        return context