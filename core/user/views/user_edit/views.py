from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class EditUserView(LoginRequiredMixin, TemplateView):
    template_name = 'user_edit/page_edit.html'
    login_url = reverse_lazy('access:Login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar perfil'
        context['btn_action'] = 'Editar'
        return context