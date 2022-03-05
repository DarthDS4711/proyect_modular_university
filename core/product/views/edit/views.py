from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from core.product.forms.size.form import SizeForm
from core.product.models import Size


class EditProductView(TemplateView):
    template_name = "editProduct.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar producto"
        context["image"] = "img/product_edit.jpg"
        return context


class EditSizeView(UpdateView):
    template_name = 'editSize.html'
    model = Size
    success_url = reverse_lazy('product:list_sizes')
    

    def get_form(self):
        return super().get_form(SizeForm)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar categoría"
        context['action'] = "Editar"
        return context
