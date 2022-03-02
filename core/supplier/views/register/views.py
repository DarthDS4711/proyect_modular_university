from django.views.generic.edit import CreateView

from core.supplier.forms.supplier.form import SupplierForm


class RegisterSupplierView(CreateView):
    template_name = "registerSupplier.html"

    def get_form(self):
        return super().get_form(SupplierForm)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registrar a un proveedor"
        context["image"] = "img/supplier.png"
        return context
