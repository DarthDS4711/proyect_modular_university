from django.views.generic.base import TemplateView


class EditIncidenceView(TemplateView):
    template_name = 'editIncidence.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar incidencia"
        context["image"] = "img/incidence.png"
        return context