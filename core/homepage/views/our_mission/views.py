from django.views.generic import TemplateView
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin

# template view for the main page
class OurMissionPageView(EmergencyModeMixin, TemplateView, ObtainColorMixin):
    template_name = 'ourMission.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Nuestra misión"
        context['color'] = self.get_number_color()
        return context
