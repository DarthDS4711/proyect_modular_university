from django.http import JsonResponse
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.app_functions.data_replication import is_actual_state_autoreplication
from core.app_functions.rollback_data import rollback_data
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.sale.models import DetailSale, Sale
from django.db import transaction


class CancelPaymentView(EmergencyModeMixin, LoginRequiredMixin, ObtainColorMixin, TemplateView):
    template_name = 'cancel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Pago declinado"
        context['color'] = self.get_number_color()
        return context

