from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.purchase.models import Purchase


class ListInvoiceSystemView(EmergencyModeMixin, LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, ListView):
    model = Purchase
    paginate_by = 50
    template_name = 'list_invoices_system.html'
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def __obtain_range_date(self):
        initial_date = self.request.GET['initial_date'] if 'initial_date' in self.request.GET.keys(
        ) else ''
        final_date = self.request.GET['final_date'] if 'final_date' in self.request.GET.keys(
        ) else ''
        return initial_date, final_date

    def get_queryset(self):
        queryset = None
        initial_date, final_date = self.__obtain_range_date()
        if initial_date != '' and final_date != '':
            queryset = Purchase.objects.filter(date_purchase__range=(initial_date, final_date))
        else:
            queryset = Purchase.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Listado de facturas del sistema"
        context["image"] = 'img/list.png'
        context['color'] = self.get_number_color()
        return context