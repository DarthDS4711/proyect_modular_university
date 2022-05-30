from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from core.status_send.models import StatusSendSale


class ListStatusUserSendView(LoginRequiredMixin, ObtainColorMixin, ListView):
    model = StatusSendSale
    paginate_by = 10
    template_name = 'list_status_send_user.html'
    login_url = reverse_lazy('access:Login')

    def get_queryset(self):
        query_set = StatusSendSale.objects.filter(sale__user = self.request.user)
        return query_set

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Estado de envio de las facturas'
        context['color'] = self.get_number_color()
        return context