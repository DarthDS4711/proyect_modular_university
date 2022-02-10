from django.views.generic.base import TemplateView


class EditWarrantyView(TemplateView):
    template_name = 'editWarranty.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Editar garantía'
        context["image"] = 'img/warranty.png'
        context["action"] = 'Editar'
        return context