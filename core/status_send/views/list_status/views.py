from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.status_send.models import StatusSend


class ListStatusView(LoginRequiredMixin, ValidateSessionGroupMixin,ObtainColorMixin, ListView):
    model = StatusSend
    paginate_by = 4
    template_name = 'listStatusSend.html'
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de estatus de envio'
        context['create_status'] = reverse_lazy('status_send:register')
        context['color'] = self.get_number_color()
        return context