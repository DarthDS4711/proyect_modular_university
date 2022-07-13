from django.urls import reverse_lazy
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.product.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView


class ListSearchProductView(EmergencyModeMixin, LoginRequiredMixin, ObtainColorMixin, ListView):
    model = Product
    paginate_by = 2
    template_name = 'listSearchProduct.html'
    login_url = reverse_lazy('access:Login')


    def return_name(self):
        if 'name' in self.kwargs.keys():
            return self.kwargs['name']
        else:
            return self.request.GET['name']

    # método que nos retorna, según el caso, el orden del arreglo
    def return_data_order(self, option):
        name = self.return_name()
        match option:
            case 1:
                return Product.objects.filter(name__icontains=name).order_by('pvp')
            case 2:
                return Product.objects.filter(name__icontains=name).order_by('-pvp')
            case 3:
                return Product.objects.filter(name__icontains=name).order_by('name')
            case 4:
                return Product.objects.filter(name__icontains=name).order_by('-product_rating')
    
    def return_value_of_order(self):
        if 'order' in self.request.GET.keys():
            return int(self.request.GET['order'])
        return 1
    
    def get_queryset(self):
        type_of_order = self.return_value_of_order()
        data_set = self.return_data_order(type_of_order)
        return data_set
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Productos buscados'
        context['discount'] = True
        context['url'] = reverse_lazy('shop:list_search')
        context['name'] = self.return_name()
        context['color'] = self.get_number_color()
        context['order'] = self.return_value_of_order()
        return context