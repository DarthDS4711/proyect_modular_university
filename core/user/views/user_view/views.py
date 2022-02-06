from webbrowser import get
from django.views.generic.base import TemplateView


class ProfileUserView(TemplateView):
    template_name = 'user_view_profile/page_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Perfil'
        return context