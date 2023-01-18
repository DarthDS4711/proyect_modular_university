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
    
    # función secundaria para realizar el calculo de la normalización
    def __compute_data_to_normalize(self, minimun, maximun, data_non_normalized):
        data_normalized = (data_non_normalized - minimun) / (maximun - minimun)
        return data_normalized
    
    # función secundaria que normaliza los datos de cada conjunto de datos
    def __normalize_data_to_predict(self, category_for_prediction, supplier_for_prediction):
        list_product_disc, list_product_disc2 = self.__get_products_with__discount()
        # minimos y máximos de los proveedores 
        minimun_id_supplier = Supplier.objects.get(id = 1).id
        maximun_id_supplier = Supplier.objects.last().id
        print(f'Proveedor    Minimo: {minimun_id_supplier}, Maximo: {maximun_id_supplier}')
        # minimos y máximos de los productos
        minimun_id_category = Category.objects.get(id = 1).id
        maximun_id_category = Category.objects.last().id
        print(f'Categoria    Minimo: {minimun_id_category}, Maximo: {maximun_id_category}')

        # normalizar los datos de la predicción
        category_for_prediction = self.__compute_data_to_normalize(minimun_id_category, maximun_id_category, category_for_prediction)
        supplier_for_prediction = self.__compute_data_to_normalize(minimun_id_supplier, maximun_id_supplier, supplier_for_prediction)

        # lista normalizadas
        list_normalized_class1_X1 = []
        list_normalized_class1_X2 = []
        list_normalized_class2_X1 = []
        list_normalized_class2_X2 = []

        # proceso de normalización de los datos
        for data in list_product_disc:
            x1 = data.category.id
            x2 = data.supplier_id.id
            # actualización de los valores 
            x1 = self.__compute_data_to_normalize(minimun_id_category, maximun_id_category, x1)
            x2 = self.__compute_data_to_normalize(minimun_id_supplier, maximun_id_supplier, x2)
            print(f'Class1    x1: {x1}, Maximo: {x2}')
            list_normalized_class1_X1.append(x1)
            list_normalized_class1_X2.append(x2)
        for data in list_product_disc2:
            x1 = data.category.id
            x2 = data.supplier_id.id
            # actualización de los valores 
            x1 = self.__compute_data_to_normalize(minimun_id_category, maximun_id_category, x1)
            x2 = self.__compute_data_to_normalize(minimun_id_supplier, maximun_id_supplier, x2)
            print(f'Class2    x1: {x1}, Maximo: {x2}')
            list_normalized_class2_X1.append(x1)
            list_normalized_class2_X2.append(x2)
        return list_normalized_class1_X1, list_normalized_class1_X2, list_normalized_class2_X1, list_normalized_class2_X2, category_for_prediction, supplier_for_prediction

    
    # funcion secundaria para obtener los productos con un descuento del 25%
    def __get_products_with__discount(self):
        list_product1 = []
        list_product_2 = []
        products_discount = Product.objects.filter(discount__lte=0.25, is_active=False)[:5]
        products_discount_50 = Product.objects.filter(discount__gt=0.25, discount__lt=0.5, is_active=False).order_by('-name') [:5]
        current_products = 0
        for product in products_discount:
            if current_products < 3:
                list_product1.append(product)
                current_products += 1
                print(f'category 1 {product.category.id}   supplier: {product.supplier_id.id}')
        current_products = 0
        for product in products_discount_50:
            if current_products < 3:
                list_product_2.append(product)
                current_products += 1
                print(f'category 2 {product.category.id}   supplier: {product.supplier_id.id}')
        return list_product1, list_product_2
    


    # función primaria para enviar los datos a la api IA
    def send_api_ia_products_to_learn(self, request : HttpRequest):
        data = {}
        if request.POST['category_selected'] != '' and request.POST['supplier_selected'] != '':
            category_for_prediction = int(request.POST['category_selected'])
            supplier_for_prediction =  int(request.POST['supplier_selected'])
            print(f'Category to predict: {category_for_prediction}  Supplier to predict: {supplier_for_prediction}')
            list_dataclass1_X1,list_dataclass1_X2,list_dataclass2_X1,list_dataclass2_X2, category_for_prediction, supplier_for_prediction = self.__normalize_data_to_predict(category_for_prediction, supplier_for_prediction)
        
            data_predict = [supplier_for_prediction, category_for_prediction]
            print(f'Category to predict: {category_for_prediction}  Supplier to predict: {supplier_for_prediction}')

            body = {
                "data_class1_X1" : list_dataclass1_X1,
                "data_class2_X1" : list_dataclass2_X1,
                "data_class1_X2" : list_dataclass1_X2,
                "data_class2_X2" : list_dataclass2_X2,
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
