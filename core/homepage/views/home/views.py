from django.views.generic import TemplateView
from django.urls import reverse_lazy
from core.classes.obtain_color import ObtainColorMixin

# template view for the main page
class HomepageView(TemplateView, ObtainColorMixin):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Shop IA online"
        context['signin'] = reverse_lazy('access:signin')
        context['color'] = self.get_number_color()
        return context
