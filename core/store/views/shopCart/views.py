from django.views.generic.base import TemplateView


class ShopCartView(TemplateView):
    template_name = "shopCart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Carrito de compra"
        context["image"] = "img/shop-cart.png"
        return context