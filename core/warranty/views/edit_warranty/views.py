from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from core.app_functions.rollback_data import rollback_data
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.warranty.forms.form_warranty.forms import WarrantyForm
from core.warranty.models import WarrantySale
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction


class EditWarrantyView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, UpdateView):
    template_name = 'editWarranty.html'
    model = WarrantySale
    login_url = reverse_lazy('access:Login')
    success_url = reverse_lazy('warranty:list_warranty')
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
        return super().get_form(WarrantyForm)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Actualizar garantía"
        context['list'] = self.success_url
        context['action'] = 'update' 
        context['btn'] = 'Actualizar garantía'
        context['color'] = self.get_number_color()
        return context