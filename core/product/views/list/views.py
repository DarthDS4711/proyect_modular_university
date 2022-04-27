from django.urls import reverse_lazy
from django.views.generic.list import ListView
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.product.models import Category, Product, Size
from django.contrib.auth.mixins import LoginRequiredMixin


class ListSizeView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, ListView):
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


class ListCategoryView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, ListView):
    model = Category
    paginate_by = 4
    template_name = 'listCategories.html'
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Listado de categorías"
        context["create"] = reverse_lazy('product:register_cat')
        context["image"] = 'img/list.png'
        context['create_category'] = reverse_lazy('product:register_cat')
        context['color'] = self.get_number_color()
        return context

class ListProductView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, ListView):
    model = Product
    paginate_by = 10
    template_name = 'listProducts.html'
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Listado de productos"
        context["create"] =  reverse_lazy('product:register_product')
        context["image"] = 'img/list.png'
        context['create_category'] = reverse_lazy('product:register_product')
        context['color'] = self.get_number_color()
        return context