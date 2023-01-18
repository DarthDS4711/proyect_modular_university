from django.views.generic.base import TemplateView
from core.mixins.emergency_mixin import EmergencyModeMixin


class DeleteWarrantyView(EmergencyModeMixin, TemplateView):
    template_name = 'deleteWarranty.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Eliminar garantía'
        context["image"] = 'img/trash-incidence.png'
        return context