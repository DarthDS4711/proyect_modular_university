from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from core.app_functions.data_replication import is_actual_state_autoreplication
from core.app_functions.rollback_data import rollback_data
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.product.forms.category.forms import CategoryForm
from core.product.forms.product.forms import ProductForm
from core.product.forms.size.form import SizeForm
from core.product.models import Category, Product, Size
from django.contrib.auth.mixins import LoginRequiredMixin
from core.stock.models import Stock, StockProductSize
from django.db import transaction


class UpdateProductView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, UpdateView):
    from_class = ProductForm
    template_name = 'editProduct.html'
    model = Product
    success_url = reverse_lazy('product:list_product')
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def get_form(self):
        return super().get_form(ProductForm)

    def return_sizes_product(self, stock_product_size):
        list_sizes = []
        for stock_size in stock_product_size:
            list_sizes.append(stock_size.size.id)
        return list_sizes
    
    def make_the_transaction_sizes_stock(self, old_product_sizes):
        # procedimiento para actualizar el detail stock
        # del producto editado
        data = {}
        try:
            product = Product.objects.get(id = self.object.id)
            stock_product = Stock.objects.get(product = product)
            detail_stock_product = StockProductSize.objects.filter(stock = stock_product)
            sizes_stock_product = self.return_sizes_product(detail_stock_product)
            sizes_product = product.size.exclude(id__in=sizes_stock_product)
            print(sizes_product)
            for size in sizes_product:
                new_stock_size = StockProductSize()
                new_stock_size.stock = stock_product
                new_stock_size.size = size
                new_stock_size.save()
                new_stock_size.save(using='stock_product')
                if is_actual_state_autoreplication():
                    new_stock_size.save(using='mirror_database')
            # se vuelven a utilizar las mismas variables para ver cuales 
            # tallas ya no se encuentran en el producto
            sizes_product = product.size.all()
            detail_stock_product = StockProductSize.objects.filter(
                stock = stock_product).exclude(size__in = sizes_product)
            for size_del in detail_stock_product:
                id_stock_size = size_del.id
                size_del.delete()
                StockProductSize.objects.using('stock_product').get(
                    id = id_stock_size).delete(using='stock_product')
                if is_actual_state_autoreplication():
                    StockProductSize.objects.using('mirror_database').get(
                    id = id_stock_size).delete(using='mirror_database')
            # recalculo del ammount stock
            stock_product.calculate_amount()
            stock_product.save()
            stock_product.save(using='stock_product')
            stock_product.save(using='mirror_database')
        except Exception as e:
            data['error'] = str(e)
        return data
    
    def post(self, request, *args, **kwargs):
        data = {}
        old_product_sizes = Product.objects.get(id = self.object.id).size.all()
        with transaction.atomic():
            form = self.get_form()
            data = form.save()
            if 'error' in data:
                rollback_data(1)
        with transaction.atomic():
            data = self.make_the_transaction_sizes_stock(old_product_sizes)
            if 'error' in data:
                rollback_data(1)
    
        return JsonResponse(data)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar producto"
        context["image"] = "img/product.png"
        context['list'] = self.success_url
        context['action'] = 'update'
        context['btn'] = 'Actualizar'
        context['color'] = self.get_number_color()
        return context


class EditSizeView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, UpdateView):
    template_name = 'editSize.html'
    model = Size
    success_url = reverse_lazy('product:list_sizes')
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

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
        context["title"] = "Actualizar Talla"
        context['list'] = self.success_url
        context['action'] = 'update' 
        context['btn'] = 'Actualizar talla'
        context['color'] = self.get_number_color()
        return context

class UpdateCategoryView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, UpdateView):
    from_class = CategoryForm
    template_name = 'editCategory.html'
    model = Category
    success_url = reverse_lazy('product:list_cat')
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def get_form(self):
        return super().get_form(CategoryForm)
    
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
        return JsonResponse(data)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar Categoría"
        context["image"] = "img/send.png"
        context['list'] = self.success_url
        context['action'] = 'update'
        context['btn'] = 'Actualizar'
        context['color'] = self.get_number_color()
        return context

