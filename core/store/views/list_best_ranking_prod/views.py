from django.views.generic.list import ListView
from core.product.models import Product


class ListBestProductsView(ListView):
    model = Product 
    paginate_by = 10
    template_name = 'listBestRankingProd.html'

    def get_queryset(self):
        # filtraremos todos aquellos productos que su rating sea mayor de tres estrellas
        return Product.objects.filter(product_rating__gt=3)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Mejores productos"
        context["discount"] = False
        return context