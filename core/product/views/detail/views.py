from django.views.generic.detail import DetailView
from core.product.models import Category, Product


class DetailCategoryView(DetailView):
    model = Category
    template_name = "detailCategory.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle categoría'
        return context


class DetailProductView(DetailView):
    model = Product
    template_name = 'detailProduct.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle producto'
        return context