from django.urls import reverse_lazy
from django.views.generic.list import ListView
from core.classes.obtain_color import ObtainColorMixin
from core.product.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin


class ListDiscountProductView(LoginRequiredMixin, ObtainColorMixin, ListView):
    model = Product
    paginate_by = 5
    template_name = 'listDiscountProd.html'
    login_url = reverse_lazy('access:Login')

    # método que nos retorna, según el caso, el orden del arreglo
    def return_data_order(self, option):
        match option:
            case 1:
                return Product.objects.filter(discount__gt=0.1).order_by('pvp')
            case 2:
                return Product.objects.filter(discount__gt=0.1).order_by('-pvp')
            case 3:
                return Product.objects.filter(discount__gt=0.1).order_by('-name')
            case 4:
                return Product.objects.filter(discount__gt=0.1).order_by('-product_rating')
    
    def return_value_of_order(self):
        if 'order' in self.request.GET.keys():
            return int(self.request.GET['order'])
        else:
            return 1
    
    def get_queryset(self):
        type_of_order = self.return_value_of_order()
        data_set = self.return_data_order(type_of_order)
        return data_set

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Mejores descuentos'
        context['discount'] = True
        context['url'] = reverse_lazy('shop:list_discount')
        context['color'] = self.get_number_color()
        context['order'] = self.return_value_of_order()
        return context