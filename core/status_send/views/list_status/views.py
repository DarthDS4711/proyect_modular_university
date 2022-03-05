from django.urls import reverse_lazy
from django.views.generic.list import ListView

from core.status_send.models import StatusSend


class ListStatusView(ListView):
    model = StatusSend
    paginate_by = 4
    template_name = 'listStatusSend.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de estatus de envio'
        context['create_status'] = reverse_lazy('status_send:register')
        return context