from multiprocessing import context
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView
from core.product.models import Category, Product, Size


class DeleteSizeView(DeleteView):
    model = Size
    success_url = reverse_lazy('product:list_sizes')
    template_name = 'deleteSize.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminar talla"
        context['list'] = reverse_lazy('product:list_sizes')
        return context

class DeleteCategoryView(DeleteView):
    template_name = 'deleteCategory.html'
    success_url = reverse_lazy('product:list_cat')
    model = Category

    # sobrescritura del método dispach para obtener el objeto en cuestión (evitar duplicados)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            # eliminación del objeto (instancia) seleccionada
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data) # retorno de la respuesta del servidor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Eliminar Categoría"
        context["image"] = "img/delete_status_send.png"
        context['list'] = self.success_url
        context['action'] = 'delete'
        return context


class DeleteProductView(DeleteView):
    template_name = 'deleteProduct.html'
    success_url = reverse_lazy('product:list_product')
    model = Product

    # sobrescritura del método dispach para obtener el objeto en cuestión (evitar duplicados)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            # eliminación del objeto (instancia) seleccionada
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data) # retorno de la respuesta del servidor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Eliminar producto"
        context["image"] = "img/delete_status_send.png"
        context['list'] = self.success_url
        context['action'] = 'delete'
        return context