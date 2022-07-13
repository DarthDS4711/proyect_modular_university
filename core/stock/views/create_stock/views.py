from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from core.app_functions.data_replication import is_actual_state_autoreplication
from core.app_functions.rollback_data import rollback_data
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.product.models import Product
from core.stock.models import Stock
from core.stock.form.forms import StockForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from core.stock.models import Stock, StockProductSize
from django.db import transaction


# clase para crear los stock
class CreateStockView(EmergencyModeMixin, LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, CreateView):
    template_name = 'createStock.html'
    model = Stock
    success_url = reverse_lazy('stock:list_stock')
    form_class = StockForm
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_form(self):
        return super().get_form(self.form_class)

    # función que a traves de una transacción atómica guarda el stock nuevo
    # en las dos bases de datos, a manera de base de datos distribuida
    def create_new_stock(self, request):
        data = {}
        try:
            status_replication = is_actual_state_autoreplication()
            product = Product.objects.get(id=int(request.POST['product']))
            is_active = True if request.POST['is_activte'] == 'on' else False
            stock = Stock()
            stock.product = product
            stock.is_activte = is_active
            list_ammounts = []
            stock.save(force_insert=True)
            if status_replication:
                stock.save(using='mirror_database')
            stock.save(using="stock_product")
            sizes_product = product.size.all()
            for size in sizes_product:
                name_field = size.size_product.lower()
                ammount_size = int(request.POST[name_field])
                list_ammounts.append(ammount_size)
            number_ammounts = 0
            stock = Stock.objects.all().latest('id')
            for size in sizes_product:
                size_prod_size = StockProductSize()
                size_prod_size.size = size
                size_prod_size.stock = stock
                size_prod_size.amount = list_ammounts[number_ammounts]
                size_prod_size.save()
                size_prod_size.save(using="stock_product")
                if status_replication:
                    size_prod_size.save(using='mirror_database')
                number_ammounts += 1
            stock.amount = sum(list_ammounts)
            stock.save()
            stock.save(using="stock_product")
            if status_replication:
                stock.save(using='mirror_database')
        except Exception as e:
            data['error'] = str(e)
            print(data)
        return data

    def post(self, request, *args, **kwargs):
        data = {}
        match request.POST['action']:
            case 'obtain':
                id_product = int(request.POST['id_product'])
                product = Product.objects.get(id = id_product)
                sizes_product = product.size.all()
                data = []
                for size in sizes_product:
                    data.append(size.to_json()) 
            case 'register':
                with transaction.atomic():
                    data = self.create_new_stock(request)
                    if 'error' in data:
                        rollback_data(1)   
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Registrar Stock"
        context['list'] = self.success_url
        context['action'] = 'register' 
        context['btn'] = 'Registrar stock'
        context['color'] = self.get_number_color()
        return context