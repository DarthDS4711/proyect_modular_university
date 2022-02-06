from django.views.generic.base import TemplateView


class DetailStockProduct(TemplateView):
    template_name = 'detailStock.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Stock Producto"
        return context