from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.sale.models import Sale


class ListInvoiceView(LoginRequiredMixin, ObtainColorMixin, ListView):
    model = Sale
    paginate_by = 20
    template_name = 'list_invoices.html'
    login_url = reverse_lazy('access:Login')

    def get_queryset(self):
        queryset = Sale.objects.filter(user = self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Listado de facturas"
        context["image"] = 'img/list.png'
        context['color'] = self.get_number_color()
        return context