from datetime import datetime
import string
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from core.colorpage.models import ColorPage
from core.mixins.mixins import ValidateSessionGroupMixin
from core.product.models import Product
from django.http import JsonResponse

from core.user.models import User


class StateDatabasesView(LoginRequiredMixin, ValidateSessionGroupMixin, ObtainColorMixin, TemplateView):
    template_name = 'state_databases.html'
    login_url = reverse_lazy('access:Login')
    group_permisson = 'Administrator'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    # test main database
    def get_state_of_database(self, database):
        data = {}
        try:
            ColorPage.objects.using(database).all()
            data['type'] = 'success'
            data['message'] = f'La base de datos {database} funciona correctamente'
        except:
            data['type'] = 'danger'
            data['message'] = f'La base de datos {database} no esta funcionando'
        return data



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Estado de la página'
        context['state_main'] = self.get_state_of_database(database='default')
        context['state_stock'] = self.get_state_of_database(database='color')
        context['state_color'] = self.get_state_of_database(database='stock_product')
        context['state_mirror'] = self.get_state_of_database(database='mirror_database')
        context['color'] = self.get_number_color()
        return context
