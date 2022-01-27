from django.views.generic.base import TemplateView


class DetailProductView(TemplateView):
    template_name = "detailProduct.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Vestido coleccion primavera"
        context["image"] = "img/dress.png"
        return context