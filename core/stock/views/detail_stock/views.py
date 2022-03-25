from django.views.generic.detail import DetailView

from core.stock.models import Stock


class DetailStockProduct(DetailView):
    template_name = 'detailStock.html'
    model = Stock

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Stock Producto"
        return context