from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class ShopCartView(LoginRequiredMixin, TemplateView):
    template_name = "shopCart.html"
    login_url = reverse_lazy('access:Login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Carrito de compra"
        context["image"] = "img/shop-cart.png"
        return context