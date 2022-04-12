from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class StatusSendView(LoginRequiredMixin, TemplateView):
    template_name = "statusSend.html"
    login_url = reverse_lazy('access:Login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Status envio de productos"
        return context