import django


from django.views.generic.list import ListView
from core.product.models import Product


class ListAllProductsView(ListView):
    model = Product
    paginate_by = 10
    template_name = 'listAllProducts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Todos los productos"
        context["discount"] = False
        return context

