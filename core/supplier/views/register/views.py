from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.app_functions.rollback_data import rollback_data
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.supplier.forms.supplier.form import SupplierForm
from core.supplier.models import Supplier
from django.db import transaction


class RegisterSupplierView(EmergencyModeMixin, LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, CreateView):
    template_name = "registerSupplier.html"
    model = Supplier
    success_url = reverse_lazy('supplier_app:list_supplier')
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def get_form(self):
        return super().get_form(SupplierForm)
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # sobrescritura del método post para el guardado de los datos
    def post(self, request, *args, **kwargs):
        data = {}
        with transaction.atomic():
            # obtención de los datos
            form = self.get_form()
            # guardado de los datos
            data = form.save()
            if 'error' in data:
                rollback_data(1)
        # regreso de la respuesta del servidor
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registrar a un proveedor"
        context["image"] = "img/supplier.png"
        context['list'] = self.success_url
        context['action'] = 'register' 
        context['btn'] = 'Registrar proovedor'
        context['color'] = 3
        context['color'] = self.get_number_color()
        return context
