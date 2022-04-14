from urllib import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from core.product.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


class ListAllProductsView(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 3
    template_name = 'listAllProducts.html'
    login_url = reverse_lazy('access:Login')

    # método que nos retorna, según el caso, el orden del arreglo
    def return_data_order(self, option):
        match option:
            case 1:
                return Product.objects.all().order_by('pvp')
            case 2:
                return Product.objects.all().order_by('-pvp')
            case 3:
                return Product.objects.all().order_by('-name')
            case 4:
                return Product.objects.all().order_by('-product_rating')
    
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
        context["title"] = "Todos los productos"
        context["discount"] = False
        context['url'] = reverse_lazy('shop:list_all')
        return context

