from django.urls import reverse_lazy
from django.views.generic.list import ListView
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.stock.models import Stock
from django.contrib.auth.mixins import LoginRequiredMixin


class ListStockView(EmergencyModeMixin, LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, ListView):
    model = Stock
    template_name = 'listStock.html'
    paginate_by = 20
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de stock'
        context["image"] = 'img/list.png'
        context['create'] = reverse_lazy('stock:create_stock')
        context['color'] = self.get_number_color()
        return context