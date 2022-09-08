from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from core.app_functions.data_replication import is_actual_state_autoreplication
from core.app_functions.rollback_data import rollback_data
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from core.sale.models import Sale
from core.status_send.forms.form_status_send_client import StatusSendClientForm
from core.status_send.models import StatusSend, StatusSendSale
from django.db import transaction



class RegisterStatusSendSaleView(EmergencyModeMixin, LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, CreateView):
    template_name = "registerStatusSendSale.html"
    model = StatusSendSale
    success_url = reverse_lazy('status_send:list_status_send_admin')
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def convert_string_number(self, request):
        try:
            number = int(request.POST['term'])
            return number
        except:
            return 1
    
    # función que guarda el estatus de envio 
    def save_status_send_sale(self, request):
        data = {}
        try:
            sale_invoice = Sale.objects.get(id = int(request.POST['sale']))
            status_send_invoice = StatusSend.objects.get(id = int(request.POST['status_send']))
            date_arrival = request.POST['date_arrival']
            status_send_sale = StatusSendSale()
            status_send_sale.sale = sale_invoice
            status_send_sale.status_send = status_send_invoice
            status_send_sale.date_arrival = date_arrival
            status_send_sale.save()
            if is_actual_state_autoreplication():
                status_send_sale.save(using='mirror_database')
        except Exception as e:
            data['error'] = str(e)
        return data

    # sobrescritura del método post para el guardado de los datos
    def post(self, request, *args, **kwargs):
        data = {}
        match request.POST['action']:
            case 'autocomplete':
                data = []
                sales_data = Sale.objects.filter(id = self.convert_string_number(request), is_completed=True)
                if sales_data.exists():
                    sale = sales_data[0]
                    item = sale.toJSON()
                    item['text'] = f'Factura: {sale.id}, Usuario: {sale.user.username}'
                    data.append(item)
            case 'register':
                data = self.save_status_send_sale(request)
                with transaction.atomic():
                    if 'error' in data:
                        rollback_data(3)
        # regreso de la respuesta del servidor
        return JsonResponse(data, safe=False)


    def get_form(self):
        return super().get_form(StatusSendClientForm)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registrar estado de envio usuario"
        context['list'] = self.success_url
        context['action'] = 'register' 
        context['btn'] = 'Registrar estado usuario'
        context['color'] = self.get_number_color()
        return context
