from multiprocessing import context
from django.views.generic.base import TemplateView


class ShowWarrantyProductView(TemplateView):
    template_name = 'warrantyProduct.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Garantía del producto"
        context["image"] = "img/dress_warranty.png"
        return context