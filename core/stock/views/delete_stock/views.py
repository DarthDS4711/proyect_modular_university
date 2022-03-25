from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from core.stock.models import Stock


class DeleteStockView(DeleteView):
    model = Stock
    success_url = reverse_lazy('stock:list_stock')
    template_name = 'deleteStock.html'

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
        context["title"] = "Eliminar producto"
        context["image"] = "img/delete_status_send.png"
        context['list'] = self.success_url
        context['action'] = 'delete'
        return context