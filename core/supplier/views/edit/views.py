from django.views.generic.base import TemplateView


class EditSupplierView(TemplateView):
    template_name = "editSupplier.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar al proveedor"
        context["image"] = "img/editSupplier.png"
        return context
