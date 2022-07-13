from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.app_functions.data_replication import is_actual_state_autoreplication
from core.app_functions.rollback_data import rollback_data
from core.classes.obtain_color import ObtainColorMixin
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.sale.models import DetailSale, Sale
from core.stock.models import Stock, StockProductSize
from django.db import transaction


class SuccessPaymentView(EmergencyModeMixin, LoginRequiredMixin, ObtainColorMixin, TemplateView):
    template_name = 'sucess.html'

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

    def get(self, request, *args, **kwargs):
        data = {}
        with transaction.atomic():
            data = self.reduce_stock_products()
            if 'error' in data:
                rollback_data(1)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Pago exitoso"
        context['color'] = self.get_number_color()
        return context
