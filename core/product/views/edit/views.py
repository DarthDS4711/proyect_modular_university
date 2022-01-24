from django.views.generic.base import TemplateView


class EditProductView(TemplateView):
    template_name = "editProduct.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar producto"
        context["image"] = "img/product_edit.jpg"
        return context
