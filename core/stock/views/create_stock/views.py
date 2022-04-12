from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from core.stock.models import Stock
from core.stock.form.forms import StockForm
from django.contrib.auth.mixins import LoginRequiredMixin


# clase para crear los stock
class CreateStockView(LoginRequiredMixin, CreateView):
    template_name = 'createStock.html'
    model = Stock
    success_url = reverse_lazy('stock:list_stock')
    form_class = StockForm
    login_url = reverse_lazy('access:Login')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_form(self):
        return super().get_form(self.form_class)
    
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
        context['title'] = "Registrar Stock"
        context['list'] = self.success_url
        context['action'] = 'register' 
        context['btn'] = 'Registrar stock'
        return context