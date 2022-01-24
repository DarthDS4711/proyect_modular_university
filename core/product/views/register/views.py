from django.views.generic.base import TemplateView


class RegisterProductView(TemplateView):
    template_name = "registerProduct.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registrar producto"
        context["image"] = "img/product.png"
        return context
