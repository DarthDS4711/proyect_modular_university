from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.mixins import ValidateSessionGroupMixin
from core.stock.models import Stock
from core.stock.form.forms import StockEditForm
from django.contrib.auth.mixins import LoginRequiredMixin


# clase para crear los stock
class UpdateStockView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, UpdateView):
    template_name = 'editStock.html'
    model = Stock
    success_url = reverse_lazy('stock:list_stock')
    form_class = StockEditForm
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
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
        context['title'] = "Editar Stock"
        context['list'] = self.success_url
        context['action'] = 'update' 
        context['btn'] = 'Editar stock'
        context['color'] = self.get_number_color()
        return context