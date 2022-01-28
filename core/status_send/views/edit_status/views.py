from django.views.generic.base import TemplateView

from core.status_send.forms.form_register_status import StatusSendForm
from core.status_send.models import StatusSend


'''
class UpdateStatusSendView(UpdateView):
    from_class = StatusSendForm
    model = StatusSend
    template_name = 'editStatusSend.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar Estado"
        context["image"] = "img/send.png"
        return context
'''

class UpdateStatusSendView(TemplateView):
    template_name = 'editStatusSend.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar Estado de Envio"
        context["image"] = "img/send.png"
        return context