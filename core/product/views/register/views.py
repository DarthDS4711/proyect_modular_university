from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from core.app_functions.rollback_data import rollback_data
from core.mixins.mixins import ValidateSessionGroupMixin
from core.product.forms.category.forms import CategoryForm
from core.product.forms.product.forms import ProductForm
from core.product.forms.size.form import SizeForm
from core.product.models import Category, Product
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from django.db import transaction



class RegisterProductView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, CreateView):
    template_name = "registerProduct.html"
    model = Product
    success_url = reverse_lazy('product:list_product')
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # sobrescritura del método post para el guardado de los datos
    def post(self, request, *args, **kwargs):
        data = {}
        with transaction.atomic():
            form = self.get_form()
            data = form.save()
            if 'error' in data:
                rollback_data(1)
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
