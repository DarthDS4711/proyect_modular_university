from django.http import JsonResponse, HttpRequest
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from core.app_functions.rollback_data import rollback_data
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.product.forms.category.forms import CategoryForm
from core.product.forms.product.forms import ProductForm
from core.product.forms.size.form import SizeForm
from core.product.models import Category, Product
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from django.db import transaction
from django.db.models import Q
from core.supplier.models import Supplier
import requests



class RegisterProductView(EmergencyModeMixin, LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, CreateView):
    template_name = "registerProduct.html"
    model = Product
    success_url = reverse_lazy('product:list_product')
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    
    # funcion secundaria para obtener los productos con un descuento del 25%
    def __get_products_with__discount(self):
        list_product1 = []
        list_product_2 = []
        list_product_3 = []
        products_discount = Product.objects.filter(discount=0.25, is_active=False)[:5]
        products_discount_50 = Product.objects.filter(discount=0.5, is_active=False).order_by('-name') [:5]
        products_discount_75 = Product.objects.filter(discount=0.75, is_active=False).order_by('-id')[:5]
        current_products = 0
        for product in products_discount:
            if current_products < 2:
                list_product1.append(product)
                current_products += 1
                print(f'category 1 {product.category.id}   supplier: {product.supplier_id.id}')

        current_products = 0
        for product in products_discount_50:
            if current_products < 2:
                list_product_2.append(product)
                current_products += 1
                print(f'category 2 {product.category.id}   supplier: {product.supplier_id.id}')
        
        current_products = 0
        for product in products_discount_75:
            if current_products < 2:
                list_product_3.append(product)
                current_products += 1
                print(f'category 3 {product.category.id}   supplier: {product.supplier_id.id}')
        return list_product1, list_product_2, list_product_3
    


    # función primaria para enviar los datos a la api IA
    def send_api_ia_products_to_learn(self, request : HttpRequest):
        data = {}
        if request.POST['category_selected'] != '' and request.POST['supplier_selected'] != '':
            list_25_percent, list_50_percent, list_75_percent = self.__get_products_with__discount()
            list_dataclass1_X1 = []
            list_dataclass2_X1 = []
            list_dataclass3_X1 = []
            list_dataclass1_X2 = []
            list_dataclass2_X2 = []
            list_dataclass3_X2 = []
            for data in list_25_percent:
                list_dataclass1_X1.append(data.category.id)
                list_dataclass1_X2.append(data.supplier_id.id)
            
            for data in list_50_percent:
                list_dataclass2_X1.append(data.category.id)
                list_dataclass2_X2.append(data.supplier_id.id)
            
            for data in list_75_percent:
                list_dataclass3_X1.append(data.category.id)
                list_dataclass3_X2.append(data.supplier_id.id)
            data_predict = [int(request.POST['category_selected']), int(request.POST['supplier_selected'])]

            body = {
                "data_class1_X1" : list_dataclass1_X1,
                "data_class2_X1" : list_dataclass2_X1,
                "data_class3_X1" : list_dataclass3_X1,
                "data_class1_X2" : list_dataclass1_X2,
                "data_class2_X2" : list_dataclass2_X2,
                "data_class3_X2" : list_dataclass3_X2,
                "data_predict" : data_predict
            }   
            url = "http://localhost:8080/products/prediction-discount/"
            response = requests.get(url, json = body)
            data = response.json()
        else:
            data['error'] = 'No hay datos por enviar'
        return data


    # sobrescritura del método post para el guardado de los datos
    def post(self, request, *args, **kwargs):
        data = {}
        print(request.POST)
        match request.POST['action']:
            case 'autocomplete':
                data = []
                suppliers = Supplier.objects.filter(
                    Q(is_active = True) & 
                    (Q(first_names__icontains = request.POST['term']) | 
                    Q(last_names__icontains = request.POST['term'])))[0:10]
                print(suppliers)

                for supplier in suppliers:
                    item = supplier.to_json_faster()
                    item['text'] = f'Proveedor: {supplier.get_name()}'
                    data.append(item)
            case 'register':
                with transaction.atomic():
                    form = self.get_form()
                    data = form.save()
                    if 'error' in data:
                        rollback_data(1)
            case 'prediction_discount':
                data = self.send_api_ia_products_to_learn(request)

        # regreso de la respuesta del servidor
        return JsonResponse(data, safe=False)


    def get_form(self):
        return super().get_form(ProductForm)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registrar producto"
        context['list'] = self.success_url
        context['action'] = 'register' 
        context['btn'] = 'Registrar producto'
        context['color'] = self.get_number_color()
        return context


class RegisterCategoryView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, CreateView):
    template_name = 'registerCategory.html'
    model = Category
    success_url = reverse_lazy('product:list_cat')
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # sobrescritura del método post para el guardado de los datos
    def post(self, request, *args, **kwargs):
        data = {}
        try:
           with transaction.atomic():
                form = self.get_form()
                data = form.save()
                if 'error' in data:
                    rollback_data(1)
        except Exception as e:
            data['error'] = str(e)
        # regreso de la respuesta del servidor
        return JsonResponse(data, safe=False)


    def get_form(self):
        return super().get_form(CategoryForm)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registrar Categoría"
        context['list'] = self.success_url
        context['action'] = 'register' 
        context['btn'] = 'Registrar categoria'
        context['color'] = self.get_number_color()
        return context


class RegisterSizeView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, CreateView):
    template_name = 'registerSize.html'
    success_url = reverse_lazy('product:list_sizes')
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def get_form(self):
        return super().get_form(SizeForm)
    

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            with transaction.atomic():
                form = self.get_form()
                data = form.save()
                if 'error' in data:
                    rollback_data(1)
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registrar Talla"
        context['list'] = self.success_url
        context['action'] = 'register' 
        context['btn'] = 'Registrar talla'
        context['color'] = self.get_number_color()
        return context
