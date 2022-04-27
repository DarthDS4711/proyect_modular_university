from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.warranty.forms.form_warranty.forms import WarrantyForm
from core.warranty.models import WarrantySale
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateWarrantyView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, CreateView):
    template_name = 'createWarranty.html'
    model = WarrantySale
    login_url = reverse_lazy('access:Login')
    success_url = reverse_lazy('warranty:list_warranty')
    group_permisson = 'Administrator'

    # sobrescritura del método post para el guardado de los datos
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            # obtención de los datos
            form = self.get_form()
            # guardado de los datos
            data = form.save()
        except Exception as e:
            data['error'] = str(e)
        # regreso de la respuesta del servidor
        return JsonResponse(data, safe=False)


    def get_form(self):
        return super().get_form(WarrantyForm)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registrar garantía"
        context['list'] = self.success_url
        context['action'] = 'register' 
        context['btn'] = 'Registrar garantía'
        context['color'] = self.get_number_color()
        return context