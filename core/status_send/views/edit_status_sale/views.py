from datetime import datetime
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from core.app_functions.data_replication import is_actual_state_autoreplication
from core.app_functions.rollback_data import rollback_data
from core.mixins.mixins import ValidateSessionGroupMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from core.status_send.forms.form_edit_status_sale import EditStatusSendClientForm
from core.status_send.models import StatusSend, StatusSendSale
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction


class UpdateStatusSendSaleView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, UpdateView):
    template_name = "registerStatusSendSale.html"
    model = StatusSendSale
    success_url = reverse_lazy('status_send:list_status_send_admin')
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def convert_string_boolean(self, request):
        if request.POST.get('delivered') == None:
            return False
        else:
            return True
    
    # función que edita y guarda el registro actual del estado de envio
    # para el usuario en cuestión
    def update_status_send_sale(self, request):
        data = {}
        try:
            status_send_invoice = StatusSend.objects.get(id = int(request.POST['status_send']))
            date_actual_state = datetime.now()
            delivered = self.convert_string_boolean(request)
            self.object.status_send = status_send_invoice
            self.object.delivered = delivered
            self.object.date_actual_state = date_actual_state
            self.object.save()
            if is_actual_state_autoreplication():
                self.object.save(using='mirror_database')
        except Exception as e:
            data['error'] = str(e)
        return data

    # sobrescritura del método post para el guardado de los datos
    def post(self, request, *args, **kwargs):
        data = {}
        with transaction.atomic():
            data = self.update_status_send_sale(request)
            if 'error' in data:
                rollback_data(3)
        
        # regreso de la respuesta del servidor
        return JsonResponse(data, safe=False)


    def get_form(self):
        return super().get_form(EditStatusSendClientForm)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Actualizar estado de envio usuario"
        context['list'] = self.success_url
        context['action'] = 'update' 
        context['btn'] = 'Actualizar estado usuario'
        context['color'] = self.get_number_color()
        return context
