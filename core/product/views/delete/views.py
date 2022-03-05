from multiprocessing import context
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView

from core.product.models import Size


class DeleteProductView(TemplateView):
    template_name = 'deleteProduct.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Eliminar producto"
        context["image"] = "img/delete-product.png"
        return context


class DeleteSizeView(DeleteView):
    model = Size
    success_url = reverse_lazy('product:list_sizes')
    template_name = 'deleteSize.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminar talla"
        context['list'] = reverse_lazy('product:list_sizes')
        return context