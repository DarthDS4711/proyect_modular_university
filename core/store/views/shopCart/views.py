import json
from locale import currency
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import stripe
from config.stripe.secret_keys_payment import STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY
from core.app_functions.data_replication import is_actual_state_autoreplication
from core.app_functions.rollback_data import rollback_data
from core.classes.obtain_color import ObtainColorMixin
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from core.mixins.emergency_mixin import EmergencyModeMixin
from core.product.models import Product, Size
from core.stock.models import Stock, StockProductSize
from core.sale.models import DetailSale, Sale
from core.user.models import DirectionUser


class ShopCartView(EmergencyModeMixin, LoginRequiredMixin, ObtainColorMixin, TemplateView):
    template_name = "shopCart.html"
    login_url = reverse_lazy('access:Login')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def return_status_stock(self, request, products):
        # request que nos valida primero la compra mediante la deteccion de
        # faltantes en el stock por medio de bases de datos distribuidas
        data = {}
        try:
            validate_transaction = True
            with transaction.atomic():
                for product in products:
                    product_sale = Product.objects.get(id=int(product['id']))
                    ammount_product_size = int(product['amount'])
                    size_sale = Size.objects.get(size_product=product['size'])
                    new_stock = Stock.objects.using('stock_product').get(product=product_sale)
                    new_stocks_size = StockProductSize.objects.using(
                        'stock_product').get(stock=new_stock, size=size_sale)
                    new_stocks_size.amount = new_stocks_size.amount - ammount_product_size
                    new_stocks_size.save(using='stock_product')
                    new_stock.amount = new_stock.amount - ammount_product_size
                    new_stock.save(using='stock_product')
                    if new_stocks_size.amount < 0:
                        validate_transaction = False
                        break
                transaction.set_rollback(True, using='stock_product')
                if validate_transaction == False:
                    data['error'] = 'Stock insuficiente en alguno de tus productos'
        except Exception as e:
            data['error'] = str(e)
        return data
    
    def do_the_purchase(self, request):
        # petición post que realiza con una transacción atómica
        # la venta al sistema, pero, sin que esta disminuya los stocks
        # es decir, unicamente crea la orden 
        data = {}
        try:
            status_replication = is_actual_state_autoreplication()
            products = json.loads(request.POST['products'])
            sale = Sale()
            sale.user = self.request.user
            sale.subtotal = float(request.POST['subtotal'])
            sale.total = float(request.POST['total'])
            direction = DirectionUser.objects.get(id = int(request.POST['direction_user']))
            sale.direction = direction
            sale.is_completed = False
            sale.save()
            if status_replication:
                sale.save(using='mirror_database')
            sale = Sale.objects.all().latest('id')
            # recorrido de los productos solicitados para su procesamiento
            for product in products:
                detail_sale = DetailSale()
                detail_sale.sale = sale
                product_sale = Product.objects.get(id=int(product['id']))
                detail_sale.product = product_sale
                detail_sale.ammount = int(product['amount'])
                detail_sale.color = product['color']
                size_sale = Size.objects.get(size_product=product['size'])
                detail_sale.size = size_sale
                detail_sale.price = float(product['price']) / detail_sale.ammount
                detail_sale.subtotal = float(product['price'])
                detail_sale.save()
                if status_replication:
                    detail_sale.save(using='mirror_database')
            data['success'] = str(sale.id)
        except Exception as e:
            data['error'] = str(e)
        return data
    
    # función que valida la cantidad de productos en la tienda
    def validate_update_stock_product(self, request):
        data = {}
        product_id = int(request.POST['product'])
        stock = Stock.objects.get(product=product_id)
        stock_by_size = StockProductSize.objects.filter(stock=stock)
        for st_size in stock_by_size:
            if st_size.size.size_product == request.POST['size']:
                if st_size.amount - int(request.POST['ammount']) > 0:
                    data['success'] = ''
                else:
                    data['error'] = 'No hay suficiente stock'
        return data
    
    # función que nos valida si no existen pagos que no se han cumplido
    def validate_non_paid_invoices(self):
        data = {}
        try:
            unpaid_invoices = Sale.objects.filter(user=self.request.user, is_completed=False)
            if len(unpaid_invoices) > 0:
                data['error'] = 'No puede comprar más productos ya que tiene cargos pendientes'
            else:
                data['success'] = ''
        except Exception as e:
            data['error'] = str(e)
        return data

    
    
    # función que procesa el pago con stripe
    def process_data_payment(self, request, sale_id):
        data = {}
        try:
            stripe.api_key = STRIPE_SECRET_KEY
            DOMAIN_PAGE = "http://127.0.0.1:8000"
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                customer_email = self.request.user.email,
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price_data': {
                            'currency' : 'MXN',
                            'unit_amount' : int(float(request.POST['total'])*100),
                            'product_data': {
                                'name' : f'Pago de productos usuario: {self.request.user.username}'
                            }
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url= DOMAIN_PAGE + reverse_lazy('shop:success'),
                cancel_url= DOMAIN_PAGE + reverse_lazy('shop:cancel'),
                payment_intent_data={
                    'metadata' : {'order_id' : sale_id}
                }
            )
            print(checkout_session)
            data['id'] = checkout_session.id
        except Exception as e:
            data['error'] = str(e)
        return data

    # sobrescritura del método post para la obtención y guardado de datos
    def post(self, request, *args, **kwargs):
        data = {}
        match request.POST['action']:
            # caso de obtención de los colores del producto
            case 'obtain':
                id_prod = int(request.POST['data'])
                product_return = Product.objects.get(id=id_prod)
                data['color1'] = product_return.primary_color
                data['color2'] = product_return.secondary_color
                data['color3'] = product_return.last_color
            # caso donde se valida la edición del producto (cantidad)
            case 'validate':
                data = self.validate_update_stock_product(request)
            # caso donde retorna el nombre del producto y su imagen
            case 'image':
                id_prod = int(request.POST['data'])
                product_return = Product.objects.get(id=id_prod)
                data['image'] = product_return.get_image()
                data['name'] = product_return.name
            # caso donde se prevalida la cantidad total de productos a comprar
            # además de si existen facturas pendientes por pagar
            case 'validate_buy':
                data = self.validate_non_paid_invoices()
                if 'success' in data:
                    products = json.loads(request.POST['products'])
                    if len(products) > 0:
                        data = self.return_status_stock(request, products)
                    else:
                        data['error'] = 'No hay productos por comprar'
            # caso de checkout donde se realiza la compra de los productos
            case 'checkout':
                data_products = {}
                with transaction.atomic():
                    data_products = self.do_the_purchase(request)
                    if 'success' in data_products:
                        print(data_products['success'])
                        data = self.process_data_payment(request, data_products['success'])
                        print(data)
                        if 'error' in data:
                            rollback_data(1)
                    else:
                        rollback_data(1)
                        data['error'] = 'error'

                
        # retorno de la información como JSON al front-end
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Carrito de compra"
        context["image"] = "img/shop-cart.png"
        context['color'] = self.get_number_color()
        context['directions'] = DirectionUser.objects.filter(
            user=self.request.user)
        context['public_stripe'] = STRIPE_PUBLIC_KEY
        return context
