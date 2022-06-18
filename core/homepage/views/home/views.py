from itertools import product
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from core.classes.obtain_color import ObtainColorMixin
from core.product.models import Product

# template view for the main page
class HomepageView(TemplateView, ObtainColorMixin):
    template_name = 'index.html'

    # method that return best products for the shop
    def best_ranking_products(self):
        best_ranking = Product.objects.filter(product_rating__gt = 3.0).order_by('-product_rating')
        return best_ranking

    def get_context_data(self, **kwargs):
        products = self.best_ranking_products()
        context = super().get_context_data(**kwargs)
        context["title"] = "Shop IA online"
        context['signin'] = reverse_lazy('access:signin')
        context['best_products'] = products[1:]
        context['best_product'] = products[0]
        context['color'] = self.get_number_color()
        return context
