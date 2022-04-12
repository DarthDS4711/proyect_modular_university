from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class OptionsProductView(LoginRequiredMixin, TemplateView):
    template_name = 'optionsProducts.html'
    login_url = reverse_lazy('access:Login')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Opciones'
        return context