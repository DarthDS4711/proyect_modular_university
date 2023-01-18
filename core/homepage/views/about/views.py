from django.views.generic import TemplateView
from django.urls import reverse_lazy
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin

# template view for the main page
class AboutPageView(EmergencyModeMixin, TemplateView, ObtainColorMixin):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Acerca de nosotros"
        context['color'] = self.get_number_color()
        return context
