from django.views.generic.base import TemplateView

class DeleteSupplierView(TemplateView):
    template_name =  "deleteSupplier.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Eliminar proveedor"
        return context

