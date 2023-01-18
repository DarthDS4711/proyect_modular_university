from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.sale.models import DetailSale, Sale


class DetailInvoiceView(EmergencyModeMixin, LoginRequiredMixin, ObtainColorMixin, DetailView):
    template_name = 'detail_invoice.html'
    login_url = reverse_lazy('access:Login')
    model = Sale

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Detalle factura"
        context["image"] = "img/shop-cart.png"
        context['color'] = self.get_number_color()
        context['details'] = DetailSale.objects.filter(sale = self.object)
        context['number_elements'] = self.object.get_number_elements()
        context['iva'] = "16%"
        return context