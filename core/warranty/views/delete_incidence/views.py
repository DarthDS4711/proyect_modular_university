from django.views.generic.base import TemplateView
from core.mixins.emergency_mixin import EmergencyModeMixin


class DeleteIncidenceView(EmergencyModeMixin, TemplateView):
    template_name = 'deleteIncidence.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context["title"] = "Eliminar incidencia"
        context["image"] = "img/trash-incidence.png"
        return context