from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin

class CancelPaymentView(LoginRequiredMixin, ObtainColorMixin, TemplateView):
    template_name = 'cancel.html'
