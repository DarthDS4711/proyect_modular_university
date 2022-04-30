from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.stock.models import Stock, StockProductSize
from core.stock.form.forms import StockEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction


# clase para crear los stock
class UpdateStockView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, UpdateView):
    template_name = 'editStock.html'
    model = Stock
    success_url = reverse_lazy('stock:list_stock')
    form_class = StockEditForm
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def get_form(self):
        return super().get_form(StockEditForm)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            print(request.POST)
            if request.POST['action'] == 'update':
                # obtención del stock actual
                stock = self.object
                product = stock.product
                is_active = True if request.POST['is_activte'] == 'on' else False
                with transaction.atomic():
                    stock.is_activte = is_active
                    list_ammounts = []
                    sizes_product = product.size.all()
                    stock_sizes_product = StockProductSize.objects.filter(stock = stock)
                    for size in sizes_product:
                        name_field = size.size_product
                        ammount_size = int(request.POST[name_field])
                        list_ammounts.append(ammount_size)      
                    number_ammounts = 0
                    for stock_size in stock_sizes_product:
                        stock_size.amount = list_ammounts[number_ammounts]
                        stock_size.save()
                        number_ammounts += 1
                    stock.amount = sum(list_ammounts)
                    stock.save()
        except Exception as e:
            data['error'] = str(e)
        # regreso de la respuesta del servidor
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Stock"
        context['list'] = self.success_url
        context['action'] = 'update' 
        context['btn'] = 'Editar stock'
        context['color'] = self.get_number_color()
        context['stock_size'] = StockProductSize.objects.filter(stock = self.object)
        print(context['stock_size'])
        return context