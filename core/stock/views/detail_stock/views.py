from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.stock.models import Stock


class DetailStockProduct(LoginRequiredMixin, DetailView):
    template_name = 'detailStock.html'
    model = Stock
    login_url = reverse_lazy('access:Login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Stock Producto"
        return context