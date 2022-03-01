from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from core.product.forms.category.forms import CategoryForm
from core.product.forms.size.form import SizeForm



class RegisterProductView(TemplateView):
    template_name = "registerProduct.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registrar producto"
        context["image"] = "img/product.png"
        return context


class RegisterCategoryView(CreateView):
    template_name = 'registerCategory.html'

    def get_form(self):
        return super().get_form(CategoryForm)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registrar Categoría"
        return context


class RegisterSizeView(CreateView):
    template_name = 'registerSize.html'

    def get_form(self):
        return super().get_form(SizeForm)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registrar talla"
        return context
