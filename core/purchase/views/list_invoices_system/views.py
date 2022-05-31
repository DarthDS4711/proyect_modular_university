from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.purchase.models import Purchase


class ListInvoiceSystemView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, ListView):
    model = Purchase
    paginate_by = 50
    template_name = 'list_invoices_system.html'
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Listado de facturas del sistema"
        context["image"] = 'img/list.png'
        context['color'] = self.get_number_color()
        return context