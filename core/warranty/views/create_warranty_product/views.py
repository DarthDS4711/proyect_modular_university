from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.warranty.forms.form_warranty_product.forms import WarrantyProductForm
from core.warranty.models import WarrantyProduct
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateWarrantyProductView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, CreateView):
    template_name = 'createWarrantyProduct.html'
    model = WarrantyProduct
    login_url = reverse_lazy('access:Login')
    success_url = reverse_lazy('warranty:list_warrantyproduct')
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
        # regreso de la respuesta del 
        print(data)
        return JsonResponse(data, safe=False)


    def get_form(self):
        return super().get_form(WarrantyProductForm)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registrar garantía del producto"
        context['list'] = self.success_url
        context['action'] = 'register' 
        context['btn'] = 'Registrar garantía'
        context['color'] = self.get_number_color()
        return context