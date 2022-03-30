from django.views.generic.list import ListView
from core.product.models import Category, Product


class ListProductsShopView(ListView):
    template_name = 'listProductsShop.html'
    model = Product
    paginate_by = 10
    
    def get_queryset(self):
        # sobreescritura del método get_query_set para obtener los productos relacionados a la categoría
        return Product.objects.filter(category=self.kwargs['id_category'])

    def get_context_data(self, **kwargs):
        # obtención del nombre de la categoría
        category = Category.objects.filter(id=self.kwargs['id_category'])[0]
        context = super().get_context_data(**kwargs) 
        context["title"] = category
        return context