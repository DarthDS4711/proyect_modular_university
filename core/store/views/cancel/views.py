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

    # función que en el caso de que el pago sea declinado eliminara la factura 
    # pero mantendrá visible en el navegador los productos a comprar
    def return_previous_state_checkout(self):
        data = {}
        try:
            status_replication = is_actual_state_autoreplication()
            sale_to_reject = Sale.objects.filter(user = self.request.user).last()
            if sale_to_reject.is_completed == False:
                id_sale_to_reject = sale_to_reject.id
                details_sale_to_reject = DetailSale.objects.filter(sale = sale_to_reject)
                for detail_sale in details_sale_to_reject:
                    id_detail = detail_sale.id
                    detail_sale.delete()
                    if status_replication:
                        DetailSale.objects.using('mirror_database').get(
                            id = id_detail).delete(using='mirror_database')
                sale_to_reject.delete()
                if status_replication:
                    Sale.objects.using('mirror_database').get(
                        id = id_sale_to_reject).delete(using='mirror_database')
        except Exception as e:
            data['error'] = str(e)
        return data
    
    def post(self, request, *args, **kwargs):
        data = {}
        with transaction.atomic():
            data = self.return_previous_state_checkout()
            if 'error' in data:
                rollback_data(1)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Pago declinado"
        context['color'] = self.get_number_color()
        return context

