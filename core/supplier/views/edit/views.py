from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from core.classes.obtain_color import ObtainColorMixin
from core.supplier.forms.supplier.form import SupplierForm
from django.contrib.auth.mixins import LoginRequiredMixin
from core.supplier.models import Supplier

    
class EditSupplierView(LoginRequiredMixin, ObtainColorMixin, UpdateView):
    template_name = "editSupplier.html"
    model = Supplier
    success_url = reverse_lazy('supplier_app:list_supplier')
    login_url = reverse_lazy('access:Login')

    def get_form(self):
        return super().get_form(SupplierForm)
    
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registrar a un proveedor"
        context["image"] = "img/supplier.png"
        context['list'] = self.success_url
        context['action'] = 'register' 
        context['btn'] = 'Registrar proovedor'
        context['color'] = self.get_number_color()
        return context
