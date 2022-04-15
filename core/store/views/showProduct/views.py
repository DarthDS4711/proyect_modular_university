from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from core.classes.obtain_color import ObtainColorMixin
from core.product.models import Product
from core.stock.models import Stock
from django.contrib.auth.mixins import LoginRequiredMixin



class DetailProductView(LoginRequiredMixin, ObtainColorMixin ,DetailView):
    template_name = "detailProductShop.html"
    model = Product
    login_url = reverse_lazy('access:Login')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    # método que bloquea o habilita el botón de agregar al carrito
    def return_status_stock(self):
        stock = Stock.objects.get(product=self.object.id)
        if stock is not None:
            if stock.amount > 0:
                return True
            else:
                return False
        else:
            return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.name
        context['stock'] = self.return_status_stock()
        context['color'] = self.get_number_color()
        return context