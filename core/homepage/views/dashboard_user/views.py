from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin
from django.contrib.sessions.models import Session

from core.sale.models import DetailSale, Sale


class DashboardUserView(EmergencyModeMixin, LoginRequiredMixin, ObtainColorMixin, TemplateView):
    template_name = 'dashboardUser.html'
    login_url = reverse_lazy('access:Login')

    # función que gestiona el número de sesiones ativas
    def __get_number_sessions(self):
        number_sessions = 0
        session_query = Session.objects.all()
        for session in session_query:
            user_key = session.get_decoded().get('_auth_user_id')
            if self.request.user.pk == int(user_key):
                number_sessions += 1
        return number_sessions
    
    # función que valida si el producto ha sido agregado anteriormente
    def __is_valid_insertion(self, list_products, product, number_products):
        is_found = True
        if number_products < 3:
            for product_to_search in list_products:
                if product_to_search.name == product.name:
                    is_found = False
        else:
            is_found = False
        return is_found

    
    # función que obtiene los últimos productos comprados por el usuario y la cantidad de los mismos
    def __obtain_last_bought_products(self):
        number_products = 0
        list_last_bought_products = []
        sales_user = Sale.objects.filter(
            user = self.request.user, is_completed=True).order_by('-date_sale')
        for sale_user in sales_user:
            bought_products = DetailSale.objects.filter(sale = sale_user)
            for bought_product in bought_products:
                if self.__is_valid_insertion(list_last_bought_products, bought_product.product, number_products):
                    list_last_bought_products.append(bought_product.product)
                    number_products += 1
        return number_products, list_last_bought_products


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        number_products, list_last_bought_products = self.__obtain_last_bought_products()
        context['title'] = 'Dashboard'
        context['color'] = self.get_number_color()
        context['number_sessions'] = self.__get_number_sessions()
        context['class_css'] = number_products
        context['last_products'] = list_last_bought_products
        return context