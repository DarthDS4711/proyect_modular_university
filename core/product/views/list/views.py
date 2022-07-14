from django.urls import reverse_lazy
from django.views.generic.list import ListView
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.product.models import Category, Product, Size
from django.contrib.auth.mixins import LoginRequiredMixin


class ListSizeView(EmergencyModeMixin, LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, ListView):
    model = Size
    paginate_by = 10
    template_name = 'listSize.html'
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Listado de tamaños disponibles"
        context["create"] = reverse_lazy('product:register_size')
        context["image"] = 'img/list.png'
        context['color'] = self.get_number_color()
        return context


class ListCategoryView(EmergencyModeMixin, LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, ListView):
    model = Category
    paginate_by = 4
    template_name = 'listCategories.html'
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def return_status(self):
        if 'status' in self.kwargs.keys():
            return self.kwargs['status']
        elif 'status' in self.request.GET:
            return self.request.GET['status']
        else:
            return ''
    
    def return_queryset_with_filter(self, categories, status):
        match status:
            case '':
                return categories
            case '1':
                return categories
            case '2':
                return categories.filter(is_active=True)
            case '3':
                return categories.filter(is_active=False)
    
    def get_queryset(self):
        name = self.return_name()
        status = self.return_status()
        if name != '':
            categories = Category.objects.filter(name__icontains=self.return_name())
            return self.return_queryset_with_filter(categories, status)
        else:
            categories = Category.objects.all()
            return self.return_queryset_with_filter(categories, status)

    def return_name(self):
        if 'name' in self.kwargs.keys():
            return self.kwargs['name']
        elif 'name' in self.request.GET:
            return self.request.GET['name']
        else:
            return ''


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Listado de categorías"
        context["create"] = reverse_lazy('product:register_cat')
        context["image"] = 'img/list.png'
        context['create_category'] = reverse_lazy('product:register_cat')
        context['color'] = self.get_number_color()
        context['url'] = reverse_lazy('product:list_cat')
        context['name'] = self.return_name()
        context['status'] = self.return_status()
        return context

class ListProductView(EmergencyModeMixin, LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, ListView):
    model = Product
    paginate_by = 10
    template_name = 'listProducts.html'
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
    
    def return_queryset_with_filter(self, products, status):
        match status:
            case '':
                return products
            case '1':
                return products
            case '2':
                return products.filter(is_active=True)
            case '3':
                return products.filter(is_active=False)
    
    def get_queryset(self):
        name = self.return_name()
        status = self.return_status()
        if name != '':
            products_and_names = Product.objects.filter(name__icontains=self.return_name())
            return self.return_queryset_with_filter(products_and_names, status)
        else:
            products = Product.objects.all()
            return self.return_queryset_with_filter(products, status)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Listado de productos"
        context["create"] =  reverse_lazy('product:register_product')
        context["image"] = 'img/list.png'
        context['create_category'] = reverse_lazy('product:register_product')
        context['color'] = self.get_number_color()
        context['url'] = reverse_lazy('product:list_product')
        context['name'] = self.return_name()
        context['status'] = self.return_status()
        return context