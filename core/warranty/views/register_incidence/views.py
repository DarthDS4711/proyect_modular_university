from django.views.generic.edit import CreateView

from core.warranty.forms.form_incidence.form import IncidenceForm


class RegisterIncidenceView(CreateView):
    template_name = 'registerIncidence.html'

    def get_form(self):
        return super().get_form(IncidenceForm)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registrar incidencia"
        context["image"] = "img/incidence.png"
        return context