from webbrowser import get
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileUserView(LoginRequiredMixin, TemplateView):
    template_name = 'user_view_profile/page_view.html'
    login_url = reverse_lazy('access:Login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Perfil'
        return context