from django.urls import reverse_lazy
from django.views.generic.list import ListView
from core.product.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin


class ListDiscountProductView(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 10
    template_name = 'listDiscountProd.html'
    login_url = reverse_lazy('access:Login')

    def get_queryset(self):
        # con __gt obtenemos todos los productos cuyo descuento existe 
        return Product.objects.filter(discount__gt=0.1)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Mejores descuentos'
        context['discount'] = True
        return context