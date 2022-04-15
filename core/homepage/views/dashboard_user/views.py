from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin


class DashboardUserView(LoginRequiredMixin, ObtainColorMixin, TemplateView):
    template_name = 'dashboardUser.html'
    login_url = reverse_lazy('access:Login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dashboard'
        context['color'] = self.get_number_color()
        return context