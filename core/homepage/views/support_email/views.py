from django.views.generic import TemplateView
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin


class SupportEmailView(EmergencyModeMixin, TemplateView, ObtainColorMixin):
    template_name = 'emailSupport.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Correo del equipo de soporte"
        context['color'] = self.get_number_color()
        return context
