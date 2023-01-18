from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from core.app_functions.rollback_data import rollback_data
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.warranty.forms.form_warranty_product.forms import WarrantyProductForm
from core.warranty.models import WarrantyProduct
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction


class UpdateWarrantyProductView(EmergencyModeMixin, LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, UpdateView):
    template_name = 'edit_warrantyProduct.html'
    model = WarrantyProduct
    login_url = reverse_lazy('access:Login')
    success_url = reverse_lazy('warranty:list_warrantyproduct')
    group_permisson = 'Administrator'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
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
                rollback_data(3)
        return JsonResponse(data, safe=False)


    def get_form(self):
        return super().get_form(WarrantyProductForm)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Actualizar garantía del producto"
        context['list'] = self.success_url
        context['action'] = 'update' 
        context['btn'] = 'Actualizar garantía'
        context['color'] = self.get_number_color()
        return context