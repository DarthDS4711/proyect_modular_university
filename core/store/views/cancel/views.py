import json
from django.http import JsonResponse
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.app_functions.data_replication import is_actual_state_autoreplication
from core.app_functions.rollback_data import rollback_data
from core.classes.obtain_color import ObtainColorMixin
from core.product.models import Product, Size
from core.sale.models import DetailSale, Sale
from core.stock.models import Stock, StockProductSize
from django.db import transaction

class CancelPaymentView(LoginRequiredMixin, ObtainColorMixin, TemplateView):
    template_name = 'cancel.html'

    # función que en el caso de que el pago sea declinado eliminara la factura 
    # y regresará los productos que el usuario haya comprado
    def return_previous_state_checkout(self, request):
        data = {}
        try:
            status_replication = is_actual_state_autoreplication()
            products = json.loads(request.POST['products'])
            sale_to_reject = Sale.objects.filter(user = self.request.user).last()
            id_sale_to_reject = sale_to_reject.id
            details_sale_to_reject = DetailSale.objects.filter(sale = sale_to_reject)
            for detail_sale in details_sale_to_reject:
                id_detail = detail_sale.id
                detail_sale.delete()
                if status_replication:
                    DetailSale.objects.using('mirror_database').get(
                        id = id_detail).delete(using='mirror_database')
            sale_to_reject.delete()
            if status_replication:
                Sale.objects.using('mirror_database').get(
                    id = id_sale_to_reject).delete(using='mirror_database')
            for product in products:
                amount_to_return = int(product['amount'])
                product_sale = Product.objects.get(id=int(product['id']))
                size_sale = Size.objects.get(size_product=product['size'])
                new_stock = Stock.objects.get(product=product_sale)
                new_stocks_size = StockProductSize.objects.get(stock=new_stock, size=size_sale)
                new_stocks_size.amount += amount_to_return
                new_stocks_size.save()
                new_stocks_size.save(using='stock_product')
                if status_replication:
                    new_stocks_size.save(using='mirror_database')
                new_stock.amount = new_stock.amount + amount_to_return
                new_stock.save()
                new_stock.save(using='stock_product')
                if status_replication:
                    new_stock.save(using='mirror_database')
        except Exception as e:
            data['error'] = str(e)
        return data
    
    def post(self, request, *args, **kwargs):
        data = {}
        with transaction.atomic():
            data = self.return_previous_state_checkout(request)
            if 'error' in data:
                rollback_data(1)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Pago declinado"
        context['color'] = self.get_number_color()
        return context

