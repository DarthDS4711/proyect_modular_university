from django.views.generic.base import TemplateView


class RegisterSupplierView(TemplateView):
    template_name = "registerSupplier.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registrar a un proveedor"
        return context
