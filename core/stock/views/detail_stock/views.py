from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from core.stock.models import Stock


class DetailStockProduct(LoginRequiredMixin, ObtainColorMixin, DetailView):
    template_name = 'detailStock.html'
    model = Stock
    login_url = reverse_lazy('access:Login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Stock Producto"
        context['color'] = self.get_number_color()
        return context