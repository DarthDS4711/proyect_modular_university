from django.urls import reverse_lazy
from django.views.generic.list import ListView
from core.classes.obtain_color import ObtainColorMixin
from core.product.models import Category, Product
from django.contrib.auth.mixins import LoginRequiredMixin


class ListProductsShopView(LoginRequiredMixin, ObtainColorMixin, ListView):
    template_name = 'listProductsShop.html'
    model = Product
    paginate_by = 10
    login_url = reverse_lazy('access:Login')
    
    def get_queryset(self):
        # sobreescritura del método get_query_set para obtener los productos relacionados a la categoría
        return Product.objects.filter(category=self.kwargs['id_category'])

    def get_context_data(self, **kwargs):
        # obtención del nombre de la categoría
        category = Category.objects.filter(id=self.kwargs['id_category'])[0]
        context = super().get_context_data(**kwargs) 
        context["title"] = category
        context["discount"] = False
        context['color'] = self.get_number_color()
        return context