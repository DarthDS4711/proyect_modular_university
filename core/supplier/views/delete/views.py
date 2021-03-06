from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.supplier.models import Supplier


class DeleteSupplierView(EmergencyModeMixin, LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, DeleteView):
    template_name = 'deleteSupplier.html'
    success_url = reverse_lazy('supplier_app:list_supplier')
    model = Supplier
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    # sobrescritura del método dispach para obtener el objeto en cuestión (evitar duplicados)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            # eliminación del objeto (instancia) seleccionada
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data) # retorno de la respuesta del servidor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Eliminar Proveedor"
        context["image"] = "img/delete_status_send.png"
        context['list'] = self.success_url
        context['action'] = 'delete'
        context['color'] = self.get_number_color()
        return context

