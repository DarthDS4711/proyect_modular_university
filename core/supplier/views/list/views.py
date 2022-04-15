from multiprocessing import context
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from core.product.models import Product
from core.supplier.models import Supplier


class ListSupplierView(LoginRequiredMixin, ObtainColorMixin, ListView):
    model = Supplier # modelo a usar para la consulta del ListView
    paginate_by = 4 # número de elementos a mostrar por pagina
    template_name = 'listSupplier.html'
    login_url = reverse_lazy('access:Login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Listado de proveedores"
        context["create"] = reverse_lazy('supplier_app:register_supplier')
        context["image"] = 'img/list.png'
        context['color'] = self.get_number_color()
        return context


class ListAllProductSupplierView(LoginRequiredMixin, ObtainColorMixin, ListView):
    model = Product
    paginate_by = 5
    template_name = 'listAllProductsOfSupplier.html'
    login_url = reverse_lazy('access:Login')

    def get_queryset(self):
        queryset = Product.objects.filter(supplier_id=self.kwargs['id_supplier'])
        return queryset
    

    def get_context_data(self, **kwargs):
        name = Supplier.objects.get(id=self.kwargs['id_supplier'])
        context = super().get_context_data(**kwargs)
        context['title'] = f'Productos del proveedor: {name.get_name()}'
        context['color'] = self.get_number_color()
        return context
    

