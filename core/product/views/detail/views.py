from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from core.product.models import Category, Product
from django.contrib.auth.mixins import LoginRequiredMixin


class DetailCategoryView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = "detailCategory.html"
    login_url = reverse_lazy('access:Login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle categoría'
        return context


class DetailProductView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'detailProduct.html'
    login_url = reverse_lazy('access:Login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle producto'
        return context