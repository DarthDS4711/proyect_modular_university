from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.product.models import Product
from core.supplier.models import Supplier
from django.contrib.auth.mixins import LoginRequiredMixin


class DetailSupplierView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, DetailView):
    model = Supplier
    template_name = "detailSupplier.html"
    login_url = reverse_lazy('access:Login')


    # método que nos devuelve algunos productos relacionados al proveedor
    def get_products_of_supplier(self):
        # consulta en la cual obtenemos los primeros 2 productos de mejor valoracion del proveedor
        queryset = Product.objects.filter(supplier_id=self.object.id).order_by('product_rating')[0:2]
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalles proveedor'
        context['page_obj'] = self.get_products_of_supplier()
        context['color'] = self.get_number_color()
        return context