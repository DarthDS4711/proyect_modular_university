from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from core.classes.obtain_color import ObtainColorMixin
from core.product.forms.category.forms import CategoryForm
from core.product.forms.product.forms import ProductForm
from core.product.forms.size.form import SizeForm
from core.product.models import Category, Product, Size
from django.contrib.auth.mixins import LoginRequiredMixin


class UpdateProductView(LoginRequiredMixin, ObtainColorMixin, UpdateView):
    from_class = CategoryForm
    template_name = 'editProduct.html'
    model = Product
    success_url = reverse_lazy('product:list_product')
    login_url = reverse_lazy('access:Login')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def get_form(self):
        return super().get_form(ProductForm)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            form = self.get_form()
            data = form.save()
        except Exception as e:
            data['error'] = str(e)
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


class EditSizeView(LoginRequiredMixin, ObtainColorMixin, UpdateView):
    template_name = 'editSize.html'
    model = Size
    success_url = reverse_lazy('product:list_sizes')
    login_url = reverse_lazy('access:Login')

    def get_form(self):
        return super().get_form(SizeForm)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar categoría"
        context['action'] = "Editar"
        context['list'] = self.success_url
        context['color'] = self.get_number_color()
        return context

class UpdateCategoryView(LoginRequiredMixin, ObtainColorMixin, UpdateView):
    from_class = CategoryForm
    template_name = 'editCategory.html'
    model = Category
    success_url = reverse_lazy('product:list_cat')
    login_url = reverse_lazy('access:Login')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def get_form(self):
        return super().get_form(CategoryForm)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            form = self.get_form()
            data = form.save()
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

