from multiprocessing import context
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from core.product.models import Category, Product, Size


class ListSizeView(ListView):
    model = Size
    paginate_by = 3
    template_name = 'listSize.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Listado de tamaños disponibles"
        context["create"] = reverse_lazy('product:register_size')
        context["image"] = 'img/list.png'
        return context


class ListCategoryView(ListView):
    model = Category
    paginate_by = 4
    template_name = 'listCategories.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Listado de categorías"
        context["create"] = reverse_lazy('product:register_cat')
        context["image"] = 'img/list.png'
        context['create_category'] = reverse_lazy('product:register_cat')
        return context

class ListProductView(ListView):
    model = Product
    paginate_by = 5
    template_name = 'listProducts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Listado de productos"
        context["create"] =  reverse_lazy('product:register_product')
        context["image"] = 'img/list.png'
        context['create_category'] = reverse_lazy('product:register_product')
        return context