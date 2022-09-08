from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from config.stripe.secret_keys_payment import STRIPE_SECRET_KEY
from core.app_functions.data_replication import is_actual_state_autoreplication
from core.app_functions.rollback_data import rollback_data
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.sale.models import DetailSale, Sale
from core.status_send.models import StatusSend, StatusSendSale
from core.stock.models import Stock, StockProductSize
from django.db import transaction
import stripe
import time
from datetime import timedelta, datetime
from django.urls import reverse_lazy



class SuccessPaymentView(EmergencyModeMixin, LoginRequiredMixin, ObtainColorMixin, TemplateView):
    template_name = 'sucess.html'
    login_url = reverse_lazy('access:Login')

    # función que, en el caso de que la venta haya sido exitosa, se reduce el stock de nuestra
    # aplicación, pero validando que, en el caso de que el usuario regrese a esta pestaña
    # no se reduzca de nuevo
    def reduce_stock_products(self):
        data = {}
        try:
            status_replication = is_actual_state_autoreplication()
            lastest_sale_user = Sale.objects.filter(user = self.request.user).last()
            if lastest_sale_user.is_completed == False:
                details_lastest_sale = DetailSale.objects.filter(sale = lastest_sale_user)
                for detail_sale in details_lastest_sale:
                    new_stock = Stock.objects.get(product=detail_sale.product)
                    new_stocks_size = StockProductSize.objects.get(stock=new_stock, size=detail_sale.size)
                    new_stocks_size.amount = new_stocks_size.amount - detail_sale.ammount
                    new_stocks_size.save()
                    new_stocks_size.save(using='stock_product')
                    if status_replication:
                        new_stocks_size.save(using='mirror_database')
                    new_stock.amount = new_stock.amount - detail_sale.ammount
                    new_stock.save()
                    new_stock.save(using='stock_product')
                    if status_replication:
                        new_stock.save(using='mirror_database')
                lastest_sale_user.is_completed = True
                lastest_sale_user.save()
                if status_replication:
                    lastest_sale_user.save(using='mirror_database')
        except Exception as e:
            data['error'] = str(e)
        return data
    
    # función que genera de forma automática el estado de envio
    def __create_new_status_send(self):
        data = {}
        try:
            # creación de el estado de envio
            status_initial_send = StatusSend.objects.filter(id = 1)
            lastest_sale_user = Sale.objects.filter(user = self.request.user).last()
            status_send_sales_prev = StatusSendSale.objects.filter(sale = lastest_sale_user)
            print(status_send_sales_prev)
            if status_initial_send.exists() and (not status_send_sales_prev.exists()):
                print("creacion automática orden de envio")
                status_initial_send = status_initial_send[0]
                date_send = datetime.now() + timedelta(days=30)
                status_send_sale = StatusSendSale()
                status_send_sale.sale = lastest_sale_user
                status_send_sale.date_arrival = date_send
                status_send_sale.status_send = status_initial_send
                status_send_sale.save()
                if is_actual_state_autoreplication():
                    status_send_sale.save(using='mirror_database')
        except Exception as e:
            data['error'] = str(e)
        return data
    
    # función que obtiene el último cargo del usuario
    def obtain_list_of_charges(self, sale_id):
        last_charge = stripe.Charge.search(
            query=f"metadata['order_id']:'{sale_id}' and status:'succeeded'"
        )['data']
        return last_charge

    # función en la cual obtenemos el último cargo del usuario
    # con un tiempo de espera entre cada consulta para validar su compra
    def search_last_charge_customer(self):
        is_paid_the_transaction = False
        stripe.api_key = STRIPE_SECRET_KEY
        lastest_sale_user = Sale.objects.filter(user = self.request.user, is_completed=False).last()
        limit_attempts = 15
        if lastest_sale_user != None:
            last_charge = self.obtain_list_of_charges(lastest_sale_user.id)
            number_attempts = 0
            while len(last_charge) <= 0 and number_attempts <= limit_attempts:
                last_charge = self.obtain_list_of_charges(lastest_sale_user.id)
                number_attempts += 1
                time.sleep(3)
            if number_attempts <= limit_attempts:
                last_charge = last_charge[0]
                print(last_charge)
                if 'status' in last_charge:
                    if last_charge['status'] == 'succeeded':
                        is_paid_the_transaction = True
                        print("pagada")
        return is_paid_the_transaction


    def get(self, request, *args, **kwargs):
        data = {}
        is_paid_transaction = self.search_last_charge_customer()
        if is_paid_transaction:
            with transaction.atomic():
                data = self.reduce_stock_products()
                if 'error' in data:
                    rollback_data(1)
            if 'error' not in data:
                with transaction.atomic():
                    data = self.__create_new_status_send()
                    if 'error' in data:
                        rollback_data(3)

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Pago exitoso"
        context['color'] = self.get_number_color()
        return context
