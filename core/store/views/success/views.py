from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin

class SuccessPaymentView(LoginRequiredMixin, ObtainColorMixin, TemplateView):
    template_name = 'sucess.html'
