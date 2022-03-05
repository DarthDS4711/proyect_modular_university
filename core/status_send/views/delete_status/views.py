from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from core.status_send.models import StatusSend


class DeleteStatusSendView(DeleteView):
    template_name = 'deleteStatusSend.html'
    success_url = reverse_lazy('status_send:list')
    model = StatusSend

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
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Eliminar Estado de Envio"
        context["image"] = "img/delete_status_send.png"
        context['list'] = self.success_url
        context['action'] = 'delete'
        return context