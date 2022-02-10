from django.views.generic.base import TemplateView


class CreateWarrantyView(TemplateView):
    template_name = 'createWarranty.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Crear garantía'
        context["image"] = 'img/warranty.png'
        context["action"] = 'Registrar'
        return context