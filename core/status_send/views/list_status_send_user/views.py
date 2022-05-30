from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.status_send.models import StatusSendSale


class ListStatusUserAdminSendView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, ListView):
    model = StatusSendSale
    paginate_by = 25
    template_name = 'list_status_send_store.html'
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de estatus de envio para usuarios'
        context['color'] = self.get_number_color()
        return context