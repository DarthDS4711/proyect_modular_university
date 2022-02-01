from django.views.generic.base import TemplateView


class RegisterIncidenceView(TemplateView):
    template_name = 'registerIncidence.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registrar incidencia"
        context["image"] = "img/incidence.png"
        return context