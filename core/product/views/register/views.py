from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from core.product.forms.category.forms import CategoryForm
from core.product.forms.size.form import SizeForm
from core.product.models import Category



class RegisterProductView(TemplateView):
    template_name = "registerProduct.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registrar producto"
        context["image"] = "img/product.png"
        return context


class RegisterCategoryView(CreateView):
    template_name = 'registerCategory.html'
    model = Category
    success_url = reverse_lazy('product:list_cat')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # sobrescritura del método post para el guardado de los datos
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            # obtención de los datos
            form = self.get_form()
            # guardado de los datos
            data = form.save()
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
        return context


class RegisterSizeView(CreateView):
    template_name = 'registerSize.html'
    success_url = reverse_lazy('product:list_sizes')

    def get_form(self):
        return super().get_form(SizeForm)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registrar talla"
        context['action'] = "Guardar"
        return context
