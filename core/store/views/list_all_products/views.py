from django.urls import reverse_lazy
from django.views.generic.list import ListView
from core.product.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin


class ListAllProductsView(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 10
    template_name = 'listAllProducts.html'
    login_url = reverse_lazy('access:Login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Todos los productos"
        context["discount"] = False
        return context

