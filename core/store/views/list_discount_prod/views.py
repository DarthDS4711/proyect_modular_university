from django.views.generic.list import ListView
from core.product.models import Product


class ListDiscountProductView(ListView):
    model = Product
    paginate_by = 10
    template_name = 'listDiscountProd.html'

    def get_queryset(self):
        # con __gt obtenemos todos los productos cuyo descuento existe 
        return Product.objects.filter(discount__gt=0.1)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Mejores descuentos'
        context['discount'] = True
        return context