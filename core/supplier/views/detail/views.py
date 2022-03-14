from django.views.generic.detail import DetailView
from core.supplier.models import Supplier


class DetailSupplierView(DetailView):
    model = Supplier
    template_name = "detailSupplier.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalles proveedor'
        return context