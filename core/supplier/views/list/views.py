from django.urls import reverse_lazy
from django.views.generic.list import ListView

from core.supplier.models import Supplier


class ListSupplierView(ListView):
    model = Supplier # modelo a usar para la consulta del ListView
    paginate_by = 4 # número de elementos a mostrar por pagina
    template_name = 'listSupplier.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Listado de proveedores"
        context["create"] = reverse_lazy('supplier_app:register_supplier')
        context["image"] = 'img/list.png'
        return context
