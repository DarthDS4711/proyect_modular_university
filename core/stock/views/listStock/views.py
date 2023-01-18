from django.urls import reverse_lazy
from django.views.generic.list import ListView
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.stock.models import Stock
from django.contrib.auth.mixins import LoginRequiredMixin


class ListStockView(EmergencyModeMixin, LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, ListView):
    model = Stock
    template_name = 'listStock.html'
    paginate_by = 20
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def return_name(self):
        if 'name' in self.kwargs.keys():
            return self.kwargs['name']
        elif 'name' in self.request.GET:
            return self.request.GET['name']
        else:
            return ''
    
    def return_status(self):
        if 'status' in self.kwargs.keys():
            return self.kwargs['status']
        elif 'status' in self.request.GET:
            return self.request.GET['status']
        else:
            return ''
    
    def return_queryset_with_filter(self, stocks, status):
        match status:
            case '':
                return stocks
            case '1':
                return stocks
            case '2':
                return stocks.filter(is_activte=True)
            case '3':
                return stocks.filter(is_activte=False)
    
    def get_queryset(self):
        name = self.return_name()
        status = self.return_status()
        if name != '':
            stocks = Stock.objects.filter(product__name__icontains=self.return_name())
            return self.return_queryset_with_filter(stocks, status)
        else:
            stocks = Stock.objects.all()
            return self.return_queryset_with_filter(stocks, status)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de stock'
        context["image"] = 'img/list.png'
        context['create'] = reverse_lazy('stock:create_stock')
        context['color'] = self.get_number_color()
        context['url'] = reverse_lazy('stock:list_stock')
        context['name'] = self.return_name()
        return context