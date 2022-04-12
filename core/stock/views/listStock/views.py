from django.urls import reverse_lazy
from django.views.generic.list import ListView
from core.stock.models import Stock
from django.contrib.auth.mixins import LoginRequiredMixin


class ListStockView(LoginRequiredMixin, ListView):
    model = Stock
    template_name = 'listStock.html'
    paginate_by = 6
    login_url = reverse_lazy('access:Login')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de stock'
        context["image"] = 'img/list.png'
        context['create'] = reverse_lazy('stock:create_stock')
        return context